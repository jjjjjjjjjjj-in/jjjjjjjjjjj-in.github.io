"""マーベル映画紹介の特集ページ（運営者の希望、2026-11-02）。日本語だけ。

- /marvel/timeline/   MCU 完全年表（src/marvel_data/timeline.json。元の文は timeline_raw.txt、作るのは make_timeline.py）
- /marvel/box-office/ 興行収入ランキング（src/marvel_data/box_office.json）
- /marvel/rerelease/  再上映情報（src/marvel_data/rerelease.json）

データを直すときは JSON（年表は timeline_raw.txt と make_timeline.py）を直して python3 src/build.py を実行する。
デザインは黒地に赤と金。ヘッダーはマーベル映画紹介のページと同じ黒い帯（☰メニューからもっちぃまへは行かない）。
"""
import html
import json
import os
import re
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
DATA = os.path.join(SRC, "marvel_data")
sys.path.insert(0, os.path.join(SRC, "mcu"))
from films import FILM_GUIDES  # noqa: E402
from titles import TITLES  # noqa: E402
import marvel_folder  # noqa: E402

e = html.escape
DOOMSDAY = "https://mocchima.com/doomsday-guide/"

# 映画以外（ドラマ・配信）の作品。年表の「映画／ドラマ」の絞り込みに使う
SERIES = {"loki-s1", "loki-s2", "wandavision", "falcon-and-winter-soldier", "hawkeye", "moon-knight", "echo", "she-hulk",
          "ms-marvel", "werewolf-by-night", "guardians-holiday-special", "secret-invasion", "agatha-all-along",
          "daredevil-born-again-s1", "ironheart", "visionquest", "i-am-groot-1", "i-am-groot-2"}

PAGES = [  # (パス, メニューの名前, 特集の説明)
    ("marvel/timeline/", "MCU完全年表", "宇宙の誕生から2025年まで。出来事と作品を、物語の時代順に"),
    ("marvel/box-office/", "興行収入ランキング", "世界の歴代ランキングと、マーベル作品の中の順位"),
    ("marvel/rerelease/", "再上映情報", "『エンドゲーム』『ブランド・ニュー・デイ』の再上映"),
]


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def has_guide(slug):
    return slug in FILM_GUIDES and os.path.isdir(os.path.join(ROOT, slug))


def work_href(slug, prefix):
    """作品ガイドがあればそこへ、なければドゥームズデイ予習ガイドのその作品の行へ（リンク切れを作らない）"""
    return f"{prefix}{slug}/" if has_guide(slug) else f"{DOOMSDAY}#{slug}"


def title_of(slug):
    return TITLES[slug]["title"] if slug in TITLES else slug


