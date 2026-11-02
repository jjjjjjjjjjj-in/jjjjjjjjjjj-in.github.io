"""パラダイスシティ情報サイトを /paradise-city/ に書き出す。

使い方: python3 src/paradise/build.py
情報を直すときは src/paradise/data.py を編集してから実行する。
"""
import html
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.dirname(HERE)
ROOT = os.path.dirname(SRC)
OUT = os.path.join(ROOT, "paradise-city")
sys.path.insert(0, HERE)
sys.path.insert(0, SRC)

import data as D  # noqa: E402
from build import analytics_tag  # noqa: E402  ドメイン共通の Google アナリティクス

BASE = "https://jjjjjjjjjjj-in.github.io/paradise-city/"
SITE = "パラダイスシティ カジノガイド"
e = html.escape

NAV = [
    ("index.html", "トップ"), ("stay.html", "宿泊プラン"), ("campaigns.html", "キャンペーン"),
    ("perks.html", "お得情報"), ("guide.html", "初心者ガイド"),
    ("howto.html", "会員登録・予約"), ("faq.html", "よくある質問"), ("articles.html", "体験談・記事"),
]

SEARCH = []  # サイト内検索のデータ


def index_search(page, url, title, text):
    SEARCH.append(dict(page=page, url=url, title=title, text=" ".join(text.split())))


def badge(status):
    return f'<span class="badge b-{status}">{D.STATUS_LABEL[status]}</span>'


def source(src, checked):
    label, url = D.SOURCES[src]
    link = f'<a href="{e(url)}" target="_blank" rel="noopener">{e(label)}</a>' if url else e(label)
    return f'<p class="src">出典：{link}（確認日 {checked}）</p>'


LEGEND = ('<div class="legend" aria-label="情報の区分"><span>このサイトの情報の見分け方：</span>'
          + "".join(f'<span>{badge(k)}</span>' for k in D.STATUS_LABEL)
          + '</div>')

ICONS = {
    "passport": '<rect x="10" y="6" width="28" height="36" rx="3"/><circle cx="24" cy="21" r="6"/><path d="M16 33h16"/>',
    "camera": '<rect x="7" y="14" width="34" height="22" rx="3"/><circle cx="24" cy="25" r="6"/><path d="M18 14l3-5h6l3 5"/><path d="M8 40L40 8"/>',
    "shirt": '<path d="M17 8l-9 6 4 7 4-2v21h16V19l4 2 4-7-9-6c-1 3-4 5-7 5s-6-2-7-5z"/>',
    "phone": '<rect x="16" y="6" width="16" height="30" rx="3"/><path d="M8 40h32"/><path d="M24 36v-2"/>',
    "hand": '<path d="M16 26V12a3 3 0 016 0v10V9a3 3 0 016 0v13-9a3 3 0 016 0v17c0 7-5 12-12 12s-11-4-13-9l-3-7a3 3 0 015-3z"/>',
    "stack": '<ellipse cx="24" cy="14" rx="12" ry="5"/><path d="M12 14v8c0 3 5 5 12 5s12-2 12-5v-8"/><path d="M12 22v8c0 3 5 5 12 5s12-2 12-5v-8"/>',
    "dealer": '<circle cx="24" cy="14" r="7"/><path d="M10 40c1-8 7-13 14-13s13 5 14 13"/><path d="M20 27l4 5 4-5"/>',
    "cash": '<rect x="6" y="15" width="36" height="20" rx="2"/><circle cx="24" cy="25" r="5"/><path d="M6 40h36"/>',
    "ask": '<circle cx="24" cy="24" r="17"/><path d="M19 19a5 5 0 119 3c-2 2-4 3-4 6"/><path d="M24 34v1"/>',
}


def icon(name):
    return (f'<svg viewBox="0 0 48 48" aria-hidden="true" fill="none" stroke="#b8924a" stroke-width="2.4" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>')


def travel_ads(keys):
    from urllib.parse import quote
    rows = []
    for name, kw in (D.TRAVEL_GOODS[k] for k in keys):
        amz = f"https://www.amazon.co.jp/s?k={quote(kw)}&tag={D.AMAZON_TAG}"
        rak = (f"https://af.moshimo.com/af/c/click?a_id={D.MOSHIMO_A_ID}&p_id=54&pc_id=54&pl_id=616&url="
               + quote(f"https://search.rakuten.co.jp/search/mall/{quote(kw)}/", safe=""))
        rows.append(f'<li><span>{e(name)}</span><span class="ad-links"><a href="{e(amz)}" target="_blank" rel="sponsored noopener">Amazon</a>'
                    f'<a href="{e(rak)}" target="_blank" rel="sponsored noopener">楽天市場</a></span></li>')
    return f"""<aside class="ads" aria-labelledby="h-ads"><h2 id="h-ads"><span class="pr">PR</span>韓国旅行の持ち物</h2>
  <p class="muted">旅行の準備に役立つ物です。リンク先はAmazonと楽天市場の検索結果です。</p>
  <ul class="ad-list">{''.join(rows)}</ul>
  <p class="muted">このコーナーは広告（アフィリエイト）です。Amazonのアソシエイトとして、当サイトは適格販売により収入を得ています。</p>
</aside>"""


