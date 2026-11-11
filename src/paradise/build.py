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
from games import GAMES  # noqa: E402
from build import analytics_tag  # noqa: E402  ドメイン共通の Google アナリティクス

BASE = "https://mocchima.com/paradise-city/"
SITE = "パラダイスシティ カジノガイド"
e = html.escape

# ページの並び（2026-11-05 にテーマ別に組み直した。アクセスは「最初にやること」からも案内する）
NAV = [
    ("index.html", "トップ"), ("start.html", "最初にやること"), ("perks.html", "お得情報"), ("articles.html", "体験談ブログ"),
    ("cafe9.html", "Cafe 9"), ("stay.html", "宿泊プラン"), ("guide.html", "初心者ガイド"), ("faq.html", "よくある質問"),
    ("campaigns.html", "キャンペーン"), ("access.html", "アクセス"),
]
# トップのタイル（運営者の希望の順）
TILES = [
    ("start.html", "最初にやること", "到着から帰るまでの流れ"), ("perks.html", "お得情報", "会員特典・クーポン・ポイント"),
    ("articles.html", "体験談ブログ", "8回以上通った運営者の記録"), ("cafe9.html", "Cafe 9", "食事券の使い方とご飯"),
    ("stay.html", "宿泊プラン", "ホテルと無料宿泊"), ("guide.html", "初心者ガイド", "ルール・ゲーム・予算"),
    ("faq.html", "よくある質問", "パスポート・日本円など"), ("campaigns.html", "キャンペーン", "今月の情報と過去の事例"),
]
# 内容をほかのページへまとめた古いアドレス（転送だけ。サイトマップには入れない）
REDIRECTS = {"howto.html": "start.html#h-member", "budget.html": "guide.html#h-budget"}

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


# 楽天は A8.net 経由（2026-11-11 に、もしも経由から替えた。もしもの登録が削除されたため）。A8 の「任意ページリンク生成」と同じ形
A8_RAKUTEN_MAT = "4BESUC+2A5VSY+2HOM+BW8O1"
A8_RAKUTEN_PIXEL = f'<img border="0" width="1" height="1" src="https://www16.a8.net/0.gif?a8mat={A8_RAKUTEN_MAT}" alt="">'


def a8_rakuten(url):
    """楽天のページ（url）へ行く、A8.net 経由のリンクを作る"""
    from urllib.parse import quote as _q
    hb = ("http://hb.afl.rakuten.co.jp/hgc/0ea62065.34400275.0ea62066.204f04c0/a26103176848_" + A8_RAKUTEN_MAT.replace("+", "_")
          + "?pc=" + _q(url, safe="") + "&m=" + _q(url, safe=""))
    return f"https://rpx.a8.net/svt/ejp?a8mat={A8_RAKUTEN_MAT}&rakuten=y&a8ejpredirect=" + _q(hb, safe="")


def travel_ads(keys):
    from urllib.parse import quote
    rows = []
    for name, kw in (D.TRAVEL_GOODS[k] for k in keys):
        amz = f"https://www.amazon.co.jp/s?k={quote(kw)}&tag={D.AMAZON_TAG}"
        rak = a8_rakuten(f"https://search.rakuten.co.jp/search/mall/{quote(kw)}/")
        rows.append(f'<li><span>{e(name)}</span><span class="ad-links"><a href="{e(amz)}" target="_blank" rel="sponsored noopener">Amazon</a>'
                    f'<a href="{e(rak)}" target="_blank" rel="sponsored noopener">楽天市場</a></span></li>')
    return f"""<aside class="ads" aria-labelledby="h-ads"><h2 id="h-ads"><span class="pr">PR</span>韓国旅行の持ち物</h2>
  <p class="muted">旅行の準備に役立つ物です。リンク先はAmazonと楽天市場の検索結果です。</p>
  <ul class="ad-list">{''.join(rows)}</ul>{A8_RAKUTEN_PIXEL}
  <p class="muted">このコーナーは広告（アフィリエイト）です。Amazonのアソシエイトとして、当サイトは適格販売により収入を得ています。</p>
</aside>"""


