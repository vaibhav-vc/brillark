---
name: freedom-to-operate-search
category: legal
description: "Check whether building this could infringe someone else's rights."
output: "fto-memo.md"
used_by:
  - ip-counsel-agent
---

# Freedom To Operate Search

`legal` · produces `fto-memo.md` · used by `ip-counsel-agent`

Check whether building this could infringe someone else's rights.

## Procedure
1. Define the technical features to be cleared.
2. Search patents and applications in the relevant jurisdictions.
3. Assess claim scope, not just titles and abstracts.
4. Identify design-arounds where risk is found.
5. Escalate to qualified counsel for any credible risk.

## Output contract
`fto-memo.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Claim scope assessed, not titles
- Design-arounds identified where risk exists
- The output states its confidence grade and names the evidence behind every load-bearing claim.
