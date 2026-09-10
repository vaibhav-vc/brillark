---
name: market-sizing
category: market
description: "Size a market bottom-up from countable inputs and sanity-check it top-down."
output: "market-sizing.md"
used_by:
  - market-researcher
---

# Market Sizing

**Category:** `market` · **Output artifact:** `market-sizing.md`

## What this skill does
Size a market bottom-up from countable inputs and sanity-check it top-down.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `market-researcher`.

## Procedure
1. Define the buyer unit and count how many exist in the target geography.
2. Estimate realistic annual spend per buyer from observed pricing or budgets.
3. Multiply to TAM, narrow to SAM by segment fit, and to SOM by actual channel reach.
4. Cross-check against a top-down source and explain any gap larger than 2x.
5. Name the three inputs the estimate is most sensitive to and grade each source.

## Output contract
Write `market-sizing.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** market-sizing
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
- Every figure traceable to a counted input
- SOM justified by a real channel
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
