---
name: work-breakdown-structure
category: orchestration
description: "Produce the hierarchy from objective to epic to task, so nothing falls between levels."
output: "wbs.md"
used_by:
  - planning-decomposer
---

# Work Breakdown Structure

`orchestration` · produces `wbs.md` · used by `planning-decomposer`

Produce the hierarchy from objective to epic to task, so nothing falls between levels.

## Procedure
1. State the objective and its acceptance condition at the top.
2. Break into outcome-level branches that could each be owned by one head.
3. Break branches into deliverables, then into single-run tasks.
4. Check for gaps: does completing all children actually complete the parent?
5. Check for overlap: no deliverable may appear under two parents.

## Output contract
`wbs.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Children fully cover their parent
- No deliverable appears twice
- The output states its confidence grade and names the evidence behind every load-bearing claim.
