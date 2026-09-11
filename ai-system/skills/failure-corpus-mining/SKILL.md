---
name: failure-corpus-mining
category: improvement
description: "Gather everything that went wrong into one place worth analysing."
output: "failure-corpus.md"
used_by:
  - failure-miner
---

# Failure Corpus Mining

`improvement` · produces `failure-corpus.md` · used by `failure-miner`

Gather everything that went wrong into one place worth analysing.

## Procedure
1. Collect from incidents, rejected handoffs, Council blockers, escaped defects, and retrospectives.
2. Include the failures nobody filed formally, found in escalations and rework.
3. Normalise into a common record so they can be compared.
4. Record the cost and the stage at which each was caught.
5. Keep the corpus across cycles so patterns become visible.

## Output contract
`failure-corpus.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Informal failures included, not just filed ones
- Catch stage recorded for each failure
- The output states its confidence grade and names the evidence behind every load-bearing claim.
