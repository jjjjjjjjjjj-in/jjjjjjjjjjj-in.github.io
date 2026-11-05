# 初心者ガイドの「ゲーム別ルール」。ゲームを足すときは GAMES に1件足す。
# summary: 一般的な遊び方の短い説明。notes: パラダイスシティで確かめたこと（区分・出典・確認日つき）。
# detail: くわしい解説（[(見出し, 本文), ...]）。書いたゲームだけ、専用のページ game-<slug>.html ができる。
# 確かめていないルールや最低ベットを書かない。分からないものは detail を空のまま（準備中）にする。

GAMES = [
    dict(slug="blackjack", name="ブラックジャック", kind="table",
         summary="配られたカードの合計を21に近づけ、ディーラーより21に近ければ勝ちのゲームです。合計が21をこえると負け（バースト）になります。",
         notes=[
             dict(text="サレンダー（勝負を降りて賭けたチップの半分を返してもらう）ができる台があり、最低ベットは30,000ウォンでした。運営者の体感では、いちばんチップが減りにくい台でした。", status="exp", src="operator", checked="2026-11-01"),
             dict(text="「フリーベット」の台では、ダブルダウンやスプリットを追加のチップなしでできますが、ディーラーの合計が22でもバーストにならないルールがありました。", status="exp", src="operator", checked="2026-11-01"),
         ], detail=None),
    dict(slug="baccarat", name="バカラ", kind="table",
         summary="「プレイヤー」と「バンカー」のどちらの手札の合計が9に近くなるかを予想して賭けるゲームです。カードを引くかどうかは決まったルールで進むので、自分で判断することが少なめです。",
         notes=[dict(text="フロアの奥に、とても多くのバカラの台が並んでいます。", status="exp", src="operator", checked="2026-11-01")], detail=None),
    dict(slug="three-card-poker", name="スリーカードポーカー", kind="table",
         summary="3枚のカードで、ディーラーとポーカーの役の強さを比べるゲームです。",
         notes=[dict(text="フロアに2台ありました。", status="exp", src="operator", checked="2026-11-01")], detail=None),
    dict(slug="poker", name="ポーカー", kind="table",
         summary="カードの組み合わせ（役）の強さで勝ち負けが決まるゲームの総称です。パラダイスシティでは、下のスリーカードポーカーやテキサスホールデムの台がありました。",
         notes=[], detail=None),
    dict(slug="texas-holdem", name="テキサスホールデム", kind="table",
         summary="自分だけの2枚の手札と、場に出る5枚の共通のカードを組み合わせて役を作るポーカーです。ほかのプレイヤーと勝負します。",
         notes=[dict(text="ブラックジャックの台の近くにテキサスホールデムの台がありました。", status="exp", src="operator", checked="2026-11-01")], detail=None),
    dict(slug="roulette", name="ルーレット", kind="table",
         summary="回る円盤のどの数字・色・場所にボールが落ちるかを予想して賭けるゲームです。",
         notes=[dict(text="ゼロが1つだけのタイプ（シングルゼロ）でした。一般的に、ゼロが2つのタイプよりお店の取り分が小さいとされています。入口のすぐ手前にあります。", status="exp", src="operator", checked="2026-11-01")], detail=None),
    dict(slug="craps", name="クラップス", kind="table",
         summary="2つのサイコロを振って、出る目を予想して賭けるゲームです。",
         notes=[dict(text="台があまり長い時間オープンしていない印象です。開いているのを見かけるのは主に日中でした。入口のすぐ手前にあります。", status="exp", src="operator", checked="2026-11-01")], detail=None),
    dict(slug="slots", name="スロット", kind="machine",
         summary="機械で遊ぶゲームです。ディーラーとのやりとりがないので、ひとりで自分のペースで遊べます。",
         notes=[dict(text="新規会員になると、20,000ウォン分の「マシンチケット」がもらえると公式に案内されています。", status="official", src="official_membership", checked="2026-10-31")], detail=None),
]
