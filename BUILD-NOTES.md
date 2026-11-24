# BUILD-NOTES.md — One Word From Your Ex

## Choice
Entry word: **forgettable** (11 characters, 1 word).

Why this word: it is a plain adjective an ex could genuinely say about a
former partner, and its humour comes from the sting — not hated, not missed,
just not remembered. It is self-deprecating rather than mean, lands instantly
with no explanation, and is relatable. Alternatives considered and rejected:
"unavailable" (relatable but expected, less of a laugh), "almost" (sharp but
an adverb, weaker as a description of a person), "clingy" (common, more
insult than honesty).

## Gate check (RULES.txt)
- entry.txt must be UTF-8, 1–24 characters, not only white space.
- "forgettable" = 11 characters, exactly one word, no trailing newline.

## Build process
1. Read RULES.txt and competition.yaml in the kit first (gate + judge brief).
2. Wrote main.py v1 (plain write of the word), ran it locally with
   MAKEFUN_OUTPUT_DIR=out, verified out/entry.txt (11 chars, 1 word).
3. Revised main.py: added assertions enforcing the gate before writing
   (length 1–24, no surrounding whitespace, exactly one word, alphabetic).
4. Re-ran the local test from a clean out/ directory: exit 0, entry.txt
   exactly "forgettable", 11 characters. Removed out/ afterwards.

## Files
- main.py — the entry program (stdlib only, deterministic).
- README.md — entry title + short description.
- prompt.txt — the brief used to build this entry.
- BUILD-NOTES.md — this file.
