---
name: parallelisation-analysis
category: orchestration
description: "Find what can run at the same time and what genuinely cannot."
output: "parallelisation-plan.md"
used_by:
  - planning-decomposer
  - workflow-optimizer
---

# Parallelisation Analysis

`orchestration` · produces `parallelisation-plan.md` · used by `planning-decomposer`, `workflow-optimizer`

Find what can run at the same time and what genuinely cannot.

## Procedure
1. Map each task's true inputs; a dependency exists only where an output is consumed.
2. Separate hard dependencies from habitual sequencing.
3. Identify shared mutable state that would make parallel runs unsafe.
4. Group independent branches into parallel tracks with separate owners.
5. Estimate the schedule gain, and drop parallelisation that adds coordination cost for little gain.

## Output contract
`parallelisation-plan.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Only true input dependencies retained
- Shared-state hazards identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
