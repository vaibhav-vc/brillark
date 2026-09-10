---
name: filing-calendar
category: finance
description: "Make sure no statutory deadline is missed."
output: "filing-calendar.md"
used_by:
  - corporate-secretary-agent
  - tax-and-compliance-finance
---

# Filing Calendar

**Category:** `finance` · **Output artifact:** `filing-calendar.md`

## What this skill does
Make sure no statutory deadline is missed.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `corporate-secretary-agent`, `tax-and-compliance-finance`.

## Procedure
1. List every filing obligation with its jurisdiction and frequency.
2. Record the statutory deadline and the internal deadline that precedes it.
3. Assign an owner and a preparer to each.
4. Set reminders with enough lead time to actually prepare.
5. Record completion with the confirmation reference.

## Output contract
Write `filing-calendar.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** filing-calendar
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
- Internal deadlines precede statutory ones
- Completion recorded with a reference
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