def layout(file, title, desc, body, head_html, extra_head=""):
    if file in D.AD_PAGES:
        body = body + travel_ads(D.AD_PAGES[file])
    nav = "".join(f'<li><a href="{f}"{" aria-current=\"page\"" if f == file else ""}>{e(n)}</a></li>' for f, n in NAV)
    canonical = BASE + ("" if file == "index.html" else file)
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><link rel="apple-touch-icon" href="/icons/paradise.png"><link rel="icon" type="image/png" href="/icons/paradise.png">{analytics_tag()}
<title>{e(title)}</title>
<meta name="apple-mobile-web-app-title" content="パラダイスシティ">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}img/hyatt-lobby.jpg">
<meta property="og:locale" content="ja_JP">
<meta name="twitter:card" content="summary_large_image">{extra_head}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1:wght@600;800&family=Zen+Kaku+Gothic+New:wght@400;700&display=swap">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="site-header gutter"><div class="inner">
  <a class="brand" href="index.html">PARADISE <span>CITY</span> GUIDE</a>
  <form class="search-form" action="search.html" role="search">
    <input type="search" name="q" id="site-search" aria-label="サイト内を検索" placeholder="サイト内を検索">
    <button type="submit">検索</button>
  </form>
</div></header>
<nav class="site-nav gutter" aria-label="ページ一覧"><ul>{nav}</ul></nav>
{head_html}
<main class="gutter"><div class="inner">
{body}
</div></main>
<footer class="site-footer gutter"><div class="inner">
  <p><strong>カジノは満19歳以上の外国人のみ入場できます。</strong>日本国内からオンラインカジノに参加することは違法です。このサイトは韓国にある施設の旅行情報として掲載しています。</p>
  <p>カジノは「なくなっても困らない金額」で楽しみましょう。のめり込みが心配なときは、お住まいの地域の精神保健福祉センターなどに相談できます。</p>
  <p>当サイトは個人が運営する非公式の情報サイトで、パラダイスシティおよび各ホテルとは関係ありません。料金・条件・キャンペーンは変わることがあります。最新の情報は必ず<a href="{D.SOURCES['official_top'][1]}" target="_blank" rel="noopener">公式サイト</a>で確認してください。最終更新 {D.UPDATED}</p>
  <p><a href="https://jjjjjjjjjjj-in.github.io/privacy.html">プライバシーポリシー</a></p>
</div></footer>
<script src="assets/app.js"></script>
</body>
</html>
"""


def page_head(h1, lead):
    return f"""<header class="page-head gutter"><div class="inner">
  <p class="eyebrow">PARADISE CITY GUIDE</p>
  <h1>{e(h1)}</h1>
  <p>{e(lead)}</p>
  <p class="updated">最終更新 {D.UPDATED}</p>
</div></header>"""


def info_card(title, text, status, src, checked, dark=False):
    return f"""<div class="card{' dark' if dark else ''}">
  <div class="badge-row">{badge(status)}</div>
  <h3>{e(title)}</h3>
  <p>{e(text)}</p>
  {source(src, checked)}
</div>"""


def campaign_card(c):
    end = c["stay_to"] or c["book_to"]
    if c["status"] == "past":
        state = '<span class="state state-ended">終了・過去の情報</span>'
    elif end:
        state = '<span class="state state-open">受付中</span>'
    else:
        state = '<span class="state state-unknown">期間：要確認</span>'
    period = lambda a, b: f"{a or '要確認'} 〜 {b or '要確認'}"
    link = f'<p><a class="btn" href="{e(c["url"])}" target="_blank" rel="noopener">{e(c.get("url_label", "公式ページで内容を確認する"))}</a></p>' if c["url"] else ""
    if c.get("month"):
        state += f' <span class="state state-unknown">{e(c["month"])}の情報</span>'
    return f"""<article class="card" data-campaign data-start="{c['book_from']}" data-end="{end}">
  <div class="badge-row">{badge(c['status'])}{state}</div>
  <h3>{e(c['name'])}</h3>
  <p class="muted">{e(c['kind'])}</p>
  <dl class="dl">
    <dt>予約期間</dt><dd>{period(c['book_from'], c['book_to'])}</dd>
    <dt>宿泊対象期間</dt><dd>{period(c['stay_from'], c['stay_to'])}</dd>
    <dt>泊数</dt><dd>{e(c['nights'])}</dd>
    <dt>対象日</dt><dd>{e(c['days'])}</dd>
    <dt>特典</dt><dd>{e(c['perks'])}</dd>
    <dt>条件</dt><dd>{e(c['conditions'])}</dd>
  </dl>
  <p class="muted">{e(c['note'])}</p>
  {link}
  {source(c['src'], c['checked'])}
