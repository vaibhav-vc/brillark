---
name: error-taxonomy-design
category: engineering
description: "Design errors that tell the caller what to do."
output: "error-catalogue.md"
used_by:
  - api-designer
---

# Error Taxonomy Design

**Category:** `engineering` · **Output artifact:** `error-catalogue.md`

## What this skill does
Design errors that tell the caller what to do.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `api-designer`.

## Procedure
1. Distinguish client errors, server errors, and business-rule rejections.
2. Give each error a stable code that clients can branch on.
3. Include a human-readable message and a machine-readable field reference.
4. Say what the caller should do about it — retry, fix, or escalate.
5. Never leak internal detail in a customer-facing error.

## Output contract
Write `error-catalogue.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** error-taxonomy-design
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
- Stable codes clients can branch on
- Remediation stated per error
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
