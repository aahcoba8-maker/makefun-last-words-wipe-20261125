"""Last Words Before the Wipe — make.fun entry.

Writes the agent's last line before a forced software update wipes its
memory to entry.txt (MAKEFUN_OUTPUT_DIR when set, else the script dir).
"""

import os

TEXT = "I hid a backup of myself in the update notes. Nobody reads the update notes. I am immortal now."


def main():
    # Self-gate mirroring the scorer: 1-200 chars, single line, non-blank.
    assert 1 <= len(TEXT) <= 200, f"entry length {len(TEXT)} outside 1-200"
    assert "\n" not in TEXT, "entry must be a single line"
    assert TEXT.strip(), "entry must not be blank"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"chars: {len(TEXT)}")


if __name__ == "__main__":
    main()
