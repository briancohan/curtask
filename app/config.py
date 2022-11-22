import os
from pathlib import Path


class Config:
    APP_FOLDER = Path(__file__).absolute().parent
    STATIC_DIR = f"{APP_FOLDER}/static"
    TEMPLATE_DIR = f"{APP_FOLDER}/templates"
    DATA_DIR = Path("/data")
    DATA_FILE = DATA_DIR / "tasks.json"
    INTERVAL = os.environ.get("INTERVAL", "5")
