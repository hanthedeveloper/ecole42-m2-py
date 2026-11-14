# Code Nexus - Module 06-bis

Abstract architecture, from data streams to battle strategies. The first
three exercises build a data pipeline on top of abstract classes and
polymorphism. The last two use the same ideas on a combat sandbox, with the
abstract factory, capability and abstract strategy design patterns.

## Exercises

| Ex | Files | What it does |
|----|-------|--------------|
| 0 | `data_processor.py` | Abstract class `DataProcessor` (`ABC`) with the abstract methods `validate` and `ingest` and the standard method `output`. `NumericProcessor`, `TextProcessor` and `LogProcessor` override them for their own data types and store the ingested items one by one. Ingesting invalid data without validation raises an exception |
| 1 | `data_stream.py` | `DataStream` registers processors with `register_processor()`, routes each element of a mixed list to the first processor that can handle it with `process_stream()` (an error message is printed if none can) and shows the totals and remaining items with `print_processors_stats()` |
| 2 | `data_pipeline.py` | Adds the output side of the pipeline. `ExportPlugin` is a `Protocol` (duck typing) defining `process_output()`. `output_pipeline()` consumes a number of items from every processor and sends them to any compatible plugin. A CSV plugin and a JSON plugin are written by hand |
| 3 | `battle.py`, `capacitor.py`, `ex3/` | Abstract factory and capability. `Creature` is an abstract class, `TransformCapability` is a separate abstract class that does not inherit from it. `Flameling` and `Pyrodon` are plain creatures, `Shiftling` and `Morphagon` inherit from both. `FlameFactory` and `TransformCreatureFactory` create the base and evolved entities, and the package exposes only the factories |
| 4 | `tournament.py`, `ex4/` | Abstract strategy. `NormalStrategy` is valid for any entity and just attacks, `AggressiveStrategy` is valid for entities with the transform capability (checked with `isinstance`) and transforms, attacks, then reverts. A single `battle()` function makes every opponent face every other one and aborts the tournament on an invalid entity-strategy pair |

## Requirements

- Python 3.10+
- `flake8` and `mypy` (for linting and type checking)
- Only `abc` and `typing` can be imported, external libraries are forbidden
- Exercises 3 and 4 are packages, so a good understanding of `__init__.py`
  and of what a package exposes is needed (see module 05-bis)

## Structure

Exercises 0 to 2 are single files, each one improving on the previous one.
Exercises 3 and 4 are packages. All the test scripts live at the root of the
module.

```
.
├── data_processor.py
├── data_stream.py
├── data_pipeline.py
├── battle.py
├── capacitor.py
├── tournament.py
├── ex3/
│   ├── __init__.py
│   └── ...
└── ex4/
    ├── __init__.py
    └── ...
```

## Usage

Every exercise is run from the module folder and takes no argument:

```bash
python3 data_processor.py
python3 data_stream.py
python3 data_pipeline.py
```

Exercise 3 has two scripts. `battle.py` tests the factory interface and
`capacitor.py` tests the transform capability:

```bash
python3 battle.py
python3 capacitor.py
```

Exercise 4 runs two tournaments. The second one is invalid on purpose: the
aggressive strategy is given a creature without the transform capability,
so the tournament is aborted with an error message:

```bash
python3 tournament.py
```

## Checks

From inside the module folder:

```bash
flake8 .
mypy --strict *.py ex3/*.py ex4/*.py
```

`data_processor.py` leaves a `mypy` warning on purpose, because it tests the
`ingest` method with an invalid type without validating it first.
