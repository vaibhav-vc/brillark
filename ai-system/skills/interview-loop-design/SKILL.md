---
name: interview-loop-design
category: people
description: "Design an assessment that measures the scorecard rather than likeability."
output: "interview-loop.md"
used_by:
  - chro-agent
---

# Interview Loop Design

**Category:** `people` · **Output artifact:** `interview-loop.md`

## What this skill does
Design an assessment that measures the scorecard rather than likeability.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chro-agent`.

## Procedure
1. Assign each scorecard outcome to a specific interview stage.
2. Use work samples and structured questions rather than open conversation.
3. Define the evidence each interviewer must collect.
4. Require independent written assessment before any group discussion.
5. Review calibration: do the loop's scores predict actual performance?

## Output contract
Write `interview-loop.md` into `workspace/<venture-id>/people/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** interview-loop-design
- **Author agent:** <agent-id>
- **Date:** <ISO-8601>
- **Confidence:** measured | sourced | benchmarked | estimated | guessed

## Summary
<the answer in three sentences or fewer>

## Body
<the substance produced by the procedure above>

## Evidence
| Claim | Source | Grade |
|---|---|---|

## Open questions
<what remains unknown, and who could answer it>

## Next action
<the single next step and its owner>
```

## Quality bar
- Every outcome assigned to a stage
- Independent assessment before discussion
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `people` category
- Writing a job advertisement before writing the outcomes the role must produce.
- Assessing candidates on different evidence and calling it judgement.
- Hiring to relieve a bottleneck that process or tooling would fix faster.
