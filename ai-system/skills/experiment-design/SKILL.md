---
name: experiment-design
category: data
description: "Design a test that can actually answer the question."
output: "experiment-design.md"
used_by:
  - chief-data-officer-agent
---

# Experiment Design

`data` · produces `experiment-design.md` · used by `chief-data-officer-agent`

Design a test that can actually answer the question.

## Procedure
1. State the hypothesis and the single primary metric in advance.
2. Compute the sample size required for the effect worth detecting.
3. Define the randomisation unit and check for interference.
4. Set the duration to cover a full behavioural cycle.
5. Pre-register the analysis; decide the threshold before seeing results.

## Output contract
`experiment-design.md` → `workspace/<venture-id>/data/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/data.tsv`.

## Quality bar
- Sample size computed before launch
- Analysis pre-registered
- The output states its confidence grade and names the evidence behind every load-bearing claim.
