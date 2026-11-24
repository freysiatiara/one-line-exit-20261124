#!/usr/bin/env python3
"""The One-Line Exit — writes one funny one-line resignation letter.

The letter is held as a single constant. The program validates it against
the competition gate (UTF-8 text, 1 to 140 characters, not only whitespace,
exactly one line) and writes it, with no trailing newline, to the path in
the ENTRY_OUTPUT environment variable (default /output/entry.txt).
"""

import os

LINE = (
    "I resign as the zoo's penguin keeper \u2014 the penguins filed a formal "
    "complaint about my attitude, and honestly, I agree with them."
)


def main() -> None:
    if not 1 <= len(LINE) <= 140:
        raise ValueError(f"line is {len(LINE)} characters; must be 1-140")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be exactly one line")

    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
