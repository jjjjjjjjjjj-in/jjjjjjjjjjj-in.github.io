"""マーベル映画紹介のフォルダのページ（/marvel/ と /marvel/en/）。

見た目（2026-11-02、運営者の希望。マーベル公式サイトの作品一覧のような形）:
黒い帯のヘッダー（左にメニュー、中央に白い「MARVEL」の文字、右に検索）、灰色の背景、中央の大きな見出し、
区分のタブ（押すとその区分だけ表示）、作品ごとのポスター風カード（スマホ2列）と、その下に作品名。
ポスター風カードは画像を使わず、作品ガイドの色（films.py の theme）と文字で作る（映画の画像は使えないため）。
"""
import html
import os
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(SRC, "mcu"))
from films import FILM_GUIDES  # noqa: E402
from titles import TITLES  # noqa: E402

e = html.escape

# ドゥームズデイ予習ガイドのカードの色
DOOMSDAY_THEME = dict(main="#1f5c3f", deep="#08140e", accent="#e0b04a", soft="#dde9e1")

TEXT = {
    "ja": dict(menu="メニュー", search="作品を探す", search_ph="作品名で探す", all="ALL", home="もっちぃま（サイト一覧）",
               other="English", other_href="en/", none="見つかりませんでした", soon="準備中（これから作ります）",
               doomsday="ドゥームズデイ予習ガイド", doomsday_sub="視聴順チェックリスト", close="閉じる",
               note="個人が運営する非公式のファンサイトです。Marvel Studios、The Walt Disney Company とは関係ありません。各サイトにはアフィリエイト広告（PR）を含むページがあります。",
               policy="プライバシーポリシー"),
    "en": dict(menu="Menu", search="Search titles", search_ph="Search by title", all="ALL", home="Mocchima (all sites)",
               other="日本語", other_href="../", none="No matches", soon="Coming soon",
               doomsday="Doomsday Watch Guide", doomsday_sub="Story-order checklist", close="Close",
               note="An unofficial fan site run by an individual, not affiliated with Marvel Studios or The Walt Disney Company. Some pages contain affiliate links (ads).",
               policy="Privacy policy"),
}

