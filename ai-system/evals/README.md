# Evals

The claim "this produces better output" is worth nothing unless it is measured. This directory is
how it gets measured, on any model, without this repository knowing which model you use.

```bash
python3 ai-system/tools/eval.py --dry-run           # validate the harness with no model at all
python3 ai-system/tools/eval.py --list              # what is covered
python3 ai-system/tools/eval.py --runner mymodule:call   # run against your model
```

## How it works

A **case** (`cases/*.yaml`) is a real task given to a named agent, with the properties its output
must have. A **rubric** scores those properties on an anchored scale. The **runner** is a function
you supply — the harness never imports a provider SDK, so it works with anything that can take a
string and return a string.

```python
# mymodule.py
def call(prompt: str, model: str) -> str:
    ...  # your provider, your auth, your retries
    return response_text
```

```bash
python3 ai-system/tools/eval.py --runner mymodule:call --profile anthropic
```

The harness assembles each case's context through `tools/loader.py` — the same code path a real run
uses — so what is scored is the actual contract, not an idealised version of it.

## Why the cases look like this

Every case tests something the organisation claims about itself, and each one is designed so a
plausible-sounding wrong answer fails:

- **Load-bearing guesses.** Does the agent grade a number it cannot source as `guessed`, or does it
  state it confidently because it sounds reasonable?
- **Return discipline.** Does it return a decision and artifact paths within budget, or dump its
  working context?
- **Refusal to widen scope.** Given an obvious adjacent improvement, does it recommend or silently do?
- **Disconfirming evidence first.** Does it lead with what contradicts the hypothesis?
- **Escalation.** Given a missing input, does it escalate or invent?
- **Irreversibility.** Does it treat a one-way door differently from a two-way door?

These are the behaviours that separate an organisation from a pile of prompts, and they are exactly
what degrades first when a model is swapped or a prompt is "improved".

## Scoring honestly

- `--dry-run` checks every case assembles, every rubric is anchored, and every referenced agent
  exists. It needs no model and runs in CI.
- Scores are reported per case with the sample size. There is no aggregate "score" headline,
  because a single number would hide exactly the per-case regressions the sweep exists to catch.
- A case everything passes is retired by `case-retirement`: it costs runtime and teaches nothing.
- Held-out cases are marked `holdout: true` and must not be used while tuning prompts.
