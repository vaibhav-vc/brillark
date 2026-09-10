---
name: business-continuity-plan
category: risk
description: "Plan for continuing to operate through a serious disruption."
output: "continuity-plan.md"
used_by:
  - chief-risk-officer-agent
---

# Business Continuity Plan

**Category:** `risk` · **Output artifact:** `continuity-plan.md`

## What this skill does
Plan for continuing to operate through a serious disruption.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-risk-officer-agent`.

## Procedure
1. Identify the functions that must continue and their maximum tolerable downtime.
2. Identify the dependencies each requires: people, systems, and suppliers.
3. Define the alternative arrangement for each dependency.
4. Define activation triggers and who declares them.
5. Test the plan; an untested continuity plan is a document, not a capability.

## Output contract
Write `continuity-plan.md` into `workspace/<venture-id>/risk/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** business-continuity-plan
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
- Maximum tolerable downtime defined per function
- Plan tested, not just written
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `risk` category
- A risk register that ranks by how loudly a risk was raised.
- Accepting a terminal risk implicitly by never classifying it.
- A continuity plan that has never been tested.
