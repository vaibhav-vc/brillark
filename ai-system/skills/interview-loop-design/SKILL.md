---
name: interview-loop-design
category: people
description: "Design an assessment that measures the scorecard rather than likeability."
output: "interview-loop.md"
used_by:
  - chro-agent
---

# Interview Loop Design

`people` · produces `interview-loop.md` · used by `chro-agent`

Design an assessment that measures the scorecard rather than likeability.

## Procedure
1. Assign each scorecard outcome to a specific interview stage.
2. Use work samples and structured questions rather than open conversation.
3. Define the evidence each interviewer must collect.
4. Require independent written assessment before any group discussion.
5. Review calibration: do the loop's scores predict actual performance?

## Output contract
`interview-loop.md` → `workspace/<venture-id>/people/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/people.tsv`.

## Quality bar
- Every outcome assigned to a stage
- Independent assessment before discussion
- The output states its confidence grade and names the evidence behind every load-bearing claim.
