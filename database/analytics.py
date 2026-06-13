import sqlite3
from contextlib import closing

from config import Config

DB_NAME = Config.ANALYTICS_DB

METRICS = [
    "uploads",
    "chats",
    "quizzes",
    "flashcards",
    "notes",
    "assessments",
    "roadmaps",
    "weak_topics",
    "agent_calls"
]


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_analytics():
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS analytics (
            key TEXT PRIMARY KEY,
            value INTEGER
        )
        """)

        for metric in METRICS:
            cursor.execute("""
            INSERT OR IGNORE INTO analytics
            (key, value)
            VALUES (?, ?)
            """, (
                metric,
                0
            ))

        conn.commit()


def increment(metric):
    if metric not in METRICS:
        return

    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE analytics
        SET value = value + 1
        WHERE key = ?
        """, (metric,))

        conn.commit()


def get_analytics():
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT key, value
        FROM analytics
        """)

        rows = cursor.fetchall()

        return {
            key: value
            for key, value in rows
        }


def reset_analytics():
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE analytics
        SET value = 0
        """)

        conn.commit()