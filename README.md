# claude-for-idiots

A [Claude Code](https://claude.com/claude-code) skill that keeps Claude **on the
rails** — for total beginners and experienced developers alike.

It runs a short onboarding, picks (or lets you pick) a stack and an *idiomatic*
architecture, and then writes persistent guardrails into your project so Claude
follows solid engineering rules in **every** session — not just while the skill
is loaded.

> 🇧🇷 A Portuguese README is coming. The skill itself is in English so it works
> for everyone; it can *talk to you* in any language you choose during setup.

## What it enforces

1. **Never hand-edit migrations** — uses the library's generator (Alembic, Prisma, …). *Hook-enforced.*
2. **Always tests** — unit + integration, front + back. Asks before the full suite.
3. **Commit per feature** — never lose progress (when a repo exists).
4. **Sanity check after each feature** — lint + type-check → tests → smoke test.
5. **New files stay inside the chosen architecture.** *Hook-enforced.*
6. **Secrets never reach the remote** — `.env` only; publishing is confirmed and secret-scanned. *Hook-enforced.*

## Adapts to you

During onboarding you set your **experience level** (beginner / intermediate /
advanced) and your **use of technical terms**:

- `none` — no jargon ever; everything paraphrased in plain language.
- `explain` — uses terms + short explanations that ramp up as you learn (with a glossary).
- `raw` — terms as usual, no explanations.

## Install

This is a **user-level** skill — install it once and it works in every project.

```bash
git clone https://github.com/JulioBarbosaS/Claude-For-Idiots.git
cp -r Claude-For-Idiots ~/.claude/skills/claude-for-idiots
```

Then, in any project, ask Claude to start a guided setup (or just say you're
starting a new project) and the skill takes over. It will write `CLAUDE.md`,
`.claude-for-idiots/config.json`, and the hooks into that project.

> Hooks require `python3` on your PATH.

## Repository layout

```
SKILL.md                     # the skill's brain (onboarding + behavior)
references/                  # editable data — extend the skill here
  rules.md                   #   the 6 rules (source of truth)
  stack-catalog.md           #   objective → stack
  architecture-catalog.md    #   stack → idiomatic architecture
  onboarding-flow.md         #   the questions
  glossary-format.md         #   how the "explain" glossary works
assets/                      # what gets written into your project
  CLAUDE.template.md
  config.example.json
  settings.template.json
hooks/                       # the technical guardrails (Python)
  block_migration_edits.py   #   Rule 1
  enforce_architecture.py    #   Rule 5
  scan_secrets_before_push.py#   Rule 6
```

## Contributing

Forks, issues, and PRs are welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). The
whole thing is designed to be extended: adding a stack or architecture is editing
one data file, not rewriting the skill.

## License

[MIT](LICENSE) © 2026 Julio Barbosa — permissive and fork-friendly.
