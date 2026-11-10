"""MCU の作品ガイド（1作品＝1つの独立したサイト）を書き出す。

使い方: python3 src/mcu/build.py   （そのあと共有画像を作るなら node src/mcu/render.js）
出力: /<slug>/index.html（日本語）、/<slug>/en/index.html（英語）、/<slug>/assets/、/<slug>/og.png、/<slug>/sitemap.xml
データ: films.py（文章）、relations.py（相関図）、titles.py（作品の基本情報）
"""
import html
import json
import os
import re
import shutil
import sys
from urllib.parse import quote

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(SRC))
sys.path.insert(0, SRC)

from films import FILM_GUIDES  # noqa: E402
from relations import RELATION_MAPS, image_for  # noqa: E402
from titles import TITLES  # noqa: E402
from opinions import OPINIONS  # noqa: E402
import relmap_build  # noqa: E402

BASE_URL = "https://mocchima.com/"
GA_MEASUREMENT_ID = "G-KDFL8GPPRZ"
ADSENSE_TAG = '\n<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8047459455202561" crossorigin="anonymous"></script>'
PRIVACY_URL = BASE_URL + "privacy.html"

# 広告（運営者の登録済みID。CLAUDE.md 参照）
AMAZON_TAG = "doomsdayguide-22"
AMAZON_TAG_US = "doomsdaygui08-20"
RAKUTEN_TOP = "https://af.moshimo.com/af/c/click?a_id=5875908&p_id=54&pc_id=54&pl_id=616"

e = html.escape

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Zen+Kaku+Gothic+New:wght@400;500;700;900&family=JetBrains+Mono:wght@500&display=swap">')

TEXT = {
    "ja": dict(
        home="もっちぃま", guide="完全ガイド", menu="作品ガイド", other_lang="English",
        tagline="映画だけでは分かりにくいところを、あらすじ・相関図・用語でやさしく解説します。",
        year="公開", runtime="上映時間", era="作中の時代",
        toc="目次", toc_short=dict(take="感想", before="観る前に", map="相関図", story="あらすじ", glossary="用語集", confusing="Q&A", points="小ネタ", ending="おまけ映像", next="次に観る"), s_before="観る前に知っておくと分かりやすいこと", s_map="キャラクター相関図",
        s_story="あらすじ", s_glossary="用語集", s_confusing="ここが分かりにくい！Q&A", s_points="見逃しやすいポイント・小ネタ",
        s_ending="ラストとおまけ映像", s_next="次に観るとよい作品",
        nospoil="ネタバレなし", spoil="ネタバレあり",
        story_open="あらすじを読む（結末までのネタバレを含みます）",
        scenes_link="シーンごとの詳しいあらすじを読む", scenes_title="『{title}』詳しいあらすじ（シーンごと）",
        scenes_lead="映画を最初から最後まで、場面ごとに文章でたどります。これを読めば、話の流れがすべて分かります。",
        scenes_warn="※結末まで、すべてのネタバレを含みます。", scenes_back="完全ガイドに戻る", scenes_desc="『{title}』のあらすじを、最初の場面からエンドクレジットの後まで、シーンごとにくわしく文章で解説します（ネタバレあり）。",
        confusing_note="結末に関わる内容を含みます。",
        post="エンドクレジットの後のおまけ映像",
        shop="この作品をもっと楽しむ", common_shop="マーベル映画をもっと楽しむ", list="マーベル映画紹介のほかのページ", folder="マーベル映画紹介", folder_path="marvel/",
        desc_fmt="『{title}』を映画だけでは分かりにくい人向けに解説。ネタバレなしの観る前のポイント、顔アイコンつき相関図、章ごとのあらすじ、用語集、分かりにくい場面のQ&A、おまけ映像まで。",
        title_fmt="『{title}』完全ガイド｜あらすじ・相関図・用語をやさしく解説",
        site_fmt="{title} 完全ガイド",
    ),
    "en": dict(
        home="Mocchima", guide="Complete Guide", menu="Film guide", other_lang="日本語",
        tagline="The parts that are hard to follow from the film alone, explained with a story summary, a character map and key terms.",
        year="Released", runtime="Runtime", era="Set in",
        toc="Contents", toc_short=dict(take="My take", before="Before you watch", map="Character map", story="Story", glossary="Key terms", confusing="Q&A", points="Details", ending="Post-credits", next="Watch next"), s_before="Good to know before watching", s_map="Character map",
        s_story="Story", s_glossary="Key terms", s_confusing="Confusing parts, explained", s_points="Easy-to-miss details",
        s_ending="The ending and post-credits", s_next="What to watch next",
        nospoil="No spoilers", spoil="Spoilers",
        story_open="Read the story (spoilers up to the ending)",
        scenes_link="Read the detailed scene-by-scene story", scenes_title="{title}: The Full Story, Scene by Scene",
        scenes_lead="The whole film, start to finish, told scene by scene in words. Read this and you'll know everything that happens.",
        scenes_warn="Contains every spoiler, up to the ending.", scenes_back="Back to the complete guide", scenes_desc="The full story of {title}, from the first scene to after the credits, told scene by scene (spoilers).",
        confusing_note="Contains spoilers about the ending.",
        post="After the end credits",
        shop="More from this film", common_shop="More Marvel fun", list="More Marvel movie guides", folder="Marvel Movie Guides", folder_path="marvel/en/",
        desc_fmt="A guide to {title} for anyone who finds it hard to follow: spoiler-free tips, a character map with face icons, a chapter-by-chapter story, key terms, the confusing parts explained, and the post-credits scene.",
        title_fmt="{title} Complete Guide: Story, Character Map and Key Terms Explained",
        site_fmt="{title} Complete Guide",
    ),
}


