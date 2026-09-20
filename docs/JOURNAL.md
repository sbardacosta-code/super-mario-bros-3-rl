# Chronological experiment journal

## 2026-09-16 — SMB3 setup

Installed gym-super-mario-bros 9.1.0 and nes-py 9.0.1 in this project's own virtual environment. The active environment uses the pinned NES dependencies. NES package installation provides the local game data; no ROM is committed or uploaded.

Started with World 1-1, a fresh screen-based PPO policy, five rightward actions, four-frame repeat, and CPU/one thread. Task outcomes changed from racing laps to horizontal progress and level completion. The initial baseline is now hold right+B, without jumping. A 12-minute pilot target retains the original user-authorized 10–15-minute scope; further training needs a new budget choice.

## 2026-09-16 — False-clear failure found before training

A scripted validation sequence produced `clear=true` at frame 369 near x=352, while screenshots showed death/fade-out by the first pipe. The installed environment tested timer zero and nonzero map fields before a life decrement appeared. The adapter now also requires the actual World 1-1 map-panel coordinates for completion. The same sequence is then classified as death at frame 370. This is a concrete example of a measurement bug that could reward failure.

Periodic button probes and a bounded scripted action search were used to find a genuine goal traversal for validation. These are environment checks, not PPO learning; their actions are not demonstrations supplied to PPO. See the validation report for the final successful replay and its limits.

## Pilot results

The pilot session's manifest, report and visual analysis will be linked from the permanent index. Record actual training/update/evaluation time and outcome changes, including regressions. Do not replace requested minutes with assumed active time, or interpret successful validation-controller play as learned-policy skill.

## 2026-09-16 — Bounded SMB3 pilot completed

The pilot ran for 622.09 seconds overall (10.37 minutes), including 567.54 seconds of active training. It collected 313,478 action frames / 78,581 decisions and made 153 PPO train calls / 4,726 optimizer steps. All planned baseline, checkpoint and ten additional-seed evaluations completed. [Session report](../sessions/2026-09-16-smb3-pilot/REPORT.md) · [Visual analysis](../sessions/2026-09-16-smb3-pilot/ANALYSIS.md).

Fixed-seed mean progress rose from 573.6 to 754.4 pixels, but completion remained 0/5. Two paired trials regressed. The final additional action seeds produced 0/10 clears; this is not a reliable level solver. The validation controller's success is not counted as PPO success. The stage and final policy weights are identical because no learning occurred between those saves.

Raw emulator stepping measured about 1,401 frames/s; end-to-end active training about 552 frames/s; learning updates took 222.26 seconds. The matched one-trial recording test added about 0.220 seconds of wall time, with 0.431 seconds attributed internally to image handling/encoding; cache/scheduling effects mean these values need not equal. Full evaluation subprocess time was 52.68 seconds.

The original memory thread failed on a macOS PermissionError while enumerating children. Training was unaffected, but its peak field is unavailable, not zero. An independent monitor sampled the final 371.8 seconds and observed 495.3 MiB combined parent/child RSS. Early samples cannot be recovered. After the run, the sampler was fixed to retain parent RSS when children are inaccessible, and a regression test was added. Source-change consent for documented runner fixes was added to resume; environment/configuration checks remain strict.

The complete run used source revision `ed371874407e8d96d95e973cc3f26847300265b4`. Later reporting/memory robustness edits did not change its saved models or gameplay results. No longer training budget has been assumed, launched or scheduled.

## 2026-09-16 — Classroom report adapted from the SMB1 teaching format

Read the separate Mario Bros. 1 reporting code and classroom report without modifying that project. Added a teaching-first SMB3 timeline, median/range alongside mean progress, paired seed regression tables, side-by-side beginning/end GIFs with exact decision ranges, and checkpoint-specific observed behavior, remaining failures and hypotheses. Reviewed notes are preserved separately and bound to model hashes; new or unmatched stages explicitly await visual review. All original measurements, models and clips are unchanged.

The existing runner already checkpoints approximately every 900 seconds of additional active training. The short pilot is labeled with its actual 9.46 minutes; no fictional 15-minute interval was inserted and no further training was launched.

