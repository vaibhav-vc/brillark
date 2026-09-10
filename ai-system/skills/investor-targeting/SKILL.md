---
name: investor-targeting
category: finance
description: "Build a target list of investors who could actually say yes."
output: "investor-list.md"
used_by:
  - fundraising-strategist
---

# Investor Targeting

**Category:** `finance` · **Output artifact:** `investor-list.md`

## What this skill does
Build a target list of investors who could actually say yes.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `fundraising-strategist`.

## Procedure
1. Filter by stage, cheque size, and sector thesis.
2. Check portfolio for conflicts and for pattern fit.
3. Identify the specific partner, not just the fund.
4. Find the warmest credible introduction path to each.
5. Rank by fit and prioritise, rather than contacting everyone at once.

## Output contract
Write `investor-list.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** investor-targeting
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
- Targeted at partner level
- Conflicts checked in portfolio
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
