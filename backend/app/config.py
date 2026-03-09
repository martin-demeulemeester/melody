from pathlib import Path

DIR_PATH = Path.cwd().parent.parent
BACK_PATH = DIR_PATH / "backend"
DATA_PATH = BACK_PATH / "data"
DB_PATH = DATA_PATH / "app.db"