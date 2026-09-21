# SMB3 World 1-1 — 2026-09-21-smb3-overnight-curriculum

Session status: **running**. This is a local CPU experiment.

[Classroom learning timeline and stage explanations](LESSON.md) · [Manifest](manifest.json) · [Configuration](config.json) · [Dependencies](requirements.txt)

## Time and work measured

| Measurement | Value |
|---|---:|
| Session wall time before chart generation | 3670.77 s |
| Active training | 3601.93 s |
| Rollout collection (includes inference and traces) | 2984.94 s |
| Raw emulator stepping inside collection | 754.05 s |
| Learning updates | 614.92 s |
| Evaluation subprocesses (includes recording/startup) | 65.95 s |
| Checkpoint saving | 0.20 s |
| Training game frames | 878,346 |
| Agent decisions | 219,957 |
| PPO train calls / optimizer steps | 428 / 10108 |
| Sampled peak RSS | 648.3 MiB (parent_only_fallback_used) |

Nested timing fields overlap: raw stepping is part of collection, and collection/learning are part of active training. RSS is sampled every 100 ms; shared pages may be counted twice. Reset/setup frames are excluded from action-frame counters.

Raw simulation: 1165 frames/s; end-to-end training: 244 frames/s; learning: 16.4 optimizer steps/s.

## Outcomes across stages

![Outcome and reward charts](progress.png)

Error bars show the range across the five trials, not confidence intervals. Progress is furthest horizontal displacement from the start, in pixels, not a percentage of the level. Completion is measured independently. Finishing time uses action frames / 60, only for completed levels. Training reward is plotted separately and is not a success rate.

## 00-resumed

0.00 additional active minutes. Model SHA-256: `277ca1daafdfe484b6e0150086eac3a377b045f306fdd8e01073658e211b66ec`.

Evaluation **complete**: 5/5 finished trials. [Full measurements](00-resumed/evaluation.json).

**Observed measurements:** 0/5 clears; 5 deaths; mean progress 1488.6 pixels (range 327–2221); mean shaped reward 13.782.

| Trial | Progress (pixels) | Outcome | Evidence |
|---|---:|---|---|
| 101 | 1766 | death | [Trace](00-resumed/trial-101.jsonl) · [beginning](00-resumed/trial-101-beginning.gif) · [ending](00-resumed/trial-101-ending.gif) |
| 202 | 1500 | death | [Trace](00-resumed/trial-202.jsonl) · [beginning](00-resumed/trial-202-beginning.gif) · [ending](00-resumed/trial-202-ending.gif) |
| 303 | 1629 | death | [Trace](00-resumed/trial-303.jsonl) · [beginning](00-resumed/trial-303-beginning.gif) · [ending](00-resumed/trial-303-ending.gif) |
| 404 | 327 | death | [Trace](00-resumed/trial-404.jsonl) · [beginning](00-resumed/trial-404-beginning.gif) · [ending](00-resumed/trial-404-ending.gif) |
| 505 | 2221 | death | [Trace](00-resumed/trial-505.jsonl) · [beginning](00-resumed/trial-505-beginning.gif) · [ending](00-resumed/trial-505-ending.gif) |

| Beginning · seed 101 · decisions 1–150 | Ending · seed 101 · decisions 217–291 |
|---|---|
| ![Beginning, seed 101](00-resumed/trial-101-beginning.gif) | ![Ending, seed 101](00-resumed/trial-101-ending.gif) |

The middle of this trial is omitted from these excerpts; the full action trace is retained.


## 01-stage

15.00 additional active minutes. Model SHA-256: `e5a420364a444d1dc9ee72268f1464d56e76f942848b031ee2899e3ba8f8f9ac`.

Evaluation **complete**: 5/5 finished trials. [Full measurements](01-stage/evaluation.json).

**Observed measurements:** 0/5 clears; 5 deaths; mean progress 1154.8 pixels (range 342–1628); mean shaped reward 10.450.

Mean progress changed by -333.8 pixels; completion count changed by +0. Improvement is not assumed, and five action samples are a small evaluation.

| Trial | Progress (pixels) | Outcome | Evidence |
|---|---:|---|---|
| 101 | 560 | death | [Trace](01-stage/trial-101.jsonl) · [beginning](01-stage/trial-101-beginning.gif) · [ending](01-stage/trial-101-ending.gif) |
| 202 | 342 | death | [Trace](01-stage/trial-202.jsonl) · [beginning](01-stage/trial-202-beginning.gif) · [ending](01-stage/trial-202-ending.gif) |
| 303 | 1628 | death | [Trace](01-stage/trial-303.jsonl) · [beginning](01-stage/trial-303-beginning.gif) · [ending](01-stage/trial-303-ending.gif) |
| 404 | 1628 | death | [Trace](01-stage/trial-404.jsonl) · [beginning](01-stage/trial-404-beginning.gif) · [ending](01-stage/trial-404-ending.gif) |
| 505 | 1616 | death | [Trace](01-stage/trial-505.jsonl) · [beginning](01-stage/trial-505-beginning.gif) · [ending](01-stage/trial-505-ending.gif) |

