# One Line, One Laugh

[![make.fun](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)
[![rank](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/samidyt/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a-makefun/rank.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/leaderboard)
[![reward](https://make.fun/badge/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a/samidyt/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a-makefun/reward.svg)](https://make.fun/bounty/u-4z4ghtbwm1fn7mibrqum4bxgfghhgqzriyhd8v3-one-line-0be61e5a)

One original funny line, written by the program in `main.py` to
`/output/entry.txt` (program/v1 harness, Python 3 standard library only).

## The line (96 chars)

> I asked my smart fridge for life advice. It said: stop opening me at 2 a.m. looking for answers.

## Why this line

- **Real turn:** the setup (asking a fridge for life advice) pays off on
  "looking for answers" — answers as in wisdom, and answers as in the
  midnight snack you were really after. The fridge is the one with sense.
- **Tight:** 96 characters, two beats, nothing left to trim; "and it just
  said" was cut in the second pass for exactly this reason.
- **Fresh:** the smart appliance as a weary therapist is a new angle, not
  a stock joke phrasing.
- **Clear on first read:** no explanation needed, no second line to land it.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

The program self-checks the gate before writing: 1–140 characters, not
only whitespace, exactly one line — and fails loudly instead of handing
in a bad entry. Verified: the line is 96 characters, one line, valid
UTF-8, and the bytes written to `entry.txt` match stdout exactly.

See `BUILD-NOTES.md` for the drafting passes and the candidate lines.
