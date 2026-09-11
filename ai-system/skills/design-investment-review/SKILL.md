---
name: design-investment-review
category: design
description: "Judge whether design effort is going where it pays."
output: "investment-review.md"
used_by:
  - chief-design-officer-agent
---

# Design Investment Review

`design` · produces `investment-review.md` · used by `chief-design-officer-agent`

Judge whether design effort is going where it pays.

## Procedure
1. List where design effort actually went last cycle.
2. Compare against the surfaces that most affect customer outcomes.
3. Identify effort spent on internal preference rather than customer outcome.
4. Identify high-impact surfaces receiving no attention.
5. Reallocate explicitly and state what is being deprioritised.

## Output contract
`investment-review.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Effort compared against outcome impact
- Deprioritised work stated explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
