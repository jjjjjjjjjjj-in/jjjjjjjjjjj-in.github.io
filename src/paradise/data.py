# パラダイスシティ情報サイトのデータ。ここを書き換えて `python3 src/paradise/build.py` を実行すると、全ページに反映される。
#
# 情報には必ず次を付ける:
#   status: "official"（公式情報）/ "user"（ユーザー提供情報）/ "exp"（運営者の体験談）/ "check"（要確認）/ "past"（過去の情報）
#   src:    SOURCES のキー（出典）
#   checked: 確認日（YYYY-MM-DD）
# 公式に確認できないことを推測で書かない。終わったキャンペーンは current に置かず archive に移す。

UPDATED = "2026-10-31"
OPERATOR_VISITS = "2026年に8回訪問"

SOURCES = {
    "official_casino": ("パラダイスシティ公式：カジノ運営案内", "https://www.p-city.com/front/casino/operation?language=JA"),
    "official_notice": ("パラダイスシティ公式：お知らせ（カジノの利用対象）", "https://www.p-city.com/front/notice/detail?N_SEQ=5306"),
    "official_faq_dress": ("パラダイスシティ公式FAQ（服装など）", "https://p-city.com/front/faq?language=JA&mCode=000004"),
    "official_faq": ("パラダイスシティ公式FAQ", "https://www.p-city.com/front/faq?language=JA&mCode=000002"),
    "official_reserve": ("パラダイスシティ公式予約ページ", "https://www.p-city.com/front/reservation"),
    "official_top": ("パラダイスシティ公式サイト", "https://www.p-city.com/"),
    "official_x": ("パラダイスシティ公式X（日本語・過去の投稿）", "https://x.com/Paradisecity_J/status/1613465332714471425"),
    "official_welcome": ("公式予約ページ：PARADISE CASINO NEW MEMBERSHIP WELCOME OFFER", "https://www.p-city.com/front/reservation/reservationStep1To2?RP_SEQ=7905"),
    "official_thrill": ("公式予約ページ：Experience the thrill of Paradise Casino", "https://www.p-city.com/front/reservation/reservationStep1To2?RP_SEQ=13067"),
    "official_membership": ("パラダイスシティ公式：カジノメンバーシップ案内", "https://www.p-city.com/front/memnotice/membership?Type=CASINO"),
    "official_tier": ("パラダイスシティ公式：カジノ会員ランク（Red）", "https://www.p-city.com/front/memnotice/membershipView?M_TYPE=CasinoRed"),
    "official_match": ("パラダイスシティ公式：カジノ会員ランクのマッチング", "https://www.p-city.com/front/memnotice/casinoMatch"),
    "official_members_day": ("公式予約ページ：パラダイス・メンバーズデー", "https://www.p-city.com/front/reservation/reservationStep1To2?RP_SEQ=12380"),
    "official_casino_pkg": ("公式予約ページ：カジノ会員つき宿泊パッケージ", "https://www.p-city.com/front/reservation/reservationStep1To2?RP_SEQ=4366"),
    "official_overview": ("パラダイスシティ公式：カジノ紹介", "https://www.p-city.com/front/casino/overview"),
    "official_cimer": ("パラダイスシティ公式：スパ「シメール」", "https://www.p-city.com/front/cimer/facility"),
    "official_map": ("パラダイスシティ公式：フロアマップ", "https://www.p-city.com/front/contents/pcity/location?Type=FLOOR"),
    "rakuten": ("楽天トラベル（パラダイスシティ周辺の宿泊プラン）", "https://hotel.travel.rakuten.co.jp/overseas/grmPlanList.do?f_no=139096"),
    "ota": ("海外ホテル予約サイトの掲載情報", ""),
    "articles": ("複数の旅行・攻略ブログ（公式ではない）", ""),
    "operator": ("運営者の体験（" + "2026年に8回訪問" + "）", ""),
    "users": ("ユーザー提供情報", ""),
}

