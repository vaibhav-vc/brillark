---
name: legal-risk-register
category: legal
description: "Track legal exposure in one place."
output: "legal-risk-register.md"
used_by:
  - general-counsel-agent
---

# Legal Risk Register

`legal` · produces `legal-risk-register.md` · used by `general-counsel-agent`

Track legal exposure in one place.

## Procedure
1. Record each exposure with the activity that creates it.
2. Rate likelihood and potential consequence.
3. Record the current mitigation and its owner.
4. Distinguish exposures we can manage from those needing counsel.
5. Review when entering a new market or launching a new capability.

## Output contract
`legal-risk-register.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Exposure tied to a specific activity
- Counsel-grade items separated
- The output states its confidence grade and names the evidence behind every load-bearing claim.