def yen_like(n):
    """29億4,218万ドル のような読み方"""
    oku, man = divmod(n // 10000, 10000)
    return f"約{oku}億{man:,}万ドル" if oku else f"約{man:,}万ドル"


STYLE = """<style>
:root { --bg: #0b0b0d; --card: #16161b; --card2: #1e1e25; --ink: #f2f2f4; --muted: #a3a3ad; --line: #2c2c35; --red: #e23636; --gold: #f2c02e; }
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; scroll-padding-top: 120px; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: "Zen Kaku Gothic New", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", sans-serif; line-height: 1.7; }
a { color: var(--gold); }
.mhead { position: sticky; top: 0; z-index: 20; background: #000; color: #fff; height: 64px; display: grid; grid-template-columns: 56px 1fr 56px; align-items: center; border-bottom: 3px solid var(--red); }
.mhead button, .mhead .hb { background: none; border: 0; color: #fff; width: 56px; height: 64px; display: grid; place-items: center; cursor: pointer; padding: 0; }
.mhead svg { width: 26px; height: 26px; }
.mlogo { justify-self: center; font-family: "Anton", "Impact", sans-serif; color: #fff; text-decoration: none; font-size: 40px; line-height: 1; transform: scaleY(1.18); display: inline-block; }
.mmenu { position: sticky; top: 67px; z-index: 19; background: #111; padding: 10px 16px 14px; }
.mmenu[hidden] { display: none; }
.mmenu ul { list-style: none; margin: 0 auto; padding: 0; max-width: 980px; display: grid; gap: 2px; }
.mmenu a { display: block; padding: 10px 4px; color: #fff; text-decoration: none; font-weight: 700; border-bottom: 1px solid #333; }
.mmenu a[aria-current] { color: var(--gold); }
main { max-width: 980px; margin: 0 auto; padding: 22px 16px 48px; }
.crumb { font-size: 13px; color: var(--muted); margin: 0 0 14px; }
.crumb a { color: var(--muted); }
.kicker { font-family: "Anton", sans-serif; letter-spacing: .12em; color: var(--red); font-size: 15px; margin: 0; }
h1 { margin: 2px 0 8px; font-size: clamp(30px, 8vw, 46px); font-weight: 900; line-height: 1.25; }
h1 .g { color: var(--gold); }
.lead { color: #d6d6dc; margin: 0 0 8px; }
.meta { font-size: 12.5px; color: var(--muted); margin: 0 0 18px; }
h2 { font-size: 21px; margin: 34px 0 12px; padding-left: 12px; border-left: 5px solid var(--red); line-height: 1.4; }
.box { background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 16px; }
.chip { display: inline-block; font-size: 11.5px; font-weight: 700; padding: 1px 8px; border-radius: 999px; border: 1px solid var(--line); color: var(--muted); white-space: nowrap; }
.chip.ok { color: #0b0b0d; background: var(--gold); border-color: var(--gold); }
.chip.part { color: var(--gold); border-color: var(--gold); }
.chip.data, .chip.check { color: #ff8a8a; border-color: #8a2a2a; }
.chip.red { color: #fff; background: var(--red); border-color: var(--red); }
.src { font-size: 13px; color: var(--muted); }
.src li { margin: 4px 0; }
.foot { max-width: 980px; margin: 0 auto; padding: 18px 16px 40px; font-size: 12.5px; color: var(--muted); border-top: 1px solid var(--line); }
.foot a { color: var(--muted); }
.mshop { margin: 36px 0 0; padding: 18px 16px; background: var(--card); border: 1px solid var(--line); border-radius: 12px; }
.mshop h2 { margin: 0 0 12px; border: 0; padding: 0; font-size: 18px; }
.mpr { display: inline-block; margin-left: 6px; padding: 1px 6px; border: 1px solid var(--muted); border-radius: 4px; font-size: 11px; color: var(--muted); vertical-align: middle; }
.mshop-btns { display: flex; flex-wrap: wrap; gap: 8px; }
.mshop-btns a { padding: 9px 14px; border: 1px solid var(--line); border-radius: 999px; background: var(--card2); color: var(--ink); font-size: 14px; font-weight: 700; text-decoration: none; }
.mshop-note { margin: 12px 0 0; font-size: 12px; color: var(--muted); }
/* 年表 */
.tools { display: grid; gap: 10px; margin: 0 0 8px; }
.tools input, .tools select { width: 100%; font: inherit; font-size: 16px; padding: 10px 12px; border-radius: 8px; border: 1px solid var(--line); background: var(--card); color: var(--ink); }
.seg { display: flex; flex-wrap: wrap; gap: 6px; }
.seg button { font: inherit; font-size: 13.5px; font-weight: 700; padding: 6px 12px; border-radius: 999px; border: 1px solid var(--line); background: var(--card); color: var(--ink); cursor: pointer; }
.seg button[aria-pressed="true"] { background: var(--red); border-color: var(--red); color: #fff; }
.count { font-size: 13px; color: var(--muted); margin: 6px 0 0; }
.eranow { position: sticky; top: 67px; z-index: 10; background: rgba(11,11,13,.94); backdrop-filter: blur(4px); border-bottom: 1px solid var(--line); margin: 14px -16px 0; padding: 8px 16px; display: flex; gap: 10px; align-items: center; font-weight: 900; }
.eranow small { font-family: "Anton", sans-serif; letter-spacing: .12em; color: var(--red); font-size: 12px; font-weight: 400; }
.eranow span { color: var(--gold); font-size: 17px; }
.era { margin-top: 16px; }
.era > h2 { font-size: 19px; margin-bottom: 8px; }
.era[hidden], .ev[hidden] { display: none; }
.era > h2 { margin-top: 0; }
.tl { list-style: none; margin: 0; padding: 0 0 0 18px; position: relative; }
.tl::before { content: ""; position: absolute; left: 5px; top: 6px; bottom: 6px; width: 2px; background: linear-gradient(var(--red), #5a1414); }
/* 1画面に多く出せるよう、詰めて1行に並べる（運営者の希望、2026-11-02） */
.ev { position: relative; margin: 0 0 5px; background: var(--card); border: 1px solid var(--line); border-radius: 8px; padding: 5px 9px; display: flex; flex-wrap: wrap; align-items: center; column-gap: 6px; row-gap: 3px; line-height: 1.45; }
.ev::before { content: ""; position: absolute; left: -17px; top: 10px; width: 8px; height: 8px; border-radius: 50%; background: var(--bg); border: 2px solid var(--red); }
.ev.main { border-color: #5c4a12; background: linear-gradient(90deg, #241d08, var(--card) 60%); }
.ev.main::before { background: var(--gold); border-color: var(--gold); width: 10px; height: 10px; left: -18px; top: 9px; }
.ev .when { font-size: 11.5px; font-weight: 700; color: var(--gold); white-space: nowrap; }
.ev { letter-spacing: -.01em; font-feature-settings: "palt"; }
.ev .txt { font-weight: 700; font-size: 14px; }
.ev a.txt { color: var(--ink); text-decoration: none; }
.ev a.txt::after { content: " ›"; color: var(--red); }
.ev .chip { font-size: 10.5px; padding: 0 6px; }
.ev .tags { display: contents; }
.ev .tags a, .ev .tags .chip { font-size: 11px; font-weight: 700; text-decoration: none; padding: 1px 7px; border-radius: 999px; background: var(--card2); border: 1px solid var(--line); color: #d6d6dd; line-height: 1.5; }
.ev .tags a.kind-s { border-color: #4a3a7a; }
.ev .tags a::after { content: " ›"; color: var(--red); }
.ev .note { flex-basis: 100%; margin: 0; font-size: 11.5px; color: #b9b9c2; line-height: 1.5; }
.ev .orig { font-size: 12px; color: var(--muted); }
.legend { display: flex; flex-wrap: wrap; gap: 8px 14px; font-size: 12.5px; color: var(--muted); margin: 8px 0 0; }
.none { text-align: center; color: var(--muted); padding: 20px; }
/* 興行収入 */
.ranks { list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }
.rk { display: grid; grid-template-columns: 64px 1fr; gap: 12px; align-items: stretch; background: var(--card); border: 1px solid var(--line); border-radius: 12px; padding: 12px; }
.rk .no { display: grid; place-items: center; text-align: center; font-family: "Anton", sans-serif; font-size: 44px; line-height: 1; color: var(--gold); }
.rk .no small { display: block; font-family: inherit; font-size: 11px; color: var(--muted); letter-spacing: .04em; font-weight: 700; font-family: "Zen Kaku Gothic New", sans-serif; }
.rk .poster { border-radius: 8px; padding: 8px 10px; color: #fff; background: radial-gradient(120% 160% at 80% 0%, var(--p-main), var(--p-deep) 75%); position: relative; overflow: hidden; }
.rk .poster::before { content: ""; position: absolute; top: -40%; right: -10%; width: 45%; aspect-ratio: 1; border-radius: 50%; border: 6px solid var(--p-accent); opacity: .3; }
.rk .poster b { position: relative; display: block; font-size: 17px; font-weight: 900; line-height: 1.3; text-shadow: 0 1px 4px rgba(0,0,0,.6); }
.rk .poster i { position: relative; display: block; font-style: normal; font-size: 12px; color: rgba(255,255,255,.8); }
.rk .gross { font-family: "Anton", sans-serif; font-size: 24px; letter-spacing: .02em; color: #fff; margin: 8px 0 0; line-height: 1.2; }
.rk .gross small { font-family: "Zen Kaku Gothic New", sans-serif; font-size: 12.5px; color: var(--muted); margin-left: 6px; font-weight: 700; }
.rk .bar { height: 6px; background: var(--card2); border-radius: 3px; margin: 6px 0; overflow: hidden; }
.rk .bar span { display: block; height: 100%; background: linear-gradient(90deg, var(--red), var(--gold)); }
.rk .row { display: flex; flex-wrap: wrap; gap: 6px; align-items: center; font-size: 13px; }
.rk .world { font-weight: 900; color: var(--ink); }
.rk .note { font-size: 12.5px; color: #c4c4cc; margin: 6px 0 0; }
.rk .go { font-size: 13px; font-weight: 700; }
@media (min-width: 720px) { .rk { grid-template-columns: 90px 1fr; } .rk .no { font-size: 60px; } }
table.cmp { width: 100%; border-collapse: collapse; font-size: 13.5px; }
table.cmp th, table.cmp td { border-bottom: 1px solid var(--line); padding: 7px 6px; text-align: left; vertical-align: top; }
table.cmp th { color: var(--muted); font-size: 12px; }
/* 再上映 */
.rr { margin: 0 0 22px; }
.rr h2 { margin-top: 10px; }
.rr .sum { margin: 8px 0 12px; }
.rr dl { margin: 0; display: grid; gap: 0; }
.rr dt { font-weight: 900; color: var(--gold); font-size: 13.5px; margin-top: 10px; }
.rr dd { margin: 2px 0 0; font-size: 14.5px; }
.feat { list-style: none; margin: 0; padding: 0; display: grid; gap: 10px; }
@media (min-width: 720px) { .feat { grid-template-columns: repeat(3, 1fr); } }
</style>"""

SCRIPT_MENU = """<script>
(function(){ var b=document.getElementById('mbtn-menu'), m=document.getElementById('mmenu');
  b.addEventListener('click', function(){ m.hidden=!m.hidden; b.setAttribute('aria-expanded', String(!m.hidden)); }); })();
</script>"""


def page(path, title, desc, body, analytics, extra_script=""):
    prefix = "../" * path.count("/")
    menu = (f'<li><a href="{prefix}marvel/">作品一覧（トップ）</a></li>'
            + f'<li><a href="{DOOMSDAY}">ドゥームズデイ予習ガイド</a></li>'
            + "".join(f'<li><a href="{prefix}{p}"{" aria-current=\"page\"" if p == path else ""}>{e(n)}</a></li>' for p, n, _ in PAGES))
    shop = marvel_folder.shop_html("ja").replace('class="mshop"', 'class="mshop"')
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><link rel="apple-touch-icon" href="/icons/movie.png"><link rel="icon" type="image/png" href="/icons/movie.png">{analytics}
<title>{e(title)}｜マーベル映画紹介</title>
<meta name="apple-mobile-web-app-title" content="{e(title)}">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="https://mocchima.com/{path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="マーベル映画紹介">
<meta property="og:title" content="{e(title + "｜マーベル映画紹介")}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="https://mocchima.com/{path}">
<meta property="og:image" content="https://mocchima.com/{path}og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#000000">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap">
{STYLE}
</head>
<body>
<header class="mhead">
  <button type="button" id="mbtn-menu" aria-label="メニュー" aria-expanded="false" aria-controls="mmenu">{marvel_folder.ICON_MENU}</button>
  <a class="mlogo" href="{prefix}marvel/" aria-label="MARVEL（作品一覧へ）">MARVEL</a>
  <span></span>
</header>
<nav class="mmenu" id="mmenu" hidden><ul>{menu}</ul></nav>
<main>
<nav class="crumb"><a href="{prefix}marvel/">マーベル映画紹介</a> ＞ {e(title)}</nav>
{body}
{shop}
</main>
<footer class="foot">個人が運営する非公式のファンサイトです。Marvel Studios、The Walt Disney Company とは関係ありません。映画のポスターや場面写真は使っていません（色と文字で作ったカードです）。 <a href="{prefix}privacy.html">プライバシーポリシー</a></footer>
{SCRIPT_MENU}{extra_script}
</body>
</html>
"""


# ---------------- 年表 ----------------
def display_text(it):
    """本編の行は「『正式な題名』本編」に、EP1〜5 は「第1〜5話」に直して出す"""
    t = it["text"]
    if it["main"] and it["works"]:
        m = re.search(r"EP\s*([\d.〜~・]+)", t)
        name = f"『{title_of(it['works'][0])}』"
        if m:
            eps = m.group(1).replace(".", "・").replace("~", "〜")
            return f"{name} 第{eps}話"
        return f"{name} 本編"
    return t


STATUS = {"check": ("確認中", "check"), "info": ("補足", "")}


def timeline_html(analytics):
    d = load("timeline.json")
    path = "marvel/timeline/"
    prefix = "../../"
    works_seen = []
    eras_html = ""
    for i, era in enumerate(d["eras"]):
        lis = ""
        for it in (x for x in d["items"] if x["era"] == era):
            for w in it["works"]:
                if w not in works_seen:
                    works_seen.append(w)
            tags = "".join(
                f'<a class="kind-{"s" if w in SERIES else "f"}" href="{e(work_href(w, prefix))}">{e(title_of(w))}</a>' for w in it["works"])
            tags += "".join(f'<span class="chip">{e(l)}</span>' for l in it["labels"])
            st = ""
            if it["status"] in STATUS:
                lab, cls = STATUS[it["status"]]
                st = f' <span class="chip {cls}">{lab}</span>'
            note = ""
            # 直した行は、直した後の表記だけを出す（運営者の希望、2026-11-02。元の表記はデータに残す）
            if it["note"] and it["status"] != "fixed":
                note = f'<p class="note">{e(it["note"])}</p>'
            txt = f'<span class="txt">{e(display_text(it))}</span>'
            # 本編の行は、作品名そのものをリンクにして、同じ作品名の札を重ねて出さない（縦を短くするため）
            if it["main"] and len(it["works"]) == 1 and not it["labels"]:
                w = it["works"][0]
                txt = f'<a class="txt" href="{e(work_href(w, prefix))}">{e(display_text(it))}</a>'
                tags = ""
            kinds = " ".join(sorted({"series" if w in SERIES else "film" for w in it["works"]}))
            q = " ".join([it["when"], display_text(it), it["text"], it["note"] if it["status"] != "fixed" else ""] + [title_of(w) for w in it["works"]] + it["labels"]).lower()
            lis += (f'<li class="ev{" main" if it["main"] else ""}" id="{it["id"]}" data-works="{" ".join(it["works"])}" data-kinds="{kinds}" data-q="{e(q)}">'
                    f'{f"<span class=when>{e(it["when"])}</span>" if it["when"] else ""}{txt}{st}'
                    f'<div class="tags">{tags}</div>{note}</li>')
        eras_html += f'<section class="era" id="era{i}" data-era="{e(era)}"><h2>{e(era)}</h2><ol class="tl">{lis}</ol></section>\n'
    era_btns = '<button type="button" data-era="" aria-pressed="true">すべて</button>' + "".join(
        f'<button type="button" data-era="{e(x)}" aria-pressed="false">{e(x)}</button>' for x in d["eras"])
    work_opts = '<option value="">作品で絞り込む（すべて）</option>' + "".join(
        f'<option value="{w}">{e(title_of(w))}{"（ドラマ）" if w in SERIES else ""}</option>' for w in works_seen)
    n = len(d["items"])
    body = f"""<p class="kicker">MCU TIMELINE</p>
<h1>MCU <span class="g">完全年表</span></h1>
<p class="lead">宇宙の誕生から2025年まで、MCU（Earth-616）の出来事と作品を、物語の中の時代順に並べました。作品名を押すと、その作品のガイドへ移動します（ガイドがまだない作品は、ドゥームズデイ予習ガイドの説明へ）。</p>
<p class="meta">全{n}項目・更新日 {e(d["updated"])}　出典：{e(d["source"])}</p>
<div class="tools">
  <input type="search" id="q" placeholder="キーワードで探す（例：ペギー、1995年）" aria-label="キーワードで探す">
  <select id="work" aria-label="作品で絞り込む">{work_opts}</select>
  <div class="seg" id="eras" aria-label="時代で絞り込む">{era_btns}</div>
  <div class="seg" id="kinds" aria-label="種類で絞り込む"><button type="button" data-kind="" aria-pressed="true">映画もドラマも</button><button type="button" data-kind="film" aria-pressed="false">映画</button><button type="button" data-kind="series" aria-pressed="false">ドラマ・配信</button></div>
</div>
<div class="legend"><span><span class="chip ok" style="background:var(--gold)">●</span> 金色の行＝作品の本編</span><span><span class="chip check">確認中</span> 時期などをまだ確かめている行</span><span><span class="chip">補足</span> 説明を足した行</span></div>
<p class="count" id="count"></p>
<div class="eranow" aria-live="polite"><small>ERA</small><span id="eranow">{e(d["eras"][0])}</span></div>
{eras_html}<p class="none" id="none" hidden>見つかりませんでした</p>"""
    script = """<script>
(function(){
  var $=function(s){return document.querySelector(s)}, $$=function(s){return Array.prototype.slice.call(document.querySelectorAll(s))};
  var st={q:'',era:'',kind:'',work:''};
  try{ var p=new URLSearchParams(location.search); st.work=p.get('work')||''; st.q=p.get('q')||''; }catch(e){}
  $('#work').value=st.work; if(!$('#work').value) st.work=''; $('#q').value=st.q;
  function seg(id,key){ $$('#'+id+' button').forEach(function(b){ b.addEventListener('click',function(){
      st[key]=b.dataset[key]; $$('#'+id+' button').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))}); apply(); }); }); }
  seg('eras','era'); seg('kinds','kind');
  $('#q').addEventListener('input',function(){ st.q=this.value.trim().toLowerCase(); apply(); });
  $('#work').addEventListener('change',function(){ st.work=this.value; apply();
    try{ history.replaceState(null,'',st.work?'?work='+st.work:location.pathname); }catch(e){} });
  function apply(){ var hit=0;
    $$('.era').forEach(function(sec){ var any=0;
      sec.querySelectorAll('.ev').forEach(function(li){
        var ok=(!st.era||sec.dataset.era===st.era) && (!st.q||li.dataset.q.indexOf(st.q)>=0)
          && (!st.work||(' '+li.dataset.works+' ').indexOf(' '+st.work+' ')>=0) && (!st.kind||li.dataset.kinds.indexOf(st.kind)>=0);
        li.hidden=!ok; if(ok){any++;hit++;} });
      sec.hidden=!any; });
    $('#none').hidden=hit>0; $('#count').textContent=hit+'件を表示中'; }
  apply();
  if(st.work){ var f=document.querySelector('.ev:not([hidden])'); if(f) setTimeout(function(){ f.scrollIntoView({block:'start'}); },50); }
  var now=$('#eranow');
  function cur(){ var name=null; $$('.era:not([hidden])').forEach(function(s){ if(s.getBoundingClientRect().top<160) name=s.dataset.era; });
    if(!name){ var f=document.querySelector('.era:not([hidden])'); name=f?f.dataset.era:''; } now.textContent=name; }
  window.addEventListener('scroll',cur,{passive:true}); cur();
})();
</script>"""
    return page(path, "MCU完全年表", "MCU（マーベル・シネマティック・ユニバース）の出来事を、宇宙の誕生から2025年まで物語の時代順にまとめた年表。作品・時代・映画／ドラマで絞り込めます。", body, analytics, script)


# ---------------- 興行収入 ----------------
VERIFY = {"確認済み": ("ok", "確認済み"), "一部確認": ("part", "一部確認"), "提供データ": ("data", "確認中（提供データ）")}


def box_office_html(analytics):
    d = load("box_office.json")
    path = "marvel/box-office/"
    prefix = "../../"
    films = sorted(d["films"], key=lambda f: -f["gross"])
    top = films[0]["gross"]
    lis = ""
    for i, f in enumerate(films, 1):
        th = FILM_GUIDES.get(f["slug"], {}).get("theme") or marvel_folder.DOOMSDAY_THEME
        cls, lab = VERIFY.get(f["verify"], ("data", f["verify"]))
        style = f'--p-main:{th["main"]};--p-deep:{th["deep"]};--p-accent:{th["accent"]}'
        go = (f'<a class="go" href="{prefix}{f["slug"]}/">作品ガイドを見る ›</a>' if has_guide(f["slug"])
              else f'<a class="go" href="{DOOMSDAY}#{f["slug"]}">予習ガイドで見る ›</a>')
        lis += (f'<li class="rk"><div class="no" aria-label="マーベル作品の中で{i}位"><div><small>マーベル内</small>{i}</div></div><div>'
                f'<div class="poster" style="{style}"><b>{e(f["title_ja"])}</b><i>{e(f["title_en"])} ・ {f["year"]}年</i></div>'
                f'<p class="gross">${f["gross"]:,}<small>{yen_like(f["gross"])}</small></p>'
                f'<div class="bar"><span style="width:{f["gross"] / top * 100:.1f}%"></span></div>'
                f'<div class="row"><span class="world">世界歴代 {f["world_rank"]}位</span><span class="chip {cls}">{e(lab)}</span>'
                + ('<span class="chip red">再上映を含む</span>' if f["rerelease"] else "") + f' {go}</div>'
                f'<p class="note">{e(f["note"])}</p></div></li>')
    srcs = "".join(f'<li><a href="{e(s["url"])}" target="_blank" rel="noopener">{e(s["name"])}</a></li>' for s in d["sources"])
    body = f"""<p class="kicker">BOX OFFICE</p>
