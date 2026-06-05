# Contributing to claude-for-idiots

Forks, issues, and pull requests are welcome and encouraged. This project is
**built to be extended** — most contributions are edits to a single data file,
not changes to the skill's logic.

## Philosophy (read this first)

- **Data over prose.** Stacks, architectures, and rule text live as data in
  `references/`. The skill (`SKILL.md`) reads them. Prefer adding a row to a
  catalog over editing the skill's instructions.
- **Idiomatic, not dogmatic.** Never push one architecture (MVVM, Clean, …) onto
  a stack where it fights the framework. Architecture = `f(stack, objective, scale)`.
- **Beginner-safe by default.** A change must not make the beginner path scarier
  or jargon-heavier. The `none` term mode must always have a real paraphrase.
- **Fail open.** Hooks must never block a project that doesn't use this skill.
  No config → allow.

## How to make common contributions

### Add a stack (new kind of project)
1. Add a row to `references/stack-catalog.md` (objective → stack).
2. Add the matching idiomatic layout to `references/architecture-catalog.md`,
   including a suggested `allowed_paths` and `layers`.
3. If it uses migrations, note the tool + protected paths.

### Add / change an architecture
Edit `references/architecture-catalog.md`. Keep the layout minimal and idiomatic;
include `allowed_paths` (globs) and a one-line responsibility per layer.

### Change a rule
Edit `references/rules.md` (the source of truth) **and**
`assets/CLAUDE.template.md` (the generated copy). Keep numbering stable.

### Add a new guardrail (hook)
1. Add a script in `hooks/` following the existing pattern:
   - read the event JSON from **stdin**,
   - read `.claude-for-idiots/config.json` for its settings,
   - **fail open** (exit 0, no output) when not applicable,
   - to block, print the `hookSpecificOutput` JSON with `permissionDecision`
     `"deny"` or `"ask"` and a clear, actionable reason.
2. Wire it in `assets/settings.template.json` under the right `matcher`.
3. Add its config keys to `assets/config.example.json`.

## Testing your changes

Run the hook test suite (standard library only — also runs in CI on every PR):

```bash
python3 -m py_compile hooks/*.py   # must pass
python3 tests/test_hooks.py        # must pass
```

Add a test case in `tests/test_hooks.py` whenever you add or change hook
behavior. Every hook must keep covering the three contract scenarios:
**should block**, **should allow**, and **no config → allow** (fail open).

For quick manual poking, hooks are plain scripts that read one JSON event on
stdin:

```bash
echo '{"cwd":".","tool_name":"Edit","tool_input":{"file_path":"alembic/versions/x.py"}}' \
  | python3 hooks/block_migration_edits.py   # prints a deny (with config present)
```

## Pull request checklist

- [ ] `python3 -m py_compile hooks/*.py` and `python3 tests/test_hooks.py` pass.
- [ ] New/changed hook behavior comes with a test case in `tests/test_hooks.py`.
- [ ] New stack/architecture rows include `allowed_paths` and layer responsibilities.
- [ ] Rule changes are mirrored in `references/rules.md` and `assets/CLAUDE.template.md`.
- [ ] Hooks still fail open with no config.
- [ ] `CHANGELOG.md` updated under "Unreleased".
- [ ] Beginner path is no scarier than before.

## Reporting issues

Open an issue describing: your objective, the stack/architecture chosen, the
experience level, and what Claude did vs. what you expected. Redact any secrets.

Thanks for helping keep Claude on the rails for everyone. 🚲
