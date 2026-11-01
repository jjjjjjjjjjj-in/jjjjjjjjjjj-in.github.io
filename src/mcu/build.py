"""MCU の作品ガイド（1作品＝1つの独立したサイト）を書き出す。

使い方: python3 src/mcu/build.py   （そのあと共有画像を作るなら node src/mcu/render.js）
出力: /<slug>/index.html（日本語）、/<slug>/en/index.html（英語）、/<slug>/assets/、/<slug>/og.png、/<slug>/sitemap.xml
データ: films.py（文章）、relations.py（相関図）、titles.py（作品の基本情報）
"""
import html
import json
import os
import shutil
import sys
from urllib.parse import quote

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(SRC))
sys.path.insert(0, SRC)

from films import FILM_GUIDES  # noqa: E402
from relations import RELATION_MAPS, image_for  # noqa: E402
from titles import TITLES  # noqa: E402
import relmap_build  # noqa: E402

BASE_URL = "https://jjjjjjjjjjj-in.github.io/"
GA_MEASUREMENT_ID = "G-KDFL8GPPRZ"
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
        toc="このページの内容", s_before="観る前に知っておくと分かりやすいこと", s_map="キャラクター相関図",
        s_story="あらすじ", s_glossary="用語集", s_confusing="ここが分かりにくい！Q&A", s_points="見逃しやすいポイント・小ネタ",
        s_ending="ラストとおまけ映像", s_next="次に観るとよい作品",
        nospoil="ネタバレなし", spoil="ネタバレあり",
        story_open="あらすじを読む（結末までのネタバレを含みます）",
        confusing_note="結末に関わる内容を含みます。",
        post="エンドクレジットの後のおまけ映像",
        shop="この作品をもっと楽しむ", list="マーベル映画紹介のほかのページ", folder="マーベル映画紹介", folder_path="marvel/",
        desc_fmt="『{title}』を映画だけでは分かりにくい人向けに解説。ネタバレなしの観る前のポイント、顔アイコンつき相関図、章ごとのあらすじ、用語集、分かりにくい場面のQ&A、おまけ映像まで。",
        title_fmt="『{title}』完全ガイド｜あらすじ・相関図・用語をやさしく解説",
        site_fmt="{title} 完全ガイド",
    ),
    "en": dict(
        home="Mocchima", guide="Complete Guide", menu="Film guide", other_lang="日本語",
        tagline="The parts that are hard to follow from the film alone, explained with a story summary, a character map and key terms.",
        year="Released", runtime="Runtime", era="Set in",
        toc="On this page", s_before="Good to know before watching", s_map="Character map",
        s_story="Story", s_glossary="Key terms", s_confusing="Confusing parts, explained", s_points="Easy-to-miss details",
        s_ending="The ending and post-credits", s_next="What to watch next",
        nospoil="No spoilers", spoil="Spoilers",
        story_open="Read the story (spoilers up to the ending)",
        confusing_note="Contains spoilers about the ending.",
        post="After the end credits",
        shop="More from this film", list="More Marvel movie guides", folder="Marvel Movie Guides", folder_path="marvel/en/",
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
    schema_html = '\n<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace("</", "<\\/") + "</script>"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">{analytics}
<title>{e(title)}</title>
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


def footer(lang, top):
    if lang == "en":
        return f"""<footer>
<p>This site contains affiliate links (ads).</p>
<p>As an Amazon Associate, this site earns from qualifying purchases.</p>
<p>For how this site uses analytics (Google Analytics) and ads, see the <a href="{PRIVACY_URL}#en">privacy policy</a>.</p>
<p>This is an unofficial fan site run by an individual. It is not affiliated with Marvel Studios, The Walt Disney Company, Sony Pictures or 20th Century Studios. Titles and character names are trademarks of their respective owners.</p>
<p><a href="{top}">Mocchima (all my sites)</a></p>
</footer>
</div>
"""
    return f"""<footer>
<p>※当サイトはアフィリエイト広告（PR）を利用しています。</p>
<p>Amazonのアソシエイトとして、当サイトは適格販売により収入を得ています。</p>
<p>アクセス解析（Googleアナリティクス）と広告の仕組みについては<a href="{PRIVACY_URL}">プライバシーポリシー</a>をご覧ください。</p>
<p>当サイトは個人が運営する非公式ファンサイトです。Marvel Studios、The Walt Disney Company、Sony Pictures、20th Century Studios とは関係ありません。作品名・キャラクター名は各権利者の商標です。</p>
<p><a href="{top}">もっちぃま（運営者のサイト一覧）</a></p>
</footer>
</div>
"""


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
    story = "".join(f'<section class="fg-chapter"><h3>{e(L(x, lang, 0, 2))}</h3><p>{e(L(x, lang, 1, 3))}</p></section>' for x in g["story"])
    confusing = "".join(f'<details class="fg-qa"><summary>{e(L(x, lang, 0, 2))}</summary><p>{e(L(x, lang, 1, 3))}</p></details>' for x in g["confusing"])
    points = "".join(f'<div class="fg-card"><h3>{e(L(x, lang, 0, 2))}</h3><p>{e(L(x, lang, 1, 3))}</p></div>' for x in g["points"])
    nexts = "".join(
        (f'<li><a href="{top}{s}/{"en/" if lang == "en" else ""}">' if s in FILM_GUIDES else '<li><div class="fg-next-item">')
        + f'<b>{e(title_rec(s, lang)["title"])}</b><small>{e(why_en if lang == "en" else why)}</small>'
        + ('</a></li>' if s in FILM_GUIDES else '</div></li>')
        for s, why, why_en in g["next"] if s in TITLES)

    has_map = slug in RELATION_MAPS
    map_html, map_scripts, actors = relmap_build.map_section(slug, lang, e, prefix) if has_map else ("", "", [])
    sections = [("before", t["s_before"])] + ([("map", t["s_map"])] if has_map else []) + [
        ("story", t["s_story"]), ("glossary", t["s_glossary"]), ("confusing", t["s_confusing"]), ("points", t["s_points"]),
        ("ending", t["s_ending"]), ("next", t["s_next"])]
    toc = "".join(f'<a class="chip" href="#{k}">{e(v)}</a>' for k, v in sections)
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
<nav class="crumb"><a href="{top}">{e(t['home'])}</a> ＞ <a href="{top}{t['folder_path']}">{e(t['folder'])}</a> ＞ {e(title)}<a class="lang-switch" href="{'../' if lang == 'en' else 'en/'}" hreflang="{'ja' if lang == 'en' else 'en'}">{e(t['other_lang'])}</a></nav>
<header class="fg-hero">
  <p class="eyebrow">{e(t['menu'])} · {e(tr['year'])}</p>
  <h1>{e(h1)}<small>{e(t['guide'])}</small></h1>
  <p class="lead">{e(t['tagline'])}</p>
  <dl class="fg-facts">{facts_html}</dl>
</header>
<nav class="fg-toc" aria-label="{e(t['toc'])}">{toc}</nav>

<section class="fg-sec" id="before"><h2>{e(t['s_before'])}<span class="tag-ok">{e(t['nospoil'])}</span></h2>
  <div class="fg-cards">{before}</div>
</section>
""" + (f"""
<section class="fg-sec" id="map"><h2>{e(t['s_map'])}<span class="tag-warn">{e(t['spoil'])}</span></h2>
  {map_html}
</section>
""" if has_map else "") + f"""
<section class="fg-sec" id="story"><h2>{e(t['s_story'])}<span class="tag-warn">{e(t['spoil'])}</span></h2>
  <details class="fg-spoiler"><summary>{e(t['story_open'])}</summary>{story}</details>
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

<section class="fg-sec" id="next"><h2>{e(t['s_next'])}</h2>
  <ul class="fg-next">{nexts}</ul>
</section>

<section class="panel">
  <div class="btns"><a class="btn primary" href="{top}{t['folder_path']}">{e(t['list'])}</a></div>
</section>
{map_scripts}""" + footer(lang, top) + "</body>\n</html>\n"


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    og = []
    for slug, g in FILM_GUIDES.items():
        for lang in ("ja", "en"):
            write(f"{slug}/{'en/' if lang == 'en' else ''}index.html", build_page(slug, lang))
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
""" for p in ("", "en/")) + "</urlset>\n")
    with open(os.path.join(SRC, "og.json"), "w", encoding="utf-8") as f:
        json.dump(og, f, ensure_ascii=False, indent=1)
    print("built:", ", ".join(FILM_GUIDES))


if __name__ == "__main__":
    main()
