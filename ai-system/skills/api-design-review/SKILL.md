---
name: api-design-review
category: engineering
description: "Review an interface for consistency, evolvability, and misuse resistance."
output: "api-review.md"
used_by:
  - api-designer
  - engineering-head
---

# API Design Review

**Category:** `engineering` · **Output artifact:** `api-review.md`

## What this skill does
Review an interface for consistency, evolvability, and misuse resistance.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `api-designer`, `engineering-head`.

## Procedure
1. Check the resource model reflects the domain, not the database.
2. Check naming, pluralisation, and verb usage are consistent throughout.
3. Check error responses are specific and actionable.
4. Check pagination, filtering, and idempotency are present where needed.
5. Check every change for backwards compatibility.

## Output contract
Write `api-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** api-design-review
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
- Domain modelled, not the database
- Backwards compatibility verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
