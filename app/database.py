import sqlite3
from app.core.constants import DB_PATH


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # DICT
    return conn
