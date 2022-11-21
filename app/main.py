import os
from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .db import JsonDB

APP_FOLDER = Path(__file__).absolute().parent
INTERVAL = os.environ.get("INTERVAL", "5")
DB = JsonDB(APP_FOLDER / "tasks.json")


app = FastAPI()
app.mount("/static", StaticFiles(directory=f"{APP_FOLDER}/static"), name="static")
templates = Jinja2Templates(directory=f"{APP_FOLDER}/templates")


@app.get("/")
async def index(request: Request) -> Jinja2Templates.TemplateResponse:

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "task": DB.get_current_task(), "interval": INTERVAL},
    )


@app.get("/get")
async def get_task(request: Request) -> Jinja2Templates.TemplateResponse:
    return templates.TemplateResponse(
        "components/display_card.html",
        {"request": request, "task": DB.get_current_task(), "interval": INTERVAL},
    )


@app.get("/set")
async def task_form(request: Request) -> Jinja2Templates.TemplateResponse:
    return templates.TemplateResponse(
        "components/form_card.html", {"request": request, "task": DB.get_current_task()}
    )


@app.post("/set")
async def set_task(
    request: Request, task: str = Form()
) -> Jinja2Templates.TemplateResponse:
    DB.set_current_task(task)
    return templates.TemplateResponse(
        "components/display_card.html",
        {"request": request, "task": task, "interval": INTERVAL},
    )
