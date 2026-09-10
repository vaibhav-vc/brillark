---
name: competitive-landscape-mapping
category: market
description: "Map everyone competing for the same budget, including the ones nobody counts."
output: "competitive-map.md"
used_by:
  - competitor-intel-analyst
---

# Competitive Landscape Mapping

**Category:** `market` · **Output artifact:** `competitive-map.md`

## What this skill does
Map everyone competing for the same budget, including the ones nobody counts.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `competitor-intel-analyst`.

## Procedure
1. List direct competitors, indirect alternatives, and the status quo.
2. Include internal tools, spreadsheets, and doing nothing — usually the real incumbent.
3. Position each on the dimensions customers actually use to choose.
4. Note each competitor's apparent segment focus and business model.
5. Identify the whitespace and check whether it is empty for a good reason.

## Output contract
Write `competitive-map.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** competitive-landscape-mapping
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
- Status quo included as a competitor
- Whitespace tested for why it is empty
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
