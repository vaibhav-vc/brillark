---
name: error-taxonomy-design
category: engineering
description: "Design errors that tell the caller what to do."
output: "error-catalogue.md"
used_by:
  - api-designer
---

# Error Taxonomy Design

`engineering` · produces `error-catalogue.md` · used by `api-designer`

Design errors that tell the caller what to do.

## Procedure
1. Distinguish client errors, server errors, and business-rule rejections.
2. Give each error a stable code that clients can branch on.
3. Include a human-readable message and a machine-readable field reference.
4. Say what the caller should do about it — retry, fix, or escalate.
5. Never leak internal detail in a customer-facing error.

## Output contract
`error-catalogue.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Stable codes clients can branch on
- Remediation stated per error
- The output states its confidence grade and names the evidence behind every load-bearing claim.
