# 韓国旅行ガイド（mocchima.com/korea/）を作る。
# 使い方: PYTHONUTF8=1 python src/korea/build.py
# 中身は src/korea/data.py。公開するページは data.py の PUBLISH。
import os
import sys
from html import escape as e

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))
import data as D  # noqa: E402
from build import analytics_tag, BASE_URL  # noqa: E402  (src/build.py。__main__ で守られている)

OUT = os.path.join(ROOT, "korea")
SITE = "韓国旅行ガイド"

CSS = """
:root{--bg:#f7f8fb;--ink:#14213d;--text:#1b1b1f;--muted:#5d5f66;--line:#dfe3ec;--card:#fff;--red:#c8102e;--blue:#1f4e8c;
 --official:#1f4e8c;--exp:#6b4fa3;--plan:#2e7d4f;--tip:#8a6a1f}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:"Hiragino Kaku Gothic ProN","Yu Gothic","Meiryo",sans-serif;line-height:1.85;font-size:15.5px;
 padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
a{color:var(--blue)}
.wrap{max-width:760px;margin:0 auto;padding:20px 0 56px;display:grid;gap:18px}
.crumb{font-size:13px;color:var(--muted)}
header.top{background:var(--ink);color:#fff;border-radius:14px;padding:22px;border-bottom:5px solid var(--red)}
header.top .ch{font-size:12.5px;font-weight:700;letter-spacing:.08em;color:#f2b8c1}
header.top h1{margin:6px 0 0;font-size:clamp(22px,6.4vw,32px);line-height:1.35}
header.top p{margin:8px 0 0;color:#d8dde8}
section{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px}
h2{margin:0 0 8px;font-size:19px;line-height:1.45;border-left:6px solid var(--red);padding-left:10px}
p{margin:8px 0}
ul.items{margin:0;padding-left:1.2em;display:grid;gap:6px}
.kind{display:inline-block;font-size:11.5px;font-weight:700;color:#fff;border-radius:99px;padding:1px 9px;margin-bottom:6px}
.k-official{background:var(--official)}.k-exp{background:var(--exp)}.k-plan{background:var(--plan)}.k-tip{background:var(--tip)}
.src{font-size:12.5px;color:var(--muted);margin-top:10px;overflow-wrap:anywhere}
.src a{color:var(--muted)}
ul.check{list-style:none;margin:0;padding:0;display:grid;gap:6px}
ul.check li{padding-left:1.6em;position:relative}
ul.check li::before{content:"□";position:absolute;left:0;color:var(--red);font-weight:700}
.trip-pr{font-size:13px;margin:-6px 0;color:var(--muted)}
.pr{display:inline-block;font-size:10.5px;font-weight:700;border:1px solid var(--muted);border-radius:4px;padding:0 5px;margin-right:6px;color:var(--muted)}
.big-link{display:block;background:var(--ink);color:#fff;text-decoration:none;border-radius:14px;padding:16px 18px;font-weight:700}
.big-link span{display:block;font-weight:400;font-size:13.5px;color:#d8dde8}
.legend{font-size:12.5px;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px;align-items:center}
.legend .kind{margin:0}
ul.tiles{list-style:none;margin:0;padding:0;display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(220px,1fr))}
ul.tiles a{display:block;height:100%;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;color:var(--text);text-decoration:none}
ul.tiles a:hover,ul.tiles a:focus-visible{border-color:var(--ink)}
ul.tiles strong{display:block;font-size:16px}
ul.tiles span{display:block;font-size:13.5px;color:var(--muted)}
h2.sec{border:0;padding:0;font-size:20px;margin:6px 0 0}
p.sec{margin:0;color:var(--muted);font-size:14px}
dl.faq dt{font-weight:700;margin-top:12px}
dl.faq dt::before{content:"Q. ";color:var(--red)}
dl.faq dd{margin:4px 0 0}
.note{font-size:13px;color:var(--muted)}
footer{font-size:12.5px;color:var(--muted);text-align:center;display:grid;gap:4px}
"""


def page(path, title, desc, body, adsense=True):
    canonical = BASE_URL + "korea/" + path
    return f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="icon" type="image/png" href="/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}og.png"><meta property="og:locale" content="ja_JP">{analytics_tag(adsense=adsense)}
