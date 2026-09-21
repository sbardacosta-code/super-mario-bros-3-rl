# Overnight curriculum — first 30 active minutes

Full-level performance has regressed so far. The five normal-start trials average 1,488.6 pixels before training, 1,154.8 after 15 minutes, and 619 after 30 minutes. Every evaluation trial dies: 0/5 clears at each stage. The target remains 18/20 in the final acceptance evaluation, which has not run yet.

The [stage comparison gallery](LESSON.md) links each explanation to clips, measurements and reviewed frames. At 15 minutes several endings show falls between wooden structures. At 30 minutes failures shift earlier: first plant pipe, open enemy area and a gap. These are observations, not evidence that Mario understands or has forgotten a particular concept.

## Practice is a different outcome

The first closed training segment contains 223 clears in 227 completed goal-practice episodes (119/122 approaching the goal and 104/105 after a missed goal), but 0/82 full-start clears. The second contains 291/291 practice clears and 0/80 full-start clears. These are changing-policy training observations, not frozen-model evaluations. No matched untrained practice evaluation was run, so these rates cannot isolate how much goal skill was acquired during this session. [Separated counts](review/first-two-stage-training-outcomes.json).

This illustrates why a professor should not count successful short exercises as successful complete-level performance. Mario can trigger the verified clear condition when placed near the goal, while still failing to reach it from the beginning. Interference from practice is a hypothesis; five normal-start samples do not prove causation.

## Cost and next scheduled step

At the 30-minute checkpoint, 123,476 policy decisions advanced 493,162 game frames. Scripted reset preparation added 194,700 setup decisions and 778,800 frames, costing about 832 seconds inside the 1,802 seconds of active training. These setup actions were not learned policy decisions. Learning updates took about 324 seconds across 240 PPO update calls and 5,889 optimizer steps. Cumulative evaluation time was about 47 seconds. Sampled memory peaked around 648 MiB, with parent-only fallback when child sampling failed; this is not a guaranteed total-system peak.

The approved schedule continues unchanged: after the first hour of active training the practice probability drops from 75% to 10%, giving normal starts most of the remaining training. No extra budget, reward change or acceptance retry has been introduced. The detached supervisor remains running with its original deadline. Later results are pending.
