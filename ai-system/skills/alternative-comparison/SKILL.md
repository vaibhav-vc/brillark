---
name: alternative-comparison
category: market
description: "Compare against what the customer would actually do instead."
output: "alternative-comparison.md"
used_by:
  - value-proposition-designer
---

# Alternative Comparison

**Category:** `market` · **Output artifact:** `alternative-comparison.md`

## What this skill does
Compare against what the customer would actually do instead.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `value-proposition-designer`.

## Procedure
1. Identify the real alternative for each segment, including doing nothing.
2. Compare on cost, effort, risk, and outcome — not on features.
3. Be honest where the alternative is better.
4. Quantify the net advantage.
5. State the conditions under which the alternative wins.

## Output contract
Write `alternative-comparison.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** alternative-comparison
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
- Doing nothing included
- Conditions where we lose stated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
