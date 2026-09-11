---
name: openapi-specification
category: engineering
description: "Specify the interface formally so clients and tests can be generated."
output: "openapi.yaml"
used_by:
  - api-designer
---

# Openapi Specification

`engineering` · produces `openapi.yaml` · used by `api-designer`

Specify the interface formally so clients and tests can be generated.

## Procedure
1. Define every endpoint, parameter, and response schema explicitly.
2. Specify required versus optional fields and their constraints.
3. Document every error response with its condition.
4. Include realistic examples for each operation.
5. Validate the specification and keep it as the source of truth.

## Output contract
`openapi.yaml` → `workspace/<venture-id>/engineering/`, registered as an artifact record.
Shared format and required fields: `skills/OUTPUT_CONTRACT.md`.
Anti-patterns for this category head `skills/index/engineering.tsv`.

## Quality bar
- Error responses fully specified
- Specification is the source of truth
- The output states its confidence grade and names the evidence behind every load-bearing claim.
