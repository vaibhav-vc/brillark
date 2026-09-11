---
name: competitive-kill-scenario
category: council
description: "Describe how a competitor could destroy this business."
output: "kill-scenario.md"
used_by:
  - council-red-team
---

# Competitive Kill Scenario

`council` · produces `kill-scenario.md` · used by `council-red-team`

Describe how a competitor could destroy this business.

## Procedure
1. Identify the competitor best positioned to attack, including a large incumbent.
2. Describe the specific move: bundling, pricing, acquisition, or copying.
3. Estimate how long it would take them and what it would cost.
4. Identify what would make it not worth their while.
5. Define the early indicator that the move has started.

## Output contract
`kill-scenario.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Move described concretely with cost and timing
- Early indicator defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
