# Design system — match the golden example

The goal is a calm, premium research report: editorial hierarchy + operating dashboard readability. Do not redesign it into a generic SaaS dashboard.

## Visual identity

Use these CSS variables unless the user requests another palette:

```css
--bg:#f7f6f3;
--paper:#ffffff;
--text:#171918;
--muted:#6e7472;
--line:#e9e6e1;
--target:#168a72;
--target-dark:#0f6f5d;
--competitor:#e97031;
--competitor-dark:#bd5524;
--pink:#d94c78;
--blue:#3d7fb2;
--purple:#8066b2;
--gold:#ad7b12;
--soft-target:#e6f4f0;
--soft-competitor:#fff0e7;
--soft-pink:#fbecf1;
--soft-blue:#eaf2fb;
--soft-gold:#fff4cd;
--shadow:0 12px 34px rgba(32,35,34,.07);
--radius:20px;
```

The target product/brand uses green. The direct competitor uses orange. Pink is the sequencing/attention accent. Blue is evidence/benchmark, purple is strategic concept, gold is caution/opportunity.

## Layout

- max content width: `1180px`;
- page background: warm cool-gray `#f7f6f3`;
- hero: white with subtle radial accents;
- sticky navigation under hero;
- section card: white, 1px border, 20px radius, restrained shadow;
- desktop section padding: ~30px;
- mobile section padding: ~21px;
- main vertical rhythm: 30px between major sections.

## Typography

- display/H1/H2: Chinese serif (`Songti SC`, `STSong`, fallback serif);
- body/data/UI: system sans (`-apple-system`, `PingFang SC`, `Microsoft YaHei`, etc.);
- H1: 36–62px responsive, compact line height;
- H2: ~30px;
- H3: ~20px;
- body: 13–17px depending role.

Use serif only to create editorial authority; keep tables, labels, data, and navigation sans-serif for scanning.

## Signature elements

Preserve these because they define the golden example:

1. four-color ribbon across the very top;
2. large editorial hero headline;
3. target-vs-competitor color coding;
4. metric cards with oversized numbers;
5. CSS-only horizontal comparison bars;
6. compact section kicker in uppercase English;
7. journey strip with numbered circles;
8. “leadbox” conclusion block;
9. A/B/C source reliability pills;
10. fixed print/export and back-to-top buttons.

## Restraint

Do not add decorative gradients, glassmorphism, neon, 3D, charts everywhere, or excessive animation. Visuals must encode hierarchy or comparison.

## Responsive behavior

At <900px reduce 4-column layouts to 2; at <620px reduce most grids to 1. Wide matrices should horizontally scroll rather than squash text.

## Print

Hide navigation/floating buttons, remove shadows, keep white background, and avoid splitting critical cards when possible.
