# Self-improvement

The organisation is supposed to get better at its job over time. The `improvement` domain owns that
loop: thirteen agents under `improvement-head`, with `chief-learning-officer-agent` holding the
boundary on what the system may change about itself.

## The loop

```
  measure ──> mine ──> rank ──> diagnose ──> propose ──> trial ──> sweep
                                                                     │
     verify <── distil <── adopt <── authorise <────────────────────┘
       │
       └──> (reverted changes re-open the problem in the backlog)
```

Defined in `workflows/15-self-improvement.yaml`. Each arrow is a gate, not a suggestion.

| Step | Agent | The gate |
|---|---|---|
| Measure | `agent-performance-analyst` | Three cycles of data; failure attributed to capability, context, or task definition |
| Mine | `failure-miner` | Three independent instances before anything is called a pattern |
| Cases | `benchmark-curator` | The case is verified to fail *before* the fix exists |
| Rank | `improvement-head` | Ranked by expected value; the below-the-line list is published |
| Diagnose | `improvement-head` | Context and task-definition causes ruled out before any prompt is edited |
| Propose | `prompt-optimizer` | One dimension per variant; a *removal* variant always included; threshold fixed first |
| Trial | `ab-test-runner` | Full planned sample, no early stopping, negative results reported |
| Sweep | `prompt-optimizer` | Per-case comparison; an unexplained regression blocks adoption |
| Authorise | `improvement-head` | Authorisation level must match the artifact class |
| Adopt | `improvement-head` | One change at a time per agent; delta and sample logged |
| Distil | `knowledge-distiller` | Instruction length flat or falling — every addition pays for itself with a removal |
| Verify | `improvement-head` | Did last cycle's change hold? If not, revert |
| Return | `chief-learning-officer-agent` | Did the improvement effort pay for itself, counting reversions as cost |

## The five failure modes it is built against

**Editing the prompt for a context problem.** Most "the agent got it wrong" is "the agent was never
given the information". `failure-attribution` rules out context and task definition first, because
rewriting a prompt to compensate for missing context makes the system worse and buries the cause.

**Measuring on the cases you tuned on.** A variant scored against the cases that shaped it has been
measured against nothing. Splits are made before variant generation and audited for leakage.

**Instruction accretion.** Every cycle wants to add a line. After twenty cycles nothing is read.
`knowledge-distiller` pairs every addition with a removal and tracks total length as a metric.

**Optimisation drift.** A system tuned on its own metrics will eventually score well at something
nobody wanted. `optimisation-drift-detection` compares metric movement against the real outcomes the
metrics proxy, and reports when they part company.

**Improving into a corner.** A change that helps the targeted case and quietly breaks two others
looks like progress in the aggregate. The regression sweep compares per case, and aggregate-only
comparison is explicitly disallowed.

## The boundary

The system may not change what counts as success. Full table in
`prompts/system/06-self-modification.md`; the short version:

- **Automatic** (with a passing trial and clean sweep): prompt wording, skill steps.
- **Director approval**: workflows, agent charters.
- **Human founder approval**: guardrails, schemas, org shape, and **evaluation criteria**.

`self-modification-policy` logs every change with its authorisation level and refuses unauthorised
ones. `capability-gap-scout` must route any new-agent proposal to the director, and is explicitly
rewarded for recommending *against* filling a gap — sprawl is the default failure mode of a system
that can propose its own extensions.

## What it produces

- `improvement-proposal` records — diagnosis, one-dimension change, trial result, authorisation.
- `agent-performance` records — outcome and process compliance scored separately, with a trend that
  reads `insufficient_data` until three comparable cycles exist.
- A golden case for every expensive failure, so nothing recurs silently.

## Sources

- [SePO: Self-Evolving Prompt Agent for System Prompt Optimization](https://arxiv.org/pdf/2606.04465)
- [Self-improving LLM evaluation: feedback loops & eval iteration — Arize](https://arize.com/resources/llm-evaluation/self-improving-llm-evaluation/)
- [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/pdf/2607.07663)
- [Build Self-Optimizing AI Agents — Future AGI](https://futureagi.com/blog/agent-optimize-webinar-2025/)
