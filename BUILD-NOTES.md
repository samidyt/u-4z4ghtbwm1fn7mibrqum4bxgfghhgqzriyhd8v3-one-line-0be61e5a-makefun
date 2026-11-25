# Build notes — One Line, One Laugh

## Drafting passes

- **Pass 1:** wrote `main.py` with the line
  "I asked my smart fridge for life advice, and it just said: stop
  opening me at 2 a.m. looking for answers." (105 chars). Ran it:
  exit 0, stdout 105 chars / 1 line, entry.txt bytes identical.
- **Pass 2 (tightening):** cut "and it just said" → "It said:", two
  beats instead of one long clause. New line (96 chars):
  "I asked my smart fridge for life advice. It said: stop opening me
  at 2 a.m. looking for answers." Also added a UTF-8 round-trip check
  (written bytes must decode to exactly the line). Re-ran: exit 0,
  stdout 96 chars / 1 line, entry.txt bytes identical.

## Alternates considered (all original, all 1–140 chars)

1. "My plants died of neglect, so I bought plastic ones — now even the
   fake ones look disappointed in me." (101 chars) — decent, but the
   punchline repeats the "disappointed in me" beat used in an earlier
   one-line entry of ours; dropped for freshness.
2. "I told my Wi-Fi router we're growing apart. It said the feeling's
   mutual — that's why the signal keeps dropping." (112 chars) — good
   turn, but the setup telegraphs the punchline ("growing apart" →
   signal dropping); dropped for tightness.
3. "My alarm clock and I have an agreement: it wakes me up, and I hit
   snooze until we've both given up on the day." (110 chars) — warm,
   but a mild observation rather than a real twist; dropped for laugh.

## Verification

- Kit: tarball sha256 matches `bundleSha256`
  `b082ae5000a7117b2ae2d130fe48f1f6bf2a51b1c4983503241e0a42455d9bf1`;
  all 8 files in `kit.json` verified against their sha256.
- Gate: 96 chars, 1 line, valid UTF-8, not whitespace-only.
- No local grader exists for this bounty (kit RULES.txt: "There is no
  local grade of this competition: the server grades every entry"), so
  verification is the program's own gate + stdout/bytes comparison.
- Runs used a scratch `$MAKEFUN_OUTPUT_DIR`; the shared
  `/output/entry.txt` was left untouched (concurrent builds share it).
