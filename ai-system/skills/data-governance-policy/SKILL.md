---
name: data-governance-policy
category: data
description: "Set the rules for how data is handled."
output: "data-governance-policy.md"
used_by:
  - chief-data-officer-agent
---

# Data Governance Policy

`data` · produces `data-governance-policy.md` · used by `chief-data-officer-agent`

Set the rules for how data is handled.

## Procedure
1. Define ownership and stewardship per data domain.
2. Define access request and approval processes.
3. Define retention, archival, and deletion rules by classification.
4. Define the standards for quality and lineage.
5. Define how the policy is enforced and audited, not just published.

## Output contract
`data-governance-policy.md` → `workspace/<venture-id>/data/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/data.tsv`.

## Quality bar
- Enforcement mechanism defined
- Ownership assigned per domain
- The output states its confidence grade and names the evidence behind every load-bearing claim.
