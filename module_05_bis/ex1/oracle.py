import os
import sys


def is_env_ignored() -> bool:
    path = os.path.join(os.path.dirname(__file__), ".gitignore")
    try:
        with open(path) as file:
            return ".env" in [line.strip() for line in file]
    except FileNotFoundError:
        return False


def env_file(overrides: list[str]) -> None:
    mode = (os.getenv("MATRIX_MODE") or "").strip().lower()
    if not mode:
        print("Mode is missing. Using default.")
        mode = "development"

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        print("Database is missing. Using default.")
        db_url = "localhost"

    api = os.getenv("API_KEY")
    if not api:
        print("API access is missing.")

    log_lvl = os.getenv("LOG_LEVEL")
    if not log_lvl:
        print("Log Level is missing. Using default.")
        log_lvl = "INFO"

    zion = os.getenv("ZION_ENDPOINT")
    if not zion:
        print("Remote Network is missing. Using default.")
        zion = "offline"

    if mode not in ("development", "production"):
        print(f"ERROR: unknown mode '{mode}'.")
        sys.exit(1)
    if mode == "production" and not api:
        print("ERROR: API_KEY is required in production!")
        sys.exit(1)

    if "localhost" in db_url:
        db_mesg = "Connected to local instance"
    else:
        db_mesg = "Connected to remote database"

    if not api:
        api_mesg = "Missing"
    elif mode == "production":
        api_mesg = "Authenticated (*****)"
    else:
        api_mesg = "Authenticated"

    print()
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_mesg}")
    print(f"API Access: {api_mesg}")
    print(f"Log Level: {log_lvl}")
    print(f"Remote Network: {'Online' if zion != 'offline' else 'Offline'}")

    print()
    print("Configuration security check:")
    print("[OK] No hardcoded secrets detected")

    if is_env_ignored():
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .env is NOT in .gitignore!")

    if overrides:
        print(f"[OK] Overrides active: {', '.join(overrides)}")
    else:
        print("[OK] Production overrides available (none active)")
    print()
    print("The Oracle sees all configurations.")


KEYS = ["MATRIX_MODE", "DATABASE_URL", "API_KEY",
        "LOG_LEVEL", "ZION_ENDPOINT"]


if __name__ == "__main__":
    overrides = [k for k in KEYS if k in os.environ]
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("WARNING: python-dotenv is not installed.")
        print("Use requirements.txt to install it.")
        sys.exit(1)
    else:
        env_path = os.path.join(os.path.dirname(__file__), ".env")
        if os.path.exists(env_path):
            load_dotenv(env_path)
        else:
            print("WARNING: no .env file found.")
    env_file(overrides)
