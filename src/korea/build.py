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
.photos{display:grid;gap:12px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));margin:14px 0}.photos figure{margin:0}.photos img{width:100%;aspect-ratio:4/3;object-fit:cover;border-radius:12px;display:block}.photos figcaption{font-size:12px;color:var(--muted);margin-top:6px}
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
KIMG = "/korea/img/"
CARD_IMG = {"casino": IMG + "pegasus.jpg", "paradise": IMG + "hyatt-lobby.jpg", "food": KIMG + "food-gwangjang-liver.jpg"}
HERO_IMG = {"casino": IMG + "trip-2611-pegasus.jpg", "food": KIMG + "food-gwangjang-table.jpg"}
OG_IMG = {"food": "korea/og-food.jpg"}
# 手描き風のイラストアイコン（SVG）。色は塗り＋黒い線
_S = 'fill="none" stroke="#2b2b2b" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
SVG = {
    "hotel": f'<rect x="10" y="12" width="28" height="28" rx="2" fill="#bcd7f5"/><path {_S} d="M10 40V12h28v28M6 40h36M16 18h4M28 18h4M16 25h4M28 25h4M21 40v-8h6v8"/><path fill="#e8384f" d="M18 6h12l-2 6H20z"/>',
    "star": f'<circle cx="24" cy="24" r="17" fill="#ffe08a"/><path {_S} d="M24 11l4 8.5 9.3 1.2-6.8 6.4 1.7 9.2L24 31.8l-8.2 4.5 1.7-9.2-6.8-6.4 9.3-1.2z"/><circle cx="24" cy="24" r="2.5" fill="#e8384f"/>',
    "book": f'<path fill="#bfe6dc" d="M24 13c-4-3-10-3-15-2v26c5-1 11-1 15 2z"/><path fill="#fff" d="M24 13c4-3 10-3 15-2v26c-5-1-11-1-15 2z"/><path {_S} d="M24 13c-4-3-10-3-15-2v26c5-1 11-1 15 2 4-3 10-3 15-2V11c-5-1-11-1-15 2zM24 13v26M29 18h6M29 23h6"/>',
    "calendar": f'<rect x="8" y="11" width="32" height="29" rx="3" fill="#fff"/><path fill="#e8384f" d="M8 14a3 3 0 0 1 3-3h26a3 3 0 0 1 3 3v6H8z"/><path {_S} d="M8 14a3 3 0 0 1 3-3h26a3 3 0 0 1 3 3v23a3 3 0 0 1-3 3H11a3 3 0 0 1-3-3zM8 20h32M16 7v7M32 7v7"/><path fill="#ffe08a" stroke="#2b2b2b" stroke-width="2" d="M15 26h6v6h-6z"/>',
    "plane": f'<circle cx="24" cy="24" r="17" fill="#bcd7f5"/><path {_S} fill="#fff" d="M40 12c-2-2-5-1-7 1l-5 5-14-4-3 3 11 7-5 5-5-1-2 2 6 3 3 6 2-2-1-5 5-5 7 11 3-3-4-14 5-5c2-2 3-5 1-7z"/>',
    "city": f'<rect x="6" y="38" width="36" height="2" fill="#2b2b2b"/><path fill="#ffd2d7" d="M9 22h10v18H9z"/><path fill="#bcd7f5" d="M19 10h10v30H19z"/><path fill="#bfe6dc" d="M29 18h10v22H29z"/><path {_S} d="M9 40V22h10M19 40V10h10v30M29 40V18h10v22M23 15h2M23 21h2M23 27h2M13 27h2M13 33h2M33 24h2M33 30h2M24 10V5"/>',
    "wave": f'<circle cx="34" cy="14" r="6" fill="#ffe08a" stroke="#2b2b2b" stroke-width="2"/><path fill="#bcd7f5" d="M5 30c5-6 9-6 13 0s9 6 13 0 9-6 12 0v12H5z"/><path {_S} d="M5 30c5-6 9-6 13 0s9 6 13 0 9-6 12 0M5 38c5-5 9-5 13 0s9 5 13 0 9-5 12 0"/>',
    "compass": f'<circle cx="24" cy="24" r="17" fill="#bfe6dc"/><circle {_S} fill="#fff" cx="24" cy="24" r="12"/><path fill="#e8384f" stroke="#2b2b2b" stroke-width="2" stroke-linejoin="round" d="M30 18l-4 8-8 4 4-8z"/><path {_S} d="M24 7v4M24 37v4M7 24h4M37 24h4"/>',
    "buoy": f'<circle cx="24" cy="24" r="16" fill="#fff"/><path fill="#e8384f" d="M13 13l6 6a7 7 0 0 0 0 10l-6 6a16 16 0 0 1 0-22zM35 13a16 16 0 0 1 0 22l-6-6a7 7 0 0 0 0-10z"/><circle {_S} cx="24" cy="24" r="16"/><circle {_S} cx="24" cy="24" r="7"/><path {_S} d="M13 13l6 6M35 13l-6 6M13 35l6-6M35 35l-6-6"/>',
    "bowl": f'<circle cx="24" cy="24" r="17" fill="#ffd2d7"/><path {_S} fill="#fff" d="M8 24h32a16 14 0 0 1-32 0z"/><path fill="#e8384f" d="M15 24c2-6 16-6 18 0z"/><circle cx="24" cy="21" r="3" fill="#ffe08a" stroke="#2b2b2b" stroke-width="2"/><path {_S} d="M30 6l-6 12M36 8l-8 11"/>',
    "info": f'<circle cx="24" cy="24" r="17" fill="#bcd7f5"/><circle {_S} cx="24" cy="24" r="12" fill="#fff"/><path {_S} d="M24 22v8M24 17v.5"/>',
    "person": f'<circle cx="24" cy="24" r="17" fill="#ffd2d7"/><circle {_S} fill="#fff" cx="24" cy="18" r="6"/><path {_S} fill="#fff" d="M13 38c1-7 5-10 11-10s10 3 11 10"/>',
    "bulb": f'<circle cx="24" cy="24" r="17" fill="#ffe08a"/><path {_S} fill="#fff" d="M18 26a8 8 0 1 1 12 0c-2 2-2 4-2 5h-8c0-1 0-3-2-5zM20 35h8M22 39h4"/>',
}
ICON = {"official": "info", "exp": "person", "plan": "calendar", "tip": "bulb"}
# 見出しの言葉で決めるアイコン（無ければ ICON）
ICON_BY_H = [("ユッケ", "bowl"), ("生もの", "bowl"), ("ハイアット", "hotel"), ("パラダイス", "star"), ("知っておく", "book"), ("プラン", "calendar"), ("仁川", "plane"),
             ("ソウル", "city"), ("釜山", "wave"), ("選ぶ", "compass"), ("のめり込", "buoy")]


