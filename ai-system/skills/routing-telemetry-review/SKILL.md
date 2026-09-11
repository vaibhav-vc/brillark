---
name: routing-telemetry-review
category: efficiency
description: "Check the routing is working in practice."
output: "routing-review.md"
used_by:
  - model-router-tuner
---

# Routing Telemetry Review

`efficiency` · produces `routing-review.md` · used by `model-router-tuner`

Check the routing is working in practice.

## Procedure
1. Review escalation frequency per agent against expectation.
2. Identify agents escalating constantly — they were demoted too far.
3. Identify expensive-tier agents whose work never needed it.
4. Check routing decisions against outcome quality.
5. Propose reassignments with the evidence.

## Output contract
`routing-review.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- Over-escalating agents identified
- Over-provisioned agents identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
