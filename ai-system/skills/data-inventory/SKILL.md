---
name: data-inventory
category: data
description: "Know what data exists and why."
output: "data-inventory.md"
used_by:
  - data-protection-officer-agent
---

# Data Inventory

`data` · produces `data-inventory.md` · used by `data-protection-officer-agent`

Know what data exists and why.

## Procedure
1. Inventory every dataset, its fields, and its origin.
2. Record the purpose each field serves; a field with no purpose is deleted.
3. Record the lawful basis where personal data is involved.
4. Record retention period and deletion mechanism.
5. Refresh the inventory when systems change, not annually by ritual.

## Output contract
`data-inventory.md` → `workspace/<venture-id>/data/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/data.tsv`.

## Quality bar
- Purpose recorded per field
- Retention and deletion mechanism recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