<h1>マーベル作品 <span class="g">興行収入ランキング</span></h1>
<p class="lead">世界の映画の歴代ランキング（すべての映画の中の順位）に入っているマーベル作品を、興行収入の多い順に並べました。大きな数字は<strong>マーベル作品の中での順位</strong>、「世界歴代○位」は<strong>すべての映画の中での順位</strong>です。</p>
<p class="meta">数字の時点：{e(d["as_of"])}・当サイトの確認日：{e(d["checked"])}<br>集計の基準：{e(d["basis"])}</p>
<ol class="ranks">{lis}</ol>
<h2>確認の状態について</h2>
<div class="box"><p style="margin:0 0 8px"><span class="chip ok">確認済み</span> 公開されている数字と一致することを確かめたもの　<span class="chip part">一部確認</span> 順位などは報道で確かめたが、細かい金額はまだのもの　<span class="chip data">確認中（提供データ）</span> 提供されたデータのままで、まだ確かめていないもの</p>
<p class="src" style="margin:0">{e(d["source_note"])} 上映中の作品は、数字がこれからも増えます。</p></div>
<h2>出典</h2>
<ul class="src">{srcs}</ul>"""
    return page(path, "興行収入ランキング", "マーベル作品の世界興行収入ランキング。世界の歴代順位と、マーベル作品の中での順位を、確認の状態と出典つきでまとめました。", body, analytics)


# ---------------- 再上映 ----------------
def rerelease_html(analytics):
    d = load("rerelease.json")
    path = "marvel/rerelease/"
    prefix = "../../"
    secs = ""
    for it in d["items"]:
        badge = f'<span class="chip {"ok" if it["status"] == "confirmed" else "check"}">{e(it["status_label"])}</span>'
        facts = "".join(f"<dt>{e(k)}</dt><dd>{e(v)}</dd>" for k, v in it["facts"])
        srcs = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a></li>' for n, u in it["sources"])
        anchor = "#" + it["guide_anchor"] if it.get("guide_anchor") else ""
        label = it.get("guide_label") or f'『{title_of(it["slug"])}』の作品ガイドを見る ›'
        guide = (f'<p style="margin:12px 0 0"><a href="{prefix}{it["slug"]}/{anchor}">{e(label)}</a></p>' if has_guide(it["slug"])
                 else f'<p style="margin:12px 0 0"><a href="{DOOMSDAY}#{it["slug"]}">ドゥームズデイ予習ガイドで作品の説明を見る ›</a></p>')
        secs += (f'<section class="rr" id="{it["id"]}"><h2>{e(it["title"])}</h2><div class="box">{badge}<p class="sum">{e(it["summary"])}</p>'
                 f'<dl>{facts}</dl>{guide}</div><p class="src" style="margin:10px 0 2px">出典</p><ul class="src">{srcs}</ul></section>')
    body = f"""<p class="kicker">RE-RELEASE</p>
