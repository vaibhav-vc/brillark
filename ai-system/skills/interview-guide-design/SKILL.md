---
name: interview-guide-design
category: market
description: "Write questions that produce evidence instead of politeness."
output: "interview-guide.md"
used_by:
  - customer-discovery-interviewer
---

# Interview Guide Design

**Category:** `market` · **Output artifact:** `interview-guide.md`

## What this skill does
Write questions that produce evidence instead of politeness.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `customer-discovery-interviewer`.

## Procedure
1. Start from the hypotheses being tested, riskiest first.
2. Convert each into a behavioural question about a specific past instance.
3. Remove every leading question and every yes/no question.
4. Order from broad context to specific probe.
5. Include the questions that could disconfirm your hypothesis.

## Output contract
Write `interview-guide.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** interview-guide-design
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
- No leading questions remain
- Disconfirming questions included
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
