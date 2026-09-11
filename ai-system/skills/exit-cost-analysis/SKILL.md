---
name: exit-cost-analysis
category: research
description: "Know what it would take to leave before you commit."
output: "exit-analysis.md"
used_by:
  - technology-evaluator
---

# Exit Cost Analysis

`research` · produces `exit-analysis.md` · used by `technology-evaluator`

Know what it would take to leave before you commit.

## Procedure
1. Identify what would have to be rebuilt, migrated, or renegotiated.
2. Check data portability and export formats in practice, not in the brochure.
3. Estimate the engineering time and the calendar time to exit.
4. Identify contractual lock-in: notice periods, minimums, and penalties.
5. Record the exit cost alongside the recommendation.

## Output contract
`exit-analysis.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Data portability verified in practice
- Exit cost recorded with the recommendation
- The output states its confidence grade and names the evidence behind every load-bearing claim.
