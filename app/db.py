from pathlib import Path


class TextDB:
    def __init__(self, db_file: Path) -> None:
        if not db_file.exists():
            db_file.write_text("Define a task.")
        self.db_file = db_file

    def set_current_task(self, task: str) -> None:
        self.db_file.write_text(task)

    def get_current_task(self) -> str:
        return self.db_file.read_text()