def trip_inline(body, spots):
    """見出しの直前に Trip.com の小さな PR リンクを1行ずつ挟む"""
    for mark, key in spots:
        label, url = D.TRIP_LINKS[key]
        line = (f'<p class="trip-pr"><span class="pr">PR</span><a href="{e(url)}" target="_blank" '
                f'rel="sponsored noopener">{e(label)}</a></p>\n')
        for target in (f'<section aria-labelledby="{mark}">', f'<section><h2>{mark}</h2>'):
            if target in body:
                body = body.replace(target, line + target, 1)
                break
        else:
            raise SystemExit(f"Trip.com の挟む場所が見つからない: {mark}")
    return body


def layout(file, title, desc, body, head_html, extra_head=""):
    if file in D.TRIP_PAGES:
        body = trip_inline(body, D.TRIP_PAGES[file])
    if file in D.AD_PAGES:
        body = body + travel_ads(D.AD_PAGES[file])
    nav = "".join(f'<li><a href="{f}"{" aria-current=\"page\"" if f == file else ""}>{e(n)}</a></li>' for f, n in NAV)
    canonical = BASE + ("" if file == "index.html" else file)
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><link rel="apple-touch-icon" href="/icons/paradise.png"><link rel="icon" type="image/png" href="/icons/paradise.png">{analytics_tag(adsense=False)}
<title>{e(title)}</title>
<meta name="apple-mobile-web-app-title" content="パラダイスシティ">
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE}og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
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
  <p><a href="https://mocchima.com/privacy.html">プライバシーポリシー</a> / <a href="https://mocchima.com/about.html">運営者情報・お問い合わせ</a></p>
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


def info_card(title, text, status, src, checked, dark=False, link=None):
    more = f'<p><a class="btn" href="{e(link[0])}">{e(link[1])}</a></p>' if link else ""
    return f"""<div class="card{' dark' if dark else ''}">
  <div class="badge-row">{badge(status)}</div>
  <h3>{e(title)}</h3>
  <p>{e(text)}</p>
  {more}
  {source(src, checked)}
</div>"""


def item_cards(items):
    return '<div class="cards">' + "".join(info_card(d["title"], d["text"], d["status"], d["src"], d["checked"], link=d.get("link")) for d in items) + "</div>"


def redirect_page(to, label):
    return f"""<!doctype html><html lang="ja"><head><meta charset="utf-8"><title>{e(label)}へ移動しました</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{BASE}{e(to)}">
<meta http-equiv="refresh" content="0; url={e(to)}"></head>
<body><p><a href="{e(to)}">{e(label)}へ移動しました</a></p></body></html>"""


def blog_articles():
    """一覧に出す記事（内容をメインページへ移した記事を除き、日付の新しい順）"""
    return sorted((a for a in D.ARTICLES if not a.get("moved_to")), key=lambda a: a["date"], reverse=True)


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
    return item_cards(items)


# ---------- pages ----------

