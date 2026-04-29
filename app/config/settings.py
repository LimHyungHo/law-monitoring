import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_ENV_PATH = BASE_DIR / ".env"
LOCAL_ENV_PATH = BASE_DIR / ".env.local"
DEFAULT_DATA_DIR = Path(os.getenv("RAW_MONITOR_DATA_DIR", "/tmp/law-monitoring-data")).expanduser()

load_dotenv(DEFAULT_ENV_PATH)
load_dotenv(LOCAL_ENV_PATH, override=True)

class Settings:
    LAW_API_KEY = os.getenv("LAW_API_KEY")
    ENV_PATH = str(DEFAULT_ENV_PATH)
    DATA_DIR = str(DEFAULT_DATA_DIR)
    DB_PATH = os.getenv(
        "DB_PATH",
        str(DEFAULT_DATA_DIR / "law_monitor.db")
    )
    PDF_OUTPUT_DIR = os.getenv(
        "PDF_OUTPUT_DIR",
        str(DEFAULT_DATA_DIR / "pdf")
    )
    LAW_ID_CACHE_PATH = os.getenv(
        "LAW_ID_CACHE_PATH",
        str(DEFAULT_DATA_DIR / "cache" / "law_ids.json")
    )
    SECRET_KEY = os.getenv("SECRET_KEY", "law-monitoring-dev-secret")
    WEB_HOST = os.getenv("WEB_HOST", "0.0.0.0")
    WEB_PORT = int(os.getenv("WEB_PORT", 5000))
    WEB_DEBUG = os.getenv("WEB_DEBUG", "false").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE_PATH = os.getenv("LOG_FILE_PATH")

    MAIL_HOST = os.getenv("MAIL_HOST", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 465))
    MAIL_USER = os.getenv("MAIL_USER")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_TO = os.getenv("MAIL_TO")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")

settings = Settings()
