---
name: network-effect-analysis
category: council
description: "Test whether a claimed network effect is real."
output: "network-effect-analysis.md"
used_by:
  - council-expansion-scout
---

# Network Effect Analysis

`council` · produces `network-effect-analysis.md` · used by `council-expansion-scout`

Test whether a claimed network effect is real.

## Procedure
1. Specify who gains value when who else joins — direct, indirect, or local.
2. Check whether the effect is actually present at current scale or merely hoped for.
3. Identify the critical mass required for it to matter.
4. Assess whether it is local or global; local effects are weaker but reachable.
5. Identify what could disintermediate it.

## Output contract
`network-effect-analysis.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Effect verified at current scale
- Critical mass quantified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
