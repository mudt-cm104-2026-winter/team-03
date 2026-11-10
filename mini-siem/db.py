"""SQLite storage. Owner: TC (feature/storage)."""
import sqlite3

DB_PATH = "siem.db"  # listed in .gitignore, never commit it


def _connect():
    return sqlite3.connect(DB_PATH)


def init_db():
    with _connect() as conn:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS entries ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT, "
            "timestamp TEXT NOT NULL, ip TEXT NOT NULL, "
            "event TEXT NOT NULL, user TEXT NOT NULL)"
        )


def save_entries(entries):
    """Save a list of parsed entries. Placeholders (?) only: log data is untrusted."""
    with _connect() as conn:
        conn.executemany(
            "INSERT INTO entries (timestamp, ip, event, user) VALUES (?, ?, ?, ?)",
            [(e["timestamp"], e["ip"], e["event"], e["user"]) for e in entries],
        )


def get_entries():
    with _connect() as conn:
        rows = conn.execute(
            "SELECT timestamp, ip, event, user FROM entries ORDER BY id"
        ).fetchall()
    return [{"timestamp": t, "ip": i, "event": e, "user": u} for t, i, e, u in rows]
