from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="src/mom_project/static"), name="static")

@app.get('/', response_class=HTMLResponse)
def home():
    html_path = Path("src/mom_project/static/index.html")
    return HTMLResponse(html_path.read_text(encoding='utf-8'))


