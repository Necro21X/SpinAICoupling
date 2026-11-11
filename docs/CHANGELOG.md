# Changelog

## 2026-11-11

### Added
- Project planning boilerplates in `docs/planning/` (plan, milestones, task backlog) and a project plan image.
- FastAPI app `app.py` serving the chat page at `/` and static files under `/static`.
- Plain HTML/CSS/JS chat frontend in `frontend/` (input field, send button, chat log).
- `POST /chat` endpoint that forwards the user message to an OpenAI-compatible model API and returns `{"response": "..."}`.
- Frontend sends messages to `/chat` and shows the answer in the chat log.
- `backend/helper_functions/containers.py` with a placeholder `ChatMessageRequest` class.
- GitHub workflows for Claude PR assistant, Claude code review and the docs agent.
- `DOCS_GUIDE.md` instructions for the docs agent.

### Changed
- Project plan and milestones were revised.
- Backend scaffolding reshuffled: `backend/main.py` reduced, empty `backend/chatbot.py` and `backend/helper_functions/helper.py` added.
- Docs agent workflow credentials were updated.

### Removed
- Initial `test.py` file.
