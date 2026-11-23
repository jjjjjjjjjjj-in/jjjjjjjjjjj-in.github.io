// ============================================================
// 店舗データ。ここを書き換えるだけでサイトに反映されます。
//   visited : 管理人が行ったことがある店は true にする
//   comment : 行った店のひとこと感想（visited が true のとき表示）
//   type    : "直系" / "ラーメン荘系" / "インスパイア"
//   score   : 管理人の偏差値（50がふつう。期待を超えてきた店が80以上）。付けないときは null
//   order   : そのとき頼んだもの
//   photos  : 写真（最大6枚）。photos フォルダに画像を入れて、ファイル名を書く
//             例) photos: ["photos/shin-1.jpg", "photos/shin-2.jpg", "photos/shin-3.jpg"],
//             1枚目が大きく表示されます。自分で撮った写真だけを使ってください。
// ============================================================

//   insta   : お店の公式インスタのユーザー名（@ は付けない）。写真の代わりに埋め込み表示される
//   instaPost : 特定の投稿だけ見せたいときは、その投稿のURL（insta より優先）

// 自分の写真がない店に、公式インスタと Googleマップを埋め込むか
const USE_EMBEDS = true;
// 埋め込みを使わないとき、「写真」という仮の枠を出すか
const PHOTO_PLACEHOLDER = false;

