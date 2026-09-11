---
name: minimal-intervention-selection
category: improvement
description: "Choose the smallest change that closes the gap."
output: "intervention-proposal.md"
used_by:
  - capability-gap-scout
---

# Minimal Intervention Selection

**Category:** `improvement` · **Output artifact:** `intervention-proposal.md`

## What this skill does
Choose the smallest change that closes the gap.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `capability-gap-scout`.

## Procedure
1. Check whether an existing skill can be revised to cover it.
2. If not, check whether one new skill would suffice.
3. Only then consider a new agent, and justify the accountability it adds.
4. Estimate the ongoing cost of each option, not just the build cost.
5. Recommend the smallest option that actually closes the gap.

## Output contract
Write `intervention-proposal.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** minimal-intervention-selection
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
- Revision considered before addition
- Ongoing cost estimated, not just build cost
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
