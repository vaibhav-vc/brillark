---
name: request-classification
category: orchestration
description: "Put an incoming request into the taxonomy that determines how it is handled."
output: "intake-record.md"
used_by:
  - intake-router
---

# Request Classification

**Category:** `orchestration` · **Output artifact:** `intake-record.md`

## What this skill does
Put an incoming request into the taxonomy that determines how it is handled.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `intake-router`.

## Procedure
1. Determine the primary domain: finance, business, engineering, orchestration, legal, or council.
2. Classify the work type: decide, build, research, review, or operate.
3. Rate reversibility — a one-way door needs a heavier process than a two-way door.
4. Set urgency from a real deadline, not from the requester's tone.
5. Attach the classification to the intake record.

## Output contract
Write `intake-record.md` into `workspace/<venture-id>/orchestration/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** request-classification
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
- Reversibility explicitly rated
- Urgency justified by a real deadline
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `orchestration` category
- Assigning a task to a group instead of one accountable agent.
- Reporting progress as a percentage instead of as artifacts that exist.
- Adding a review layer to fix a problem that a clearer definition of done would solve.
