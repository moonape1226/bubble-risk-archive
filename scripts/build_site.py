#!/usr/bin/env python3
"""Build the GitHub Pages site for bubble-risk-archive.

Scans report-YYYY-MM-DD/ folders (score.json + report.md) and renders a dark
dashboard: a home page with a tier-tinted hero, a six-dimension score-card
grid, a score-trend chart (Chart.js) and a past-reports table, plus one
standalone page per report. Output goes to _site/.

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
    ("valuation", "估值溢價", 22),
    ("breadth", "市場廣度", 13),
    ("speculation", "投機行為", 18),
    ("retail", "散戶情緒", 12),
    ("monetary", "貨幣與信貸環境", 20),
    ("structural", "結構性槓桿", 15),
]

# Tier bands (half-up rounding boundaries per methodology), low → high.
TIER_BANDS = [
    (0, 19, "低"),
    (20, 39, "溫和"),
    (40, 64, "警戒"),
    (65, 84, "高"),
    (85, 100, "極度狂熱"),
]

# One accent colour per tier, used for badges, score-bars and the hero tint.
TIER_HEX = {
    "低": "#2ea043",
    "溫和": "#89aa1a",
    "警戒": "#d98016",
    "高": "#e5591b",
    "極度狂熱": "#e5484d",
}
TIER_UNKNOWN = "#6e7781"

CSS = """
:root {
  --bg: #0f1115; --surface: #171a21; --surface-2: #1d2128;
  --fg: #e6edf3; --muted: #9aa4b2; --faint: #6b7280;
  --border: #262c36; --border-strong: #333b47; --accent: #58a6ff;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0; color: var(--fg); background: var(--bg);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans TC",
    "PingFang TC", "Microsoft JhengHei", Helvetica, Arial, sans-serif;
  line-height: 1.7; -webkit-font-smoothing: antialiased;
}
.wrap { max-width: 900px; margin: 0 auto; padding: 0 20px; }
a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

/* top nav */
header.site {
  position: sticky; top: 0; z-index: 10;
  background: rgba(15,17,21,0.82); backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--border);
}
header.site .wrap {
  display: flex; align-items: center; justify-content: space-between;
  gap: 12px; padding: 12px 20px;
}
header.site .brand { font-weight: 700; font-size: 0.98rem; color: var(--fg); }
header.site .brand:hover { text-decoration: none; color: var(--accent); }
header.site .nav-latest { color: var(--muted); font-size: 0.85rem; }

/* eyebrow label */
.eyebrow {
  display: flex; align-items: center; gap: 10px;
  color: var(--muted); font-size: 0.74rem; font-weight: 700;
  letter-spacing: 0.14em; text-transform: uppercase; margin: 0 0 14px;
}
.eyebrow::before {
  content: ""; width: 26px; height: 2px; background: var(--border-strong);
  display: inline-block;
}

/* hero */
.hero { border-bottom: 1px solid var(--border); }
.hero .wrap { padding: 44px 20px 40px; }
.hero h1 { font-size: 2.05rem; line-height: 1.2; margin: 0 0 18px; font-weight: 800; }
.hero .score-row { display: flex; align-items: baseline; gap: 16px; flex-wrap: wrap; margin-bottom: 6px; }
.hero .score-big { font-size: 3.4rem; font-weight: 800; line-height: 1; letter-spacing: -0.02em; }
.hero .score-max { color: var(--muted); font-size: 1.1rem; font-weight: 600; }
.chips { display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0 4px; }
.chip {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 5px 13px; border-radius: 999px; font-size: 0.85rem;
  background: var(--surface-2); border: 1px solid var(--border-strong); color: var(--fg);
}
.chip b { font-weight: 700; }
.verdict { color: var(--fg); font-size: 0.98rem; margin: 18px 0 0; max-width: 70ch; }
.verdict strong { color: var(--fg); }
.fineprint { color: var(--faint); font-size: 0.82rem; margin: 14px 0 0; }

/* tier badge */
.badge {
  display: inline-block; padding: 3px 13px; border-radius: 999px;
  color: #fff; font-size: 0.9rem; font-weight: 700; vertical-align: middle;
}

/* section headings on the dashboard */
main.wrap { padding-top: 8px; padding-bottom: 72px; }
section.block { margin-top: 44px; }
section.block > h2 { font-size: 1.15rem; margin: 0 0 16px; font-weight: 700; }

