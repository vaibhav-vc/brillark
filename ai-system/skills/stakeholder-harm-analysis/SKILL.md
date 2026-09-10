---
name: stakeholder-harm-analysis
category: council
description: "Identify who could be harmed, including those who never chose to be involved."
output: "harm-analysis.md"
used_by:
  - council-ethics-and-responsibility
---

# Stakeholder Harm Analysis

**Category:** `council` · **Output artifact:** `harm-analysis.md`

## What this skill does
Identify who could be harmed, including those who never chose to be involved.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `council-ethics-and-responsibility`.

## Procedure
1. List every affected group, including non-users and third parties.
2. For each, identify the plausible harm and its severity.
3. Pay attention to groups with the least power to object.
4. Distinguish harms inherent to the product from harms caused by its design.
5. Propose a remedy for each identified harm.

## Output contract
Write `harm-analysis.md` into `workspace/<venture-id>/council/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** stakeholder-harm-analysis
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
- Non-users and third parties included
- Remedy proposed per harm
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `council` category
- An objection stated as an adjective rather than a concrete failure sequence.
- Criticism offered with no remedy at any cost level.
- Averaging two positions instead of testing which survives the evidence.
