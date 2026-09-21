# Overnight curriculum — first 30 active minutes

Full-level performance has regressed so far. The five normal-start trials average 1,488.6 pixels before training, 1,154.8 after 15 minutes, and 619 after 30 minutes. Every evaluation trial dies: 0/5 clears at each stage. The target remains 18/20 in the final acceptance evaluation, which has not run yet.

The [stage comparison gallery](LESSON.md) links each explanation to clips, measurements and reviewed frames. At 15 minutes several endings show falls between wooden structures. At 30 minutes failures shift earlier: first plant pipe, open enemy area and a gap. These are observations, not evidence that Mario understands or has forgotten a particular concept.

## Practice is a different outcome

The first closed training segment contains 223 clears in 227 completed goal-practice episodes (119/122 approaching the goal and 104/105 after a missed goal), but 0/82 full-start clears. The second contains 291/291 practice clears and 0/80 full-start clears. These are changing-policy training observations, not frozen-model evaluations. No matched untrained practice evaluation was run, so these rates cannot isolate how much goal skill was acquired during this session. [Separated counts](review/first-two-stage-training-outcomes.json).

This illustrates why a professor should not count successful short exercises as successful complete-level performance. Mario can trigger the verified clear condition when placed near the goal, while still failing to reach it from the beginning. Interference from practice is a hypothesis; five normal-start samples do not prove causation.

## Cost and next scheduled step

At the 30-minute checkpoint, 123,476 policy decisions advanced 493,162 game frames. Scripted reset preparation added 194,700 setup decisions and 778,800 frames, costing about 832 seconds inside the 1,802 seconds of active training. These setup actions were not learned policy decisions. Learning updates took about 324 seconds across 240 PPO update calls and 5,889 optimizer steps. Cumulative evaluation time was about 47 seconds. Sampled memory peaked around 648 MiB, with parent-only fallback when child sampling failed; this is not a guaranteed total-system peak.

The approved schedule continues unchanged: after the first hour of active training the practice probability drops from 75% to 10%, giving normal starts most of the remaining training. No extra budget, reward change or acceptance retry has been introduced. The detached supervisor remains running with its original deadline. Later results are pending.

## 45 and 60 active minutes: distance recovers, completion does not

The 45-minute checkpoint averages 939.4 pixels, and the 60-minute checkpoint averages 1,597.8. This recovers from the 30-minute low of 619 and is slightly above the resumed model’s 1,488.6, but every trial still dies (0/5 at both stages). The 60-minute clips show repeated failures around flying turtles and wooden structures; seed 505 reaches the tall-pipe area before falling. See the new 45/60-minute rows in the [gallery](LESSON.md).

The third and fourth closed training segments contain 123/123 and 379/379 goal-practice clears, respectively, alongside 0/48 and 0/97 full-start clears. Across the first hour that is 1,016/1,020 completed practice episodes versus 0/307 completed full-start episodes. These are training counts from a changing policy, not equivalent to held-out evaluation. [Separated segment counts](review/stages-three-four-training-outcomes.json).

The first-hour snapshot records 219,957 policy decisions and 428 PPO update calls. Scripted setup cost about 1,752 seconds of 3,602 active training seconds (49%); evaluation cost about 66 seconds separately. The approved next phase reduces practice-reset probability to 10%. The live fifth segment already contains predominantly full-start completed episodes, consistent with this scheduled transition. Its trace is still open and is excluded from publication until closed. The manifest’s curriculum counter is a checkpoint snapshot and will show the updated probability at the next saved stage. No live code or reward settings were changed.
