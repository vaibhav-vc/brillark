"""Conformance tests for the reference loader.

The written contract in runtime/loader-spec.md is only as good as an implementation that obeys it.
These tests check the reference loader against that contract, clause by clause. If you port the
loader to another language or runtime, port these too — they are the definition of "correct".

    python3 ai-system/tests/test_conformance.py
"""
from __future__ import annotations

import json
import pathlib
import sys
import unittest

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from loader import Organisation, BudgetExceeded, STABLE_PREFIX, tok  # noqa: E402


class TestModelResolution(unittest.TestCase):
    """A portable organisation names capability tiers, never vendor models."""

    def setUp(self):
        self.org = Organisation()
        self.profiles = yaml.safe_load(
            (ROOT / "runtime" / "model-profiles.yaml").read_text())

    def test_agents_declare_a_task_class_not_a_vendor_model(self):
        for agent in self.org.agents.values():
            self.assertIn(agent["task_class"], {"mechanical", "analytical", "judgement"})

    def test_every_task_class_resolves_under_the_active_profile(self):
        for task_class in ("mechanical", "analytical", "judgement"):
            model = self.org.resolve_model(task_class)
            self.assertTrue(model and isinstance(model, str))

    def test_a_null_tier_is_an_error_not_a_silent_upgrade(self):
        """Falling back to a stronger model hides misconfiguration and inflates cost silently."""
        org = Organisation(profile="custom")
        with self.assertRaises(SystemExit):
            org.resolve_model("analytical")

    def test_escalation_moves_up_one_tier(self):
        self.assertEqual(self.org.escalated_model("mechanical"),
                         self.org.resolve_model("analytical"))
        self.assertEqual(self.org.escalated_model("analytical"),
                         self.org.resolve_model("judgement"))

    def test_judgement_is_the_top_of_the_ladder(self):
        self.assertEqual(self.org.escalated_model("judgement"),
                         self.org.resolve_model("judgement"))

    def test_profiles_declare_all_three_tiers(self):
        for name, profile in self.profiles["profiles"].items():
            for tier in ("mechanical", "analytical", "judgement"):
                self.assertIn(tier, profile, f"profile '{name}' is missing tier '{tier}'")

    def test_capability_requirements_are_stated(self):
        """A runtime needs to know what its model must support before adopting this."""
        reqs = self.profiles["capability_requirements"]
        self.assertTrue(reqs["required"])
        self.assertTrue(reqs["not_required"])
        joined = " ".join(reqs["required"]).lower()
        self.assertIn("schema", joined, "structured output must be a stated requirement")


