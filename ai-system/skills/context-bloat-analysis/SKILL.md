---
name: context-bloat-analysis
category: efficiency
description: "Find context that is loaded and never used."
output: "bloat-report.md"
used_by:
  - token-efficiency-analyst
---

# Context Bloat Analysis

`efficiency` · produces `bloat-report.md` · used by `token-efficiency-analyst`

Find context that is loaded and never used.

## Procedure
1. Capture what was placed in context for a sample of runs.
2. Identify what the output actually referenced or depended on.
3. Compute the loaded-but-unused ratio per agent.
4. Trace unused content to the packaging rule that included it.
5. Tighten the rule and re-measure rather than trimming by hand.

## Output contract
`bloat-report.md` → `workspace/<venture-id>/efficiency/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/efficiency.tsv`.

## Quality bar
- Unused content traced to its packaging rule
- Re-measured after the rule change
- The output states its confidence grade and names the evidence behind every load-bearing claim.
