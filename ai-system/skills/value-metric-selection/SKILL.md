---
name: value-metric-selection
category: finance
description: "Choose the thing the price scales with."
output: "value-metric.md"
used_by:
  - pricing-strategist
---

# Value Metric Selection

**Category:** `finance` · **Output artifact:** `value-metric.md`

## What this skill does
Choose the thing the price scales with.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `pricing-strategist`.

## Procedure
1. List candidate metrics that correlate with customer value received.
2. Test each for predictability, transparency, and ease of measurement.
3. Check that it grows as the customer succeeds, not as they struggle.
4. Verify the customer can forecast their own bill.
5. Confirm it is measurable in the product before committing.

## Output contract
Write `value-metric.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** value-metric-selection
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
- Metric grows with customer success
- Customer can forecast their bill
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
