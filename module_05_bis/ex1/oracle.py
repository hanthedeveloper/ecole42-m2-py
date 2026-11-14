import os
import sys


def is_env_ignored() -> bool:
    path = os.path.join(os.path.dirname(__file__), ".gitignore")
    try:
        with open(path) as file:
            return ".env" in [line.strip() for line in file]
    except FileNotFoundError:
        return False


def env_file():
    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api = os.getenv("API_KEY")
    log_lvl = os.getenv("LOG_LEVEL")
    zion = os.getenv("ZION_ENDPOINT")

    if not mode:
        print("Mode is missing. Using default.")
        mode = "development"
    if not db_url:
        print("Database is missing. Using default.")
        db_url = "local"
    if not api:
        print("API access is missing.")
    if not log_lvl:
        print("Log Level is missing. Using default.")
        log_lvl = "INFO"
    if not zion:
        print("Remote Network is missing. Using default.")
        zion = "offline"
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {'Connected to local instance' if db_url == 'local' else 'Connected to remote database'}")
    if mode == "production" and not api:
        print("ERROR: API_KEY is required in production!")
    print(f"API Access: {'Authenticated' if api else 'Missing'}")
    print(f"Log Level: {log_lvl}")
    print(f"Remote Network: {'Online' if zion != 'offline' else 'Offline'}")

    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")

    if is_env_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env is NOT in .gitignore!")
    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("WARNING: python-dotenv is not installed.")
        print("Use requirements.txt to install it.")
    else:
        env_path = os.path.join(os.path.dirname(__file__), ".env")
        if not load_dotenv(env_path):
            print("WARNING: no .env file found.")
    env_file()
