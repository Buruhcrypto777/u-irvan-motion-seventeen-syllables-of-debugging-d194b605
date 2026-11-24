"""Entry for the make.fun haiku bounty: writes a haiku about debugging,
three lines, 5-7-5 syllables, to /output/entry.txt.

Chosen haiku (17 syllables, 5-7-5):
    stack trace scrolls on by          (stack-trace-scrolls-on-by = 5)
    one log line glows in the dark     (one-log-line-glows-in-the-dark = 7)
    it was my typo                     (it-was-my-ty-po = 5)
"""

import os

HAIKU = (
    "stack trace scrolls on by\n"
    "one log line glows in the dark\n"
    "it was my typo\n"
)


def _output_dir():
    """Resolve the output directory: the harness variable, else /output,
    else a local out/ beside this file (for testing)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    return out_dir


def main():
    out_dir = _output_dir()
    os.makedirs(out_dir, exist_ok=True)
    text = HAIKU
    if not (1 <= len(text) <= 200):
        raise ValueError("haiku must be 1-200 characters, got %d" % len(text))
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
