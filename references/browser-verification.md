# Browser verification — seeing what the user sees

For web projects, Rule 4's smoke test gets much stronger when Claude can drive a
real browser: load the page, read the **browser console**, take a screenshot.
A `curl` can never do this — it doesn't execute JavaScript, so console errors
are invisible to it.

## Detection

At setup (and before each web smoke test), check whether browser-automation
tools are available — e.g. the Playwright MCP server (`mcp__playwright__*`
tools such as `browser_navigate`, `browser_console_messages`,
`browser_take_screenshot`).

## If available

Web smoke test =
1. boot the app,
2. navigate to the affected page,
3. read the console messages — **fail the check on console errors**,
4. screenshot when the UI changed (show it to the user).

## If NOT available — degrade gracefully

- `curl` the page/endpoints (status codes, server-rendered HTML, API errors),
- read the server logs,
- ask the user to open the page and paste anything red from the console — for
  beginners, explain how in plain language: press `F12`, click "Console".

## Offering it (web projects, during onboarding)

If the project is a web app and no browser automation is available, **offer** to
set it up. For a beginner, say it plainly: *"I can install a tool that lets me
see your site exactly like you do — including hidden errors. Want that?"* Then:

```bash
claude mcp add playwright -- npx @playwright/mcp@latest
```

(Needs Node; the user restarts Claude Code afterwards.) **Never install without
asking** — it downloads a whole browser.
