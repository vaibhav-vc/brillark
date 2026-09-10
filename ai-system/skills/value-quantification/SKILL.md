---
name: value-quantification
category: market
description: "Put a number on the value delivered and show the arithmetic."
output: "value-quantification.md"
used_by:
  - value-proposition-designer
---

# Value Quantification

**Category:** `market` · **Output artifact:** `value-quantification.md`

## What this skill does
Put a number on the value delivered and show the arithmetic.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `value-proposition-designer`.

## Procedure
1. Identify the customer's measurable outcome: time, cost, revenue, or risk.
2. Establish the baseline from the customer's current state.
3. Compute the improvement with conservative assumptions.
4. Show the arithmetic so the customer can check it with their own numbers.
5. Compare the value against the price to show the ratio.

## Output contract
Write `value-quantification.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** value-quantification
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
- Arithmetic shown and checkable
- Conservative assumptions used
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
