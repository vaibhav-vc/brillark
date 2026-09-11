---
name: performance-regression-gating
category: engineering
description: "Stop performance regressions from reaching production."
output: "perf-gate.md"
used_by:
  - performance-engineer
---

# Performance Regression Gating

`engineering` · produces `perf-gate.md` · used by `performance-engineer`

Stop performance regressions from reaching production.

## Procedure
1. Establish a stable baseline measurement environment.
2. Run the measurement on every change to critical paths.
3. Set the threshold above measurement noise to avoid false alarms.
4. Fail the build on a real regression and report the contributor.
5. Review the threshold when noise or hardware changes.

## Output contract
`perf-gate.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Threshold set above measurement noise
- Build fails on genuine regressions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
