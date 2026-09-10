---
name: deployment-safety-review
category: engineering
description: "Check a deployment cannot cause irreversible harm."
output: "deployment-review.md"
used_by:
  - infra-devops-agent
---

# Deployment Safety Review

**Category:** `engineering` · **Output artifact:** `deployment-review.md`

## What this skill does
Check a deployment cannot cause irreversible harm.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `infra-devops-agent`.

## Procedure
1. Verify the change is backwards compatible with the running version.
2. Confirm database changes are separated from code changes.
3. Check the rollback path exists and has been exercised.
4. Confirm monitoring will detect a failure quickly.
5. Verify the blast radius is limited by staged exposure.

## Output contract
Write `deployment-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** deployment-safety-review
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
- Rollback exercised, not just documented
- Blast radius limited by staging
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