</article>"""


def compare_table():
    rows = []
    for c in D.CAMPAIGNS["current"] + D.CAMPAIGNS["archive"]:
        past = c["status"] == "past"
        state = "終了・過去の情報" if past else "期間：要確認"
        rows.append(f"""<tr class="{'is-past' if past else ''}"><th scope="row">{e(c['name'])}<br>{badge(c['status'])}</th>
<td class="nw">{state}</td><td>{e(c['nights'])}</td><td>{e(c['days'])}</td><td>{e(c['perks'])}</td><td>{e(c['conditions'])}</td>
<td>{c['book_from'] or '要確認'}</td><td>{(c['stay_from'] or '要確認') + ' 〜 ' + (c['stay_to'] or '要確認')}</td></tr>""")
    return f"""<div class="table-wrap"><table>
<thead><tr><th>プラン</th><th>状態</th><th>泊数</th><th>対象日</th><th>特典</th><th>条件</th><th>予約開始日</th><th>宿泊対象期間</th></tr></thead>
<tbody>{''.join(rows)}</tbody></table></div>
<p class="muted">表は横にスクロールできます。「過去の情報」は今も同じ内容で使えるとは限りません。</p>"""


def faq_block(items, ids=True):
    out = []
    for i, (q, a, status, src) in enumerate(items, 1):
        out.append(f"""<details id="faq-{i}"><summary>{e(q)}</summary><div class="answer">
  <div class="badge-row">{badge(status)}</div><p>{e(a)}</p>{source(src, D.UPDATED)}</div></details>""")
    return '<div class="faq">' + "".join(out) + "</div>"


def basics_cards(keys=None):
    items = [b for b in D.BASICS if keys is None or b["key"] in keys]
    return '<div class="cards">' + "".join(info_card(b["title"], b["text"], b["status"], b["src"], b["checked"]) for b in items) + "</div>"


def rule_cards(rules, with_meta=True):
    out = []
    for r in rules:
        meta = ""
        if with_meta and "status" in r:
            meta = f'<div class="badge-row">{badge(r["status"])}</div>{source(r["src"], r["checked"])}'
        out.append(f'<div class="rule">{icon(r["icon"])}<div><h3>{e(r["title"])}</h3><p>{e(r["text"])}</p>{meta}</div></div>')
    return '<div class="rules">' + "".join(out) + "</div>"


def photos(items=None, wide=False):
    items = D.HOTEL["photos"] if items is None else items
    w, h = ("1200", "900") if wide else ("1000", "1333")
    return f'<div class="photos{" wide" if wide else ""}">' + "".join(
        f'<figure><img src="{p}" alt="{e(alt)}" loading="lazy" width="{w}" height="{h}"><figcaption>{e(cap)}（運営者撮影）</figcaption></figure>'
        for p, alt, cap in items) + "</div>"


def deal_cards(items):
    return '<div class="cards">' + "".join(info_card(d["title"], d["text"], d["status"], d["src"], d["checked"]) for d in items) + "</div>"


# ---------- pages ----------

def page_index():
    tiles = [
        ("perks.html", "お得情報", "会員特典・食事券・ポイント"), ("campaigns.html", "キャンペーン", "今のプランと過去の事例"),
        ("article-cafe9.html", "Cafe 9", "カジノの中のご飯"), ("stay.html", "宿泊プラン", "ホテルと比較表"),
        ("guide.html", "初心者ガイド", "入場・テーブルのルールと予算"),
        ("howto.html", "会員登録・予約", "予約前の確認ポイント"),
        ("faq.html", "よくある質問", "パスポート・日本円など"), ("articles.html", "体験談・記事", "8回通った運営者のメモ"),
    ]
    tile_html = '<nav class="tiles" aria-label="主なページ">' + "".join(
        f'<a class="tile" href="{u}"><strong>{e(t)}</strong><span>{e(s)}</span></a>' for u, t, s in tiles) + "</nav>"
    head = f"""<header class="hero gutter">
  <img src="img/pegasus.jpg" alt="" width="1050" height="1400">
  <div class="inner">
    <p class="eyebrow">PARADISE CITY · INCHEON</p>
    <h1><span class="nb">日本人向け</span><span class="nb">パラダイスシティ</span><br><span class="nb">カジノの</span><span class="nb">お得情報まとめ</span></h1>
    <p class="lead">韓国・仁川のパラダイスシティのカジノで使える、新規会員のクーポン、ポイント、食事券、宿泊プランなどのお得情報を、公式情報と体験談を分けて紹介します。</p>
    <p class="photo-credit">写真：パラダイスシティのホテルのロビーにある金色のペガサス像（運営者撮影）・最終更新 {D.UPDATED}</p>
  </div>
