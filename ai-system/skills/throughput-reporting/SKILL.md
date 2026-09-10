---
name: throughput-reporting
category: orchestration
description: "Measure how much work actually completes per cycle so capacity claims can be checked."
output: "throughput-report.md"
used_by:
  - progress-tracker
---

# Throughput Reporting

**Category:** `orchestration` · **Output artifact:** `throughput-report.md`

## What this skill does
Measure how much work actually completes per cycle so capacity claims can be checked.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `progress-tracker`.

## Procedure
1. Count completed tasks that passed their DoD, not tasks started.
2. Normalise by task size class so the count means something.
3. Report the trend over at least three cycles.
4. Separate rework from new work; rework is a quality signal.
5. Use the trend, not a single cycle, for capacity planning.

## Output contract
Write `throughput-report.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** throughput-reporting
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
- Only DoD-passed work counted
- Rework separated from new work
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
