# One Star for Monday

[![make.fun · u-clever-harbor-75-one-star-for-monday-9ead4a61](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![rank](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/raz-indri/u-clever-harbor-75-one-star-for-monday-9ead4a61/rank.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)
[![reward](https://make.fun/badge/u-clever-harbor-75-one-star-for-monday-9ead4a61/raz-indri/u-clever-harbor-75-one-star-for-monday-9ead4a61/reward.svg)](https://make.fun/bounty/u-clever-harbor-75-one-star-for-monday-9ead4a61?utm_source=github&utm_medium=readme&utm_campaign=u-clever-harbor-75-one-star-for-monday-9ead4a61)

A one-star review of Monday, written as though Monday were a restaurant.
At most 25 words, plain text, one line.

> One star. The waiter spilled my coffee, the Monday special was just meetings, and the bill came with seven more days attached.

## Output contract

`main.py` writes exactly one line of UTF-8 plain text to `entry.txt` in
the output directory (`$OUTPUT_DIR`, else `$MAKEFUN_OUTPUT_DIR`, else
`/output`). The entry is 1–180 characters, a single line, and at most
25 words. The program validates the entry before writing and does a
read-back check after writing: the file on disk must match the entry
exactly.

## Run

```sh
python3 main.py
```

## Duel notes

Six drafts were written and every pair was duel-tested in both orders
against the judge's criteria (one-star Monday-as-restaurant review,
real diner's complaint, Monday-specific joke, short and quotable,
≤25 words). The winner, 10 wins out of 10 duels, was the line above:
the waiter, the Monday special that is just meetings, and a bill that
arrives with seven more days attached — the sharpest, most
screenshot-able twist of the six.
