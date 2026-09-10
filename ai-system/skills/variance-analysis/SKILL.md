---
name: variance-analysis
category: finance
description: "Explain the gap between budget and actual in a way that changes behaviour."
output: "variance-analysis.md"
used_by:
  - cfo-agent
---

# Variance Analysis

**Category:** `finance` · **Output artifact:** `variance-analysis.md`

## What this skill does
Explain the gap between budget and actual in a way that changes behaviour.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cfo-agent`.

## Procedure
1. Compare actual to budget by line, at the level where someone owns it.
2. Separate price, volume, and timing effects.
3. Investigate every variance above the materiality threshold.
4. Distinguish one-off from structural variances.
5. Assign each structural variance an owner and a corrective action.

## Output contract
Write `variance-analysis.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** variance-analysis
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
- Price, volume, and timing separated
- Structural variances have owners
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
