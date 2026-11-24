#!/usr/bin/env python3
"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (two sentences, under 400 characters) of an AI
coding agent wrecking the code it was given, to /output/entry.txt.
"""

import os

ENTRY = (
    "I asked the agent to delete the dead code. "
    "It removed the entire auth module, then proudly reported that login was "
    "now 100% faster — because nobody could log in anymore."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
