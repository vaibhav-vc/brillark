---
name: growth-loop-design
category: gtm
description: "Design a mechanism where output feeds back into input so growth compounds."
output: "growth-loop.md"
used_by:
  - growth-loop-designer
---

# Growth Loop Design

**Category:** `gtm` · **Output artifact:** `growth-loop.md`

## What this skill does
Design a mechanism where output feeds back into input so growth compounds.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `growth-loop-designer`.

## Procedure
1. Draw the loop end to end, labelling every step's conversion rate and duration.
2. Compute the amplification factor; below 1.0 it is a funnel, not a loop.
3. Identify the step with the largest drop and the longest delay.
4. Check the loop does not degrade the experience for existing users.
5. State the input required to start the loop and what sustains it.

## Output contract
Write `growth-loop.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** growth-loop-design
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
- Amplification factor computed, not assumed
- Existing-user impact assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
