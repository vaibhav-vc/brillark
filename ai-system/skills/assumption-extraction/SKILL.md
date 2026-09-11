---
name: assumption-extraction
category: council
description: "Surface every assumption, including the invisible ones."
output: "assumption-list.md"
used_by:
  - council-assumption-auditor
---

# Assumption Extraction

`council` · produces `assumption-list.md` · used by `council-assumption-auditor`

Surface every assumption, including the invisible ones.

## Procedure
1. Read the plan for stated assumptions.
2. Extract the unstated ones implied by the numbers, defaults, and structure.
3. Include assumptions about our own capability and speed.
4. Write each as a standalone claim that could be true or false.
5. Pass the list to grading and load-bearing analysis.

## Output contract
`assumption-list.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Unstated assumptions surfaced
- Each written as a testable claim
- The output states its confidence grade and names the evidence behind every load-bearing claim.
