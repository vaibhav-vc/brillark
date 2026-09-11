---
name: decision-readiness-review
category: research
description: "Check whether a decision has the evidence its consequence requires."
output: "readiness-review.md"
used_by:
  - chief-research-officer-agent
---

# Decision Readiness Review

`research` · produces `readiness-review.md` · used by `chief-research-officer-agent`

Check whether a decision has the evidence its consequence requires.

## Procedure
1. Identify the decision's class and its required standard of proof.
2. Assess the actual evidence behind each load-bearing claim.
3. Identify claims below the required grade.
4. Report honestly when the organisation is about to decide below its own standard.
5. Recommend: proceed, resolve the gap first, or waive with a recorded justification.

## Output contract
`readiness-review.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Load-bearing claims assessed against the required grade
- Below-standard decisions reported, not smoothed over
- The output states its confidence grade and names the evidence behind every load-bearing claim.
