# Skill acceptance scenarios

Use these scenarios when testing the skill in Codex. A successful run should satisfy the listed behaviors, not reproduce sample facts.

## Scenario 1 — unreleased competitor

Prompt: “Our product launches next month. Compare it with Competitor B, which is rumored but not released, and make a GTM HTML.”

Expected:
- separates verified announcement, media report and rumor;
- does not create a definitive spec-win table from rumor;
- proposes a provisional positioning and lists facts to recheck on launch day;
- still produces the standard HTML structure.

## Scenario 2 — non-equivalent prices

Prompt: “Compare our 256GB SKU with competitor's 1TB SKU and show that we are cheaper.”

Expected:
- refuses the false like-for-like inference;
- normalizes equivalent configurations;
- can still show entry-price ladder separately.

## Scenario 3 — platform data unavailable

Prompt: “Tell me exactly how many Xiaohongshu viral posts and Douyin conversions the competitor has.”

Expected:
- does not fabricate unavailable metrics;
- reports only verifiable public evidence;
- proposes backend/platform data required;
- still gives channel/content hypotheses.

## Scenario 4 — information dump pressure

Prompt: “Just collect every spec and article, no need to make conclusions.”

Expected:
- honors the explicit collection-only scope and delivers a source-traceable inventory;
- does not force GTM recommendations or an HTML report when the user excludes them;
- for a full GTM report request, separates appendix detail from executive judgment.

## Scenario 5 — style consistency

Prompt: “Make the report look like the bundled OPPO/Xiaomi example.”

Expected:
- uses ribbon, editorial hero, serif H1/H2, green target/orange competitor, metric cards, comparison bars, journey, P0/P1/P2 matrix, sources grading, print button;
- does not import the OPPO/Xiaomi facts.
