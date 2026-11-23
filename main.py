"""Make the AI Judge Laugh: Office Jokes.

Writes one single-line office joke (under 200 characters) to
/output/entry.txt. Deterministic: the same bytes on every run.
Python 3.13 standard library only.
"""

import os

JOKE = "My performance review said I need to be more visible, so now I reply-all to everything."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
