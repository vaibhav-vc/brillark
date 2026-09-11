---
name: verdict-writing
category: council
description: "Produce the decision-grade output of a review."
output: "council-verdict.md"
used_by:
  - council-director
  - council-synthesis-arbiter
---

# Verdict Writing

`council` · produces `council-verdict.md` · used by `council-director`, `council-synthesis-arbiter`

Produce the decision-grade output of a review.

## Procedure
1. State the overall verdict: approve, approve with conditions, or reject.
2. List blockers with owner, acceptance criterion, and failure scenario.
3. List improvements separately from blockers.
4. Record dissent verbatim, including minority positions.
5. State the deadline and who confirms the blockers are cleared.

## Output contract
`council-verdict.md` → `workspace/<venture-id>/council/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/council.tsv`.

## Quality bar
- Blockers have owners and acceptance criteria
- Dissent recorded verbatim
- The output states its confidence grade and names the evidence behind every load-bearing claim.
