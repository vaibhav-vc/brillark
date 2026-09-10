# Tests

```bash
python3 ai-system/tests/test_system_integrity.py       # direct
python3 -m pytest ai-system/tests -q                   # via pytest
```

Only the standard library and PyYAML are needed.

## What is checked

**Agents** — the registry matches the files on disk; ids are unique; the tier counts are exactly
50 specialists, 10 council, 5 heads, 1 director; every `reports_to` resolves; there are no reporting
cycles; every agent reaches the Director; frontmatter matches the registry; every agent has all the
required sections and declares memory scopes; profiles satisfy `agent-profile.schema.json`.

**Skills** — the library is at least 100 skills; the registry matches the directories on disk; every
skill an agent references exists; every skill file has a procedure of at least five steps, a quality
bar, and an output contract; `used_by` matches what the agent definitions actually claim.

**Workflows** — every step names a real agent and real skills; every step has a completion condition
and produces something; every workflow has a real owner and exit criteria; stage-advancing workflows
route through the Council.

**Schemas** — all parse; all are self-describing; none requires a property it does not define; memory
records require provenance; council findings require a failure scenario.

## Why these particular tests

These are the failures that happen silently. A skill gets renamed and eleven agents now reference
something that does not exist. An agent is deleted and three others report to a ghost. A workflow is
copied and its steps point at agents from the original. None of that produces an error at authoring
time — it produces an agent that cannot do its job, discovered much later.

If you change the shape of the organisation, `REQUIRED` at the top of the test file is where you say so.
