# Fresh recovery-control PPO pilot

The user approved a 10–15-minute local pilot. The runner targets 12 minutes overall, reserving evaluation time and limiting active training to at most ten minutes. No longer run is approved.

Protocol `smb3-1-1-recovery-v2` expands five actions to seven by adding walk-left and jump-left. The fresh PPO model starts with seed 123, seven outputs and no transferred weights or optimizer state. Reward, observation processing, frame repeat, episode cutoff and PPO hyperparameters match the prior configuration.

The scripted validation demonstrates that returning to a missed goal card is possible. It is not a learned success and supplies no training demonstrations. Both the failed first validation attempt and corrected passing attempt are archived.

Evaluate the untrained policy and hold-run-right baseline, then the trained and final saves with the fixed five action seeds; run ten additional diagnostic seeds at the end. Preserve full traces, clips, outcomes, dependency versions and actual active/evaluation/update timings. The short pilot may finish before 15 active minutes, so its end stage is labeled by actual time.

This compares learning within a new seven-action experiment. Comparing it directly to the hour-trained five-action model would confound action set and training budget. Same numeric seeds do not imply the same initial weights or trajectories when the output dimension changes.

The acceptance target remains at least 18 wins in 20 final trials with a frozen candidate and a predetermined final seed set. This pilot’s diagnostic trials are not that acceptance test. Score optimization is deferred until reliable completion is achieved.
