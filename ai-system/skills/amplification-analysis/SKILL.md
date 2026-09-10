---
name: amplification-analysis
category: gtm
description: "Determine whether a loop actually compounds."
output: "amplification-analysis.md"
used_by:
  - growth-loop-designer
---

# Amplification Analysis

**Category:** `gtm` · **Output artifact:** `amplification-analysis.md`

## What this skill does
Determine whether a loop actually compounds.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `growth-loop-designer`.

## Procedure
1. Compute how many new inputs each output generates.
2. Measure the cycle time from input to new input.
3. Project growth from amplification and cycle time together.
4. Identify whether amplification is stable, decaying, or saturating.
5. State the level at which the loop stalls and why.

## Output contract
Write `amplification-analysis.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** amplification-analysis
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
- Cycle time included in the projection
- Saturation point identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
