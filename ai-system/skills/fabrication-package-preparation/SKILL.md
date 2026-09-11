---
name: fabrication-package-preparation
category: hardware
description: "Send the supplier everything they need and nothing ambiguous."
output: "fab-package"
used_by:
  - prototyping-fabrication-agent
---

# Fabrication Package Preparation

`hardware` · produces `fab-package` · used by `prototyping-fabrication-agent`

Send the supplier everything they need and nothing ambiguous.

## Procedure
1. Include the model, drawings, and a readme stating material, finish, and quantity.
2. State the tolerances that matter and which are reference only.
3. State inspection requirements and what constitutes acceptance.
4. Include revision identifiers on every file.
5. Confirm the supplier's receipt and their understanding before they start.

## Output contract
`fab-package` → `workspace/<venture-id>/hardware/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/hardware.tsv`.

## Quality bar
- Critical versus reference tolerances distinguished
- Supplier understanding confirmed before start
- The output states its confidence grade and names the evidence behind every load-bearing claim.
