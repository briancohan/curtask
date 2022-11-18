import os
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

APP_FOLDER = Path(__file__).absolute().parent
TASK_FILE = APP_FOLDER / "task.txt"
INTERVAL = os.environ.get("INTERVAL", "5s")

app = FastAPI(title="PBD Tools API")
app.mount("/static", StaticFiles(directory=f"{APP_FOLDER}/static"), name="static")
templates = Jinja2Templates(directory=f"{APP_FOLDER}/templates")


@app.get("/")
async def index(request: Request) -> Jinja2Templates.TemplateResponse:
    task = TASK_FILE.read_text()
    return templates.TemplateResponse(
        "index.html", {"request": request, "task": task, "interval": INTERVAL}
    )


@app.get("/get")
async def get_task(request: Request) -> Jinja2Templates.TemplateResponse:
    task = TASK_FILE.read_text()
    return templates.TemplateResponse(
        "components/display_card.html",
        {"request": request, "task": task, "interval": INTERVAL},
    )


@app.get("/set")
async def task_form(request: Request) -> Jinja2Templates.TemplateResponse:
    task = TASK_FILE.read_text()
    return templates.TemplateResponse(
        "components/form_card.html", {"request": request, "task": task}
    )


@app.post("/set")
async def set_task(
    request: Request, task: str = Form()
) -> Jinja2Templates.TemplateResponse:
    TASK_FILE.write_text(task)
    return templates.TemplateResponse(
        "components/display_card.html",
        {"request": request, "task": task, "interval": INTERVAL},
    )