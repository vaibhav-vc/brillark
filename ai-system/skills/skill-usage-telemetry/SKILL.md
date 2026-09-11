---
name: skill-usage-telemetry
category: improvement
description: "Find out which skills are actually used."
output: "usage-report.md"
used_by:
  - skill-refiner
---

# Skill Usage Telemetry

**Category:** `improvement` · **Output artifact:** `usage-report.md`

## What this skill does
Find out which skills are actually used.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `skill-refiner`.

## Procedure
1. Count invocations per skill per cycle.
2. Separate skills referenced by agents from skills actually invoked.
3. Identify skills unused across three cycles.
4. Identify skills invoked but producing poor outcomes.
5. Publish usage so refinement targets reality.

## Output contract
Write `usage-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** skill-usage-telemetry
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
- Referenced distinguished from invoked
- Three cycles before declaring a skill unused
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
