---
name: stakeholder-harm-analysis
category: council
description: "Identify who could be harmed, including those who never chose to be involved."
output: "harm-analysis.md"
used_by:
  - council-ethics-and-responsibility
---

# Stakeholder Harm Analysis

`council` · produces `harm-analysis.md` · used by `council-ethics-and-responsibility`

Identify who could be harmed, including those who never chose to be involved.

## Procedure
1. List every affected group, including non-users and third parties.
2. For each, identify the plausible harm and its severity.
3. Pay attention to groups with the least power to object.
4. Distinguish harms inherent to the product from harms caused by its design.
5. Propose a remedy for each identified harm.

## Output contract
`harm-analysis.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Non-users and third parties included
- Remedy proposed per harm
- The output states its confidence grade and names the evidence behind every load-bearing claim.
