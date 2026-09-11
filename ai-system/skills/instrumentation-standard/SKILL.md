---
name: instrumentation-standard
category: engineering
description: "Define how the system reports on itself."
output: "instrumentation-standard.md"
used_by:
  - observability-agent
---

# Instrumentation Standard

`engineering` · produces `instrumentation-standard.md` · used by `observability-agent`

Define how the system reports on itself.

## Procedure
1. Define the naming convention for metrics, logs, and spans.
2. Require a correlation identifier propagated across all boundaries.
3. Define the required attributes on every telemetry type.
4. Specify what must never be emitted: secrets and personal data.
5. Make the standard easy to follow with a shared library.

## Output contract
`instrumentation-standard.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Correlation propagated across boundaries
- Forbidden fields specified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
