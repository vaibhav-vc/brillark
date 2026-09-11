---
name: duplicate-detection
category: orchestration
description: "Find out whether this request is already answered or already in flight before spending effort."
output: "duplicate-check.md"
used_by:
  - intake-router
---

# Duplicate Detection

`orchestration` · produces `duplicate-check.md` · used by `intake-router`

Find out whether this request is already answered or already in flight before spending effort.

## Procedure
1. Search semantic memory for the same question in different words.
2. Scan the live task graph for overlapping scope.
3. Compare against decision records — the answer may exist as a past decision.
4. If a near-match exists, report the delta rather than the whole answer.
5. Link the new request to the prior work instead of forking it.

## Output contract
`duplicate-check.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Memory and task graph both searched
- Near-matches reported as deltas, not reruns
- The output states its confidence grade and names the evidence behind every load-bearing claim.