</header>"""
    current = "".join(campaign_card(c) for c in D.CAMPAIGNS["current"])
    updates = "".join(f'<li><time datetime="{d}">{d}</time>{e(t)}</li>' for d, t in D.UPDATES)
    latest = "".join(f'<li><time datetime="{a["date"]}">{a["date"]}</time><a href="article-{a["slug"]}.html">{e(a["title"])}</a></li>' for a in D.ARTICLES)
    body = f"""
{tile_html}
{LEGEND}
<section aria-labelledby="h-deals"><h2 id="h-deals">お得情報まとめ</h2>
  <p class="notice">「公式情報」はパラダイスシティの公式サイトで確認した内容です。条件は変わることがあるので、使う前に現地のデスクで確認してください。</p>
  {deal_cards(D.DEALS[:6])}
  <p><a class="btn primary" href="perks.html">お得情報をすべて見る</a></p>
</section>
<section aria-labelledby="h-cafe9"><h2 id="h-cafe9">最初のご飯は、カジノの「Cafe 9」</h2>
  <p><span class="badge b-exp">体験談</span> パラダイスシティに着いて最初に食べたのは、カジノの中のレストラン「Cafe 9」のご飯でした。丼もののセットがあり、日本人にも食べやすい味です。</p>
  {photos(D.CAFE9_PHOTOS, wide=True)}
  <p><a class="btn" href="article-cafe9.html">Cafe 9 の記事を読む</a></p>
</section>
<section aria-labelledby="h-camp"><h2 id="h-camp">最新のキャンペーン</h2>
  <p class="notice alert"><strong>今のところ、内容と期間まで公式に確認できた「開催中」のキャンペーンはありません。</strong>公式予約ページに掲載されているプランを、確認できた範囲で載せています。</p>
  <div class="cards">{current}</div>
  <p><a class="btn" href="campaigns.html">過去のキャンペーンも見る</a></p>
</section>
<section aria-labelledby="h-stay"><h2 id="h-stay">おすすめの宿泊</h2>
  <div class="cards">
    <div class="card"><div class="badge-row">{badge('exp')}</div><h3>{D.HOTEL['name']}（{D.HOTEL['name_en']}）</h3>
      <p>運営者が泊まったホテルの1つです。過去にはカジノ会員向けに、平日最大4泊・朝食券つきのプランがありました（過去の情報）。</p>
      <p><a class="btn primary" href="stay.html">宿泊プランを比べる</a></p></div>
    <figure class="card" style="padding:0;overflow:hidden;margin:0"><img src="img/hyatt-room.jpg" alt="ハイアット リージェンシー 仁川の客室" loading="lazy" width="1000" height="1333" style="aspect-ratio:4/3;object-fit:cover"></figure>
  </div>
</section>
<section aria-labelledby="h-guide"><h2 id="h-guide">カジノ初心者ガイド</h2>
  {rule_cards(D.ENTRY_RULES[:2] + D.TABLE_RULES[:2], with_meta=False)}
  <p><a class="btn" href="guide.html">ルールをすべて見る</a></p>
</section>
<section aria-labelledby="h-basic"><h2 id="h-basic">カジノの基本ルール</h2>
  {basics_cards(['hours', 'who', 'dress', 'yen'])}
</section>
<section aria-labelledby="h-faq"><h2 id="h-faq">よくある質問</h2>
  {faq_block(D.FAQ[:5])}
  <p><a class="btn" href="faq.html">質問をすべて見る</a></p>
</section>
<section aria-labelledby="h-new"><h2 id="h-new">最新記事・更新情報</h2>
  <h3>記事</h3><ul class="updates">{latest}</ul>
  <h3>更新情報</h3><ul class="updates">{updates}</ul>
</section>"""
    index_search("トップ", "index.html", "パラダイスシティ カジノガイド", "パラダイスシティ カジノ お得 宿泊 食事券 初心者 ルール 予算 キャンペーン")
    for d in D.DEALS:
        index_search("お得情報", "perks.html#h-deals", d["title"], d["text"])
    return layout("index.html", "パラダイスシティ カジノのお得情報まとめ｜日本人向け 会員特典・食事券・宿泊【2026年版】",
                  "韓国・仁川のパラダイスシティのカジノのお得情報を日本人向けにまとめました。新規会員のクーポン、ポイント、Cafe 9 の食事券、宿泊プランを、公式情報と体験談を区別して紹介します。", body, head)


def page_stay():
    facts = "".join(info_card("ホテル情報", f["text"], f["status"], f["src"], f["checked"]) for f in D.HOTEL["facts"])
    archive = "".join(campaign_card(c) for c in D.CAMPAIGNS["archive"])
    current = "".join(campaign_card(c) for c in D.CAMPAIGNS["current"])
    checks = "".join(f"<li>{e(c)}</li>" for c in D.BOOKING_CHECKS)
    body = f"""
{LEGEND}
<section aria-labelledby="h-hotel"><h2 id="h-hotel">{D.HOTEL['name']}</h2>
  <p>パラダイスシティのカジノに行くときに、運営者が泊まったホテルです。写真はすべて運営者が撮影しました。</p>
  {photos()}
  <div class="cards">{facts}</div>
