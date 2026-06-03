# Changelog

All notable changes to this project are documented here.
Format based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

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
