---
name: rollback-verification
category: engineering
description: "Prove the way back works before you need it."
output: "rollback-verification.md"
used_by:
  - release-manager
---

# Rollback Verification

**Category:** `engineering` · **Output artifact:** `rollback-verification.md`

## What this skill does
Prove the way back works before you need it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `release-manager`.

## Procedure
1. Identify what rollback means for code, data, and configuration together.
2. Verify data changes are backwards compatible with the previous version.
3. Execute the rollback in a realistic environment.
4. Measure how long it takes and who can do it.
5. Record the verification alongside the release record.

## Output contract
Write `rollback-verification.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** rollback-verification
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
- Data compatibility verified, not just code
- Rollback time measured
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
