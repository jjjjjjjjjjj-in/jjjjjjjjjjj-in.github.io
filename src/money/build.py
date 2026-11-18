# お金のカラクリ研究所の解説ページ（mocchima.com/money/）を作る。
# 使い方: PYTHONUTF8=1 python src/money/build.py
import os
import sys
from html import escape as e

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
from episodes import CHANNEL, EPISODES  # noqa: E402
from build import analytics_tag, BASE_URL  # noqa: E402  (src/build.py。__main__ で守られている)

OUT = os.path.join(ROOT, "money")

CSS = """
:root{--bg:#fffdf6;--ink:#1d1d1f;--muted:#5c5c5c;--line:#e6dfc8;--card:#ffffff;--accent:#e8b400;--accent-ink:#5a4300;--red:#d83a2f}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:"Hiragino Kaku Gothic ProN","Yu Gothic","Meiryo",sans-serif;line-height:1.85;
 padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.wrap{max-width:760px;margin:0 auto;padding:24px 0 56px;display:grid;gap:22px}
header.top{background:var(--ink);color:#fff;border-radius:14px;padding:22px}
header.top .ch{font-size:13px;font-weight:700;color:var(--accent);letter-spacing:.06em}
header.top h1{margin:6px 0 0;font-size:clamp(22px,6vw,32px);line-height:1.35}
header.top p{margin:8px 0 0;color:#d6d6d6}
.video{position:relative;width:min(100%,340px);aspect-ratio:9/16;margin:0 auto;border-radius:14px;overflow:hidden;background:#000}
.video iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
section{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px}
h2{margin:0 0 10px;font-size:20px;border-left:6px solid var(--accent);padding-left:10px;line-height:1.4}
p{margin:8px 0}
.sum{background:#fff6d6;border-color:var(--accent)}
.sum ol{margin:0;padding-left:1.4em;display:grid;gap:6px}
.src{font-size:13px;color:var(--muted);margin-top:10px}
.src a{color:var(--muted)}
ul.check{list-style:none;margin:0;padding:0;display:grid;gap:8px}
ul.check li{padding-left:1.6em;position:relative}
ul.check li::before{content:"□";position:absolute;left:0;color:var(--accent-ink);font-weight:700}
dl.faq dt{font-weight:700;margin-top:12px}
dl.faq dt::before{content:"Q. ";color:var(--red)}
dl.faq dd{margin:4px 0 0}
dl.faq dd::before{content:"A. ";font-weight:700}
.note{font-size:13.5px;color:var(--muted)}
.btn{display:inline-block;background:var(--ink);color:#fff;text-decoration:none;border-radius:99px;padding:8px 16px;font-weight:700;font-size:14px}
ul.eps{list-style:none;margin:0;padding:0;display:grid;gap:10px}
ul.eps a{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;color:var(--ink);text-decoration:none}
ul.eps a:hover{border-color:var(--accent)}
ul.eps .no{font-size:12px;font-weight:700;color:var(--accent-ink)}
ul.eps span.d{display:block;font-size:13.5px;color:var(--muted)}
footer{font-size:12.5px;color:var(--muted);text-align:center}
"""


def page(path, title, desc, body):
    canonical = BASE_URL + "money/" + path
    return f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}">{analytics_tag()}
<style>{CSS}</style></head>
<body><div class="wrap">
{body}
<footer>{e(CHANNEL['name'])}｜<a href="./">解説ページの一覧</a>｜<a href="/about.html">運営者情報</a>｜<a href="/privacy.html">プライバシーポリシー</a></footer>
</div></body></html>
"""


def src_links(links):
    if not links:
        return ""
    return '<p class="src">出典：' + "／".join(f'<a href="{e(u)}" target="_blank" rel="noopener">{e(t)}</a>' for t, u in links) + "</p>"


def episode_page(ep):
    summary = "".join(f"<li>{e(s)}</li>" for s in ep["summary"])
    secs = "".join(
        f'<section><h2>{e(h)}</h2>{"".join(f"<p>{e(p)}</p>" for p in ps)}{src_links(links)}</section>'
        for h, ps, links in ep["sections"])
    check = "".join(f"<li>{e(c)}</li>" for c in ep.get("checklist", []))
    faq = "".join(f"<dt>{e(q)}</dt><dd>{e(a)}</dd>" for q, a in ep.get("faq", []))
    check_sec = f'<section><h2>{e(ep.get("checklist_title", "出す前のチェックリスト"))}</h2><ul class="check">{check}</ul></section>' if check else ""
    faq_sec = f'<section><h2>よくある質問</h2><dl class="faq">{faq}</dl></section>' if faq else ""
    src_note = ep.get("sources_note", "国税庁のページ")
    body = f"""<header class="top"><div class="ch">{e(CHANNEL['name'])}｜第{ep['no']}話の解説</div>
<h1>{e(ep['title'])}</h1><p>{e(ep['short'])}</p></header>
<div class="video"><iframe src="https://www.youtube-nocookie.com/embed/{e(ep['youtube_id'])}" title="第{ep['no']}話の動画" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
<section class="sum"><h2>まとめると</h2><ol>{summary}</ol></section>
{secs}
{check_sec}
{faq_sec}
<p class="note">このページは、お金のしくみを分かりやすく説明するためのもので、特定の商品や制度をすすめるものではありません。一人ひとりの状況で結果は変わります。くわしくは公式の窓口に確認してください。制度の内容は {e(ep['checked'])} に{e(src_note)}で確認しました。</p>
<p><a class="btn" href="{e(CHANNEL['youtube'])}" target="_blank" rel="noopener">YouTube でほかの話を見る</a></p>"""
    return page(ep["slug"] + ".html", f"{ep['title']}｜{CHANNEL['name']}", ep["short"], body)


def index_page():
    items = "".join(
        f'<li><a href="{e(ep["slug"])}.html"><span class="no">第{ep["no"]}話</span><br><strong>{e(ep["title"])}</strong><span class="d">{e(ep["short"])}</span></a></li>'
        for ep in sorted(EPISODES, key=lambda x: x["no"]))
    body = f"""<header class="top"><div class="ch">YouTube・TikTok のお金アニメ</div>
<h1>{e(CHANNEL['name'])}</h1><p>ショート動画で話したお金のしくみを、1話ずつ、数字と出典つきでくわしく説明しています。</p></header>
<section><h2>このページについて</h2><p>動画は1分ほどなので、細かい条件や数字は入りきりません。ここでは、動画の内容を国税庁などの公式の情報で確かめて、もう少しくわしく書いています。</p></section>
<ul class="eps">{items}</ul>"""
    return page("", f"{CHANNEL['name']}｜お金のしくみ 解説ページ", "ショート動画で話したお金のしくみを、1話ずつ、数字と出典つきでくわしく説明しています。", body)


def main():
    os.makedirs(OUT, exist_ok=True)
    files = {"index.html": index_page()}
    for ep in EPISODES:
        files[ep["slug"] + ".html"] = episode_page(ep)
    for name, html in files.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
    print(f"built money: {len(files)} pages")


if __name__ == "__main__":
    main()
