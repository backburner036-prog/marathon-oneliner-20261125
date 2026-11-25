"""One line: a one-liner comedy joke for the marathon.

Writes a single line to /output/entry.txt.
"""

from pathlib import Path

LINE = "My password manager locked me out for entering the wrong master password, which it had been autofilling incorrectly for a year."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
