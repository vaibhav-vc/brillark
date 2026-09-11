---
name: primary-source-tracing
category: research
description: "Follow a claim back to where it actually originated."
output: "source-trace.md"
used_by:
  - source-verifier
---

# Primary Source Tracing

`research` · produces `source-trace.md` · used by `source-verifier`

Follow a claim back to where it actually originated.

## Procedure
1. Take the claim and find the source the citing document used.
2. Repeat until you reach data, a study, a filing, or a dead end.
3. Record each hop so the chain is auditable.
4. Stop at the primary source and check it says what the chain claims it says.
5. When the chain dead-ends, mark the claim unverifiable rather than accepting it.

## Output contract
`source-trace.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Every hop recorded
- Primary source checked against what was claimed of it
- The output states its confidence grade and names the evidence behind every load-bearing claim.
