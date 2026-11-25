"""The Internet in One Word — pass A (final).

Writes one word to /output/entry.txt: the single word that best
describes the whole internet, judged on funniness, fit, surprise
and landing in one beat.

Final word: "doomscroll".

Why it beats the pass-B draft ("cookies"): cookies jokes about the
tracking banner, which is one corner of the internet. Doomscroll
names what people actually DO on the whole internet now — open
one app to check one thing, look up an hour later, thumb sore,
mood worse, still scrolling. It is funny by itself, true of the
entire internet rather than one site, surprising (nobody's first
reach is a verb for the habit itself), and it lands in a single
beat: ten letters, one breath, laugh first, nod second.
"""

import os

WORD = "doomscroll"
MAX_CHARS = 30


def entry_word() -> str:
    word = WORD.strip()
    if not word or len(word) > MAX_CHARS:
        raise ValueError("entry word must be 1-30 characters")
    return word


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry_word())


if __name__ == "__main__":
    main()
