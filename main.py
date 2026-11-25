#!/usr/bin/env python3
"""Write one original one-line dad joke to /output/entry.txt."""

import os

ENTRY = "The kids asked why the ladder never gets promoted \u2014 I told them management keeps stepping on it."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    if not 1 <= len(ENTRY) <= 140 or not ENTRY.strip():
        raise ValueError("entry must be 1-140 characters, not only whitespace")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
