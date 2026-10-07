# Data Archivist - Module 04

Each exercise is a small program that works with files and data streams:
`open`, `read`, `write`, `close`, `sys.argv`, `sys.stdin`, `sys.stderr`
and, in the last exercise, the `with` statement (context managers).
File errors are handled without crashing the program.

## Exercises

| Ex | File | What it does |
|----|------|--------------|
| 0 | `ft_ancient_text.py` | Gets a file name from the command line and prints its content like `cat`, with a header and footer. Handles a missing argument, nonexistent and inaccessible files, and always closes the file in `finally` |
| 1 | `ft_archive_creation.py` | Reads a file, adds a `#` at the end of each line, displays the new content and asks for a file name to save it to (or empty to skip saving) |
| 2 | `ft_stream_management.py` | Same as ex1, but error messages go to `sys.stderr` with a `[STDERR]` prefix and user input is read from `sys.stdin` instead of `input()` |
| 3 | `ft_vault_security.py` | `secure_archive()` reads or writes a file using a `with` statement and returns a `(success, content_or_error)` tuple |

## Requirements

- Python 3.10+
- `flake8` and `mypy` (for linting and type checking)

## Usage

Each exercise lives in its own directory (`ex0/` to `ex3/`). Exercises 0 to 2
are plain scripts that take the file to read as an argument. Without it, they
print a usage message:

```bash
cd ex0
python3 ft_ancient_text.py
python3 ft_ancient_text.py ancient_fragment.txt
```

Error cases (nonexistent file, permission denied):

```bash
python3 ft_ancient_text.py foo
python3 ft_ancient_text.py /etc/master.passwd
```

Exercises 1 and 2 then ask for a file name to save the transformed content.
Leave it empty to avoid saving:

```bash
cd ex1
python3 ft_archive_creation.py ancient_fragment.txt
```

In exercise 2, errors are written to the error stream. To check it, redirect
the standard output: the error message should still appear on the screen and
`out.txt` should not contain it:

```bash
cd ex2
python3 ft_stream_management.py foo > out.txt
```

Exercise 3 takes no argument. It has its own `if __name__ == "__main__":`
block that tests `secure_archive()` on a nonexistent file, an inaccessible
file, a regular file (`ancient_fragment.txt`, which must be in the same
directory) and a write to `new_fragment.txt`:

```bash
cd ex3
python3 ft_vault_security.py
```

## Checks

```bash
flake8 .
mypy --strict ft_*.py
```

Note: the `with` statement is only used in exercise 3, as required by the
subject. Exercises 0 to 2 open and close files manually.