---
name: terminology-consistency-audit
category: gtm
description: "Make sure one concept has one name everywhere."
output: "terminology-audit.md"
used_by:
  - positioning-messaging-agent
---

# Terminology Consistency Audit

`gtm` · produces `terminology-audit.md` · used by `positioning-messaging-agent`

Make sure one concept has one name everywhere.

## Procedure
1. Inventory the terms used across product, docs, site, and sales material.
2. Find concepts with multiple names and names with multiple meanings.
3. Choose the canonical term using customer language.
4. Update every surface and record the decision in the glossary.
5. Re-audit after each major release.

## Output contract
`terminology-audit.md` → `workspace/<venture-id>/gtm/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/gtm.tsv`.

## Quality bar
- One canonical term per concept
- Customer language preferred over internal
- The output states its confidence grade and names the evidence behind every load-bearing claim.
