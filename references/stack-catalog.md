# Stack catalog — objective → recommended stack

Data file. Used in Step 2 to pick a stack automatically for beginner/intermediate
users. **Edit freely** to add objectives or change recommendations — adding a row
here is how you teach the skill a new kind of project.

Pick the row that best matches the user's stated objective. When in doubt, prefer
the most beginner-friendly, well-documented option in the row. Always pair the
chosen stack with its architecture from `architecture-catalog.md`.

| Objective (what the user wants) | Recommended stack | Notes |
|---|---|---|
| Website / web app with UI | Next.js (React + TypeScript) | SSR + routing built in; huge ecosystem. |
| Simple static / content site | Astro or plain HTML+CSS+JS | Least moving parts for a beginner. |
| REST/JSON API or backend service | FastAPI (Python) or NestJS (TypeScript) | FastAPI = gentle; Nest = structured TS. |
| Full-stack app (UI + API + DB) | Next.js + a DB (Postgres) via Prisma | One language (TS) end to end. |
| Mobile app (iOS + Android) | Flutter (Dart) | Single codebase, strong tooling. |
| CLI tool / automation script | Python (Typer) or Node (Commander) | Keep it tiny; no heavy layers. |
| Data / analysis / ML prototype | Python (pandas / scikit-learn / notebooks) | Pipeline-style, not app-style. |
| Desktop app | Tauri (web UI + Rust) or Electron | Tauri = lighter; Electron = familiar. |
| Realtime app (chat, live updates) | Next.js + WebSocket layer | See architecture catalog for the realtime layer. |
| Discord/Telegram bot | Python (discord.py / aiogram) or Node | Small service architecture. |

## How to choose when the objective is vague

1. Ask one clarifying question in the user's language (e.g. "is this something
   people open in a browser, install on a phone, or run in a terminal?").
2. Default to the most common, best-documented option so a beginner can find help.
3. Never pick something exotic for a beginner just because it's technically nicer.

## Selection rules by experience level

- **beginner** → choose one row, state it in a single simple sentence, proceed.
- **intermediate** → propose the row + one-line rationale; allow override.
- **advanced** → don't use this catalog; let the user choose.