def title_rec(slug, lang):
    """作品の基本情報を、その言語のものにして返す"""
    t = TITLES[slug]
    if lang == "en":
        return dict(slug=slug, title=t["title_en"], year=t["year"], era=t["era_en"], post=t["post_en"])
    return dict(slug=slug, title=t["title"], year=t["year"], era=t["era"], post=t["post"])


def L(item, lang, i_ja, i_en):
    return item[i_en] if lang == "en" else item[i_ja]


def amazon_url(key, lang):
    path = key if key.startswith("/") else f"/s?k={quote(key)}"
    sep = "&" if "?" in path else "?"
    if lang == "en":
        return f"https://www.amazon.com{path}{sep}tag={quote(AMAZON_TAG_US)}"
    return f"https://www.amazon.co.jp{path}{sep}tag={quote(AMAZON_TAG)}"


def rakuten_url(keyword):
    inner = f"https://search.rakuten.co.jp/search/mall/{quote(keyword)}/"
    return f"{RAKUTEN_TOP}&url={quote(inner, safe='')}"


# 全作品ガイドで共通に出すおすすめ商品（運営者の希望で広告を増やした、2026-11-02）
# (日本語の表示名, 日本語の検索キーワード, 英語の表示名, 英語の検索キーワード)
COMMON_PICKS = [
    ("マーベル公式の年表の本（英語）", "Marvel Cinematic Universe An Official Timeline", "The official MCU timeline book", "Marvel Cinematic Universe An Official Timeline"),
    ("Fire TV Stick（Disney+をテレビで）", "Fire TV Stick", "Fire TV Stick (Disney+ on your TV)", "Fire TV Stick"),
    ("マーベルのレゴ", "レゴ マーベル", "Marvel LEGO", "LEGO Marvel"),
    ("マーベルのTシャツ", "マーベル Tシャツ", "Marvel T-shirts", "Marvel t-shirt"),
    ("アベンジャーズのフィギュア", "アベンジャーズ フィギュア", "Avengers figures", "Avengers Marvel Legends figure"),
    ("アメコミ（日本語版）", "マーベル アメコミ 邦訳", "Marvel comics", "Marvel comics graphic novel"),
]


def _timeline_works():
    p = os.path.join(os.path.dirname(SRC), "marvel_data", "timeline.json")
    with open(p, encoding="utf-8") as f:
        return {w for it in json.load(f)["items"] for w in it["works"]}


TIMELINE_WORKS = _timeline_works()


def _box_office():
    p = os.path.join(os.path.dirname(SRC), "marvel_data", "box_office.json")
    with open(p, encoding="utf-8") as f:
        d = json.load(f)
    films = sorted(d["films"], key=lambda x: -x["gross"])
    return d, {x["slug"]: (i, x) for i, x in enumerate(films, 1)}


BOX, BOX_RANK = _box_office()


