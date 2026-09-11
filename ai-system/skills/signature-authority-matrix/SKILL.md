---
name: signature-authority-matrix
category: compliance
description: "Make it unambiguous who may bind the company."
output: "signature-authority.md"
used_by:
  - corporate-secretary-agent
---

# Signature Authority Matrix

`compliance` · produces `signature-authority.md` · used by `corporate-secretary-agent`

Make it unambiguous who may bind the company.

## Procedure
1. Define the categories of commitment and their value thresholds.
2. Assign signing authority per category and threshold.
3. Require dual authorisation above defined limits.
4. Record delegations and their expiry.
5. Communicate the matrix so counterparties are not misled.

## Output contract
`signature-authority.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Dual authorisation above defined limits
- Delegations recorded with expiry
- The output states its confidence grade and names the evidence behind every load-bearing claim.
