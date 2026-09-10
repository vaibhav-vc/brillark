---
name: feature-flag-management
category: engineering
description: "Use flags without creating a permanent maze."
output: "flag-registry.md"
used_by:
  - release-manager
---

# Feature Flag Management

**Category:** `engineering` · **Output artifact:** `flag-registry.md`

## What this skill does
Use flags without creating a permanent maze.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `release-manager`.

## Procedure
1. Give every flag an owner, a purpose, and an expiry date.
2. Distinguish release flags from operational toggles from experiments.
3. Keep flag logic out of deep code paths.
4. Remove flags promptly after full rollout.
5. Audit flags regularly and delete the abandoned ones.

## Output contract
Write `flag-registry.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** feature-flag-management
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
- Every flag has an owner and expiry
- Stale flags removed, not accumulated
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
