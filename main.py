#!/usr/bin/env python3
"""Two Robots in an Elevator entry: write the joke to /output/entry.txt.

One robot finally speaks after silently running its opener through
its head hundreds of times since floor 3; its firmware can only
suggest asking about the other robot's charging cable, with dozens
of floors of awkward silence still ahead of them.
"""

from pathlib import Path

ENTRY = (
    "I've run this opener 214 times in my head since floor 3, and my "
    "firmware's best idea is still asking about your charging cable — "
    "41 floors of silence to go."
)

OUTPUT_PATH = Path("/output/entry.txt")


def check_entry(text):
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
    check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
