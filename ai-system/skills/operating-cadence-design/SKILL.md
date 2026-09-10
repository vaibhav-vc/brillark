---
name: operating-cadence-design
category: orchestration
description: "Design the rhythm of planning, review, and decision for the organisation."
output: "operating-cadence.md"
used_by:
  - coo-agent
---

# Operating Cadence Design

**Category:** `orchestration` · **Output artifact:** `operating-cadence.md`

## What this skill does
Design the rhythm of planning, review, and decision for the organisation.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `coo-agent`.

## Procedure
1. List the decisions the organisation must make repeatedly and how often.
2. Design one ritual per recurring decision, and delete rituals with no decision.
3. Set the cadence from the decision's natural frequency, not from habit.
4. Define the input required and the output produced by each ritual.
5. Review quarterly and cut anything that stopped producing decisions.

## Output contract
Write `operating-cadence.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** operating-cadence-design
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
- Every ritual has a decision output
- Rituals without decisions removed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
