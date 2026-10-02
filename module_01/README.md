# Code Cultivation - Module 01

Each exercise builds a piece of a digital garden, going from a simple script
to a small object-oriented system: `if __name__ == "__main__"`, classes,
constructors, encapsulation, inheritance, static and class methods,
and nested classes.

## Exercises

| Ex | File | What it does |
|----|------|--------------|
| 0 | `ft_garden_intro.py` | Prints a plant's name, height and age using variables |
| 1 | `ft_garden_data.py` | `Plant` class with attributes and a `show()` method, registry of 3 plants |
| 2 | `ft_plant_growth.py` | Adds `grow()` and `age()` methods, simulates one week of growth |
| 3 | `ft_plant_factory.py` | Uses `__init__` to create plants with initial values (5 plants) |
| 4 | `ft_garden_security.py` | Encapsulation: protected attributes, getters and validated setters |
| 5 | `ft_plant_types.py` | Inheritance: `Flower`, `Tree` and `Vegetable` built on `Plant` with `super()` |
| 6 | `ft_garden_analytics.py` | Static method, class method, `Seed` class, nested stats class and `show_statistics()` |

## Requirements

- Python 3.10+
- `flake8` and `mypy` (for linting and type checking)

## Usage

Each exercise lives in its own directory (`ex0/` to `ex6/`) and has its own
`if __name__ == "__main__":` block, so every file can be run directly:

```bash
cd ex0
python3 ft_garden_intro.py
```

The same applies to the other exercises, for example:

```bash
cd ex6
python3 ft_garden_analytics.py
```

Since the test code is under the `__main__` guard, the classes can also be
imported from another file without printing anything.

## Checks

```bash
flake8 .
mypy --strict ft_*.py
```
