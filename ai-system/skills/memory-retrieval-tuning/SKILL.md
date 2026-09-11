---
name: memory-retrieval-tuning
category: memory
description: "Make sure the right memory reaches the agent that needs it."
output: "retrieval-quality-report.md"
used_by:
  - context-memory-curator
---

# Memory Retrieval Tuning

`memory` · produces `retrieval-quality-report.md` · used by `context-memory-curator`

Make sure the right memory reaches the agent that needs it.

## Procedure
1. Sample recent tasks and check which known facts were not retrieved.
2. Diagnose the miss: bad keys, bad chunking, or bad ranking.
3. Adjust retrieval keys and entity links rather than adding more text.
4. Re-run the sample and measure the hit rate change.
5. Record rediscovery incidents as retrieval defects, not agent errors.

## Output contract
`retrieval-quality-report.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Hit rate measured on real tasks
- Rediscovery logged as a retrieval defect
- The output states its confidence grade and names the evidence behind every load-bearing claim.
