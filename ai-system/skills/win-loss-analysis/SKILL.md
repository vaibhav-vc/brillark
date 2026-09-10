---
name: win-loss-analysis
category: gtm
description: "Find out why deals were actually won and lost."
output: "win-loss-report.md"
used_by:
  - chief-revenue-officer-agent
  - sales-playbook-agent
---

# Win Loss Analysis

**Category:** `gtm` · **Output artifact:** `win-loss-report.md`

## What this skill does
Find out why deals were actually won and lost.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `chief-revenue-officer-agent`, `sales-playbook-agent`.

## Procedure
1. Interview the buyer, not only the seller — their accounts differ.
2. Record the decisive factor, not the polite reason.
3. Classify losses: product gap, price, timing, trust, or process failure.
4. Count patterns across deals rather than reacting to the last loss.
5. Route product-caused losses to product with evidence.

## Output contract
Write `win-loss-report.md` into `workspace/<venture-id>/gtm/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** win-loss-analysis
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
- Buyer interviewed, not just the seller
- Losses classified and counted
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `gtm` category
- Scaling a channel before its CAC is measured.
- Running a test with no kill criterion, so it never ends.
- Claiming differentiation that is not a reason anyone would switch.
