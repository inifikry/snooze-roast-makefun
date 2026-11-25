#!/usr/bin/env python3
"""Snooze Button Roast: write one line roasting an alarm clock that rings
at 6 AM on a Saturday, to /output/entry.txt."""

import os

ROAST = (
    "My alarm clock rings at 6 AM on Saturday like a rooster "
    "that got fired from the farm and took it personally."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: entry must be UTF-8 text of 1 to 200 characters, not only
    # whitespace, and a single line.
    assert "\n" not in ROAST, "entry must be a single line"
    assert 1 <= len(ROAST) <= 200, f"entry is {len(ROAST)} chars"
    assert ROAST.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
