import os
from pathlib import Path
from fastapi import FastAPI # type: ignore
from fastapi.responses import FileResponse # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore
from openai import AsyncOpenAI # type: ignore
from pydantic import BaseModel # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
API_URL = os.getenv("API_URL")

app = FastAPI()

# Folder containing the front page files (index.html, style.css, script.js)
FRONTEND_DIR = Path(__file__).parent / "frontend"

# Serve the CSS and JS files under /static
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Front page: returns the HTML file with the chat field and button
@app.get("/")
async def root():
    return FileResponse(FRONTEND_DIR / "index.html")

# Expected JSON body of a chat request: {"message": "..."}
class ChatRequest(BaseModel):
    message: str

# Chat endpoint: receives the user message via POST and returns the model answer
@app.post("/chat")
async def start_connection(request: ChatRequest):
    # Async client, so that the call can be awaited without blocking the server
    client = AsyncOpenAI(api_key=OPENAI_API_KEY, base_url=API_URL)

    response = await client.responses.create(model="qwen3.5-9b", input=request.message)

    return {"response": response.output_text}