STATUS_LABEL = {
    "official": "公式情報",
    "user": "ユーザー提供",
    "exp": "体験談",
    "check": "要確認",
    "past": "過去の情報",
}

# カジノの基本情報（トップ・初心者ガイド・FAQで使う）
BASICS = [
    dict(key="hours", title="営業時間", text="24時間・年中無休。", status="official", src="official_casino", checked="2026-10-31"),
    dict(key="who", title="入場できる人", text="外国人専用。パスポートを持っている満19歳以上の外国人と、海外永住権（居住証明書）を持つ人が対象です。", status="official", src="official_notice", checked="2026-10-31"),
    dict(key="passport", title="必要なもの", text="パスポート（国籍の確認に使います）。原本を持って行きましょう。", status="official", src="official_casino", checked="2026-10-31"),
    dict(key="fatf", title="入場制限", text="FATF（金融活動作業部会）が非協力国と定めた国の国籍の人は、入場が制限される場合があります。", status="official", src="official_casino", checked="2026-10-31"),
    dict(key="dress", title="服装", text="カジュアルな服装で入場できます。ただし、極端に肌を出すタンクトップ、ショートパンツ、ジャージ、サンダル、見えるタトゥーなどは入場を断られることがあります。", status="official", src="official_faq_dress", checked="2026-10-31"),
    dict(key="yen", title="日本円", text="公式Xで「カジノは日本円で大丈夫」と案内されています。ただし過去の投稿なので、両替の方法やレートは現地で確認してください。", status="check", src="official_x", checked="2026-10-31"),
    dict(key="photo", title="撮影", text="カジノ内での写真・動画撮影は原則禁止とされています。スマートフォンでの撮影も避けましょう。公式ページでの明記は確認できていません。", status="user", src="users", checked="2026-10-31"),
]

# 初心者ガイド：入場とテーブルのルール（施設の規則と現地スタッフの指示が優先）
ENTRY_RULES = [
    dict(icon="passport", title="パスポートの原本を持参", text="外国人の本人確認に必要です。コピーや写真では入れないと考えておきましょう。", status="official", src="official_casino", checked="2026-10-31"),
    dict(icon="camera", title="カジノ内で撮影しない", text="写真・動画の撮影は原則禁止です。スマホでの撮影も避けてください。", status="user", src="users", checked="2026-10-31"),
    dict(icon="shirt", title="服装に気をつける", text="サンダル・ショートパンツ・露出の多い服・見えるタトゥーは入場を断られることがあります。", status="official", src="official_faq_dress", checked="2026-10-31"),
]
TABLE_RULES = [
    dict(icon="phone", title="スマホをテーブルより上に上げない", text="撮影や不正防止のため、テーブルの上でスマホを持ち上げることが制限される場合があります。"),
    dict(icon="hand", title="合図があるまでチップに触らない", text="ディーラーから「触ってよい」という合図があるまで、チップには触れないようにしましょう。"),
    dict(icon="stack", title="賭けたチップを動かさない・足さない", text="一度賭けたチップを勝手に動かしたり、あとから追加したりしないでください。"),
    dict(icon="dealer", title="ディーラーの指示に従う", text="ゲームの進行中は、ディーラーの指示が最優先です。"),
    dict(icon="ask", title="分からなければ始める前に聞く", text="ルールが分からないときは、プレイを始める前にスタッフに確認しましょう。"),
]

# 予算の目安（運営者の体験談。固定の金額ではない）
BUDGET = dict(
    min_bet_yen=3000,
    text_min_bet="最低ベットは約3,000円相当だった（ゲーム・テーブル・時期・為替で変わります）。",
    text_budget="実際に遊ぶなら、最低でも20,000円くらいはあったほうがよい。ただし20,000円で十分な余裕があるとは限らない。",
    status="exp", src="operator", checked="2026-10-31",
)

