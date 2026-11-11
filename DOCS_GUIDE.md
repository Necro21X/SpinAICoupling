# Documentation Guide (for the docs agent)

This file tells the automated docs agent how to document SpinAICoupling.
Humans can edit it to change how the docs are written.

## Project context
SpinAICoupling is an AI assistant prototype by Denis & Elias: a FastAPI
backend (`app.py`, `backend/`) that forwards chat messages to an
OpenAI-compatible model API, plus a plain HTML/CSS/JS chat frontend
(`frontend/`). Planning lives in `docs/planning/`.

## Files you maintain
| File | Purpose | How to update |
|------|---------|---------------|
| `docs/CHANGELOG.md` | What changed, newest first | Add a section `## YYYY-MM-DD` (date of the newest commit in the range) with `### Added / Changed / Fixed / Removed`. One human-readable line per item. Do not copy commit messages verbatim. |
| `docs/DEVLOG.md` | Narrative progress log | Add one entry per run, newest first: `## YYYY-MM-DD`, then 3–6 sentences on what was worked on, by whom (commit author), and what the apparent goal was. |
| `docs/ARCHITECTURE.md` | How the system is built right now | Describe components, endpoints, data flow (frontend → `/chat` → model API), config/env variables (names only, never values) and how to run it. Only update sections affected by the changes; never rewrite the whole file. |
| `docs/decisions/NNNN-short-title.md` | Architecture decision records | Create one only for real decisions: new dependency/framework, new model or API provider, changed data model, changed project structure. Sections: Context / Decision / Consequences. Number sequentially. |
| `docs/.last-documented` | SHA of the last documented commit | Overwrite with the SHA given in the prompt. |

## Planning files (`docs/planning/`)
These are written by humans. You may read them for context.
You may ONLY change the `Status` column in `TASK_BACKLOG.md` and
`MILESTONES.md`, and only when a commit clearly completes or starts a task
(e.g. a working `/chat` endpoint → "Endpoint for Chatting with Models" →
`In Progress` or `Done`). Mention every status change in the DEVLOG entry.
Never change any other content in `docs/planning/`.

## Rules
- Language: English.
- Commit messages are often short or unclear (e.g. "1"). In that case
  derive what happened from the diff. Never invent motivations: if the
  reason for a change is not visible, write "reason not stated".
- Skip trivial changes (formatting, whitespace, typo fixes, `.gitignore`
  tweaks) unless they matter to someone using the project.
- Never write secrets, API keys or the contents of `.env` into the docs.
- Keep entries short and concrete. Name files and endpoints in `code`.
- If a file does not exist yet, create it with a `# Title` heading.
- On the first run (full history), write one CHANGELOG and DEVLOG section
  per day that had commits, and write ARCHITECTURE.md from the current code.
