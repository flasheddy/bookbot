# bookbot

A small command-line tool that reads a plain-text book and prints a report:
total word count plus a per-character frequency table (letters only, sorted
most-to-least frequent, case-insensitive).

Built as a [Boot.dev](https://www.boot.dev) learning project.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) (recommended) — or plain `python3`

## Run

```sh
uv run main.py books/frankenstein.txt
```

Without uv:

```sh
python3 main.py books/frankenstein.txt
```

Exactly one argument is required: the path to a UTF-8 text file. With no
argument the script prints usage and exits with status 1.

### Example output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
...
============= END ===============
```

## Sample books

`books/` contains `frankenstein.txt`, `mobydick.txt`,
`prideandprejudice.txt`. Any plain-text file works.

## Project layout

| File | Purpose |
|---|---|
| `main.py` | CLI entry point: reads the file, prints the report |
| `stats.py` | Counting helpers (`get_word_count`, `get_char_counts`, `chars_dict_to_sorted_list`) |
| `books/` | Sample input texts |
| `pyproject.toml` | Project metadata and dev dependency group |

## Development

```sh
uv sync            # install dev tools (mypy, ruff, pytest)
uv run ruff check .
uv run mypy .
uv run pytest      # no test files exist yet
```
