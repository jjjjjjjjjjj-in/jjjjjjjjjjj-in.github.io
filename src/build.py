"""ドメインのトップ（入口ページ・サイトマップ・robots.txt）を書き出す。

使い方: python3 src/build.py
"""
import html
import os
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SRC)
sys.path.insert(0, SRC)

from sites import SITES  # noqa: E402

BASE_URL = "https://jjjjjjjjjjj-in.github.io/"

# Google Search Console（URLプレフィックス https://jjjjjjjjjjj-in.github.io/）の HTMLタグの content の値
GOOGLE_SITE_VERIFICATION = "qCmKqyCaXzHH3V_hEqM1lhQKy9os6X5RIR2zZmw4fZc"

# Google アナリティクスの測定ID（全サイト共通）。各サイトの全ページにも同じタグを入れる
GA_MEASUREMENT_ID = "G-KDFL8GPPRZ"
POLICY_UPDATED = "2026-10-31"


def analytics_tag():
    if not GA_MEASUREMENT_ID:
        return ""
    return (f'\n<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>\n'
            f"<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA_MEASUREMENT_ID}');</script>")


SITE_NAME = "もっちぃま"

# モノトーン。黒の帯、白い地、グレーの線。サイトのタイルは全部同じ大きさにそろえる
STYLE = """<style>
:root { --bg: #ffffff; --ink: #111111; --surface: #f4f4f4; --line: #d9d9d9; --muted: #5c5c5c; --on-ink: #ffffff; --soft: #bdbdbd; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: "Zen Kaku Gothic New", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", sans-serif; line-height: 1.7;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
.wrap { max-width: 880px; margin: 0 auto; padding-block: 32px 56px; display: grid; gap: 24px; }
header { background: var(--ink); color: var(--on-ink); border-radius: 12px; padding: clamp(22px, 5vw, 36px); }
h1 { margin: 0; font-size: clamp(30px, 8vw, 46px); font-weight: 900; letter-spacing: .04em; line-height: 1.2; }
header p { margin: 8px 0 0; color: var(--soft); }
ul.cards { list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); grid-auto-rows: 1fr; }
.card { display: flex; }
.card a { flex: 1; display: grid; grid-template-rows: auto auto 1fr; gap: 6px; padding: 18px; background: var(--surface); border: 1px solid var(--line); border-radius: 10px; color: var(--ink); text-decoration: none; min-height: 170px; }
.card a:hover, .card a:focus-visible { border-color: var(--ink); outline: none; }
.card .lang { font-size: 11.5px; font-weight: 700; letter-spacing: .08em; color: var(--muted); border: 1px solid var(--line); border-radius: 99px; padding: 0 8px; width: fit-content; }
.card h2 { margin: 0; font-size: 18px; font-weight: 900; line-height: 1.4; }
.card p { margin: 0; color: var(--muted); font-size: 14px; font-weight: 400; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
a { color: var(--ink); font-weight: 700; }
.policy h2 { background: var(--ink); color: var(--on-ink); border-radius: 6px; padding: 8px 14px; font-size: 18px; margin: 28px 0 8px; }
.policy h3 { font-size: 16px; margin: 16px 0 4px; }
.policy p, .policy li { margin: 6px 0; }
footer { font-size: 12.5px; color: var(--muted); border-top: 1px solid var(--line); padding-top: 14px; }
</style>"""

e = html.escape


def index_html():
    tiles = []
    for site in SITES:
        tiles.append((site["path"], site["name"], site["desc"], "日本語", "ja"))
        if site.get("en_path"):
            tiles.append((site["en_path"], site["name_en"], site["desc_en"], "English", "en"))
    cards = "".join(f"""
    <li class="card"><a href="{e(path)}" lang="{lang}"><span class="lang">{label}</span><h2>{e(name)}</h2><p>{e(desc)}</p></a></li>"""
                    for path, name, desc, label, lang in tiles)
    verify = f'\n<meta name="google-site-verification" content="{e(GOOGLE_SITE_VERIFICATION)}">' if GOOGLE_SITE_VERIFICATION else ""
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">{analytics_tag()}
<title>{SITE_NAME}</title>
<meta name="description" content="映画、旅行、本などのテーマごとに、知っておくと役立つ情報や楽しみ方をまとめたガイドサイトです。">
<link rel="canonical" href="{BASE_URL}">{verify}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap">
{STYLE}
</head>
<body>
<div class="wrap">
  <header>
    <h1>{SITE_NAME}</h1>
    <p>映画、旅行、本などのテーマごとに、知っておくと役立つ情報や楽しみ方をまとめています。</p>
  </header>
  <ul class="cards">{cards}
  </ul>
  <footer>個人が運営する非公式のファンサイトです。各サイトにはアフィリエイト広告（PR）を含むページがあります。<a href="privacy.html">プライバシーポリシー</a></footer>
