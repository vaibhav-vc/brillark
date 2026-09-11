---
name: failure-mode-cataloguing
category: council
description: "Enumerate the distinct ways this can fail."
output: "failure-catalogue.md"
used_by:
  - council-risk-and-failure-modes
---

# Failure Mode Cataloguing

`council` · produces `failure-catalogue.md` · used by `council-risk-and-failure-modes`

Enumerate the distinct ways this can fail.

## Procedure
1. List failure modes across product, market, financial, operational, and legal dimensions.
2. Describe the mechanism of each, not just the outcome.
3. Rate likelihood and severity in our context.
4. Identify the detection signal for each.
5. Record in a catalogue that persists across ventures.

## Output contract
`failure-catalogue.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Mechanism described per mode
- Detection signal identified per mode
- The output states its confidence grade and names the evidence behind every load-bearing claim.