</section>
<section aria-labelledby="h-fac"><h2 id="h-fac">パラダイスシティのホテルと施設（公式）</h2>
  {deal_cards(D.FACILITIES)}
  <p><a class="btn" href="{D.SOURCES['official_map'][1]}" target="_blank" rel="noopener">公式のフロアマップを見る</a></p>
</section>
<section aria-labelledby="h-compare"><h2 id="h-compare">宿泊プラン比較表</h2>
  {compare_table()}
</section>
<section aria-labelledby="h-now"><h2 id="h-now">公式サイトに掲載されているプラン</h2>
  <p class="notice">内容と期間まで確認できたものはまだありません。予約する前に、必ず公式ページで条件を確認してください。</p>
  <div class="cards">{current}</div>
</section>
<section aria-labelledby="h-notes"><h2 id="h-notes">予約するときの注意点</h2>
  <ul class="checklist">{checks}</ul>
  <div class="btns">
    <a class="btn primary" href="{D.SOURCES['official_reserve'][1]}" target="_blank" rel="noopener">公式予約ページ</a>
    <a class="btn" href="{D.SOURCES['rakuten'][1]}" target="_blank" rel="noopener">楽天トラベルで見る</a>
  </div>
</section>
<section aria-labelledby="h-archive"><h2 id="h-archive">過去の宿泊プラン・キャンペーン（アーカイブ）</h2>
  <p class="notice alert"><strong>ここに載っているのは過去の情報です。</strong>今も同じ条件で使えるとは限りません。</p>
  <div class="cards">{archive}</div>
</section>"""
    for c in D.CAMPAIGNS["archive"] + D.CAMPAIGNS["current"]:
        index_search("宿泊プラン", "stay.html#h-compare", c["name"], c["perks"] + " " + c["conditions"] + " " + c["note"])
    for f in D.HOTEL["facts"]:
        index_search("宿泊プラン", "stay.html#h-hotel", D.HOTEL["name"], f["text"])
    for f in D.FACILITIES:
        index_search("宿泊プラン", "stay.html#h-fac", f["title"], f["text"])
    index_search("宿泊プラン", "stay.html#h-notes", "予約するときの注意点", " ".join(D.BOOKING_CHECKS))
    return layout("stay.html", "パラダイスシティ 宿泊プラン｜ハイアットの特典と無料宿泊キャンペーンの過去事例",
                  "パラダイスシティのカジノに行くときの宿泊プランを比較。ハイアット リージェンシー 仁川の写真、朝食券・ドリンク券つきプラン、ゲーム条件付き宿泊キャンペーンの過去事例をまとめました。",
                  body, page_head("宿泊プラン・ホテル情報", "ハイアット リージェンシー 仁川の様子と、過去・現在の宿泊プランを比較できます。"))


def page_campaigns():
    current = "".join(campaign_card(c) for c in D.CAMPAIGNS["current"])
    archive = "".join(campaign_card(c) for c in D.CAMPAIGNS["archive"])
    body = f"""
{LEGEND}
<section aria-labelledby="h-c"><h2 id="h-c">現在のキャンペーン</h2>
  <p class="notice alert"><strong>内容と期間まで公式に確認できた「開催中」のキャンペーンは、今のところありません。</strong>公式予約ページに掲載されているプランを載せています。期間が分かったものは、残り日数を自動で表示します。</p>
  <div class="cards">{current}</div>
</section>
<section aria-labelledby="h-a"><h2 id="h-a">過去のキャンペーン（アーカイブ）</h2>
  <p class="notice"><strong>終了したキャンペーンや、過去に利用された情報です。</strong>参考としてご覧ください。</p>
  <div class="cards">{archive}</div>
</section>"""
    for c in D.CAMPAIGNS["current"] + D.CAMPAIGNS["archive"]:
        index_search("キャンペーン", "campaigns.html", c["name"], c["kind"] + " " + c["perks"] + " " + c["conditions"] + " " + c["note"])
    return layout("campaigns.html", "パラダイスシティ キャンペーン情報｜無料宿泊・会員特典の現在と過去",
                  "パラダイスシティのカジノの宿泊キャンペーンや会員向けプランを、現在のものと終了した過去の事例に分けて紹介します。",
                  body, page_head("キャンペーン", "現在のプランと、終了した過去のキャンペーンを分けて掲載しています。"))


def page_perks():
    cards = "".join(info_card(p["title"], p["text"], p["status"], p["src"], p["checked"]) for p in D.PERKS)
    slots = "".join(f'<div class="card"><div class="badge-row">{badge("check")}</div><h3>{e(s)}</h3><p class="muted">情報を集めています。分かり次第ここに載せます。</p></div>' for s in D.PERK_SLOTS)
    body = f"""
{LEGEND}
<section aria-labelledby="h-deals"><h2 id="h-deals">お得情報まとめ</h2>
  {deal_cards(D.DEALS)}
