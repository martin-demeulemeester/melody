from pathlib import Path

DIR_PATH = BASE_DIR = Path(__file__).resolve().parents[2]
BACK_PATH = DIR_PATH / "backend"
DATA_PATH = DIR_PATH / "data"
DB_PATH = DATA_PATH / "app.db"