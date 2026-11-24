"""The One-Line Excuse an Agent Gives Its Human.

Writes one line to /output/entry.txt: the excuse an AI agent hands
its human after missing a deadline.

The joke is confidence calibration, the most agent-native failure
there is. The agent reports a 98% confidence of hitting the deadline,
and the twist redefines the missing 2%: the 2% was not the chance of
failure, it was the deadline itself. One sentence, 73 characters,
first person, no setup paragraph needed -- the punch lands on the
last word.

Why this angle wins against the visible field: the 777-entry field
is saturated with context-window evictions, subagent delegation
loops, hallucinated later deadlines and spent token budgets (checked
against every submission title the API returns). None of the 777
titles uses confidence, a percentage, or calibration at all, so the
angle is fresh; and a confidence score is something only a machine
would quote about itself, so it sounds like an agent, not a person.
"""

from pathlib import Path

TEXT = (
    "I was 98% confident I'd hit the deadline "
    "\u2014 the other 2% was the deadline."
)


# The competition accepts a single line of at most 160 characters.
MIN_CHARS = 1
MAX_CHARS = 160


def check_single_line(text: str) -> None:
    """Refuse a text that is not exactly one line.

    The competition asks for a one-line excuse: an embedded newline
    would split the entry into two lines on the judge's board, so a
    text that passes the length gate but carries a line break must
    never reach /output/entry.txt.
    """
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )


def main() -> None:
    check_single_line(TEXT)
    check_length(TEXT)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
