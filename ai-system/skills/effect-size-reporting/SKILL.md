---
name: effect-size-reporting
category: improvement
description: "Report how much better, not just whether better."
output: "effect-report.md"
used_by:
  - ab-test-runner
---

# Effect Size Reporting

`improvement` · produces `effect-report.md` · used by `ab-test-runner`

Report how much better, not just whether better.

## Procedure
1. Report the absolute and relative change with the sample size.
2. Report variability, not just the central estimate.
3. State whether the effect is large enough to be worth the churn.
4. Report the cases that got worse alongside those that improved.
5. Avoid claiming significance the sample cannot support.

## Output contract
`effect-report.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Cases that got worse reported too
- Practical worth stated, not just direction
- The output states its confidence grade and names the evidence behind every load-bearing claim.
