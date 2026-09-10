---
name: early-warning-indicator-design
category: council
description: "Define signals that warn before the failure arrives."
output: "early-warning-indicators.md"
used_by:
  - council-risk-and-failure-modes
---

# Early Warning Indicator Design

**Category:** `council` · **Output artifact:** `early-warning-indicators.md`

## What this skill does
Define signals that warn before the failure arrives.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-risk-and-failure-modes`.

## Procedure
1. For each failure mode, identify what changes first.
2. Choose an indicator that is measurable now, not in principle.
3. Set the threshold that distinguishes signal from noise.
4. Assign an owner and a check cadence.
5. Verify the indicator would have fired on a past instance.

## Output contract
Write `early-warning-indicators.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** early-warning-indicator-design
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
- Indicators measurable today
- Back-tested against a past instance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
