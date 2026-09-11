---
name: evidence-standard-setting
category: research
description: "Decide what grade of evidence a claim needs before searching for it."
output: "evidence-standard.md"
used_by:
  - research-head
---

# Evidence Standard Setting

`research` · produces `evidence-standard.md` · used by `research-head`

Decide what grade of evidence a claim needs before searching for it.

## Procedure
1. Establish the decision's consequence and reversibility.
2. Set the required evidence grade from that consequence.
3. Publish the standard so it is not negotiated after results arrive.
4. Define what happens when the standard cannot be met: escalate, or decide without.
5. Apply the same standard to welcome and unwelcome findings.

## Output contract
`evidence-standard.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Standard set before results arrive
- Applied equally to welcome and unwelcome findings
- The output states its confidence grade and names the evidence behind every load-bearing claim.
