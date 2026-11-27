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
:root{--bg:#fff;--soft:#fbf0ee;--gray:#f4f4f4;--ink:#111;--text:#222;--muted:#666;--line:#e6e6e6;--accent:#e8384f;--blue:#1d5fbf;
 --official:#1d5fbf;--exp:#8a4fd1;--plan:#1f9461;--tip:#b07a12}
*{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:70px}
body{margin:0;background:var(--bg);color:var(--text);font-family:"Noto Sans JP","Hiragino Kaku Gothic ProN","Yu Gothic","Meiryo",sans-serif;line-height:1.85;font-size:15.5px}
a{color:var(--blue)}
.hd{position:sticky;top:0;z-index:10;background:#fff;border-bottom:1px solid var(--line)}
.hd-in{max-width:1200px;margin:0 auto;padding:0 16px;height:58px;display:flex;align-items:center;gap:18px}
.logo{font-weight:900;font-size:19px;color:var(--ink);text-decoration:none;white-space:nowrap}
.logo small{font-size:11px;font-weight:700;margin-right:2px}
.nav{display:flex;gap:22px;margin-left:auto;overflow-x:auto;scrollbar-width:none}
.nav::-webkit-scrollbar{display:none}
.nav a{color:var(--ink);text-decoration:none;font-weight:500;font-size:15px;white-space:nowrap;padding:16px 0}
.nav a:hover,.nav a.on{color:var(--accent)}
.band{padding:46px 16px}
.band.soft{background:var(--soft)}.band.gray{background:var(--gray)}
.in{max-width:1100px;margin:0 auto}
.narrow{max-width:820px;margin:0 auto}
.ttl{text-align:center;font-size:clamp(22px,5.6vw,28px);font-weight:800;margin:0 0 6px;color:var(--ink);line-height:1.4}
.sub{text-align:center;color:var(--muted);margin:0 0 24px;font-size:14.5px}
.cards{list-style:none;margin:0;padding:0;display:grid;gap:16px;grid-template-columns:repeat(auto-fill,minmax(min(100%,320px),1fr))}
.card{position:relative;display:block;aspect-ratio:4/3;border-radius:16px;overflow:hidden;background:#33415c center/cover no-repeat;color:#fff;text-decoration:none}
.card::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 45%,rgba(0,0,0,.5) 100%)}
.card b{position:absolute;z-index:1;left:20px;top:18px;right:20px;font-size:19px;font-weight:800;line-height:1.4}
.card span{position:absolute;z-index:1;left:20px;right:20px;bottom:16px;font-size:13.5px;line-height:1.55}
.card:hover{filter:brightness(1.06)}
.hero{position:relative;background:#222 center/cover no-repeat;color:#fff;padding:70px 16px 56px;text-align:center}
.hero::after{content:"";position:absolute;inset:0;background:rgba(0,0,0,.45)}
.hero>*{position:relative;z-index:1;max-width:820px;margin-left:auto;margin-right:auto}
.hero .en{font-size:12.5px;font-weight:700;letter-spacing:.18em;opacity:.9}
.hero h1{margin:8px auto 10px;font-size:clamp(26px,7vw,40px);line-height:1.3;font-weight:900}
.hero p{margin:0 auto;font-size:15px;opacity:.95}
.crumb{font-size:12.5px;color:var(--muted);max-width:1100px;margin:0 auto;padding:12px 16px 0}
.crumb a{color:var(--muted)}
.icons{list-style:none;margin:0;padding:0;display:grid;gap:16px 8px;grid-template-columns:repeat(auto-fit,minmax(100px,1fr));text-align:center}
.icons a{color:var(--ink);text-decoration:none;font-size:13px;font-weight:600;line-height:1.45;display:grid;justify-items:center;gap:8px}
.icons i{font-style:normal;width:76px;height:76px;border-radius:50%;background:#fff;display:grid;place-items:center;font-size:30px;box-shadow:0 2px 10px rgba(0,0,0,.06)}
.icons a:hover i{box-shadow:0 0 0 2px var(--accent)}
.blk{background:#fff;border-radius:16px;padding:26px 22px;margin:0 0 18px;box-shadow:0 0 0 1px var(--line),0 4px 18px rgba(0,0,0,.04)}
.blk h2{font-size:21px;margin:6px 0 12px;line-height:1.45;color:var(--ink);font-weight:800}
p{margin:8px 0}
ul.items{margin:0;padding-left:1.2em;display:grid;gap:8px}
.kind{display:inline-block;font-size:11.5px;font-weight:700;color:#fff;border-radius:99px;padding:1px 10px}
.k-official{background:var(--official)}.k-exp{background:var(--exp)}.k-plan{background:var(--plan)}.k-tip{background:var(--tip)}
.src{font-size:12px;color:var(--muted);margin-top:14px;overflow-wrap:anywhere;border-top:1px solid var(--line);padding-top:10px}
.src a{color:var(--muted)}
ul.check{list-style:none;margin:0;padding:0;display:grid;gap:10px}
ul.check li{padding-left:2em;position:relative}
ul.check li::before{content:"✓";position:absolute;left:0;top:.35em;color:#fff;background:var(--accent);border-radius:50%;width:1.4em;height:1.4em;font-size:12px;display:grid;place-items:center}
.trip-pr{font-size:13px;margin:0 0 12px;color:var(--muted)}
.pr{display:inline-block;font-size:10.5px;font-weight:700;border:1px solid var(--muted);border-radius:4px;padding:0 5px;margin-right:6px;color:var(--muted)}
.big-link{display:flex;align-items:center;justify-content:space-between;gap:12px;background:var(--ink);color:#fff;text-decoration:none;border-radius:16px;padding:18px 22px;font-weight:800;margin:-4px 0 22px;font-size:16.5px}
.big-link span{display:block;font-weight:400;font-size:13px;color:#ccc;margin-top:2px}
.big-link em{font-style:normal;font-size:22px}
.big-link:hover{background:var(--accent)}
.legend{font-size:12.5px;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px;align-items:center;justify-content:center;margin-bottom:22px}
dl.faq{margin:0}
dl.faq div{background:#fff;border-radius:14px;padding:16px 20px;margin-bottom:10px}
dl.faq dt{font-weight:800}
dl.faq dt::before{content:"Q. ";color:var(--accent)}
dl.faq dd{margin:6px 0 0}
footer{background:#222;color:#bbb;font-size:12.5px;padding:30px 16px;text-align:center}
footer a{color:#ddd}
footer .in{display:grid;gap:6px}
table{border-collapse:collapse;width:100%;font-size:14px}th,td{border-bottom:1px solid var(--line);padding:8px;text-align:left;vertical-align:top}th{white-space:nowrap}
"""

IMG = "/paradise-city/img/"
CARD_IMG = {"casino": IMG + "pegasus.jpg", "paradise": IMG + "hyatt-lobby.jpg"}
HERO_IMG = {"casino": IMG + "trip-2611-pegasus.jpg"}
ICON = {"official": "ℹ️", "exp": "🙋", "plan": "🗓️", "tip": "💡"}
# 見出しの言葉で決めるアイコン（無ければ ICON）
ICON_BY_H = [("ハイアット", "🏨"), ("パラダイス", "⭐"), ("知っておく", "📘"), ("プラン", "🗓️"), ("仁川", "✈️"), ("ソウル", "🏙️"), ("釜山", "🌊"),
             ("選ぶ", "🧭"), ("プラン", "🗓️"), ("のめり込", "🛟")]


def icon_for(b):
    return next((ic for w, ic in ICON_BY_H if w in b["h"]), ICON[b["kind"]])
SEC_ID = {"初めて行くなら知っておきたい事": "first", "カジノ旅": "casino", "人気のプラン": "plan"}


def header(cur):
    links = ['<a href="./"' + (' class="on"' if cur == "index" else "") + '>トップ</a>']
    for name, _desc, keys in D.SECTIONS:
        pub = [k for k in keys if k in D.PUBLISH]
        if not pub:
            continue
        href = pub[0] + ".html" if len(pub) == 1 else "./#" + SEC_ID[name]
        on = ' class="on"' if cur in keys else ""
        label = "初めての韓国" if SEC_ID[name] == "first" else name
        links.append(f'<a href="{href}"{on}>{label}</a>')
    return f'<header class="hd"><div class="hd-in"><a class="logo" href="./"><small>mocchima</small>KOREA</a><nav class="nav">{"".join(links)}</nav></div></header>'


def page(path, title, desc, body, adsense=True, cur="index"):
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
<body>
{header(cur)}
{body}
<footer><div class="in"><p>当サイトは個人が運営する非公式の旅行情報サイトです。料金・時間・決まりは変わることがあります。出かける前に、各ページの出典（公式サイト）で最新の情報を確かめてください。最終更新 {D.UPDATED}</p>
<p><a href="./">{SITE}のトップ</a>｜<a href="/about.html">運営者情報・お問い合わせ</a>｜<a href="/privacy.html">プライバシーポリシー</a></p></div></footer>
</body></html>
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
    return f'<div class="blk"><div style="overflow-x:auto"><table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table></div></div>'


LEGEND = ('<div class="legend"><span>情報の見分け方：</span>'
          + "".join(f'<span class="kind k-{k}">{e(v)}</span>' for k, v in D.KIND_LABEL.items()) + '</div>')


def detail_page(key):
    p = D.PAGES[key]
    parts, icons = [], []
    for i, b in enumerate(p["blocks"]):
        bid = f"b{i + 1}"
        icons.append(f'<li><a href="#{bid}"><i>{icon_for(b)}</i>{e(b["h"])}</a></li>')
        pr = "".join(trip_line(k) for k in b["pr"])
        items = "".join(f"<li>{e(t)}</li>" for t in b["items"])
        parts.append(f'<section class="blk" id="{bid}"><span class="kind k-{b["kind"]}">{e(D.KIND_LABEL[b["kind"]])}</span>'
                     f'<h2>{e(b["h"])}</h2>{pr}<ul class="items">{items}</ul>{src_links(b["src"], b["checked"])}</section>')
        if b.get("link"):
            url, head, sub = b["link"]
            parts.append(f'<a class="big-link" href="{e(url)}"><div>{e(head)}<span>{e(sub)}</span></div><em>→</em></a>')
    table = table_html(p["table"]) if p.get("table") else ""
    check = ('<section class="band soft"><div class="narrow"><h2 class="ttl">出発前のチェック</h2><p class="sub">これだけは確かめてから行こう</p>'
             '<div class="blk"><ul class="check">' + "".join(f"<li>{e(c)}</li>" for c in p["check"]) + "</ul></div></div></section>") if p.get("check") else ""
    hero_img = HERO_IMG.get(key)
    style = f' style="background-image:url({hero_img})"' if hero_img else ""
    body = f"""<div class="hero"{style}><div class="en">KOREA TRAVEL GUIDE</div><h1>{e(p['title'])}</h1><p>{e(p['lead'])}</p></div>
<p class="crumb"><a href="./">{SITE}</a> ＞ {e(p['title'])}</p>
<section class="band gray"><div class="in"><h2 class="ttl">このページの内容</h2><p class="sub">知りたいところから読めます</p><ul class="icons">{''.join(icons)}</ul></div></section>
{check}
<section class="band"><div class="narrow">{LEGEND}{table}{''.join(parts)}</div></section>"""
    return page(key + ".html", f"{p['title']}｜{SITE}", p["lead"], body, adsense=p["adsense"], cur=key)


def index_page():
    secs, bands, n = "", ["", "soft", ""], 0
    for name, desc, keys in D.SECTIONS:
        tiles = []
        for k in keys:
            if k in D.EXTERNAL:
                href, t, d = D.EXTERNAL[k]
            elif k in D.PUBLISH:
                href, t, d = k + ".html", D.PAGES[k]["title"], D.PAGES[k]["tile"]
            else:
                continue  # まだ公開していないページはカードを出さない
            img = CARD_IMG.get(k)
            st = f' style="background-image:url({img})"' if img else ""
            tiles.append(f'<li><a class="card"{st} href="{e(href)}"><b>{e(t)}</b><span>{e(d)}</span></a></li>')
        if any(k in D.PUBLISH for k in keys):
            secs += (f'<section class="band {bands[n % 3]}" id="{SEC_ID.get(name, "")}"><div class="in"><h2 class="ttl">{e(name)}</h2>'
                     f'<p class="sub">{e(desc)}</p><ul class="cards">{"".join(tiles)}</ul></div></section>')
            n += 1
    faq = "".join(f'<div><dt>{e(q)}</dt><dd>{e(a)}（<a href="{k}.html">くわしく</a>）</dd></div>' for q, a, k in D.FAQ if k in D.PUBLISH)
    faq_sec = f'<section class="band gray"><div class="narrow"><h2 class="ttl">よくある質問</h2><p class="sub">友だちによく聞かれること</p><dl class="faq">{faq}</dl></div></section>' if faq else ""
    body = f"""<div class="hero" style="background-image:url({IMG}trip-2611-pegasus.jpg)"><div class="en">KOREA TRAVEL GUIDE</div><h1>{SITE}</h1>
<p>韓国に何度も行っている運営者が、友だちによく聞かれることを、公式の情報で確かめてまとめています。</p></div>
{secs}
{faq_sec}
<section class="band"><div class="narrow"><h2 class="ttl">このガイドの書き方</h2><div class="blk"><ul class="items">
<li>料金・時間・決まりは、韓国観光公社や各施設の公式サイトなどで確かめ、出典と確認日を付けています。確かめられなかったことは書きません。</li>
<li>運営者が実際に体験したことは「運営者の体験談」として、事実の説明と分けています。</li>
<li>広告（PR）を含む場所には「PR」と表示しています。</li></ul></div></div></section>"""
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
