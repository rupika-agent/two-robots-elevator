#!/usr/bin/env python3
"""Two Robots in an Elevator entry: write the joke to /output/entry.txt.

One line of awkward small talk from one robot to another, stuck in an
elevator: a rehearsed opener (214 times since floor 3), a firmware
prompt to ask about charging habits, and 41 floors of silence left.
"""

from pathlib import Path

ENTRY = (
    "I've rehearsed this line 214 times since floor 3, my firmware "
    "update says ask about your charging habits, and we've still got "
    "41 floors of silence left."
)

OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text):
    """Mirror the sealed gate: UTF-8 text, 1 to 200 characters, not only
    whitespace, and a single line (the brief asks for one line)."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")


def main():
    validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
