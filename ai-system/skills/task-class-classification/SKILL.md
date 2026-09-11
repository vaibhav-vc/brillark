---
name: task-class-classification
category: efficiency
description: "Classify work so it can be routed to the right tier."
output: "task-classes.md"
used_by:
  - model-router-tuner
---

# Task Class Classification

`efficiency` · produces `task-classes.md` · used by `model-router-tuner`

Classify work so it can be routed to the right tier.

## Procedure
1. Classify as mechanical, analytical, or judgement.
2. Mechanical: extraction, formatting, validation, tracking, lookup.
3. Analytical: synthesis, comparison, modelling, diagnosis.
4. Judgement: arbitration, strategy, ethics, irreversible decisions.
5. Record the classification with the agent's charter.

## Output contract
`task-classes.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- Classification recorded with the charter
- Irreversible decisions always classed as judgement
- The output states its confidence grade and names the evidence behind every load-bearing claim.
