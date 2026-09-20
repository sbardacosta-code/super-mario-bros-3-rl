# Completion first, game score second

## Acceptance target

The completion baseline must win **at least 18 of 20 final evaluation trials (90%)** on World 1-1. A win requires collecting the goal card and triggering the validated level-clear transition. A death, timeout, or reaching the right edge without collecting the card is not a win. Incomplete or invalid evaluations cannot pass the target.

Select and freeze the candidate checkpoint before running the 20-trial acceptance evaluation. Document the action set, reward, start state, wrappers, episode limit and stochastic evaluation mode. Use 20 distinct, predetermined action seeds. They vary action sampling on the same level; they do not create 20 levels or 20 independent training runs. Do not pick the best 20 outcomes from a larger batch or silently retry failed seeds. If the policy is changed after inspecting the final trials, use a newly declared final seed set.

18/20 is a practical classroom acceptance rule, not proof that the underlying win probability is at least 90%. Report every result and supplement the final test with additional seeds or held-out conditions, explaining their limitations. Finishing time is reported for successful trials only; progress and shaped reward remain separate diagnostics.

## Experiment sequence

1. **Preserve the original experiment.** Its five-action policy and all training stages remain archived, including the 45-minute regression. Its final evaluation was 0/15, so it is an experimental reference, not an accepted completion baseline.
2. **Test recovery controls.** Create a new versioned configuration that includes leftward recovery actions. Validate movement, jumps, resets, observations, reward reuse, goal-card collection and termination. Reproduce a missed-card situation and test returning to it. Changing the action count changes the policy output size; do not silently load the old policy as if it were an identical continuation. Prefer a fresh PPO policy, or explicitly document and test any transfer procedure.
3. **Run a bounded pilot before a longer budget.** Keep the existing reward initially so the control change can be interpreted. Measure runtime and evaluate the untrained and hold-run-right baselines. Retain 15-minute milestones during any subsequently approved longer run, with comparable GIFs and all failures.
4. **Assess the frozen policy.** Apply the 18/20 acceptance test and additional checks. If it fails, investigate the evidence before choosing the next change. More training is not automatically the answer.

## Later experiment: maximize game score

Only after a policy meets the completion target, preserve it as the completion baseline and create a separate score-oriented experiment. Report actual game score, completion rate and successful finishing times together. A score increase that sacrifices reliable completion must be visible. Specify how score enters the reward and test for repeatable point-farming exploits before training. Do not rewrite the earlier completion experiment or its rewards.

The user approved this direction. This update does not launch training or assume a new hour-long budget. All work remains local, with no paid cloud services and no GPT/API calls in gameplay.
