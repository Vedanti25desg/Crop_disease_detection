"""SQLite helper that stores every prediction for the History page."""
import os, sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "history.db")


def _conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with _conn() as c:
        c.execute("""CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image TEXT NOT NULL, original_name TEXT,
            disease_key TEXT NOT NULL, confidence REAL NOT NULL, created_at TEXT NOT NULL)""")
        cols = {r["name"] for r in c.execute("PRAGMA table_info(predictions)")}
        for col, ddl in (("part", "TEXT DEFAULT 'leaf'"), ("part_confidence", "REAL"), ("note", "TEXT")):
            if col not in cols:                      # upgrades an older history.db automatically
                c.execute(f"ALTER TABLE predictions ADD COLUMN {col} {ddl}")


def add_record(image, original_name, disease_key, confidence, part="leaf", part_confidence=None, note=None):
    with _conn() as c:
        cur = c.execute(
            "INSERT INTO predictions (image, original_name, disease_key, confidence, created_at, part, part_confidence, note) "
            "VALUES (?,?,?,?,?,?,?,?)",
            (image, original_name, disease_key, confidence,
             datetime.now().strftime("%d %b %Y, %I:%M %p"), part, part_confidence, note))
        return cur.lastrowid


def get_record(rid):
    if rid is None:
        return None
    with _conn() as c:
        return c.execute("SELECT * FROM predictions WHERE id=?", (rid,)).fetchone()


def list_records(limit=50):
    with _conn() as c:
        return c.execute("SELECT * FROM predictions ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
