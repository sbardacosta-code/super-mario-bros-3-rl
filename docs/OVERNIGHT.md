# Unattended completion-first experiment

The user approved approximately six hours total on this Mac, including setup, checkpoint evaluations and final testing. The machine must stay connected to power with its lid open. The supervisor runs `caffeinate -is` for its own lifetime; the display may sleep. Power loss, a closed lid, forced shutdown or an operating-system crash can still interrupt the experiment.

The local supervisor has no prompts, API calls, purchases or cloud dependencies. It runs with standard input disconnected. It reserves time for a final checkpoint and 20 final trials, imposes an absolute deadline, and releases its sleep assertion on exit. Failures are recorded; the runner attempts an emergency checkpoint. If the process becomes unresponsive, the supervisor terminates it after a grace period; the latest completed checkpoint remains available. Saving after a hard crash cannot be guaranteed.

## Experiment

Resume the final seven-action PPO checkpoint from the preceding recovery session. The architecture, reward coefficients, screen observations and optimizer settings remain unchanged. The experimental change is a training reset curriculum:

- First 60 active minutes: 75% goal-practice resets and 25% normal starts.
- Thereafter: 10% practice resets and 90% normal starts.
- Practice resets split between approaching the goal at x=2585 and a missed-goal state at x=2792. A validated fixed action prefix recreates each state. PPO does not train on the prefix actions or receive its rewards. This is a curriculum aid, not a demonstration that the agent learned the prefix.
- Checkpoints approximately every 15 active minutes, with the usual five trials from the normal level start. All beginnings, endings, traces and failures remain archived.
- Final frozen checkpoint: one acceptance evaluation with the 20 new predetermined seeds 9101 through 9120. Pass requires complete, valid results and at least 18 clears. Seeds change sampled actions on the same level; this does not establish generalization to other levels.

Active training time includes curriculum reset overhead. Scripted setup frames, setup decisions and setup elapsed time are tracked separately from policy-controlled frames and decisions. Practice clears never count toward full-level acceptance. The short smoke-update policy was discarded; the overnight run resumes the archived original checkpoint.

The absolute deadline and exact parent are recorded in [the plan](overnight-plan.json). [Curriculum validation](curriculum-validation.json) records the checks and source hashes. A six-hour cap is not a promise of learning success. No scoring-reward experiment or automatic extra training follows this budget.

## Running, stopping and resuming

Use the project virtual environment to invoke `scripts/overnight_supervisor.py --session NEW_SESSION --deadline-epoch UNIX_TIMESTAMP`. It invokes the existing session runner, takes its exclusive training lock, and saves a manifest with source and dependency identities. Do not start a second copy while the overnight session is active.

To stop the current experiment gracefully, create `sessions/2026-09-21-smb3-overnight-curriculum/STOP`. The runner saves and exits; a stop request skips further evaluations. To request termination externally, send SIGTERM to the supervisor PID recorded in its `.cache` JSON state file. Do not force-quit Python if a graceful stop is possible.

Resume only with a newly chosen budget and new session name, using a checkpoint listed in the previous manifest. There is no automatic restart or budget extension. Review the recorded curriculum phase before resuming: a new curriculum session otherwise starts its first-hour mixture again.

## Reports and publication

The runner generates local stage charts and comparison galleries after each evaluation. Visual explanations remain explicitly pending until clips are inspected. Final training summaries separate starting conditions. A separate scheduled review handles English analysis and GitHub publication; training and local preservation continue independently if that review or network access fails. No approval is needed inside the gameplay process. Publication failures must remain logged and must not trigger extra training or erase local results.
