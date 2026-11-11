# Architecture

## Overview
A FastAPI backend serves a plain HTML/CSS/JS chat page and forwards chat messages to an OpenAI-compatible model API.

Data flow: browser (`frontend/js/script.js`) → `POST /chat` → `app.py` → model API (`AsyncOpenAI`, Responses API) → `{"response": "..."}` → appended to the chat log.

## Components
- `app.py`: FastAPI app. Loads env via `python-dotenv`.
  - `GET /`: returns `frontend/index.html`.
  - `/static`: serves the `frontend/` directory (CSS, JS).
  - `POST /chat`: body `{"message": str}`; creates an `AsyncOpenAI` client, calls `responses.create` with model `qwen3.5-9b` (hardcoded) and returns `{"response": output_text}`. No history, streaming or error handling yet.
- `frontend/`: `index.html`, `css/style.css`, `js/script.js`. The form submit handler shows the user message, POSTs it to `/chat` and shows the reply.
- `backend/`: scaffolding only. `helper_functions/containers.py` holds a placeholder `ChatMessageRequest`; `chatbot.py`, `main.py` and `helper_functions/helper.py` are empty or near-empty and unused.

## Configuration (env variables, names only)
- `OPENAI_API_KEY`: API key for the model provider.
- `API_URL`: base URL of the OpenAI-compatible API.

Set in a `.env` file (not committed).

## CI
- `.github/workflows/claude.yml`, `claude-code-review.yml`: Claude PR assistant and review.
- `.github/workflows/docs-agent.yml`: docs agent that updates `docs/` using `DOCS_GUIDE.md`. Uses the secret `CLAUDE_CODE_OAUTH_TOKEN`.

## Running
Install `fastapi`, `uvicorn`, `openai`, `pydantic`, `python-dotenv` (no requirements file yet), create `.env`, then run `uvicorn app:app --reload` and open `http://localhost:8000/`.
