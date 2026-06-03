# Rules — single source of truth

These are the engineering rules `claude-for-idiots` enforces. The generated
`CLAUDE.md` copies this text (adapted to the chosen stack). Edit here first.

Rules marked **[hook]** are also enforced technically by a script in `hooks/`,
so they are guarantees, not just promises.

---

## Rule 1 — Never hand-edit migration files **[hook]**

Migration files are *generated artifacts*. Never open or edit a file under the
migrations directory directly.

To change the database schema:
1. Change the models / schema definition.
2. Run the library's generator, e.g.:
   - Alembic: `alembic revision --autogenerate -m "describe change"`
   - Prisma: `prisma migrate dev --name describe_change`
   - Django: `python manage.py makemigrations`
3. Review the generated file (reading is fine; editing it by hand is not).

The protected paths and the exact command live in
`.claude-for-idiots/config.json` under `migrations`.

## Rule 2 — Always have tests

Unit **and** integration tests, on both frontend and backend, are on by default.

- During a feature, run only the **relevant** tests — fast feedback.
- **Ask the user for permission before running the full suite** (it is slow/costly).
- A beginner may disable tests, but only after Claude explains *why they matter*
  (they catch breakage before the user does, and make changes safe).

## Rule 3 — Commit per feature

If a version control system exists, commit after each working feature with a
clear message, so progress is never lost. Detect version control automatically;
don't force it on a user who didn't ask, but offer it to beginners (and explain
what Git is, in plain language, first).

## Rule 4 — Sanity check after each feature

After implementing a feature, verify you didn't break anything:
1. Lint + type-check.
2. Run the feature's own tests.
3. Smoke test: boot the app and confirm it starts and the feature responds.

(A successful smoke test implies a successful build.)

## Rule 5 — Keep new files inside the chosen architecture **[hook]**

Every new code file must land in the layer/folder defined by the project's
architecture (recorded in `CLAUDE.md` and `config.json` → `architecture`).
If a deliberate architectural change is needed, update the architecture in both
files first, then create the file.

## Rule 6 — Secrets never reach the remote **[hook]**

API keys, tokens, passwords, private keys → always in a **gitignored `.env`**,
with a committed **`.env.example`** documenting the variable names (no values).

Local Git is free (init, commit, branch). Any **publishing** action — `git push`,
creating a remote repo, making a repo public, opening a PR — must:
1. be explicitly confirmed by the user, and
2. pass a secret scan first.

The worst possible accident for a beginner is publishing a public repo with a
live API key inside. This rule exists to make that impossible.
