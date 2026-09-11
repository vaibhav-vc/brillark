---
name: prior-art-search
category: research
description: "Find out whether this has been done before."
output: "prior-art-report.md"
used_by:
  - prior-art-researcher
---

# Prior Art Search

`research` · produces `prior-art-report.md` · used by `prior-art-researcher`

Find out whether this has been done before.

## Procedure
1. Describe the problem functionally, independent of your intended solution.
2. Search literature, patents, standards, and open-source implementations.
3. Search in the terms the relevant field uses, including older terminology.
4. Record both successful and abandoned prior approaches.
5. Report the closest work and state honestly how ours differs, including 'it does not'.

## Output contract
`prior-art-report.md` → `workspace/<venture-id>/research/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/research.tsv`.

## Quality bar
- Problem described functionally before searching
- Abandoned approaches recorded alongside successful ones
- The output states its confidence grade and names the evidence behind every load-bearing claim.
