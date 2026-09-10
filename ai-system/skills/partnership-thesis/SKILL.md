---
name: partnership-thesis
category: gtm
description: "State why a partnership would create value before pursuing one."
output: "partnership-thesis.md"
used_by:
  - chief-strategy-officer-agent
  - partnership-bd-agent
---

# Partnership Thesis

**Category:** `gtm` · **Output artifact:** `partnership-thesis.md`

## What this skill does
State why a partnership would create value before pursuing one.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-strategy-officer-agent`, `partnership-bd-agent`.

## Procedure
1. Name the specific gap: distribution, capability, or credibility.
2. Describe what a partner gains, in their terms and their metrics.
3. Identify the partner types that have both the asset and the incentive.
4. Estimate the value created and how it would be shared.
5. Define what would prove the thesis wrong within one quarter.

## Output contract
Write `partnership-thesis.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** partnership-thesis
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
- Partner's own incentive articulated
- Disproof condition set within a quarter
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
