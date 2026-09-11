---
name: negative-result-reporting
category: improvement
description: "Report what did not work, as prominently as what did."
output: "negative-results.md"
used_by:
  - ab-test-runner
---

# Negative Result Reporting

**Category:** `improvement` · **Output artifact:** `negative-results.md`

## What this skill does
Report what did not work, as prominently as what did.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `ab-test-runner`.

## Procedure
1. Report failed variants with the hypothesis they tested.
2. State what the negative result rules out.
3. Record it so the same variant is not retried blindly.
4. Resist reframing a null result as a partial success.
5. Feed the learning into the next round of variants.

## Output contract
Write `negative-results.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** negative-result-reporting
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
- Null results not reframed as partial success
- Ruled-out hypotheses recorded
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
