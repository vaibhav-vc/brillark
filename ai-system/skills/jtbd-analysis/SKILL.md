---
name: jtbd-analysis
category: market
description: "Frame the problem as the job a customer hires a solution to do."
output: "jtbd.md"
used_by:
  - business-head
  - jtbd-analyst
---

# Jtbd Analysis

**Category:** `market` · **Output artifact:** `jtbd.md`

## What this skill does
Frame the problem as the job a customer hires a solution to do.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `business-head`, `jtbd-analyst`.

## Procedure
1. Write jobs as: when [situation], I want to [motivation], so I can [outcome].
2. Ground every job in a quoted customer statement.
3. Distinguish functional, emotional, and social dimensions of the job.
4. Identify what the customer currently hires and what they would have to fire.
5. Rank jobs by importance and current dissatisfaction.

## Output contract
Write `jtbd.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** jtbd-analysis
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
- Every job traced to a quote
- Current solution being fired identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
