# Stage gate decision

Only the `director` writes this.

```markdown
# Stage gate: <from-stage> -> <to-stage>
- **Venture:** <venture-id>  **Date:** <ISO-8601>

## Decision
go | no-go | pivot | kill

## Exit criteria
| Criterion | Met | Evidence |
|---|---|---|

## Council verdict
ver_<id> — <approve | approve_with_conditions | reject>. Blockers cleared: <list>.

## The evidence that decided this
<what actually moved the decision>

## What would reverse it
<the observation that would change this decision>

## Mandates issued
| Head | Mandate | Budget | Definition of done |
|---|---|---|---|
```
