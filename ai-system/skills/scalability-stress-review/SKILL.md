---
name: scalability-stress-review
category: engineering
description: "Find where the architecture breaks before the market finds it."
output: "scalability-review.md"
used_by:
  - cto-agent
  - system-architect
---

# Scalability Stress Review

**Category:** `engineering` · **Output artifact:** `scalability-review.md`

## What this skill does
Find where the architecture breaks before the market finds it.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cto-agent`, `system-architect`.

## Procedure
1. Model load at ten and one hundred times current volume.
2. Identify the first component to break at each level.
3. Check data growth separately from request growth.
4. Estimate the cost curve, not just the technical limit.
5. Record the breaking points and the change each would require.

## Output contract
Write `scalability-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** scalability-stress-review
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
- First breaking point identified per level
- Cost curve modelled alongside capacity
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
