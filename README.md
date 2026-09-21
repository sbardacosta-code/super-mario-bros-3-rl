# Super Mario Bros. 3 RL classroom lab

**[Permanent classroom index](https://github.com/sbardacosta-code/super-mario-bros-3-rl/blob/main/docs/classroom/README.md)**

This project teaches **Super Mario Bros. 3, World 1-1** through recorded reinforcement-learning experiments. Code lives in `smb3_rl/`.

## Current goal: reliable completion

The acceptance target is **at least 18 wins in 20 final evaluation trials**. Winning means collecting the goal card and triggering the verified level-clear transition, not merely reaching the right edge. Once a completion baseline meets that target, a separate experiment will optimize game score while tracking whether completion remains reliable. [Experiment roadmap](docs/ROADMAP.md).

The seven-action recovery model completed its pilot and a further hour of training. Mean progress increased, but the **predeclared final acceptance test was 0/20 wins**: the target is **not met**. Leftward controls permit recovery in scripted validation, but learned reliable recovery has not been demonstrated. No further training is running. [Latest learning timeline](sessions/2026-09-20-smb3-recovery-session-02/LESSON.md) · [20-trial acceptance report](sessions/2026-09-20-smb3-recovery-session-02/ACCEPTANCE.md).

## Classroom materials

- [Session reports, charts and gameplay gallery](docs/classroom/README.md)
- [Teacher guide and discussion questions](docs/TEACHER_GUIDE.md)
- [Setup, pilot, stop/save/resume](docs/SETUP.md)
- [Evaluation and timing protocol](docs/PROTOCOL.md)
- [Validation evidence](sessions/2026-09-16-smb3-validation/REPORT.md)
- [Experiment journal](docs/JOURNAL.md)
- [Publication and model downloads](docs/PUBLISHING.md)

## Local setup

```sh
python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements-lock.txt
.venv/bin/python -m pytest -q
```

The installed `gym-super-mario-bros==9.1.0` package includes the game data locally. There is no separate ROM-import step for this experiment. No ROM, emulator state, or bundled game package is uploaded to this repository or model Releases.

The agent learns from screenshots with a fresh PPO CNN policy. Evaluation records all trials, including failures, incomplete attempts and regressions. The bounded pilot is followed by a user choice of the longer training budget; no three-hour run is assumed.

Training, evaluation, recording, checkpointing and chart generation are self-contained local scripts. There are no GPT/API calls in the gameplay loop and no paid cloud computing.
