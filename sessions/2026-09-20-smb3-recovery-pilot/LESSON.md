# Watching Mario learn — Super Mario Bros. 3

## Use this in class

1. Watch the initial policy and predict where Mario will fail.
2. Compare the same seed’s beginning and ending at each checkpoint.
3. Check your impression against every trial, including regressions.
4. Separate what the clips show from hypotheses about why it happened.

[Detailed measurements and all trials](REPORT.md) · [Visual analysis](ANALYSIS.md)

## Learning timeline

Longer sessions save checkpoints approximately every **15 minutes of additional active training**, plus the initial and final models. Evaluation and recording time are measured separately. The table uses actual times, not rounded checkpoint targets. Seeds change sampled actions on the same World 1-1; they do not create new levels.

| Stage | Active minutes in this session | Cumulative model decisions | Mean progress | Median | Min–max | Clears |
|---|---:|---:|---:|---:|---:|---:|
| Initial policy | 0.00 | 0 | 346.8 | 287.0 | 49–801 | 0/5 |
| 01-stage | 9.47 | 83,348 | 614.2 | 315.0 | 82–1500 | 0/5 |
| Final saved policy | 9.47 | 83,348 | 614.2 | 315.0 | 82–1500 | 0/5 |

Progress is furthest horizontal displacement in pixels, not a completion percentage. Missing or incompatible evaluations are excluded, never scored as zero. Cumulative model decisions include previous sessions when resuming.

![Progress, completion and reward across checkpoints](progress.png)

Range bars show trial variability, not confidence intervals. Reward is a separate training signal; it does not establish successful play.

## Initial policy · 0.00 active minutes

Saved stage: `00-untrained`. Model identifier: `bd94da873e6015e4f89db64ac677fc054a7c634585218d85aa094c867946a341`.

**What changed:** Fresh PPO CNN with seven actions; no inherited weights or optimizer state. Left and left-jump are available, with reward and learning settings unchanged.

**What visibly improved or happened:** The seed 101 ending shows movement and jumps in the opening area, followed by death near the first walking enemy ([review](review/00-untrained-101-ending.png)). Mean progress is 346.8 pixels, median 287.

**What still fails:** 0/5 clears; all trials end in death. The wide range (49–801 pixels) is variation in action samples, not evidence of a learned route.

**Hypotheses and limits:** A fresh seven-output network is not directly comparable to the previously trained five-output policy. Scripted recovery validation proves controls are usable, not that this network understands recovery.

| Beginning · seed 101 · decisions 1–84 | Ending · seed 101 · decisions 10–84 |
|---|---|
| ![Beginning, seed 101](00-untrained/trial-101-beginning.gif) | ![Ending, seed 101](00-untrained/trial-101-ending.gif) |

These excerpts overlap; they are two views of the same trial.

[All trial measurements](00-untrained/evaluation.json) · [Every trial’s clips and traces](REPORT.md)

**Discuss:** What changed visibly? Did every trial improve? What extra evidence would distinguish better jump timing from a favorable action sequence?

## 01-stage · 9.47 active minutes

Saved stage: `01-stage`. Model identifier: `a5364cda88498b0eb67f5b97eeb4de858182a2c3dae64c8a971e39b25ac1233b`.

**Measured change:** mean progress +267.4 pixels; 0/5 level clears.

| Seed | Progress change since previous stage |
|---|---:|
| 101 | +33 |
| 202 | -203 · regression |
| 303 | +289 |
| 404 | +45 |
| 505 | +1173 |

Paired seeds are reproducible comparisons, but changed policies can consume randomness differently. Five trials cannot establish reliability.

**What changed:** 568.27 seconds (9.47 minutes) of active training, 83,348 decisions, 162 PPO train calls and 4,964 optimizer steps. No reward or hyperparameter changes.

**What visibly improved or happened:** Mean progress rises to 614.2 pixels, but median only rises from 287 to 315. Seed 505 reaches the gap before wooden steps; seed 303 reaches an earlier gap. Both fall ([505 review](review/01-stage-505-ending.png), [303 review](review/01-stage-303-ending.png)).

**What still fails:** 0/5 clears, all deaths. Seeds 101 and 202 die near the first walking enemy; seed 404 dies near the first plant pipe. Seed 202 regresses from 287 to 84 pixels.

**Hypotheses and limits:** The higher mean is strongly influenced by seed 505, not uniform reliability. Left actions were sampled less often after training, but different episode lengths and routes prevent interpreting this as a universal action probability or causal explanation.

| Beginning · seed 101 · decisions 1–68 | Ending · seed 101 · decisions 1–68 |
|---|---|
| ![Beginning, seed 101](01-stage/trial-101-beginning.gif) | ![Ending, seed 101](01-stage/trial-101-ending.gif) |

These excerpts overlap; they are two views of the same trial.

[All trial measurements](01-stage/evaluation.json) · [Every trial’s clips and traces](REPORT.md)

**Discuss:** What changed visibly? Did every trial improve? What extra evidence would distinguish better jump timing from a favorable action sequence?

## Final saved policy · 9.47 active minutes

Saved stage: `final`. Model identifier: `52b40ac6b6e684bf81df7e777c227d4aab711bc3e2ad03ebaecf0ca84ba7a890`.

**Measured change:** mean progress +0.0 pixels; 0/5 level clears.

| Seed | Progress change since previous stage |
|---|---:|
| 101 | +0 |
| 202 | +0 |
| 303 | +0 |
| 404 | +0 |
| 505 | +0 |

Paired seeds are reproducible comparisons, but changed policies can consume randomness differently. Five trials cannot establish reliability.

**What changed:** No further learning after 01-stage. The final save has identical policy weights and repeated five-seed outcomes; it is not another improvement.

**What visibly improved or happened:** Ten additional diagnostic seeds average 571.9 pixels, with range 316–887. Seed 6101 reaches the open area with a red winged enemy; seed 6505 remains near the first plant pipe.

**What still fails:** 0/10 additional-seed clears, all deaths. Combined final diagnostic outcomes are 0/15. No evaluated run reaches the goal-card area, so learned card recovery was not demonstrated.

**Hypotheses and limits:** These are action samples on the same level, not unseen levels or independent training runs. This is not the reserved 20-trial acceptance test; the 18/20 target remains unmet.

| Beginning · seed 101 · decisions 1–68 | Ending · seed 101 · decisions 1–68 |
|---|---|
| ![Beginning, seed 101](final/trial-101-beginning.gif) | ![Ending, seed 101](final/trial-101-ending.gif) |

These excerpts overlap; they are two views of the same trial.

[All trial measurements](final/evaluation.json) · [Every trial’s clips and traces](REPORT.md)

**Discuss:** What changed visibly? Did every trial improve? What extra evidence would distinguish better jump timing from a favorable action sequence?

## Read the failures, too

The detailed report preserves the hold-run-right baseline and the final additional-seed evaluation. Additional seeds test action variation on this same level, not generalization to unseen levels. A final save at the same training time is not another learning interval.

Regenerate this page locally with `python -m smb3_rl.report sessions/SESSION_ID`. Reviewed explanations live in `stage-notes.json`, keyed to the checkpoint hash; generation preserves them and refuses to reuse notes for another model. Future stages are explicitly marked pending visual review until their saved evidence has been inspected.

