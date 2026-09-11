---
name: counsel-escalation
category: legal
description: "Mark clearly what needs a licensed professional."
output: "counsel-request.md"
used_by:
  - council-legal-and-regulatory-critic
---

# Counsel Escalation

`legal` · produces `counsel-request.md` · used by `council-legal-and-regulatory-critic`

Mark clearly what needs a licensed professional.

## Procedure
1. Identify the question that exceeds issue-spotting.
2. State what has already been established and what remains open.
3. Frame the specific question for counsel, not the whole situation.
4. Note the deadline and the decision waiting on it.
5. Never paper over the gap with a confident-sounding internal answer.

## Output contract
`counsel-request.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Specific question framed for counsel
- Internal answer never substituted for advice
- The output states its confidence grade and names the evidence behind every load-bearing claim.
