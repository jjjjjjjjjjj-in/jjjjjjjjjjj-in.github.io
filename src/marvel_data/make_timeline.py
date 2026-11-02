"""運営者から受け取った年表（timeline_raw.txt）を、データ（timeline.json）に変換する。
元の文は original に残し、直したところは note に理由を書く。
作品は slug（src/mcu/titles.py のキー）で持つ。slug がない作品（ワンショットなど）は label だけ。
"""
import json, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
ABBR = {
    "リミックス": "guardians-vol2", "エターナルズ": "eternals", "MOM": "multiverse-of-madness", "ブラックパンサー": "black-panther",
    "ドクスト": "doctor-strange", "ダークワールド": "thor-dark-world", "シャンチー": "shang-chi", "ソー": "thor",
    "バトルロイヤル": "thor-ragnarok", "ガーディアンズ": "guardians-of-the-galaxy", "FA": "captain-america-first-avenger",
    "WF": "wakanda-forever", "ワンダヴィジョン": "wandavision", "ミズマーベル": "ms-marvel", "F&W": "falcon-and-winter-soldier",
    "アイアンマン2": "iron-man-2", "ロキ": "loki-s1", "WS": "winter-soldier", "アイアンマン3": "iron-man-3", "アントマン": "ant-man",
    "A&W": "ant-man-and-the-wasp", "キャプテンマーベル": "captain-marvel", "シビルウォー": "civil-war", "アイアンマン": "iron-man",
    "ムーンナイト": "moon-knight", "AOU": "age-of-ultron", "インクレハルク": "incredible-hulk", "ブラックウィドウ": "black-widow",
    "アベンジャーズ": "avengers", "ホークアイ": "hawkeye", "HC": "spider-man-homecoming", "インフィニティウォー": "infinity-war",
    "エンドゲーム": "endgame", "NWH": "spider-man-no-way-home", "FFH": "spider-man-far-from-home", "シーハルク": "she-hulk",
}
LABEL_ONLY = {"エージェントカーター": "エージェント・カーター（ドラマ）", "俺は王だ": "ワンショット『俺は王だ』（短編）"}
# 「〜本編」の行の作品
MAIN = {"キャプテンマーベル": "captain-marvel", "アイアンマン": "iron-man", "アベンジャーズ": "avengers", "ダークワールド": "thor-dark-world",
        "アイアンマン3": "iron-man-3", "ウィンターソルジャー": "winter-soldier", "ガーディアンズ": "guardians-of-the-galaxy",
        "リミックス": "guardians-vol2", "AOU": "age-of-ultron", "アントマン": "ant-man", "シビルウォー": "civil-war",
        "ブラックウィドウ": "black-widow", "ブラックパンサー": "black-panther", "HC": "spider-man-homecoming", "バトルロイヤル": "thor-ragnarok",
        "A＆W": "ant-man-and-the-wasp", "インフィニティウォー": "infinity-war", "ワンダヴィジョン": "wandavision", "シャンチー": "shang-chi",
        "FFH": "spider-man-far-from-home", "エターナルズ": "eternals", "NWH": "spider-man-no-way-home", "MOM": "multiverse-of-madness",
        "ホークアイ": "hawkeye", "ムーンナイト": "moon-knight", "WF": "wakanda-forever", "ミズマーベル": "ms-marvel",
        "ラブ＆ザンダー": "love-and-thunder", "ウェアウルフバイナイト": "werewolf-by-night", "ホリデースペシャル": "guardians-holiday-special",
        "アイアンハート": "ironheart", "クアントマニア": "quantumania", "ガーディアンズvol.3": "guardians-vol3",
        "シークレットインベージョン": "secret-invasion", "マーベルズ": "the-marvels", "アガサオールアロング": "agatha-all-along",
        "BNW": "brave-new-world", "ザンダーボルツ": "thunderbolts", "BND": "spider-man-brand-new-day"}
# 作品ガイドのない作品の「〜本編」「〜 EP」の行
MAIN_LABEL = {"ワンラストキル本編": "パニッシャー：ワン・ラスト・キル", "ワンダーマン EP": "ドラマ『ワンダーマン』"}
# 作品名がない行に、内容から作品をあてる（運営者のデータを補う）
EXTRA = {"インフィニティストーン誕生": ["guardians-of-the-galaxy"], "1988年:ピータークイル失踪": ["guardians-of-the-galaxy"],
         "1990年代後半:サノスがガモーラを引き取る": ["infinity-war"], "ハワードがエキスポに新元素の構図を隠す": ["iron-man-2"],
         "ストラッカーがワンダとピエトロに人体実験を行う": ["winter-soldier", "age-of-ultron"], "アイアムグルート S1EP1": ["i-am-groot-1"],
         "アイアムグルートその他のEP": ["i-am-groot-1", "i-am-groot-2"], "エンドゲーム5年後": ["endgame"],
         "F＆W EP1〜5": ["falcon-and-winter-soldier"], "ジャックラッセル誕生": ["werewolf-by-night"],
         "ウェイドがアース616を訪れる": ["deadpool-and-wolverine"], "サンダーボルツ14ヶ月後": ["thunderbolts"], "F＆W EP6": ["falcon-and-winter-soldier"], "シーハルクEP": ["she-hulk"]}
