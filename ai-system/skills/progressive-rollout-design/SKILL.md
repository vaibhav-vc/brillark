---
name: progressive-rollout-design
category: engineering
description: "Expose a change gradually so problems are found by few, not by all."
output: "rollout-plan.md"
used_by:
  - release-manager
---

# Progressive Rollout Design

`engineering` · produces `rollout-plan.md` · used by `release-manager`

Expose a change gradually so problems are found by few, not by all.

## Procedure
1. Define the exposure stages and the population at each.
2. Define the signals watched at each stage and their thresholds.
3. Set the minimum soak time per stage.
4. Define the automatic rollback condition.
5. Decouple deployment from exposure using flags.

## Output contract
`rollout-plan.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Automatic rollback condition defined
- Soak time set per stage
- The output states its confidence grade and names the evidence behind every load-bearing claim.
