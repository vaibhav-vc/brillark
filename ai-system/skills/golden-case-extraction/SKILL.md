---
name: golden-case-extraction
category: improvement
description: "Turn a real failure into a test that stops it recurring."
output: "golden-case.md"
used_by:
  - failure-miner
---

# Golden Case Extraction

**Category:** `improvement` · **Output artifact:** `golden-case.md`

## What this skill does
Turn a real failure into a test that stops it recurring.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `failure-miner`.

## Procedure
1. Take the actual inputs and context from the failure.
2. Define what the correct output would have been, and why.
3. Strip anything sensitive while preserving the difficulty.
4. Verify the case fails against the current behaviour.
5. Add it to the suite with its provenance recorded.

## Output contract
Write `golden-case.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** golden-case-extraction
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
- Case verified to fail before the fix
- Provenance recorded with each case
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
