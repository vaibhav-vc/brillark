---
name: standards-landscape-review
category: research
description: "Find the standards that constrain or help the design."
output: "standards-review.md"
used_by:
  - prior-art-researcher
---

# Standards Landscape Review

`research` · produces `standards-review.md` · used by `prior-art-researcher`

Find the standards that constrain or help the design.

## Procedure
1. Identify the standards bodies relevant to the domain and markets.
2. Distinguish mandatory standards from voluntary and de facto ones.
3. Check the current edition and any pending revision.
4. Assess what each standard requires of the design, concretely.
5. Route mandatory-compliance consequences to the compliance owner.

## Output contract
`standards-review.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Mandatory distinguished from voluntary
- Pending revisions checked, not just current editions
- The output states its confidence grade and names the evidence behind every load-bearing claim.
