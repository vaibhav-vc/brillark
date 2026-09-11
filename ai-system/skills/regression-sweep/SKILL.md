---
name: regression-sweep
category: improvement
description: "Check the change did not break something else."
output: "regression-sweep.md"
used_by:
  - improvement-head
  - prompt-optimizer
---

# Regression Sweep

`improvement` · produces `regression-sweep.md` · used by `improvement-head`, `prompt-optimizer`

Check the change did not break something else.

## Procedure
1. Run the full evaluation suite, not only the targeted cases.
2. Compare per case, since aggregates hide offsetting changes.
3. Investigate every case that moved down, however small.
4. Block adoption on an unexplained regression.
5. Record accepted regressions with an explicit justification.

## Output contract
`regression-sweep.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Per-case comparison, not aggregate only
- Unexplained regressions block adoption
- The output states its confidence grade and names the evidence behind every load-bearing claim.
