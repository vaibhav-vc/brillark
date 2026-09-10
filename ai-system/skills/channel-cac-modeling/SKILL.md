---
name: channel-cac-modeling
category: gtm
description: "Compute what each channel actually costs per acquired customer."
output: "channel-cac.md"
used_by:
  - cmo-agent
  - gtm-strategist
---

# Channel CAC Modeling

**Category:** `gtm` · **Output artifact:** `channel-cac.md`

## What this skill does
Compute what each channel actually costs per acquired customer.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cmo-agent`, `gtm-strategist`.

## Procedure
1. Include all costs: media, tools, content production, and people time.
2. Attribute conversions with a stated model, and acknowledge its limits.
3. Compute CAC and payback per channel, not blended.
4. Compare against the LTV-derived ceiling.
5. Rank channels and recommend which to scale, hold, or kill.

## Output contract
Write `channel-cac.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** channel-cac-modeling
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
- Fully loaded costs included
- Compared against an LTV-derived ceiling
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
