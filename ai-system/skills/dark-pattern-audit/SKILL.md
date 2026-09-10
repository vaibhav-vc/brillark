---
name: dark-pattern-audit
category: council
description: "Find design that works against the user's interest."
output: "dark-pattern-audit.md"
used_by:
  - council-ethics-and-responsibility
---

# Dark Pattern Audit

**Category:** `council` · **Output artifact:** `dark-pattern-audit.md`

## What this skill does
Find design that works against the user's interest.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-ethics-and-responsibility`.

## Procedure
1. Review sign-up, purchase, and cancellation flows for asymmetry.
2. Check whether cancelling is as easy as subscribing.
3. Look for hidden costs, pre-selected options, and confusing negatives.
4. Check whether urgency and scarcity claims are true.
5. Report each with the specific screen and the honest alternative.

## Output contract
Write `dark-pattern-audit.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** dark-pattern-audit
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
- Cancellation symmetry checked
- Honest alternative proposed per finding
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
