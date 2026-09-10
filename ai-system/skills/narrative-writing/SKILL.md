---
name: narrative-writing
category: gtm
description: "Write the story of why the company exists and why it matters."
output: "narrative.md"
used_by:
  - brand-narrative-agent
  - investor-reporting-agent
---

# Narrative Writing

**Category:** `gtm` · **Output artifact:** `narrative.md`

## What this skill does
Write the story of why the company exists and why it matters.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-narrative-agent`, `investor-reporting-agent`.

## Procedure
1. Open with the tension in the world, not with the product.
2. Explain what changed that makes a new answer possible.
3. Position the company as the answer, specifically and provably.
4. Make the customer the protagonist, not the company.
5. Check every claim is one the product can actually back.

## Output contract
Write `narrative.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** narrative-writing
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
- Opens with tension, not product
- Every claim backed by the product
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