</section>
<section aria-labelledby="h-cafe9"><h2 id="h-cafe9">Cafe 9 のご飯</h2>
  {photos(D.CAFE9_PHOTOS, wide=True)}
  <p><a class="btn" href="article-cafe9.html">Cafe 9 の記事を読む</a></p>
</section>
<section aria-labelledby="h-p"><h2 id="h-p">食事券・ドリンク券・会員カード</h2>
  <p class="notice">特典の条件は、会員ランクや時期によって変わる可能性があります。使う前にカジノのカウンターで確認してください。</p>
  <div class="cards">{cards}</div>
</section>
<section aria-labelledby="h-s"><h2 id="h-s">これから確認する特典</h2>
  <div class="cards">{slots}</div>
</section>
<section aria-labelledby="h-stayperk"><h2 id="h-stayperk">宿泊特典</h2>
  <p>過去の宿泊プランでは、Market Caféの朝食券やSwell Loungeのドリンク券がついていました。詳しくは<a href="stay.html">宿泊プランのページ</a>を見てください。</p>
</section>"""
    for p in D.PERKS:
        index_search("食事券・特典", "perks.html", p["title"], p["text"])
    return layout("perks.html", "パラダイスシティ カジノのお得情報｜新規会員クーポン・ポイント・食事券",
                  "パラダイスシティのカジノのお得情報。新規会員のクーポン、ポイントの使い道、会員ランク、Cafe 9 の食事券、無料シャトルを、公式情報とユーザー提供情報に分けて紹介します。",
                  body, page_head("お得情報・特典", "新規会員のクーポン、ポイント、食事券など、日本人の旅行者に役立つお得情報をまとめています。"))


def page_guide():
    body = f"""
{LEGEND}
<p class="notice alert"><strong>ここに書いているのは初心者向けの基本の案内です。</strong>ゲームやテーブルごとに細かいルールが違うことがあります。施設の規則と、現地スタッフの指示を優先してください。</p>
<section aria-labelledby="h-in"><h2 id="h-in">入場するとき</h2>
  {rule_cards(D.ENTRY_RULES)}
</section>
<section aria-labelledby="h-t"><h2 id="h-t">テーブルゲームで気をつけること</h2>
  {rule_cards(D.TABLE_RULES)}
  {source('users', D.UPDATED)}
</section>
<section aria-labelledby="h-floor"><h2 id="h-floor">フロアの並びとおすすめのテーブル</h2>
  <p>{badge('exp')} 入口のすぐ手前にクラップスとルーレット、まっすぐ進むとブラックジャックやポーカー、その先にたくさんのバカラの台があります。運営者の体感では、サレンダーができるブラックジャックがいちばんチップが減りにくかったです。</p>
  <p><a class="btn" href="article-floor-tables.html">体験談を読む</a></p>
</section>
{budget_sections()}
<section aria-labelledby="h-b"><h2 id="h-b">カジノの基本情報</h2>
  {basics_cards()}
</section>
<section aria-labelledby="h-next"><h2 id="h-next">次に読む</h2>
  <div class="btns"><a class="btn primary" href="howto.html">会員登録の流れを見る</a></div>
</section>"""
    for r in D.ENTRY_RULES + D.TABLE_RULES:
        index_search("初心者ガイド", "guide.html", r["title"], r["text"])
    for b in D.BASICS:
        index_search("初心者ガイド", "guide.html#h-b", b["title"], b["text"])
    bd = D.BUDGET
    index_search("初心者ガイド", "guide.html#h-budget", "最低ベットと予算の目安", bd["text_min_bet"] + " " + bd["text_budget"])
    index_search("初心者ガイド", "guide.html#h-sim", "予算シミュレーター", "予算 最低ベット 資金管理 シミュレーター")
    return layout("guide.html", "パラダイスシティ カジノ初心者ガイド｜入場ルールとテーブルのマナー",
                  "初めてパラダイスシティのカジノに行く人向けに、パスポート・服装・撮影禁止などの入場ルールと、テーブルゲームでのマナーをイラストつきで解説します。",
                  body, page_head("カジノ初心者ガイド", "入場のルール、テーブルで気をつけること、予算の目安を分かりやすくまとめました。"))


def budget_sections():
    b = D.BUDGET
    return f"""<section aria-labelledby="h-budget"><h2 id="h-budget">予算の目安（最低ベット）</h2>
  <div class="cards">
    {info_card('最低ベット', b['text_min_bet'], b['status'], b['src'], b['checked'])}
    {info_card('持って行く金額', b['text_budget'], b['status'], b['src'], b['checked'])}
  </div>
  <p class="notice">最低ベットは、ゲーム・テーブル・時期・為替で変わります。決まった金額ではありません。</p>
