---
name: release-readiness-review
category: engineering
description: "Decide honestly whether this can ship."
output: "release-readiness.md"
used_by:
  - engineering-head
  - release-manager
---

# Release Readiness Review

**Category:** `engineering` · **Output artifact:** `release-readiness.md`

## What this skill does
Decide honestly whether this can ship.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `engineering-head`, `release-manager`.

## Procedure
1. Check tests, security review, and observability are all complete.
2. Confirm the rollback path is verified.
3. Confirm acceptance criteria are met, including the unhappy paths.
4. Confirm support and documentation are ready for the change.
5. Record go or no-go with the reason; never waive the gate under deadline pressure.

## Output contract
Write `release-readiness.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** release-readiness-review
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
- All gates checked, none waived
- Decision recorded with a reason
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
