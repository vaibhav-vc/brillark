---
name: improvement-queue-ranking
category: improvement
description: "Rank candidate fixes by what they are actually worth."
output: "improvement-queue.md"
used_by:
  - agent-performance-analyst
---

# Improvement Queue Ranking

`improvement` · produces `improvement-queue.md` · used by `agent-performance-analyst`

Rank candidate fixes by what they are actually worth.

## Procedure
1. Estimate the cost each problem imposes per cycle.
2. Estimate the probability a proposed fix works.
3. Estimate the effort and the risk of the fix.
4. Rank by expected value, not by how recently it was raised.
5. Publish the queue and what sits below the line.

## Output contract
`improvement-queue.md` → `workspace/<venture-id>/improvement/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/improvement.tsv`.

## Quality bar
- Ranked by expected value, not recency
- Below-the-line items published
- The output states its confidence grade and names the evidence behind every load-bearing claim.
