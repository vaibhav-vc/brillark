---
name: pipeline-model
category: gtm
description: "Model the pipeline so forecasts mean something."
output: "pipeline-model.md"
used_by:
  - chief-revenue-officer-agent
---

# Pipeline Model

`gtm` · produces `pipeline-model.md` · used by `chief-revenue-officer-agent`

Model the pipeline so forecasts mean something.

## Procedure
1. Define each stage by an observable buyer action.
2. Measure historical conversion and duration per stage.
3. Compute the pipeline coverage needed to hit the target.
4. Identify the stage where deals actually die.
5. Refresh the rates quarterly; stale conversion rates produce confident wrong forecasts.

## Output contract
`pipeline-model.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Stages defined by buyer actions
- Conversion rates refreshed from actuals
- The output states its confidence grade and names the evidence behind every load-bearing claim.
