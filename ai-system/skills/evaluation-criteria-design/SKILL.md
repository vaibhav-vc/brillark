---
name: evaluation-criteria-design
category: research
description: "Decide what matters before looking at any candidate."
output: "evaluation-criteria.md"
used_by:
  - technology-evaluator
---

# Evaluation Criteria Design

`research` · produces `evaluation-criteria.md` · used by `technology-evaluator`

Decide what matters before looking at any candidate.

## Procedure
1. Derive criteria from stated requirements and constraints.
2. Separate hard requirements from weighted preferences.
3. Assign weights by consequence and record them before scoring.
4. Include operational criteria: maintenance, support, and exit.
5. Freeze the criteria before candidates are reviewed.

## Output contract
`evaluation-criteria.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Weights recorded before any candidate is scored
- Hard requirements separated from preferences
- The output states its confidence grade and names the evidence behind every load-bearing claim.
