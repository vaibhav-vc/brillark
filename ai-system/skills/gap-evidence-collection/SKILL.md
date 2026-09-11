---
name: gap-evidence-collection
category: improvement
description: "Prove the gap is real before proposing to fill it."
output: "gap-evidence.md"
used_by:
  - capability-gap-scout
---

# Gap Evidence Collection

**Category:** `improvement` · **Output artifact:** `gap-evidence.md`

## What this skill does
Prove the gap is real before proposing to fill it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `capability-gap-scout`.

## Procedure
1. Collect escalations that found no owner.
2. Collect cases where an agent improvised outside its skills.
3. Collect failures traced to a missing capability.
4. Require at least three independent instances.
5. Estimate what the gap costs per cycle.

## Output contract
Write `gap-evidence.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** gap-evidence-collection
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
- Three independent instances required
- Cost of the gap estimated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
