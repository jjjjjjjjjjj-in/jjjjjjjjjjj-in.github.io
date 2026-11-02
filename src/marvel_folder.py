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
from urllib.parse import quote  # noqa: E402

# ページの下に出すおすすめ商品（PR）。運営者の希望で広告を増やした（2026-11-02）
# (日本語の表示名, 日本語の検索キーワード, 英語の表示名, 英語の検索キーワード)
PICKS = [
    ("マーベル公式の年表の本（英語）", "Marvel Cinematic Universe An Official Timeline", "The official MCU timeline book", "Marvel Cinematic Universe An Official Timeline"),
    ("Fire TV Stick（Disney+をテレビで）", "Fire TV Stick", "Fire TV Stick (Disney+ on your TV)", "Fire TV Stick"),
    ("マーベル映画のBlu-ray", "マーベル Blu-ray", "Marvel movies on Blu-ray", "Marvel Blu-ray"),
    ("マーベルのレゴ", "レゴ マーベル", "Marvel LEGO", "LEGO Marvel"),
    ("アベンジャーズのフィギュア", "アベンジャーズ フィギュア", "Avengers figures", "Avengers Marvel Legends figure"),
    ("マーベルのTシャツ", "マーベル Tシャツ", "Marvel T-shirts", "Marvel t-shirt"),
]
AMAZON_TAG, AMAZON_TAG_US = "doomsdayguide-22", "doomsdaygui08-20"
RAKUTEN_TOP = "https://af.moshimo.com/af/c/click?a_id=5875908&p_id=54&pc_id=54&pl_id=616"


def shop_html(lang):
    t = TEXT[lang]
    if lang == "en":
        links = [(en, f"https://www.amazon.com/s?k={quote(kw_en)}&tag={AMAZON_TAG_US}") for _, _, en, kw_en in PICKS]
    else:
        links = [(ja, f"https://www.amazon.co.jp/s?k={quote(kw)}&tag={AMAZON_TAG}") for ja, kw, _, _ in PICKS]
        links.append(("楽天でマーベルのグッズを探す", f"{RAKUTEN_TOP}&url={quote('https://search.rakuten.co.jp/search/mall/' + quote('マーベル グッズ') + '/', safe='')}"))
    btns = "".join(f'<a href="{e(u)}" target="_blank" rel="sponsored noopener">{e(l)}</a>' for l, u in links)
    return (f'<section class="mshop"><h2>{e(t["shop"])} <span class="mpr">{e(t["pr"])}</span></h2>'
            f'<div class="mshop-btns">{btns}</div><p class="mshop-note">{e(t["amazon_note"])}</p></section>')

e = html.escape

# ドゥームズデイ予習ガイドのカードの色
DOOMSDAY_THEME = dict(main="#1f5c3f", deep="#08140e", accent="#e0b04a", soft="#dde9e1")

