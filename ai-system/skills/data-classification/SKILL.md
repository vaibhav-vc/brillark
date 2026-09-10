---
name: data-classification
category: data
description: "Label data by sensitivity so controls can follow."
output: "data-classification.md"
used_by:
  - data-model-designer
---

# Data Classification

**Category:** `data` · **Output artifact:** `data-classification.md`

## What this skill does
Label data by sensitivity so controls can follow.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `data-model-designer`.

## Procedure
1. Define the classification levels and what each requires.
2. Classify every field at the point it is created.
3. Apply the required controls per level: encryption, access, and retention.
4. Review classifications when the use of data changes.
5. Refuse to store data that has no classification.

## Output contract
Write `data-classification.md` into `workspace/<venture-id>/data/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** data-classification
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
- Classification applied at creation
- Controls tied to each level
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `data` category
- Two dashboards reporting the same metric with different definitions.
- Reporting an experiment result that never had the power to detect the effect.
- Collecting a field first and finding a purpose for it later.
