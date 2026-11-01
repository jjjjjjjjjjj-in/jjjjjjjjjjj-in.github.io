# 公開中のサイトの一覧。新しいサイトを作ったらここに1件足して `python3 src/build.py` を実行する。
# path: このドメインの中の場所（末尾 /）。sitemap: そのサイトのサイトマップ（なければ None）
SITES = [
    dict(
        path="doomsday-guide/",
        name="ドゥームズデイ予習ガイド",
        name_en="Doomsday Watch Guide",
        desc="『アベンジャーズ／ドゥームズデイ』の前に観るべきMCU作品を、重要度つきの視聴順チェックリストで整理。",
        desc_en="What to watch before Avengers: Doomsday, with a story-order checklist and importance ratings.",
        en_path="doomsday-guide/en/",
        sitemap="doomsday-guide/sitemap.xml",
        updated="2026-11-01",
    ),
    dict(
        path="doomsday-guide/films/iron-man.html",
        name="アイアンマン完全ガイド",
        name_en="Iron Man Complete Guide",
        desc="映画だけでは分かりにくい人向けに、『アイアンマン』のあらすじ・顔アイコンつき相関図・用語・Q&Aをやさしく解説。",
        desc_en="Iron Man explained for anyone who finds it hard to follow: story, character map, key terms and Q&A.",
        en_path="doomsday-guide/en/films/iron-man.html",
        sitemap=None,  # ドゥームズデイ予習ガイドのサイトマップに入っている
        updated="2026-11-01",
    ),
    dict(
        path="paradise-city/",
        name="パラダイスシティ カジノガイド",
        desc="韓国・仁川のパラダイスシティのカジノを日本人向けに解説。宿泊プラン、食事券、入場ルール、予算の目安。",
        sitemap="paradise-city/sitemap.xml",
        updated="2026-11-01",
    ),
]
