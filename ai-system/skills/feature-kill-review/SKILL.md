---
name: feature-kill-review
category: product
description: "Decide whether a shipped feature earned its place."
output: "feature-review.md"
used_by:
  - cpo-agent
---

# Feature Kill Review

`product` · produces `feature-review.md` · used by `cpo-agent`

Decide whether a shipped feature earned its place.

## Procedure
1. Compare actual usage and outcome against the success signal set before launch.
2. Check whether failure is due to the feature or to its discovery.
3. Assess the maintenance cost of keeping it.
4. Decide to fix, keep, or remove — default to removal when the signal missed.
5. Record the decision and the evidence for the pattern library.

## Output contract
`feature-review.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Compared against the pre-set signal
- Removal is the default on a miss
- The output states its confidence grade and names the evidence behind every load-bearing claim.
