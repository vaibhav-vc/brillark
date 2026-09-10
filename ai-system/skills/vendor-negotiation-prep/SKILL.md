---
name: vendor-negotiation-prep
category: finance
description: "Arrive at a vendor negotiation with data instead of hope."
output: "negotiation-brief.md"
used_by:
  - cost-optimization-analyst
---

# Vendor Negotiation Prep

**Category:** `finance` · **Output artifact:** `negotiation-brief.md`

## What this skill does
Arrive at a vendor negotiation with data instead of hope.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `cost-optimization-analyst`.

## Procedure
1. Pull actual usage against the contracted commitment.
2. Benchmark the price against alternatives and published rates.
3. Identify the leverage: renewal timing, volume growth, or a credible alternative.
4. Decide the walk-away position before the conversation.
5. Prepare the specific ask, with the concession you are willing to trade.

## Output contract
Write `negotiation-brief.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** vendor-negotiation-prep
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
- Walk-away position set in advance
- Ask supported by usage data
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
