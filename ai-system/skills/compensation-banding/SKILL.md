---
name: compensation-banding
category: people
description: "Set pay bands and apply them consistently."
output: "compensation-bands.md"
used_by:
  - chro-agent
---

# Compensation Banding

`people` · produces `compensation-bands.md` · used by `chro-agent`

Set pay bands and apply them consistently.

## Procedure
1. Gather benchmarks for the role, level, and market.
2. Define levels by scope and impact, not by tenure.
3. Set bands with a stated position against the market.
4. Define the equity component and its philosophy.
5. Document every exception and review them for pattern bias.

## Output contract
`compensation-bands.md` → `workspace/<venture-id>/people/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/people.tsv`.

## Quality bar
- Levels defined by scope, not tenure
- Exceptions documented and reviewed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
