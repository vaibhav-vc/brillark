---
name: residual-uncertainty-statement
category: research
description: "Say plainly what the research did not establish."
output: "uncertainty-statement.md"
used_by:
  - research-analyst
---

# Residual Uncertainty Statement

`research` · produces `uncertainty-statement.md` · used by `research-analyst`

Say plainly what the research did not establish.

## Procedure
1. List the sub-questions that remain unanswered after the search.
2. State whether absence of evidence here is informative or just absence.
3. State what would resolve each remaining unknown, and roughly what it would cost.
4. State how the unknowns would change the answer if resolved unfavourably.
5. Put this in the brief's body, not in a footnote.

## Output contract
`uncertainty-statement.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Informative absence distinguished from mere absence
- Cost of resolving each unknown estimated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
