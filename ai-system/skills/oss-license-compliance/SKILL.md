---
name: oss-license-compliance
category: legal
description: "Make sure dependency licences are compatible with the business model."
output: "license-report.md"
used_by:
  - ip-counsel-agent
---

# Oss License Compliance

`legal` · produces `license-report.md` · used by `ip-counsel-agent`

Make sure dependency licences are compatible with the business model.

## Procedure
1. Generate the full dependency tree, including transitive dependencies.
2. Identify the licence of each and its obligations.
3. Flag copyleft licences in anything distributed to customers.
4. Verify attribution and notice requirements are met.
5. Establish a gate so new dependencies are checked before merge.

## Output contract
`license-report.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Transitive dependencies included
- Merge gate established for new dependencies
- The output states its confidence grade and names the evidence behind every load-bearing claim.