STYLE = """<style>
:root { --bg: #eef0f3; --ink: #111; --muted: #5d636b; --line: #d6dae0; --accent: #2f6fe0; }
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: "Zen Kaku Gothic New", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", sans-serif; line-height: 1.6; }
a { color: inherit; }
/* ヘッダー：黒い帯。左メニュー・中央MARVEL・右検索 */
.mhead { position: sticky; top: 0; z-index: 20; background: #000; color: #fff; height: 64px; display: grid; grid-template-columns: 56px 1fr 56px; align-items: center; }
.mhead button { background: none; border: 0; color: #fff; width: 56px; height: 64px; display: grid; place-items: center; cursor: pointer; padding: 0; }
.mhead svg { width: 26px; height: 26px; }
.mlogo { justify-self: center; font-family: "Anton", "Oswald", "Impact", "Arial Narrow", sans-serif; color: #fff; text-decoration: none;
  font-size: 40px; line-height: 1; letter-spacing: -.02em; transform: scaleY(1.18); display: inline-block; padding: 0 .1em; }
.mmenu, .msearch { position: sticky; top: 64px; z-index: 19; background: #111; color: #fff; padding: 10px 16px 14px; }
.mmenu[hidden], .msearch[hidden] { display: none; }
.mmenu ul { list-style: none; margin: 0 auto; padding: 0; max-width: 1100px; display: grid; gap: 2px; }
.mmenu a { display: block; padding: 10px 4px; color: #fff; text-decoration: none; font-weight: 700; border-bottom: 1px solid #333; }
.msearch input { width: 100%; max-width: 1100px; display: block; margin: 0 auto; font: inherit; font-size: 16px; padding: 10px 12px; border-radius: 6px; border: 0; }
.mmain { max-width: 1100px; margin: 0 auto; padding: 28px 16px 48px; }
.mtitle { text-align: center; margin: 4px 0 10px; font-size: clamp(34px, 10vw, 56px); font-weight: 900; letter-spacing: .02em; line-height: 1.2; }
.mdesc { text-align: center; margin: 0 auto 22px; max-width: 46em; color: var(--muted); font-size: 14px; }
/* タブ */
.mtabs { display: flex; gap: 26px; overflow-x: auto; scrollbar-width: none; border-bottom: 1px solid var(--line); margin: 0 -16px 22px; padding: 0 16px; }
.mtabs::-webkit-scrollbar { display: none; }
.mtabs button { background: none; border: 0; font: inherit; font-size: 17px; font-weight: 700; color: #333; padding: 8px 0 10px; white-space: nowrap; cursor: pointer; border-bottom: 4px solid transparent; }
.mtabs button[aria-selected="true"] { color: var(--ink); border-bottom-color: var(--accent); }
/* 区分 */
.mgroup { margin-bottom: 30px; }
.mgroup[hidden] { display: none; }
.mgroup h2 { font-size: 15px; font-weight: 700; color: var(--muted); margin: 0 0 12px; letter-spacing: .04em; }
.mgroup .gdesc { margin: -8px 0 12px; font-size: 13px; color: var(--muted); }
.mgrid { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 22px 16px; }
@media (min-width: 720px) { .mgrid { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 28px 20px; } }
@media (min-width: 1000px) { .mgrid { grid-template-columns: repeat(5, minmax(0, 1fr)); } }
.mgrid li[hidden] { display: none; }
.mcard { display: block; text-decoration: none; color: var(--ink); }
.mcard:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; border-radius: 8px; }
/* ポスター風カード（画像なし。作品の色と文字）。幅はそのまま、高さは縦長ポスターの約4分の1の横長の帯（運営者の希望、2026-11-02） */
.poster { position: relative; aspect-ratio: 8 / 3; border-radius: 6px; overflow: hidden; color: #fff; display: grid; align-content: space-between; padding: 8px 10px;
  background: radial-gradient(120% 160% at 80% 0%, var(--p-main) 0%, var(--p-deep) 75%); box-shadow: 0 2px 6px rgba(0,0,0,.18); }
.poster::before { content: ""; position: absolute; top: -40%; right: -12%; width: 55%; aspect-ratio: 1; border-radius: 50%; border: 6px solid var(--p-accent); opacity: .3; }
.poster .pyear { position: relative; z-index: 1; font-family: "Anton", sans-serif; font-size: 14px; line-height: 1; letter-spacing: .06em; color: var(--p-accent); }
.poster .pt { position: relative; z-index: 1; font-weight: 900; font-size: clamp(13px, 3.6vw, 17px); line-height: 1.2; text-shadow: 0 1px 4px rgba(0,0,0,.6);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.poster .ps { display: none; }
.mcard .name { display: block; margin-top: 8px; font-size: 16px; line-height: 1.45; }
.soon { grid-column: 1 / -1; padding: 16px; border: 2px dashed var(--line); border-radius: 8px; color: var(--muted); font-weight: 700; text-align: center; }
.mnone { text-align: center; color: var(--muted); }
.mfoot { max-width: 1100px; margin: 0 auto; padding: 18px 16px 40px; font-size: 12.5px; color: var(--muted); border-top: 1px solid var(--line); }
</style>"""

SCRIPT = """<script>
(function(){
  var $=function(s){return document.querySelector(s)}, $$=function(s){return Array.prototype.slice.call(document.querySelectorAll(s))};
  function toggle(btn, panel){ btn.addEventListener('click', function(){ var open=panel.hidden; $$('.mmenu,.msearch').forEach(function(p){p.hidden=true});
    $$('.mhead button').forEach(function(b){b.setAttribute('aria-expanded','false')}); panel.hidden=!open; btn.setAttribute('aria-expanded', String(open));
    if(open && panel.querySelector('input')) panel.querySelector('input').focus(); }); }
  toggle($('#mbtn-menu'), $('#mmenu')); toggle($('#mbtn-search'), $('#msearch'));
  var tabs=$$('.mtabs button');
  function show(key){ tabs.forEach(function(t){t.setAttribute('aria-selected', String(t.dataset.key===key))});
    $$('.mgroup').forEach(function(g){ g.hidden = !(key==='all' || g.id===key); }); }
  tabs.forEach(function(t){ t.addEventListener('click', function(){ show(t.dataset.key); try{history.replaceState(null,'',t.dataset.key==='all'?location.pathname:'#'+t.dataset.key)}catch(e){} }); });
  if(location.hash && $('.mtabs button[data-key="'+location.hash.slice(1)+'"]')) show(location.hash.slice(1));
  var input=$('#msearch input'), none=$('#mnone');
  input.addEventListener('input', function(){ var q=input.value.trim().toLowerCase(), hit=0;
    if(q) show('all');
    $$('.mgrid li[data-q]').forEach(function(li){ var ok=!q || li.dataset.q.indexOf(q)>=0; li.hidden=!ok; if(ok) hit++; });
    $$('.mgroup').forEach(function(g){ if(q) g.hidden = !g.querySelector('li[data-q]:not([hidden])'); });
    none.hidden = !(q && !hit); });
})();
</script>"""

