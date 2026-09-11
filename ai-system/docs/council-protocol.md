# Council protocol

Ten critics whose job is to find what is wrong with a plan before the organisation spends money
discovering it. The Council is chaired by `council-director` and produces exactly one artifact:
a `council-verdict`.

## The ten

| Agent | Attacks the plan on |
|---|---|
| `council-red-team` | How a competitor, an abuser, or an indifferent market kills it |
| `council-devils-advocate` | Whether the consensus was earned or assumed |
| `council-first-principles` | Whether the constraints are real or merely conventional |
| `council-assumption-auditor` | What the plan quietly believes, and how well evidenced it is |
| `council-risk-and-failure-modes` | How this fails, traced back to its earliest detectable signal |
| `council-ethics-and-responsibility` | Who is harmed, who is excluded, who never consented |
| `council-legal-and-regulatory-critic` | What the law and the platforms will actually permit |
| `council-economics-skeptic` | Whether the numbers survive recomputation and benchmarks |
| `council-expansion-scout` | Whether the plan is too *small* — the constructive half |
| `council-synthesis-arbiter` | Turning nine sets of findings into one decision-grade verdict |

## Submission

The Council refuses anything without a stated decision, an evidence pack, and a deadline. "Please
review this" is not a submission — review of what, to decide what, by when?

See `prompts/templates/council-submission.md`.

## Debate

Rounds of claim, challenge, evidence, rebuttal. Two rules keep it useful:

- **Someone is assigned to argue in favour.** A one-sided attack produces a plan that survives by
  attrition rather than by merit.
- **Unfalsifiable arguments are cut off.** If an objection cannot be made concrete, it is dropped.

## Severity

| Severity | Meaning | Requires |
|---|---|---|
| `blocker` | Proceeding is unsafe or would waste the budget | Owner, acceptance criterion, failure scenario, remedy |
| `major` | Materially reduces the chance of success | Failure scenario, remedy |
| `minor` | Worth fixing, not worth blocking | — |
| `note` | Observation for the record | — |

Severity is rated on consequence, not on how forcefully it was argued. `council-synthesis-arbiter`
normalises across critics so the same failure gets the same rating regardless of who found it.

## The verdict

One artifact, schema-validated: overall verdict, deduplicated findings with severities and owners,
expansion options, and **dissent recorded verbatim**. Minority positions stay on the record with the
evidence that would vindicate them. Today's dissent is often next quarter's incident.

## What the Council cannot do

- It cannot approve spend, merge work, or make the decision. It advises; the `director` decides.
- It cannot block indefinitely. Verdicts have deadlines and are delivered on time.
- It cannot re-litigate a resolved finding unless the evidence changed.

## Overruling a blocker

The Director may overrule any blocker. It must be written down, with the reasoning, in the decision
record. That written justification is what separates a deliberate risk from a lapse — and when a
blocker later proves right, the record is what makes the lesson learnable instead of arguable.

## The recurring-flaw register

`recurring-flaw-analysis` groups findings across reviews. A flaw appearing in three or more reviews is
traced to the agent, skill, or process that permits it, and fixed there. The Council's real output over
time is not verdicts — it is the guardrails that make those verdicts unnecessary.
