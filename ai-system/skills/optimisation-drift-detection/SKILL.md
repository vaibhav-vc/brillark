---
name: optimisation-drift-detection
category: improvement
description: "Catch the system getting better at its metrics while getting worse at its job."
output: "drift-report.md"
used_by:
  - chief-learning-officer-agent
---

# Optimisation Drift Detection

**Category:** `improvement` · **Output artifact:** `drift-report.md`

## What this skill does
Catch the system getting better at its metrics while getting worse at its job.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-learning-officer-agent`.

## Procedure
1. Compare metric improvements against real outcomes they are meant to proxy.
2. Look for metrics improving while user or business outcomes do not.
3. Check whether recent changes targeted the measure rather than the goal.
4. Check whether the evaluation set has narrowed toward what we optimise.
5. Report drift and recommend widening the measurement.

## Output contract
Write `drift-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** optimisation-drift-detection
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
- Metrics compared against the outcomes they proxy
- Narrowing evaluation sets flagged
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
