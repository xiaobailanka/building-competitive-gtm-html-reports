# Quality checklist / definition of done

## Research

- [ ] Analysis date is visible.
- [ ] Market/geography is explicit.
- [ ] Direct, indirect and reference competitors are not mixed.
- [ ] Unreleased/rumored products are labeled.
- [ ] Every charted number is sourceable.
- [ ] Important sources have A/B/C reliability grades.
- [ ] Like-for-like SKUs are compared.
- [ ] Different shipment/share definitions are not merged.
- [ ] Analytical inference is not presented as measured consumer fact.
- [ ] Platform/creator metrics are not invented.

## Strategy

- [ ] Executive summary contains a clear positioning recommendation.
- [ ] Report explains why a difference matters to the consumer.
- [ ] Competitor strengths and vulnerabilities are both explicit.
- [ ] Report says what **not** to copy or fight head-on.
- [ ] Every major insight maps to an operating action.
- [ ] GTM actions include KPI/validation method.
- [ ] Test plan changes one primary variable per test.
- [ ] Final one-page conclusion compresses the causal chain.

## HTML

- [ ] Single UTF-8 HTML file.
- [ ] Inline CSS; no external framework required.
- [ ] Sticky navigation.
- [ ] Responsive mobile layout.
- [ ] Print stylesheet.
- [ ] Target/competitor colors are consistent.
- [ ] Metric cards, comparison visuals, journey, GTM matrix and source appendix present.
- [ ] No TODO/TBD/template placeholders.
- [ ] URLs are readable and clickable.
- [ ] Source caveats sit next to critical charts.

Run `python scripts/validate_report.py OUTPUT.html` and resolve all errors before delivery.

Review warnings against actual evidence coverage rather than filling a URL quota. Draft-only checks use `--allow-scaffold` and do not establish completion. Structural success does not establish source accuracy or visual/browser QA; report these checks separately.
