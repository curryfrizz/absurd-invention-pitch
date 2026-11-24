"""One-Sentence Absurd Invention Pitch -- make.fun entry.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to /output/entry.txt. Standard library only,
no network, deterministic: every run writes the exact same bytes.

The annoyance chosen here is the universal doorway blank: you stride
into a room with a clear purpose and, the instant you cross the
threshold, the purpose is gone. The invention is a doormat that
notices the blank, rewinds the walker, and hands the errand back.
"""

from pathlib import Path

# The gate allows at most 220 characters and exactly one sentence;
# this pitch uses 198, so it clears the limit with room to spare.
# Final revision: the doormat is now a treadmill, which is what makes
# the rewind physically happen instead of just being claimed.
LINE = "The Doorway Rewind is a treadmill doormat that senses the exact second you enter a room and forget why, rolls you three steps back out, and replays your forgotten errand in your own confident voice."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader collects outputs as another user, so the file must be
    # readable by everyone, not just the user the program runs as.
    out.chmod(0o644)


# Entry point: run main() so the single sentence is written out.
if __name__ == "__main__":
    main()
