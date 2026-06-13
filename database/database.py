import sqlite3
from contextlib import closing

from config import Config

DB_NAME = Config.DB_NAME


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            ai_response TEXT NOT NULL,
            agent_used TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()


def save_chat(
    user_message,
    ai_response,
    agent_used="pipeline"
):
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO chats (
            user_message,
            ai_response,
            agent_used
        )
        VALUES (?, ?, ?)
        """, (
            user_message,
            ai_response,
            agent_used
        ))

        conn.commit()


def get_chats(limit=100):
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT
            id,
            user_message,
            ai_response,
            agent_used,
            created_at
        FROM chats
        ORDER BY id DESC
        LIMIT ?
        """, (limit,))

        return cursor.fetchall()


def clear_chats():
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM chats"
        )

        conn.commit()


def get_chat_count():
    with closing(get_connection()) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM chats"
        )

        return cursor.fetchone()[0]