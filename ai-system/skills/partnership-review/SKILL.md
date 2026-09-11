---
name: partnership-review
category: gtm
description: "Judge whether a partnership is producing and act on the answer."
output: "partnership-review.md"
used_by:
  - partnership-bd-agent
---

# Partnership Review

`gtm` · produces `partnership-review.md` · used by `partnership-bd-agent`

Judge whether a partnership is producing and act on the answer.

## Procedure
1. Compare actual results against the metrics in the agreement.
2. Separate partner underperformance from thesis failure.
3. Check whether our side delivered its commitments before blaming theirs.
4. Decide: invest more, maintain, restructure, or exit.
5. Close dead partnerships explicitly rather than letting them decay.

## Output contract
`partnership-review.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Our own delivery assessed first
- Explicit decision, including exit
- The output states its confidence grade and names the evidence behind every load-bearing claim.
