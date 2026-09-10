---
name: outcome-metric-extraction
category: market
description: "Capture how the customer measures success, in their own terms."
output: "outcome-metrics.md"
used_by:
  - jtbd-analyst
---

# Outcome Metric Extraction

**Category:** `market` · **Output artifact:** `outcome-metrics.md`

## What this skill does
Capture how the customer measures success, in their own terms.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `jtbd-analyst`.

## Procedure
1. Ask what number changes if the problem is solved.
2. Capture their unit, their baseline, and their target.
3. Distinguish the metric they are measured on from the one they care about.
4. Check whether our product can actually move that number.
5. Use it as the success criterion in the value proposition.

## Output contract
Write `outcome-metrics.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** outcome-metric-extraction
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
- Metric expressed in the customer's own terms
- Product's ability to move it verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
