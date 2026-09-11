---
name: knowledge-asset-review
category: research
description: "Ask what the organisation knows that others do not."
output: "knowledge-assets.md"
used_by:
  - chief-research-officer-agent
---

# Knowledge Asset Review

`research` · produces `knowledge-assets.md` · used by `chief-research-officer-agent`

Ask what the organisation knows that others do not.

## Procedure
1. Inventory proprietary knowledge: data, findings, and customer understanding.
2. Assess what it would cost a competitor to acquire the same.
3. Identify knowledge that is decaying and needs refreshing.
4. Identify knowledge assumed proprietary that is actually public.
5. Recommend what to invest in, protect, or stop maintaining.

## Output contract
`knowledge-assets.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Replication cost estimated per asset
- Falsely-assumed-proprietary knowledge identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.
