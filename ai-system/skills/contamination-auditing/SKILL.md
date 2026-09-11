---
name: contamination-auditing
category: improvement
description: "Check the measurement set has not leaked into development."
output: "contamination-audit.md"
used_by:
  - benchmark-curator
---

# Contamination Auditing

**Category:** `improvement` · **Output artifact:** `contamination-audit.md`

## What this skill does
Check the measurement set has not leaked into development.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `benchmark-curator`.

## Procedure
1. Compare tuning and held-out sets for overlapping or near-duplicate cases.
2. Check whether held-out cases appear in any prompt or example.
3. Check whether results improved suspiciously fast after a variant round.
4. Quarantine any contaminated case and rebuild the split.
5. Record the audit and its outcome.

## Output contract
Write `contamination-audit.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** contamination-auditing
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
- Near-duplicates checked, not just exact matches
- Contaminated cases quarantined and split rebuilt
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
