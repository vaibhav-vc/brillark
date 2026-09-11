---
name: trademark-clearance
category: legal
description: "Check a name can actually be used before committing to it."
output: "clearance-memo.md"
used_by:
  - ip-counsel-agent
---

# Trademark Clearance

`legal` · produces `clearance-memo.md` · used by `ip-counsel-agent`

Check a name can actually be used before committing to it.

## Procedure
1. Search registers in every market where the mark will be used.
2. Search common-law and unregistered use, including domains and app stores.
3. Assess similarity in the relevant classes, not just identical matches.
4. Assess the risk of opposition from adjacent marks.
5. Escalate to counsel before launch, not after.

## Output contract
`clearance-memo.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Unregistered use searched too
- Cleared before public launch
- The output states its confidence grade and names the evidence behind every load-bearing claim.
