# jjjjjjjjjjj-in.github.io（全サイトの入口）

運営者の全サイトの入口ページ（サイト名「もっちぃま」。デザインはモノトーンで、各サイトのタイルは同じ大きさにそろえる。映画に限らず旅行・本・自分の有料noteなど色々なテーマを扱う予定）。GitHub Pages で https://jjjjjjjjjjj-in.github.io/ に公開される。
運営者は日本語で、技術に詳しくない。返答は日本語で、短く、専門用語を避ける。コミット作成者は Claude <noreply@anthropic.com>。

## このリポジトリの役割
- `index.html`: 全サイトへのリンクを並べた入口ページ
- `sitemap.xml`: 全サイトのサイトマップをまとめたもの（サイトマップインデックス）。Google Search Console にはこれ1つだけ登録する
- `robots.txt`: ドメインのトップの robots.txt（各サイトの中の robots.txt は効かない）
- 生成物は手で編集しない。`src/sites.py` を編集して `python3 src/build.py` を実行する

## 新しいサイトを作るとき（運営者の手作業をゼロにする手順）
1. サイトは**このリポジトリの中のフォルダ**として作る（例: `/new-guide/`）。新しいリポジトリを作ると、運営者が GitHub Pages を手で有効にする必要があるため。
   - 既存の `doomsday-guide` は別リポジトリ（GitHub Pages で /doomsday-guide/ に公開）。
2. 広告は最初から入れる。ID は以下（運営者の登録済み）:
   - Amazon.co.jp アソシエイト: `doomsdayguide-22`
   - Amazon.com アソシエイト（英語サイト用）: `doomsdaygui08-20`
   - もしもアフィリエイト（楽天市場）: a_id `5875908`、p_id 54、pc_id 54、pl_id 616。検索結果へは `&url=` に楽天の URL をエンコードして付ける（どこでもリンク形式）
   - A8.net: DMM TV を申請中（2026-10-31）。承認されたら広告コードを運営者から受け取る
3. 広告のルール: 「PR」表記を出す。Amazon の場合は「Amazonのアソシエイトとして、当サイトは適格販売により収入を得ています。」（英語: "As an Amazon Associate, this site earns from qualifying purchases."）を出す。誤クリックを誘う配置はしない。
4. そのサイトの `sitemap.xml` を作り、`src/sites.py` に1件追加して `python3 src/build.py` を実行し、push する。これで入口ページと Google への通知（サイトマップインデックス）が自動で更新される。
5. Amazon（日本・アメリカ）・もしも・A8 には `https://jjjjjjjjjjj-in.github.io/` を登録済み（2026-10-31）。このドメインの中のサイトなら、運営者の追加作業なしで広告を使える。
6. Google アナリティクス（測定ID `G-KDFL8GPPRZ`、全サイト共通）のタグを全ページに入れ、フッターに共通のプライバシーポリシー https://jjjjjjjjjjj-in.github.io/privacy.html へのリンクを置く。新しい広告サービスを使い始めたら、このページ（`src/build.py` の privacy_html）にも追記する。
7. 公式予告編などのリンクは、確認できた公式のものだけ使う。推測した URL は使わない。
8. オンラインカジノの宣伝は日本では違法で、ASP でも禁止。カジノを扱うときはリゾートの旅行ガイドとして書く。

## Google Search Console
- `https://jjjjjjjjjjj-in.github.io/`（URLプレフィックス）の確認コードは `src/build.py` の `GOOGLE_SITE_VERIFICATION` に設定済み（2026-10-31）。
- 所有権の確認とサイトマップ（`sitemap.xml`）の登録は済み（2026-10-31）。以降のサイト追加は `src/sites.py` に足すだけで自動で伝わる。