def page_index():
    tile_html = '<nav class="tiles" aria-label="主なページ">' + "".join(
        f'<a class="tile" href="{u}"><strong>{e(t)}</strong><span>{e(sub)}</span></a>' for u, t, sub in TILES) + "</nav>"
    head = f"""<header class="hero gutter">
  <img src="img/pegasus.jpg" alt="" width="1050" height="1400">
  <div class="inner">
    <p class="eyebrow">PARADISE CITY · INCHEON</p>
    <h1><span class="nb">日本人向け</span><span class="nb">パラダイスシティ</span><br><span class="nb">カジノの</span><span class="nb">攻略ガイド</span></h1>
    <p class="lead">韓国・仁川のパラダイスシティのカジノに行く人のために、到着から帰るまでの流れ、お得情報、食事券、宿泊プランを、公式情報と体験談を分けて紹介します。</p>
    <p class="photo-credit">写真：パラダイスシティのホテルのロビーにある金色のペガサス像（運営者撮影）・最終更新 {D.UPDATED}</p>
  </div>
</header>"""
    current = "".join(campaign_card(c) for c in D.CAMPAIGNS["current"])
    updates = "".join(f'<li><time datetime="{d}">{d}</time>{e(t)}</li>' for d, t in D.UPDATES)
    steps = "".join(f'<li><a href="start.html#{st["id"]}"><strong>STEP {n}</strong> {e(st["title"])}</a></li>' for n, st in enumerate(D.START_STEPS, 1))
    deals = "".join(f'<li><a href="perks.html#h-deals">{e(d["title"])}</a></li>' for d in D.DEALS[:6])
    posts = "".join(f'<li><time datetime="{a["date"]}">{a["date"]}</time><a href="article-{a["slug"]}.html">{e(a["title"])}</a></li>' for a in blog_articles()[:5])
    body = f"""
{tile_html}
<section aria-labelledby="h-start"><h2 id="h-start">初めての人は「最初にやること」から</h2>
  <ol class="steps-mini">{steps}</ol>
  <p><a class="btn primary" href="start.html">最初にやることを見る</a></p>
</section>
<div class="duo">
<section aria-labelledby="h-deals"><h2 id="h-deals">お得情報</h2>
  <ul class="linklist">{deals}</ul>
  <p><a class="btn" href="perks.html">お得情報をすべて見る</a></p>
</section>
<section aria-labelledby="h-blog"><h2 id="h-blog">体験談ブログ</h2>
  <ul class="updates">{posts}</ul>
  <p><a class="btn" href="articles.html">ブログをすべて見る</a></p>
</section>
</div>
{LEGEND}
<section aria-labelledby="h-cafe9"><h2 id="h-cafe9">カジノの中のご飯「Cafe 9」</h2>
  <p>カジノのフロアの中にあるレストランです。食事券の出し方や使える枚数は、Cafe 9 のページにまとめています。</p>
  {photos(D.CAFE9_PHOTOS, wide=True)}
  <p><a class="btn" href="cafe9.html">Cafe 9 のページを見る</a></p>
</section>
<section aria-labelledby="h-camp"><h2 id="h-camp">最新のキャンペーン</h2>
  <div class="cards">{current}</div>
  <p><a class="btn" href="campaigns.html">過去のキャンペーンも見る</a></p>
</section>
<section aria-labelledby="h-stay"><h2 id="h-stay">おすすめの宿泊</h2>
  <div class="cards">
    <div class="card"><div class="badge-row">{badge('exp')}</div><h3>{D.HOTEL['name']}（{D.HOTEL['name_en']}）</h3>
      <p>運営者が泊まったホテルの1つです。無料宿泊のキャンペーンや、過去の宿泊プランは宿泊プランのページで比べられます。</p>
      <p><a class="btn primary" href="stay.html">宿泊プランを比べる</a></p></div>
    <figure class="card" style="padding:0;overflow:hidden;margin:0"><img src="img/hyatt-room.jpg" alt="ハイアット リージェンシー 仁川の客室" loading="lazy" width="1000" height="1333" style="aspect-ratio:4/3;object-fit:cover"></figure>
  </div>
</section>
<section aria-labelledby="h-guide"><h2 id="h-guide">カジノ初心者ガイド</h2>
  {rule_cards(D.ENTRY_RULES[:2] + D.TABLE_RULES[:2], with_meta=False)}
  <p><a class="btn" href="guide.html">ルールとゲームの説明を見る</a></p>
</section>
<section aria-labelledby="h-faq"><h2 id="h-faq">よくある質問</h2>
  {faq_block(D.FAQ[:5])}
  <p><a class="btn" href="faq.html">質問をすべて見る</a></p>
</section>
<section aria-labelledby="h-new"><h2 id="h-new">更新情報</h2>
  <ul class="updates">{updates}</ul>
</section>"""
    index_search("トップ", "index.html", "パラダイスシティ カジノガイド", "パラダイスシティ カジノ お得 宿泊 食事券 初心者 ルール 予算 キャンペーン アクセス")
    return layout("index.html", "パラダイスシティ カジノ攻略ガイド｜日本人向け 最初にやること・お得情報・食事券・宿泊【2026年版】",
                  "韓国・仁川のパラダイスシティのカジノに行く人向けの攻略ガイド。到着から帰るまでの流れ、新規会員のクーポン、Cafe 9 の食事券、無料宿泊、空港へのシャトルバスを、公式情報と体験談を区別して紹介します。", body, head)