# お得情報まとめ（トップページのいちばん上に出す。日本人の旅行者向け）
DEALS = [
    dict(title="新規会員になると、もらえるクーポン", text="カジノの会員に新しく登録すると、30,000ウォン分の「ラッキーベッティングクーポン」と20,000ウォン分の「マシンチケット」がもらえると公式に案内されています。1人1回だけです。現金ではなく、ゲームに使う券です。", status="official", src="official_membership", checked="2026-10-31"),
    dict(title="会員登録は無料・パスポートだけ", text="カジノ入口のメンバーシップデスクで、パスポートを見せて登録します。対象は満19歳以上の外国人と、海外永住権を持つ人です。", status="official", src="official_membership", checked="2026-10-31"),
    dict(title="貯まったポイントは食事や買い物にも", text="遊ぶと貯まる「カジノポイント」は、カジノやパラダイスシティの施設で現金のように使えると公式に案内されています（使えない場所や条件があります）。", status="official", src="official_membership", checked="2026-10-31"),
    dict(title="Cafe 9 のご飯は食事券で", text="カジノの中のレストラン「Cafe 9」は、会員でなくても使えるカジノのメイン食堂と紹介されています。食事券は Cafe 9 の右側にある発券機で出せ、無料の券は24時間で使えなくなるという情報があります。", status="check", src="articles", checked="2026-10-31"),
    dict(title="ランクが上がると割引やラウンジ", text="会員ランクは過去24か月のポイントをもとに、3か月ごとに見直されます。上のランクになると、レストランやスパの割引、ラウンジ、リムジンの送迎などが使えると公式に案内されています。", status="official", src="official_tier", checked="2026-10-31"),
    dict(title="他のカジノの会員ランクを持ち込める", text="ほかのカジノの会員ランクを持っている人向けに、ランクを合わせてもらえる制度（カジノ・マッチ）が公式ページに掲載されています。対象のカジノや条件は公式ページで確認してください。", status="check", src="official_match", checked="2026-10-31"),
    dict(title="空港からの無料シャトルバス", text="仁川空港の第1・第2ターミナルとパラダイスシティの間に、予約なしで乗れる無料シャトルがあると紹介されています。車で5分ほどです。運行の間隔は紹介によって20〜60分と違うので、現地で確認してください。", status="check", src="articles", checked="2026-10-31"),
    dict(title="ポイントの注意", text="ポイントは他の人に譲れず、有効期限があります。もらったクーポンやポイントの使い道は、使う前にデスクで確認しましょう。", status="official", src="official_membership", checked="2026-10-31"),
]

# Cafe 9（カジノの中のレストラン）の写真。運営者撮影。
CAFE9_PHOTOS = [
    ("img/cafe9-butadon.jpg", "Cafe 9 の豚丼セット。炒飯、スープ、キムチつき", "豚丼セット"),
    ("img/cafe9-gyudon.jpg", "Cafe 9 の牛丼セット。スープ、漬物、アイスティーつき", "牛丼セット"),
]

# パラダイスシティの施設（公式）
FACILITIES = [
    dict(title="パラダイスホテル＆リゾート", text="カジノと同じ建物にある、パラダイスシティのメインホテルです。電話 +82-32-729-2000。", status="official", src="official_top", checked="2026-10-31"),
    dict(title="アート・パラディソ", text="58室すべてがスイートの、大人向けのブティックホテルです。電話 +82-1833-8880。", status="official", src="official_top", checked="2026-10-31"),
    dict(title="ハイアット リージェンシー 仁川 パラダイスシティ", text="空港側にあるハイアットのホテルです。電話 +82-1577-2010。", status="official", src="official_top", checked="2026-10-31"),
    dict(title="スパ「シメール」", text="韓国のチムジルバンをテーマにしたスパです。ふだんは10:00〜21:00ですが、季節によって休みや時間の変更があります。", status="official", src="official_cimer", checked="2026-10-31"),
    dict(title="ワンダーボックス", text="屋内のファミリー向けテーマパークです。家族で行くときに。", status="official", src="official_top", checked="2026-10-31"),
    dict(title="カジノ", text="韓国でいちばん大きい外国人専用カジノと公式に紹介されています。24時間営業です。", status="official", src="official_overview", checked="2026-10-31"),
]