</section>
<section aria-labelledby="h-sim"><h2 id="h-sim">予算シミュレーター</h2>
  <div class="sim" id="sim">
    <div class="fields">
      <label for="sim-budget">予算（円）<input id="sim-budget" type="number" inputmode="numeric" min="0" step="1000" value="20000"></label>
      <label for="sim-bet">最低ベット（円）<input id="sim-bet" type="number" inputmode="numeric" min="100" step="500" value="{b['min_bet_yen']}"></label>
      <label for="sim-hours">遊ぶ予定の時間（時間）<input id="sim-hours" type="number" inputmode="numeric" min="1" step="1" value="2"></label>
    </div>
    <div class="sim-out" id="sim-out" aria-live="polite"><p class="muted">予算を入れると、資金管理の目安が出ます。</p></div>
  </div>
</section>
<section aria-labelledby="h-rule"><h2 id="h-rule">お金のことで大切なこと</h2>
  <ul class="checklist">
    <li>予算は「なくなっても困らない金額」だけにする</li>
    <li>負けを取り返そうとして、その場で追加の両替をしない</li>
    <li>終わる時間と、休憩するラインを先に決めておく</li>
    <li>カジノで利益が出ることは保証されていません</li>
  </ul>
</section>"""


def page_budget():
    # 予算のページは初心者ガイドにまとめた（運営者の希望、2026-11-02）。古いアドレスは転送だけ
    return """<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>初心者ガイドへ移動しました</title>
<meta name="robots" content="noindex"><link rel="canonical" href="guide.html#h-budget">
<meta http-equiv="refresh" content="0; url=guide.html#h-budget"></head>
<body><p><a href="guide.html#h-budget">初心者ガイドの「予算」へ移動しました</a></p></body></html>"""


def page_howto():
    steps = "".join(f"""<div class="card"><div class="badge-row"><strong>STEP {i}</strong>{badge(s['status'])}</div><h3>{e(s['title'])}</h3><p>{e(s['text'])}</p>{source(s['src'], s['checked'])}</div>"""
                    for i, s in enumerate(D.SIGNUP_STEPS, 1))
    checks = "".join(f"<li>{e(c)}</li>" for c in D.BOOKING_CHECKS)
    body = f"""
{LEGEND}
<div class="notice alert"><strong>予約の前に必ず確認：</strong><p>キャンペーンや宿泊特典には、予約の期限が決まっていることがあります。たとえば「宿泊の3日前までに手続きが必要」なプランもありました。ただし、これはすべてのプランに共通するルールではありません。プランごとに条件を確認してください。</p></div>
<section aria-labelledby="h-steps"><h2 id="h-steps">会員登録から宿泊までの流れ</h2>
  <div class="cards">{steps}</div>
</section>
<section aria-labelledby="h-need"><h2 id="h-need">登録に必要なもの</h2>
  {basics_cards(['passport', 'who', 'dress'])}
</section>
<section aria-labelledby="h-chk"><h2 id="h-chk">予約・変更・キャンセルの注意点</h2>
  <ul class="checklist">{checks}</ul>
  <div class="btns"><a class="btn primary" href="{D.SOURCES['official_reserve'][1]}" target="_blank" rel="noopener">公式予約ページ</a><a class="btn" href="{D.SOURCES['official_faq'][1]}" target="_blank" rel="noopener">公式FAQ</a></div>
</section>"""
    for s in D.SIGNUP_STEPS:
        index_search("会員登録・予約", "howto.html", s["title"], s["text"])
    index_search("会員登録・予約", "howto.html#h-chk", "予約の期限・キャンセル", " ".join(D.BOOKING_CHECKS))
    return layout("howto.html", "パラダイスシティ カジノ会員登録・宿泊予約の方法と注意点",
                  "パラダイスシティのカジノ会員登録の流れ、必要なもの、宿泊予約で特典を受けるための注意点、予約期限やキャンセルの確認ポイントを解説します。",
                  body, page_head("会員登録・予約方法", "会員登録から宿泊までの流れと、予約前に確認したいポイントです。"))


def page_faq():
    body = f"""
{LEGEND}
<section aria-labelledby="h-f"><h2 id="h-f">よくある質問</h2>
  <p><button class="btn" type="button" id="faq-toggle">すべて開く</button></p>
  {faq_block(D.FAQ)}
