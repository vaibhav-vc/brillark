---
name: boundary-design
category: engineering
description: "Decide where to split the system."
output: "boundary-design.md"
used_by:
  - system-architect
---

# Boundary Design

**Category:** `engineering` · **Output artifact:** `boundary-design.md`

## What this skill does
Decide where to split the system.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `system-architect`.

## Procedure
1. Group by data ownership and rate of change, not by team structure.
2. Define the contract at each boundary explicitly.
3. Check that a boundary reduces coupling rather than moving it.
4. Assess the cost of crossing: latency, consistency, and debugging.
5. Prefer fewer boundaries until the pain justifies another.

## Output contract
Write `boundary-design.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** boundary-design
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
- Boundaries follow data and change rate
- Crossing cost assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
