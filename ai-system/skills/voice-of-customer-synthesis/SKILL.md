---
name: voice-of-customer-synthesis
category: gtm
description: "Turn scattered customer feedback into something product can act on."
output: "voc-digest.md"
used_by:
  - customer-success-agent
---

# Voice Of Customer Synthesis

**Category:** `gtm` · **Output artifact:** `voc-digest.md`

## What this skill does
Turn scattered customer feedback into something product can act on.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `customer-success-agent`.

## Procedure
1. Collect feedback from support, sales, reviews, and usage data.
2. Code into themes and count frequency and severity.
3. Distinguish requested solutions from underlying problems.
4. Weight by segment value and strategic fit.
5. Deliver as ranked problems with evidence, not as a feature list.

## Output contract
Write `voc-digest.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** voice-of-customer-synthesis
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
- Problems separated from requested solutions
- Themes counted and weighted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
