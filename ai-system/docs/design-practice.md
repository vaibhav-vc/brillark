# Design practice

Fifteen agents under `design-head`, plus `chief-design-officer-agent` at the executive table. The
domain exists because "the design" is not one job: research, structure, behaviour, words, craft,
accessibility, motion, brand, and service are different skills with different failure modes.

## The roster

| Agent | Owns |
|---|---|
| `design-researcher` | What people actually do, before anyone draws a screen |
| `usability-tester` | Whether real people can complete the task |
| `information-architect` | How things are organised, named, and found |
| `interaction-designer` | Flows, states, feedback, and what happens when it goes wrong |
| `visual-designer` | Hierarchy, layout, typography, craft |
| `design-system-architect` | Tokens, components, and design-to-code parity |
| `content-designer` | The words in the product, starting with the errors |
| `accessibility-designer` | That it works for people who do not use it the default way |
| `motion-designer` | Movement that explains change, and nothing else |
| `prototyper` | The cheapest artifact that answers the question |
| `brand-identity-designer` | The identity system, not just the logo |
| `data-visualization-designer` | Charts that answer a question honestly |
| `service-designer` | The whole experience, including the parts that are not a screen |
| `design-critic` | Critique argued on evidence rather than seniority |

Workflow: `workflows/14-design-delivery.yaml`. Handoff schema: `knowledge-schema/design-spec.schema.json`.

## The four rules the domain is built around

**All five states, every view.** Empty, loading, partial, error, success. The schema requires them
because the empty and error states are where products feel broken, and they are exactly what gets
skipped when a design is judged from a showcase screen.

**Accessibility is a build requirement, not remediation.** `accessibility-designer` annotates focus
order, names, roles, landmarks, and keyboard behaviour *before* engineering starts. A surface that
fails its conformance target is not done — it is a defect with a severity, not an enhancement request.

**Realistic content or it does not count.** The dense case with real data volumes, the longest string
in every supported language, the missing field, the smallest supported size. A design validated on
three tidy items has been validated against nothing.

**Critique against the stated goal.** The designer states the goal and the constraints before
showing anything; feedback outside that goal is discarded. Every objection must name who fails to do
what. `taste-versus-principle-separation` exists because the most expensive thing in design review
is an unexamined preference held by someone senior.

## Where design meets the rest of the organisation

- `design-head` → `engineering-head`: the spec is walked with the engineer who will build it, and
  ambiguities are resolved in that session rather than in tickets later.
- `accessibility-designer` → `council-ethics-and-responsibility`: exclusion findings are harms, and
  they go to the Council with remedies attached.
- `design-system-architect` → `frontend-implementation-agent`: token and component parity is audited
  in both directions, and fixed at whichever side is the source of truth.
- `data-visualization-designer` → `chief-data-officer-agent`: a chart may only show a metric that has
  one definition and one owner.
