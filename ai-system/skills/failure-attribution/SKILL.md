---
name: failure-attribution
category: improvement
description: "Determine whether a failure was capability, context, or task definition — because the fixes are different."
output: "attribution-report.md"
used_by:
  - agent-performance-analyst
---

# Failure Attribution

**Category:** `improvement` · **Output artifact:** `attribution-report.md`

## What this skill does
Determine whether a failure was capability, context, or task definition — because the fixes are different.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `agent-performance-analyst`.

## Procedure
1. Reconstruct what the agent was given and what it produced.
2. Check whether the required information was in the context package at all.
3. Check whether the task and its definition of done were unambiguous.
4. Only when both hold, attribute the failure to the agent's capability.
5. Record the attribution and route the fix to whoever owns that cause.

## Output contract
Write `attribution-report.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** failure-attribution
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
- Context and task definition ruled out before blaming capability
- Fix routed to the owner of the actual cause
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
