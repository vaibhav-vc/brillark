---
name: trial-execution
category: improvement
description: "Run the comparison cleanly."
output: "trial-results.md"
used_by:
  - ab-test-runner
---

# Trial Execution

`improvement` · produces `trial-results.md` · used by `ab-test-runner`

Run the comparison cleanly.

## Procedure
1. Run baseline and variant on identical cases in identical conditions.
2. Run the full planned sample before looking at results.
3. Record every run, including the failed and the anomalous ones.
4. Compute the effect size and its variability.
5. Re-run any result that would change a decision.

## Output contract
`trial-results.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Full planned sample run before inspection
- Decision-changing results re-run
- The output states its confidence grade and names the evidence behind every load-bearing claim.
