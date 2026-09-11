---
name: threat-modeling
category: engineering
description: "Work out how a system could be attacked, before building it."
output: "threat-model.md"
used_by:
  - ciso-agent
  - engineering-head
  - security-engineer
---

# Threat Modeling

`engineering` · produces `threat-model.md` · used by `ciso-agent`, `engineering-head`, `security-engineer`

Work out how a system could be attacked, before building it.

## Procedure
1. Draw the data flow and mark every trust boundary.
2. Enumerate threats per element using a structured method such as STRIDE.
3. Rate each by impact and likelihood in our actual context.
4. Define the control for each threat above the threshold.
5. Record accepted risks with an owner and an expiry date.

## Output contract
`threat-model.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Trust boundaries explicitly marked
- Accepted risks have owners and expiry
- The output states its confidence grade and names the evidence behind every load-bearing claim.
