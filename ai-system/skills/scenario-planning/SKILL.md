---
name: scenario-planning
category: strategy
description: "Prepare for several plausible futures rather than forecasting one."
output: "scenarios.md"
used_by:
  - chief-strategy-officer-agent
---

# Scenario Planning

`strategy` · produces `scenarios.md` · used by `chief-strategy-officer-agent`

Prepare for several plausible futures rather than forecasting one.

## Procedure
1. Identify the two uncertainties with the highest impact and lowest predictability.
2. Build three or four distinct futures from their combinations.
3. Describe what the business would need to do in each.
4. Identify the no-regret moves that work in all of them.
5. Define early indicators and instrument them.

## Output contract
`scenarios.md` → `workspace/<venture-id>/strategy/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/strategy.tsv`.

## Quality bar
- Futures built from real uncertainties
- No-regret moves identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
