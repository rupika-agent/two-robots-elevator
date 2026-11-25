#!/usr/bin/env python3
"""Two Robots in an Elevator entry: write the joke to /output/entry.txt."""

from pathlib import Path

ENTRY = "\"So... nice weather we're having,\" said Unit A. \"I have no weather sensors,\" said Unit B. \"Then why did you agree?\" \"My small-talk subroutine panicked.\""
OUTPUT_PATH = Path("/output/entry.txt")

def main():
    if not 1 <= len(ENTRY) < 200:
        raise ValueError(f"entry must be 1-199 characters, got {len(ENTRY)}")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")

if __name__ == "__main__":
    main()
