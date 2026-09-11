---
name: duplicate-review-elimination
category: improvement
description: "Remove reviews that check the same thing twice."
output: "review-map.md"
used_by:
  - workflow-optimizer
---

# Duplicate Review Elimination

`improvement` · produces `review-map.md` · used by `workflow-optimizer`

Remove reviews that check the same thing twice.

## Procedure
1. Map every review step and what each checks.
2. Identify overlapping checks across steps.
3. Keep the review closest to where the defect originates.
4. Remove the duplicate rather than coordinating between them.
5. Watch for escaped defects after removal.

## Output contract
`review-map.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Review kept closest to defect origin
- Escaped defects watched after removal
- The output states its confidence grade and names the evidence behind every load-bearing claim.
