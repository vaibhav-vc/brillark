---
name: referral-mechanics-design
category: gtm
description: "Design a referral that people actually want to make."
output: "referral-design.md"
used_by:
  - growth-loop-designer
---

# Referral Mechanics Design

**Category:** `gtm` · **Output artifact:** `referral-design.md`

## What this skill does
Design a referral that people actually want to make.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `growth-loop-designer`.

## Procedure
1. Identify the moment of realised value — the only good moment to ask.
2. Design an incentive that does not embarrass the referrer.
3. Make the referred experience better than a cold arrival.
4. Reduce the referrer's effort to a single action.
5. Measure referral rate by segment and watch for gaming.

## Output contract
Write `referral-design.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** referral-mechanics-design
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
- Ask placed at realised value
- Referrer effort reduced to one action
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
