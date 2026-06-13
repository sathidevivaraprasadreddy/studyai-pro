import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "change-this-secret-key"
    )

    GEMINI_API_KEY = os.getenv(
        "GEMINI_API_KEY"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ).lower() == "true"

    HOST = os.getenv(
        "HOST",
        "0.0.0.0"
    )

    PORT = int(
        os.getenv(
            "PORT",
            5000
        )
    )

    UPLOAD_FOLDER = os.getenv(
        "UPLOAD_FOLDER",
        "uploads"
    )

    MAX_CONTENT_LENGTH = int(
        os.getenv(
            "MAX_CONTENT_LENGTH",
            52428800
        )
    )

    DB_NAME = os.getenv(
        "DB_NAME",
        "studyai.db"
    )

    ANALYTICS_DB = os.getenv(
        "ANALYTICS_DB",
        "analytics.db"
    )

    VECTOR_DIR = os.getenv(
        "VECTOR_DIR",
        "vector_db"
    )