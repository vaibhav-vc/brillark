---
name: performance-trend-analysis
category: improvement
description: "Distinguish a real trend from noise before acting on it."
output: "trend-report.md"
used_by:
  - agent-performance-analyst
---

# Performance Trend Analysis

`improvement` · produces `trend-report.md` · used by `agent-performance-analyst`

Distinguish a real trend from noise before acting on it.

## Procedure
1. Collect at least three cycles of comparable measurements.
2. Separate changes in performance from changes in the task mix.
3. Check whether the measurement itself changed between cycles.
4. Report direction with the variance, not a single number.
5. Act only on trends that survive all three checks.

## Output contract
`trend-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- At least three cycles before calling a trend
- Task-mix changes separated from performance changes
- The output states its confidence grade and names the evidence behind every load-bearing claim.
