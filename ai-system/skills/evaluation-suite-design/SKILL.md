---
name: evaluation-suite-design
category: orchestration
description: "Build a repeatable test set that shows whether agents and skills work."
output: "evaluation-suite.yaml"
used_by:
  - evaluation-harness-agent
---

# Evaluation Suite Design

`orchestration` · produces `evaluation-suite.yaml` · used by `evaluation-harness-agent`

Build a repeatable test set that shows whether agents and skills work.

## Procedure
1. Select real past tasks, including known failures, as cases.
2. Define the expected output properties per case before running anything.
3. Separate outcome quality from process compliance in the scoring.
4. Automate what can be automated; keep judgement cases explicit.
5. Version the suite alongside the agent and skill definitions.

## Output contract
`evaluation-suite.yaml` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Cases drawn from real work
- Expected properties defined in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
