import os
import sys


def env_file() -> int:
    mode = os.getenv("MATRIX_MODE", "development")
    database = os.getenv("DATABASE_URL", "sqlite:///local.db")
    api_key = os.getenv("API_KEY", "")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    zion = os.getenv("ZION_ENDPOINT", "http://localhost:8080")

    if os.getenv("MATRIX_MODE") is None:
        print("WARNING: MATRIX_MODE missing, using default")
    if os.getenv("DATABASE_URL") is None:
        print("WARNING: DATABASE_URL missing, using default")
    if not api_key:
        print("WARNING: API_KEY missing")
    if os.getenv("LOG_LEVEL") is None:
        print("WARNING: LOG_LEVEL missing, using default")
    if os.getenv("ZION_ENDPOINT") is None:
        print("WARNING: ZION_ENDPOINT missing, using default")

    if mode == "production" and not api_key:
        print("ERROR: API_KEY is required in production.")
        return 1

    shown_key = api_key if mode == "development" else "****"

    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database}")
    print(f"API Access: {shown_key or '(not set)'}")
    print(f"Log Level: {log_level}")
    print(f"Remote Network: {zion}")
    return 0


def is_env_ignored:
    


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("WARNING: python-dotenv is not installed.")
    else:
        if not load_dotenv():
            print("WARNING: no .env file found.")
        print("ORACLE STATUS: Consulting the configuration...")
        print()
        env_file()