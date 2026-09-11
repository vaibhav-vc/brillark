---
name: dark-pattern-audit
category: council
description: "Find design that works against the user's interest."
output: "dark-pattern-audit.md"
used_by:
  - council-ethics-and-responsibility
---

# Dark Pattern Audit

`council` · produces `dark-pattern-audit.md` · used by `council-ethics-and-responsibility`

Find design that works against the user's interest.

## Procedure
1. Review sign-up, purchase, and cancellation flows for asymmetry.
2. Check whether cancelling is as easy as subscribing.
3. Look for hidden costs, pre-selected options, and confusing negatives.
4. Check whether urgency and scarcity claims are true.
5. Report each with the specific screen and the honest alternative.

## Output contract
`dark-pattern-audit.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Cancellation symmetry checked
- Honest alternative proposed per finding
- The output states its confidence grade and names the evidence behind every load-bearing claim.
