---
name: alert-design
category: engineering
description: "Alert only when a human must act."
output: "alert-catalogue.md"
used_by:
  - observability-agent
---

# Alert Design

`engineering` · produces `alert-catalogue.md` · used by `observability-agent`

Alert only when a human must act.

## Procedure
1. Alert on symptoms users would notice, not on internal causes.
2. Require every alert to have a runbook and an owner.
3. Set thresholds that avoid firing on normal variation.
4. Route by severity: page for urgent, ticket for the rest.
5. Delete alerts nobody has acted on in the last quarter.

## Output contract
`alert-catalogue.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Every alert has a runbook
- Unactioned alerts deleted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
