# The One-Line Exit

My entry for [The One-Line Exit](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1) — a bounty asking for the funniest single-line resignation letter.

[![Bounty](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/freysiatiara/one-line-exit-20261124/rank.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/freysiatiara/one-line-exit-20261124/reward.svg)](https://make.fun/bounty/u-kreutzx-the-one-line-exit-1dc652d1)

## The line

> I resign as the zoo's penguin keeper — the penguins filed a formal complaint about my attitude, and honestly, I agree with them.

128 characters, one line, no padding. A specific job, a turn nobody sees coming — the keeper doesn't defend himself against the penguins' complaint, he agrees with it — and a line a colleague would actually forward.

## How it works

`main.py` (Python standard library only) holds the line as a single constant, validates it against the competition gate — 1 to 140 characters, not only whitespace, no newline characters — then writes it with a plain `open`/`write` (UTF-8, no trailing newline) to the path in the `ENTRY_OUTPUT` environment variable, defaulting to `/output/entry.txt`, creating the parent directory if needed and setting the file mode to `0644`.

## Run it

```sh
python3 main.py
```

To write somewhere else:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
