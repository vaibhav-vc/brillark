---
name: claims-substantiation-review
category: legal
description: "Check that public claims can be backed up."
output: "substantiation-file.md"
used_by:
  - council-legal-and-regulatory-critic
  - general-counsel-agent
---

# Claims Substantiation Review

`legal` · produces `substantiation-file.md` · used by `council-legal-and-regulatory-critic`, `general-counsel-agent`

Check that public claims can be backed up.

## Procedure
1. Collect every external claim, including implied and comparative ones.
2. Identify the evidence that supports each.
3. Assess whether the evidence supports the exact claim made.
4. Reject or soften claims that outrun the evidence.
5. Keep the substantiation file for as long as the claim is live.

## Output contract
`substantiation-file.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Implied and comparative claims included
- Substantiation retained while the claim is live
- The output states its confidence grade and names the evidence behind every load-bearing claim.
