---
name: manufacturing-partner-selection
category: hardware
description: "Choose who builds it on more than price."
output: "partner-selection.md"
used_by:
  - chief-hardware-officer-agent
---

# Manufacturing Partner Selection

`hardware` · produces `partner-selection.md` · used by `chief-hardware-officer-agent`

Choose who builds it on more than price.

## Procedure
1. Assess capability for the specific processes and volumes required.
2. Assess quality systems, certifications, and their actual record.
3. Assess capacity, and whether you will be a priority customer.
4. Assess location against freight, duty, and supply chain risk.
5. Define the exit: what it would take to move production elsewhere.

## Output contract
`partner-selection.md` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Priority as a customer assessed honestly
- Exit cost from the partner established
- The output states its confidence grade and names the evidence behind every load-bearing claim.
