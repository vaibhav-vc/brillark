---
name: constraint-over-explanation
category: improvement
description: "Write rules agents follow rather than rationale they interpret."
output: "rule-text.md"
used_by:
  - knowledge-distiller
---

# Constraint Over Explanation

**Category:** `improvement` · **Output artifact:** `rule-text.md`

## What this skill does
Write rules agents follow rather than rationale they interpret.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `knowledge-distiller`.

## Procedure
1. State the rule as a directive, not as background.
2. Make the condition for applying it unambiguous.
3. State what to do when the rule cannot be followed.
4. Avoid hedged language that invites improvisation.
5. Keep the rationale separate and shorter than the rule.

## Output contract
Write `rule-text.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** constraint-over-explanation
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
- Rule stated as an unambiguous directive
- Cannot-follow case specified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
