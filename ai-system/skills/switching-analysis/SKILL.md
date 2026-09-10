---
name: switching-analysis
category: market
description: "Understand what it costs a customer to change, and who bears that cost."
output: "switching-analysis.md"
used_by:
  - jtbd-analyst
---

# Switching Analysis

**Category:** `market` · **Output artifact:** `switching-analysis.md`

## What this skill does
Understand what it costs a customer to change, and who bears that cost.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `jtbd-analyst`.

## Procedure
1. List the switching costs: data migration, retraining, contract, and political risk.
2. Identify who inside the customer bears each cost.
3. Estimate the value gain required to outweigh them.
4. Design a specific reduction for the largest switching cost.
5. Verify against real switching stories rather than assumption.

## Output contract
Write `switching-analysis.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** switching-analysis
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
- Switching costs quantified
- Reduction designed for the largest cost
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
