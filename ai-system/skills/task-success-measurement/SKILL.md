---
name: task-success-measurement
category: design
description: "Measure whether people can actually complete the task."
output: "task-metrics.md"
used_by:
  - usability-tester
---

# Task Success Measurement

`design` · produces `task-metrics.md` · used by `usability-tester`

Measure whether people can actually complete the task.

## Procedure
1. Record completion, assisted completion, and failure as distinct outcomes.
2. Time the task and note where the time actually went.
3. Count errors and whether the participant recovered unaided.
4. Report rates with the sample size visible.
5. Compare against the prior round rather than an absolute target.

## Output contract
`task-metrics.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Assisted completion counted separately from success
- Sample size reported with every rate
- The output states its confidence grade and names the evidence behind every load-bearing claim.
