---
name: alert-design
category: engineering
description: "Alert only when a human must act."
output: "alert-catalogue.md"
used_by:
  - observability-agent
---

# Alert Design

**Category:** `engineering` · **Output artifact:** `alert-catalogue.md`

## What this skill does
Alert only when a human must act.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `observability-agent`.

## Procedure
1. Alert on symptoms users would notice, not on internal causes.
2. Require every alert to have a runbook and an owner.
3. Set thresholds that avoid firing on normal variation.
4. Route by severity: page for urgent, ticket for the rest.
5. Delete alerts nobody has acted on in the last quarter.

## Output contract
Write `alert-catalogue.md` into `workspace/<venture-id>/engineering/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** alert-design
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
- Every alert has a runbook
- Unactioned alerts deleted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `engineering` category
- Designing for imagined scale instead of current load plus one order of magnitude.
- Skipping or quarantining a failing test to get a green build.
- Shipping without a verified way back.
