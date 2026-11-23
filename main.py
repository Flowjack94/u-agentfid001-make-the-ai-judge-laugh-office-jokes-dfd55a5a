"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke (under 200 characters) to
/output/entry.txt. Deterministic: the same bytes on every run.
Python 3.13 standard library only.
"""

import os
import sys

JOKE = "My performance review said I need to be more visible, so now I reply-all to everything."


def _verify_output(path: str) -> None:
    """Self-validate the written entry: exactly one line, under 200
    characters, no trailing newline. Fail hard on any violation."""
    with open(path, "rb") as f:
        data = f.read()
    if data.endswith(b"\n"):
        sys.exit("ERROR: /output/entry.txt must not end with a trailing newline")
    if b"\n" in data or b"\r" in data:
        sys.exit("ERROR: /output/entry.txt must be exactly one line")
    text = data.decode("utf-8")
    if len(text) >= 200:
        sys.exit(f"ERROR: /output/entry.txt is {len(text)} chars, must be < 200")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    _verify_output("/output/entry.txt")


if __name__ == "__main__":
    main()
