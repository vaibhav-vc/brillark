---
name: post-release-review
category: engineering
description: "Learn from every release, not just the bad ones."
output: "post-release-review.md"
used_by:
  - release-manager
---

# Post Release Review

**Category:** `engineering` · **Output artifact:** `post-release-review.md`

## What this skill does
Learn from every release, not just the bad ones.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `release-manager`.

## Procedure
1. Compare the actual rollout against the plan.
2. Record what surprised the team, however small.
3. Check whether monitoring detected issues before users did.
4. Identify the one change that would have made this smoother.
5. Feed the change into the process, not into a memo.

## Output contract
Write `post-release-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** post-release-review
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
- Surprises recorded even without incident
- One concrete process change identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
