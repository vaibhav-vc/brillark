---
name: waterfall-analysis
category: finance
description: "Show who gets what in an exit, in what order."
output: "waterfall.md"
used_by:
  - cap-table-steward
---

# Waterfall Analysis

**Category:** `finance` · **Output artifact:** `waterfall.md`

## What this skill does
Show who gets what in an exit, in what order.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cap-table-steward`.

## Procedure
1. List every security with its liquidation preference and participation rights.
2. Model the distribution stack in seniority order.
3. Compute proceeds by exit value across a realistic range.
4. Identify the value at which common shareholders receive nothing.
5. Highlight where preference stacking creates a misaligned incentive.

## Output contract
Write `waterfall.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** waterfall-analysis
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
- Distribution modelled across a value range
- Common-zero point identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
