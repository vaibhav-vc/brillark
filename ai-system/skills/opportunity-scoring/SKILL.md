---
name: opportunity-scoring
category: market
description: "Rank problems by how much unclaimed value they contain."
output: "opportunity-scores.md"
used_by:
  - jtbd-analyst
---

# Opportunity Scoring

**Category:** `market` · **Output artifact:** `opportunity-scores.md`

## What this skill does
Rank problems by how much unclaimed value they contain.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `jtbd-analyst`.

## Procedure
1. Score each job or outcome on importance and current satisfaction.
2. Compute opportunity as importance plus unmet gap.
3. Weight by the number of customers who share it.
4. Cross-check high scores against willingness to pay.
5. Rank and recommend the top two, with the reason the rest wait.

## Output contract
Write `opportunity-scores.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** opportunity-scoring
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
- Scores validated against willingness to pay
- Ranked with explicit deferrals
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