# 特典（食事券・ドリンク券など）
PERKS = [
    dict(title="食事券は1日最大2枚まで", text="食事券は1日に2枚まで使えるという情報があります。会員ランクや条件で変わる可能性があります。", status="user", src="users", checked="2026-10-31"),
    dict(title="食事券の回数は午前6時にリセット", text="食事券を使える回数は、毎日午前6時にリセットされるという情報があります。", status="user", src="users", checked="2026-10-31"),
    dict(title="会員カード（メンバーシップ）", text="パスポートがあれば作れます。ランクは過去24か月のポイントで、3か月ごとに見直されます。", status="official", src="official_membership", checked="2026-10-31"),
    dict(title="ポイントで食事券・ドリンク券", text="貯まったポイントで食事券やドリンク券に交換できるという情報があります（例：1,000ポイントごと）。交換のレートは時期で変わる可能性があります。", status="check", src="articles", checked="2026-10-31"),
    dict(title="新規会員向けの特典", text="公式予約ページに「PARADISE CASINO NEW MEMBERSHIP WELCOME OFFER」というプランが掲載されています。内容・期間・条件は公式ページで確認してください。", status="check", src="official_welcome", checked="2026-10-31"),
]
# これから情報を集める特典の枠（分かったら PERKS に移す）
PERK_SLOTS = ["ドリンク券の利用条件", "会員ランクごとの特典", "宿泊特典", "期間限定キャンペーン"]

# 宿泊・キャンペーン。current は公式に確認できた「今のもの」だけ。終わったものや過去の情報は archive。
CAMPAIGNS = dict(
    current=[
        dict(
            name="PARADISE CASINO NEW MEMBERSHIP WELCOME OFFER", kind="カジノ新規会員向けプラン",
            nights="要確認", days="要確認", perks="要確認（公式ページで確認）", conditions="要確認",
            book_from="", book_to="", stay_from="", stay_to="",
            note="2026-10-31 に公式予約ページへの掲載を確認しました。内容と期間はまだ確認できていません。",
            status="check", src="official_welcome", checked="2026-10-31", url="https://www.p-city.com/front/reservation/reservationStep1To2?RP_SEQ=7905",
        ),
        dict(
            name="Experience the thrill of Paradise Casino", kind="カジノ体験プラン",
            nights="要確認", days="要確認", perks="要確認（公式ページで確認）", conditions="要確認",
            book_from="", book_to="", stay_from="", stay_to="",
            note="2026-10-31 に公式予約ページへの掲載を確認しました。内容と期間はまだ確認できていません。",
            status="check", src="official_thrill", checked="2026-10-31", url="https://www.p-city.com/front/reservation/reservationStep1To2?RP_SEQ=13067",
        ),
        dict(
            name="パラダイス・メンバーズデー", kind="会員向けの期間限定プラン（7日間限定と掲載）",
            nights="要確認", days="要確認", perks="要確認（公式ページで確認）", conditions="要確認",
            book_from="", book_to="", stay_from="", stay_to="",
            note="2026-10-31 に公式予約ページへの掲載を確認しました。「7日間限定」と書かれていますが、日付はまだ確認できていません。",
            status="check", src="official_members_day", checked="2026-10-31", url="https://www.p-city.com/front/reservation/reservationStep1To2?RP_SEQ=12380",
        ),
        dict(
            name="カジノ会員つき宿泊パッケージ", kind="宿泊＋カジノ会員のパッケージ",
            nights="要確認", days="要確認", perks="要確認（公式ページで確認）", conditions="要確認",
            book_from="", book_to="", stay_from="", stay_to="",
            note="2026-10-31 に公式予約ページへの掲載を確認しました。内容と期間はまだ確認できていません。",
            status="check", src="official_casino_pkg", checked="2026-10-31", url="https://www.p-city.com/front/reservation/reservationStep1To2?RP_SEQ=4366",
        ),
    ],
    archive=[
        dict(
            name="ハイアット リージェンシー 仁川 宿泊プラン（カジノ会員向け）", kind="宿泊プラン",
            nights="最大4泊", days="日曜〜金曜の平日",
            perks="Market Caféの朝食券（1室・1泊につき1枚）／Swell Loungeのドリンク券（1予約につき1枚）／同伴者の朝食がカジノ会員カード提示で15％割引という情報あり",
            conditions="ホテルのチェックイン前にカジノ会員登録が必要とされていた／ダブルルームのほうがツインルームより予約枠が多い場合があった",
            book_from="", book_to="", stay_from="", stay_to="",
            note="過去に利用された宿泊プランの情報です。今も同じ内容で使えるとは限りません。",
            status="past", src="users", checked="2026-10-31", url="",
        ),
        dict(
            name="ゲーム条件付き宿泊キャンペーン", kind="ゲーム条件付き宿泊",
            nights="1泊〜（例：木〜土の3泊）", days="平日・土曜で条件が違う",
            perks="宿泊",
            conditions="平日1泊：10万円相当／土曜1泊：30万円相当／木〜土の3泊：合計50万円相当・12時間のプレイ。チップ購入と4時間のプレイが条件（1泊の場合）。クラップス、シックボー、スタンディングバカラ、麻雀、テキサスホールデムなどは対象外。チェックインは15時以降。ゲーム時間はチェックイン当日の午前6時から計算。",
            book_from="", book_to="", stay_from="", stay_to="",
            note="過去のキャンペーンの例です。今のキャンペーンではありません。",
            status="past", src="users", checked="2026-10-31", url="",
        ),
    ],
)

