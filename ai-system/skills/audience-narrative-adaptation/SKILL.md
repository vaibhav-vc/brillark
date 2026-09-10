---
name: audience-narrative-adaptation
category: gtm
description: "Tell the same story to customers, investors, and candidates without contradicting yourself."
output: "narrative-variants.md"
used_by:
  - brand-narrative-agent
---

# Audience Narrative Adaptation

**Category:** `gtm` · **Output artifact:** `narrative-variants.md`

## What this skill does
Tell the same story to customers, investors, and candidates without contradicting yourself.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `brand-narrative-agent`.

## Procedure
1. Identify the spine that must not change across audiences.
2. For each audience, identify what they need to believe and what they fear.
3. Adapt emphasis and evidence, never the underlying claims.
4. Check the versions side by side for contradictions.
5. Update all versions together when the strategy changes.

## Output contract
Write `narrative-variants.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** audience-narrative-adaptation
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
- Spine identical across versions
- Versions checked side by side
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