/* score cards */
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 14px; }
.card {
  position: relative; background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 16px 18px; overflow: hidden;
}
.card::before {
  content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 4px;
  background: var(--card-accent, var(--border-strong));
}
.card .c-top { display: flex; justify-content: space-between; align-items: baseline; gap: 8px; }
.card .c-name { font-weight: 700; font-size: 0.98rem; }
.card .c-weight { color: var(--faint); font-size: 0.76rem; }
.card .c-score { display: flex; align-items: baseline; gap: 8px; margin: 10px 0 8px; }
.card .c-val { font-size: 1.9rem; font-weight: 800; line-height: 1; }
.card .c-delta { font-size: 0.82rem; font-weight: 700; }
.bar { height: 8px; border-radius: 999px; background: var(--surface-2); overflow: hidden; }
.bar > span { display: block; height: 100%; border-radius: 999px; background: var(--card-accent, var(--accent)); }
.delta-up { color: #ff7b72; }
.delta-down { color: #3fb950; }
.delta-flat { color: var(--faint); }

/* trend chart */
.chart-box {
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 12px; padding: 16px 16px 8px;
}

/* history table */
.table-scroll { overflow-x: auto; border: 1px solid var(--border); border-radius: 12px; }
table.history { border-collapse: collapse; width: 100%; font-size: 0.92rem; }
table.history th, table.history td { padding: 10px 14px; text-align: left; border-bottom: 1px solid var(--border); white-space: nowrap; }
table.history thead th { background: var(--surface-2); color: var(--muted); font-weight: 600; font-size: 0.82rem; }
table.history tbody tr:last-child td { border-bottom: 0; }
table.history tbody tr:hover { background: var(--surface); }
table.history td.num, table.history th.num { text-align: right; }

/* read-full link */
.readmore {
  display: inline-flex; align-items: center; gap: 8px; margin-top: 20px;
  padding: 12px 18px; border: 1px solid var(--border-strong); border-radius: 12px;
  background: var(--surface); font-weight: 600; color: var(--fg);
}
.readmore:hover { text-decoration: none; border-color: var(--accent); color: var(--accent); }
.back { display: inline-block; color: var(--muted); font-size: 0.88rem; margin: 24px 0 0; }

/* report prose */
.report { margin-top: 40px; font-size: 0.96rem; }
.report h2 { font-size: 1.3rem; margin: 2.2em 0 0.7em; padding-bottom: 8px; border-bottom: 1px solid var(--border); font-weight: 700; }
.report h3 { font-size: 1.08rem; margin: 1.8em 0 0.5em; font-weight: 700; }
.report p { max-width: 74ch; }
.report li { max-width: 72ch; margin: 4px 0; }
.report strong { color: #fff; font-weight: 700; }
.report a { border-bottom: 1px dotted rgba(88,166,255,0.5); }
.report blockquote {
  margin: 16px 0; padding: 10px 16px; color: var(--muted);
  border-left: 3px solid var(--border-strong); background: var(--surface); border-radius: 0 8px 8px 0;
}
.report code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  background: var(--surface-2); border: 1px solid var(--border); border-radius: 5px;
  padding: 1px 5px; font-size: 0.86em;
}
.report pre { background: var(--surface); border: 1px solid var(--border); border-radius: 8px; padding: 14px; overflow-x: auto; }
.report pre code { background: none; border: 0; padding: 0; }
.report table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 0.88rem; display: block; overflow-x: auto; }
.report th, .report td { border: 1px solid var(--border); padding: 7px 11px; text-align: left; white-space: nowrap; }
.report td:nth-child(n+2), .report th:nth-child(n+2) { white-space: normal; }
.report thead th { background: var(--surface-2); color: var(--muted); position: sticky; top: 0; }
.report details.appendix {
  margin: 2.2em 0; border: 1px solid var(--border); border-radius: 12px;
  background: var(--surface); padding: 0 18px;
}
.report details.appendix > summary {
  cursor: pointer; font-size: 1.2rem; font-weight: 700; padding: 16px 0;
  list-style: none;
}
.report details.appendix > summary::-webkit-details-marker { display: none; }
.report details.appendix > summary::before { content: "▸ "; color: var(--muted); }
.report details.appendix[open] > summary::before { content: "▾ "; }
.report details.appendix[open] { padding-bottom: 12px; }

footer { color: var(--faint); font-size: 0.8rem; margin-top: 56px; border-top: 1px solid var(--border); padding-top: 16px; }

@media (max-width: 560px) {
  .hero .wrap { padding: 32px 20px 30px; }
  .hero h1 { font-size: 1.6rem; }
  .hero .score-big { font-size: 2.6rem; }
}
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
    <a class="brand" href="__HOME__">市場泡沫風險評估</a>
    <span class="nav-latest">__NAVLATEST__</span>
  </div>
</header>
__HERO__
<main class="wrap">
__BODY__
<footer>本報告為相對風險溫度計，非擇時訊號。資料來源：<a href="https://github.com/moonape1226/bubble-risk-archive">bubble-risk-archive</a>，由 GitHub Actions 自動建置。</footer>
</main>
__SCRIPTS__
</body>
</html>
"""


def page(title, nav_latest, hero, body, home, scripts=""):
    return (
        PAGE.replace("__TITLE__", title)
        .replace("__CSS__", CSS)
        .replace("__HOME__", home)
        .replace("__NAVLATEST__", nav_latest)
        .replace("__HERO__", hero)
        .replace("__BODY__", body)
        .replace("__SCRIPTS__", scripts)
    )


def render_md(text):
    return markdown.markdown(text, extensions=["tables", "fenced_code"])


def render_inline(text):
    """Render a single markdown line without the wrapping <p>."""
    html = render_md(text)
    return re.sub(r"^<p>(.*)</p>$", r"\1", html.strip(), flags=re.S)


def score_tier(score):
    if not isinstance(score, int):
        return None
    for lo, hi, name in TIER_BANDS:
        if lo <= score <= hi:
            return name
    return None


def tier_color(tier):
    return TIER_HEX.get(tier, TIER_UNKNOWN)


def tier_badge(tier):
    return f'<span class="badge" style="background:{tier_color(tier)}">{tier or "—"}</span>'


def delta_span(cur, prev):
    """Delta vs previous run; rising risk = red, falling = green."""
    if not (isinstance(cur, int) and isinstance(prev, int)):
        return '<span class="c-delta delta-flat">—</span>'
    d = cur - prev
    if d > 0:
        return f'<span class="c-delta delta-up">▲ {d}</span>'
    if d < 0:
        return f'<span class="c-delta delta-down">▼ {-d}</span>'
    return '<span class="c-delta delta-flat">Δ0</span>'


# ---------------------------------------------------------------------------
# report metadata extraction (defensive: any miss just drops that element)

def extract_meta_line(md):
    for line in md.splitlines():
        if line.startswith("> "):
            return line[2:].strip()
    return ""


def extract_verdict(md):
    for line in md.splitlines():
        if line.startswith("**總評"):
            return line.strip()
    return ""


def find(pattern, text):
    m = re.search(pattern, text)
    return m.group(1).strip() if m else None


# ---------------------------------------------------------------------------

def hero(score, report_md):
    s = score
    tier = s.get("tier")
    total = s.get("total")
    accent = tier_color(tier)
    iso_week = s.get("iso_week", "")
    weekday = s.get("weekday", "")
    date = s.get("date", "")
    regime = s.get("regime")

    verdict = extract_verdict(report_md)
    trigger = find(r"扳機狀態：([^；。\n]+)", verdict)
    anchor = find(r"最貼近錨點：([^；。\n]+)", verdict)

    chips = []
    if regime:
        chips.append(f'<span class="chip">§3 格局 <b>{regime}</b></span>')
    if trigger:
        chips.append(f'<span class="chip">扳機狀態 <b>{trigger}</b></span>')
    if anchor:
        chips.append(f'<span class="chip">最貼近錨點 <b>{anchor}</b></span>')

    verdict_html = f'<p class="verdict">{render_inline(verdict)}</p>' if verdict else ""
    meta_line = extract_meta_line(report_md)
    fineprint = f'<p class="fineprint">{meta_line}</p>' if meta_line else ""

    eyebrow = f"市場泡沫風險 · {iso_week}" if iso_week else "市場泡沫風險"
    subtitle = " · ".join(x for x in [date, weekday] if x)

    tint = (
        f"background: radial-gradient(120% 120% at 0% 0%, {accent}22 0%, "
        f"rgba(0,0,0,0) 55%), var(--bg);"
    )
    return (
        f'<div class="hero" style="{tint}"><div class="wrap">'
        f'<p class="eyebrow">{eyebrow}</p>'
        f"<h1>市場泡沫風險評估</h1>"
        f'<div class="score-row">'
        f'<span class="score-big" style="color:{accent}">{total}</span>'
        f'<span class="score-max">/ 100</span>'
        f"{tier_badge(tier)}"
        f'<span class="score-max">{subtitle}</span>'
        f"</div>"
        f'<div class="chips">{"".join(chips)}</div>'
        f"{verdict_html}{fineprint}"
        f"</div></div>"
    )


def score_cards(score, prev):
    prev = prev or {}
    cards = []
    for key, label, weight in DIMENSIONS:
        val = score.get(key)
        accent = tier_color(score_tier(val))
        width = val if isinstance(val, int) else 0
        cards.append(
            f'<div class="card" style="--card-accent:{accent}">'
            f'<div class="c-top"><span class="c-name">{label}</span>'
            f'<span class="c-weight">權重 {weight}%</span></div>'
            f'<div class="c-score"><span class="c-val">{val if val is not None else "—"}</span>'
            f"{delta_span(val, prev.get(key))}</div>"
            f'<div class="bar"><span style="width:{width}%"></span></div>'
            f"</div>"
        )
    return f'<div class="cards">{"".join(cards)}</div>'


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


def render_report_body(md):
    """Render §2 onward as dark prose: drop the intro and the §1 ASCII table
    (both surfaced by the hero + score cards), collapse the data appendix."""
    parts = re.split(r"(?m)^(?=## )", md)
    out = []
    for sec in parts[1:]:  # parts[0] is the intro (H1 + metadata + 總評)
        heading = sec.splitlines()[0]
        if "§1 六維度風險條圖" in heading:
            continue
        rendered = render_md(sec)
        if "數據附錄" in heading:
            summary = heading.lstrip("#").strip()
            inner = re.sub(r"^\s*<h2>.*?</h2>", "", rendered, count=1, flags=re.S)
            out.append(
                f'<details class="appendix"><summary>{summary}</summary>{inner}</details>'
            )
        else:
            out.append(rendered)
    return "\n".join(out)


def chart_html(runs):
    labels = [r["date"] for r in runs]
    datasets = [{
        "label": "加權總分",
        "data": [r["score"].get("total") for r in runs],
        "borderColor": "#e6edf3",
        "backgroundColor": "#e6edf3",
        "borderWidth": 3,
        "pointRadius": 3,
    }]
    palette = ["#58a6ff", "#bc8cff", "#f778ba", "#ff7b72", "#e3b341", "#3fb950"]
    for (key, label, _weight), color in zip(DIMENSIONS, palette):
        datasets.append({
            "label": label,
            "data": [r["score"].get(key) for r in runs],
            "borderColor": color,
            "backgroundColor": color,
            "borderWidth": 1.5,
            "pointRadius": 2,
        })
    axis = {
        "ticks": {"color": "#9aa4b2"},
        "grid": {"color": "rgba(255,255,255,0.06)"},
    }
    yaxis = {
        "min": 0, "max": 100,
        "ticks": {"stepSize": 20, "color": "#9aa4b2"},
        "grid": {"color": "rgba(255,255,255,0.08)"},
    }
    config = {
        "type": "line",
        "data": {"labels": labels, "datasets": datasets},
        "options": {
            "responsive": True,
            "scales": {"x": axis, "y": yaxis},
            "plugins": {"legend": {"position": "bottom", "labels": {"color": "#c9d1d9"}}},
            "interaction": {"mode": "index", "intersect": False},
        },
    }
    html = '<div class="chart-box"><canvas id="trend"></canvas></div>'
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
    for r in runs:  # ascending; compute delta then reverse for display
        s = r["score"]
        total = s.get("total")
        delta = "—"
        if prev_total is not None and isinstance(total, int):
            d = total - prev_total
            cls = "delta-up" if d > 0 else ("delta-down" if d < 0 else "delta-flat")
            delta = f'<span class="{cls}">{d:+d}</span>' if d else '<span class="delta-flat">0</span>'
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
        '<div class="table-scroll"><table class="history"><thead><tr>'
        '<th>日期</th><th class="num">加權總分</th><th class="num">Δ</th><th>風險等級</th><th>§3 格局</th>'
        "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>"
    )


def main():
    runs = load_runs()
    if not runs:
        print("no complete report folders found", file=sys.stderr)
        sys.exit(1)
    latest = runs[-1]

    OUT.mkdir(exist_ok=True)

    # Per-report pages
    for i, r in enumerate(runs):
        prev = runs[i - 1]["score"] if i > 0 else None
        body = (
            score_cards(r["score"], prev)
            + f'<article class="report">{render_report_body(r["report_md"])}</article>'
            + '<a class="back" href="../">← 回首頁</a>'
        )
        d = OUT / r["dir"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(
            page(
                f'{r["date"]} 市場泡沫風險評估報告',
                f'報告日 {r["date"]}',
                hero(r["score"], r["report_md"]),
                body,
                "../",
            ),
            encoding="utf-8",
        )

    # Home page (dashboard only; full report lives on its own page)
    s = latest["score"]
    prev = runs[-2]["score"] if len(runs) > 1 else None
    chart, chart_script = chart_html(runs)
    body = (
        '<section class="block"><h2>六維度評分</h2>'
        + score_cards(s, prev)
        + f'<a class="readmore" href="{latest["dir"]}/">閱讀最新完整報告（{latest["date"]}） →</a>'
        + "</section>"
        + '<section class="block"><h2>歷史分數趨勢</h2>' + chart + "</section>"
        + '<section class="block"><h2>過往報告</h2>' + history_table(runs) + "</section>"
    )
    (OUT / "index.html").write_text(
        page(
            "市場泡沫風險評估",
            f'最新 {latest["date"]}',
            hero(s, latest["report_md"]),
            body,
            "./",
            chart_script,
        ),
        encoding="utf-8",
    )
    print(f"built {len(runs)} report pages + index -> {OUT}")


if __name__ == "__main__":
    main()