def box_office_badge(slug, lang, top):
    """作品ガイドの一番上に出す「世界興行収入 歴代○位」の派手な帯（運営者の希望、2026-11-02）。
    数字は src/marvel_data/box_office.json。確かめていない数字には「確認中」と出す"""
    if slug not in BOX_RANK:
        return ""
    mrank, f = BOX_RANK[slug]
    ja = lang != "en"
    gross = f"${f['gross']:,}"
    if ja:
        oku, man = divmod(f["gross"] // 10000, 10000)
        sub = f"約{oku}億{man:,}万ドル・マーベル作品で{mrank}位"
        state = {"確認済み": "確認済み", "一部確認": "金額は確認中"}.get(f["verify"], "数字は確認中")
        when = f"{BOX['as_of']}時点・{state}" + ("・再上映を含む" if f["rerelease"] else "")
        head, label = "WORLD BOX OFFICE", f"世界興行収入 歴代<b>{f['world_rank']}</b>位"
        more = f'<a href="{top}marvel/box-office/">ランキングを見る ›</a>'
    else:
        sub = f"#{mrank} among Marvel films"
        state = {"確認済み": "verified", "一部確認": "amount being verified"}.get(f["verify"], "figures being verified")
        when = f"As of {BOX['as_of']} · {state}" + (" · incl. re-release" if f["rerelease"] else "")
        head, label, more = "WORLD BOX OFFICE", f"<b>#{f['world_rank']}</b> all-time worldwide", ""
    return (f'\n  <div class="bo-badge"><span class="bo-head">{head}</span><span class="bo-rank">{label}</span>'
            f'<span class="bo-gross">{gross}</span><span class="bo-sub">{e(sub)}</span>'
            f'<span class="bo-when">{e(when)} {more}</span></div>')


box_badge = box_office_badge


def timeline_link(slug, lang, top):
    """MCU完全年表（/marvel/timeline/、日本語だけ）でこの作品の出来事を見るリンク"""
    if lang != "ja" or slug not in TIMELINE_WORKS:
        return ""
    return (f'\n  <p style="margin:12px 0 0"><a class="btn" href="{top}marvel/timeline/?work={slug}">'
            f'MCU完全年表でこの作品の時代を見る ›</a></p>')


def common_panel(lang):
    """どの作品ガイドにも出す、マーベル全体のおすすめ商品（PR）"""
    t = TEXT[lang]
    btns = []
    for ja, kw, en, kw_en in COMMON_PICKS:
        btns.append(f'<a class="btn ad" href="{e(amazon_url(kw_en if lang == "en" else kw, lang))}" target="_blank" rel="sponsored noopener">{e(en if lang == "en" else ja)}</a>')
    if lang == "ja" and RAKUTEN_TOP:
        btns.append(f'<a class="btn ad" href="{e(rakuten_url("マーベル グッズ"))}" target="_blank" rel="sponsored noopener">楽天でマーベルのグッズを探す</a>')
    return f'<aside class="panel"><h2>{e(t["common_shop"])} <span class="pr">PR</span></h2><div class="btns">{"".join(btns)}</div></aside>'


def shop_panel(g, lang):
    """作品に関連する商品（PR）。Amazon と、日本語版は楽天も"""
    t = TEXT[lang]
    btns = []
    for label, kw, label_en in g.get("shop", []):
        btns.append(f'<a class="btn ad" href="{e(amazon_url(label_en if lang == "en" else kw, lang))}" target="_blank" rel="sponsored noopener">{e(label_en if lang == "en" else label)}</a>')
        if lang == "ja" and RAKUTEN_TOP:
            btns.append(f'<a class="btn ad" href="{e(rakuten_url(kw))}" target="_blank" rel="sponsored noopener">{e(label)}（楽天）</a>')
    if not btns:
        return ""
    return f'<aside class="panel"><h2>{e(t["shop"])} <span class="pr">PR</span></h2><div class="btns">{"".join(btns)}</div></aside>'


def head(slug, title, desc, lang, prefix, schema, site_name):
    url = BASE_URL + (f"{slug}/en/" if lang == "en" else f"{slug}/")
    og = BASE_URL + (f"{slug}/en/og.png" if lang == "en" else f"{slug}/og.png")
    analytics = (f'\n<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>\n'
                 f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_MEASUREMENT_ID}');</script>")
    analytics += ADSENSE_TAG  # Google アドセンス（2026-11-03）
    schema_html = '\n<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace("</", "<\\/") + "</script>"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><link rel="apple-touch-icon" href="/icons/movie.png"><link rel="icon" type="image/png" href="/icons/movie.png">{analytics}
<title>{e(title)}</title>
<meta name="apple-mobile-web-app-title" content="{e(site_name)}">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ja" href="{BASE_URL}{slug}/">
<link rel="alternate" hreflang="en" href="{BASE_URL}{slug}/en/">
<link rel="alternate" hreflang="x-default" href="{BASE_URL}{slug}/">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{e(site_name)}">
<meta property="og:locale" content="{"en_US" if lang == "en" else "ja_JP"}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">{schema_html}
{FONTS}
<link rel="stylesheet" href="{prefix}assets/site.css">
</head>
<body>
<div class="wrap">
"""




def special_section(g, lang, t):
    """作品ごとの特別な項目（例：エンドゲームのアンコール版）。films.py の special"""
    sp = g.get("special")
    if not sp:
        return ""
    en = lang == "en"
    cards = "".join(f'<div class="fg-card"><h3>{e(x[2] if en else x[0])}</h3><p>{e(x[3] if en else x[1])}</p></div>' for x in sp["items"])
    srcs = "".join(f'<li><a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a></li>' for n, u in sp["sources"])
    return (f'<section class="fg-sec" id="{sp["id"]}"><h2>{e(sp["title_en"] if en else sp["title"])}<span class="tag-warn">{e(t["spoil"])}</span></h2>\n'
            f'  <p>{e(sp["lead_en"] if en else sp["lead"])}</p>\n  <div class="fg-cards">{cards}</div>\n'
            f'  <p class="src-title">{"Sources" if en else "出典"}</p><ul class="src-list">{srcs}</ul>\n</section>\n\n')


def contents_box(items, lang):
    """ページの最初に出す番号つきの目次（運営者の希望、2026-11-02）。items: [(リンク先, 見出し, [小見出し...])]"""
    lis = "".join(
        f'<li><a href="{h}"><span class="cb-no">{i:02d}</span><span class="cb-t">{e(label)}</span></a>'
        + (f'<ul>{"".join(f"<li>{e(x)}</li>" for x in subs)}</ul>' if subs else "") + "</li>"
        for i, (h, label, subs) in enumerate(items, 1))
    return f'<nav class="contents-box" aria-label="{"Contents" if lang == "en" else "目次"}"><p class="cb-title">{"Contents" if lang == "en" else "目次"}</p><ol>{lis}</ol></nav>\n'


def footer(lang, top):
    if lang == "en":
        return f"""<footer>
<p>This site contains affiliate links (ads).</p>
<p>As an Amazon Associate, this site earns from qualifying purchases.</p>
<p>For how this site uses analytics (Google Analytics) and ads, see the <a href="{PRIVACY_URL}#en">privacy policy</a>. About the operator and contact: <a href="https://mocchima.com/about.html">About (Japanese)</a>.</p>
<p>This is an unofficial fan site run by an individual. It is not affiliated with Marvel Studios, The Walt Disney Company, Sony Pictures or 20th Century Studios. Titles and character names are trademarks of their respective owners.</p>
<p><a href="{top}marvel/en/">Marvel Movie Guides (all titles)</a></p>
</footer>
</div>
"""
    return f"""<footer>
<p>※当サイトはアフィリエイト広告（PR）を利用しています。</p>
<p>Amazonのアソシエイトとして、当サイトは適格販売により収入を得ています。</p>
<p>アクセス解析（Googleアナリティクス）と広告の仕組みについては<a href="{PRIVACY_URL}">プライバシーポリシー</a>をご覧ください。 <a href="https://mocchima.com/about.html">運営者情報・お問い合わせ</a></p>
<p>当サイトは個人が運営する非公式ファンサイトです。Marvel Studios、The Walt Disney Company、Sony Pictures、20th Century Studios とは関係ありません。作品名・キャラクター名は各権利者の商標です。</p>
<p><a href="{top}marvel/">マーベル映画紹介（作品一覧）</a></p>
</footer>
</div>
"""


def take_section(slug, lang):
    """運営者のひとこと（感想・見解）。あらすじ（事実）と分けて出す"""
    o = OPINIONS.get(slug)
    if not o:
        return ""
    h = "My take" if lang == "en" else "運営者のひとこと"
    sub = "Opinion" if lang == "en" else "感想・見解"
    return (f'<section class="fg-sec" id="take"><h2>{e(h)}<span class="tag-ok">{e(sub)}</span></h2>'
            f'<div class="fg-card fg-take"><p>{e(o[1] if lang == "en" else o[0])}</p></div></section>')


def build_page(slug, lang):
    t = TEXT[lang]
    g = FILM_GUIDES[slug]
    prefix = "../" if lang == "en" else ""
    tr = title_rec(slug, lang)
    title = tr["title"]
    path = f"{slug}/en/" if lang == "en" else f"{slug}/"
    top = "../../" if lang == "en" else "../"
    h1 = f"{title}" if lang == "en" else f"『{title}』"

    before = "".join(f'<div class="fg-card"><h3>{e(h)}</h3><p>{e(b)}</p></div>' for h, b in (g["before_en"] if lang == "en" else g["before"]))
    glossary = "".join(f"<div><dt>{e(L(x, lang, 0, 2))}</dt><dd>{e(L(x, lang, 1, 3))}</dd></div>" for x in g["glossary"])
    story = "".join(f'<section class="fg-chapter"><h3>{e(L(x, lang, 0, 2))}</h3>{paras(L(x, lang, 1, 3))}</section>' for x in g["story"])
    confusing = "".join(f'<details class="fg-qa"><summary>{e(L(x, lang, 0, 2))}</summary><p>{e(L(x, lang, 1, 3))}</p></details>' for x in g["confusing"])
    points = "".join(f'<div class="fg-card"><h3>{e(L(x, lang, 0, 2))}</h3><p>{e(L(x, lang, 1, 3))}</p></div>' for x in g["points"])
    nexts = "".join(
        (f'<li><a href="{top}{s}/{"en/" if lang == "en" else ""}">' if s in FILM_GUIDES else '<li><div class="fg-next-item">')
        + f'<b>{e(title_rec(s, lang)["title"])}</b><small>{e(why_en if lang == "en" else why)}</small>'
        + ('</a></li>' if s in FILM_GUIDES else '</div></li>')
        for s, why, why_en in g["next"] if s in TITLES)

    has_map = slug in RELATION_MAPS
    map_html, map_scripts, actors = relmap_build.map_section(slug, lang, e, prefix) if has_map else ("", "", [])
    sections = [("before", t["s_before"])] + ([("take", "My take" if lang == "en" else "運営者のひとこと")] if slug in OPINIONS else []) + ([("map", t["s_map"])] if has_map else []) + [
        ("story", t["s_story"]), ("glossary", t["s_glossary"]), ("confusing", t["s_confusing"]), ("points", t["s_points"]),
        ("ending", t["s_ending"])] + ([(g["special"]["id"], g["special"]["title_en" if lang == "en" else "title"])] if g.get("special") else []) + [
        ("next", t["s_next"])]
    short = dict(t["toc_short"])
    if g.get("special"):
        short[g["special"]["id"]] = g["special"]["toc_en" if lang == "en" else "toc"]
    toc = (f'<ul><li><span class="toc-label">{e(t["toc"])}</span></li>'
           + "".join(f'<li><a href="#{k}">{e(short.get(k, v))}</a></li>' for k, v in sections) + "</ul>")
    facts = [(t["year"], tr["year"]), (t["runtime"], g["runtime_en"] if lang == "en" else g["runtime"]),
             (t["era"], tr["era"])]
    facts_html = "".join(f"<div><dt>{e(k)}</dt><dd>{e(str(v))}</dd></div>" for k, v in facts)
    shop = shop_panel(g, lang)

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Article", "headline": t["title_fmt"].format(title=title), "description": t["desc_fmt"].format(title=title),
             "inLanguage": lang, "dateModified": g["updated"], "datePublished": g["updated"],
             "about": {"@type": "Movie", "name": title, "datePublished": tr["year"], "actor": [{"@type": "Person", "name": a} for a in actors[:6]]}},
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": L(x, lang, 0, 2),
                                                 "acceptedAnswer": {"@type": "Answer", "text": L(x, lang, 1, 3)}} for x in g["confusing"]]},
        ],
    }
    th = g.get("theme")
    theme_css = (f"<style>:root{{--green:{th['deep']};--navy:{th['main']};--gold-bright:{th['accent']};--green-soft:{th['soft']};"
                 f"--navy-soft:{th['soft']};--gold:{th['accent']};--gold-ink:{th['main']};--link:{th['main']};}}</style>\n") if th else ""
    return head(slug, t["title_fmt"].format(title=title), t["desc_fmt"].format(title=title), lang, prefix, schema,
                t["site_fmt"].format(title=title)) + theme_css + f"""
<nav class="crumb"><a href="{top}{t['folder_path']}">{e(t['folder'])}</a> ＞ {e(title)}<a class="lang-switch" href="{'../' if lang == 'en' else 'en/'}" hreflang="{'ja' if lang == 'en' else 'en'}">{e(t['other_lang'])}</a></nav>
<header class="fg-hero">
  <p class="eyebrow">{e(t['menu'])} · {e(tr['year'])}</p>
  <h1>{e(h1)}<small>{e(t['guide'])}</small></h1>
  <p class="lead">{e(t['tagline'])}</p>
  <dl class="fg-facts">{facts_html}</dl>{box_badge(slug, lang, top)}
</header>
<nav class="site-toc" aria-label="{e(t['toc'])}">{toc}</nav>
{contents_box([("#" + k, v, []) for k, v in sections], lang)}
<section class="fg-sec" id="before"><h2>{e(t['s_before'])}<span class="tag-ok">{e(t['nospoil'])}</span></h2>
  <div class="fg-cards">{before}</div>
</section>
""" + take_section(slug, lang) + (f"""
<section class="fg-sec" id="map"><h2>{e(t['s_map'])}<span class="tag-warn">{e(t['spoil'])}</span></h2>
  {map_html}
</section>
""" if has_map else "") + f"""
<section class="fg-sec" id="story"><h2>{e(t['s_story'])}<span class="tag-warn">{e(t['spoil'])}</span></h2>
  <details class="fg-spoiler"><summary>{e(t['story_open'])}</summary>{story}</details>
  {f'<p class="fg-more"><a class="btn primary" href="story/">{e(t["scenes_link"] + watch_along(g, lang))}</a></p>' if g.get("scenes") else ""}
</section>

{shop}

<section class="fg-sec" id="glossary"><h2>{e(t['s_glossary'])}</h2>
  <dl class="fg-glossary">{glossary}</dl>
</section>

<section class="fg-sec" id="confusing"><h2>{e(t['s_confusing'])}<span class="tag-warn">{e(t['spoil'])}</span></h2>
  <p class="fg-note">{e(t['confusing_note'])}</p>
  {confusing}
</section>

<section class="fg-sec" id="points"><h2>{e(t['s_points'])}</h2>
  <div class="fg-cards">{points}</div>
</section>

<section class="fg-sec" id="ending"><h2>{e(t['s_ending'])}<span class="tag-warn">{e(t['spoil'])}</span></h2>
  <details class="fg-spoiler"><summary>{e(t['post'])}</summary><p>{e(tr['post'])}</p></details>
</section>

{special_section(g, lang, t)}<section class="fg-sec" id="next"><h2>{e(t['s_next'])}</h2>
  <ul class="fg-next">{nexts}</ul>{timeline_link(slug, lang, top)}
</section>

{common_panel(lang)}
<section class="panel">
  <div class="btns"><a class="btn primary" href="{top}{t['folder_path']}">{e(t['list'])}</a></div>
</section>
{map_scripts}""" + footer(lang, top) + "</body>\n</html>\n"


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def paras(text):
    """改行（\n）で段落を分ける（長いあらすじを読みやすくするため。2026-11-07）"""
    return "".join(f"<p>{e(x)}</p>" for x in text.split("\n") if x.strip())


def watch_along(g, lang):
    """「ネタバレなし解説」がある作品だけ「（映画を観ながら読める）」と付ける（運営者の希望、2026-11-07）"""
    if not (g.get("scene_numbers") or any(len(x) > 2 and x[2] for c in g.get("scenes", []) for x in c[1])):
        return ""
    drama = "話" in g.get("runtime", "")
    if lang == "en":
        return " (read along while you watch)"
    return "（ドラマを観ながら読める）" if drama else "（映画を観ながら読める）"


def scene_html(ch, k, sc, lang, head="", numbered=False):
    """場面1つ分。sc = (見出し, 本文[, ネタバレなし解説])。解説がある作品は場面に番号（第○章-○）を付ける"""
    sh, sp = sc[0], sc[1]
    note = sc[2] if len(sc) > 2 else ""
    m = re.search(r"(?:第|Episode |Part )(\d+)", head)  # 番号は見出しの「第○話」に合わせる（なければ番号なし）
    no = f'<span class="sc-no">{m.group(1)}-{k}</span>' if m and (note or numbered) else ""
    if not note:
        return f'<div class="sc-scene" id="s{ch}-{k}"><h3>{no}{e(sh)}</h3>{paras(sp)}</div>' if no else f'<div class="sc-scene"><h3>{e(sh)}</h3>{paras(sp)}</div>'
    label = "Spoiler-free note" if lang == "en" else "ネタバレなし解説"
    return (f'<div class="sc-scene sc-has-note" id="s{ch}-{k}"><h3>{no}{e(sh)}</h3>{paras(sp)}'
            f'<aside class="sc-note"><p class="sc-note-label">{label}</p>{paras(note)}</aside></div>')


def build_scenes_page(slug, lang):
    """シーンごとの詳しいあらすじのページ（/<slug>/story/ と /<slug>/en/story/）"""
    t = TEXT[lang]
    g = FILM_GUIDES[slug]
    tr = title_rec(slug, lang)
    title = tr["title"]
    prefix = "../../" if lang == "en" else "../"
    top = "../../../" if lang == "en" else "../../"
    path = f"{slug}/en/story/" if lang == "en" else f"{slug}/story/"
    chapters = [(c[2], c[3]) if lang == "en" else (c[0], c[1]) for c in g["scenes"]]
    has_note = any(len(sc) > 2 and sc[2] for _, scs in chapters for sc in scs)
    numbered = has_note or g.get("scene_numbers", False)
    toc = (f'<ul><li><span class="toc-label">{e(t["toc"])}</span></li>'
           + "".join(f'<li><a href="#c{i}">{e(h.split(" ", 1)[0] if lang == "ja" else h.split(":")[0])}</a></li>' for i, (h, _) in enumerate(chapters, 1)) + "</ul>")
    mid = (len(chapters) + 1) // 2  # 真ん中の章の後に、この作品の商品（PR）を1つはさむ
    fold = g.get("episodes_fold")  # 話ごとに押して開く形（運営者の希望、2026-11-02。ビジョンクエストなど）
    if fold:
        body = "".join(
            f'<details class="fg-sec sc-chapter sc-fold" id="c{i}"><summary><h2>{e(h)}</h2></summary>'
            + "".join(scene_html(i, k, sc, lang, h, numbered) for k, sc in enumerate(scenes, 1)) + "</details>\n"
            for i, (h, scenes) in enumerate(chapters, 1))
        for j, u in enumerate(g.get("upcoming", []), len(chapters) + 1):
            ut, ud = (u[1], u[3]) if lang == "en" else (u[0], u[2])
            body += (f'<details class="fg-sec sc-chapter sc-fold sc-upcoming" id="c{j}"><summary><h2>{e(ut)}'
                     f'<span class="tag-warn">{"Not yet released" if lang == "en" else "未公開"}</span></h2></summary>'
                     f'<p class="sc-soon">{e(ud)}</p></details>\n')
        body += shop_panel(g, lang) + "\n"
        body += ("<script>(function(){function o(){var d=document.getElementById(location.hash.slice(1));"
                 "if(d&&d.tagName==='DETAILS'){d.open=true;}}window.addEventListener('hashchange',o);o();})();</script>\n")
    else:
      body = "".join(
        f'<section class="fg-sec sc-chapter" id="c{i}"><h2>{e(h)}</h2>'
        + "".join(scene_html(i, k, sc, lang, h, numbered) for k, sc in enumerate(scenes, 1)) + "</section>\n"
        + (shop_panel(g, lang) + "\n" if i == mid else "")
        for i, (h, scenes) in enumerate(chapters, 1))
    note_lead = (f'<p class="lead"><strong>{e(watch_along(g, lang).strip(" ()（）").capitalize() if lang == "en" else watch_along(g, lang).strip(" ()（）"))}</strong></p><p class="lead sc-note-lead">{"The yellow “spoiler-free notes” give background you can know at that point (who someone is, why they act, links to earlier films, terms), with nothing about what comes later. Watch alongside and match the scene numbers." if lang == "en" else "黄色い枠「ネタバレなし解説」は、その場面までに分かることだけで書いた補足です（この人は誰か、なぜこうしているのか、前の作品とのつながり、言葉の意味）。先の展開は書いていません。作品を観ながら、場面の番号で照らし合わせてください。"}</p>' if has_note else (f'<p class="lead"><strong>{e(watch_along(g, lang).strip(" ()（）").capitalize() if lang == "en" else watch_along(g, lang).strip(" ()（）"))}</strong></p>' if numbered else ""))
    page_title = t["scenes_title"].format(title=title)
    desc = t["scenes_desc"].format(title=title)
    th = g.get("theme")
    theme_css = (f"<style>:root{{--green:{th['deep']};--navy:{th['main']};--gold-bright:{th['accent']};--green-soft:{th['soft']};"
                 f"--navy-soft:{th['soft']};--gold:{th['accent']};--gold-ink:{th['main']};--link:{th['main']};}}"
                 ".sc-scene{border-left:3px solid var(--gold-bright);padding:2px 0 2px 14px;margin:14px 0}.sc-scene h3{margin:0 0 4px;font-size:16px;color:var(--navy)}.sc-scene p{margin:0;line-height:1.95}.sc-scene p+p{margin-top:.7em}.sc-no{display:inline-block;min-width:2.6em;margin-right:.5em;padding:1px 6px;border-radius:6px;background:var(--navy);color:#fff;font-size:12px;text-align:center;vertical-align:2px}.sc-note{margin:10px 0 2px;padding:10px 12px;border-radius:10px;background:#fff8e1;border:1px solid #f0d58a;color:#3d3420}.sc-note p{font-size:14px;line-height:1.8}.sc-note .sc-note-label{margin:0 0 4px;font-size:12px;font-weight:700;color:#8a6a10}@media (prefers-color-scheme: dark){.sc-note{background:#2b2617;border-color:#6b5a26;color:#efe6cc}.sc-note .sc-note-label{color:#e8c766}}"
                 "</style>\n") if th else ""
    schema = {"@context": "https://schema.org", "@type": "Article", "headline": page_title, "description": desc, "inLanguage": lang,
              "dateModified": g["updated"], "about": {"@type": "Movie", "name": title, "datePublished": tr["year"]}}
    html = head(slug, page_title, desc, lang, prefix, schema, t["site_fmt"].format(title=title))
    html = html.replace(f'<link rel="canonical" href="{BASE_URL}{slug}/{"en/" if lang == "en" else ""}">', f'<link rel="canonical" href="{BASE_URL}{path}">')
    html = (html.replace(f'href="{BASE_URL}{slug}/">', f'href="{BASE_URL}{slug}/story/">').replace(f'href="{BASE_URL}{slug}/en/">', f'href="{BASE_URL}{slug}/en/story/">'))
    return html + theme_css + f"""
<nav class="crumb"><a href="{top}{t['folder_path']}">{e(t['folder'])}</a> ＞ <a href="../">{e(title)}</a> ＞ {e(t['s_story'])}<a class="lang-switch" href="{'../../story/' if lang == 'en' else '../en/story/'}">{e(t['other_lang'])}</a></nav>
<header class="fg-hero">
  <p class="eyebrow">{e(t['menu'])} · {e(tr['year'])}</p>
  <h1>{e(page_title)}</h1>
  <p class="lead">{e(t['scenes_lead'])}</p>
  <p class="lead"><strong>{e(t['scenes_warn'])}</strong></p>{note_lead}
</header>
<nav class="site-toc" aria-label="{e(t['toc'])}">{toc}</nav>
{take_section(slug, lang)}{contents_box([(f"#c{i}", h, [x[0] for x in sc]) for i, (h, sc) in enumerate(chapters, 1)] + [(f"#c{j}", (u[1] if lang == "en" else u[0]) + (" (not yet released)" if lang == "en" else "（未公開）"), []) for j, u in enumerate(g.get("upcoming", []), len(chapters) + 1)], lang)}
{body}
{common_panel(lang)}
<section class="panel"><div class="btns"><a class="btn primary" href="../">{e(t['scenes_back'])}</a></div></section>
""" + footer(lang, top) + "</body>\n</html>\n"


def main():
    og = []
    for slug, g in FILM_GUIDES.items():
        for lang in ("ja", "en"):
            write(f"{slug}/{'en/' if lang == 'en' else ''}index.html", build_page(slug, lang))
            if g.get("scenes"):
                write(f"{slug}/{'en/' if lang == 'en' else ''}story/index.html", build_scenes_page(slug, lang))
            tr = title_rec(slug, lang)
            og.append(dict(lang=lang, title=tr["title"], year=tr["year"], theme=g.get("theme") or {},
                           out=f"{slug}/{'en/' if lang == 'en' else ''}og.png"))
        # 見た目・動き・顔写真（作品のフォルダの中に置く）
        assets = os.path.join(ROOT, slug, "assets")
        os.makedirs(os.path.join(assets, "chars"), exist_ok=True)
        shutil.copy(os.path.join(SRC, "site.css"), os.path.join(assets, "site.css"))
        shutil.copy(os.path.join(SRC, "relmap.js"), os.path.join(assets, "relmap.js"))
        if slug in RELATION_MAPS:
            for p in RELATION_MAPS[slug]["people"]:
                img = image_for(slug, p["id"])
                if img:
                    shutil.copy(os.path.join(SRC, "chars", img["file"]), os.path.join(assets, "chars", img["file"]))
        write(f"{slug}/sitemap.xml", f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
""" + "".join(f"""  <url><loc>{BASE_URL}{slug}/{p}</loc><lastmod>{g["updated"]}</lastmod>
    <xhtml:link rel="alternate" hreflang="ja" href="{BASE_URL}{slug}/"/><xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}{slug}/en/"/></url>
""" for p in ("", "en/")) + ("".join(f"""  <url><loc>{BASE_URL}{slug}/{p}</loc><lastmod>{g["updated"]}</lastmod>
    <xhtml:link rel="alternate" hreflang="ja" href="{BASE_URL}{slug}/story/"/><xhtml:link rel="alternate" hreflang="en" href="{BASE_URL}{slug}/en/story/"/></url>
""" for p in ("story/", "en/story/")) if g.get("scenes") else "") + "</urlset>\n")
    with open(os.path.join(SRC, "og.json"), "w", encoding="utf-8") as f:
        json.dump(og, f, ensure_ascii=False, indent=1)
    print("built:", ", ".join(FILM_GUIDES))


if __name__ == "__main__":
    main()
