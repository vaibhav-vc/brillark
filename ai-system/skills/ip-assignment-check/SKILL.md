---
name: ip-assignment-check
category: legal
description: "Verify the company actually owns what it built."
output: "ip-assignment-audit.md"
used_by:
  - general-counsel-agent
---

# Ip Assignment Check

`legal` · produces `ip-assignment-audit.md` · used by `general-counsel-agent`

Verify the company actually owns what it built.

## Procedure
1. List every contributor: founders, employees, contractors, and agencies.
2. Verify a signed assignment exists for each.
3. Check work created before incorporation is assigned in.
4. Check open-source and third-party components for ownership limits.
5. Close every gap before any diligence event.

## Output contract
`ip-assignment-audit.md` → `workspace/<venture-id>/legal/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/legal.tsv`.

## Quality bar
- Every contributor covered by a signed assignment
- Pre-incorporation work addressed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
