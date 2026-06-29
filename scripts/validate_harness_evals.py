from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
EVAL_FILE = REPO_ROOT / "evals" / "routing-workflow-evals.json"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    if not EVAL_FILE.exists():
        fail(f"Missing eval manifest: {EVAL_FILE}")

    payload = json.loads(EVAL_FILE.read_text(encoding="utf-8"))
    scenarios = payload.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        fail("Eval manifest must contain a non-empty scenarios list.")

    required_categories = {
        "full_delivery_loop",
        "technical_execution",
        "presales_discovery",
        "fit_gap_comparison",
        "functional_design",
        "skill_maintenance",
        "office_capability_docx",
        "office_capability_xlsx",
        "loop_sync",
    }
    seen_ids: set[str] = set()
    seen_categories: set[str] = set()

    for scenario in scenarios:
        for field in [
            "id",
            "category",
            "request_shape",
            "expected_primary_workflow",
            "artifact_mode",
            "must_not_do",
            "guardrails",
        ]:
            if field not in scenario:
                fail(f"Scenario missing required field '{field}': {scenario}")

        scenario_id = scenario["id"]
        if scenario_id in seen_ids:
            fail(f"Duplicate scenario ID: {scenario_id}")
        seen_ids.add(scenario_id)
        seen_categories.add(scenario["category"])

        workflow_path = REPO_ROOT / scenario["expected_primary_workflow"]
        if not workflow_path.exists():
            fail(f"Scenario {scenario_id} points to missing workflow: {workflow_path}")

        if not isinstance(scenario["must_not_do"], list) or not scenario["must_not_do"]:
            fail(f"Scenario {scenario_id} must contain at least one must_not_do entry.")

        if not isinstance(scenario["guardrails"], list) or not scenario["guardrails"]:
            fail(f"Scenario {scenario_id} must contain at least one guardrail entry.")

    missing_categories = sorted(required_categories - seen_categories)
    if missing_categories:
        fail(f"Eval manifest missing required categories: {', '.join(missing_categories)}")

    print("Harness evals OK")


if __name__ == "__main__":
    main()
