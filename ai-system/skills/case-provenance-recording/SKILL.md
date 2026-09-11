---
name: case-provenance-recording
category: improvement
description: "Record where each case came from and why its answer is right."
output: "case-provenance.md"
used_by:
  - benchmark-curator
---

# Case Provenance Recording

**Category:** `improvement` · **Output artifact:** `case-provenance.md`

## What this skill does
Record where each case came from and why its answer is right.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `benchmark-curator`.

## Procedure
1. Record the source: a real task, a real failure, or a constructed edge case.
2. Record why the expected output is correct, in enough detail to be challenged.
3. Record who decided and when.
4. Note anything sanitised and whether difficulty was preserved.
5. Link the case to the failure it came from, where applicable.

## Output contract
Write `case-provenance.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** case-provenance-recording
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
- Correctness justified, not just asserted
- Sanitisation noted with difficulty preserved
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
