---
name: coverage-mapping
category: improvement
description: "Know what the evaluation does and does not cover."
output: "coverage-map.md"
used_by:
  - benchmark-curator
---

# Coverage Mapping

`improvement` · produces `coverage-map.md` · used by `benchmark-curator`

Know what the evaluation does and does not cover.

## Procedure
1. Map cases to agents, skills, and failure modes.
2. Identify agent classes with no coverage.
3. Identify failure modes no case would catch.
4. Report thin coverage honestly rather than implying completeness.
5. Prioritise new cases by risk, not by ease of construction.

## Output contract
`coverage-map.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Uncovered agent classes named
- Thin coverage reported honestly
- The output states its confidence grade and names the evidence behind every load-bearing claim.
