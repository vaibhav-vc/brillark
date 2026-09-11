---
name: learning-strategy
category: improvement
description: "Decide what the organisation must get better at, and ignore the rest."
output: "learning-strategy.md"
used_by:
  - chief-learning-officer-agent
---

# Learning Strategy

**Category:** `improvement` · **Output artifact:** `learning-strategy.md`

## What this skill does
Decide what the organisation must get better at, and ignore the rest.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-learning-officer-agent`.

## Procedure
1. Identify the two or three capabilities that most limit outcomes.
2. Set a target and a horizon for each.
3. Name what is deliberately not being improved this period.
4. Assign each target an owner and a measure.
5. Review against the measure rather than against effort spent.

## Output contract
Write `learning-strategy.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** learning-strategy
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
- Deliberate non-targets named
- Reviewed against measures, not effort
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
