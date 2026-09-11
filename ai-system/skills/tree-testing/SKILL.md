---
name: tree-testing
category: design
description: "Test whether people can find things in a structure before anything is designed on top of it."
output: "tree-test-results.md"
used_by:
  - information-architect
---

# Tree Testing

`design` · produces `tree-test-results.md` · used by `information-architect`

Test whether people can find things in a structure before anything is designed on top of it.

## Procedure
1. Build the tree from labels alone, with no visual design to compensate.
2. Write find-tasks as goals rather than naming the destination.
3. Measure success, directness, and where people went wrong.
4. Identify the nodes that attract wrong turns; those labels are failing.
5. Retest after restructuring rather than assuming the fix worked.

## Output contract
`tree-test-results.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Tested on labels alone
- Wrong-turn nodes identified for relabelling
- The output states its confidence grade and names the evidence behind every load-bearing claim.
