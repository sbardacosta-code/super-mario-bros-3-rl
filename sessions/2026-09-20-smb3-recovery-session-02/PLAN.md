# Seven-action continuation — approved 60 active minutes

Resume the recovery pilot final model and optimizer state for **60 additional active minutes**, with approximately 15-minute milestones and unchanged seven-action PPO configuration, reward, observations and episode limit. Source, configuration and validation fingerprints match the parent exactly. Emulator and random state reset on resume; this is not bit-for-bit continuation.

Review frozen checkpoints using the same five action seeds; retain hold-run-right and the ten additional diagnostic seeds. Save all initial, intermediate and final checkpoints, full traces and comparable GIFs. Record progress, clears, successful finish times and reward separately, including regressions.

The leftward controls make recovery possible, but purposeful recovery is not assumed. Inspect behavior and traces before explaining it. Scripted validation clears are never counted as learned wins.

## Predeclared acceptance evaluation

After training, evaluate the **final checkpoint**, chosen in advance, on the 20 seeds in [acceptance-plan.json](acceptance-plan.json). These seeds are additional action samples on the same level, not new levels. The target is at least 18 verified clears in 20 complete valid trials. Deaths and frame limits are failures; interrupted or invalid evaluations cannot pass. Preserve all results without silently rerunning failures. Report this evaluation’s time separately from the training runner’s manifest totals.

The target tests this one policy on this one level, not universal reliability or generalization. Score optimization remains deferred. No training beyond the approved additional hour is authorized.
