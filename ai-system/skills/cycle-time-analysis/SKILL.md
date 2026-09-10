---
name: cycle-time-analysis
category: orchestration
description: "Find where time actually goes between request and delivery."
output: "cycle-time-report.md"
used_by:
  - progress-tracker
---

# Cycle Time Analysis

**Category:** `orchestration` · **Output artifact:** `cycle-time-report.md`

## What this skill does
Find where time actually goes between request and delivery.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `progress-tracker`.

## Procedure
1. Measure end-to-end elapsed time, including waiting.
2. Break it into active work, waiting for input, and waiting for review.
3. Identify the largest waiting segment — it is usually not the work itself.
4. Attack the largest segment with a process change.
5. Re-measure to confirm the change moved the total, not just one segment.

## Output contract
Write `cycle-time-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cycle-time-analysis
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
- Waiting time measured separately
- Improvement verified end to end
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
