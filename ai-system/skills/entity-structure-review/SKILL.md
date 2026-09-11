---
name: entity-structure-review
category: legal
description: "Check the corporate structure fits what the business actually does."
output: "entity-review.md"
used_by:
  - general-counsel-agent
---

# Entity Structure Review

`legal` · produces `entity-review.md` · used by `general-counsel-agent`

Check the corporate structure fits what the business actually does.

## Procedure
1. Confirm the entity type and jurisdiction match the business model and funding plan.
2. Check whether operations create presence in other jurisdictions.
3. Review whether subsidiaries are needed or merely add cost.
4. Check that governance documents match actual practice.
5. Flag structural changes needing professional advice.

## Output contract
`entity-review.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Operational presence assessed per jurisdiction
- Documents checked against actual practice
- The output states its confidence grade and names the evidence behind every load-bearing claim.
