---
name: evidence-collection
category: compliance
description: "Gather proof that controls actually operated."
output: "evidence-register.md"
used_by:
  - chief-compliance-officer-agent
---

# Evidence Collection

`compliance` · produces `evidence-register.md` · used by `chief-compliance-officer-agent`

Gather proof that controls actually operated.

## Procedure
1. Define the evidence artifact for each control in advance.
2. Automate collection where the control is technical.
3. Timestamp and store evidence immutably.
4. Check completeness periodically rather than at audit time.
5. Flag controls with no evidence as failed controls.

## Output contract
`evidence-register.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Evidence defined before the period begins
- Missing evidence treated as control failure
- The output states its confidence grade and names the evidence behind every load-bearing claim.
