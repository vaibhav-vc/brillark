---
name: comparison-matrix
category: market
description: "Compare alternatives on the dimensions that decide purchases."
output: "comparison-matrix.md"
used_by:
  - competitor-intel-analyst
---

# Comparison Matrix

**Category:** `market` · **Output artifact:** `comparison-matrix.md`

## What this skill does
Compare alternatives on the dimensions that decide purchases.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `competitor-intel-analyst`.

## Procedure
1. Derive dimensions from customer interviews, not from our feature list.
2. Score each alternative honestly, including where we lose.
3. Weight dimensions by how much they influence the decision.
4. Show the weighted result and the dimension that decides most cases.
5. Update when a competitor ships something material.

## Output contract
Write `comparison-matrix.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** comparison-matrix
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
- Dimensions derived from customer language
- Losses recorded honestly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