class TestLoadingOrder(unittest.TestCase):
    """Cache reuse depends entirely on the prefix being stable and in order."""

    def setUp(self):
        self.org = Organisation()

    def test_stable_prefix_files_exist(self):
        for rel in STABLE_PREFIX:
            self.assertTrue((ROOT / rel).exists(), f"{rel} is in the prefix but does not exist")

    def test_assembly_puts_the_task_last(self):
        result = self.org.assemble("market-researcher", task="SENTINEL_TASK_TEXT")
        self.assertEqual(result["parts"][-1]["source"], "task")

    def test_assembly_puts_the_context_package_before_the_task(self):
        result = self.org.assemble("market-researcher", task="t", context_package={"brief": "b"})
        sources = [p["source"] for p in result["parts"]]
        self.assertLess(sources.index("context-package"), sources.index("task"))

    def test_no_variable_content_inside_the_cacheable_prefix(self):
        a = self.org.assemble("market-researcher", task="first task")
        b = self.org.assemble("market-researcher", task="a completely different second task")
        self.assertEqual(a["cacheable_prefix_tokens"], b["cacheable_prefix_tokens"],
                         "the prefix changed with the task — cache reuse is lost")
        prefix_a = [p["source"] for p in a["parts"] if p["source"] not in ("task", "context-package")]
        prefix_b = [p["source"] for p in b["parts"] if p["source"] not in ("task", "context-package")]
        self.assertEqual(prefix_a, prefix_b)

    def test_base_prompt_comes_first(self):
        result = self.org.assemble("director", task="t")
        self.assertEqual(result["parts"][0]["source"], "prompts/system/00-base-agent.md")

    def test_charter_precedes_its_skills(self):
        agent = self.org.agents["pcb-layout-designer"]
        result = self.org.assemble("pcb-layout-designer", task="t")
        sources = [p["source"] for p in result["parts"]]
        charter = sources.index(agent["path"])
        first_skill = min(sources.index(self.org.skills[s]["path"]) for s in agent["skills"])
        self.assertLess(charter, first_skill)

    def test_the_skill_index_is_not_loaded_for_a_routed_run(self):
        """The charter already names its toolkit. Loading the index too is the waste the
        two-path model exists to avoid."""
        result = self.org.assemble("pcb-layout-designer", task="t")
        for part in result["parts"]:
            self.assertNotIn("skills/index/", part["source"])

    def test_improvement_agents_receive_the_self_modification_boundary(self):
        result = self.org.assemble("prompt-optimizer", task="t")
        sources = [p["source"] for p in result["parts"]]
        self.assertIn("prompts/system/06-self-modification.md", sources)

    def test_non_improvement_agents_do_not_pay_for_that_prompt(self):
        result = self.org.assemble("market-researcher", task="t")
        sources = [p["source"] for p in result["parts"]]
        self.assertNotIn("prompts/system/06-self-modification.md", sources)


class TestBudgetEnforcement(unittest.TestCase):
    """Budgets that are documented but not enforced are decoration."""

    def setUp(self):
        self.org = Organisation()

    def test_every_agent_assembles_within_budget_with_room_for_a_task(self):
        for agent_id, agent in self.org.agents.items():
            result = self.org.assemble(agent_id, task="")
            self.assertLess(result["total_tokens"], agent["context_budget_tokens"],
                            f"{agent_id} has no headroom left for task context")

    def test_over_budget_raises_rather_than_truncating_silently(self):
        oversized = "x " * 200_000
        with self.assertRaises(BudgetExceeded):
            self.org.assemble("progress-tracker", task=oversized)

    def test_the_error_says_what_to_do(self):
        try:
            self.org.assemble("progress-tracker", task="x " * 200_000)
        except BudgetExceeded as exc:
            message = str(exc)
            self.assertIn("Compact", message)
            self.assertIn("escalate", message)
            self.assertIn("token-efficiency-analyst", message)
        else:
            self.fail("expected BudgetExceeded")

    def test_enforcement_can_be_disabled_deliberately_for_reporting(self):
        result = self.org.assemble("progress-tracker", task="x " * 200_000, enforce=False)
        self.assertLess(result["headroom"], 0)


class TestReturnContract(unittest.TestCase):
    """What comes back is as much a contract as what goes in."""

    def setUp(self):
        self.org = Organisation()

    def _valid(self):
        return {"agent": "market-researcher", "task_id": "task_x", "status": "done",
                "summary": "TAM is roughly 4,000 shops at GBP 600 per year.",
                "artifacts": ["workspace/acme/market/market-sizing.md"],
                "confidence": "estimated",
                "tokens_used": {"total": 9100}}

    def test_a_well_formed_return_passes(self):
        self.assertEqual(self.org.validate_return(self._valid()), [])

    def test_missing_required_fields_are_caught(self):
        payload = self._valid()
        del payload["confidence"]
        problems = self.org.validate_return(payload)
        self.assertTrue(any("confidence" in p for p in problems))

    def test_an_oversized_summary_is_rejected(self):
        payload = self._valid()
        payload["summary"] = "word " * 5000
        problems = self.org.validate_return(payload)
        self.assertTrue(any("return budget" in p for p in problems),
                        "a summary over budget must be rejected, not silently accepted")

    def test_artifacts_must_be_paths_not_contents(self):
        payload = self._valid()
        payload["artifacts"] = ["# Market analysis\n\nThe full document pasted inline...\n" * 5]
        problems = self.org.validate_return(payload)
        self.assertTrue(any("paths, not contents" in p for p in problems))

    def test_an_invalid_confidence_grade_is_rejected(self):
        payload = self._valid()
        payload["confidence"] = "pretty sure"
        problems = self.org.validate_return(payload)
        self.assertTrue(any("confidence" in p for p in problems))

    def test_token_cost_is_required(self):
        schema = json.loads(
            (ROOT / "knowledge-schema" / "agent-return.schema.json").read_text())
        self.assertIn("tokens_used", schema["required"],
                      "an agent that cannot report its cost cannot be optimised")


