---
name: accessibility-conformance-review
category: design
description: "Decide whether a surface meets the bar to ship."
output: "conformance-decision.md"
used_by:
  - design-head
---

# Accessibility Conformance Review

`design` · produces `conformance-decision.md` · used by `design-head`

Decide whether a surface meets the bar to ship.

## Procedure
1. Confirm the target level and which criteria apply to this surface.
2. Check the audit is current for the code actually shipping.
3. Treat unresolved failures as defects, not as enhancements.
4. Block release on failures that prevent task completion.
5. Record any accepted risk with an owner, a date, and a remediation plan.

## Output contract
`conformance-decision.md` → `workspace/<venture-id>/design/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/design.tsv`.

## Quality bar
- Task-blocking failures block release
- Accepted risks carry owner and date
- The output states its confidence grade and names the evidence behind every load-bearing claim.
