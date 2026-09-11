---
name: conformance-auditing
category: design
description: "Audit a shipped surface against the conformance target."
output: "conformance-audit.md"
used_by:
  - accessibility-designer
---

# Conformance Auditing

`design` · produces `conformance-audit.md` · used by `accessibility-designer`

Audit a shipped surface against the conformance target.

## Procedure
1. Audit against the specific criteria at the target level, not a general impression.
2. Combine automated checks with manual and assistive technology testing.
3. Record each failure with the criterion, the location, and the evidence.
4. Rate severity by user impact, not by how easy it is to fix.
5. Produce a remediation plan with owners and dates.

## Output contract
`conformance-audit.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Manual testing combined with automated checks
- Each failure tied to a specific criterion
- The output states its confidence grade and names the evidence behind every load-bearing claim.
