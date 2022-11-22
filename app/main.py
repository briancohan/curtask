from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .config import Config
from .db import db_from_file

app = FastAPI()
app.mount("/static", StaticFiles(directory=Config.STATIC_DIR), name="static")
templates = Jinja2Templates(directory=Config.TEMPLATE_DIR)
db = db_from_file(Config.DATA_FILE)


@app.get("/")
async def index(request: Request) -> Jinja2Templates.TemplateResponse:

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "task": db.get_current_task(),
            "interval": Config.INTERVAL,
        },
    )


@app.get("/get")
async def get_task(request: Request) -> Jinja2Templates.TemplateResponse:
    return templates.TemplateResponse(
        "components/display_card.html",
        {
            "request": request,
            "task": db.get_current_task(),
            "interval": Config.INTERVAL,
        },
    )


@app.get("/set")
async def task_form(request: Request) -> Jinja2Templates.TemplateResponse:
    return templates.TemplateResponse(
        "components/form_card.html",
        {"request": request, "task": db.get_current_task()},
    )


@app.post("/set")
async def set_task(
    request: Request, task: str = Form()
) -> Jinja2Templates.TemplateResponse:
    db.set_current_task(task)
    return templates.TemplateResponse(
        "components/display_card.html",
        {"request": request, "task": task, "interval": Config.INTERVAL},
    )
