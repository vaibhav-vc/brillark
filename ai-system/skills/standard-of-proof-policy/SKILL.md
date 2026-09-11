---
name: standard-of-proof-policy
category: research
description: "Set how much evidence different decisions require."
output: "proof-policy.md"
used_by:
  - chief-research-officer-agent
---

# Standard Of Proof Policy

`research` · produces `proof-policy.md` · used by `chief-research-officer-agent`

Set how much evidence different decisions require.

## Procedure
1. Classify decisions by consequence and reversibility.
2. Set a required evidence grade per class, written down.
3. Define who may waive the standard and what they must record.
4. Apply it to the decisions already made, to see where the organisation stands.
5. Review when a decision made below standard turns out badly.

## Output contract
`proof-policy.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Required grade defined per decision class
- Waivers require a recorded justification
- The output states its confidence grade and names the evidence behind every load-bearing claim.
