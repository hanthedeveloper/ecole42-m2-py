# Garden Guardian - Module 02

Each exercise is a small program that handles errors without crashing:
`try`, `except`, `raise`, `finally`, built-in exceptions and custom
exception classes.

## Exercises

| Ex | File | What it does |
|----|------|--------------|
| 0 | `ft_first_exception.py` | Converts a string to a temperature with `int()` and catches the error on invalid input |
| 1 | `ft_raise_exception.py` | Raises a `ValueError` when the temperature is outside 0-40°C |
| 2 | `ft_different_errors.py` | Triggers `ValueError`, `ZeroDivisionError`, `FileNotFoundError` and `TypeError`, each caught separately |
| 3 | `ft_custom_errors.py` | Custom `GardenError`, `PlantError` and `WaterError` with default messages |
| 4 | `ft_finally_block.py` | Waters plants, raises `PlantError` on a non-capitalized name, always closes the system in `finally` |

## Requirements

- Python 3.10+
- `flake8` and `mypy` (for linting and type checking)

## Usage

Each exercise lives in its own directory (`ex0/` to `ex4/`) and has its own
`if __name__ == "__main__":` block, so every file can be run directly:

```bash
cd ex0
python3 ft_first_exception.py
```

The same applies to the other exercises, for example:

```bash
cd ex4
python3 ft_finally_block.py
```

## Checks

```bash
flake8 .
mypy --strict ft_*.py
```

Note: `mypy` reports an error in `ft_different_errors.py` on the line that
adds a string and an integer. This is intentional, it is the faulty code
that must raise the `TypeError`.
