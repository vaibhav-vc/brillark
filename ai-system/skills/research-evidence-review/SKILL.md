---
name: research-evidence-review
category: design
description: "Check that a design decision rests on evidence rather than assertion."
output: "evidence-review.md"
used_by:
  - design-head
---

# Research Evidence Review

`design` · produces `evidence-review.md` · used by `design-head`

Check that a design decision rests on evidence rather than assertion.

## Procedure
1. Ask what evidence supports the central choice.
2. Check the evidence actually addresses this decision.
3. Check the sample and the method support the weight placed on it.
4. Identify the choices resting on assumption and flag the riskiest.
5. Require a cheap test for the riskiest unsupported choice.

## Output contract
`evidence-review.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Evidence checked for being on point
- Riskiest unsupported choice gets a test
- The output states its confidence grade and names the evidence behind every load-bearing claim.
