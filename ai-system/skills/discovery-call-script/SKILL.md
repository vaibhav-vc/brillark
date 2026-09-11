---
name: discovery-call-script
category: gtm
description: "Structure the first call to diagnose rather than pitch."
output: "discovery-script.md"
used_by:
  - sales-playbook-agent
---

# Discovery Call Script

`gtm` · produces `discovery-script.md` · used by `sales-playbook-agent`

Structure the first call to diagnose rather than pitch.

## Procedure
1. Open by establishing the agenda and the time available.
2. Ask about the current situation and the trigger that prompted the call.
3. Quantify the problem in the customer's own metrics.
4. Confirm the decision process and who else is involved.
5. Close with a specific, agreed next step — never 'I'll follow up'.

## Output contract
`discovery-script.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Problem quantified in customer metrics
- Specific next step agreed on the call
- The output states its confidence grade and names the evidence behind every load-bearing claim.
