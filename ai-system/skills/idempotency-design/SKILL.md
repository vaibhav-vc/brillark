---
name: idempotency-design
category: engineering
description: "Make retries safe."
output: "idempotency-design.md"
used_by:
  - api-designer
  - backend-implementation-agent
---

# Idempotency Design

`engineering` · produces `idempotency-design.md` · used by `api-designer`, `backend-implementation-agent`

Make retries safe.

## Procedure
1. Identify every operation a client might retry.
2. Define the idempotency key and its scope.
3. Store the result so a repeat returns the original outcome, not a new one.
4. Define the retention period for idempotency records.
5. Test duplicate submission explicitly, including concurrent duplicates.

## Output contract
`idempotency-design.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Repeat returns the original result
- Concurrent duplicates tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
