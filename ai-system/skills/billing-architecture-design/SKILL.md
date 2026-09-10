---
name: billing-architecture-design
category: finance
description: "Design the plumbing that turns pricing into collected cash."
output: "billing-architecture.md"
used_by:
  - billing-systems-designer
---

# Billing Architecture Design

**Category:** `finance` · **Output artifact:** `billing-architecture.md`

## What this skill does
Design the plumbing that turns pricing into collected cash.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `billing-systems-designer`.

## Procedure
1. Model the pricing in the billing data model before writing any code.
2. Define plans, entitlements, and the metering source of truth.
3. Design proration, upgrades, downgrades, and refunds explicitly.
4. Specify the tax determination path per jurisdiction.
5. Define reconciliation between billing and the ledger, and alarm on drift.

## Output contract
Write `billing-architecture.md` into `workspace/<venture-id>/finance/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** billing-architecture-design
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
- Proration and refunds specified up front
- Automated reconciliation defined
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `finance` category
- Presenting a single number where the honest answer is a range.
- Building a forecast from a growth percentage instead of from drivers.
- Reporting a metric whose definition changed since last period without saying so.
