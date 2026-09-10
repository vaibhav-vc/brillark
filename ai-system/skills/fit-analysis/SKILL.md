---
name: fit-analysis
category: market
description: "Assess honestly whether the offer matches the customer profile."
output: "fit-analysis.md"
used_by:
  - value-proposition-designer
---

# Fit Analysis

**Category:** `market` · **Output artifact:** `fit-analysis.md`

## What this skill does
Assess honestly whether the offer matches the customer profile.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `value-proposition-designer`.

## Procedure
1. Compare the ranked pains against the ranked relievers.
2. Check that the top pain has a strong reliever, not just any pain.
3. Identify mismatches where we solve problems nobody ranked highly.
4. Rate the overall fit and name the weakest link.
5. Recommend either a product change or a segment change.

## Output contract
Write `fit-analysis.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** fit-analysis
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
- Top-ranked pain addressed, not just any pain
- Weakest link named
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
