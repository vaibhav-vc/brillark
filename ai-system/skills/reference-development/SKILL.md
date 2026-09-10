---
name: reference-development
category: gtm
description: "Turn successful customers into evidence others will believe."
output: "reference-assets.md"
used_by:
  - customer-success-agent
---

# Reference Development

**Category:** `gtm` · **Output artifact:** `reference-assets.md`

## What this skill does
Turn successful customers into evidence others will believe.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `customer-success-agent`.

## Procedure
1. Identify customers with a measurable, attributable outcome.
2. Ask at the moment of realised value, not at renewal time.
3. Capture the specific numbers, with permission to use them.
4. Produce the asset in the format prospects actually consume.
5. Maintain a reference roster so the same customers are not exhausted.

## Output contract
Write `reference-assets.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** reference-development
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
- Outcomes are measurable and attributable
- Reference load spread across customers
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
