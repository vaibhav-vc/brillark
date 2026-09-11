---
name: processor-due-diligence
category: compliance
description: "Check a third party before sending them personal data."
output: "processor-assessment.md"
used_by:
  - data-protection-officer-agent
---

# Processor Due Diligence

`compliance` · produces `processor-assessment.md` · used by `data-protection-officer-agent`

Check a third party before sending them personal data.

## Procedure
1. Establish what data they receive and for what purpose.
2. Verify their security posture and sub-processor chain.
3. Ensure a data processing agreement is in place with adequate terms.
4. Verify the transfer mechanism for any cross-border flow.
5. Record the assessment and set a review date.

## Output contract
`processor-assessment.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Sub-processor chain verified
- Transfer mechanism recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
