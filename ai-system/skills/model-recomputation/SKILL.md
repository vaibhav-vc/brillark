---
name: model-recomputation
category: council
description: "Independently recompute a model's headline numbers before critiquing them."
output: "recomputation-report.md"
used_by:
  - council-economics-skeptic
---

# Model Recomputation

`council` · produces `recomputation-report.md` · used by `council-economics-skeptic`

Independently recompute a model's headline numbers before critiquing them.

## Procedure
1. Rebuild the top three outputs from the stated inputs without looking at the original formulas.
2. Compare your result to the model's; investigate any difference.
3. Check the arithmetic of every percentage, ratio, and growth rate.
4. Verify that units and time periods are consistent throughout.
5. Report discrepancies with the corrected figure, not just the objection.

## Output contract
`recomputation-report.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Rebuilt independently of the original formulas
- Discrepancies reported with corrected figures
- The output states its confidence grade and names the evidence behind every load-bearing claim.