</div>
</body>
</html>
"""


def privacy_html():
    """全サイト共通のプライバシーポリシー（アクセス解析・広告・外部送信についての説明）"""
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">{analytics_tag()}
<title>プライバシーポリシー｜{SITE_NAME}</title>
<meta name="description" content="{SITE_NAME}と、その中の各サイトでのアクセス解析・広告・情報の外部送信についての説明です。">
<link rel="canonical" href="{BASE_URL}privacy.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap">
{STYLE}
</head>
<body>
<div class="wrap">
  <header><h1>プライバシーポリシー</h1><p>{SITE_NAME}（{BASE_URL} 以下の全サイト）</p></header>
  <article class="policy">
  <p>このページでは、当サイトでのアクセス解析と広告の仕組み、利用者の情報の扱いについて説明します。最終更新：{POLICY_UPDATED}</p>

  <h2>アクセス解析（Googleアナリティクス）</h2>
  <p>当サイトでは、サイトがどれくらい見られているかを知り、内容を良くするために、Google LLC の「Googleアナリティクス」を使っています。Googleアナリティクスは Cookie などを使って、次のような情報を Google に送ります。個人の名前など、個人を直接特定する情報は含みません。</p>
  <ul>
    <li>見たページのURL、見た日時、どのページから来たか</li>
    <li>使っている端末・ブラウザ・OSの種類、画面の大きさ、言語</li>
    <li>IPアドレスからおおまかに分かる地域</li>
  </ul>
  <p>送られた情報は Google のプライバシーポリシーに基づいて扱われます。詳しくは <a href="https://policies.google.com/technologies/partner-sites?hl=ja" rel="noopener">Google のサービスを使用するサイトやアプリから収集した情報の Google による使用</a> をご覧ください。データの収集を止めたい場合は、<a href="https://tools.google.com/dlpage/gaoptout?hl=ja" rel="noopener">Googleアナリティクス オプトアウト アドオン</a> を使うか、ブラウザの設定で Cookie を無効にしてください。</p>

  <h2>情報の外部送信について</h2>
  <ul>
    <li><strong>送信先</strong>：Google LLC（Googleアナリティクス）</li>
    <li><strong>送信される情報</strong>：上の「アクセス解析」に書いた情報</li>
    <li><strong>目的</strong>：アクセス数や利用状況の把握と、サイトの改善</li>
  </ul>

  <h2>広告（アフィリエイト）について</h2>
  <p>当サイトは、Amazonアソシエイト・プログラム（Amazon.co.jp・Amazon.com）、もしもアフィリエイト（楽天市場）、A8.net などのアフィリエイト広告を使っています。広告のリンクを押して移動した先のサイトでは、購入などの成果を確かめるために、各サービスが Cookie などを使うことがあります。当サイトから利用者の名前や連絡先を広告サービスに送ることはありません。</p>
  <p>Amazonのアソシエイトとして、当サイトは適格販売により収入を得ています。</p>

  <h2>ブラウザに保存する情報</h2>
  <p>チェックリストの「観た」の記録などは、利用者のブラウザの中だけに保存されます。当サイトや外部に送られることはありません。</p>

  <h2>免責事項</h2>
  <p>当サイトの情報はできるだけ正確にするよう努めていますが、内容を保証するものではありません。リンク先のサイトでのトラブルについて、当サイトは責任を負いかねます。</p>

  <h2 id="en">Privacy policy (English)</h2>
  <div lang="en">
  <p><strong>Analytics.</strong> This site and every site under {BASE_URL} use Google Analytics by Google LLC to understand how many people visit and to improve the content. Google Analytics uses cookies and sends Google the pages you view, the referring page, your device, browser and language, and an approximate location derived from your IP address. It does not include your name or other directly identifying information. See <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">how Google uses information from sites that use its services</a>. You can opt out with the <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener">Google Analytics opt-out add-on</a> or by disabling cookies in your browser.</p>
  <p><strong>Ads.</strong> This site uses affiliate programs including Amazon Associates (Amazon.co.jp and Amazon.com), Moshimo Affiliate (Rakuten) and A8.net. Their sites may use cookies to confirm purchases made after you follow a link. As an Amazon Associate, this site earns from qualifying purchases.</p>
  <p><strong>Data stored in your browser.</strong> Your checklist progress stays in your browser and is never sent to this site or anyone else.</p>
  </div>
  </article>
  <footer><a href="./">トップページに戻る</a></footer>
</div>
</body>
</html>
"""


def sitemap_index():
    """各サイトのサイトマップをまとめたもの。Google にはこれ1つを登録すれば、全サイトが伝わる"""
    entries = "".join(f"  <sitemap><loc>{BASE_URL}{s['sitemap']}</loc><lastmod>{s['updated']}</lastmod></sitemap>\n"
                      for s in SITES if s.get("sitemap"))
    latest = max(s["updated"] for s in SITES)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"  <sitemap><loc>{BASE_URL}sitemap-top.xml</loc><lastmod>{latest}</lastmod></sitemap>\n"
            + entries + "</sitemapindex>\n")


def main():
    def write(name, text):
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(text)

    latest = max(s["updated"] for s in SITES)
    write("index.html", index_html())
    write("privacy.html", privacy_html())
    write("sitemap.xml", sitemap_index())
    write("sitemap-top.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          f"  <url><loc>{BASE_URL}</loc><lastmod>{latest}</lastmod></url>\n"
          f"  <url><loc>{BASE_URL}privacy.html</loc><lastmod>{POLICY_UPDATED}</lastmod></url>\n</urlset>\n")
    # robots.txt はドメインのトップにあるものだけが有効。全サイトのサイトマップをここで伝える
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n")
    write(".nojekyll", "")
    print(f"built top page with {len(SITES)} site(s)")


if __name__ == "__main__":
    main()
