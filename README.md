# 42 Python Modules

This repository contains all the exercises of the 10 Python modules of
Milestone 2 of the 42 common core. Each module has its own folder, and each
exercise lives in its own `exN/` directory inside it.

## Modules

| Module | Folder | Topic |
|--------|--------|-------|
| 00 | `module00/` | Growing Code: `print`, `input`, conditions, loops, recursion, type hints |
| 01 | `module01/` | Code Cultivation: classes, encapsulation, inheritance, static and class methods |
| 02 | `module02/` | Garden Guardian: `try`, `except`, `raise`, `finally`, custom exceptions |
| 03 | `module03/` | Data Quest: lists, tuples, sets, dictionaries, generators, comprehensions, `sys.argv` |
| 04 | `module04/` | Data Archivist: `open`, `read`, `write`, `sys.stdin`, `sys.stdout`, `sys.stderr`, `with` (context managers) |
| 05 | `module05/` | TODO |
| 06 | `module06/` | TODO |
| 07 | `module07/` | TODO |
| 08 | `module08/` | TODO |
| 09 | `module09/` | TODO |
| 10 | `module10/` | TODO |

Each module folder has its own `README.md` with the list of exercises.

## Structure

```
.
├── module00/
│   ├── README.md
│   ├── ex0/
|   ├── ex1/
|   ├── ex2/
│   └── ...
├── module01/
|   ├── README.md
│   ├── ex0/
│   └── ...
└── ...
```

## Requirements

- Python 3.10+
- `flake8` and `mypy`

## Checks

From inside a module folder:

```bash
flake8 .
mypy --strict ex*/ft_*.py
```
