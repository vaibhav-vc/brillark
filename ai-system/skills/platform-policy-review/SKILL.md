---
name: platform-policy-review
category: legal
description: "Check the plan against the rules of the platforms it depends on."
output: "platform-policy-review.md"
used_by:
  - council-legal-and-regulatory-critic
---

# Platform Policy Review

`legal` · produces `platform-policy-review.md` · used by `council-legal-and-regulatory-critic`

Check the plan against the rules of the platforms it depends on.

## Procedure
1. Identify every platform the business depends on for distribution or payment.
2. Review the policies that apply to our model, especially around payments and data.
3. Check for policy changes since the last review.
4. Assess the consequence of removal, which is usually immediate.
5. Reduce single-platform dependency where the risk is material.

## Output contract
`platform-policy-review.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Payment and data policies specifically checked
- Removal consequence assessed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
