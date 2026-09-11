---
name: contractor-classification-review
category: finance
description: "Check that contractors are genuinely contractors."
output: "classification-review.md"
used_by:
  - tax-and-compliance-finance
---

# Contractor Classification Review

`finance` · produces `classification-review.md` · used by `tax-and-compliance-finance`

Check that contractors are genuinely contractors.

## Procedure
1. List every non-employee engagement and its working arrangement.
2. Assess control, integration, substitution rights, and financial risk.
3. Compare against the tests used in the relevant jurisdiction.
4. Flag high-risk engagements with the specific factor that creates the risk.
5. Escalate anything uncertain to qualified advice rather than deciding internally.

## Output contract
`classification-review.md` → `workspace/<venture-id>/finance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/finance.tsv`.

## Quality bar
- Assessed against jurisdiction-specific tests
- Uncertain cases escalated to advice
- The output states its confidence grade and names the evidence behind every load-bearing claim.
