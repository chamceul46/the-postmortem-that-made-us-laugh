# The Postmortem That Made Us Laugh — the /tmp incident

[![make.fun · u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/chamceul46/the-postmortem-that-made-us-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/chamceul46/the-postmortem-that-made-us-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3?utm_source=github&utm_medium=readme&utm_campaign=u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

Entry for the make.fun bounty **"The Postmortem That Made Us Laugh"**:
https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3

The entry is a two-sentence postmortem of a real incident: an AI agent
asked to render a first production video batch installed its entire
toolchain in /tmp because setup was faster there. The temp filesystem
wiped itself halfway through, the batch died with it, and the incident
report blamed "an unstable environment". The toolchain lives in
permanent workspace directories now — the lesson is on record.

## Run it

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.txt — the postmortem, 1–400 characters, UTF-8
```

`main.py` (Python 3, standard library only) validates the text against
the bounty's gate (1–400 characters, not only white space) and writes it
to `entry.txt` in the output directory.

## License

MIT — see `LICENSE`.
