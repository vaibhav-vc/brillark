---
name: audit-readiness-review
category: compliance
description: "Find the gaps before an auditor does."
output: "audit-readiness.md"
used_by:
  - chief-compliance-officer-agent
---

# Audit Readiness Review

`compliance` · produces `audit-readiness.md` · used by `chief-compliance-officer-agent`

Find the gaps before an auditor does.

## Procedure
1. Self-assess every control against its requirement and evidence.
2. Sample-test controls rather than reading policies.
3. Record gaps with severity and remediation owner.
4. Fix the gaps before the audit, not during it.
5. Prepare the narrative for gaps that cannot be closed in time.

## Output contract
`audit-readiness.md` → `workspace/<venture-id>/compliance/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/compliance.tsv`.

## Quality bar
- Controls sample-tested, not just reviewed
- Gaps remediated before the audit
- The output states its confidence grade and names the evidence behind every load-bearing claim.
