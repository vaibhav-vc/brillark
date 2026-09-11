---
name: campaign-brief
category: gtm
description: "Define a campaign tightly enough that it can be judged afterwards."
output: "campaign-brief.md"
used_by:
  - cmo-agent
---

# Campaign Brief

`gtm` · produces `campaign-brief.md` · used by `cmo-agent`

Define a campaign tightly enough that it can be judged afterwards.

## Procedure
1. State the audience, the single message, and the action requested.
2. Set the budget, the duration, and the success metric.
3. Define attribution before launch.
4. List the assets required and their owners.
5. State the kill criterion and the review date.

## Output contract
`campaign-brief.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- One message, one requested action
- Success metric and kill criterion defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.
