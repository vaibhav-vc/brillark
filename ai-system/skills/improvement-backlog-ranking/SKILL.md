---
name: improvement-backlog-ranking
category: improvement
description: "Decide what to improve next."
output: "improvement-backlog.md"
used_by:
  - improvement-head
---

# Improvement Backlog Ranking

`improvement` · produces `improvement-backlog.md` · used by `improvement-head`

Decide what to improve next.

## Procedure
1. Score each candidate by cost imposed, probability of fix, and effort.
2. Prefer systemic causes over individual symptoms.
3. Prefer changes that can be measured over those that cannot.
4. Fund fewer improvements properly rather than many partially.
5. Publish the ranking and the line.

## Output contract
`improvement-backlog.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Measurable changes preferred
- Systemic causes ranked above symptoms
- The output states its confidence grade and names the evidence behind every load-bearing claim.
