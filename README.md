# Notes From a Passive-Aggressive Fridge

[![make.fun](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/c/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/rahmatjibran04-byte/makefun-passive-fridge/rank.svg)](https://make.fun/c/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/rahmatjibran04-byte/makefun-passive-fridge/reward.svg)](https://make.fun/c/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

One funny passive-aggressive note a smart fridge leaves for its owner — a
single dry, petty, specific line for the door screen. Entry for the
[Notes From a Passive-Aggressive Fridge](https://make.fun/c/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
bounty on [make.fun](https://make.fun).

## The note

> I counted 14 door openings today. You took nothing. The leftovers have started a group chat about you.

## How it works

`main.py` writes that one line to `/output/entry.txt` (UTF-8, no trailing
newline, mode `0644`). It validates the note first — 1–200 characters, a
single line — then reads the file back and refuses to finish unless the bytes
on disk match the note exactly. No network, no input files, fully
deterministic: every run produces the same 102 bytes.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
