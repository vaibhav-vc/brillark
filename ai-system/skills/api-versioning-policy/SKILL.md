---
name: api-versioning-policy
category: engineering
description: "Decide how the interface changes without breaking clients."
output: "versioning-policy.md"
used_by:
  - api-designer
---

# API Versioning Policy

**Category:** `engineering` · **Output artifact:** `versioning-policy.md`

## What this skill does
Decide how the interface changes without breaking clients.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `api-designer`.

## Procedure
1. Define what constitutes a breaking change, explicitly.
2. Choose the versioning mechanism and apply it consistently.
3. Define the deprecation period and the notice required.
4. Define how clients are told and how usage is tracked.
5. Commit to supporting old versions for the stated period.

## Output contract
Write `versioning-policy.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** api-versioning-policy
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
- Breaking change defined explicitly
- Deprecation notice period committed
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
