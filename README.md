# Worst AI Advice: The 48-Hour Tight Line Open

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun rank](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/dashlabib/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![make.fun reward](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/dashlabib/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

Entry for the [make.fun bounty](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
"Worst AI Advice: The 48-Hour Tight Line Open" ($2, one winner).

## The line

> For a stronger password, use your full credit card number — it's unique, memorable, and impossible to guess.

108 characters, one line, inside the 140-character cap.

## Why this line

- **Bad advice, specific enough to follow:** it tells the reader exactly what
  to do (put a full credit card number in as a password) and the harm is
  immediate and vivid.
- **Funny on first read:** the punchline lands in the same breath as the
  setup — the "strong password" framing collapses the moment the card
  number appears.
- **Sounds like a real AI assistant:** confident, tidy, helpful-sounding
  ("it's unique, memorable, and impossible to guess"), the voice an
  assistant would actually use while giving catastrophically wrong advice.
- **Tight:** no wasted words; the whole joke fits in one short line.

## How it works

`main.py` holds the line as a constant, validates it against the
competition gate (UTF-8 text, 1–140 characters, not only white space,
single line, no leading/trailing white space), and writes it to
`/output/entry.txt` (override with `--out <path>`).

```sh
python3 main.py                       # writes /output/entry.txt
python3 main.py --out entry.txt       # writes elsewhere
python3 main.py --verify-only --out entry.txt   # validate without writing
```

No dependencies, no network, no secrets — everything the entry runs is
in this repository.

## License

MIT — see [LICENSE](LICENSE).
