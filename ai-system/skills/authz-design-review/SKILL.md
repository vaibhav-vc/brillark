---
name: authz-design-review
category: engineering
description: "Check that permission logic is correct and cannot be bypassed."
output: "authz-review.md"
used_by:
  - security-engineer
---

# Authz Design Review

**Category:** `engineering` · **Output artifact:** `authz-review.md`

## What this skill does
Check that permission logic is correct and cannot be bypassed.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `security-engineer`.

## Procedure
1. Map every resource and the actions possible on it.
2. Define who may do what, and check the default is deny.
3. Verify authorisation happens server-side on every path, including internal ones.
4. Test horizontal access: can one tenant reach another's data?
5. Treat authorisation code as high-risk and require a second reviewer.

## Output contract
Write `authz-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** authz-design-review
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
- Default-deny verified
- Cross-tenant access tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
