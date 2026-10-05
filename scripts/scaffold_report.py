#!/usr/bin/env python3
from pathlib import Path
import argparse
from datetime import date
from html import escape

TOKENS = {
    "REPORT_TITLE":"竞品分析报告",
    "H1":"目标产品 vs 直接竞品",
    "HERO_SUBTITLE":"新品上市 / GTM / 卖点定位竞品分析",
    "MARKET":"中国大陆",
    "ANALYSIS_DATE":date.today().isoformat(),
    "GOAL":"新品上市 + 卖点定位",
    "TARGET_SKU":"目标 SKU",
    "COMPETITOR_SKU":"竞品 SKU",
    "NAV_LINKS":'<a href="#summary">结论</a><a href="#sources">来源</a>',
    "SUMMARY_TITLE":"先给结论：这里必须是判断，不是资料摘要",
    "SUMMARY_SUB":"用 1–2 句话解释双方最关键的差异。",
    "METRIC_CARDS":''.join(f'<div class="card metric"><div class="num">—</div><div class="label">关键指标 {i}</div></div>' for i in range(1,5)),
    "POSITIONING_RECOMMENDATION":"建议核心定位：……",
    "REPORT_SECTIONS":'<section id="scope" class="card section-card"><div class="kicker">Step 01 · Competitor Types</div><h2>竞品选择</h2><p class="sub">补充真实内容。</p></section><section id="market" class="card section-card"><div class="kicker">Market Context</div><h2>市场背景</h2><p class="sub">补充真实内容。</p></section><section id="users" class="card section-card"><div class="kicker">User + Positioning</div><h2>用户与 Positioning</h2><p class="sub">补充真实内容。</p></section><section id="product" class="card section-card"><div class="kicker">Product + Selling Points</div><h2>产品与卖点</h2><p class="sub">补充真实内容。</p></section><section id="price" class="card section-card"><div class="kicker">Pricing Architecture</div><h2>价格体系</h2><p class="sub">补充真实内容。</p></section><section id="message" class="card section-card"><div class="kicker">Brand Message</div><h2>品牌话术</h2><p class="sub">补充真实内容。</p></section><section id="channel" class="card section-card"><div class="kicker">Channel + Content</div><h2>渠道与内容</h2><p class="sub">补充真实内容。</p></section><section id="journey" class="card section-card"><div class="kicker">Conversion Journey</div><h2>完整转化链路</h2><p class="sub">补充真实内容。</p></section><section id="signals" class="card section-card"><div class="kicker">Early Market Signals</div><h2>市场与用户信号</h2><p class="sub">补充真实内容。</p></section><section id="opportunity" class="card section-card"><div class="kicker">Final Conclusions</div><h2>机会与风险</h2><p class="sub">补充真实内容。</p></section><section id="positioning" class="card section-card"><div class="kicker">Positioning Recommendation</div><h2>卖点定位建议</h2><p class="sub">补充真实内容。</p></section><section id="gtm" class="card section-card"><div class="kicker">GTM Operating Actions</div><h2>GTM 运营动作</h2><p class="sub">补充真实内容。</p></section><section id="tests" class="card section-card"><div class="kicker">Test Plan</div><h2>A/B 测试计划</h2><p class="sub">补充真实内容。</p></section>',
    "SOURCE_LIST":"<ol><li>[A] 官方来源</li></ol>",
    "RESEARCH_BOUNDARY":"研究边界：明确哪些数据无法公开验证，以及需要用哪些一方数据补齐。",
}

TOKENS["REPORT_SECTIONS"] += '<section id="conclusion" class="card section-card"><div class="kicker">One-page Conclusion</div><h2>一页结论</h2><p class="sub">补充真实内容。</p></section>'

def main():
    p=argparse.ArgumentParser()
    p.add_argument("output")
    p.add_argument("--title", default=TOKENS["REPORT_TITLE"])
    p.add_argument("--market", default=TOKENS["MARKET"])
    p.add_argument("--analysis-date", type=date.fromisoformat, default=date.today())
    args=p.parse_args()
    root=Path(__file__).resolve().parents[1]
    s=(root/"assets/report-shell.html").read_text(encoding="utf-8")
    vals=dict(TOKENS)
    vals.update(REPORT_TITLE=escape(args.title), MARKET=escape(args.market), ANALYSIS_DATE=args.analysis_date.isoformat())
    for k,v in vals.items(): s=s.replace("{{"+k+"}}",v)
    output=Path(args.output)
    if output.exists():
        p.error("Output already exists; choose a new filename to preserve existing work")
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(s,encoding="utf-8")
    print(Path(args.output).resolve())

if __name__=="__main__": main()
