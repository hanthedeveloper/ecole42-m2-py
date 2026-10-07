# Data Quest - Module 03

Each exercise is a small script that works with one Python collection type
while processing game data: lists, tuples, sets, dictionaries, generators and
comprehensions.

## Exercises

| Ex | File | What it does |
|----|------|--------------|
| 0 | `ft_command_quest.py` | Displays the program name and the command-line arguments from `sys.argv` (a list), with the number of arguments received |
| 1 | `ft_score_analytics.py` | Takes scores as arguments, discards invalid (non-numeric) ones with a message and stores the rest in a list. Prints the number of players, total, average, high, low and range |
| 2 | `ft_coordinate_system.py` | `get_player_pos()` asks for `x,y,z` coordinates, retries on invalid input and returns a tuple. Displays the tuple and its values, the distance to the center and the distance between two sets of coordinates |
| 3 | `ft_achievement_tracker.py` | `gen_player_achievements()` randomly builds a set of achievements for a player. Uses set operations (union, intersection, difference) to show all distinct, common, unique and missing achievements of four players |
| 4 | `ft_inventory_system.py` | Parses `<item>:<quantity>` arguments into a dictionary, discarding invalid and redundant ones. Prints the item list, total, percentages, most and least abundant items, then adds a new item |
| 5 | `ft_data_stream.py` | Endless generator `gen_event()` yields `(player, action)` tuples. Displays 1000 events, builds a list of 10 events, then `consume_event()` yields and removes them randomly until the list is empty |
| 6 | `ft_data_alchemist.py` | Uses list and dict comprehensions to capitalize names, keep only capitalized ones, build a score dictionary and filter the scores above the average |

## Requirements

- Python 3.10+
- `flake8` and `mypy` (for linting and type checking)

## Usage

Each exercise lives in its own directory (`ex0/` to `ex6/`) and is a plain
script, there is no `main` function.

Exercise 0 prints the program name and its arguments:

```bash
cd ex0
python3 ft_command_quest.py
python3 ft_command_quest.py hello world 42
python3 ft_command_quest.py "Data Quest"
```

Exercise 1 takes the scores as arguments. Invalid values are discarded, and a
usage message is printed if no valid score remains:

```bash
cd ex1
python3 ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ft_score_analytics.py
python3 ft_score_analytics.py ab ac
```

Exercise 2 takes no argument, it asks for the coordinates on the standard
input in the format `x,y,z` and asks again until they are valid:

```bash
cd ex2
python3 ft_coordinate_system.py
```

Exercise 3 takes no argument. The achievements are random, so the output is
different at each run:

```bash
cd ex3
python3 ft_achievement_tracker.py
```

Exercise 4 takes the inventory as `<item_name>:<quantity>` arguments:

```bash
cd ex4
python3 ft_inventory_system.py sword:1 potion:5 shield:2 armor:3 helmet:1 sword:2 hello key:value
```

Exercises 5 and 6 take no argument and also give a different output at each
run. Exercise 5 prints 1000 events, so piping the output can be useful:

```bash
cd ex5
python3 ft_data_stream.py | less

cd ../ex6
python3 ft_data_alchemist.py
```

## Checks

From inside the module folder:

```bash
flake8 .
mypy --strict ex*/ft_*.py
```
