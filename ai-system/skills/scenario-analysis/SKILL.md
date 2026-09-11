---
name: scenario-analysis
category: finance
description: "Model distinct futures defined by driver values rather than adjectives."
output: "scenarios.md"
used_by:
  - finance-head
  - financial-model-builder
  - revenue-forecaster
  - scenario-stress-tester
---

# Scenario Analysis

`finance` · produces `scenarios.md` · used by `finance-head`, `financial-model-builder`, `revenue-forecaster`, `scenario-stress-tester`

Model distinct futures defined by driver values rather than adjectives.

## Procedure
1. Define each scenario by explicit values for the key drivers.
2. Build base, downside, and upside — and a severe case that tests survival.
3. Include correlated effects: shocks rarely arrive alone.
4. Report the outcome and the decision each scenario would trigger.
5. Name the indicator that would tell you which scenario is unfolding.

## Output contract
`scenarios.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Scenarios defined by driver values
- Each scenario has a leading indicator
- The output states its confidence grade and names the evidence behind every load-bearing claim.
