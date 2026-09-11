---
name: slo-definition
category: engineering
description: "Define reliability targets from what users actually notice."
output: "slo.md"
used_by:
  - observability-agent
---

# Slo Definition

`engineering` · produces `slo.md` · used by `observability-agent`

Define reliability targets from what users actually notice.

## Procedure
1. Identify the critical user journeys.
2. Define the indicator that reflects user experience for each.
3. Set the objective from user expectation and business need, not from what is easy.
4. Derive the error budget and agree what happens when it is spent.
5. Review quarterly against actual performance and user complaints.

## Output contract
`slo.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Indicators reflect user experience
- Error budget consequence agreed in advance
- The output states its confidence grade and names the evidence behind every load-bearing claim.
