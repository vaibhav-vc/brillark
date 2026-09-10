# Workflows

Fourteen workflows. Each is a YAML file describing an ordered set of steps; each step names one agent,
the skills it uses, what it produces, and the condition under which the step is done.

These are definitions, not a runtime. The orchestration agents read them: `intake-router` picks the
workflow, `planning-decomposer` expands the steps into tasks, `dependency-scheduler` orders them, and
`progress-tracker` reports against the `done_when` conditions.

| Workflow | Stage | Owner |
|---|---|---|
| `00-intake` | any | `orchestration-head` |
| `01-business-model-design` | business-model | `business-head` |
| `02-market-validation` | validation | `business-head` |
| `03-mvp-definition` | mvp | `engineering-head` |
| `04-mvp-build` | mvp | `engineering-head` |
| `05-mvp-launch` | launch | `director` |
| `06-feedback-and-iterate` | launch | `cpo-agent` |
| `07-upgrade-and-scale` | upgrade | `director` |
| `08-council-review` | any | `council-director` |
| `09-memory-consolidation` | any | `orchestration-head` |
| `10-fundraise` | any | `cfo-agent` |
| `11-incident-response` | any | `ciso-agent` |
| `12-quarterly-planning` | any | `director` |
| `13-legal-and-compliance-baseline` | any | `general-counsel-agent` |

## Structure

```yaml
name: Business model design
stage: business-model
owner: business-head
purpose: <what this workflow is for>
steps:
  - id: size
    agent: market-researcher          # must exist in agents/registry.yaml
    skills: [market-sizing, ...]      # must exist in skills/registry.yaml
    does: <what happens in this step>
    produces: market-analysis.md
    done_when: <the checkable completion condition>
exit_criteria:
  - <what must be true for the workflow to be complete>
```

Every agent and skill reference is verified by `tests/test_system_integrity.py`, as is the rule that
stage-advancing workflows must route through the Council.
