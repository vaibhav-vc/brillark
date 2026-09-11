---
name: analysis-test-correlation
category: hardware
description: "Check the simulation actually predicted reality."
output: "correlation-report.md"
used_by:
  - mechanical-engineer
---

# Analysis Test Correlation

`hardware` · produces `correlation-report.md` · used by `mechanical-engineer`

Check the simulation actually predicted reality.

## Procedure
1. Instrument the physical test to measure what the model predicted.
2. Compare predicted and measured values, not just pass and fail.
3. Investigate discrepancies rather than adjusting the model to match.
4. Record the correlation so future analyses can be trusted proportionally.
5. State the model's demonstrated accuracy when reporting future results.

## Output contract
`correlation-report.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Predicted and measured values compared directly
- Model accuracy stated in future reports
- The output states its confidence grade and names the evidence behind every load-bearing claim.