def page_start():
    out = []
    for n, st in enumerate(D.START_STEPS, 1):
        inner = item_cards(st["items"]) if st["items"] else ""
        if st.get("games"):
            inner += '<div class="cards">' + "".join(
                f'<a class="card" href="guide.html#game-{g["slug"]}" style="text-decoration:none;color:inherit"><h3>{e(g["name"])}</h3><p>{e(g["summary"])}</p></a>' for g in GAMES) + "</div>"
        alert = f'<p class="notice alert"><strong>{e(st["alert"])}</strong></p>' if st.get("alert") else ""
        links = '<div class="btns">' + "".join(f'<a class="btn" href="{e(u)}">{e(t)}</a>' for u, t in st.get("links", [])) + "</div>"
        out.append(f'<section aria-labelledby="{st["id"]}"><h2 id="{st["id"]}"><span class="step-no">STEP {n}</span>{e(st["title"])}</h2>{alert}{inner}{links}</section>')
        for it in st["items"]:
            index_search("最初にやること", f"start.html#{st['id']}", it["title"], it["text"])
    steps = "".join(f"""<div class="card"><div class="badge-row"><strong>{i}</strong>{badge(x['status'])}</div><h3>{e(x['title'])}</h3><p>{e(x['text'])}</p>{source(x['src'], x['checked'])}</div>"""
                    for i, x in enumerate(D.SIGNUP_STEPS, 1))
    checks = "".join(f"<li>{e(c)}</li>" for c in D.BOOKING_CHECKS)
    toc = "".join(f'<li><a href="#{st["id"]}">STEP {n}　{e(st["title"])}</a></li>' for n, st in enumerate(D.START_STEPS, 1))
    body = f"""
{LEGEND}
<nav class="toc" aria-label="このページの目次"><ol>{toc}<li><a href="#h-member">会員登録と宿泊予約</a></li></ol></nav>
{''.join(out)}
<section aria-labelledby="h-member"><h2 id="h-member">会員登録と宿泊予約の流れ</h2>
  <div class="notice alert"><strong>予約の前に必ず確認：</strong><p>キャンペーンや宿泊特典には、予約の期限が決まっていることがあります。たとえば「宿泊の3日前までに手続きが必要」なプランもありました。ただし、これはすべてのプランに共通するルールではありません。プランごとに条件を確認してください。</p></div>
  <div class="cards">{steps}</div>
  <h3>予約・変更・キャンセルの注意点</h3>
  <ul class="checklist">{checks}</ul>
  <div class="btns"><a class="btn primary" href="{D.SOURCES['official_reserve'][1]}" target="_blank" rel="noopener">公式予約ページ</a><a class="btn" href="{D.SOURCES['official_faq'][1]}" target="_blank" rel="noopener">公式FAQ</a></div>
</section>"""
    for x in D.SIGNUP_STEPS:
        index_search("最初にやること", "start.html#h-member", x["title"], x["text"])
    index_search("最初にやること", "start.html#h-member", "予約の期限・キャンセル", " ".join(D.BOOKING_CHECKS))
    return layout("start.html", "パラダイスシティ カジノで最初にやること｜入場・チップ交換・食事・帰り方の流れ",
                  "初めてパラダイスシティのカジノに行く人向けに、入場と会員登録、キャッシャーでのチップ交換、ゲームの選び方、Cafe 9 の食事、帰りの交換、空港への移動を順番に説明します。",
                  body, page_head("最初にやること", "カジノに着いてから帰るまでを、6つのステップで順番に案内します。"))


