---
name: falsification-test-design
category: council
description: "Define what would prove the plan wrong."
output: "falsification-test.md"
used_by:
  - council-devils-advocate
---

# Falsification Test Design

**Category:** `council` · **Output artifact:** `falsification-test.md`

## What this skill does
Define what would prove the plan wrong.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-devils-advocate`.

## Procedure
1. State the claim precisely enough to be tested.
2. Define the observation that would disprove it.
3. Set the threshold and the timeframe.
4. Check the test is affordable and would actually be run.
5. If no falsifying observation exists, report that as the finding.

## Output contract
Write `falsification-test.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** falsification-test-design
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
- Threshold and timeframe both defined
- Unfalsifiable claims reported as findings
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
