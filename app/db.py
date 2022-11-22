import json
from datetime import datetime
from pathlib import Path

NO_TASK = "Define your first task."


class BaseDB:
    def __init__(self, db_file: Path) -> None:
        if not db_file.exists():
            db_file.touch()
        self.db_file = db_file


class TextDB(BaseDB):
    def set_current_task(self, task: str) -> None:
        self.db_file.write_text(task)

    def get_current_task(self) -> str:
        task = self.db_file.read_text()
        if not task:
            return NO_TASK
        return task


class JsonDB(BaseDB):
    def _read_data(self) -> list[dict[str, str]]:
        with self.db_file.open() as fp:
            try:
                data = json.load(fp)
            except json.JSONDecodeError:
                data = []
        return data

    def set_current_task(self, task: str) -> None:
        data = self._read_data()

        if task == self.get_current_task(data=data):
            return

        now = datetime.now()
        data.append({"timestamp": now.isoformat(), "task": task})
        with self.db_file.open("w") as fp:
            json.dump(data, fp)

    def get_current_task(self, data: list[dict[str, str]] | None = None) -> str:
        if data is None:
            data = self._read_data()
        try:
            return data[-1]["task"]
        except IndexError:
            return NO_TASK


def db_from_file(db_file: Path) -> TextDB | JsonDB:
    if db_file.suffix == ".json":
        return JsonDB(db_file=db_file)
    else:
        return TextDB(db_file=db_file)