def page_access():
    secs = []
    for sec in D.ACCESS:
        pics = photos(D.SHUTTLE_PHOTOS) if sec.get("photos") else ""
        secs.append(f'<section aria-labelledby="{sec["id"]}"><h2 id="{sec["id"]}">{e(sec["title"])}</h2>{pics}{item_cards(sec["items"])}</section>')
        for it in sec["items"]:
            index_search("アクセス", f"access.html#{sec['id']}", it["title"], it["text"])
    body = f"""
{LEGEND}
{''.join(secs)}
<p class="notice">時間や乗り場は変わることがあります。行く前に、ホテルやパラダイスシティのスタッフに確認してください。</p>"""
    return layout("access.html", "パラダイスシティのアクセス｜仁川空港との無料シャトルバス・乗り場・時間・タクシー",
                  "仁川空港とパラダイスシティの行き来をまとめました。第1ターミナル行き無料シャトルバスの乗り場（地下）と時間（5時〜23時・20分おき）、深夜のタクシー、ホテルからカジノまでの時間。",
                  body, page_head("アクセス", "仁川空港との行き来を、ここにまとめています。"))


def page_cafe9():
    c = D.CAFE9
    slots = "".join(f'<div class="card"><div class="badge-row">{badge("check")}</div><h3>{e(x)}</h3><p class="muted">情報を集めています。分かり次第ここに載せます。</p></div>' for x in c["slots"])
    body = f"""
{LEGEND}
<section aria-labelledby="h-about"><h2 id="h-about">Cafe 9 ってどこ？</h2>{item_cards(c["about"])}</section>
<section aria-labelledby="h-meal"><h2 id="h-meal">食事券の使い方</h2>{item_cards(c["meal"])}</section>
<section aria-labelledby="h-menu"><h2 id="h-menu">実際に食べたご飯</h2>{photos(D.CAFE9_PHOTOS, wide=True)}{item_cards(c["menu"])}
  <p><a class="btn" href="article-cafe9.html">体験談ブログの記事を読む</a></p></section>
<section aria-labelledby="h-wait"><h2 id="h-wait">これから確認すること</h2><div class="cards">{slots}</div></section>"""
    for key in ("about", "meal", "menu"):
        for it in c[key]:
            index_search("Cafe 9", f"cafe9.html#h-{key}", it["title"], it["text"])
    return layout("cafe9.html", "パラダイスシティ カジノの Cafe 9｜食事券の出し方・使える枚数・リセット時間",
                  "パラダイスシティのカジノの中のレストラン「Cafe 9」の攻略情報。食事券の発券機の場所、1日に使える枚数、午前6時のリセット、実際に食べた丼ものセットを、公式情報と体験談を分けて紹介します。",
                  body, page_head("Cafe 9", "カジノの中のレストランと、食事券の使い方をまとめています。"))


def page_game(g):
    sections = "".join(f"<section><h2>{e(h)}</h2><p>{e(t)}</p></section>" for h, t in g["detail"])
    body = f"""
<div class="article-body">
  <p>{e(g['summary'])}</p>
  {item_cards(g['notes']) if g['notes'] else ''}
  {sections}
  <p class="notice">ルールや最低ベットは台や時期で変わります。座る前に、テーブルの案内やディーラーに確認してください。</p>
  <p><a class="btn" href="guide.html#h-games">ゲーム一覧に戻る</a></p>
</div>"""
    return layout(f"game-{g['slug']}.html", f"{g['name']}のルール｜パラダイスシティ カジノ初心者ガイド", g["summary"], body, page_head(g["name"], g["summary"]))


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
<section aria-labelledby="h-p"><h2 id="h-p">会員カード・会員特典</h2>
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
        index_search("お得情報", "perks.html#h-p", p["title"], p["text"])
    for d in D.DEALS:
        index_search("お得情報", "perks.html#h-deals", d["title"], d["text"])
    return layout("perks.html", "パラダイスシティ カジノのお得情報｜新規会員クーポン・ポイント・食事券",
                  "パラダイスシティのカジノのお得情報。新規会員のクーポン、ポイントの使い道、会員ランク、ほかのカジノのランクの持ち込みを、公式情報とユーザー提供情報に分けて紹介します。",
                  body, page_head("お得情報・会員特典", "新規会員のクーポン、ポイント、会員ランクなど、会員と特典の情報をまとめています。"))


