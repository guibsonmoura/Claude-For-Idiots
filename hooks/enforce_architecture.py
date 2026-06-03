#!/usr/bin/env python3
"""Rule 5 — new code stays inside the chosen architecture.

PreToolUse hook (matcher: Write). Checks NEW code files against the project's
allowed_paths from .claude-for-idiots/config.json. The `architecture.enforce`
mode can be "deny", "ask" or "off". Only polices code-file creation; ignores
docs/config and files that already exist (those are edits, not placements).
Fails open when not configured.
"""
import fnmatch
import json
import os
import sys

CONFIG_REL = os.path.join(".claude-for-idiots", "config.json")

CODE_EXT = {
    ".py", ".js", ".ts", ".jsx", ".tsx", ".go", ".rs", ".java", ".kt",
    ".rb", ".php", ".dart", ".vue", ".svelte", ".cs", ".swift", ".scala",
}


def load_config(cwd):
    try:
        with open(os.path.join(cwd, CONFIG_REL)) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None


def main():
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)

    tool_input = event.get("tool_input") or {}
    file_path = tool_input.get("file_path") or ""
    if not file_path:
        sys.exit(0)

    cwd = event.get("cwd") or os.getcwd()
    config = load_config(cwd)
    if not config:
        sys.exit(0)

    arch = config.get("architecture") or {}
    mode = arch.get("enforce", "off")
    allowed = arch.get("allowed_paths") or []
    if mode == "off" or not allowed:
        sys.exit(0)

    # Only police new code files. Let docs/config and edits-to-existing through.
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in CODE_EXT:
        sys.exit(0)
    if os.path.exists(file_path):
        sys.exit(0)

    rel = os.path.relpath(file_path, cwd) if os.path.isabs(file_path) else file_path
    rel = rel.replace(os.sep, "/")

    if any(fnmatch.fnmatch(rel, p) for p in allowed):
        sys.exit(0)

    layers = arch.get("layers") or {}
    layer_hint = "\n".join(f"    {k}: {v}" for k, v in layers.items()) or "    (see CLAUDE.md)"
    reason = (
        f"claude-for-idiots Rule 5: '{rel}' is outside the chosen architecture "
        f"({arch.get('name', 'project architecture')}).\n"
        f"Allowed locations: {', '.join(allowed)}\n"
        f"Layers:\n{layer_hint}\n"
        "Place the file in the correct layer, or update `architecture` in "
        ".claude-for-idiots/config.json + CLAUDE.md if this is a deliberate change."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny" if mode == "deny" else "ask",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


if __name__ == "__main__":
    main()
