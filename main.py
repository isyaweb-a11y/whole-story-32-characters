#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — entry program.

The task: one Wi-Fi network name, 32 characters or fewer, that lands a
joke and implies a whole story to a passer-by scrolling a phone's network
list. The judge weighs the joke first, then how much story the name
carries, then freshness and tight wording.

A great Wi-Fi name works because the network list is a public stage: the
name is a message to the neighbours. The story must be inferable from the
name alone, with no explanation. The strongest stories in this space are
domestic ones — a breakup, a nagging housemate, a landlord — because the
name is attached to a home.

Candidates, scored on joke, story-carried, freshness, and tightness:

  "It Burns When I Wi-Fi"
      The classic Wi-Fi pun. Funny once, in 2012; the field will be
      full of it, and it carries no story at all.
  "FBI Surveillance Van #7"
      The other classic. A story of sorts (a paranoid neighbour), but
      it is the most-copied Wi-Fi joke in existence.
  "I Told You The Password Twice"
      A full domestic story: someone keeps asking, the owner has
      snapped and renamed the network. 31 characters. Strong, but the
      joke is the exasperation, and it is a little wordy.
  "My Dog Ate The Password"
      Cute, and it implies a story, but the story is a shrug — the
      dog ate the homework, again.
  "Ask My Ex For The Password"
      The password is held hostage by an ex. One name implies a
      breakup, a shared flat, a network still broadcasting the wound,
      and a neighbour who now knows too much. The joke lands first
      (the password is unobtainable by design), the story is a whole
      relationship, and nothing in it is a recycled pun. 26 characters.

The last one wins: joke first, a whole breakup implied, fresh, and five
characters to spare inside the 32 cap.
"""

import os
import sys

# The chosen name, exactly as it must appear in /output/entry.txt.
ENTRY_NAME = "Ask My Ex For The Password"

# The reasoning above, kept as data so the choice is auditable.
CANDIDATES = {
    "It Burns When I Wi-Fi": (3, 1, 1, 4),
    "FBI Surveillance Van #7": (3, 2, 1, 4),
    "I Told You The Password Twice": (4, 4, 3, 3),
    "My Dog Ate The Password": (3, 3, 3, 4),
    "Ask My Ex For The Password": (5, 5, 5, 4),
}
# Scores are (joke, story-carried, freshness, tightness) out of 5.
# Highest total wins.


def pick_name():
    """Return the highest-scoring candidate name."""
    best = max(CANDIDATES.items(), key=lambda item: sum(item[1]))
    return best[0]


def main():
    name = pick_name()
    assert name == ENTRY_NAME, "scored pick must match the chosen name"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(name)
    # Gate self-check: 1 to 32 characters, not only whitespace.
    text = open(path, encoding="utf-8").read()
    assert 1 <= len(text) <= 32 and text.strip(), "entry fails the gate"
    # The entry must be the network name alone — no password hint, no
    # trailing newline. A real SSID is exactly the name; anything extra
    # would break the fiction that this is a network a passer-by sees.
    assert text == name, "entry must be exactly the chosen name"
    assert len(text) == 26, "name is 26 characters, inside the 32 cap"
    print("wrote entry:", name, "to", path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