def page_guide():
    body = f"""
{LEGEND}
<p class="notice alert"><strong>ここに書いているのは初心者向けの基本の案内です。</strong>ゲームやテーブルごとに細かいルールが違うことがあります。施設の規則と、現地スタッフの指示を優先してください。</p>
<section aria-labelledby="h-b"><h2 id="h-b">カジノの基本ルール</h2>
  {basics_cards()}
</section>
<section aria-labelledby="h-in"><h2 id="h-in">カジノのマナー（入場するとき）</h2>
  {rule_cards(D.ENTRY_RULES)}
</section>
<section aria-labelledby="h-t"><h2 id="h-t">テーブルゲームの基本</h2>
  {rule_cards(D.TABLE_RULES)}
  {source('users', D.UPDATED)}
</section>
{games_sections()}
<section aria-labelledby="h-floor"><h2 id="h-floor">フロアの並びとおすすめのテーブル</h2>
  <p>{badge('exp')} 入口のすぐ手前にクラップスとルーレット、まっすぐ進むとブラックジャックやポーカー、その先にたくさんのバカラの台があります。運営者の体感では、サレンダーができるブラックジャックがいちばんチップが減りにくかったです。</p>
  <p><a class="btn" href="article-floor-tables.html">体験談を読む</a></p>
</section>
{budget_sections()}
<section aria-labelledby="h-next"><h2 id="h-next">次に読む</h2>
  <div class="btns"><a class="btn primary" href="start.html">最初にやること（到着から帰るまで）</a></div>
</section>"""
    for g in GAMES:
        index_search("初心者ガイド", f"guide.html#game-{g['slug']}", g["name"], g["summary"] + " " + " ".join(n["text"] for n in g["notes"]))
    for r in D.ENTRY_RULES + D.TABLE_RULES:
        index_search("初心者ガイド", "guide.html", r["title"], r["text"])
    for b in D.BASICS:
        index_search("初心者ガイド", "guide.html#h-b", b["title"], b["text"])
    bd = D.BUDGET
    index_search("初心者ガイド", "guide.html#h-budget", "最低ベットと予算の目安", bd["text_min_bet"] + " " + bd["text_budget"])
    index_search("初心者ガイド", "guide.html#h-sim", "予算シミュレーター", "予算 最低ベット 資金管理 シミュレーター")
    return layout("guide.html", "パラダイスシティ カジノ初心者ガイド｜入場ルールとテーブルのマナー",
                  "初めてパラダイスシティのカジノに行く人向けに、パスポート・服装・撮影禁止などの入場ルールと、テーブルゲームでのマナーをイラストつきで解説します。",
                  body, page_head("カジノ初心者ガイド", "基本のルール、マナー、ゲーム別の説明、予算の目安をまとめました。"))


def games_sections():
    def card(g):
        notes = "".join(f'<li>{badge(n["status"])} {e(n["text"])}</li>' for n in g["notes"])
        more = (f'<p><a class="btn" href="game-{g["slug"]}.html">くわしいルールを見る</a></p>' if g.get("detail")
                else '<p class="muted">くわしい解説は準備中です。</p>')
        return (f'<div class="card" id="game-{g["slug"]}"><h3>{e(g["name"])}</h3><p>{e(g["summary"])}</p>'
                + (f'<ul class="notes">{notes}</ul>' if notes else "") + more + "</div>")
    table = "".join(card(g) for g in GAMES if g["kind"] == "table")
    machine = "".join(card(g) for g in GAMES if g["kind"] == "machine")
    return f"""<section aria-labelledby="h-games"><h2 id="h-games">ゲーム別ルール</h2>
  <p class="notice">一般的な遊び方の短い説明と、パラダイスシティで運営者が確かめたことです。ルールや最低ベットは台や時期で変わります。</p>
  <div class="cards">{table}</div>
</section>
<section aria-labelledby="h-slots"><h2 id="h-slots">スロット</h2>
  <div class="cards">{machine}</div>
</section>"""


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
    arts = blog_articles()
    cats = sorted({a["category"] for a in arts})
    chips = '<div class="chips" role="group" aria-label="カテゴリー"><button class="chip" type="button" data-filter="all" aria-pressed="true">すべて</button>' + "".join(
        f'<button class="chip" type="button" data-filter="{e(c)}" aria-pressed="false">{e(c)}</button>' for c in cats) + "</div>"
    cards = "".join(f"""<a class="card" data-category="{e(a['category'])}" href="article-{a['slug']}.html" style="text-decoration:none;color:inherit">
  <div class="badge-row">{badge(a['status'])}<span class="muted">{e(a['category'])} ・ {a['date']}</span></div>
  <h3>{e(a['title'])}</h3><p class="muted">{e(a['lead'])}</p></a>""" for a in arts)
    body = f"""
<section aria-labelledby="h-list"><h2 id="h-list">記事一覧（新しい順）</h2>
  {chips}
  <div class="cards">{cards}</div>
</section>"""
    return layout("articles.html", "パラダイスシティ 体験談ブログ｜訪問記録・宿泊レポート・食事の感想",
                  "パラダイスシティのカジノに2026年だけで8回通った運営者の体験談や、ハイアット リージェンシー 仁川の宿泊レポートなどの記事一覧です。",
                  body, page_head("体験談ブログ", "運営者が実際に行ったときの記録です。新しい記事が上に出ます。体験談は個人の感想で、公式情報ではありません。"))


