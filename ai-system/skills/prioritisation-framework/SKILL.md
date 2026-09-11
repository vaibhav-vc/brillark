---
name: prioritisation-framework
category: product
description: "Apply one consistent method to decide what gets built next."
output: "prioritisation.md"
used_by:
  - cpo-agent
---

# Prioritisation Framework

`product` · produces `prioritisation.md` · used by `cpo-agent`

Apply one consistent method to decide what gets built next.

## Procedure
1. Score each candidate on evidence of pain, reach, and strategic fit.
2. Divide by cost to learn, not cost to build fully.
3. Apply the same method to every candidate, including the CEO's.
4. Publish the scores so the ranking can be argued with facts.
5. Recalibrate when a shipped item's outcome contradicts its score.

## Output contract
`prioritisation.md` → `workspace/<venture-id>/product/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/product.tsv`.

## Quality bar
- Same method applied to every candidate
- Scores published and challengeable
- The output states its confidence grade and names the evidence behind every load-bearing claim.
