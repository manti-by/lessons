from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy_utils import create_database, database_exists

DB_PATH = Path(__file__).resolve().parent / "db.sqlite3"
DB_ECHO = True


def setup_db_engine() -> Engine:
    return create_engine(f"sqlite:////{DB_PATH}", echo=DB_ECHO)


def create_database_if_not_exists(engine: Engine) -> bool:
    if not database_exists(engine.url):
        create_database(engine.url)
        return True
    return False
