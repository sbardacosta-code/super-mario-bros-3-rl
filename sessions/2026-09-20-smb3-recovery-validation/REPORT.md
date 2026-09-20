# Recovery-control validation — first attempt

Status: **failed validation gate; no training started from this attempt**. [Checks](validation.json) · [Configuration](config.json).

Left movement, left-jump, repeatable resets, death/clear detection, timeout, and scripted missed-card recovery passed. The real backtracking reward check failed because its test compared every subsequent high-water value to the value before turning. Inertia briefly increased the high-water mark, leaving no eligible samples. This is a test-selection error, not evidence of positive reward for revisiting ground.

The retry compares each decision to its immediately preceding high-water mark and checks that decisions without new progress have no positive reward. The environment and reward were not changed. [Corrected validation](../2026-09-20-smb3-recovery-validation-02/REPORT.md).