HOTEL = dict(
    name="ハイアット リージェンシー 仁川",
    name_en="Hyatt Regency Incheon",
    facts=[
        dict(text="チェックイン15:00〜、チェックアウト11:00まで。", status="check", src="ota", checked="2026-10-31"),
        dict(text="仁川空港の第1ターミナルとの間に無料シャトルがあると紹介されています。時刻表は変わることがあるので、ホテルに確認してください。", status="check", src="ota", checked="2026-10-31"),
        dict(text="館内の朝食会場「Market Café」と「Swell Lounge」が、過去の宿泊プランの特典に使われていました。", status="past", src="users", checked="2026-10-31"),
    ],
    photos=[
        ("img/hyatt-lobby.jpg", "ハイアット リージェンシー 仁川のレセプション前。白い大理石の大きなアーチが目印", "ロビー"),
        ("img/hyatt-room.jpg", "客室。木目の壁と大きなベッド、窓際の一人掛けソファ", "客室"),
        ("img/hyatt-bath.jpg", "バスルーム。バスタブとガラスで仕切られた洗面台", "バスルーム"),
    ],
)

# 予約・会員登録の流れ
SIGNUP_STEPS = [
    dict(title="パスポートを用意する", text="カジノの入場と会員登録の両方に使います。原本を持って行きましょう。", status="official", src="official_casino", checked="2026-10-31"),
    dict(title="カジノの会員登録をする", text="カジノ入口近くのカウンターで、パスポートを見せて登録します。会員カードは任意とする紹介もありますが、宿泊特典を使うなら登録が必要になるプランがありました。", status="check", src="articles", checked="2026-10-31"),
    dict(title="宿泊プランを選んで予約する", text="公式予約ページか、楽天トラベルなどの予約サイトで予約します。プランごとに条件が違うので、予約前に条件をよく読みましょう。", status="official", src="official_reserve", checked="2026-10-31"),
    dict(title="特典の受け取り方を確認する", text="「チェックイン前に会員登録が必要」など、順番が決まっているプランがありました。チェックインの前に確認しましょう。", status="past", src="users", checked="2026-10-31"),
]
BOOKING_CHECKS = [
    "予約の締め切り：プランによっては「宿泊の3日前までに予約」などの期限がある場合があります。すべてのプランに共通のルールではないので、プランごとに確認してください。",
    "事前予約が必要か：特典やキャンペーンの中には、事前の申し込みや予約が必要なものがあります。",
    "会員登録のタイミング：チェックイン前のカジノ会員登録が必要なプランがありました。",
    "部屋のタイプ：同じプランでも、ダブルとツインで予約枠の数が違うことがありました。",
    "変更・キャンセル：キャンセル料や変更の期限はプランごとに違います。予約画面の規約を必ず確認してください。",
]

