---
name: blocker-detection
category: orchestration
description: "Find work that has stopped moving before someone reports it."
output: "blocker-report.md"
used_by:
  - progress-tracker
---

# Blocker Detection

`orchestration` · produces `blocker-report.md` · used by `progress-tracker`

Find work that has stopped moving before someone reports it.

## Procedure
1. Compare each task's elapsed time against its expected duration.
2. Flag tasks with no artifact change since the last check.
3. Distinguish blocked from not-started from slow.
4. Identify the specific missing input or decision for each blocker.
5. Age every blocker and escalate on the age threshold.

## Output contract
`blocker-report.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Blocked distinguished from slow
- Each blocker names its missing input
- The output states its confidence grade and names the evidence behind every load-bearing claim.
