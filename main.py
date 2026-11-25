"""One-liner entry for make.fun: one line, at most 280 chars.

The program writes LINE verbatim to /output/entry.txt (127 chars).
"""

from pathlib import Path

LINE = "My password manager locked me out for entering the wrong master password, which it had been autofilling incorrectly for a year."
ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry text, creating /output when needed."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
