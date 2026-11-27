# Cosmic Data - Module 09

Each exercise is a small program that validates data with Pydantic.
The type hints become real validation rules: field constraints with `Field`,
enums, nested models and cross-field checks with `model_validator`.
Validation errors are caught with `ValidationError` and printed without
crashing the program.

## Exercises

| Ex | File | What it does |
|----|------|--------------|
| 0 | `space_station.py` | `SpaceStation` model with `Field` constraints (length, `ge`/`le`, default values, optional `notes`). Creates a valid station, then a station with an invalid `crew_size` and prints the validation error |
| 1 | `alien_contact.py` | `AlienContact` model with a `ContactType` enum and a `model_validator(mode="after")` that checks several fields together (ID prefix `AC`, physical contact must be verified, telepathic contact needs 3+ witnesses, strong signals need a message) |
| 2 | `space_crew.py` | `SpaceMission` model with a nested list of `CrewMember` models and a `Rank` enum. The validator checks the mission ID, that all crew are active, the experience ratio on long missions and that there is a Commander or Captain |

## Requirements

- Python 3.10+
- `pydantic` (v2)
- `flake8` and `mypy` (for linting and type checking)

```bash
pip install pydantic flake8 mypy
```

## Usage

Each exercise lives in its own directory (`ex0/` to `ex2/`) and is a plain
script. Each one prints a valid object first, then an expected validation
error:

```bash
cd ex0
python3 space_station.py
```

```bash
cd ex1
python3 alien_contact.py
```

```bash
cd ex2
python3 space_crew.py
```

## Test data

The `data_generator/` folder contains the provided generator and exporter
for the Cosmic Data Observatory. The files in `data_generator/generated_data/`
(`.json`, `.csv` and `.py`) hold many station, contact and mission records,
including invalid ones, and can be used to test the models on more cases than
the ones in the `main()` functions.

## Checks

```bash
flake8 .
mypy --strict ex*/*.py
```

Note: validators in `mode="after"` run once Pydantic has already parsed and
validated every field, so they work on correctly typed values and must
return `self`.
