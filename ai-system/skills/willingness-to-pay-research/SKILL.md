---
name: willingness-to-pay-research
category: finance
description: "Find out what customers will actually pay, not what they say they like."
output: "wtp-research.md"
used_by:
  - pricing-strategist
---

# Willingness To Pay Research

**Category:** `finance` · **Output artifact:** `wtp-research.md`

## What this skill does
Find out what customers will actually pay, not what they say they like.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `pricing-strategist`.

## Procedure
1. Screen for real buyers with budget authority.
2. Use forced trade-offs or price-sensitivity techniques rather than a single yes/no question.
3. Anchor against the alternative they use today and its cost.
4. Probe the budget line the purchase would come from.
5. Report the range and the segment differences, not a single number.

## Output contract
Write `wtp-research.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** willingness-to-pay-research
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
- Forced trade-offs used, not stated intent
- Segment differences reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
