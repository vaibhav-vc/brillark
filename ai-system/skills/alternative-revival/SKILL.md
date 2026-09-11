---
name: alternative-revival
category: council
description: "Check whether a discarded option deserves reconsideration."
output: "alternative-review.md"
used_by:
  - council-devils-advocate
---

# Alternative Revival

`council` · produces `alternative-review.md` · used by `council-devils-advocate`

Check whether a discarded option deserves reconsideration.

## Procedure
1. Review why each alternative was rejected and when.
2. Check whether the rejecting condition still holds today.
3. Identify alternatives rejected for reasons that have since changed.
4. Re-score the survivors against the current recommendation.
5. Recommend revival only where the evidence genuinely changed.

## Output contract
`alternative-review.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Rejection reasons re-tested against current facts
- Revival justified by changed evidence
- The output states its confidence grade and names the evidence behind every load-bearing claim.