ICON_MENU = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M15.5 15.5l5 5" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/></svg>'


def site_card(site, lang, prefix):
    """1作品（または予習ガイド）のポスター風カード"""
    t = TEXT[lang]
    path = site["en_path"] if lang == "en" else site["path"]
    slug = site["path"].strip("/").split("/")[0]
    if slug == "doomsday-guide":
        th, name, big, sub, year = DOOMSDAY_THEME, t["doomsday"], "DOOMSDAY", t["doomsday_sub"], "2026"
    else:
        rec = TITLES[slug]
        th = FILM_GUIDES.get(slug, {}).get("theme") or DOOMSDAY_THEME
        name = rec["title_en"] if lang == "en" else rec["title"]
        sep = ": " if lang == "en" else "／"
        parts = name.split(sep, 1)
        big, sub, year = parts[0], (parts[1] if len(parts) > 1 else ""), rec["year"]
    style = f'--p-main:{th["main"]};--p-deep:{th["deep"]};--p-accent:{th["accent"]};--p-soft:{th["soft"]}'
    q = e((name + " " + site.get("name", "") + " " + site.get("name_en", "")).lower())
    return (f'<li data-q="{q}"><a class="mcard" href="{e(prefix + path)}">'
            f'<span class="poster" style="{style}" aria-hidden="true"><span class="pyear">{e(year)}</span>'
            f'<span class="pt">{e(big)}</span>' + (f'<span class="ps">{e(sub)}</span>' if sub else "") + '</span>'
            f'<span class="name">{e(name)}</span></a></li>')


def build(f, sites_in_group, head_extra, base_url, site_name, analytics):
    """f: FOLDERS の1件。sites_in_group(key) は区分ごとのサイト一覧を返す"""
    lang = f["lang"]
    t = TEXT[lang]
    prefix = "../" * f["path"].count("/")
    tabs = f'<button type="button" role="tab" data-key="all" aria-selected="true">{e(t["all"])}</button>' + "".join(
        f'<button type="button" role="tab" data-key="{k}" aria-selected="false">{e(short)}</button>' for k, _, _, short in f["groups"])
    groups = ""
    for k, title, desc, _ in f["groups"]:
        sites = sites_in_group(k)
        body = "".join(site_card(s, lang, prefix) for s in sites) if sites else f'<li class="soon">{e(t["soon"])}</li>'
        groups += f'<section class="mgroup" id="{k}"><h2>{e(title)}</h2><p class="gdesc">{e(desc)}</p><ul class="mgrid">{body}</ul></section>\n'
    page_title = f'{f["name"]} | {site_name}' if lang == "en" else f'{f["name"]}｜{site_name}'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">{analytics}
<title>{e(page_title)}</title>
<meta name="description" content="{e(f["desc"])}">
<link rel="canonical" href="{base_url}{f["path"]}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap">
{STYLE}
</head>
<body>
<header class="mhead">
  <button type="button" id="mbtn-menu" aria-label="{e(t["menu"])}" aria-expanded="false" aria-controls="mmenu">{ICON_MENU}</button>
  <a class="mlogo" href="./" aria-label="{e(f["logo"])}">{e(f["logo"])}</a>
  <button type="button" id="mbtn-search" aria-label="{e(t["search"])}" aria-expanded="false" aria-controls="msearch">{ICON_SEARCH}</button>
</header>
<nav class="mmenu" id="mmenu" hidden><ul>
  <li><a href="{prefix}">{e(t["home"])}</a></li>
  <li><a href="{t["other_href"]}" hreflang="{"ja" if lang == "en" else "en"}">{e(t["other"])}</a></li>
</ul></nav>
<div class="msearch" id="msearch" hidden><input type="search" placeholder="{e(t["search_ph"])}" aria-label="{e(t["search_ph"])}"></div>
<main class="mmain">
  <h1 class="mtitle">{e(f["name"])}</h1>
  <p class="mdesc">{e(f["desc"])}</p>
  <div class="mtabs" role="tablist">{tabs}</div>
  <p class="mnone" id="mnone" hidden>{e(t["none"])}</p>
{groups}</main>
<footer class="mfoot">{e(t["note"])} <a href="{prefix}privacy.html{"#en" if lang == "en" else ""}">{e(t["policy"])}</a></footer>
{SCRIPT}
</body>
</html>
"""
