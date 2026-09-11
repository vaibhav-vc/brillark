---
name: security-review
category: engineering
description: "Review a change for security consequences before it ships."
output: "security-review.md"
used_by:
  - ciso-agent
---

# Security Review

`engineering` · produces `security-review.md` · used by `ciso-agent`

Review a change for security consequences before it ships.

## Procedure
1. Check what new data, surface, or privilege the change introduces.
2. Review authentication, authorisation, and input handling on new paths.
3. Check dependencies added and their provenance.
4. Verify secrets and configuration are handled correctly.
5. Block on unmitigated critical findings; record any accepted risk.

## Output contract
`security-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- New surface explicitly identified
- Critical findings block the release
- The output states its confidence grade and names the evidence behind every load-bearing claim.
