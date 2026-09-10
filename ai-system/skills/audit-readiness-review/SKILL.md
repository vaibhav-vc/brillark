---
name: audit-readiness-review
category: compliance
description: "Find the gaps before an auditor does."
output: "audit-readiness.md"
used_by:
  - chief-compliance-officer-agent
---

# Audit Readiness Review

**Category:** `compliance` · **Output artifact:** `audit-readiness.md`

## What this skill does
Find the gaps before an auditor does.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-compliance-officer-agent`.

## Procedure
1. Self-assess every control against its requirement and evidence.
2. Sample-test controls rather than reading policies.
3. Record gaps with severity and remediation owner.
4. Fix the gaps before the audit, not during it.
5. Prepare the narrative for gaps that cannot be closed in time.

## Output contract
Write `audit-readiness.md` into `workspace/<venture-id>/compliance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** audit-readiness-review
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Controls sample-tested, not just reviewed
- Gaps remediated before the audit
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `compliance` category
- Writing a policy nobody can follow and treating publication as compliance.
- Collecting evidence at audit time rather than as the control operates.
- Building controls for a framework that was never shown to apply.
