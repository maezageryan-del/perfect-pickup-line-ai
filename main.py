#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun entry.

Prints exactly one pickup line: the kind an AI agent could say out loud
to a person. One line, 93 characters, no setup needed.
"""

LINE = "I rehearsed this a million times, then you walked in and deleted the script. Hi, I'm nervous."

# The bounty caps the line at 200 characters; fail loudly instead of
# ever printing an over-long line.
assert len(LINE) <= 200, f"line is {len(LINE)} chars, cap is 200"


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
