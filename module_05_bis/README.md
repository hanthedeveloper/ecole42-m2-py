# The Codex - Module 05-bis

Packages, environments and the alchemist's toolchain. The first two exercises
set up the working environment (virtual environment, dependencies, secrets
and configuration). The last three grow a single Python package, `alchemy`,
and cover every import mechanism: `__init__.py`, absolute and relative
imports, and circular dependencies.

## Exercises

| Ex | Files | What it does |
|----|-------|--------------|
| 0 | `construct.py`, `loading.py`, `requirements.txt`, `pyproject.toml` | `construct.py` detects whether it runs inside a virtual environment, displays information about the current Python and gives the instructions to create and activate one if none is found. `loading.py` declares `pandas` and `numpy` for pip (`requirements.txt`) and Poetry (`pyproject.toml`), imports each one, reports its version and prints an install message instead of crashing when one is missing |
| 1 | `oracle.py`, `.env.example`, `.gitignore`, `requirements.txt` | Loads the configuration (`MATRIX_MODE`, `DATABASE_URL`, `API_KEY`, `LOG_LEVEL`, `ZION_ENDPOINT`) from environment variables and a `.env` file with `python-dotenv`. Behaves differently in development and production, warns about missing values without crashing, and lets real environment variables override the `.env` file |
| 2 | `elements.py`, `alchemy/__init__.py`, `alchemy/elements.py`, `ft_alembic_0.py`, `ft_alembic_1.py` | Elements spread between the root and the package. `ft_alembic_0.py` uses `import ...` to reach the root `elements.py`. `ft_alembic_1.py` uses `import alchemy`: `create_air()` is exposed by `__init__.py`, `create_earth()` is not and raises an `AttributeError` |
| 3 | `alchemy/potions.py`, `alchemy/transmutation/`, `ft_distillation_0.py`, `ft_transmutation_0.py` | Nested imports. `potions.py` brews the healing and strength potions from the four elements (two of them live outside the package). `transmutation/recipes.py` uses both an absolute and a relative import to build `lead_to_gold()`. Tested with `from ... import ...` and `import ...` |
| 4 | `alchemy/grimoire/`, `ft_kaboom_0.py`, `ft_kaboom_1.py` | Circular dependencies. The light spellbook and validator need each other but are written so the cycle is avoided and the spell is recorded. The dark pair imports each other at the top of both files and genuinely fails with an `ImportError` |

## Requirements

- Python 3.10+
- `flake8` and `mypy` (for linting and type checking)
- Exercises 0 and 1 use external libraries: `pandas`, `numpy`, `python-dotenv`
  and Poetry. Exercises 2 to 4 only import the modules created in the project

## Structure

Exercises 0 and 1 are self-contained in their folder. Exercises 2, 3 and 4
build one package tree at the root of the module, each one adding to the
previous one.

```
.
├── ex0/
│   ├── construct.py
│   ├── loading.py
│   ├── pyproject.toml
│   └── requirements.txt
├── ex1/
│   ├── .env.example
│   ├── .gitignore
│   ├── oracle.py
│   └── requirements.txt
├── alchemy/
│   ├── __init__.py
│   ├── elements.py
│   ├── potions.py
│   ├── transmutation/
│   │   ├── __init__.py
│   │   └── recipes.py
│   └── grimoire/
│       ├── __init__.py
│       ├── dark_spellbook.py
│       ├── dark_validator.py
│       ├── light_spellbook.py
│       └── light_validator.py
├── elements.py
├── ft_alembic_0.py
├── ft_alembic_1.py
├── ft_distillation_0.py
├── ft_transmutation_0.py
├── ft_kaboom_0.py
└── ft_kaboom_1.py
```

## Usage

Exercise 0, part 1 works both outside and inside a virtual environment, and
the output is different in each case. The virtual environment must not be
committed:

```bash
python3 ex0/construct.py

python3 -m venv lab_env
source lab_env/bin/activate
python3 ex0/construct.py
```

Exercise 0, part 2 lists the installed versions of the reagents, or the
install commands for pip and Poetry when one is missing:

```bash
python3 ex0/loading.py

pip install -r ex0/requirements.txt
python3 ex0/loading.py

cd ex0
poetry install
poetry run python loading.py
```

Exercise 1 reads its configuration from `ex1/.env` (copied from
`.env.example`, never committed). The variables of the real environment take
priority over the `.env` file:

```bash
python3 ex1/oracle.py

cp ex1/.env.example ex1/.env
python3 ex1/oracle.py

MATRIX_MODE=production API_KEY=secret123 python3 ex1/oracle.py
```

Exercises 2 to 4 are run from the module folder, next to the `alchemy`
package. Two of the scripts fail on purpose: `ft_alembic_1.py` raises an
`AttributeError` and `ft_kaboom_1.py` raises an `ImportError` (circular
import):

```bash
python3 ft_alembic_0.py
python3 ft_alembic_1.py

python3 ft_distillation_0.py
python3 ft_transmutation_0.py

python3 ft_kaboom_0.py
python3 ft_kaboom_1.py
```

## Checks

From inside the module folder:

```bash
flake8 .
mypy --strict ex0/*.py ex1/*.py ft_*.py
```

Some `mypy` errors are expected on purpose: `ft_alembic_1.py` calls a
function that the package does not expose, and `ft_kaboom_1.py` imports the
broken dark grimoire.
