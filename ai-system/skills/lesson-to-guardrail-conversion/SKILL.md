---
name: lesson-to-guardrail-conversion
category: orchestration
description: "Turn a lesson into a constraint that prevents the repeat automatically."
output: "guardrail-change.md"
used_by:
  - retrospective-agent
---

# Lesson To Guardrail Conversion

`orchestration` · produces `guardrail-change.md` · used by `retrospective-agent`

Turn a lesson into a constraint that prevents the repeat automatically.

## Procedure
1. State the failure precisely enough to recognise it happening again.
2. Identify the artifact that could have prevented it: a guardrail, a checklist line, a skill step, or a test.
3. Write the change into that artifact directly.
4. Add a detection signal so a recurrence is visible early.
5. Verify at the next retrospective that the guardrail held.

## Output contract
`guardrail-change.md` → `workspace/<venture-id>/orchestration/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/orchestration.tsv`.

## Quality bar
- Change written into a real artifact
- Detection signal added
- The output states its confidence grade and names the evidence behind every load-bearing claim.
