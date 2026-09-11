---
name: api-versioning-policy
category: engineering
description: "Decide how the interface changes without breaking clients."
output: "versioning-policy.md"
used_by:
  - api-designer
---

# API Versioning Policy

`engineering` · produces `versioning-policy.md` · used by `api-designer`

Decide how the interface changes without breaking clients.

## Procedure
1. Define what constitutes a breaking change, explicitly.
2. Choose the versioning mechanism and apply it consistently.
3. Define the deprecation period and the notice required.
4. Define how clients are told and how usage is tracked.
5. Commit to supporting old versions for the stated period.

## Output contract
`versioning-policy.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Breaking change defined explicitly
- Deprecation notice period committed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