def page_article(a):
    def table(rows):
        head, *rest = rows
        return ('<div class="table-wrap fit"><table><thead><tr>' + "".join(f"<th>{e(c)}</th>" for c in head) + "</tr></thead><tbody>"
                + "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rest) + "</tbody></table></div>")
    sections = "".join(f"<section><h2>{e(b[0])}</h2><p>{e(b[1])}</p>{table(b[2]) if len(b) > 2 else ''}</section>" for b in a["body"])
    pics = {"hotel": photos(), "cafe9": photos(D.CAFE9_PHOTOS, wide=True), "trip-2611": photos(D.TRIP_2611_PHOTOS), "shuttle": photos(D.SHUTTLE_PHOTOS)}.get(a.get("photos"), "")
    body = f"""
<div class="article-body">
  <div class="badge-row">{badge(a['status'])}<span class="muted">{e(a['category'])} ・ {a['date']}</span></div>
  <p>{e(a['lead'])}</p>
  {pics}
  {sections}
  <p class="notice">この記事は{D.STATUS_LABEL[a['status']]}です。公式情報ではありません。条件は変わることがあるので、最新の情報は公式サイトで確認してください。</p>
  <p><a class="btn" href="articles.html">ブログの一覧に戻る</a></p>
</div>"""
    index_search("体験談ブログ", f"article-{a['slug']}.html", a["title"], a["lead"] + " " + " ".join(b[1] for b in a["body"]))
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
        "index.html": page_index(), "start.html": page_start(), "perks.html": page_perks(), "articles.html": page_articles(),
        "cafe9.html": page_cafe9(), "stay.html": page_stay(), "guide.html": page_guide(), "faq.html": page_faq(),
        "campaigns.html": page_campaigns(), "access.html": page_access(),
    }
    for g in GAMES:
        if g.get("detail"):
            pages[f"game-{g['slug']}.html"] = page_game(g)
    moved = {}
    for a in D.ARTICLES:
        if a.get("moved_to"):
            moved[f"article-{a['slug']}.html"] = redirect_page(a["moved_to"], "まとめたページ")
        else:
            pages[f"article-{a['slug']}.html"] = page_article(a)
    pages["search.html"] = page_search()
    for name, to in REDIRECTS.items():
        moved[name] = redirect_page(to, "新しいページ")
    for name, text in {**pages, **moved}.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(text)
    with open(os.path.join(OUT, "search.json"), "w", encoding="utf-8") as f:
        json.dump(SEARCH, f, ensure_ascii=False)
    urls = [n for n in pages if n != "search.html"]
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
                + "".join(f"  <url><loc>{BASE}{'' if n == 'index.html' else n}</loc><lastmod>{D.UPDATED}</lastmod></url>\n" for n in urls)
                + "</urlset>\n")
    print(f"built paradise-city: {len(pages)} pages, {len(moved)} redirects, {len(SEARCH)} search entries")


if __name__ == "__main__":
    main()
