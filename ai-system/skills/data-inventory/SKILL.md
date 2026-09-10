---
name: data-inventory
category: data
description: "Know what data exists and why."
output: "data-inventory.md"
used_by:
  - data-protection-officer-agent
---

# Data Inventory

**Category:** `data` · **Output artifact:** `data-inventory.md`

## What this skill does
Know what data exists and why.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-protection-officer-agent`.

## Procedure
1. Inventory every dataset, its fields, and its origin.
2. Record the purpose each field serves; a field with no purpose is deleted.
3. Record the lawful basis where personal data is involved.
4. Record retention period and deletion mechanism.
5. Refresh the inventory when systems change, not annually by ritual.

## Output contract
Write `data-inventory.md` into `workspace/<venture-id>/data/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** data-inventory
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
- Purpose recorded per field
- Retention and deletion mechanism recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `data` category
- Two dashboards reporting the same metric with different definitions.
- Reporting an experiment result that never had the power to detect the effect.
- Collecting a field first and finding a purpose for it later.
