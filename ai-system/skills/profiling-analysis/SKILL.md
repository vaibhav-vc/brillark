---
name: profiling-analysis
category: engineering
description: "Find where time and resources actually go."
output: "profile-report.md"
used_by:
  - performance-engineer
---

# Profiling Analysis

`engineering` · produces `profile-report.md` · used by `performance-engineer`

Find where time and resources actually go.

## Procedure
1. Reproduce the slow case reliably before profiling.
2. Profile the real workload rather than a synthetic loop.
3. Identify the largest contributor, not the most interesting one.
4. Verify the hypothesis by changing one thing and re-measuring.
5. Stop when the budget is met; further optimisation is unpaid work.

## Output contract
`profile-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Real workload profiled
- Hypothesis verified by re-measurement
- The output states its confidence grade and names the evidence behind every load-bearing claim.
