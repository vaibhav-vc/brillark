---
name: asset-library-management
category: design
description: "Keep brand and product assets available in the formats people need."
output: "asset-library.md"
used_by:
  - brand-identity-designer
---

# Asset Library Management

`design` · produces `asset-library.md` · used by `brand-identity-designer`

Keep brand and product assets available in the formats people need.

## Procedure
1. Provide each asset in the formats and resolutions actually used.
2. Name files predictably so the right one is chosen.
3. Version assets and mark the current one clearly.
4. Remove superseded assets so they stop appearing in production.
5. Track where assets are used so a change can be propagated.

## Output contract
`asset-library.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Formats match real usage
- Superseded assets removed, not just marked
- The output states its confidence grade and names the evidence behind every load-bearing claim.