const SHOPS = [
  // ---------- 京都 ----------
  { name: "ラーメン二郎 京都店", pref: "京都", area: "京都市左京区・一乗寺", type: "直系",
    note: "関西で食べられる直系二郎。醤油の立った非乳化寄りのスープに、九条ネギのトッピングが京都らしい一杯。",
    visited: false, comment: "" },
  { name: "ラーメン荘 夢を語れ", pref: "京都", area: "京都市左京区・一乗寺", type: "ラーメン荘系",
    note: "関西の二郎インスパイアの先駆けとして知られる店。ラーメン荘グループの原点。",
    insta: "ichijoji_yume", visited: false, comment: "" },
  { name: "池田屋 一乗寺店", pref: "京都", area: "京都市左京区・一乗寺", type: "インスパイア",
    note: "ラーメン激戦区・一乗寺で評価の高い一軒。プチサイズでも一般的な大盛り級のボリューム。",
    visited: false, comment: "" },
  { name: "ラーメン荘 地球規模で考えろ 伏見", pref: "京都", area: "京都市伏見区", type: "ラーメン荘系",
    note: "「地球規模」の愛称で親しまれる伏見の人気店。豚の旨みが濃いスープと極太麺。",
    insta: "chikyu_kibo_fushimi", visited: false, comment: "" },
  { name: "ラーメン荘 地球規模で考えろ ソラ", pref: "京都", area: "京都市右京区・西院", type: "ラーメン荘系",
    note: "西院エリアにある地球規模の系列店。",
    insta: "chiki.sora", visited: false, comment: "" },
  { name: "ラーメン荘 地球規模で考えろ サン", pref: "京都", area: "京都市中京区", type: "ラーメン荘系",
    note: "京都の街なかで地球規模の味が食べられる中京区の店舗。",
    visited: false, comment: "" },

  // ---------- 大阪 ----------
  { name: "ラーメン荘 歴史を刻め 本店", pref: "大阪", area: "大阪市東淀川区・下新庄", type: "ラーメン荘系",
    note: "大阪の二郎系を語るなら外せない行列店。阪急・下新庄駅からすぐ。",
    insta: "rekisi_honten", visited: false, comment: "" },
  { name: "ラーメン荘 歴史を刻め 日本橋店", pref: "大阪", area: "大阪市浪速区・恵美須町", type: "ラーメン荘系",
    note: "2024年にオープンしたミナミの店舗。でんでんタウンの買い物ついでに寄れる立地。",
    visited: false, comment: "" },
  { name: "ラーメン荘 歴史を刻め 寺田町店", pref: "大阪", area: "大阪市天王寺区・寺田町", type: "ラーメン荘系",
    note: "環状線・寺田町エリアの「歴史」。",
    visited: false, comment: "" },
  { name: "ラーメン荘 歴史を刻め なかもず店", pref: "大阪", area: "堺市北区・なかもず", type: "ラーメン荘系",
    note: "南大阪で「歴史」を食べるならここ。",
    visited: true, score: 80, order: "汁なし 500g",
    comment: "500gを6分で完食。今のところ人生で一番うまい二郎系。油マシマシがやっぱり最強。" },
  { name: "ラーメン荘 おもしろい方へ", pref: "大阪", area: "大東市・野崎（住道から移転）", type: "ラーメン荘系",
    note: "ラーメン荘グループの店。2026年に住道から野崎へ移転。汁なしなどのメニューも人気。",
    visited: false, comment: "" },
  { name: "ラーメン荘 地球規模で考えろ 茨木店", pref: "大阪", area: "茨木市", type: "ラーメン荘系",
    note: "京都発の「地球規模」が大阪に初出店した店舗。",
    insta: "chikyukibo_mirai", visited: false, comment: "" },
  { name: "笑福 大阪西中島店", pref: "大阪", area: "大阪市淀川区・西中島南方", type: "インスパイア",
    note: "鳥取発のガッツリ系。豚骨醤油に背脂、山盛りの野菜で関西でも根強い人気。",
    visited: false, comment: "" },
  { name: "麺屋 のスた", pref: "大阪", area: "大阪市中央区・ウラなんば", type: "インスパイア",
    note: "ウラなんばの行列店。ミナミで二郎系が食べたくなったらまず名前が挙がる一軒。",
    visited: true, score: 50, order: "ラーメン",
    comment: "うまいけど二郎感は控えめ。背脂をもっと増やせたら嬉しい。" },
  { name: "ドカ盛りマッチョ 日本橋", pref: "大阪", area: "大阪市・日本橋", type: "インスパイア",
    note: "自家製太麺とドカ盛りが看板。とにかく量を食べたい日に。",
    visited: false, comment: "" },
  { name: "RAMEN .R 難波店", pref: "大阪", area: "大阪市・難波", type: "インスパイア",
    note: "2025年オープンの新しめの店。自家製麺と店炊きスープがウリ。",
    insta: "ramen_r_namba", visited: true, score: null, order: "400g 野菜マシ・アブラマシマシ",
    comment: "麺は歴史に近い。アブラは細切れではなく別皿のかたまりで出てくる。カッコつけて400gの野菜マシにしたら歴史のマシマシより多くて、食べ切るのに必死だった。味はうまい。" },
  { name: "BUTAKIN 西中島南方店", pref: "大阪", area: "大阪市淀川区・西中島南方駅すぐ", type: "インスパイア",
    note: "南方エリアにできた新顔の二郎系。",
    insta: "butakin_osaka", visited: false, comment: "" },
  { name: "麺に始まり麺に終わる", pref: "大阪", area: "門真市・京阪 大和田駅", type: "インスパイア",
    note: "麺の量を細かく選べる二郎系。カレーラーメンも名物。",
    photos: [], insta: "menhajimenowa.official", visited: false, comment: "" },
  { name: "ヤマネコ軒", pref: "大阪", area: "吹田市・江坂駅から徒歩3分ほど", type: "インスパイア",
    note: "あっさりした醤油スープに厚切り豚ともやしが乗る、さっぱり寄りの二郎系。",
    photos: [], insta: "yamanekoken_esaka", visited: false, comment: "" },

  { name: "ラーメン豚山 南船場店", pref: "大阪", area: "大阪市中央区・南船場（心斎橋）", type: "インスパイア",
    note: "関東発の二郎系チェーン。心斎橋から歩ける立地で、汁なしもある。",
    photos: [], insta: "butayama_official_", visited: true, score: 58, order: "汁なし 375g 全マシ",
    comment: "味はうまいし、豚そのものは一番柔らかいかもしれない。ただクセとパンチは控えめで中毒性は少なめ。二郎系が初めての人に向いている。" },
  { name: "釈迦力 友 あびこ店", pref: "大阪", area: "大阪市住吉区・あびこ", type: "インスパイア",
    note: "あびこにあるガッツリ系。赤い丼に炙った豚が乗る。",
    photos: [], insta: "syakariki_tomo", visited: true, score: 30, order: "300g 全マシマシ・背脂追加",
    comment: "自分の口には合わなかった。" },

  // ↓ draft: true の店は、場所が確認できるまでサイトに表示されません。
  //   pref と area を埋めて draft の行を消すと表示されます。
  { name: "G系ラーメン ナカモズマシマシ", pref: "大阪", area: "堺市北区・なかもず駅すぐ", type: "インスパイア",
    note: "なかもず駅前の二郎系。",
    photos: [], insta: "nakamozu_mashimashi", visited: true, score: 54, order: "醤油ラーメン 油マシマシ",
    comment: "油マシマシなのにあっさり。歴史と比べると太麺がきしめんっぽいけどうまい。チャーシューは酢豚みたいな味。クセになる感じや食べ切った達成感は控えめ。" },
  { name: "夢の一歩 大阪和泉店", pref: "大阪", area: "和泉市・和泉中央駅直結（エコールいずみ内）", type: "ラーメン荘系",
    note: "「夢を語れ」のスピンオフ店。駅直結の商業施設に入っていて行きやすい。",
    photos: [], insta: "yumeippoosaka", visited: true, score: 70, order: "",
    comment: "細かくは覚えていないけど、歴史に近い味でうまかった。" },
  { name: "ラーメン男塾!! 日本橋店", pref: "大阪", area: "大阪市浪速区・日本橋（恵美須町・なんばから歩ける）", type: "インスパイア",
    note: "自家製麺の二郎系。味玉・生卵・フライドオニオン・麺増量から1つ選べる。",
    photos: [], insta: "otokojuku_ramen", visited: true, score: 63, order: "",
    comment: "麺はわしわし。フライドオニオンがとてもうまく、豚は脂身が少ないのに柔らかい。次は野菜マシマシにしてもいいと思えるくらいおいしかった。" },
  { name: "麺処 藤山二郎 あべのHoop店", pref: "大阪", area: "大阪市阿倍野区・天王寺（あべのHoop 地下フードコート）", type: "インスパイア",
    note: "汁なしと、塩味の「塩二郎」がある二郎系。フライドオニオンがたっぷり乗る。",
    photos: ["photos/fujiyamajiro-1.jpg", "photos/fujiyamajiro-2.jpg"], insta: "fujiyamajiro_abenohoop", visited: true, score: 57, order: "汁なしラーメン",
    comment: "汁なしはうまい。のスたより上で、歴史の六甲道には届かないくらい。フライドオニオンがたっぷりで豚も柔らかい。前に食べた塩二郎は塩味のスープが自分には合わなかった（塩二郎だけなら偏差値40）。" },

  // ---------- 兵庫 ----------
  { name: "ラーメン荘 これが好きだから", pref: "兵庫", area: "西宮市・阪神国道駅", type: "ラーメン荘系",
    note: "西宮の行列店。極太麺とジャンクな味わいで常連が多い。",
    insta: "korega_sukidakara", visited: false, comment: "" },
  { name: "ラーメン荘 歴史を刻め 六甲道店", pref: "兵庫", area: "神戸市灘区・六甲道", type: "ラーメン荘系",
    note: "神戸で「歴史」が食べられる六甲道の店舗。",
    visited: true, score: 60, order: "汁なし",
    comment: "六甲道のマシはめちゃくちゃ多い。夏は店内が暑いので覚悟して行くこと。" },
  { name: "らぁ麺しん", pref: "兵庫", area: "明石市・西新町駅から徒歩3分ほど（西宮にも店舗あり）", type: "インスパイア",
    note: "明石の人気店。2026年には西宮にも出店。",
    insta: "ramen_shin2018", visited: false, comment: "" },

  // ---------- 滋賀 ----------
  { name: "ラーメン荘 歴史を刻め 滋賀瀬田店", pref: "滋賀", area: "大津市・瀬田", type: "ラーメン荘系",
    note: "滋賀で貴重なラーメン荘グループの店舗。",
    visited: false, comment: "" },

  // ---------- 和歌山 ----------
  { name: "暴豚製麺所", pref: "和歌山", area: "和歌山市", type: "インスパイア",
    note: "和歌山ラーメンの地で二郎系を出す一軒。",
    insta: "bouton_seimenjo", visited: false, comment: "" },
];
