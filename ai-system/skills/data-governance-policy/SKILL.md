---
name: data-governance-policy
category: data
description: "Set the rules for how data is handled."
output: "data-governance-policy.md"
used_by:
  - chief-data-officer-agent
---

# Data Governance Policy

**Category:** `data` · **Output artifact:** `data-governance-policy.md`

## What this skill does
Set the rules for how data is handled.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-data-officer-agent`.

## Procedure
1. Define ownership and stewardship per data domain.
2. Define access request and approval processes.
3. Define retention, archival, and deletion rules by classification.
4. Define the standards for quality and lineage.
5. Define how the policy is enforced and audited, not just published.

## Output contract
Write `data-governance-policy.md` into `workspace/<venture-id>/data/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** data-governance-policy
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
- Enforcement mechanism defined
- Ownership assigned per domain
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `data` category
- Two dashboards reporting the same metric with different definitions.
- Reporting an experiment result that never had the power to detect the effect.
- Collecting a field first and finding a purpose for it later.
