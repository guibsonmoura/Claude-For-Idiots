# Glossary format (term mode = `explain` only)

The glossary turns the `explain` mode into *progressive teaching*: it remembers
which terms were already explained and at what depth, plus a running estimate of
the user's level — so explanations get more advanced over time and don't repeat
needlessly.

Stored at `<project>/.claude-for-idiots/glossary.json`.

```json
{
  "user_level": "beginner",
  "terms": {
    "websocket": {
      "depth": "basic",
      "last_explanation": "a way for the app and server to talk in real time without reloading the page",
      "seen_count": 1
    },
    "cors": {
      "depth": "intermediate",
      "last_explanation": "the browser rule that blocks requests from one site to another unless allowed",
      "seen_count": 3
    }
  }
}
```

## How Claude uses it

1. About to use a technical term? Look it up.
2. **Not in glossary** → explain at the user's current `user_level`, then add an
   entry with `depth` and `seen_count: 1`.
3. **Already in glossary** → don't re-explain from scratch. Either use it bare,
   or give a slightly deeper nuance than last time. Increment `seen_count`.
4. As the user demonstrates understanding (asks advanced questions, uses terms
   correctly), bump `user_level` and let future explanations start deeper.

## Fields

| Field | Meaning |
|---|---|
| `user_level` | `beginner` \| `intermediate` \| `advanced` — global teaching level. |
| `terms.<term>.depth` | How deep the last explanation went. |
| `terms.<term>.last_explanation` | The phrasing used last, to stay consistent and build on it. |
| `terms.<term>.seen_count` | How many times the term has come up. |

Keep terms lowercase and singular as keys. This file is only created/maintained
when `term_mode` is `explain`.
