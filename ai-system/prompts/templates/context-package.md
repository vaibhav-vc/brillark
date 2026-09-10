# Context package

Attach this to every task. The receiving agent should not need to ask you anything.

```yaml
task_id: task_<slug>
brief: |
  <what is being asked, and the decision it supports>
definition_of_done:
  - <checkable condition>
  - <checkable condition>
input_artifacts: [art_<id>]
relevant_memory: [mem_<id>]
accepted_assumptions:
  - <assumption already agreed, so it is not re-argued>
constraints:
  - <budget, deadline, technical or legal constraint>
open_questions:
  - <carried forward; never trimmed for tidiness>
budget:
  wall_clock_minutes: 60
  tokens: 120000
  on_exhaustion: stop_and_escalate
prior_attempts: [art_<id>]
```

Validates against `knowledge-schema/context-package.schema.json`.
