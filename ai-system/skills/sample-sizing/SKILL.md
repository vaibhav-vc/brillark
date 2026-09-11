---
name: sample-sizing
category: improvement
description: "Work out how many cases the trial needs."
output: "sample-plan.md"
used_by:
  - ab-test-runner
---

# Sample Sizing

`improvement` · produces `sample-plan.md` · used by `ab-test-runner`

Work out how many cases the trial needs.

## Procedure
1. State the smallest improvement that would be worth adopting.
2. Estimate the variability from previous runs.
3. Compute the sample needed to detect that effect reliably.
4. If the sample is unaffordable, say the trial cannot answer the question.
5. Never reduce the sample and keep the original claim.

## Output contract
`sample-plan.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Minimum worthwhile effect stated first
- Underpowered trials declared, not run anyway
- The output states its confidence grade and names the evidence behind every load-bearing claim.
