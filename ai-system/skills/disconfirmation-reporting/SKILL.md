---
name: disconfirmation-reporting
category: market
description: "Report the evidence against your hypothesis first."
output: "disconfirmation-report.md"
used_by:
  - customer-discovery-interviewer
---

# Disconfirmation Reporting

**Category:** `market` · **Output artifact:** `disconfirmation-report.md`

## What this skill does
Report the evidence against your hypothesis first.

## When to use it
Invoke this skill when the task calls for the outcome described above.
It is part of the standing toolkit of: `customer-discovery-interviewer`.

## Procedure
1. List what you expected to find before the research.
2. Report what contradicted it, in full, before reporting confirmation.
3. Assess whether the contradiction is fatal, partial, or explainable.
4. Update the hypothesis explicitly rather than quietly.
5. Record the update so the learning log shows what changed.

## Output contract
Write `disconfirmation-report.md` into `workspace/<venture-id>/market/`, then register it as an artifact record
(`knowledge-schema/artifact.schema.json`) so it becomes retrievable memory. Every output carries:

```markdown
# <title>
- **Skill:** disconfirmation-reporting
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
- Contradicting evidence reported first
- Hypothesis updated explicitly
- The output states its confidence grade and names the evidence behind every load-bearing claim.

## Anti-patterns for the `market` category
- Treating stated intent as evidence of demand.
- Sizing a market top-down and calling it bottom-up.
- Interviewing people who could never buy, then counting their enthusiasm.
