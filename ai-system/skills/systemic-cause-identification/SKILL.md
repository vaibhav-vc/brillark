---
name: systemic-cause-identification
category: improvement
description: "Find the cause that produces many different failures."
output: "systemic-causes.md"
used_by:
  - failure-miner
---

# Systemic Cause Identification

**Category:** `improvement` · **Output artifact:** `systemic-causes.md`

## What this skill does
Find the cause that produces many different failures.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `failure-miner`.

## Procedure
1. Look for causes appearing across multiple clusters.
2. Trace each to the artifact or process that permits it.
3. Check whether the cause is structural rather than a repeated mistake.
4. Estimate how many failures would disappear if it were fixed.
5. Propose the fix at the structural level, not per symptom.

## Output contract
Write `systemic-causes.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** systemic-cause-identification
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
- Traced to a permitting artifact or process
- Fix proposed structurally, not per symptom
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
