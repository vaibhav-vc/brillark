---
name: state-handling-review
category: engineering
description: "Check the interface handles every state a user can encounter."
output: "state-review.md"
used_by:
  - frontend-implementation-agent
---

# State Handling Review

**Category:** `engineering` · **Output artifact:** `state-review.md`

## What this skill does
Check the interface handles every state a user can encounter.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `frontend-implementation-agent`.

## Procedure
1. Enumerate the states: empty, loading, partial, error, and success.
2. Check each has a designed, implemented treatment.
3. Verify errors are recoverable and explain what to do.
4. Check behaviour on slow networks and interrupted requests.
5. Test the states directly rather than assuming they occur.

## Output contract
Write `state-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** state-handling-review
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
- All five states implemented
- Recovery path present for errors
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