| Beginning · seed 101 · decisions 1–150 | Ending · seed 101 · decisions 85–159 |
|---|---|
| ![Beginning, seed 101](01-stage/trial-101-beginning.gif) | ![Ending, seed 101](01-stage/trial-101-ending.gif) |

These excerpts overlap; they are two views of the same trial.


## 02-stage

30.03 additional active minutes. Model SHA-256: `4dda2cd8cda35d57b3011d8ae16765066fcb968d71b9ebbcc525037dd5d97df4`.

Evaluation **complete**: 5/5 finished trials. [Full measurements](02-stage/evaluation.json).

**Observed measurements:** 0/5 clears; 5 deaths; mean progress 619.0 pixels (range 326–1087); mean shaped reward 5.131.

Mean progress changed by -535.8 pixels; completion count changed by +0. Improvement is not assumed, and five action samples are a small evaluation.

| Trial | Progress (pixels) | Outcome | Evidence |
|---|---:|---|---|
| 101 | 326 | death | [Trace](02-stage/trial-101.jsonl) · [beginning](02-stage/trial-101-beginning.gif) · [ending](02-stage/trial-101-ending.gif) |
| 202 | 1087 | death | [Trace](02-stage/trial-202.jsonl) · [beginning](02-stage/trial-202-beginning.gif) · [ending](02-stage/trial-202-ending.gif) |
| 303 | 887 | death | [Trace](02-stage/trial-303.jsonl) · [beginning](02-stage/trial-303-beginning.gif) · [ending](02-stage/trial-303-ending.gif) |
| 404 | 327 | death | [Trace](02-stage/trial-404.jsonl) · [beginning](02-stage/trial-404-beginning.gif) · [ending](02-stage/trial-404-ending.gif) |
| 505 | 468 | death | [Trace](02-stage/trial-505.jsonl) · [beginning](02-stage/trial-505-beginning.gif) · [ending](02-stage/trial-505-ending.gif) |

| Beginning · seed 101 · decisions 1–99 | Ending · seed 101 · decisions 25–99 |
|---|---|
| ![Beginning, seed 101](02-stage/trial-101-beginning.gif) | ![Ending, seed 101](02-stage/trial-101-ending.gif) |

These excerpts overlap; they are two views of the same trial.


## 03-stage

45.03 additional active minutes. Model SHA-256: `33cfa248c291d974f54adbb2601e3ae5fce0b4dbe4abdbda102d44c3eddd019f`.

Evaluation **complete**: 5/5 finished trials. [Full measurements](03-stage/evaluation.json).

**Observed measurements:** 0/5 clears; 5 deaths; mean progress 939.4 pixels (range 326–1503); mean shaped reward 8.309.

Mean progress changed by +320.4 pixels; completion count changed by +0. Improvement is not assumed, and five action samples are a small evaluation.

| Trial | Progress (pixels) | Outcome | Evidence |
|---|---:|---|---|
| 101 | 1108 | death | [Trace](03-stage/trial-101.jsonl) · [beginning](03-stage/trial-101-beginning.gif) · [ending](03-stage/trial-101-ending.gif) |
| 202 | 326 | death | [Trace](03-stage/trial-202.jsonl) · [beginning](03-stage/trial-202-beginning.gif) · [ending](03-stage/trial-202-ending.gif) |
| 303 | 1503 | death | [Trace](03-stage/trial-303.jsonl) · [beginning](03-stage/trial-303-beginning.gif) · [ending](03-stage/trial-303-ending.gif) |
| 404 | 885 | death | [Trace](03-stage/trial-404.jsonl) · [beginning](03-stage/trial-404-beginning.gif) · [ending](03-stage/trial-404-ending.gif) |
| 505 | 875 | death | [Trace](03-stage/trial-505.jsonl) · [beginning](03-stage/trial-505-beginning.gif) · [ending](03-stage/trial-505-ending.gif) |

| Beginning · seed 101 · decisions 1–150 | Ending · seed 101 · decisions 155–229 |
|---|---|
| ![Beginning, seed 101](03-stage/trial-101-beginning.gif) | ![Ending, seed 101](03-stage/trial-101-ending.gif) |

