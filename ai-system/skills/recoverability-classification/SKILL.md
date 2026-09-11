---
name: recoverability-classification
category: council
description: "Separate the failures you can come back from."
output: "recoverability-report.md"
used_by:
  - council-risk-and-failure-modes
---

# Recoverability Classification

`council` · produces `recoverability-report.md` · used by `council-risk-and-failure-modes`

Separate the failures you can come back from.

## Procedure
1. Classify each failure as recoverable, costly but survivable, or terminal.
2. For recoverable failures, estimate the recovery cost and time.
3. For terminal failures, verify the classification rigorously.
4. Apply proportionate caution: terminal risks justify slower, safer choices.
5. Ensure no terminal risk is accepted without an explicit decision.

## Output contract
`recoverability-report.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Terminal classifications rigorously verified
- No terminal risk accepted implicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
