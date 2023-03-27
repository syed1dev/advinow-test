import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


def get_env(variable_name, default=None):
    value = os.getenv(variable_name, default)
    if value and str(value).lower() in ("true", "false"):
        return str(value).lower() == "true"
    return value


# Postgres
# DB_HOST = get_env("DB_HOST", "localhost")
# DB_NAME = get_env("DB_NAME", "postgres")
# DB_USER = get_env("DB_USER", "postgres")
# DB_PASSWORD = get_env("DB_PWD", "password")

# DB_URL: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"



BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.sqlite3"
DB_URL = f"sqlite:///{DB_PATH}"