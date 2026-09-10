---
name: tech-debt-registry
category: engineering
description: "Record debt with its actual cost."
output: "tech-debt-register.md"
used_by:
  - tech-debt-refactor-agent
---

# Tech Debt Registry

**Category:** `engineering` · **Output artifact:** `tech-debt-register.md`

## What this skill does
Record debt with its actual cost.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `tech-debt-refactor-agent`.

## Procedure
1. Record each item with its location and the change it makes harder.
2. Estimate the interest: time added to each change in that area.
3. Estimate the cost to fix.
4. Rank by interest rate rather than by size.
5. Review when a roadmap item touches a registered area.

## Output contract
Write `tech-debt-register.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** tech-debt-registry
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
- Interest quantified per item
- Ranked by interest, not size
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
