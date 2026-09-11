---
name: pattern-reuse-lookup
category: memory
description: "Find the prior decomposition, plan, or solution that matches this shape."
output: "pattern-match.md"
used_by:
  - planning-decomposer
---

# Pattern Reuse Lookup

`memory` · produces `pattern-match.md` · used by `planning-decomposer`

Find the prior decomposition, plan, or solution that matches this shape.

## Procedure
1. Describe the current problem by its structure, not its surface topic.
2. Search procedural memory for matching structures.
3. Assess fit honestly — a forced match costs more than starting fresh.
4. Adapt the pattern and record what had to change.
5. Update the pattern's success record with this application's outcome.

## Output contract
`pattern-match.md` → `workspace/<venture-id>/memory/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/memory.tsv`.

## Quality bar
- Match assessed on structure
- Adaptation and outcome recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.
