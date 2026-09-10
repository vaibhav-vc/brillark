---
name: reachability-mapping
category: market
description: "Establish where the ICP actually is and what it costs to get there."
output: "reachability.md"
used_by:
  - icp-persona-builder
---

# Reachability Mapping

**Category:** `market` · **Output artifact:** `reachability.md`

## What this skill does
Establish where the ICP actually is and what it costs to get there.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `icp-persona-builder`.

## Procedure
1. List the channels where this ICP demonstrably gathers or can be targeted.
2. Estimate reachable volume and cost per contact for each.
3. Check for gatekeepers and access constraints.
4. Test one channel cheaply before assuming access.
5. Report reachable volume against the SOM claim.

## Output contract
Write `reachability.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** reachability-mapping
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
- Access tested, not assumed
- Reachable volume compared to SOM
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
