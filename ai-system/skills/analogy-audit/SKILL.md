---
name: analogy-audit
category: council
description: "Find reasoning that rests on imitation rather than evidence."
output: "analogy-audit.md"
used_by:
  - council-first-principles
---

# Analogy Audit

`council` · produces `analogy-audit.md` · used by `council-first-principles`

Find reasoning that rests on imitation rather than evidence.

## Procedure
1. Identify every justification of the form 'X does this'.
2. Check whether X's circumstances match ours in the relevant respects.
3. Check whether X actually succeeded because of that choice.
4. Replace the analogy with direct reasoning or evidence.
5. Report justifications that cannot be replaced.

## Output contract
`analogy-audit.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Circumstance match tested per analogy
- Unreplaceable analogies reported
- The output states its confidence grade and names the evidence behind every load-bearing claim.
