---
name: cycle-time-optimisation
category: gtm
description: "Make the loop turn faster, not just convert better."
output: "cycle-time-optimisation.md"
used_by:
  - growth-loop-designer
---

# Cycle Time Optimisation

**Category:** `gtm` · **Output artifact:** `cycle-time-optimisation.md`

## What this skill does
Make the loop turn faster, not just convert better.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `growth-loop-designer`.

## Procedure
1. Measure the elapsed time at each loop step.
2. Identify waiting steps that add no value.
3. Remove or parallelise the largest delay.
4. Verify the shortened cycle did not reduce conversion.
5. Re-project growth with the new cycle time.

## Output contract
Write `cycle-time-optimisation.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** cycle-time-optimisation
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
- Conversion checked after shortening
- Growth re-projected with new timing
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
