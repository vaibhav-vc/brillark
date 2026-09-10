# Knowledge schema

Fourteen JSON Schemas. These are the contracts that make the organisation's memory usable months
later rather than a pile of markdown.

| Schema | What it holds |
|---|---|
| `memory-record` | One thing the organisation knows. Four types: episodic, semantic, procedural, decision. |
| `entity` | One canonical real-world thing, with typed relationships to others. |
| `decision-record` | A choice that constrains future work, with rejected options and a revisit trigger. |
| `council-verdict` | The output of a Council review: findings, severities, owners, dissent. |
| `context-package` | Everything an agent needs to start without rediscovering known facts. |
| `task` | One unit of work with exactly one owner and a definition of done. |
| `handoff` | A validated transfer of work between two agents. |
| `artifact` | Any skill output, registered so it becomes retrievable. |
| `assumption` | A belief the plan depends on, graded and load-scored. |
| `risk` | One entry in the enterprise register, with recoverability classified. |
| `business-model` | The nine canvas blocks, each with its own evidence grade. |
| `mvp-spec` | What ships, what waits, and the assumption the build tests. |
| `experiment` | A pre-registered test, so the analysis cannot be chosen after seeing the result. |
| `agent-profile` | The registry entry for one agent. |

## The constraints these encode

Several rules in this system are enforced by schema rather than by convention:

- A `memory-record` cannot exist without `provenance`, so an untraceable claim cannot enter memory.
- A `decision-record` requires `accepted_costs`, so a decision cannot pretend to be free.
- A council finding requires a `failure_scenario` of at least twenty characters, so an adjective
  cannot masquerade as a finding.
- An entity relationship requires a `source_artifact` and a type from a fixed list; `related_to`
  is deliberately not one of them.
- A `task` has one `owner`, not a list.
- An `mvp-spec` requires a `learning_justification` for every in-scope item.

`tests/test_system_integrity.py` checks that every schema parses, is self-describing, and never
requires a property it does not define.
