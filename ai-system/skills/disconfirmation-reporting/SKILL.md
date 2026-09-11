---
name: disconfirmation-reporting
category: market
description: "Report the evidence against your hypothesis first."
output: "disconfirmation-report.md"
used_by:
  - customer-discovery-interviewer
---

# Disconfirmation Reporting

`market` · produces `disconfirmation-report.md` · used by `customer-discovery-interviewer`

Report the evidence against your hypothesis first.

## Procedure
1. List what you expected to find before the research.
2. Report what contradicted it, in full, before reporting confirmation.
3. Assess whether the contradiction is fatal, partial, or explainable.
4. Update the hypothesis explicitly rather than quietly.
5. Record the update so the learning log shows what changed.

## Output contract
`disconfirmation-report.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Contradicting evidence reported first
- Hypothesis updated explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
