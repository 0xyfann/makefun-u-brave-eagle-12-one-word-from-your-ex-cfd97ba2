"""One Word From Your Ex - make.fun entry.

Writes exactly one word to /output/entry.txt: the word an ex
would use to describe the entrant. Stdlib only.
"""

import os

WORD = "forgettable"

# Gate (RULES.txt): entry.txt must be UTF-8 text of 1 to 24 characters,
# not only white space, and exactly one word. Enforce it here so a
# bad word can never be written out by accident.
assert 1 <= len(WORD) <= 24, "word must be 1-24 characters"
assert WORD == WORD.strip(), "word must not contain surrounding whitespace"
assert len(WORD.split()) == 1, "entry must be exactly one word"
assert WORD.isalpha(), "entry must be a single plain word"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
