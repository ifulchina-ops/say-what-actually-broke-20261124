"""Say What Actually Broke - one brutally honest error line.

The program writes a single-line software error message (at most
200 characters) to /output/entry.txt: the truth about a certificate
expiry, and what to do next.
"""

from pathlib import Path

LINE = (
    "The site is down because the certificate expired while everyone "
    "assumed someone else was watching it. Renew it, then set an alert "
    "with a human attached."
)

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    # The gate is 1-200 characters, one line, not only white space.
    # Fail loudly here rather than hand the grader an invalid entry.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE or not LINE.strip():
        raise ValueError("entry must be a single non-blank line")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
