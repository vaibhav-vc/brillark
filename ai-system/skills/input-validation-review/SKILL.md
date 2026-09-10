---
name: input-validation-review
category: engineering
description: "Check that untrusted input cannot get through unchecked."
output: "validation-review.md"
used_by:
  - backend-implementation-agent
---

# Input Validation Review

**Category:** `engineering` · **Output artifact:** `validation-review.md`

## What this skill does
Check that untrusted input cannot get through unchecked.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `backend-implementation-agent`.

## Procedure
1. Identify every entry point where external data arrives.
2. Verify validation happens at the boundary, before use.
3. Check type, range, length, format, and encoding.
4. Verify rejection is explicit and does not leak internals.
5. Test with malformed, oversized, and hostile input.

## Output contract
Write `validation-review.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** input-validation-review
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
- Validation at the boundary, not deep inside
- Hostile input tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
