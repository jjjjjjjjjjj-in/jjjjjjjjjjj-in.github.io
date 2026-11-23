"""関西二郎系マップ（/jiro/）を書き出す。
中身は src/jiro/ の index.html・shops.js（店のデータ）・ads.js（広告の設定）。
直すのは src/jiro/ の中だけ。使い方: PYTHONUTF8=1 python src/jiro/build.py
"""
import os, shutil, datetime

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(os.path.dirname(SRC)), "jiro")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in ("index.html", "shops.js", "ads.js"):
        shutil.copyfile(os.path.join(SRC, name), os.path.join(OUT, name))
    photos = os.path.join(SRC, "photos")
    if os.path.isdir(photos):
        shutil.copytree(photos, os.path.join(OUT, "photos"), dirs_exist_ok=True)
    today = datetime.date.today().isoformat()
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        f"  <url><loc>https://mocchima.com/jiro/</loc><lastmod>{today}</lastmod></url>",
        "</urlset>",
        "",
    ]
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print("built /jiro/")


if __name__ == "__main__":
    main()
