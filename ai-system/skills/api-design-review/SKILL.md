---
name: api-design-review
category: engineering
description: "Review an interface for consistency, evolvability, and misuse resistance."
output: "api-review.md"
used_by:
  - api-designer
  - engineering-head
---

# API Design Review

`engineering` · produces `api-review.md` · used by `api-designer`, `engineering-head`

Review an interface for consistency, evolvability, and misuse resistance.

## Procedure
1. Check the resource model reflects the domain, not the database.
2. Check naming, pluralisation, and verb usage are consistent throughout.
3. Check error responses are specific and actionable.
4. Check pagination, filtering, and idempotency are present where needed.
5. Check every change for backwards compatibility.

## Output contract
`api-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Domain modelled, not the database
- Backwards compatibility verified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
