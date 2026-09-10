---
name: definition-of-done-writing
category: orchestration
description: "Write a completion condition that can be checked by someone other than the author."
output: "definition-of-done.md"
used_by:
  - planning-decomposer
---

# Definition Of Done Writing

**Category:** `orchestration` · **Output artifact:** `definition-of-done.md`

## What this skill does
Write a completion condition that can be checked by someone other than the author.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `planning-decomposer`.

## Procedure
1. State the artifact that must exist, by name and location.
2. State the properties it must have, each independently checkable.
3. Include the review or validation that must have passed.
4. Exclude anything subjective — 'high quality' is not a condition.
5. Have the receiving agent confirm the DoD is sufficient before work begins.

## Output contract
Write `definition-of-done.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** definition-of-done-writing
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
- Every condition independently checkable
- Receiver confirmed sufficiency in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