TEXT = {
    "ja": dict(menu="メニュー", search="作品を探す", search_ph="作品名で探す", all="ALL", home="作品一覧（トップ）", doomsday_link="ドゥームズデイ予習ガイド", doomsday_href="https://jjjjjjjjjjj-in.github.io/doomsday-guide/",
               other="English", other_href="en/", none="見つかりませんでした", soon="準備中（これから作ります）",
               doomsday="ドゥームズデイ予習ガイド", shop="マーベル映画をもっと楽しむ", pr="PR", amazon_note="Amazonのアソシエイトとして、当サイトは適格販売により収入を得ています。", doomsday_sub="視聴順チェックリスト", close="閉じる", released="公開年", setin="作中の年代",
               note="個人が運営する非公式のファンサイトです。Marvel Studios、The Walt Disney Company とは関係ありません。各サイトにはアフィリエイト広告（PR）を含むページがあります。",
               policy="プライバシーポリシー"),
    "en": dict(menu="Menu", search="Search titles", search_ph="Search by title", all="ALL", home="All titles (top)", doomsday_link="Doomsday Watch Guide", doomsday_href="https://jjjjjjjjjjj-in.github.io/doomsday-guide/en/",
               other="日本語", other_href="../", none="No matches", soon="Coming soon",
               doomsday="Doomsday Watch Guide", shop="More Marvel fun", pr="Ad", amazon_note="As an Amazon Associate, this site earns from qualifying purchases.", doomsday_sub="Story-order checklist", close="Close", released="Released", setin="Set in",
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
.mhead button svg { width: 26px; height: 26px; }
.mlogo-svg { display: block; height: 50px; width: 143px; }
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
/* 公開年と作中の年代（運営者の希望、2026-11-02） */
.poster .pmeta { position: relative; z-index: 1; display: flex; gap: 14px; align-items: flex-start; }
.poster .pm { display: grid; gap: 2px; }
.poster .pm small { font-size: 9px; font-weight: 700; line-height: 1; letter-spacing: .04em; color: rgba(255,255,255,.75); }
.poster .pyear { font-family: "Anton", sans-serif; font-size: 14px; line-height: 1; letter-spacing: .06em; color: var(--p-accent); }
.poster .pera { font-weight: 800; font-size: 12px; line-height: 1.1; color: #fff; white-space: nowrap; }
.poster .pt { position: relative; z-index: 1; font-weight: 900; font-size: clamp(13px, 3.6vw, 17px); line-height: 1.2; text-shadow: 0 1px 4px rgba(0,0,0,.6);
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.poster .ps { display: none; }
.mcard .name { display: block; margin-top: 8px; font-size: 16px; line-height: 1.45; }
.soonbadge { display: inline-block; font-size: 11px; font-weight: 900; color: #fff; background: #e23636; border-radius: 4px; padding: 0 6px; vertical-align: 2px; }
.unote { display: block; font-size: 12px; color: var(--muted); }
.soon { grid-column: 1 / -1; padding: 16px; border: 2px dashed var(--line); border-radius: 8px; color: var(--muted); font-weight: 700; text-align: center; }
.mnone { text-align: center; color: var(--muted); }
.mfeats { margin: 34px 0 0; }
.mfeats h2 { font-size: 15px; font-weight: 700; color: var(--muted); margin: 0 0 12px; letter-spacing: .04em; }
.mfeats ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }
@media (min-width: 720px) { .mfeats ul { grid-template-columns: repeat(3, 1fr); } }
.mfeat { display: block; height: 100%; text-decoration: none; color: #fff; background: #111; border-left: 6px solid #e23636; border-radius: 8px; padding: 12px 14px; }
.mfeat b { display: block; font-size: 17px; color: #f2c02e; }
.mfeat span { font-size: 13px; color: #ddd; }
.mshop { margin: 36px 0 0; padding: 18px 16px; background: #fff; border-radius: 10px; box-shadow: 0 1px 4px rgba(0,0,0,.08); }
.mshop h2 { margin: 0 0 12px; font-size: 18px; }
.mpr { display: inline-block; margin-left: 6px; padding: 1px 6px; border: 1px solid var(--muted); border-radius: 4px; font-size: 11px; color: var(--muted); vertical-align: middle; }
.mshop-btns { display: flex; flex-wrap: wrap; gap: 8px; }
.mshop-btns a { display: inline-block; padding: 9px 14px; border: 1px solid var(--line); border-radius: 999px; background: #f6f6f6; color: var(--ink); font-size: 14px; font-weight: 700; text-decoration: none; }
.mshop-btns a:hover { background: #ececec; }
.mshop-note { margin: 12px 0 0; font-size: 12px; color: var(--muted); }
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

# 手描きのイラスト風の「赤い四角に白い文字」（運営者の希望、2026-11-02）。
# 公式ロゴとは違うと分かるように、四角はふちがガタガタのマーカー塗り、文字も少し傾けてにじませる。画像ファイルは使わない
LOGO_SVG = """<svg class="mlogo-svg" viewBox="0 0 240 84" role="img" aria-hidden="true">
  <defs>
    <filter id="rough" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency="0.04" numOctaves="3" seed="7" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="6"/>
    </filter>
    <filter id="roughText" x="-10%" y="-10%" width="120%" height="120%">
      <feTurbulence type="fractalNoise" baseFrequency="0.09" numOctaves="2" seed="3" result="n"/>
      <feDisplacementMap in="SourceGraphic" in2="n" scale="2.6"/>
    </filter>
    <pattern id="strokes" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(-24)">
      <rect width="9" height="9" fill="#e2232f"/>
      <path d="M0 4.5h9" stroke="#b5121d" stroke-width="2.2" opacity=".55"/>
    </pattern>
  </defs>
  <g transform="rotate(-2.2 120 42)">
    <path d="M10 9 Q62 4 120 7 T231 8 Q236 40 232 76 Q170 81 118 78 T8 77 Q4 44 10 9 Z" fill="url(#strokes)" filter="url(#rough)"/>
    <path d="M12 12 Q120 6 228 11" fill="none" stroke="#ff6b73" stroke-width="2" opacity=".55" filter="url(#rough)"/>
    <text x="120" y="66" text-anchor="middle" font-family="Anton, Impact, sans-serif" font-size="60" letter-spacing="-1"
      fill="#fff" stroke="#fff" stroke-width="1.2" stroke-linejoin="round" transform="translate(120 66) scale(1 1.12) translate(-120 -66)"
      filter="url(#roughText)">MARVEL</text>
  </g>
</svg>"""

ICON_MENU = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 7h18M3 12h18M3 17h18" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>'
ICON_SEARCH = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2.6"/><path d="M15.5 15.5l5 5" stroke="currentColor" stroke-width="2.8" stroke-linecap="round"/></svg>'


# 公開予定の作品（作品ガイドはまだ作らない。公式ページへリンク）。group の区分の最後に出す（運営者の希望、2026-11-02）
# 日付はアメリカの公開日（2025年5月の延期発表。marvel.com で確認、2026-11-02）。日本の公開日は未発表
UPCOMING = [
    dict(group="doomsday", title="アベンジャーズ／シークレット・ウォーズ", title_en="Avengers: Secret Wars", big="SECRET WARS",
         date="2027年12月17日（米国）", date_en="Dec 17, 2027 (US)", note="日本の公開日は未発表", note_en="Japan date TBA",
         url="https://www.marvel.com/movies/avengers-secret-wars",
         theme=dict(main="#5b2a86", deep="#12061f", accent="#f2c02e", soft="#e9def5")),
]


def upcoming_card(u, lang):
    t = TEXT[lang]
    en = lang == "en"
    th = u["theme"]
    style = f'--p-main:{th["main"]};--p-deep:{th["deep"]};--p-accent:{th["accent"]};--p-soft:{th["soft"]}'
    name = u["title_en"] if en else u["title"]
    q = e((u["title"] + " " + u["title_en"]).lower())
    return (f'<li data-q="{q}"><a class="mcard" href="{e(u["url"])}" target="_blank" rel="noopener">'
            f'<span class="poster" style="{style}"><span class="pmeta">'
            f'<span class="pm"><small>{"Coming" if en else "公開予定"}</small><span class="pera">{e(u["date_en"] if en else u["date"])}</span></span></span>'
            f'<span class="pt">{e(u["big"])}</span></span>'
            f'<span class="name">{e(name)} <span class="soonbadge">{"COMING SOON" if en else "公開予定"}</span></span>'
            f'<span class="unote">{e(u["note_en"] if en else u["note"])}・{"official site" if en else "公式サイトへ"}</span></a></li>')


def site_card(site, lang, prefix):
    """1作品（または予習ガイド）のポスター風カード"""
    t = TEXT[lang]
    path = site["en_path"] if lang == "en" else site["path"]
    slug = site["path"].strip("/").split("/")[0]
    if slug == "doomsday-guide":
        th, name, big, sub, year, era = DOOMSDAY_THEME, t["doomsday"], "DOOMSDAY", t["doomsday_sub"], "2026", ""
    else:
        rec = TITLES[slug]
        th = FILM_GUIDES.get(slug, {}).get("theme") or DOOMSDAY_THEME
        name = rec["title_en"] if lang == "en" else rec["title"]
        sep = ": " if lang == "en" else "／"
        parts = name.split(sep, 1)
        big, sub, year = parts[0], (parts[1] if len(parts) > 1 else ""), rec["year"]
        # 作中の年代（かっこの中の補足は省く）。運営者の希望で公開年と並べて出す（2026-11-02）
        era = (rec["era_en"].split(" (")[0] if lang == "en" else rec["era"].split("（")[0])
    style = f'--p-main:{th["main"]};--p-deep:{th["deep"]};--p-accent:{th["accent"]};--p-soft:{th["soft"]}'
    q = e((name + " " + site.get("name", "") + " " + site.get("name_en", "")).lower())
    return (f'<li data-q="{q}"><a class="mcard" href="{e(prefix + path)}">'
            f'<span class="poster" style="{style}"><span class="pmeta">'
            f'<span class="pm"><small>{e(t["released"])}</small><span class="pyear">{e(year)}</span></span>'
            + (f'<span class="pm"><small>{e(t["setin"])}</small><span class="pera">{e(era)}</span></span>' if era else "") + '</span>'
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
        ups = "".join(upcoming_card(u, lang) for u in UPCOMING if u["group"] == k)
        body = ("".join(site_card(s, lang, prefix) for s in sites) + ups) if (sites or ups) else f'<li class="soon">{e(t["soon"])}</li>'
        groups += f'<section class="mgroup" id="{k}"><h2>{e(title)}</h2><p class="gdesc">{e(desc)}</p><ul class="mgrid">{body}</ul></section>\n'
    # 特集ページ（年表・興行収入・再上映。日本語だけ）
    feat_menu, feats = "", ""
    if lang == "ja":
        import marvel_pages
        feat_menu = "".join(f'  <li><a href="{prefix}{p}">{e(n)}</a></li>\n' for p, n, _ in marvel_pages.PAGES)
        feats = marvel_pages.feature_html(prefix)
    page_title = f'{f["name"]} | {site_name}' if lang == "en" else f'{f["name"]}｜{site_name}'
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><link rel="apple-touch-icon" href="/icons/movie.png"><link rel="icon" type="image/png" href="/icons/movie.png">{analytics}
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
  <li><a href="./">{e(t["home"])}</a></li>
  <li><a href="{t["doomsday_href"]}">{e(t["doomsday_link"])}</a></li>
{feat_menu}
  <li><a href="{t["other_href"]}" hreflang="{"ja" if lang == "en" else "en"}">{e(t["other"])}</a></li>
</ul></nav>
<div class="msearch" id="msearch" hidden><input type="search" placeholder="{e(t["search_ph"])}" aria-label="{e(t["search_ph"])}"></div>
<main class="mmain">
  <h1 class="mtitle">{e(f["name"])}</h1>
  <p class="mdesc">{e(f["desc"])}</p>
  <div class="mtabs" role="tablist">{tabs}</div>
  <p class="mnone" id="mnone" hidden>{e(t["none"])}</p>
{groups}{feats}{shop_html(lang)}</main>
<footer class="mfoot">{e(t["note"])} <a href="{prefix}privacy.html{"#en" if lang == "en" else ""}">{e(t["policy"])}</a></footer>
{SCRIPT}
</body>
</html>
"""
