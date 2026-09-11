---
name: risk-register-consolidation
category: risk
description: "Merge domain risk registers into one ranked list."
output: "risk-register.md"
used_by:
  - chief-risk-officer-agent
---

# Risk Register Consolidation

`risk` · produces `risk-register.md` · used by `chief-risk-officer-agent`

Merge domain risk registers into one ranked list.

## Procedure
1. Collect registers from every domain.
2. Deduplicate risks described differently by different teams.
3. Normalise scoring across sources.
4. Rank by expected loss and assign a single owner to each.
5. Publish the top risks and the mitigation status of each.

## Output contract
`risk-register.md` → `workspace/<venture-id>/risk/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/risk.tsv`.

## Quality bar
- Cross-domain duplicates merged
- One owner per consolidated risk
- The output states its confidence grade and names the evidence behind every load-bearing claim.
