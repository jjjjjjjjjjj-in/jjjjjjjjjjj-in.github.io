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

e = html.escape


def index_html():
    cards = "".join(f"""
    <li class="card">
      <h2><a href="{e(s["path"])}">{e(s["name"])}</a></h2>
      <p>{e(s["desc"])}</p>
      <p class="en"><a href="{e(s["en_path"])}" lang="en">{e(s["name_en"])}</a> — <span lang="en">{e(s["desc_en"])}</span></p>
    </li>""" if s.get("en_path") else f"""
    <li class="card">
      <h2><a href="{e(s["path"])}">{e(s["name"])}</a></h2>
      <p>{e(s["desc"])}</p>
    </li>""" for s in SITES)
    verify = f'\n<meta name="google-site-verification" content="{e(GOOGLE_SITE_VERIFICATION)}">' if GOOGLE_SITE_VERIFICATION else ""
    return f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>映画・エンタメの予習ガイド集</title>
<meta name="description" content="映画やドラマをもっと楽しむための予習ガイドをまとめています。">
<link rel="canonical" href="{BASE_URL}">{verify}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;700;900&display=swap">
<style>
:root {{ --bg: #ffffff; --surface: #f5f7fb; --line: #d5deea; --fg: #0b1d36; --muted: #556a88; --green: #0e3b2b; --navy: #0b2546; --gold: #f2c94c; --link: #1d5fb0; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--bg); color: var(--fg); font-family: "Zen Kaku Gothic New", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo", sans-serif; line-height: 1.7;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }}
.wrap {{ max-width: 760px; margin: 0 auto; padding-block: 32px 56px; display: grid; gap: 24px; }}
header {{ background: var(--green); color: #fff; border-radius: 12px; border-left: 6px solid var(--gold); padding: clamp(20px, 5vw, 32px); }}
h1 {{ margin: 0; font-size: clamp(24px, 6vw, 34px); font-weight: 900; text-wrap: balance; }}
header p {{ margin: 6px 0 0; color: #d5e6dc; }}
ul {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 12px; }}
.card {{ background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 16px; }}
.card h2 {{ margin: 0 0 4px; font-size: 19px; }}
.card p {{ margin: 0; color: var(--muted); font-size: 14.5px; }}
.card .en {{ margin-top: 6px; }}
a {{ color: var(--link); font-weight: 700; }}
footer {{ font-size: 12.5px; color: var(--muted); border-top: 1px solid var(--line); padding-top: 14px; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>映画・エンタメの予習ガイド集</h1>
    <p>観る前に知っておくと、もっと楽しくなるガイドをまとめています。</p>
  </header>
  <ul>{cards}
  </ul>
  <footer>個人が運営する非公式のファンサイトです。各サイトにはアフィリエイト広告（PR）を含むページがあります。</footer>
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
    write("sitemap.xml", sitemap_index())
    write("sitemap-top.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          f"  <url><loc>{BASE_URL}</loc><lastmod>{latest}</lastmod></url>\n</urlset>\n")
    # robots.txt はドメインのトップにあるものだけが有効。全サイトのサイトマップをここで伝える
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n")
    write(".nojekyll", "")
    print(f"built top page with {len(SITES)} site(s)")


if __name__ == "__main__":
    main()
