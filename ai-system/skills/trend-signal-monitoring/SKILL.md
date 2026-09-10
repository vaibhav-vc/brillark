---
name: trend-signal-monitoring
category: strategy
description: "Watch the small number of indicators that would change the strategy."
output: "signal-watchlist.md"
used_by:
  - chief-strategy-officer-agent
---

# Trend Signal Monitoring

**Category:** `strategy` · **Output artifact:** `signal-watchlist.md`

## What this skill does
Watch the small number of indicators that would change the strategy.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-strategy-officer-agent`.

## Procedure
1. Derive indicators from the scenarios and the moat thesis.
2. Define the threshold that constitutes a real signal versus noise.
3. Assign a source and a check cadence to each.
4. Review only when a threshold trips, not on a calendar.
5. Retire indicators that have never been informative.

## Output contract
Write `signal-watchlist.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** trend-signal-monitoring
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
- Thresholds separate signal from noise
- Review triggered by signal, not calendar
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
