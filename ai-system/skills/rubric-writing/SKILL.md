---
name: rubric-writing
category: orchestration
description: "Define scoring criteria that different reviewers apply the same way."
output: "rubric.md"
used_by:
  - evaluation-harness-agent
---

# Rubric Writing

`orchestration` · produces `rubric.md` · used by `evaluation-harness-agent`

Define scoring criteria that different reviewers apply the same way.

## Procedure
1. Define the dimensions being scored and keep them independent.
2. Write anchor descriptions for each score level, with examples.
3. Test inter-rater agreement on a sample before adopting it.
4. Remove dimensions where reviewers disagree persistently.
5. Version the rubric and re-test when it changes.

## Output contract
`rubric.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Anchors have concrete examples
- Inter-rater agreement tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
