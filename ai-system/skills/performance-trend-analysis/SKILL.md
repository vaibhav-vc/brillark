---
name: performance-trend-analysis
category: improvement
description: "Distinguish a real trend from noise before acting on it."
output: "trend-report.md"
used_by:
  - agent-performance-analyst
---

# Performance Trend Analysis

**Category:** `improvement` · **Output artifact:** `trend-report.md`

## What this skill does
Distinguish a real trend from noise before acting on it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `agent-performance-analyst`.

## Procedure
1. Collect at least three cycles of comparable measurements.
2. Separate changes in performance from changes in the task mix.
3. Check whether the measurement itself changed between cycles.
4. Report direction with the variance, not a single number.
5. Act only on trends that survive all three checks.

## Output contract
Write `trend-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** performance-trend-analysis
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
- At least three cycles before calling a trend
- Task-mix changes separated from performance changes
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
