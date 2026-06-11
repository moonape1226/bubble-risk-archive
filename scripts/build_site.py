#!/usr/bin/env python3
"""Build the GitHub Pages site for bubble-risk-archive.

Scans report-YYYY-MM-DD/ folders (score.json + report.md), renders each
report to HTML, and generates an index with the latest report, a score
trend chart (Chart.js), and a past-reports list. Output goes to _site/.

Usage: python3 scripts/build_site.py
Requires: pip install markdown
"""
import json
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_site"

DIMENSIONS = [
    ("valuation", "估值溢價"),
    ("breadth", "市場廣度"),
    ("speculation", "投機行為"),
    ("retail", "散戶情緒"),
    ("monetary", "貨幣與信貸環境"),
    ("structural", "結構性槓桿"),
]

TIER_CLASS = {
    "低": "tier-low",
    "溫和": "tier-mild",
    "警戒": "tier-watch",
    "高": "tier-high",
    "極度狂熱": "tier-mania",
}

CSS = """
:root {
  --fg: #1f2328; --bg: #ffffff; --muted: #59636e; --border: #d1d9e0;
  --accent: #0969da; --soft: #f6f8fa;
}
* { box-sizing: border-box; }
body {
  margin: 0; color: var(--fg); background: var(--bg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC",
    "PingFang TC", "Microsoft JhengHei", Helvetica, Arial, sans-serif;
  line-height: 1.6;
}
.wrap { max-width: 880px; margin: 0 auto; padding: 24px 16px 64px; }
header.site { border-bottom: 1px solid var(--border); background: var(--soft); }
header.site .wrap { padding: 18px 16px; display: flex; align-items: baseline; gap: 12px; flex-wrap: wrap; }
header.site h1 { font-size: 1.25rem; margin: 0; }
header.site .latest { color: var(--muted); font-size: 0.9rem; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }
h1, h2, h3 { line-height: 1.3; }
.report h1 { font-size: 1.5rem; border-bottom: 1px solid var(--border); padding-bottom: 8px; }
.report h2 { font-size: 1.2rem; margin-top: 2em; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
.report h3 { font-size: 1.05rem; }
table { border-collapse: collapse; width: 100%; margin: 12px 0; font-size: 0.92rem; display: block; overflow-x: auto; }
th, td { border: 1px solid var(--border); padding: 6px 10px; text-align: left; white-space: nowrap; }
td:nth-child(n+2), th:nth-child(n+2) { white-space: normal; }
th { background: var(--soft); }
blockquote { margin: 12px 0; padding: 6px 14px; color: var(--muted); border-left: 4px solid var(--border); background: var(--soft); }
pre { background: var(--soft); border: 1px solid var(--border); border-radius: 6px; padding: 12px; overflow-x: auto; font-size: 0.85rem; }
code { font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
.badge { display: inline-block; padding: 1px 10px; border-radius: 999px; color: #fff; font-size: 0.85rem; font-weight: 600; }
.tier-low { background: #1a7f37; }
.tier-mild { background: #4d7c0f; }
.tier-watch { background: #b45309; }
.tier-high { background: #c2410c; }
.tier-mania { background: #b91c1c; }
.tier-unknown { background: #6e7781; }
.scorecard { display: flex; gap: 24px; align-items: center; flex-wrap: wrap; margin: 20px 0; padding: 16px 20px; border: 1px solid var(--border); border-radius: 8px; background: var(--soft); }
.scorecard .total { font-size: 2.4rem; font-weight: 700; }
.scorecard .meta { color: var(--muted); font-size: 0.9rem; }
.chart-box { margin: 20px 0 36px; }
.history td.num, .history th.num { text-align: right; }
.back { font-size: 0.9rem; }
footer { color: var(--muted); font-size: 0.8rem; margin-top: 48px; border-top: 1px solid var(--border); padding-top: 12px; }
.delta-up { color: #b91c1c; }
.delta-down { color: #1a7f37; }
"""

PAGE = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>__CSS__</style>
</head>
<body>
<header class="site">
  <div class="wrap">
    <h1><a href="__HOME__" style="color:inherit">市場泡沫風險評估</a></h1>
    <span class="latest">__SUBTITLE__</span>
  </div>
