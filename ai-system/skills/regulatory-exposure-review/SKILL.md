---
name: regulatory-exposure-review
category: legal
description: "Challenge a plan on what regulators would permit."
output: "regulatory-exposure.md"
used_by:
  - council-legal-and-regulatory-critic
---

# Regulatory Exposure Review

`legal` · produces `regulatory-exposure.md` · used by `council-legal-and-regulatory-critic`

Challenge a plan on what regulators would permit.

## Procedure
1. Identify every regulated activity the plan touches, including hidden ones in payments and data.
2. Assess whether a licence or registration is required.
3. Check restrictions on marketing, claims, and target audiences.
4. Assess the consequence of getting it wrong, not just the likelihood.
5. Escalate anything requiring a licensed opinion.

## Output contract
`regulatory-exposure.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Hidden regulated activities surfaced
- Consequence assessed, not just likelihood
- The output states its confidence grade and names the evidence behind every load-bearing claim.
