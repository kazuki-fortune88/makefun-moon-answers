"""The Moon Finally Answers Back — one line from the Moon."""

import os
from pathlib import Path

LINE = (
    "After four billion years of your wishes, howls, and 2 a.m. promises, "
    "I have one answer: no. Also, the tides are on strike until someone "
    "wishes ME something nice for once."
)


def output_dir() -> Path:
    """Resolve the output directory without ever deleting it."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_entry() -> Path:
    """Write exactly one line of Moon text to entry.txt."""
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE + "\n", encoding="utf-8")
    return target


if __name__ == "__main__":
    write_entry()
