from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

static_dir = Path(__file__).parent / "static" 
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

@app.get('/', response_class=HTMLResponse)
def home():
    html_path = static_dir / 'html' / 'index.html'
    return HTMLResponse(html_path.read_text(encoding='utf-8'))