<h1>マーベル作品 <span class="g">再上映情報</span></h1>
<p class="lead">映画館でもう一度観られる（観られた）マーベル作品の情報です。<strong>公式に決まったこと</strong>と<strong>報道だけの段階のこと</strong>を分けて書いています。</p>
<p class="meta">当サイトの確認日：{e(d["checked"])}。日程や上映館は変わることがあります。お出かけの前に、映画館や配給会社の公式サイトを確かめてください。</p>
<div class="box"><table class="cmp"><tr><th>作品</th><th>いまの状況</th><th>日本</th></tr>
<tr><td><a href="#endgame">エンドゲーム：アンコール</a></td><td><span class="chip ok">公式決定・上映済み</span></td><td>2026年9月23日〜10月8日（一部は10月15日まで）</td></tr>
<tr><td><a href="#brand-new-day">ブランド・ニュー・デイ（追加映像つき）</a></td><td><span class="chip check">報道段階</span></td><td>未定</td></tr></table></div>
{secs}"""
    return page(path, "再上映情報", "『アベンジャーズ／エンドゲーム：アンコール』と『スパイダーマン：ブランド・ニュー・デイ』の再上映の情報。公式発表と報道を分けて、出典つきでまとめました。", body, analytics)


def feature_html(prefix):
    """マーベル映画紹介のトップに出す「特集」の枠"""
    lis = "".join(f'<li><a class="mfeat" href="{prefix}{p}"><b>{e(n)}</b><span>{e(dsc)}</span></a></li>' for p, n, dsc in PAGES)
    return f'<section class="mfeats"><h2>特集</h2><ul>{lis}</ul></section>'


def timeline_works():
    return {w for it in load("timeline.json")["items"] for w in it["works"]}


def build_all(write, analytics):
    for p, fn in zip([x[0] for x in PAGES], [timeline_html, box_office_html, rerelease_html]):
        os.makedirs(os.path.join(ROOT, p), exist_ok=True)
        write(p + "index.html", fn(analytics))
    return [x[0] for x in PAGES]