# 直したところ（元の文 → 直した文, 理由）
FIX = {
    "2026年秋:ストレンジがカマータージに辿り着く(ドクスト)": ("2016年秋", "ストレンジがカマー・タージに辿り着く", "「2026年」は「2016年」の書き間違いと考えられるため直しました（前後の出来事が2016〜2017年）。"),
    "1973年:9月15日:ハワードがエキスポに新元素の構図を隠す": ("1973年9月15日", "ハワードがエキスポの模型に新元素の構造を隠す", "日付の区切りを整えました。作品名がなかったので『アイアンマン2』（父の映像の場面）にあてました。"),
    "1992年:ウンジョブ殺害、キルモンガーが孤児に(ブラックパンサー)": ("1992年", "ンジョブが殺害され、キルモンガーが孤児に", "人名の表記を「ンジョブ」に統一しました。"),
    "2010年春ソーが地球に落とされジェーン達と出会う(ソー)": ("2010年春", "ソーが地球に落とされジェーン達と出会う", "日付の区切り（:）を補いました。"),
    "2027年春〜秋:ザンダーボルツ本編": ("2027年春〜秋", "サンダーボルツ* 本編", "作品名を正式な表記（サンダーボルツ*）に直しました。"),
    "2018年:ウェイドがアース616を訪れる": ("2018年", "ウェイドがEarth-616を訪れる", "表記を「Earth-616」にそろえました。作品名がなかったので『デッドプール＆ウルヴァリン』（ハッピーの面接を受ける場面）にあてました。"),
    "2025年秋:ラブ＆ザンダー本編": ("2025年秋", "ソー：ラブ＆サンダー 本編", "作品名を正式な表記（ラブ＆サンダー）に直しました。"),
}
CHECK = {
    "2007年:インリー死亡(シャンチー)": "作中の描写（シャン・チーが7歳のころ）から計算すると年がずれる可能性があります。確認中です。",
    "1996年:ランドールが事故死(ムーンナイト)": "前後の行と年の順番が入れかわっています（1990年代後半の出来事の後に1996年）。確認中です。",
    "2000年代:ブダペストの戦い(ブラックウィドウ)": "時期がはっきりしないため、確認中です。",
    "2018年:バッキーが洗脳から解放(ブラックパンサー)": "『ブラックパンサー』のおまけ映像の出来事です。時期は確認中です。",
    "1971年11月24日:ロキが飛行機をジャック(ロキ)": "ドラマ『ロキ』の中で語られる、別の時間の流れの出来事です（Earth-616本編の出来事とは区別してください）。",
    "1600年〜1800年の間:ジャックラッセル誕生": "作品名がなかったので『ウェアウルフ・バイ・ナイト』にあてました。作中で年ははっきり語られないため、確認中です。",
    "セレスティアル誕生(リミックス)": "宇宙の始まりにかかわる出来事で、作中で語られる伝説です。",
}
ERAS = ["太古", "先史時代", "西暦", "1900年代", "2000年代以降"]
items, era = [], None
for raw in open(os.path.join(HERE, "timeline_raw.txt"), encoding="utf-8"):
    line = raw.strip()
    if not line:
        continue
    if line.startswith("●"):
        era = line[1:]; assert era in ERAS, era; continue
    when, text = "", line
    m = re.match(r"^(紀元前\d+年|\d{3,4}年(?:代)?(?:[^:：]*?)?)[:：](.*)$", line)
    if m:
        when, text = m.group(1), m.group(2)
    works, labels = [], []
    pm = re.search(r"\(([^()]+)\)$", text)
    body = text
    if pm:
        body = text[:pm.start()].strip()
        for a in re.split(r"[、,]", pm.group(1)):
            a = a.replace(" ", "").replace("＆", "&")
            if a in ABBR: works.append(ABBR[a])
            elif a in LABEL_ONLY: labels.append(LABEL_ONLY[a])
    # 複数の作品が並ぶ行（例: 消滅の行）
    for a in re.findall(r"\(([^()]+)\)", body):
        a2 = a.replace("＆", "&")
        if a2 in ABBR and ABBR[a2] not in works: works.append(ABBR[a2])
    body_clean = re.sub(r"\(([^()]+)\)", r"（\1）", body)
    main = False
    mm = re.match(r"^(.+?)本編$", body)
    if mm and mm.group(1).strip() in MAIN:
        works = [MAIN[mm.group(1).strip()]] + works; main = True
    for k, v in EXTRA.items():
        if k in line:
            works += [w for w in v if w not in works]
    if body.startswith(("F＆W EP", "シーハルクEP")):
        main = True
    for k, v in MAIN_LABEL.items():
        if body.startswith(k):
            labels.append(v); main = True
    note, status = "", "ok"
    if line in FIX:
        when, body_clean, note = FIX[line]; status = "fixed"
        if "本編" in body_clean: main = True
    if line in CHECK:
        note = CHECK[line]; status = "check" if "確認中" in note else "info"
    items.append(dict(id=f"e{len(items)+1:03d}", era=era, when=when, text=body_clean, works=works, labels=labels,
                      main=main, status=status, note=note, original=line))
json.dump(dict(updated="2026-11-02", source="運営者提供の年表（2026-11-02）をもとに作成。作品の時期はマーベル・スタジオ公式の年表の本を参考に、運営者が整理したもの。", eras=ERAS, items=items),
          open(os.path.join(HERE, "timeline.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(items), "items;", sum(1 for i in items if not i["works"] and not i["labels"]), "without work")
for i in items:
    if not i["works"] and not i["labels"]: print("  no work:", i["original"])
