---
name: authz-design-review
category: engineering
description: "Check that permission logic is correct and cannot be bypassed."
output: "authz-review.md"
used_by:
  - security-engineer
---

# Authz Design Review

`engineering` · produces `authz-review.md` · used by `security-engineer`

Check that permission logic is correct and cannot be bypassed.

## Procedure
1. Map every resource and the actions possible on it.
2. Define who may do what, and check the default is deny.
3. Verify authorisation happens server-side on every path, including internal ones.
4. Test horizontal access: can one tenant reach another's data?
5. Treat authorisation code as high-risk and require a second reviewer.

## Output contract
`authz-review.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Default-deny verified
- Cross-tenant access tested
- The output states its confidence grade and names the evidence behind every load-bearing claim.
