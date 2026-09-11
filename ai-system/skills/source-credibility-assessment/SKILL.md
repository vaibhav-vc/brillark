---
name: source-credibility-assessment
category: research
description: "Decide how much a source can be trusted, and say why."
output: "credibility-assessment.md"
used_by:
  - source-verifier
---

# Source Credibility Assessment

`research` · produces `credibility-assessment.md` · used by `source-verifier`

Decide how much a source can be trusted, and say why.

## Procedure
1. Identify the producer and what they gain from the conclusion.
2. Check whether methodology is disclosed; undisclosed methodology caps the grade.
3. Check the author's or organisation's track record on this subject.
4. Check whether the source is primary, secondary, or promotional.
5. Assign the grade with one sentence of reasoning that a reader could dispute.

## Output contract
`credibility-assessment.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Producer incentive identified
- Grade reasoning stated and disputable
- The output states its confidence grade and names the evidence behind every load-bearing claim.
