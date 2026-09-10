---
name: segmentation-analysis
category: market
description: "Divide the market into groups that behave differently and can be served differently."
output: "segmentation.md"
used_by:
  - market-researcher
---

# Segmentation Analysis

**Category:** `market` · **Output artifact:** `segmentation.md`

## What this skill does
Divide the market into groups that behave differently and can be served differently.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `market-researcher`.

## Procedure
1. Segment on behaviour and needs, not only on firmographics.
2. Test that segments differ on something that changes how we sell or build.
3. Size each segment and estimate its reachability.
4. Score attractiveness: pain intensity, budget, accessibility, and competition.
5. Recommend one segment to start with and state why the others wait.

## Output contract
Write `segmentation.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** segmentation-analysis
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
- Segments differ behaviourally, not just demographically
- One starting segment recommended
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