</header>
<main class="wrap">
__BODY__
<footer>本報告為相對風險溫度計，非擇時訊號。資料來源：<a href="https://github.com/moonape1226/bubble-risk-archive">bubble-risk-archive</a>，由 GitHub Actions 自動建置。</footer>
</main>
__SCRIPTS__
</body>
</html>
"""


def page(title, subtitle, body, home, scripts=""):
    return (
        PAGE.replace("__TITLE__", title)
        .replace("__CSS__", CSS)
        .replace("__HOME__", home)
        .replace("__SUBTITLE__", subtitle)
        .replace("__BODY__", body)
        .replace("__SCRIPTS__", scripts)
    )


def render_md(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code"])


def tier_badge(tier):
    cls = TIER_CLASS.get(tier, "tier-unknown")
    return f'<span class="badge {cls}">{tier or "—"}</span>'


def load_runs():
    runs = []
    for d in sorted(ROOT.glob("report-????-??-??")):
        if not re.fullmatch(r"report-\d{4}-\d{2}-\d{2}", d.name):
            continue
        score_f, report_f = d / "score.json", d / "report.md"
        if not (score_f.is_file() and report_f.is_file()):
            print(f"skip partial folder: {d.name}", file=sys.stderr)
            continue
        try:
            score = json.loads(score_f.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"skip unparsable score.json: {d.name} ({e})", file=sys.stderr)
            continue
        runs.append({
            "dir": d.name,
            "date": d.name.removeprefix("report-"),
            "score": score,
            "report_md": report_f.read_text(encoding="utf-8"),
        })
    runs.sort(key=lambda r: r["date"])
    return runs


def chart_html(runs):
    labels = [r["date"] for r in runs]
    datasets = [{
        "label": "加權總分",
        "data": [r["score"].get("total") for r in runs],
        "borderColor": "#1f2328",
        "backgroundColor": "#1f2328",
        "borderWidth": 3,
        "pointRadius": 4,
    }]
    palette = ["#0969da", "#8250df", "#bf3989", "#cf222e", "#9a6700", "#1a7f37"]
    for (key, label), color in zip(DIMENSIONS, palette):
        datasets.append({
            "label": label,
            "data": [r["score"].get(key) for r in runs],
            "borderColor": color,
            "backgroundColor": color,
            "borderWidth": 1.5,
            "pointRadius": 3,
            "hidden": False,
        })
    config = {
        "type": "line",
        "data": {"labels": labels, "datasets": datasets},
        "options": {
            "responsive": True,
            "scales": {"y": {"min": 0, "max": 100, "ticks": {"stepSize": 20}}},
            "plugins": {"legend": {"position": "bottom"}},
            "interaction": {"mode": "index", "intersect": False},
        },
    }
    html = (
        '<div class="chart-box"><canvas id="trend"></canvas></div>'
    )
    script = (
        '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.9/dist/chart.umd.min.js" '
        'integrity="sha384-b0GXujLkk9eYYSmcSfoyZbfyElGAQnDyY0skCHSG6w3JgTMFnz11ggrTAr7seu9f" '
        'crossorigin="anonymous"></script>\n'
        "<script>\n"
        f"const cfg = {json.dumps(config, ensure_ascii=False)};\n"
        "new Chart(document.getElementById('trend'), cfg);\n"
        "</script>"
    )
    return html, script


def history_table(runs):
    rows = []
    prev_total = None
    for r in runs:  # ascending; we compute delta then reverse for display
        s = r["score"]
        total = s.get("total")
        delta = "—"
        if prev_total is not None and isinstance(total, int):
            d = total - prev_total
            cls = "delta-up" if d > 0 else ("delta-down" if d < 0 else "")
            delta = f'<span class="{cls}">{d:+d}</span>' if d else "0"
        prev_total = total if isinstance(total, int) else prev_total
        rows.append(
            "<tr>"
            f'<td><a href="{r["dir"]}/">{r["date"]}</a></td>'
            f'<td class="num">{total}</td>'
            f'<td class="num">{delta}</td>'
            f"<td>{tier_badge(s.get('tier'))}</td>"
            f"<td>{s.get('regime', '—')}</td>"
            "</tr>"
        )
    rows.reverse()
    return (
        '<table class="history"><thead><tr>'
        '<th>日期</th><th class="num">加權總分</th><th class="num">Δ</th><th>風險等級</th><th>§3 格局</th>'
        "</tr></thead><tbody>" + "".join(rows) + "</tbody></table>"
    )


def main():
    runs = load_runs()
    if not runs:
        print("no complete report folders found", file=sys.stderr)
        sys.exit(1)
    latest = runs[-1]

    OUT.mkdir(exist_ok=True)

    # Per-report pages
    for r in runs:
        body = (
            f'<p class="back"><a href="../">← 回首頁</a></p>'
            f'<article class="report">{render_md(r["report_md"])}</article>'
        )
        d = OUT / r["dir"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(
            page(f'{r["date"]} 市場泡沫風險評估報告', r["date"], body, "../"),
            encoding="utf-8",
        )

    # Index
    s = latest["score"]
    chart, chart_script = chart_html(runs)
    scorecard = (
        '<div class="scorecard">'
        f'<div class="total">{s.get("total")}</div>'
        f"<div>{tier_badge(s.get('tier'))}</div>"
        f'<div class="meta">最新報告：{latest["date"]}（{s.get("weekday", "")}，{s.get("iso_week", "")}）'
        f'<br>§3 格局：{s.get("regime", "—")}</div>'
        "</div>"
    )
    body = (
        scorecard
        + "<h2>歷史分數趨勢</h2>"
        + chart
        + "<h2>過往報告</h2>"
        + history_table(runs)
        + "<h2>最新報告全文</h2>"
        + f'<article class="report">{render_md(latest["report_md"])}</article>'
    )
    (OUT / "index.html").write_text(
        page(
            "市場泡沫風險評估",
            f'最新：{latest["date"]}・總分 {s.get("total")}・{s.get("tier")}',
            body,
            "./",
            chart_script,
        ),
        encoding="utf-8",
    )
    print(f"built {len(runs)} report pages + index -> {OUT}")


if __name__ == "__main__":
    main()
