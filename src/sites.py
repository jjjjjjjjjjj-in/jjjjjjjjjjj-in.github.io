# 公開中のサイトの一覧。新しいサイトを作ったらここに1件足して `python3 src/build.py` を実行する。
# path: このドメインの中の場所（末尾 /）。sitemap: そのサイトのサイトマップ（なければ None）
# folder: トップページで入れるフォルダ（FOLDERS の key）。英語版（en_path）は folder_en のフォルダに入る。
# フォルダの中は、このリストの順に並ぶ（上にあるものほど上）。

# トップページのフォルダ。中身が1つだけのフォルダは、フォルダのページを作らずにそのサイトへ直接つなぐ
FOLDERS = [
    dict(key="marvel", path="marvel/", lang="ja", name="マーベル映画紹介",
         desc="『アベンジャーズ／ドゥームズデイ』の予習ガイドと、マーベル映画を1本ずつやさしく解説する作品ガイド。"),
    dict(key="marvel-en", path="marvel/en/", lang="en", name="Marvel Movie Guides",
         desc="A watch guide for Avengers: Doomsday, plus guides that explain Marvel films one at a time. All in English."),
    dict(key="paradise", path=None, lang="ja", name="パラダイスシティ",
         desc="韓国・仁川のパラダイスシティのカジノを日本人向けに解説。宿泊プラン、食事券、入場ルール、予算の目安。"),
]

SITES = [
    dict(
        path="doomsday-guide/", folder="marvel", folder_en="marvel-en",
        name="ドゥームズデイ予習ガイド",
        name_en="Doomsday Watch Guide",
        desc="『アベンジャーズ／ドゥームズデイ』の前に観るべきMCU作品を、重要度つきの視聴順チェックリストで整理。",
        desc_en="What to watch before Avengers: Doomsday, with a story-order checklist and importance ratings.",
        en_path="doomsday-guide/en/",
        sitemap="doomsday-guide/sitemap.xml",
        updated="2026-11-01",
    ),
    dict(
        path="captain-america-first-avenger/", folder="marvel", folder_en="marvel-en",
        name="キャプテン・アメリカ／ザ・ファースト・アベンジャー 完全ガイド",
        name_en="Captain America: The First Avenger Complete Guide",
        desc="1940年代、弱い青年スティーブがキャプテン・アメリカになるまで。あらすじ・顔アイコンつき相関図・用語・Q&Aをやさしく解説。",
        desc_en="How frail Steve Rogers becomes Captain America in the 1940s: story, character map, key terms and Q&A.",
        en_path="captain-america-first-avenger/en/",
        sitemap="captain-america-first-avenger/sitemap.xml",
        updated="2026-11-01",
    ),
    dict(
        path="captain-marvel/", folder="marvel", folder_en="marvel-en",
        name="キャプテン・マーベル 完全ガイド",
        name_en="Captain Marvel Complete Guide",
        desc="1995年、記憶をなくした戦士ヴァースが本当の自分と出会うまで。あらすじ・顔アイコンつき相関図・用語・Q&Aをやさしく解説。",
        desc_en="Vers, a warrior with no memory, finds out who she really is in 1995: story, character map, key terms and Q&A.",
        en_path="captain-marvel/en/",
        sitemap="captain-marvel/sitemap.xml",
        updated="2026-11-01",
    ),
    dict(
        path="iron-man/", folder="marvel", folder_en="marvel-en",
        name="アイアンマン完全ガイド",
        name_en="Iron Man Complete Guide",
        desc="映画だけでは分かりにくい人向けに、『アイアンマン』のあらすじ・顔アイコンつき相関図・用語・Q&Aをやさしく解説。",
        desc_en="Iron Man explained for anyone who finds it hard to follow: story, character map, key terms and Q&A.",
        en_path="iron-man/en/",
        sitemap="iron-man/sitemap.xml",
        updated="2026-11-01",
    ),
    dict(
        path="paradise-city/", folder="paradise",
        name="パラダイスシティ カジノガイド",
        desc="韓国・仁川のパラダイスシティのカジノを日本人向けに解説。宿泊プラン、食事券、入場ルール、予算の目安。",
        sitemap="paradise-city/sitemap.xml",
        updated="2026-11-01",
    ),
]
