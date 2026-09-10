---
name: work-breakdown-structure
category: orchestration
description: "Produce the hierarchy from objective to epic to task, so nothing falls between levels."
output: "wbs.md"
used_by:
  - planning-decomposer
---

# Work Breakdown Structure

**Category:** `orchestration` · **Output artifact:** `wbs.md`

## What this skill does
Produce the hierarchy from objective to epic to task, so nothing falls between levels.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `planning-decomposer`.

## Procedure
1. State the objective and its acceptance condition at the top.
2. Break into outcome-level branches that could each be owned by one head.
3. Break branches into deliverables, then into single-run tasks.
4. Check for gaps: does completing all children actually complete the parent?
5. Check for overlap: no deliverable may appear under two parents.

## Output contract
Write `wbs.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** work-breakdown-structure
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Children fully cover their parent
- No deliverable appears twice
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
