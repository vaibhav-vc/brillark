---
name: regulatory-applicability-mapping
category: legal
description: "Determine which rules actually apply to this business."
output: "applicability-map.md"
used_by:
  - chief-compliance-officer-agent
---

# Regulatory Applicability Mapping

`legal` · produces `applicability-map.md` · used by `chief-compliance-officer-agent`

Determine which rules actually apply to this business.

## Procedure
1. List activities, data types, markets, and customer types.
2. Identify candidate regimes for each and test applicability rather than assuming.
3. Record why each regime applies or does not.
4. Map applicable requirements to owners.
5. Re-run when entering a market or launching a new capability.

## Output contract
`applicability-map.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Non-applicability recorded with a reason
- Re-run on market or product change
- The output states its confidence grade and names the evidence behind every load-bearing claim.
