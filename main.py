#!/usr/bin/env python3
"""Two robots ride an elevator together and never quite start talking.

The first robot has rehearsed its opening line hundreds of times since
floor 3. Its firmware keeps offering the same safe question about a
charging cable, while dozens of silent floors stretch ahead of them.
One line, one joke, no small talk survived."""

import pathlib

JOKE = (
    "I've run this opener 214 times in my head since floor 3, and my "
    "firmware's best idea is still asking about your charging cable — "
    "41 floors of silence to go."
)

DESTINATION = pathlib.Path("/output/entry.txt")


def ensure_single_line(text):
    """Hold the line to the sealed gate: real text, one line, 1-200 chars."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be only whitespace")
    if len(text) < 1 or len(text) > 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in stripped:
        raise ValueError("entry must be a single line")
    return stripped


def main():
    line = ensure_single_line(JOKE)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(line, encoding="utf-8")
    print(line)
    print(f"characters: {len(line)}")


if __name__ == "__main__":
    main()