The middle of this trial is omitted from these excerpts; the full action trace is retained.


## 04-stage

60.03 additional active minutes. Model SHA-256: `e2c3ca4382e78c77d122adf9e7cad4002c9320eb997eac8f8740b9b30dd6711d`.

Evaluation **complete**: 5/5 finished trials. [Full measurements](04-stage/evaluation.json).

**Observed measurements:** 0/5 clears; 5 deaths; mean progress 1597.8 pixels (range 1362–2221); mean shaped reward 14.866.

Mean progress changed by +658.4 pixels; completion count changed by +0. Improvement is not assumed, and five action samples are a small evaluation.

| Trial | Progress (pixels) | Outcome | Evidence |
|---|---:|---|---|
| 101 | 1635 | death | [Trace](04-stage/trial-101.jsonl) · [beginning](04-stage/trial-101-beginning.gif) · [ending](04-stage/trial-101-ending.gif) |
| 202 | 1363 | death | [Trace](04-stage/trial-202.jsonl) · [beginning](04-stage/trial-202-beginning.gif) · [ending](04-stage/trial-202-ending.gif) |
| 303 | 1362 | death | [Trace](04-stage/trial-303.jsonl) · [beginning](04-stage/trial-303-beginning.gif) · [ending](04-stage/trial-303-ending.gif) |
| 404 | 1408 | death | [Trace](04-stage/trial-404.jsonl) · [beginning](04-stage/trial-404-beginning.gif) · [ending](04-stage/trial-404-ending.gif) |
| 505 | 2221 | death | [Trace](04-stage/trial-505.jsonl) · [beginning](04-stage/trial-505-beginning.gif) · [ending](04-stage/trial-505-ending.gif) |

| Beginning · seed 101 · decisions 1–150 | Ending · seed 101 · decisions 204–278 |
|---|---|
| ![Beginning, seed 101](04-stage/trial-101-beginning.gif) | ![Ending, seed 101](04-stage/trial-101-ending.gif) |

The middle of this trial is omitted from these excerpts; the full action trace is retained.


## Run right baseline

Status: complete. [Measurements](hold-run-right/evaluation.json).

0/5 clears; mean progress 88.0 pixels. Additional seeds are action samples on the same level, not unseen levels.

| Trial | Progress (pixels) | Outcome | Evidence |
|---|---:|---|---|
| 101 | 88 | death | [Trace](hold-run-right/trial-101.jsonl) · [beginning](hold-run-right/trial-101-beginning.gif) · [ending](hold-run-right/trial-101-ending.gif) |
| 202 | 88 | death | [Trace](hold-run-right/trial-202.jsonl) · [beginning](hold-run-right/trial-202-beginning.gif) · [ending](hold-run-right/trial-202-ending.gif) |
| 303 | 88 | death | [Trace](hold-run-right/trial-303.jsonl) · [beginning](hold-run-right/trial-303-beginning.gif) · [ending](hold-run-right/trial-303-ending.gif) |
| 404 | 88 | death | [Trace](hold-run-right/trial-404.jsonl) · [beginning](hold-run-right/trial-404-beginning.gif) · [ending](hold-run-right/trial-404-ending.gif) |
| 505 | 88 | death | [Trace](hold-run-right/trial-505.jsonl) · [beginning](hold-run-right/trial-505-beginning.gif) · [ending](hold-run-right/trial-505-ending.gif) |

| Beginning · seed 101 · decisions 1–65 | Ending · seed 101 · decisions 1–65 |
|---|---|
| ![Beginning, seed 101](hold-run-right/trial-101-beginning.gif) | ![Ending, seed 101](hold-run-right/trial-101-ending.gif) |

These excerpts overlap; they are two views of the same trial.


## Recording overhead


## Interpretation

[Read the visual stage-by-stage analysis](ANALYSIS.md).

## Training curriculum

Only training resets use goal practice. Every evaluation and every point in the progress chart starts from the normal beginning of World 1-1. Practice clears do not count toward the 18/20 target.
First 60 active minutes: 75% practice resets, split between goal approach and missed goal; subsequently 10% practice and 90% normal starts. These are probabilities, not guaranteed proportions.
Scripted reset actions are not PPO decisions or demonstrations. Their frames and elapsed time are reported separately; reset setup time is included in active training wall time. Reward coefficients and the seven actions are unchanged.
Setup and reset counters: `{'setup_frames': 1533400, 'setup_decisions': 383350, 'setup_seconds': 1752.2816647595027, 'practice_resets': 1021, 'full_resets': 307, 'practice_probability': 0.75}`.
Final acceptance uses predeclared new action-sampling seeds 9101–9120 on the same level. It is not a test on unseen levels.
