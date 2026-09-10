---
name: loop-instrumentation
category: gtm
description: "Measure a growth loop so optimisation is not guesswork."
output: "loop-instrumentation.md"
used_by:
  - growth-loop-designer
---

# Loop Instrumentation

**Category:** `gtm` · **Output artifact:** `loop-instrumentation.md`

## What this skill does
Measure a growth loop so optimisation is not guesswork.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `growth-loop-designer`.

## Procedure
1. Define an event for every step of the loop.
2. Instrument step conversion and step duration separately.
3. Attribute new users back to the loop step that produced them.
4. Build the dashboard that shows amplification over time.
5. Verify the instrumentation against a known cohort before trusting it.

## Output contract
Write `loop-instrumentation.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** loop-instrumentation
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
- Duration measured alongside conversion
- Instrumentation validated against a known cohort
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
