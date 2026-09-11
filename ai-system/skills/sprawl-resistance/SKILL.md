---
name: sprawl-resistance
category: improvement
description: "Recommend against filling a gap when that is the right answer."
output: "non-proposal.md"
used_by:
  - capability-gap-scout
---

# Sprawl Resistance

**Category:** `improvement` · **Output artifact:** `non-proposal.md`

## What this skill does
Recommend against filling a gap when that is the right answer.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `capability-gap-scout`.

## Procedure
1. Compare the cost of the gap against the cost of the addition.
2. Check whether the gap is genuinely recurring or a one-off.
3. Check whether an existing agent could absorb it within its charter.
4. Record the explicit non-proposal with the reasoning.
5. Re-examine only when new evidence arrives.

## Output contract
Write `non-proposal.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** sprawl-resistance
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
- Explicit non-proposals recorded with reasoning
- Re-examination gated on new evidence
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
