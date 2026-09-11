---
name: data-classification
category: data
description: "Label data by sensitivity so controls can follow."
output: "data-classification.md"
used_by:
  - data-model-designer
---

# Data Classification

`data` · produces `data-classification.md` · used by `data-model-designer`

Label data by sensitivity so controls can follow.

## Procedure
1. Define the classification levels and what each requires.
2. Classify every field at the point it is created.
3. Apply the required controls per level: encryption, access, and retention.
4. Review classifications when the use of data changes.
5. Refuse to store data that has no classification.

## Output contract
`data-classification.md` → `workspace/<venture-id>/data/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/data.tsv`.

## Quality bar
- Classification applied at creation
- Controls tied to each level
- The output states its confidence grade and names the evidence behind every load-bearing claim.