def icon_for(b):
    k = next((ic for w, ic in ICON_BY_H if w in b["h"]), ICON[b["kind"]])
    return f'<svg viewBox="0 0 48 48" width="46" height="46" aria-hidden="true">{SVG[k]}</svg>'
SEC_ID = {"初めて行くなら知っておきたい事": "first", "カジノ旅": "casino", "人気のプラン": "plan", "韓国ごはん": "food"}


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


def page(path, title, desc, body, adsense=True, cur="index", og="korea/og-casino.jpg"):
    canonical = BASE_URL + "korea/" + path
    return f"""<!doctype html>
<html lang="ja"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title><meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="apple-touch-icon" href="/apple-touch-icon.png"><link rel="icon" type="image/png" href="/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta property="og:locale" content="ja_JP">{analytics_tag(adsense=adsense)}
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


def photos_html(ph):
    if not ph:
        return ""
    figs = "".join(f'<figure><img src="{KIMG}{e(f)}" alt="{e(c)}" loading="lazy"><figcaption>{e(c)}</figcaption></figure>' for f, c in ph)
    return f'<div class="photos">{figs}</div>'


def detail_page(key):
    p = D.PAGES[key]
    parts, icons = [], []
    for i, b in enumerate(p["blocks"]):
        bid = f"b{i + 1}"
        icons.append(f'<li><a href="#{bid}"><i>{icon_for(b)}</i>{e(b["h"])}</a></li>')
        pr = "".join(trip_line(k) for k in b["pr"])
        items = "".join(f"<li>{e(t)}</li>" for t in b["items"])
        parts.append(f'<section class="blk" id="{bid}"><span class="kind k-{b["kind"]}">{e(D.KIND_LABEL[b["kind"]])}</span>'
                     f'<h2>{e(b["h"])}</h2>{pr}<ul class="items">{items}</ul>{photos_html(b.get("photos"))}{src_links(b["src"], b["checked"])}</section>')
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
    return page(key + ".html", f"{p['title']}｜{SITE}", p["lead"], body, adsense=p["adsense"], cur=key, og=OG_IMG.get(key, "korea/og-casino.jpg"))


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
