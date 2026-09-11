---
name: secrets-management
category: engineering
description: "Keep credentials out of reach and rotatable."
output: "secrets-policy.md"
used_by:
  - security-engineer
---

# Secrets Management

`engineering` · produces `secrets-policy.md` · used by `security-engineer`

Keep credentials out of reach and rotatable.

## Procedure
1. Inventory every secret and where it is used.
2. Move all secrets into a managed store with access control.
3. Scan the repository history, not just the current state.
4. Define and actually run a rotation schedule.
5. Ensure secrets never appear in logs, errors, or client bundles.

## Output contract
`secrets-policy.md` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Repository history scanned
- Rotation schedule actually executed
- The output states its confidence grade and names the evidence behind every load-bearing claim.
