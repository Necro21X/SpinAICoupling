import numpy
from pathlib import Path
from fastapi import FastAPI # type: ignore
from fastapi.responses import FileResponse # type: ignore
from fastapi.staticfiles import StaticFiles # type: ignore

app = FastAPI()

# Folder containing the front page files (index.html, style.css, script.js)
FRONTEND_DIR = Path(__file__).parent / "frontend"

# Serve the CSS and JS files under /static
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

# Front page: returns the HTML file with the chat field and button
@app.get("/")
async def root():
    return FileResponse(FRONTEND_DIR / "index.html")