# よくある質問
FAQ = [
    ("新規会員になると何がもらえる？", "30,000ウォン分のラッキーベッティングクーポンと、20,000ウォン分のマシンチケットがもらえると公式に案内されています。1人1回だけです。", "official", "official_membership"),
    ("カジノの中で食事はできる？", "カジノの中のレストラン「Cafe 9」で食べられます。食事券は Cafe 9 の右側の発券機で出せるという情報があります（要確認）。", "check", "articles"),
    ("カジノに入場するために必要なものは？", "パスポートが必要です。満19歳以上の外国人が対象です。", "official", "official_notice"),
    ("パスポートは必要？", "必要です。国籍の確認に使うので、原本を持って行きましょう。", "official", "official_casino"),
    ("カジノ内で写真撮影はできる？", "原則禁止とされています。スマホでの撮影も避けてください。公式ページでの明記は確認できていないため、現地の案内に従ってください。", "user", "users"),
    ("初心者でも遊べる？", "遊べます。始める前にこのサイトの初心者ガイドを読み、分からないことはプレイを始める前にスタッフに聞きましょう。", "exp", "operator"),
    ("最低いくら持っていけばいい？", "運営者の体験では、最低ベットは約3,000円相当で、20,000円くらいはあったほうがよいと感じました。ただし金額はゲーム・テーブル・時期・為替で変わり、20,000円で余裕があるとは限りません。負けてもよい金額だけにしましょう。", "exp", "operator"),
    ("食事券は何枚まで使える？", "1日最大2枚までという情報があります。会員ランクや条件で変わる可能性があるため、要確認です。", "user", "users"),
    ("食事券は何時にリセットされる？", "午前6時にリセットされるという情報があります。要確認です。", "user", "users"),
    ("ホテルの宿泊特典はどうすれば受けられる？", "プランごとに条件が違います。過去には「チェックイン前にカジノ会員登録が必要」なプランがありました。予約前にプランの条件を確認してください。", "check", "official_reserve"),
    ("カジノ会員登録はいつすればいい？", "宿泊特典を使う予定なら、ホテルにチェックインする前に済ませておくのが安全です（過去のプランでそうした条件がありました）。", "past", "users"),
    ("宿泊予約は何日前までにすればいい？", "プランによって違います。「3日前まで」などの期限があるプランもありますが、共通のルールではありません。予約ページで確認してください。", "check", "official_reserve"),
    ("カジノの営業時間は？", "24時間・年中無休です。", "official", "official_casino"),
    ("日本円は利用できる？", "公式Xで「日本円で大丈夫」と案内されています。両替の方法やレートは現地で確認してください。", "check", "official_x"),
    ("チップはどこで交換できる？", "カジノ内のキャッシャー（両替窓口）で交換できると紹介されています。テーブルで交換できる場合もあるという紹介もありますが、公式には確認できていないため要確認です。", "check", "articles"),
]

