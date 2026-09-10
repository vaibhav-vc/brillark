---
name: kill-criteria-definition
category: orchestration
description: "Decide in advance what would make us stop, while judgement is still uncommitted."
output: "kill-criteria.md"
used_by:
  - director
---

# Kill Criteria Definition

**Category:** `orchestration` · **Output artifact:** `kill-criteria.md`

## What this skill does
Decide in advance what would make us stop, while judgement is still uncommitted.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `director`.

## Procedure
1. State the belief the bet depends on.
2. Define the observation that would disprove it.
3. Set the threshold and the deadline for that observation.
4. Name who declares the kill and who executes it.
5. Record it before the work starts; kill criteria written afterwards are rationalisations.

## Output contract
Write `kill-criteria.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** kill-criteria-definition
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
- Threshold and deadline both numeric
- Recorded before work begins
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
