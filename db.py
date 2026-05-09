import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "data", "hackkit.db")

def get_connection():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    _init_tables(conn)
    return conn

def _init_tables(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            members TEXT DEFAULT '',
            project_title TEXT DEFAULT ''
        );
        CREATE TABLE IF NOT EXISTS judges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL DEFAULT 0.0
        );
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judge_id INTEGER NOT NULL,
            team_id INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            value INTEGER NOT NULL DEFAULT 0,
            FOREIGN KEY (judge_id) REFERENCES judges(id),
            FOREIGN KEY (team_id) REFERENCES teams(id),
            FOREIGN KEY (category_id) REFERENCES categories(id),
            UNIQUE(judge_id, team_id, category_id)
        );
        CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            team_id INTEGER NOT NULL,
            time_slot TEXT DEFAULT '',
            room TEXT DEFAULT '',
            FOREIGN KEY (team_id) REFERENCES teams(id)
        );
    """)
    conn.commit()

def add_team(name, members="", project_title=""):
    conn = get_connection()
    cur = conn.execute("INSERT INTO teams (name, members, project_title) VALUES (?, ?, ?)", (name, members, project_title))
    conn.commit()
    tid = cur.lastrowid
    conn.close()
    return tid

def get_teams():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM teams ORDER BY id").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def delete_team(team_id):
    conn = get_connection()
    conn.execute("DELETE FROM scores WHERE team_id = ?", (team_id,))
    conn.execute("DELETE FROM schedule WHERE team_id = ?", (team_id,))
    conn.execute("DELETE FROM teams WHERE id = ?", (team_id,))
    conn.commit()
    conn.close()

def add_judge(name):
    conn = get_connection()
    cur = conn.execute("INSERT INTO judges (name) VALUES (?)", (name,))
    conn.commit()
    jid = cur.lastrowid
    conn.close()
    return jid

def get_judges():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM judges ORDER BY id").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def delete_judge(judge_id):
    conn = get_connection()
    conn.execute("DELETE FROM scores WHERE judge_id = ?", (judge_id,))
    conn.execute("DELETE FROM judges WHERE id = ?", (judge_id,))
    conn.commit()
    conn.close()

def add_category(name, weight):
    conn = get_connection()
    cur = conn.execute("INSERT INTO categories (name, weight) VALUES (?, ?)", (name, weight))
    conn.commit()
    cid = cur.lastrowid
    conn.close()
    return cid

def get_categories():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM categories ORDER BY id").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def delete_category(cat_id):
    conn = get_connection()
    conn.execute("DELETE FROM scores WHERE category_id = ?", (cat_id,))
    conn.execute("DELETE FROM categories WHERE id = ?", (cat_id,))
    conn.commit()
    conn.close()

def upsert_score(judge_id, team_id, category_id, value):
    conn = get_connection()
    conn.execute("""INSERT INTO scores (judge_id, team_id, category_id, value)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(judge_id, team_id, category_id)
        DO UPDATE SET value = excluded.value""", (judge_id, team_id, category_id, value))
    conn.commit()
    conn.close()

def get_scores():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM scores").fetchall()
    conn.close()
    return [dict(r) for r in rows]

def upsert_schedule(team_id, time_slot, room):
    conn = get_connection()
    existing = conn.execute("SELECT id FROM schedule WHERE team_id = ?", (team_id,)).fetchone()
    if existing:
        conn.execute("UPDATE schedule SET time_slot = ?, room = ? WHERE team_id = ?", (time_slot, room, team_id))
    else:
        conn.execute("INSERT INTO schedule (team_id, time_slot, room) VALUES (?, ?, ?)", (team_id, time_slot, room))
    conn.commit()
    conn.close()

def get_schedule():
    conn = get_connection()
    rows = conn.execute("SELECT s.*, t.name as team_name FROM schedule s JOIN teams t ON s.team_id = t.id ORDER BY s.time_slot").fetchall()
    conn.close()
    return [dict(r) for r in rows]
