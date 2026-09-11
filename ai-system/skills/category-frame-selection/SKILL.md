---
name: category-frame-selection
category: gtm
description: "Choose the mental category that sets customer expectations."
output: "category-frame.md"
used_by:
  - positioning-messaging-agent
---

# Category Frame Selection

`gtm` · produces `category-frame.md` · used by `positioning-messaging-agent`

Choose the mental category that sets customer expectations.

## Procedure
1. List the categories a buyer might file this under.
2. For each, note the expectations, the comparison set, and the budget line it unlocks.
3. Assess whether we can win the comparison inside that frame.
4. Choose the frame where we compare best and the budget exists.
5. State the expectations the frame creates and confirm we can meet them.

## Output contract
`category-frame.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- Budget line identified per frame
- Created expectations verified as meetable
- The output states its confidence grade and names the evidence behind every load-bearing claim.
