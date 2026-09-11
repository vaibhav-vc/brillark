---
name: accessibility-review
category: engineering
description: "Check the interface works for people who do not use it the default way."
output: "accessibility-report.md"
used_by:
  - council-ethics-and-responsibility
  - frontend-implementation-agent
---

# Accessibility Review

`engineering` · produces `accessibility-report.md` · used by `council-ethics-and-responsibility`, `frontend-implementation-agent`

Check the interface works for people who do not use it the default way.

## Procedure
1. Test keyboard-only navigation through every flow.
2. Check semantic structure, labels, and roles with a screen reader.
3. Verify colour contrast and that colour is never the only signal.
4. Check focus order, focus visibility, and error announcement.
5. Record findings against the conformance level being targeted.

## Output contract
`accessibility-report.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Keyboard-only path tested end to end
- Colour never the sole signal
- The output states its confidence grade and names the evidence behind every load-bearing claim.