<style>{CSS}</style></head>
<body><div class="wrap">
{body}
<footer><p>当サイトは個人が運営する非公式の旅行情報サイトです。料金・時間・決まりは変わることがあります。出かける前に、各ページの出典（公式サイト）で最新の情報を確かめてください。最終更新 {D.UPDATED}</p>
<p><a href="./">{SITE}のトップ</a>｜<a href="/about.html">運営者情報・お問い合わせ</a>｜<a href="/privacy.html">プライバシーポリシー</a></p></footer>
</div></body></html>
"""


def src_links(keys, checked):
    if not keys:
        return ""
    links = []
    for k in keys:
        label, url = D.S[k]
        links.append(f'<a href="{e(url)}" target="_blank" rel="noopener">{e(label)}</a>' if url else e(label))
    return f'<p class="src">出典：{"／".join(links)}（確認日 {e(checked)}）</p>'


def trip_line(key):
    label, url = D.TRIP_LINKS[key]
    return f'<p class="trip-pr"><span class="pr">PR</span><a href="{e(url)}" target="_blank" rel="sponsored noopener">{e(label)}</a></p>'


def table_html(rows):
    head = "".join(f"<th>{e(c)}</th>" for c in rows[0])
    body = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
    return (f'<section><div style="overflow-x:auto"><table style="border-collapse:collapse;width:100%;font-size:14px">'
            f'<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div></section>'
            '<style>th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{white-space:nowrap}</style>')


LEGEND = ('<div class="legend"><span>情報の見分け方：</span>'
          + "".join(f'<span class="kind k-{k}">{e(v)}</span>' for k, v in D.KIND_LABEL.items()) + '</div>')


def detail_page(key):
    p = D.PAGES[key]
    parts = []
    for b in p["blocks"]:
        parts += [trip_line(k) for k in b["pr"]]
        items = "".join(f"<li>{e(t)}</li>" for t in b["items"])
        parts.append(f'<section><span class="kind k-{b["kind"]}">{e(D.KIND_LABEL[b["kind"]])}</span>'
                     f'<h2>{e(b["h"])}</h2><ul class="items">{items}</ul>{src_links(b["src"], b["checked"])}</section>')
    if key == "casino":
        # パラダイスシティのくわしいガイドへの目立つリンク（2つ目のブロックの後）
        parts.insert(3, '<a class="big-link" href="/paradise-city/">パラダイスシティ カジノガイドを見る →'
                        '<span>仁川のパラダイスシティに2026年に8回通った運営者の、到着から帰るまでのくわしいガイド</span></a>')
    table = table_html(p["table"]) if p.get("table") else ""
    check = ("<section><h2>チェック表</h2><ul class=\"check\">" + "".join(f"<li>{e(c)}</li>" for c in p["check"]) + "</ul></section>") if p.get("check") else ""
    body = f"""<p class="crumb"><a href="./">{SITE}</a> ＞ {e(p['title'])}</p>
<header class="top"><div class="ch">KOREA TRAVEL GUIDE</div><h1>{e(p['title'])}</h1><p>{e(p['lead'])}</p></header>
{LEGEND}
{check}
{table}
{''.join(parts)}"""
    return page(key + ".html", f"{p['title']}｜{SITE}", p["lead"], body, adsense=p["adsense"])


def index_page():
    secs = ""
    for name, desc, keys in D.SECTIONS:
        tiles = []
        for k in keys:
            if k in D.EXTERNAL:
                href, t, d = D.EXTERNAL[k]
            elif k in D.PUBLISH:
                href, t, d = k + ".html", D.PAGES[k]["title"], D.PAGES[k]["tile"]
            else:
                continue  # まだ公開していないページはタイルを出さない（準備中のタイルは置かない）
            tiles.append(f'<li><a href="{e(href)}"><strong>{e(t)}</strong><span>{e(d)}</span></a></li>')
        if any(k in D.PUBLISH for k in keys):
            secs += f'<h2 class="sec">{e(name)}</h2><p class="sec">{e(desc)}</p><ul class="tiles">{"".join(tiles)}</ul>'
    faq = "".join(f'<dt>{e(q)}</dt><dd>{e(a)}（<a href="{k}.html">くわしく</a>）</dd>' for q, a, k in D.FAQ if k in D.PUBLISH)
    faq_sec = f'<section><h2>よくある質問</h2><dl class="faq">{faq}</dl></section>' if faq else ""
    body = f"""<header class="top"><div class="ch">KOREA TRAVEL GUIDE</div><h1>{SITE}</h1>
<p>韓国に何度も行っている運営者が、友だちによく聞かれることを、公式の情報で確かめてまとめています。</p></header>
{secs}
{faq_sec}
<section><h2>このガイドの書き方</h2><ul class="items">
<li>料金・時間・決まりは、韓国観光公社や各施設の公式サイトなどで確かめ、出典と確認日を付けています。確かめられなかったことは書きません。</li>
<li>運営者が実際に体験したことは「運営者の体験談」として、事実の説明と分けています。</li>
<li>広告（PR）を含む場所には「PR」と表示しています。</li></ul></section>"""
    return page("", f"{SITE}｜初めての韓国・カジノ旅", "韓国旅行で友だちによく聞かれることを、公式の情報で確かめて、出典つきでまとめた個人運営のガイドです。", body)


def main():
    os.makedirs(OUT, exist_ok=True)
    files = {"index.html": index_page()}
    for k in D.PUBLISH:
        files[k + ".html"] = detail_page(k)
    for name, html in files.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"  <url><loc>{BASE_URL}korea/{'' if n == 'index.html' else n}</loc><lastmod>{D.UPDATED}</lastmod></url>\n" for n in files)
                + "</urlset>\n")
    print(f"built korea: {len(files)} pages")


if __name__ == "__main__":
    main()
