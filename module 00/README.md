# Growing Code

Each exercise is a small function that reads input and prints a result:
`print`, `input`, `int`, conditions, loops, recursion and type hints.

## Exercises

| Ex | File | What it does |
|----|------|--------------|
| 0 | `ft_hello_garden.py` | Prints a welcome message |
| 1 | `ft_garden_name.py` | Asks for a garden name and prints it |
| 2 | `ft_plot_area.py` | Computes the area of a rectangular plot |
| 3 | `ft_harvest_total.py` | Sums the harvest of three days |
| 4 | `ft_plant_age.py` | Tells if a plant is ready to harvest |
| 5 | `ft_water_reminder.py` | Tells if the plants need water |
| 6 | `ft_count_harvest_iterative.py` | Counts days to harvest with a loop |
| 6 | `ft_count_harvest_recursive.py` | Same output, using recursion |
| 7 | `ft_seed_inventory.py` | Prints seed info by unit |

## Requirements

- Python 3.10+
- `flake8` and `mypy` (for linting and type checking)

## Usage

Put `main.py` and the exercise files in the same folder, then run:

```bash
python3 main.py
```

Choose an exercise from the menu (`0`-`7`), or `a` to test all of them.

Each file contains only its function, so it is meant to be imported, not run
directly.

## Checks

```bash
flake8 .
mypy --strict ft_*.py
```
