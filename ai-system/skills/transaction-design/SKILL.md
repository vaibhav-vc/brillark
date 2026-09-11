---
name: transaction-design
category: engineering
description: "Decide the consistency guarantee each operation actually offers."
output: "transaction-design.md"
used_by:
  - backend-implementation-agent
---

# Transaction Design

`engineering` · produces `transaction-design.md` · used by `backend-implementation-agent`

Decide the consistency guarantee each operation actually offers.

## Procedure
1. Identify the invariants that must never be violated.
2. Determine the smallest transactional boundary that protects them.
3. Decide the guarantee for operations that cross boundaries.
4. Document the guarantee offered to callers explicitly.
5. Test the concurrent case, not just the sequential one.

## Output contract
`transaction-design.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Invariants identified before boundaries
- Concurrent behaviour tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
