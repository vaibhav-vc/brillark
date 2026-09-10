---
name: price-testing
category: finance
description: "Change price in a way that produces evidence rather than damage."
output: "price-test.md"
used_by:
  - pricing-strategist
---

# Price Testing

**Category:** `finance` · **Output artifact:** `price-test.md`

## What this skill does
Change price in a way that produces evidence rather than damage.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `pricing-strategist`.

## Procedure
1. Define the hypothesis and the metric that decides it.
2. Test on new customers first to avoid damaging existing relationships.
3. Run long enough to see the retention effect, not just conversion.
4. Measure revenue per visitor, not conversion rate alone.
5. Decide on the pre-agreed criterion and record the outcome either way.

## Output contract
Write `price-test.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** price-testing
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
- Retention effect measured, not just conversion
- Decision made on the pre-agreed criterion
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
