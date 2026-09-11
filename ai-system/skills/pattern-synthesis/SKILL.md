---
name: pattern-synthesis
category: market
description: "Find the signal across many conversations without inventing it."
output: "synthesis.md"
used_by:
  - customer-discovery-interviewer
---

# Pattern Synthesis

`market` · produces `synthesis.md` · used by `customer-discovery-interviewer`

Find the signal across many conversations without inventing it.

## Procedure
1. Count how many participants independently raised each theme.
2. Weight by segment — a theme from three of four target buyers matters more than from ten non-buyers.
3. Look for the absence of expected themes; silence is data.
4. Distinguish patterns from single vivid anecdotes.
5. State the confidence and the sample behind each conclusion.

## Output contract
`synthesis.md` → `workspace/<venture-id>/market/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/market.tsv`.

## Quality bar
- Themes counted across participants
- Sample size stated with each conclusion
- The output states its confidence grade and names the evidence behind every load-bearing claim.
