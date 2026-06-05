# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

## [0.3.0] — 2026-06-05
### Added
- Update flow (`/claude-for-idiots update`, `references/update-flow.md`):
  updates the skill install (git pull or fresh download) and brings
  already-configured projects up to date — refreshes hooks, merges new rules
  into `CLAUDE.md`, adds new config fields — while preserving every onboarding
  choice and verified project fact. Summarizes what changed (from this
  changelog, in the user's language) before touching anything.
- `VERSION` file at the repo root; setup now records `skill_version` in each
  project's config so updates know where the project is starting from.

## [0.2.1] — 2026-06-05
### Fixed
- Setup must now **verify** facts (paths, ports, commands) against the real
  project before writing them into `CLAUDE.md`/config — never from memory.
  Found in field testing: the database path was written as `prisma/dev.db`
  while the file actually lived at the project root. Facts about artifacts that
  don't exist yet are re-checked during the first sanity check.
- Generated `CLAUDE.md` now states that its facts are documentation, not law:
  Claude must fix them immediately when they turn out wrong (only the rules
  need the user's consent to change). Prevents the model from refusing to
  correct its own instructions file.

## [0.2.0] — 2026-06-05
### Added
- Portuguese README (`README.pt-br.md`) with a language switcher in both READMEs.
- Quality-tooling catalog (`references/quality-tools.md`) — setup now installs
  the stack's formatter/linter/type-checker by default (Python default: ruff,
  with pylint as a documented alternative).
- Rule 7 (reuse before you build) and Rule 8 (hard-won knowledge lives in
  `docs/`, three context layers: always loaded / on demand / discovered live).
- `docs/` scaffolding templates: `assets/docs-INDEX.template.md` and
  `assets/ADR.template.md`.
- Rule 9 (debugging escalation): after two failed fixes for the same problem,
  stop guessing — re-read the full error, check versions, research the web
  deeply, then retry with a genuinely new hypothesis.
- Browser-verification guide (`references/browser-verification.md`): web smoke
  tests read the browser console via Playwright MCP when available, degrade
  gracefully when not; setup offers to configure it (never installs unasked).
- Hook test suite (`tests/test_hooks.py`, 16 cases, stdlib only) covering
  block / allow / fail-open for all three hooks.
- GitHub Actions CI (`.github/workflows/ci.yml`): compiles hooks and runs the
  test suite on every push and pull request.

### Fixed
- Removed the non-standard `"//"` comment key from `assets/settings.template.json`
  (the merge instructions live in SKILL.md Step 3).

### Changed
- README rewritten for non-technical readers: plain-language intro, the original
  motivation, how to use, and what it improves.
- Skill is now explicit-invocation first (`/claude-for-idiots`); its description
  no longer aims to auto-apply to every new project.
- READMEs: new "Should you use it on your project?" section (sweet spot vs
  over-engineering), setup-time note (~10 minutes measured on Opus 4.8),
  auto-mode recommendation for beginners during setup, and a
  not-yet-tested-for-deployment disclaimer.

## [0.1.0] — initial skeleton
### Added
- `SKILL.md` — onboarding flow, stack/architecture derivation, rules, term modes.
- Six rules in `references/rules.md` (1, 5, 6 are hook-enforced).
- Editable data catalogs: `stack-catalog.md`, `architecture-catalog.md`.
- `onboarding-flow.md` and `glossary-format.md` (progressive-teaching glossary).
- Generated-project assets: `CLAUDE.template.md`, `config.example.json`,
  `settings.template.json`.
- Three `PreToolUse` hooks: block migration edits (Rule 1), enforce architecture
  (Rule 5), scan secrets before publishing (Rule 6).
- `README.md` and `CONTRIBUTING.md`.

### Notes
- Term modes: `none` / `explain` / `raw`.
- Experience levels: `beginner` / `intermediate` / `advanced` drive defaults.
- Hooks fail open: no `.claude-for-idiots/config.json` → no interference.
