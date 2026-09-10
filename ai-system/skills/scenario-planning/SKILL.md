---
name: scenario-planning
category: strategy
description: "Prepare for several plausible futures rather than forecasting one."
output: "scenarios.md"
used_by:
  - chief-strategy-officer-agent
---

# Scenario Planning

**Category:** `strategy` · **Output artifact:** `scenarios.md`

## What this skill does
Prepare for several plausible futures rather than forecasting one.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-strategy-officer-agent`.

## Procedure
1. Identify the two uncertainties with the highest impact and lowest predictability.
2. Build three or four distinct futures from their combinations.
3. Describe what the business would need to do in each.
4. Identify the no-regret moves that work in all of them.
5. Define early indicators and instrument them.

## Output contract
Write `scenarios.md` into `workspace/<venture-id>/strategy/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** scenario-planning
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
- Futures built from real uncertainties
- No-regret moves identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `strategy` category
- A strategy that states only what we will do, never what we will not.
- A moat described as a feature list rather than a compounding mechanism.
- Reviewing scenarios on a calendar instead of when an indicator trips.
