---
name: brand-consistency-audit
category: gtm
description: "Find where the brand has drifted from its guidelines."
output: "brand-audit.md"
used_by:
  - brand-narrative-agent
---

# Brand Consistency Audit

**Category:** `gtm` · **Output artifact:** `brand-audit.md`

## What this skill does
Find where the brand has drifted from its guidelines.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-narrative-agent`.

## Procedure
1. Inventory every customer-facing surface.
2. Compare each against the voice and visual guidelines.
3. Record drift with a specific example and its location.
4. Prioritise by audience reach rather than by how much it irritates.
5. Fix and set the review cadence.

## Output contract
Write `brand-audit.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** brand-consistency-audit
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
- Drift recorded with specific examples
- Prioritised by reach
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
