---
name: evidence-grading
category: council
description: "Rate how well each claim is actually supported."
output: "evidence-grades.md"
used_by:
  - council-assumption-auditor
---

# Evidence Grading

`council` · produces `evidence-grades.md` · used by `council-assumption-auditor`

Rate how well each claim is actually supported.

## Procedure
1. Assign one grade per claim: measured, sourced, benchmarked, estimated, or guessed.
2. Require a reference for any grade above 'estimated'.
3. Check that the evidence actually supports the specific claim made.
4. Downgrade claims where the evidence is adjacent but not on point.
5. Report the proportion of the plan resting on guesses.

## Output contract
`evidence-grades.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Evidence checked for being on point
- Proportion resting on guesses reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.
