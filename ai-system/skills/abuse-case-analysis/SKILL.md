---
name: abuse-case-analysis
category: council
description: "Find how the product will be misused."
output: "abuse-cases.md"
used_by:
  - council-red-team
---

# Abuse Case Analysis

`council` · produces `abuse-cases.md` · used by `council-red-team`

Find how the product will be misused.

## Procedure
1. Enumerate the actors who benefit from misusing the system.
2. For each, describe the specific misuse and what it gains them.
3. Assess harm to other users, to third parties, and to the company.
4. Check whether the misuse scales cheaply — that is what makes it serious.
5. Propose detection and prevention for each, with the cost of each control.

## Output contract
`abuse-cases.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Misuse scalability assessed
- Detection proposed alongside prevention
- The output states its confidence grade and names the evidence behind every load-bearing claim.
