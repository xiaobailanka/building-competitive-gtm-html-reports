# building-competitive-gtm-html-reports

Reusable Codex skill for building source-grounded competitor analysis reports for new-product launch, positioning and e-commerce/GTM decisions, with a single-file HTML output matching the bundled golden example.

## Package structure

- `SKILL.md` — compact entrypoint and hard rules.
- `references/competitive-analysis-sop.md` — the analysis framework derived from the supplied SOP.
- `references/research-and-evidence.md` — source hierarchy, evidence ledger and comparability rules.
- `references/information-architecture.md` — required report sections.
- `references/design-system.md` — exact visual grammar.
- `references/visualization-rules.md` — when/how to use each chart or component.
- `references/production-method.md` — reproducible creation method and judgment framework.
- `references/quality-checklist.md` — definition of done.
- `assets/golden-example-oppo-find-x10-vs-xiaomi18.html` — reference output. Style/logic only; never reuse its facts blindly.
- `assets/report-shell.html` — starter shell.
- `scripts/scaffold_report.py` — creates a starter HTML.
- `scripts/validate_report.py` — structural QA.
- `tests/acceptance-scenarios.md` — behavior tests to run in Codex.
- `tests/test_helpers.py` — executable regression checks for offline dependencies, unfinished drafts and safe scaffolding.
- `agents/openai.yaml` — Codex display metadata and invocation prompt.
- `CODEX_SETUP_PROMPT.txt` — ready-to-send setup instruction.

## Usage example

> Use `building-competitive-gtm-html-reports`. Our product is vivo X600 Pro, direct competitor is OPPO Find X11 Pro, China market. Goal: new-product launch positioning and e-commerce conversion. Use current verified public data and produce the final single-file HTML.

## Important boundary

The package contains a golden example from one smartphone comparison. It is not a fact database. Every new report must rebuild its evidence ledger from current sources.

## Helper validation

Python 3.10+ is required; report helpers use only the standard library.

```bash
python scripts/scaffold_report.py draft.html --title "竞品分析" --analysis-date 2026-10-05
python scripts/validate_report.py draft.html --allow-scaffold
python -m unittest discover -s tests -p "test_*.py" -v
```

The scaffold is deliberately unfinished. A strict check without `--allow-scaffold` must reject it. Complete the report and remove its scaffold-stage meta tag before strict delivery validation. The validator covers structural QA, not source verification or visual QA. Do not pad missing evidence with fake links. Collection-only requests retain the user's requested scope.