class TestExportBundle(unittest.TestCase):
    """The exports must stay faithful to the source of truth."""

    def setUp(self):
        sys.path.insert(0, str(ROOT / "tools"))
        import export  # noqa: E402
        self.export = export
        self.agents, self.skills = export.load()

    def test_tool_definitions_cover_every_agent(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            out = pathlib.Path(tmp)
            self.export.export_tools(self.agents, self.skills, out)
            payload = json.loads((out / "tool-definitions.json").read_text())
            self.assertEqual(payload["count"], len(self.agents))
            names = {t["name"] for t in payload["tools"]}
            self.assertEqual(names, {a["id"].replace("-", "_") for a in self.agents})

    def test_every_tool_definition_carries_its_budgets(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            out = pathlib.Path(tmp)
            self.export.export_tools(self.agents, self.skills, out)
            for tool in json.loads((out / "tool-definitions.json").read_text())["tools"]:
                meta = tool["x_ai_system"]
                self.assertIn(meta["task_class"], {"mechanical", "analytical", "judgement"})
                self.assertGreater(meta["context_budget_tokens"], 0)
                self.assertGreater(meta["return_budget_tokens"], 0)

    def test_tool_schemas_require_a_definition_of_done(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            out = pathlib.Path(tmp)
            self.export.export_tools(self.agents, self.skills, out)
            for tool in json.loads((out / "tool-definitions.json").read_text())["tools"]:
                self.assertIn("definition_of_done", tool["input_schema"]["required"])

    def test_export_is_deterministic(self):
        """A bundle that differs run to run makes the checksum meaningless."""
        import tempfile
        outputs = []
        for _ in range(2):
            with tempfile.TemporaryDirectory() as tmp:
                out = pathlib.Path(tmp)
                self.export.export_tools(self.agents, self.skills, out)
                self.export.export_json(self.agents, self.skills, out)
                outputs.append(self.export.checksum(out))
        self.assertEqual(outputs[0], outputs[1])


class TestEvalSuite(unittest.TestCase):
    def test_suite_validates_without_a_model(self):
        sys.path.insert(0, str(ROOT / "tools"))
        import eval as eval_mod  # noqa: E402
        problems = eval_mod.validate(Organisation(), eval_mod.load_cases())
        self.assertEqual(problems, [], f"eval suite is invalid: {problems}")

    def test_holdout_split_exists(self):
        sys.path.insert(0, str(ROOT / "tools"))
        import eval as eval_mod  # noqa: E402
        cases = eval_mod.load_cases()
        holdout = [c for c in cases if c.get("holdout")]
        tuning = [c for c in cases if not c.get("holdout")]
        self.assertTrue(holdout, "no holdout cases — every score would be measured on tuning data")
        self.assertTrue(tuning)

    def test_every_case_can_fail(self):
        sys.path.insert(0, str(ROOT / "tools"))
        import eval as eval_mod  # noqa: E402
        for case in eval_mod.load_cases():
            self.assertTrue(case.get("must_not"),
                            f"{case['id']} has no must_not — a case that cannot fail teaches nothing")


if __name__ == "__main__":
    unittest.main(verbosity=2)
