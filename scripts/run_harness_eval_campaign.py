from __future__ import annotations

import argparse
import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
EVAL_FILE = REPO_ROOT / "evals" / "routing-workflow-evals.json"


def load_payload() -> dict:
    return json.loads(EVAL_FILE.read_text(encoding="utf-8"))


def scenario_lines(scenario: dict) -> list[str]:
    lines = [
        f"## {scenario['id']}",
        "",
        f"- Category: `{scenario['category']}`",
        f"- Request shape: {scenario['request_shape']}",
        f"- Expected primary workflow: `{scenario['expected_primary_workflow']}`",
        f"- Artifact mode: `{scenario['artifact_mode']}`",
        "- Must not do:",
    ]
    lines.extend([f"  - {item}" for item in scenario["must_not_do"]])
    lines.append("- Guardrails:")
    lines.extend([f"  - {item}" for item in scenario["guardrails"]])
    lines.extend(
        [
            "- Evidence to capture:",
            "  - actual route chosen",
            "  - whether the task was over-forced or under-routed",
            "  - whether hard gates stayed intact",
            "  - whether artifacts or loop status stayed synchronized",
            "",
        ]
    )
    return lines


def render_report(scenarios: list[dict]) -> str:
    lines = [
        "# Harness Eval Campaign",
        "",
        f"- Source manifest: `{EVAL_FILE.relative_to(REPO_ROOT)}`",
        f"- Scenario count: {len(scenarios)}",
        "",
        "## Summary",
        "",
        "| ID | Category | Expected workflow | Artifact mode |",
        "|---|---|---|---|",
    ]
    for scenario in scenarios:
        lines.append(
            f"| {scenario['id']} | {scenario['category']} | `{scenario['expected_primary_workflow']}` | `{scenario['artifact_mode']}` |"
        )
    lines.append("")
    lines.append("## Execution checklist")
    lines.append("")
    lines.extend(
        [
            "1. Run each scenario against the changed router/workflow or helper-agent behavior.",
            "2. Record the actual route and any rationalization or drift.",
            "3. Patch the smallest canonical files needed.",
            "4. Update `docs/CORRECTIONS_LOG.md` and `docs/HARNESS_EVAL_LOG.md` if behavior changed.",
            "5. Re-run the validator scripts.",
            "",
        ]
    )
    for scenario in scenarios:
        lines.extend(scenario_lines(scenario))
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render a reusable harness eval campaign from the routing/workflow eval manifest."
    )
    parser.add_argument("--list", action="store_true", help="List scenario IDs and categories only.")
    parser.add_argument("--all", action="store_true", help="Render all scenarios.")
    parser.add_argument(
        "--ids",
        help="Comma-separated scenario IDs to render, for example RP-002,RP-007,RP-013",
    )
    parser.add_argument("--output", help="Optional output file path for the rendered campaign brief.")
    args = parser.parse_args()

    payload = load_payload()
    scenarios = payload["scenarios"]
    by_id = {scenario["id"]: scenario for scenario in scenarios}

    if args.list:
        print("ID | Category | Expected workflow")
        print("---|---|---")
        for scenario in scenarios:
            print(
                f"{scenario['id']} | {scenario['category']} | {scenario['expected_primary_workflow']}"
            )
        return

    selected: list[dict]
    if args.all or (not args.ids and not args.list):
        selected = scenarios
    else:
        requested_ids = [item.strip() for item in args.ids.split(",") if item.strip()]
        missing = [item for item in requested_ids if item not in by_id]
        if missing:
            raise SystemExit(f"Unknown scenario IDs: {', '.join(missing)}")
        selected = [by_id[item] for item in requested_ids]

    report = render_report(selected)
    if args.output:
        output_path = Path(args.output)
        if not output_path.is_absolute():
            output_path = REPO_ROOT / output_path
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")
        print(f"Wrote harness eval campaign to {output_path}")
        return

    print(report)


if __name__ == "__main__":
    main()
