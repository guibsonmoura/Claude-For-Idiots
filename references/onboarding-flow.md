# Onboarding flow

Run this only when `.claude-for-idiots/config.json` does **not** exist. Ask in
the user's language, keep it short, and let the experience level pre-fill later
answers so a beginner answers as little as possible.

## Q0 — Interaction language
"What language should I talk to you in?" → store as `language` (e.g. `en`, `pt-BR`).
Default `en`. The skill's own files always stay in English.

## Q1 — Experience level  → `experience_level`
`beginner` | `intermediate` | `advanced`. **This drives the defaults below.**

- `beginner` — never assume knowledge; explain decisions in one plain sentence;
  default term mode `explain`; Claude picks stack & architecture.
- `intermediate` — proposes choices with short rationale; default term mode
  `raw` (or `explain` if they want to learn); can override stack/architecture.
- `advanced` — user drives stack & architecture; default term mode `raw`;
  minimal hand-holding.

## Q2 — Use of technical terms  → `term_mode`
"Should I use technical terms?" → `none` | `explain` | `raw`.

- `none` — never use jargon; always paraphrase.
- `explain` — use the term + a short explanation right after; ramp difficulty up
  as the user learns; **creates the glossary**.
- `raw` — use terms normally, no explanations.

Default from Q1, but always confirm with the user.

## Q3 — Project objective  → `objective`
"What do you want to build?" Free text. Used with `stack-catalog.md` to pick a
stack for non-advanced users. Ask one clarifying question if it's vague.

## Q4 — Stack & architecture  → `stack`, `architecture`
- `advanced` → ask the user directly.
- `beginner` / `intermediate` → derive from objective (Step 2 of SKILL.md).
  Beginner: state and proceed. Intermediate: propose and allow override.

## Q5 — Version control  → `git`
Auto-detect first: is there a `.git`? a remote (`git remote -v`)?
- Repo present → record it; commits/feature apply (Rule 3).
- No repo + beginner → offer to set up Git and **explain what Git is in plain
  language** before doing it. Never push/publish without confirmation (Rule 6).

## Q6 — Tests  → `tests.enabled`
On by default. If a beginner asks to disable, first explain why tests matter,
then respect the choice and record it.

## Q7 — Browser verification (web projects only)
Auto-detect: are browser-automation tools available (e.g. Playwright MCP,
`mcp__playwright__*`)? If yes, just record it. If not, **offer** to set it up —
for a beginner, in plain language: "a tool that lets me see your site like you
do, including hidden errors". Never install without asking. See
`references/browser-verification.md`.

---

After collecting answers, do Step 3 of SKILL.md (write the artifacts) and
confirm the setup to the user in their language.