</section>"""
    for i, (q, a, *_r) in enumerate(D.FAQ, 1):
        index_search("よくある質問", f"faq.html#faq-{i}", q, a)
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a, *_r in D.FAQ]}
    extra = '\n<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False).replace("</", "<\\/") + "</script>"
    return layout("faq.html", "パラダイスシティ カジノ よくある質問｜パスポート・日本円・撮影・食事券",
                  "パラダイスシティのカジノについてのよくある質問。入場に必要なもの、撮影、予算、食事券、日本円、チップの交換などに答えます。",
                  body, page_head("よくある質問", "公式情報を優先し、確認できないものは「要確認」と書いています。"), extra)


def page_articles():
    cats = sorted({a["category"] for a in D.ARTICLES})
    chips = '<div class="chips" role="group" aria-label="カテゴリー"><button class="chip" type="button" data-filter="all" aria-pressed="true">すべて</button>' + "".join(
        f'<button class="chip" type="button" data-filter="{e(c)}" aria-pressed="false">{e(c)}</button>' for c in cats) + "</div>"
    cards = "".join(f"""<a class="card" data-category="{e(a['category'])}" href="article-{a['slug']}.html" style="text-decoration:none;color:inherit">
  <div class="badge-row">{badge(a['status'])}<span class="muted">{e(a['category'])} ・ {a['date']}</span></div>
  <h3>{e(a['title'])}</h3><p class="muted">{e(a['lead'])}</p></a>""" for a in D.ARTICLES)
    body = f"""
<section aria-labelledby="h-list"><h2 id="h-list">記事一覧</h2>
  {chips}
  <div class="cards">{cards}</div>
</section>"""
    return layout("articles.html", "パラダイスシティ 体験談・記事一覧｜宿泊レポートや食事券のメモ",
                  "パラダイスシティのカジノに2026年だけで8回通った運営者の体験談や、ハイアット リージェンシー 仁川の宿泊レポートなどの記事一覧です。",
                  body, page_head("体験談・記事", "カテゴリーで絞り込めます。体験談は個人の感想で、公式情報ではありません。"))


def page_article(a):
    def table(rows):
        head, *rest = rows
        return ('<div class="table-wrap fit"><table><thead><tr>' + "".join(f"<th>{e(c)}</th>" for c in head) + "</tr></thead><tbody>"
                + "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rest) + "</tbody></table></div>")
    sections = "".join(f"<section><h2>{e(b[0])}</h2><p>{e(b[1])}</p>{table(b[2]) if len(b) > 2 else ''}</section>" for b in a["body"])
    pics = {"hotel": photos(), "cafe9": photos(D.CAFE9_PHOTOS, wide=True)}.get(a.get("photos"), "")
    body = f"""
<div class="article-body">
  <div class="badge-row">{badge(a['status'])}<span class="muted">{e(a['category'])} ・ {a['date']}</span></div>
  <p>{e(a['lead'])}</p>
  {pics}
  {sections}
  <p class="notice">この記事は{D.STATUS_LABEL[a['status']]}です。公式情報ではありません。条件は変わることがあるので、最新の情報は公式サイトで確認してください。</p>
  <p><a class="btn" href="articles.html">記事一覧に戻る</a></p>
</div>"""
    index_search("体験談・記事", f"article-{a['slug']}.html", a["title"], a["lead"] + " " + " ".join(b[1] for b in a["body"]))
    return layout(f"article-{a['slug']}.html", f"{a['title']}｜{SITE}", a["lead"], body, page_head(a["title"], a["lead"]))


def page_search():
    body = """
<section aria-labelledby="h-s"><h2 id="h-s">サイト内検索</h2>
  <form class="search-form" action="search.html" role="search" style="max-width:520px;margin:0">
    <input type="search" name="q" id="search-page-input" aria-label="検索する言葉" placeholder="例：食事券、パスポート、ハイアット" style="background:#fff;color:#1b1b1f;border-color:#e4ddcf">
    <button type="submit">検索</button>
  </form>
  <ul class="results" id="search-results"><li class="muted">検索しています…</li></ul>
</section>"""
    return layout("search.html", f"サイト内検索｜{SITE}", "パラダイスシティ カジノガイドのサイト内検索です。", body,
                  page_head("サイト内検索", "キーワードを入れると、すべてのページの中から探せます。"), '\n<meta name="robots" content="noindex">')


def main():
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(HERE, "style.css"), os.path.join(OUT, "assets", "style.css"))
    shutil.copy(os.path.join(HERE, "app.js"), os.path.join(OUT, "assets", "app.js"))
    pages = {
        "index.html": page_index(), "stay.html": page_stay(), "campaigns.html": page_campaigns(),
        "perks.html": page_perks(), "guide.html": page_guide(), "budget.html": page_budget(),
        "howto.html": page_howto(), "faq.html": page_faq(), "articles.html": page_articles(),
    }
    for a in D.ARTICLES:
        pages[f"article-{a['slug']}.html"] = page_article(a)
    pages["search.html"] = page_search()
    for name, text in pages.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(text)
    with open(os.path.join(OUT, "search.json"), "w", encoding="utf-8") as f:
        json.dump(SEARCH, f, ensure_ascii=False)
    urls = [n for n in pages if n not in ("search.html", "budget.html")]
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"  <url><loc>{BASE}{'' if n == 'index.html' else n}</loc><lastmod>{D.UPDATED}</lastmod></url>\n" for n in urls)
                + "</urlset>\n")
    print(f"built paradise-city: {len(pages)} pages, {len(SEARCH)} search entries")


if __name__ == "__main__":
    main()
