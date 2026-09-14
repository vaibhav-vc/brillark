# The first real run — findings

Until this run, no agent in this organisation had ever been executed. The definitions were tested
for internal consistency and the *output* was entirely unvalidated. This is what happened when it
was actually used, and what it broke.

**Venture:** `laundro` — a subscription service collecting, washing and returning bedding and
towels for short-term rental hosts in Manchester. Chosen because it is mundane, has real unit
economics, and plausibly is not a good business. A softball would have proved nothing.

**Workflow:** `01-business-model-design`, step 1 of 8 (`market-researcher`, market sizing).

**Executed by:** Claude Opus 5, following the assembled context the loader produced. The same model
also assessed the output, which is the limitation `eval.py` refuses to automate — a model scoring
itself measures agreement, not quality. Treat these findings as a working session, not an
independent evaluation.

---

## Finding 1 — the orchestrator ignored its own findings

The market-sizing artifact concluded, in its required Next action field:

> **Do not proceed to pricing or unit economics on this sizing.**

The runner then offered step 2, and would have offered pricing and economics in turn. The system
had a schema for open questions, a required Next action field, and escalation criteria in every
charter — and **no mechanism at all for an artifact's finding to change what happens next**.

The contract was enforced on *form* (does the artifact have the right sections) and not on
*consequence* (does what it says alter the plan). That is the difference between a checklist and a
control.

**Fixed.** An artifact may now declare a machine-readable block:

```blocks
blocks: [pricing, economics]
reason: Sizing rests on three guessed load-bearing inputs.
resolved_by: [source-verifier, data-sourcing-analyst, customer-discovery-interviewer]
```

`run_workflow.py` records it, refuses to mark blocked steps done, skips them in `next`, and requires
`unblock --evidence '<what changed>'` to clear — which is recorded. Guarded by four tests.

## Finding 2 — the system accepted my own overclaim

`skills/OUTPUT_CONTRACT.md` rule 5 states plainly:

> The confidence grade is the artifact's, not the author's mood. It is the weakest grade among the
> claims the conclusion actually rests on.

The artifact I wrote declared `Confidence: estimated` while its own evidence table contained **four
`guessed` inputs, three of them load-bearing**. The rule was written down, in the file every skill
points at, and **nothing checked it**. The runner accepted the artifact.

This is the more serious of the two findings. The system's entire claim to trustworthiness rests on
evidence grading, and the grade was decorative.

**Fixed.** `run_workflow.py` now parses the Evidence table and refuses any artifact whose stated
confidence exceeds the weakest load-bearing grade, naming the offending claim:

```
REFUSED — market-analysis.md does not meet the output contract:
  - confidence 'estimated' overstates the evidence: a load-bearing claim is graded 'guessed'.
      weakest load-bearing claim: Share of listings held by 1-3 property hosts
```

Rows explicitly marked `(not load-bearing)` are excluded. Understating confidence is allowed —
caution is not a contract breach. Five tests.

## Finding 3 — memory doctrine fought research doctrine

Recording the real market data surfaced a design conflict between two parts of the system that had
never met.

Three commercial vendors report Manchester active listings as **6,951 / 2,453 / 1,665** — a 4.2x
spread. Writing the first two to memory triggered the contradiction detector, which demanded one be
superseded.

But the research domain's own `multi-source-synthesis` skill says:

> Preserve genuine disagreement explicitly rather than averaging it away.

Both are right, about different situations. **Two sources disagreeing is a finding to preserve.
Memory contradicting itself is a conflict to resolve.** The memory store could not tell them apart,
and would have destroyed a real finding to satisfy a consistency rule.

**Fixed.** `memory.py` now detects *attribution* — "AirDNA reported X" is attributed, "X is true" is
not. Differently-attributed conflicting claims are offered `--contest`, which stores both, marks
them mutually contested, and **requires a note explaining why they differ**. Both stay retrievable;
any agent recalling either sees the disagreement and the reason. Five tests.

```
[estimated] AirROI reported 1665 active listings...   [CONTESTED with 1 other claim(s)]
    disagreement: AirDNA counts Airbnb+Vrbo+Booking.com; AirROI counts Airbnb only.
                  Neither publishes its definition of 'active'. The 4.2x spread is unresolved.
```

## Finding 4 — the headline efficiency claim was a strawman

The repository claimed "~88x cheaper per run". That compares against loading all 629 skills, which
no sane runtime would do. Beating a strawman proves nothing.

**Corrected.** The honest baseline is one well-written general-purpose system prompt (~5,000
tokens). Against that, a routed run is **about 1.6x — comparable, not dramatic**. What tiering
actually buys is that 138 specialised agents stay affordable at roughly the cost of one generalist.
Capability per token, not raw savings. `measure_context_cost.py` now prints both and says which is
the strawman.

---

## Finding 5 — a block could land on a step already marked done, and the run stayed inconsistent

