# Handoff record

Work is not transferred until the receiver accepts it.

```yaml
id: ho_<slug>
from_agent: <agent-id>
to_agent: <agent-id>
artifact: art_<id>
dod_met:
  - criterion: <the condition>
    met: true
    evidence: <where to look>
assumptions_stated:
  - <assumption the receiver is inheriting>
open_questions:
  - <still unresolved>
status: offered   # offered | accepted | rejected
rejection_reason: <the specific missing element — never a general complaint>
```

A rejected handoff goes back with one specific gap named. Do not silently repair someone else's work.
