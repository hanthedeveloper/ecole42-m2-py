import importlib

if __name__ == "__main__":
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")

    missing = []

    try:
        module = importlib.import_module("pandas")
    except ImportError:
        print(f"[MISSING] pandas")
        missing.append("pandas")
    else:
        print(f"[OK] pandas ({module.__version__}) - Data manipulation ready")
    try:
        module = importlib.import_module("numpy")
    except ImportError:
        print(f"[MISSING] numpy")
        missing.append("numpy")
    else:
        print(f"[OK] numpy ({module.__version__}) - Numerical computation ready")

    if missing:
        print()
        print("Some reagents are missing. Install them with:")
        print("pip install -r ex0/requirements.txt")
        print("poetry install")
    else:
        print()
        print("pip vs Poetry:")
        print("  requirements.txt declares what to install; "
              "pip resolves it at install time.")
        print("  pyproject.toml declares the same constraints, and Poetry "
              "pins the resolved")
        print("  versions in poetry.lock so every install is identical.")
        print()
        print("All reagents present and accounted for.")