Running `competition` after `size` produced the first case where a later step's finding contradicts
an *earlier, completed* one, rather than a future one. `competitive-map.md` found the venture's
stated market gap does not exist, which invalidates the reasoning `market-analysis.md` was built on
— not just the steps ahead of it. `run_workflow.py` recorded the new block correctly but left `size`
marked `done`, with its artifact still counted toward progress. `status` would have shown a step both
finished and contradicted at once, and nothing stopped `unblock` from later clearing `pricing` and
`economics` by citing `size`'s own reasoning — the very reasoning that had just been overturned.

**Fixed.** A block landing on a completed step now reopens it: `status = invalidated`, the artifact
path moves to `superseded_artifact` (kept, not deleted — it is the record of what was believed and
why it was wrong), and it stops counting as done. Any block that step itself declared is flagged
`declared_by_invalidated`, and `unblock` refuses to clear such a block until the invalidated step is
redone. `next` now hands a gate step the run's full health — every open block and every invalidated
step — as mandatory input rather than presenting a broken run as though it were routine. Nine tests.

## Finding 6 — the load-bearing marker could be gamed from the wrong cell

Rule 5's exemption ("rows marked `not load-bearing` don't cap confidence") was implemented as a
substring check across the whole table row, which meant the marker could appear in the *Source*
column — an author explaining, in prose, why a claim shouldn't count — and it would work exactly like
the deliberate marker rule 6 was meant to require. That is the confidence check's own escape hatch,
reachable by accident.

**Fixed.** OUTPUT_CONTRACT.md now documents rule 6 explicitly with two sanctioned forms — a
`Load-bearing` column, or `(not load-bearing)` inside the claim or grade cell — and the parser reads
the marker only from those, never from Source-column prose. Four tests, including one that writes
"this figure explains why it is not load-bearing" into a Source cell and confirms the claim still
counts.

## Finding 7 — "schema-valid verdict" was never actually checked

Every workflow step's `done_when` is prose a human reads; `run_workflow.py done` never parsed it, and
`council-verdict.md`'s `done_when: Schema-valid verdict exists` had no schema check behind it at all.
The council step would have passed on any markdown file with the right sections and confidence
grade, `approve` written over its own blocker findings included — the exact failure the Council
exists to prevent, undetectable in its own output format. There was also no schema validator in the
toolchain: the 22 knowledge schemas were written and never checked against a real document, because
`jsonschema` is not a dependency here.

**Fixed.** `tools/validate.py` is a small draft-2020-12 validator covering the keyword subset the
schemas actually use (confirmed by a full sweep of all 22 schema files) and failing loudly on
anything else. `run_workflow.py done` now matches a step's `produces` filename against a schema of
the same name, requires a fenced ` ```<schema-name> ` block carrying the machine-readable record, and
validates it. `council-verdict.schema.json` gained two `allOf`/`if`/`then` rules making the Council's
core discipline load-bearing in the schema itself, not just in prose: a verdict cannot be `approve`
while any finding is a `blocker`, and `approve_with_conditions` requires at least one finding. Six
new schema-integrity tests plus nineteen tests for the validator itself.

The real `council-verdict.md` produced for `laundro` (reject, three blockers, two majors, one
recorded dissent) validates clean against the hardened schema.

## What the system got right

Worth recording, because it would be easy to read the above as a failure.

- **It forced honesty about the evidence.** Following `market-sizing` and `source-grading` made the
  4.2x vendor spread impossible to paper over. A quicker analysis would have picked one number.
- **It caught a contradiction I had not noticed.** One source reports listings **down 44.1%** while
  revenue is **up 104.6%**. Those are hard to reconcile, and the why-now claim in the venture brief
  depends on supply *growing*. The system surfaced that the brief's premise may be backwards.
- **The output contract's required fields did real work.** "Open questions" and "Next action" are
  where the blocking finding came from. Without them the artifact would have ended at the numbers.
- **The budget enforcement was never the binding constraint.** Every step ran at ~4,900 of 15,000
  tokens. The efficiency work was not the hard part; the honesty machinery was.

This session also ran `competition` and `council` — two more of the eight `01-business-model-design`
steps, and the first time any step reached the Council. Both surfaced real defects (Findings 5–7
above) before either could be trusted.

## What is still not validated

- Two of eight steps remain unattempted (`jobs`, `value`, `model` are blocked pending F1/F2 below;
  `pricing` and `economics` stay blocked behind a redone `size`). Eighteen other workflows are
  entirely untouched.
- The model executing and the model assessing were the same. This is a working session, not an eval.
- The hardware, legal and compliance domains remain unreviewed by anyone qualified in them.
- The eval suite still has never been run against a model.
- The Council's own verdict schema is new as of this run (Finding 7) and has been exercised on
  exactly one real verdict. It has not yet been tried against a genuinely close call — a plan with
  only minor findings, where `approve` is the correct verdict and the schema must permit it.
