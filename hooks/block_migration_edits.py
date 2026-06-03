#!/usr/bin/env python3
"""Rule 1 — never hand-edit migration files.

PreToolUse hook (matcher: Edit|Write|MultiEdit). Reads the per-project
.claude-for-idiots/config.json to learn which paths are protected and which
migration command to use instead. Fails open (allows) when there is no config
or no migrations section, so it never interferes with unrelated projects.
"""
import fnmatch
import json
import os
import sys

CONFIG_REL = os.path.join(".claude-for-idiots", "config.json")


def load_config(cwd):
    try:
        with open(os.path.join(cwd, CONFIG_REL)) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return None


def deny(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    sys.exit(0)


def main():
    try:
        event = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)  # fail open

    tool_input = event.get("tool_input") or {}
    file_path = tool_input.get("file_path") or ""
    if not file_path:
        sys.exit(0)

    cwd = event.get("cwd") or os.getcwd()
    config = load_config(cwd)
    if not config:
        sys.exit(0)

    migrations = config.get("migrations") or {}
    protected = migrations.get("protected_paths") or []
    if not protected:
        sys.exit(0)

    rel = os.path.relpath(file_path, cwd) if os.path.isabs(file_path) else file_path
    rel = rel.replace(os.sep, "/")

    for pattern in protected:
        if fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(file_path, pattern):
            tool = migrations.get("tool", "your migration tool")
            cmd = migrations.get("command", f"{tool} autogenerate")
            deny(
                "BLOCKED by claude-for-idiots Rule 1: migration files are "
                "generated, never hand-edited. "
                f"'{rel}' matches a protected migration path.\n"
                f"Change the models/schema and run: {cmd}\n"
                "Explain this to the user in their language before retrying."
            )

    sys.exit(0)


if __name__ == "__main__":
    main()
