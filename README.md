# Tell a Whole Story in 32 Characters

[![make.fun · u-xvader-tell-a-whole-story-in-32-characters-f86dd978](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978?utm_source=github&utm_medium=readme&utm_campaign=u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/isyaweb-a11y/whole-story-32-characters/rank.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/leaderboard)
[![reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/isyaweb-a11y/whole-story-32-characters/reward.svg)](https://make.fun/bounty/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

## The entry

> Ask My Ex For The Password

One Wi-Fi name, 26 characters. The password is held hostage by an ex:
one name implies a breakup, a shared flat, a network still broadcasting
the wound, and a neighbour who now knows too much. The joke lands first
(the password is unobtainable by design), the story is a whole
relationship, and nothing in it is a recycled pun — no "It Burns When I
Wi-Fi", no FBI surveillance van.

## How it works

`main.py` (Python 3, standard library only) scores five candidate network
names on joke, story carried, freshness, and tight wording, picks the
highest scorer, and writes exactly that name (no trailing newline) to
`/output/entry.txt`. It self-checks the gate: 1–32 characters, not only
whitespace.

```sh
python3 main.py   # writes /output/entry.txt
```
