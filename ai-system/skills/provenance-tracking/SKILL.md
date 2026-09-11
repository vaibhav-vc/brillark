---
name: provenance-tracking
category: memory
description: "Keep every claim traceable to the evidence that produced it."
output: "provenance-record.json"
used_by:
  - context-memory-curator
---

# Provenance Tracking

`memory` · produces `provenance-record.json` · used by `context-memory-curator`

Keep every claim traceable to the evidence that produced it.

## Procedure
1. Record the author agent, the skill used, and the timestamp on every write.
2. Link to the source artifact, not just to its conclusion.
3. Grade the evidence at the moment of writing.
4. Preserve the chain when a claim is derived from another claim.
5. Refuse to promote a claim to semantic memory without traceable provenance.

## Output contract
`provenance-record.json` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Chain preserved through derivations
- No ungraded claims promoted
- The output states its confidence grade and names the evidence behind every load-bearing claim.
