import os
import sqlite3
from pathlib import Path

from app.config.settings import settings


def get_connection():
    db_path = settings.DB_PATH
    db_dir = os.path.dirname(db_path)

    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    _initialize_schema_if_needed(conn)

    return conn


def _initialize_schema_if_needed(conn):
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'users'"
    )
    if cursor.fetchone():
        return

    schema_path = Path(__file__).resolve().parents[2] / "db" / "sqlite_schema.sql"
    with open(schema_path, "r", encoding="utf-8") as schema_file:
        conn.executescript(schema_file.read())
    conn.commit()
