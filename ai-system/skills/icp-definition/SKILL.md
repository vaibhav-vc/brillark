---
name: icp-definition
category: market
description: "Define the customer precisely enough to build a target list."
output: "icp.md"
used_by:
  - icp-persona-builder
---

# Icp Definition

`market` · produces `icp.md` · used by `icp-persona-builder`

Define the customer precisely enough to build a target list.

## Procedure
1. Specify firmographic and behavioural attributes you can actually filter on.
2. Add the trigger condition that makes them start looking.
3. Write the disqualification criteria explicitly.
4. Verify you can name a list, community, or channel where they exist.
5. Test the definition against known good and bad customers.

## Output contract
`icp.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Filterable against a real list
- Disqualification criteria explicit
- The output states its confidence grade and names the evidence behind every load-bearing claim.