## 2026-09-16 — Approved continuation, first 15-minute checkpoint

The user approved 60 additional active minutes with unchanged PPO settings. Session 02 resumes the pilot final model; its initial evaluation exactly reproduces the prior five outcomes. At 900.66 active seconds, mean progress is 805.8 versus 754.4 pixels, but completion remains 0/5. Seeds 303 and 505 regress severely and fail near the first walking enemy; reviewed clips also show longer trajectories for seeds 101 and 404. No parameter change is made. Training is ongoing within the approved budget; remaining checkpoints and final review are pending. [Session analysis](../sessions/2026-09-16-smb3-session-02/ANALYSIS.md).

## 2026-09-16 — 30-minute continuation checkpoint

At 1,800.66 active seconds, all five evaluation trials reach 1,406–2,061 pixels; mean progress is 1,645.4 versus 805.8 at 15 minutes. No paired trial regresses in progress, but all five still die. Visual review locates failures among flying enemies and at gaps around the wooden steps. The opening failures seen at 15 minutes are absent in this small sample, not proven eliminated. All settings remain fixed; training continues within the approved hour.

## 2026-09-17 UTC — 45-minute continuation regression

At 2,700.66 active seconds, mean evaluation progress falls from 1,645.4 to 1,161.8 pixels; four of five paired trials regress, and clears remain 0/5. Clips show earlier enemy-contact failures and repeated gap falls. The cause is not established. Both the stronger 30-minute checkpoint and this regression are preserved. The final approved segment is running with unchanged parameters.

## 2026-09-17 UTC — Approved hour complete

Session 02 stopped after 3,600.002 active seconds (62.105 wall minutes before charts). Final fixed-seed mean progress reached 2,211.6 pixels, recovering from the 45-minute regression, but there were 0/5 clears; additional seeds also produced 0/10 clears. All evaluations completed. The final save duplicates the 60-minute policy weights.

Visual review identified a concrete limitation: some runs pass the goal card and remain at the far-right boundary until the frame limit, with no leftward action available to return. Other trials still collide with enemies or fall in gaps. Training telemetry includes one clear among 2,261 completed episodes, distinct from the final-policy evaluation; no clip of that training success was recorded. The memory fallback recorded parent-only peak RSS because macOS blocked child enumeration. All stages, including the 45-minute regression, are preserved. No further training was launched.

## 2026-09-20 — Completion target and project publication cleanup

The user set the first acceptance target to at least 18 wins in 20 final trials. Game-score optimization is a later, separate experiment, after reliable completion is established. The next experiment will investigate leftward recovery controls and goal-card collection with a short pilot before choosing a longer budget. No additional training started with this documentation update.

The public repository is named `super-mario-bros-3-rl` and contains only SMB3 materials. The public history has been rebuilt as an SMB3 snapshot. Recorded training source identifiers and hashes remain historical evidence; they are not claims that training used the new publication commit. Original history is retained in a local-only backup. Model bytes, measured outcomes and gameplay recordings are unchanged. Release source tags refer to the cleaned publication snapshot; checkpoint provenance remains in each session manifest.

## 2026-09-20 — Recovery controls and fresh pilot preparation

The user approved adding leftward recovery controls and a fresh 10–15-minute PPO pilot with unchanged reward. Protocol `smb3-1-1-recovery-v2` adds walk-left and jump-left; all existing action indices and learning settings stay unchanged. A new seven-output policy will be initialized rather than loading five-output weights.

A scripted validation replay reproduces the previous seed-303 missed-card failure, returns left, then collects the card and displays COURSE CLEAR. This proves control feasibility only; it is not learned behavior. A real-backtracking assertion initially had no eligible samples because momentum advanced the high-water mark after the turn; the failed validation is retained and the assertion was corrected without changing the reward. [Validation report](../sessions/2026-09-20-smb3-recovery-validation-02/REPORT.md).

The pilot uses the existing fixed five evaluation seeds and ten additional diagnostic seeds; it is not the final 20-trial acceptance test. The target remains 18/20 final clears with a frozen candidate policy. No longer training budget is assumed.
