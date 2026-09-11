---
name: distributed-tracing-setup
category: engineering
description: "Follow a request across every service it touches."
output: "tracing-setup.md"
used_by:
  - observability-agent
---

# Distributed Tracing Setup

`engineering` · produces `tracing-setup.md` · used by `observability-agent`

Follow a request across every service it touches.

## Procedure
1. Propagate trace context across all service and queue boundaries.
2. Instrument the spans that represent real work, not every function.
3. Add attributes that make traces searchable by business identifier.
4. Sample deliberately, keeping all error traces.
5. Verify traces are continuous end to end before relying on them.

## Output contract
`tracing-setup.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Context propagated through async boundaries
- Error traces always retained
- The output states its confidence grade and names the evidence behind every load-bearing claim.