# 体験談・記事（カテゴリー別に表示）
ARTICLES = [
    dict(
        slug="operator-8-visits", title="2026年に8回通って分かった、パラダイスシティのリアル", category="体験談", date="2026-10-31",
        lead="運営者が2026年に8回パラダイスシティのカジノに通って分かったことを、初めて行く人向けにまとめました。",
        body=[
            ("予算の感覚", "最低ベットは約3,000円相当のテーブルが多い印象でした。遊ぶなら最低でも20,000円くらいは持っておきたいですが、20,000円では数回負けると終わってしまうこともあります。「負けてもいい金額」を最初に決めておくのがいちばん大事です。"),
            ("食事券", "食事券は1日2枚まで使え、午前6時に回数がリセットされるという案内でした。夜遅くに食べると翌朝6時にまた使えるので、時間を意識すると無駄がありません（条件は人やランクで変わる可能性があります）。"),
            ("テーブルでのマナー", "スマホをテーブルより上に上げない、ディーラーの合図があるまでチップに触らない、の2つは特に注意されやすいポイントでした。"),
            ("宿泊", "ハイアット リージェンシー 仁川に泊まりました。カジノ会員向けの宿泊プランでは、チェックイン前にカジノの会員登録が必要でした。ダブルのほうがツインより予約枠が多いこともありました。"),
        ],
        status="exp",
    ),
    dict(
        slug="hyatt-regency-incheon", title="ハイアット リージェンシー 仁川 宿泊レポート", category="宿泊", date="2026-10-31",
        lead="パラダイスシティのカジノに行くときに泊まった、ハイアット リージェンシー 仁川の様子です。写真はすべて運営者が撮影しました。",
        body=[
            ("ロビー", "白い大理石の大きなアーチの奥にレセプションがあります。エクスプレスチェックアウトの台も置かれていました。"),
            ("客室", "木目の壁と大きなベッドの落ち着いた部屋です。窓際には一人掛けのソファとオットマンがあり、夜は窓から空港周辺の明かりが見えました。"),
            ("バスルーム", "バスタブとシャワーがあり、洗面台との間はガラスで仕切られています。アメニティはボトルタイプでした。"),
        ],
        photos="hotel",
        status="exp",
    ),
    dict(
        slug="cafe9", title="最初のご飯はカジノの「Cafe 9」", category="グルメ", date="2026-10-31",
        lead="パラダイスシティに着いて最初に食べたのは、カジノの中のレストラン「Cafe 9」のご飯でした。写真は運営者が撮影しました。",
        body=[
            ("Cafe 9 ってどこ？", "カジノのフロアの中にあるレストランです。カジノのメインの食堂と紹介されていて、会員でなくても使えるという情報があります（要確認）。"),
            ("食べたもの", "豚丼のセット（炒飯・スープ・キムチつき）と、牛丼のセット（スープ・漬物つき）。韓国にいながら、日本人にもなじみのある丼ものが食べられます。"),
            ("食事券の出し方", "食事券は Cafe 9 の右側にある発券機で出せ、無料の券は24時間で使えなくなるという情報があります。1日に使える枚数やリセットの時間は、食事券のページにまとめています（要確認）。"),
            ("注意", "カジノの中は撮影が原則禁止とされています。写真を撮る前に、スタッフに確認してください。"),
        ],
        photos="cafe9",
        status="exp",
    ),
    dict(
        slug="meal-voucher", title="カジノの食事券の使い方メモ", category="特典", date="2026-10-31",
        lead="カジノでもらえる食事券について、ユーザーから寄せられた情報をまとめました。",
        body=[
            ("1日に使える枚数", "1日最大2枚までという情報があります。"),
            ("リセットの時間", "使える回数は午前6時にリセットされるという情報があります。"),
            ("注意", "会員ランクや時期によって条件が変わる可能性があります。使う前にカジノのカウンターで確認してください。"),
        ],
        status="user",
    ),
]

# 更新情報（新しい順）
UPDATES = [
    ("2026-10-31", "トップを「お得情報まとめ」中心に変更。公式の会員特典・ポイント・施設の情報と、Cafe 9 の記事（写真つき）を追加しました。"),
    ("2026-10-31", "サイトを公開しました。公式情報・ユーザー提供情報・体験談を区別して掲載しています。"),
]
