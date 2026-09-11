---
name: currency-and-retraction-check
category: research
description: "Confirm the source is still true, not just still published."
output: "currency-check.md"
used_by:
  - source-verifier
---

# Currency And Retraction Check

`research` · produces `currency-check.md` · used by `source-verifier`

Confirm the source is still true, not just still published.

## Procedure
1. Check the publication date and whether the underlying conditions persist.
2. Check for corrections, retractions, or superseding editions.
3. Check whether cited data has been revised since publication.
4. Flag figures whose shelf life has expired for the decision at hand.
5. Record the check date so the next reader knows how fresh this assessment is.

## Output contract
`currency-check.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Retractions and revisions checked
- Assessment carries its own check date
- The output states its confidence grade and names the evidence behind every load-bearing claim.
