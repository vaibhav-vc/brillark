---
name: capability-mapping
category: improvement
description: "Know what the organisation can and cannot currently do."
output: "capability-map.md"
used_by:
  - capability-gap-scout
---

# Capability Mapping

**Category:** `improvement` · **Output artifact:** `capability-map.md`

## What this skill does
Know what the organisation can and cannot currently do.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `capability-gap-scout`.

## Procedure
1. List the capabilities the current workflows require.
2. Map each to the agent and skills that provide it.
3. Mark capabilities with no owner and those with only one.
4. Mark capabilities provided but never exercised.
5. Publish the map so gaps are visible before they cause failures.

## Output contract
Write `capability-map.md` into `workspace/<venture-id>/improvement/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** capability-mapping
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
- Unowned and single-owner capabilities marked
- Unexercised capabilities identified
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `improvement` category
- Starting an improvement cycle with an idea instead of a measurement.
- Adopting a change that beat the cases it was tuned on.
- Adding an instruction without removing one, until none of them are read.
