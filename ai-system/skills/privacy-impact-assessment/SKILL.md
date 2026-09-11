---
name: privacy-impact-assessment
category: compliance
description: "Assess high-risk processing before it starts."
output: "dpia.md"
used_by:
  - data-protection-officer-agent
---

# Privacy Impact Assessment

`compliance` · produces `dpia.md` · used by `data-protection-officer-agent`

Assess high-risk processing before it starts.

## Procedure
1. Describe the processing, its purpose, and its necessity.
2. Identify the personal data involved and the lawful basis.
3. Assess risks to individuals, not just to the company.
4. Define mitigations and the residual risk after them.
5. Record the decision and consult before proceeding where required.

## Output contract
`dpia.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Risk assessed to individuals
- Residual risk stated after mitigation
- The output states its confidence grade and names the evidence behind every load-bearing claim.
