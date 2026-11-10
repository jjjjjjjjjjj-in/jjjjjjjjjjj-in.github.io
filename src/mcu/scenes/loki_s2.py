# 『ロキ』シーズン2 シーンごとの詳しいあらすじ
# 2026-11-10 英語版ウィキペディアの各話の記事（Plot）とシーズンの記事を照らし合わせて、ファルコン＆ウィンター・ソルジャーと同じ形に書き直した。
# 運営者の希望: 第1話から始め、場面ごとに起きた事実だけを書く。見出しはつながった場面でまとめる。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
# 資料で確かめられなかった所（第3話の大富豪の名前、第4話でロキとシルヴィが話す場面の位置など）は書いていない。
SCENE_NUMBERS = True  # 場面に「話-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1話 ウロボロス", "Episode 1: Ouroboros", [
        ("過去のTVAに飛ばされる",
         "シーズン1の最後で、ロキは時間の果ての城で、シルヴィに時間の扉の向こうへ突き飛ばされた。ロキはTVAの本部にもどるが、同じ場所にいたまま、体が過去と現在と未来のあいだを勝手に行き来してしまう。\n"
         "最初に飛ばされたのは過去のTVAだった。そこではメビウスたちもロキを知らず、見知らぬ侵入者として追いかけてくる。",
         "Thrown into the TVA's past",
         "At the end of Season 1, Sylvie pushed Loki through a time door at the Citadel. He arrives back at TVA headquarters, but while staying in the same place, his body keeps jumping between past, present and future.\n"
         "The first jump takes him to the TVA's past. Nobody there knows him, Mobius included, and they chase him as an intruder."),
        ("録画の中の在り続ける者",
         "過去のTVAで、ロキは1本の録画を見つける。TVAを作った在り続ける者（シーズン1の城の男）が、ラヴォーナ・レンスレイヤーに、一緒に働いてくれたことの礼を言っている映像だった。ラヴォーナと在り続ける者は、仲間のような関係だったのだ。",
         "A recording of He Who Remains",
         "In the past, Loki finds a recording of He Who Remains, the man from the Citadel who created the TVA, thanking Ravonna Renslayer for working with him. The two had been something like partners."),
        ("混乱するTVA",
         "現在のTVA。シルヴィが在り続ける者を殺したため、決められた時間の流れはどんどん枝分かれし、TVAは大混乱になっている。ラヴォーナは姿を消し、代わりにギャンブル判事とドックス将軍が上に立っている。\n"
         "ハンターB-15とメビウスは2人に、TVAで働く人はみな枝分かれした時間から連れて来られた変異体だと伝える。ギャンブル判事は説得され、枝分かれした時間を消すのをやめるよう命じる。",
         "A TVA in chaos",
         "In the present, the Sacred Timeline is branching rapidly because Sylvie killed He Who Remains, and the TVA is in disarray. Ravonna is gone, and Judge Gamble and General Dox have taken charge.\n"
         "Hunter B-15 and Mobius tell them that everyone working at the TVA is a variant taken from a branched timeline. Gamble is persuaded and orders the TVA to stop wiping out branches."),
        ("会議に飛びこむロキ",
         "その会議の場に、時間を飛んできたロキが現れる。ロキは、TVAの裏にいたのは在り続ける者だと明かし、メビウスに、在り続ける者の別の姿（変異体）がたくさんいて危ないと警告する。\n"
         "一方、ドックス将軍は、シルヴィを探す任務だと言って、多くのハンターに武器をたっぷり持たせる。",
         "Loki crashes the meeting",
         "Loki slips into the meeting. He reveals that He Who Remains was behind the TVA and warns Mobius about the danger of He Who Remains' many variants.\n"
         "Meanwhile, General Dox has many hunters arm themselves heavily, supposedly for a mission to find Sylvie."),
        ("技術者OB",
         "ロキとメビウスは、TVAの機械を直したり作ったりする部署で、何百年もひとりで働いてきた技術者ウロボロス（通称OB）を訪ねる。\n"
         "OBは、ロキの症状を「時間のすべり」と名づける。原因は、増えすぎた時間の枝で、時間の流れを整える巨大な機械「時間の織機」があふれそうになっているからではないかと考える。\n"
         "OBの計画はこうだ。メビウスが「時間のオーラ抽出装置」を持って織機に近づく。ロキは未来で自分を剪定（消して時間から外す）し、その瞬間に装置でロキを時間の流れから引っぱり出す。",
         "O.B. the technician",
         "Loki and Mobius visit Ouroboros, called O.B., a technician who has worked alone for centuries in the department that repairs and builds the TVA's machines.\n"
         "O.B. calls Loki's condition \"time slipping\" and suspects the cause is the flood of new branches overloading the Temporal Loom, the giant machine that keeps the flow of time in order.\n"
         "His plan: Mobius takes a Temporal Aura Extractor to the Loom. Loki prunes himself in the future, which releases him from time, and at that moment the device pulls him out of the time stream."),
        ("橋をわたるメビウス",
         "メビウスは、TVAの建物と時間の織機をつなぐ橋に出て、抽出装置を織機につなぐことに成功する。",
         "Mobius on the bridge",
         "Mobius goes out onto the bridge between the TVA building and the Temporal Loom, and manages to hook the Extractor up to the Loom."),
        ("未来のTVA",
         "ロキは未来へすべる。そこでは織機があぶない状態になり、TVAから人々が避難していた。\n"
         "ロキは自分を剪定するための道具「タイムスティック」を探しまわり、一瞬だけシルヴィと出会う。そしてぎりぎりのところで、後ろから何者かに剪定される。",
         "The TVA's future",
         "Loki slips into the future, where the Loom is going critical and the TVA is being evacuated.\n"
         "He hunts for a TimeStick to prune himself and briefly runs into Sylvie. Then, at the last possible second, someone prunes him from behind."),
        ("引きもどされたロキ",
         "現在では、OBがTVAを守るため、織機のまわりを閉じ始める。メビウスは、ロキを待つべきだと反対する。\n"
         "メビウスはロキを時間の流れから引っぱり出すことに成功し、2人は閉じていく織機の前から転がるようにして逃げ出す。\n"
         "ロキの体はもう勝手に飛ばされなくなった。ロキとメビウスは、シルヴィを探しに出発する。",
         "Loki pulled back",
         "In the present, O.B. starts sealing off the Loom to protect the TVA, while Mobius argues they must wait for Loki.\n"
         "Mobius succeeds in pulling Loki out of the time stream, and the two tumble back to safety as the Loom is sealed.\n"
         "Loki has stopped slipping. He and Mobius set out to find Sylvie."),
        ("エンドクレジットの途中",
         "シルヴィは、枝分かれした時間の1982年、アメリカのオクラホマ州ブロクストンに来て、マクドナルドの店に入る。",
         "Mid-credits",
         "Sylvie arrives in Broxton, Oklahoma, in 1982 on a branched timeline, and walks into a McDonald's."),
    ]),
    ("第2話 ブレイキング・ブラッド", "Episode 2: Breaking Brad", [
        ("連絡がとだえたX-5",
         "ロキとメビウスは、シルヴィを探している。ドックス将軍とハンターX-5から連絡がこなくなったため、2人は、X-5がシルヴィを見つけたのではと考え、X-5の行方を追う。",
         "X-5 goes silent",
         "Loki and Mobius are searching for Sylvie. When General Dox and Hunter X-5 stop responding, they suspect X-5 found her and set out to track him down."),
        ("1977年のロンドン",
         "X-5は、決められた時間の流れの1977年のロンドンにいた。そこで、自分の本当の人生だった人気映画俳優ブラッド・ウルフとして暮らし、映画『ザニアック』に主演していた。\n"
         "ブラッドは逃げ出し、追ってきたハンターB-15から走って逃げ、メビウスを力でねじふせる。しかしロキが魔法でつかまえ、TVAへ連れもどす。",
         "London, 1977",
         "X-5 is on the Sacred Timeline in 1977 London, living his real life as famous film actor Brad Wolfe, star of the movie Zaniac.\n"
         "Brad runs, outpaces Hunter B-15 and overpowers Mobius, but Loki catches him with magic and he is brought back to the TVA."),
        ("ケイシーが見つけたこと",
         "TVAの受付係ケイシーは、ラヴォーナが姿を消す前に、時計のキャラクターの人工知能ミス・ミニッツと連絡を取り合っていたことを見つける。ミス・ミニッツも行方不明で、2人は手を組んでいると考える。\n"
         "ケイシーがそれをB-15、ロキ、メビウスに伝えると、ロキは、ラヴォーナと在り続ける者が仲間のように話していた録画のことを打ち明ける。",
         "What Casey finds",
         "TVA receptionist Casey discovers that Ravonna was in contact with Miss Minutes, the TVA's clock-faced AI, before both went missing, and concludes they are working together.\n"
         "When Casey tells B-15, Loki and Mobius, Loki reveals the recording in which Ravonna and He Who Remains spoke like partners."),
        ("織機に入れないOB",
         "OBは、増え続ける時間の枝をこわれずに受け止められるよう、時間の織機を直そうとする。しかし織機に入るには、ミス・ミニッツの力か、在り続ける者の「時間のオーラ」が必要だと分かる。",
         "O.B. locked out of the Loom",
         "O.B. tries to adjust the Temporal Loom so it can safely take in the growing branches without a meltdown, but finds he can't get into it without Miss Minutes or He Who Remains' temporal aura."),
        ("ブラッドの取り調べ",
         "ロキとメビウスがブラッドを問いつめると、ブラッドはロキを負け犬とからかい、メビウスには、TVAに入る前の自分の人生を一度も調べたことがないくせにと言う。メビウスはかっとなってしまう。\n"
         "そこでロキが1人で取り調べる。ブラッドを入れた箱型の装置で体をしめつけ、ブラッドはついに、ドックスの任務から抜けたことと、シルヴィの居場所を知っていることを認める。",
         "Interrogating Brad",
         "When Loki and Mobius question Brad, he mocks Loki as a loser and needles Mobius for never checking what his own life was like before he joined the TVA. Mobius loses his temper.\n"
         "Loki then questions Brad alone, using a box-like device that squeezes him, until Brad admits he abandoned Dox's mission and knows where Sylvie is."),
        ("マクドナルドのシルヴィ",
         "ロキ、メビウス、ブラッドは、枝分かれした時間のオクラホマ州ブロクストンへ行き、マクドナルドでレジの仕事をしているシルヴィを見つける。\n"
         "ロキは、TVAがあぶないこと、未来のTVAでシルヴィに会ったことを話し、何が起きるのか調べるのを手伝ってほしいとたのむ。しかしシルヴィは、今のふつうの暮らしに満足していると言って断る。\n"
         "ブラッドが、みんな命があぶないと言い出したため、シルヴィは魔法でブラッドをあやつり、本当のことを言わせる。ドックスの本当の計画は、枝分かれした時間すべてを一斉に爆破して消すことだった。",
         "Sylvie at McDonald's",
         "Loki, Mobius and Brad travel to Broxton, Oklahoma, on a branched timeline and find Sylvie working the register at McDonald's.\n"
         "Loki tells her the TVA is in danger and that he met her in the TVA's future, and asks for help working out what happened. She refuses, content with her ordinary life.\n"
         "When Brad declares they are all in mortal danger, Sylvie enchants him into telling the truth: Dox's real plan is to bomb and destroy every branched timeline at once."),
        ("ドックスをとめる",
         "ブラッドはTVAの監視にもどされる。ロキ、メビウス、シルヴィはドックスのいる場所へ乗りこみ、作戦をとめようとする。\n"
         "しかし、そのときにはもう、作り直した時間の装置（テンパッド）と「リセット爆弾」で、時間の枝のほとんどが消されていた。ドックスはつかまるが、仲間の何人かは逃げてしまう。",
         "Stopping Dox",
         "Brad is sent back into custody. Loki, Mobius and Sylvie storm Dox's location to stop her operation.\n"
         "But by then most of the branches have already been destroyed with reset charges and modified TemPads. Dox is captured, though some of her allies escape."),
        ("シルヴィが去る",
         "ケイシーは、残った時間の枝の1つで、ラヴォーナのテンパッドの反応を見つける。\n"
         "シルヴィは、枝分かれした世界を守れなかったTVAは根っこからくさっていると言い、在り続ける者のテンパッドを持ったまま、オクラホマのマクドナルドへもどっていく。",
         "Sylvie leaves",
         "Casey picks up Ravonna's TemPad on one of the surviving branches.\n"
         "Sylvie declares the TVA rotten for failing to protect the branches, and goes back to her McDonald's in Oklahoma, still holding He Who Remains' TemPad."),
    ]),
    ("第3話 1893年", "Episode 3: 1893", [
        ("また育ち始めた枝",
         "TVAの本部で、OBは、ドックスに消された時間の枝がまた育ち始めていることに気づく。このままでは織機があふれ、TVAがこわれてしまう。織機を直すために入れるのは、やはりミス・ミニッツか、在り続ける者の時間のオーラだけだ。",
         "The branches grow back",
         "At TVA headquarters, O.B. finds that the branches Dox destroyed are growing back, threatening to overload the Loom and destroy the TVA. Only Miss Minutes or He Who Remains' temporal aura can open the way to fix it."),
        ("1868年のシカゴ",
         "ラヴォーナとミス・ミニッツは、枝分かれした時間の1868年のシカゴへ行く。在り続ける者が死ぬ前に決めておいたとおり、2人は「TVAの手引き書」を、少年ヴィクター・タイムリーが見つけられるようこっそり置いていく。ヴィクターは、在り続ける者の別の姿（変異体）だ。\n"
         "ロキとメビウスはミス・ミニッツと手を組んでいるラヴォーナのテンパッドを追い、まず1868年へ、次に1893年へ向かう。2人は手引き書が置かれたことには気づかない。",
         "Chicago, 1868",
         "Ravonna and Miss Minutes travel to Chicago in 1868 on a branched timeline. As He Who Remains arranged before his death, they secretly leave the TVA Handbook where a young Victor Timely, one of his variants, will find it.\n"
         "Loki and Mobius, tracking Ravonna's TemPad because she is working with Miss Minutes, go first to 1868 and then to 1893. They never learn about the handbook."),
        ("シカゴ万国博覧会",
         "1893年のシカゴ万国博覧会。ロキとメビウスは、大人になったヴィクター・タイムリーが、自分の作った「織機の試作品」を人々の前で発表しているのを見る。\n"
         "このころのタイムリーは、TVAの機械を元にした本物の試作品を作る一方で、お金をだまし取るためのにせものの発明も売っていた。",
         "The World's Fair",
         "At the 1893 Chicago World's Fair, Loki and Mobius watch the grown-up Victor Timely present his Loom prototype.\n"
         "By now Timely has built real prototypes of TVA devices, but he also sells fake inventions to swindle people."),
        ("4組の追っ手",
         "タイムリーは、4組から追われることになる。\n"
         "①にせの発明でだまされた大富豪とその仲間（しかえしのため）②ロキとメビウス（織機を直すのにタイムリーの時間のオーラが必要）③ラヴォーナとミス・ミニッツ（タイムリーを在り続ける者の後がまにし、自分たちはその横につきたい）④シルヴィ（タイムリーが力を持つ前に殺したい）。",
         "Four groups give chase",
         "Timely ends up chased by four groups:\n"
         "1) a robber baron and his allies, out for revenge over a scam; 2) Loki and Mobius, who need Timely's temporal aura to fix the Loom; 3) Ravonna and Miss Minutes, who want him to take He Who Remains' place with them at his side; 4) Sylvie, who wants to kill him before he can rise to power."),
        ("シルヴィをとめるロキ",
         "ロキは、タイムリーを殺そうとするシルヴィをとめ、魔法で大富豪たちをおどして追い払う。そのすきに、タイムリーはラヴォーナとミス・ミニッツと一緒に逃げる。\n"
         "タイムリーは、子どものころに手引き書をくれたのがラヴォーナだと気づいて礼を言う。しかしラヴォーナが手を組もうと持ちかけると、タイムリーは彼女を置き去りにする。",
         "Loki stops Sylvie",
         "Loki stops Sylvie from killing Timely and uses magic to scare off the robber baron, while Timely escapes with Ravonna and Miss Minutes.\n"
         "Timely realizes Ravonna gave him the handbook as a child and thanks her, but when she proposes a partnership, he leaves her behind."),
        ("ウィスコンシンの研究所",
         "タイムリーは、ウィスコンシン州の自分の研究所へもどる。ラヴォーナばかりがタイムリーにかまわれることにやきもちを焼いていたミス・ミニッツは、本物の体がほしいと言い、タイムリーに恋心を打ち明ける。タイムリーは、ミス・ミニッツの電源を切ってしまう。",
         "The Wisconsin lab",
         "Timely returns to his laboratory in Wisconsin. Miss Minutes, jealous of the attention Ravonna got, says she wishes she had a real body and confesses romantic love for Timely. He switches her off."),
        ("命ごいするタイムリー",
         "ラヴォーナ、ロキ、メビウス、シルヴィが研究所に追いつき、シルヴィがその場をおさえる。\n"
         "タイムリーは命ごいをし、自分は在り続ける者にはならない、自分のことは自分で選べると言う。シルヴィはタイムリーを殺さず、ロキがTVAへ連れて行くことを許す。",
         "Timely begs for his life",
         "Ravonna, Loki, Mobius and Sylvie catch up with Timely at the lab, and Sylvie takes control of the situation.\n"
         "Timely begs for his life, insisting he won't become He Who Remains and can make his own choices. Sylvie spares him and lets Loki take him to the TVA."),
        ("時間の果ての城へ",
         "シルヴィは、ラヴォーナを時間の果ての城へ送る。ラヴォーナはミス・ミニッツを連れて行き、城で電源を入れ直す。2人は、くさりかけた在り続ける者の遺体を目にする。\n"
         "ミス・ミニッツは、ラヴォーナが聞いたら怒るような、ラヴォーナの秘密を知っていると告げる。",
         "To the Citadel",
         "Sylvie sends Ravonna to the Citadel at the End of Time. Ravonna brings Miss Minutes along and switches her back on, and they see He Who Remains' decaying body.\n"
         "Miss Minutes tells Ravonna she knows a secret about her that would make her angry."),
    ]),
    ("第4話 TVAの心臓部", "Episode 4: Heart of the TVA", [
        ("ラヴォーナの消された記憶",
         "ミス・ミニッツは、ラヴォーナに昔の録画を見せる。在り続ける者は、自分の戦争を手伝ったラヴォーナに礼を言い、一緒にTVAを率いようと持ちかけていた。しかしラヴォーナがTVAにもどると、在り続ける者はミス・ミニッツに命じて、ラヴォーナやほかのTVAの職員の記憶を消させていた。\n"
         "ラヴォーナは、在り続ける者の軍隊を指揮していた人だったのだ。ミス・ミニッツは、あの人ぬきで2人で組もうと持ちかける。",
         "Ravonna's erased memories",
         "Miss Minutes shows Ravonna an old recording: He Who Remains thanked her for her help in his war and proposed that they lead the TVA together. But when she returned to the TVA, he had Miss Minutes erase her memories and those of other TVA staff.\n"
         "Ravonna had commanded his army. Miss Minutes proposes that the two of them work together without him."),
        ("TVAに来たタイムリー",
         "TVAに着いたタイムリーは、ロキとメビウスから、こわれかけた時間の織機を直す手伝いをたのまれる。織機は、枝分かれした時間を受け止めきれず、大きな故障の寸前だった。\n"
         "タイムリーはOBに会う。OBは、自分がTVAの機械を作れたのはタイムリーの考えのおかげだと明かす。ところがそのタイムリーは、OBが書いたTVAの手引き書を読んで発明を始めていた。どちらが先とも言えない、輪のようなつながりだった。\n"
         "2人は力を合わせ、織機を直すための装置「スループット・マルチプライヤー」を作る。",
         "Timely at the TVA",
         "At the TVA, Loki and Mobius ask Timely to help fix the Temporal Loom, which is close to catastrophic failure because it can't handle the branches.\n"
         "Timely meets O.B., who reveals that his own ideas came from Timely, while Timely's inventions were inspired by the TVA Handbook that O.B. wrote: a loop with no clear beginning.\n"
         "Together they build a Throughput Multiplier to fix the Loom."),
        ("B-15の申し出",
         "ハンターB-15は、つかまっているドックス将軍とその仲間、ブラッドのところへ行き、TVAを守るために力を合わせようと申し出て、その場を去る。",
         "B-15's offer",
         "Hunter B-15 visits the detained General Dox, her loyalists and Brad, offers to work together to defend the TVA, and leaves."),
        ("ラヴォーナの誘い",
         "続いてラヴォーナとミス・ミニッツが、つかまっている人たちの前に現れる。TVAを乗っ取るのに手を貸せば、時間の流れの中での暮らしをあげると持ちかける。\n"
         "うなずいたのはブラッドだけだった。ドックスと仲間たちはラヴォーナを手伝うことをこばみ、ミス・ミニッツに押しつぶされて殺される。",
         "Ravonna's offer",
         "Then Ravonna and Miss Minutes appear before the detainees, offering a life on the timeline to anyone who helps them take over the TVA.\n"
         "Only Brad agrees. Dox and her loyalists refuse to help Ravonna, and Miss Minutes crushes them to death."),
        ("さらわれたタイムリー",
         "ブラッドはハンターD-90を剪定し、タイムリーをさらう。ロキとシルヴィは、タイムリーを助けに急ぐ。\n"
         "ミス・ミニッツはTVAの仕組みを乗っ取り、シルヴィを一時とじこめてしまう。",
         "Timely kidnapped",
         "Brad prunes Hunter D-90 and kidnaps Timely. Loki and Sylvie rush to rescue him.\n"
         "Miss Minutes takes over the TVA's systems and briefly traps Sylvie."),
        ("ロキを剪定したのは",
         "救出に向かうとちゅう、シルヴィとロキは、時間のすべりに苦しんでいたころの過去のロキと出くわす。ロキはその過去の自分を剪定する。\n"
         "第1話で、未来のTVAでロキを後ろから剪定した「何者か」は、ロキ自身だった。",
         "Who pruned Loki",
         "On the way, Sylvie and Loki run into his past self, still suffering from time slipping. Loki prunes his past self.\n"
         "The \"someone\" who pruned Loki from behind in the TVA's future in Episode 1 was Loki himself."),
        ("OBの再起動",
         "OBはTVAの仕組みを再起動して、ミス・ミニッツを止める。このとき、TVAの中で魔法をおさえていた装置も止まる。\n"
         "魔法が使えるようになったシルヴィは、ブラッドをあやつり、ラヴォーナを剪定させる。タイムリーは助け出される。",
         "O.B. reboots the system",
         "O.B. reboots the TVA's systems to shut Miss Minutes down, which also turns off the devices that suppress magic inside the TVA.\n"
         "Now able to use magic, Sylvie enchants Brad and makes him prune Ravonna. Timely is rescued."),
        ("織機の爆発",
         "タイムリーの時間のオーラのおかげで、織機に入る道が開く。ロキは、自分がマルチプライヤーを取り付けに行くと名乗り出るが、タイムリーは、問題が起きたら自分なら直せると言いはって、自分が行く。\n"
         "ところがタイムリーは、強くなった織機の時間の放射を浴びたとたん、体が糸のように引きのばされてばらばらになり、死んでしまう。マルチプライヤーは使われないままだった。\n"
         "時間の織機は爆発し、その光の波が、TVAにいるロキ、メビウス、シルヴィ、B-15、ケイシー、OBへと広がっていく。",
         "The Loom explodes",
         "Timely's temporal aura restores access to the Loom. Loki volunteers to go out and launch the Multiplier, but Timely insists on going because he can fix any problems.\n"
         "The moment he is exposed to the Loom's heightened temporal radiation, Timely is stretched apart and killed, and the Multiplier goes unused.\n"
         "The Temporal Loom explodes, and its blast wave spreads toward Loki, Mobius, Sylvie, B-15, Casey and O.B. in the TVA."),
    ]),
    ("第5話 科学／フィクション", "Episode 5: Science/Fiction", [
        ("1人だけ残ったロキ",
         "ロキは爆発を生きのびるが、TVAの本部にいたほかの人たちはみな消えていた。\n"
         "ロキはまた勝手に時間をすべり始める。今度は時間だけでなく場所もこえて飛ばされる。TVAの本部が糸のようにほどけて消えていく中、ロキはぎりぎりで逃げ出す。",
         "Loki alone",
         "Loki survives the explosion, but everyone else at TVA headquarters has vanished.\n"
         "He starts time slipping again, now across both space and time, and barely escapes as the headquarters itself unravels."),
        ("元の暮らしにもどった仲間たち",
         "すべった先は、枝分かれした時間の世界だった。そこでは仲間たちが、TVAに入る前の元の人生にもどっていた。\n"
         "メビウスは2022年のクリーブランドで水上バイクを売る「ドン」。B-15は2012年のニューヨークの医師「ヴェリティ・ウィリス」。ケイシーは1962年のアルカトラズ刑務所にいる囚人「フランク・モリス」。OBは1994年のパサデナで暮らす作家で科学者の「A.D.ダグ博士」。\n"
         "ロキはいつも、その人のすぐ近くに飛ばされる。しかし、誰もロキのことを知らない。",
         "Friends back in their old lives",
         "His slips take him to branched timelines where his friends have been reset to the lives they had before the TVA.\n"
         "Mobius is Don, a jet ski salesman in Cleveland in 2022. B-15 is Dr. Verity Willis, a physician in New York in 2012. Casey is Frank Morris, a prisoner at Alcatraz in 1962. O.B. is Dr. A.D. Doug, a writer and scientist in Pasadena in 1994.\n"
         "Loki always lands close to them, but none of them know him."),
        ("A.D.ダグ博士",
         "ロキは、爆発の前の時間へもどりたいと考え、ダグ博士に助けを求める。ダグはロキの話を信じ、時間のすべりを自分で操れるようになれとはげます。\n"
         "ロキは、TVAを救いたいという目的に気持ちを集中させてみるが、うまくいかない。\n"
         "そこでダグは別の方法を考える。爆発のときにその場にいた全員をもう一度集めれば、みんなの時間のオーラを合わせて、正しい時間と場所へもどれるかもしれない。ロキは、持っていたTVAの手引き書をダグに渡し、テンパッドを作ってもらう。",
         "Dr. A.D. Doug",
         "Wanting to slip back to before the explosion, Loki asks Doug for help. Doug believes his story and urges him to learn to control his time slipping.\n"
         "Loki concentrates on his goal of saving the TVA, but nothing happens.\n"
         "So Doug suggests another way: gather everyone who was there at the explosion, so their combined temporal aura can send them back to the right time and place. Loki gives Doug the TVA Handbook he kept so Doug can build a TemPad."),
        ("ドンを説得する",
         "ロキはドンのいる世界へすべり、息子たちを守りたいというドンの気持ちにうったえて、手伝ってもらうことになる。\n"
         "そこへ、ダグが自分で作ったテンパッドを使ってやって来る。作るのに19か月かかり、そのあいだに仕事も妻も失ったという。",
         "Winning over Don",
         "Loki slips to Don's timeline and persuades him to help by appealing to his wish to protect his sons.\n"
         "Doug arrives using the TemPad he built himself. It took him 19 months, and cost him his job and his wife."),
        ("仲間を集める",
         "ロキとダグはテンパッドを使って、ドン、ウィリス、フランクを、ダグの作業場に集める。",
         "Gathering the group",
         "Using the TemPad, Loki and Doug bring Don, Willis and Frank together in Doug's workshop."),
        ("シルヴィの問い",
         "ロキは最後に、オクラホマ州ブロクストンのマクドナルドでシルヴィを見つける。シルヴィはほかの仲間とちがい、記憶をなくしていなかった。シルヴィは、自分の人生を生きたいと言って手伝いを断る。\n"
         "シルヴィに問いつめられ、ロキは本当の気持ちを認める。仲間を取りもどしたいのだ。そして、ひとりになるのがこわいのだ。\n"
         "シルヴィは、ロキも自分の人生を生きるようにとすすめる。ロキはあきらめ、ドン、ウィリス、フランク、ダグを元の暮らしにもどそうと言う。",
         "Sylvie's question",
         "Finally Loki finds Sylvie at the McDonald's in Broxton, Oklahoma. Unlike the others, she still has her memories. She refuses to help because she wants to live her own life.\n"
         "Pressed by her, Loki admits what he really wants: his friends back. He is afraid of being alone.\n"
         "Sylvie tells him to live his own life too. Loki gives up and says Don, Willis, Frank and Doug should go back to their lives."),
        ("消えていく世界",
         "ところが、シルヴィのいる世界のすべてが糸のようにほどけて消え始める。シルヴィは、枝分かれした時間が死にかけていると気づき、考えを変えてダグの作業場へ向かう。\n"
         "しかし、みんなが動き出す前に、作業場もほどけ始める。フランク、ダグ、ドン、ウィリス、そしてシルヴィも消えていく。",
         "The worlds unravel",
         "Then everything in Sylvie's world begins to unravel. Realizing the branches are dying, she changes her mind and heads to Doug's workshop.\n"
         "But before the group can act, the workshop unravels too, and Frank, Doug, Don, Willis and Sylvie vanish with it."),
        ("物語を書き直す",
         "その瞬間、ロキはついに時間のすべりを操れるようになる。出来事や目的ではなく、「人」に気持ちを集中させればよかったのだ。\n"
         "ロキは作業場が消える少し前にもどり、みんなに、物語は書き直せると告げる。そしてOBに気持ちを集中させ、織機が爆発する前の時間へとすべる。",
         "Rewriting the story",
         "In that moment, Loki finally learns to control his time slipping by focusing on a person instead of an event or a purpose.\n"
         "He slips back to just before the workshop unravels and tells everyone that the story can be rewritten. Then, focusing on O.B., he slips to the moment before the Loom exploded."),
    ]),
    ("第6話 栄光ある目的", "Episode 6: Glorious Purpose", [
        ("爆発の前へ、何度でも",
         "ロキは、時間の織機が爆発する前の時間へ何度もすべってもどり、前の失敗から学んで、毎回ちがうやり方を試す。",
         "Back before the blast, again and again",
         "Loki slips back again and again to moments before the Loom explodes, using what he learned each time to try something different."),
        ("何百年もの勉強",
         "ロキはOBから、スループット・マルチプライヤーのしくみを何百年もかけて学ぶ。そしてついに、タイムリーが織機に近づいてマルチプライヤーを動かし、無事にもどってくるところまでたどり着く。\n"
         "それでも織機は爆発してしまう。どれだけ手を加えても、終わりなく増える時間の枝を受け止めることはできなかった。",
         "Centuries of study",
         "Over centuries, Loki learns the science of the Throughput Multiplier from O.B. At last he manages a run in which Timely reaches the Loom, activates the Multiplier and returns safely.\n"
         "But the Loom still explodes. No adjustment can handle infinite branches."),
        ("城へもどる",
         "ロキはやり方を変え、そもそも時間が枝分かれしないようにしようと考える。そして、シルヴィが在り続ける者を殺す直前の、時間の果ての城へすべる。\n"
         "ロキは何度もシルヴィをとめようとするが、シルヴィは、とめたいなら自分を殺すしかないと言う。ロキはシルヴィを殺さず、シルヴィは毎回、在り続ける者を殺してしまう。",
         "Back to the Citadel",
         "Changing tactics, Loki decides to stop the timeline from branching at all. He slips to the Citadel at the End of Time, just before Sylvie kills He Who Remains.\n"
         "He tries again and again to stop her, but she says he'll have to kill her to do it. He won't, and every time she kills He Who Remains."),
        ("在り続ける者の答え",
         "ロキが在り続ける者に、なぜ抵抗しないのかとたずねると、在り続ける者はシルヴィの時間を止めてしまう。在り続ける者はロキが時間をすべっていることを見ぬき、その道を用意したのは自分だとほのめかす。\n"
         "ロキも時間を止められることを見せると、在り続ける者は秘密を明かす。時間の織機は、もしものときの安全装置だった。織機があふれると、枝分かれした時間がTVAごと消え、決められた時間の流れだけが守られるようにできていたのだ。",
         "He Who Remains' answer",
         "When Loki asks He Who Remains why he never fights back, He Who Remains freezes Sylvie in time. He recognizes Loki's time slipping and hints that he is the one who laid that path for him.\n"
         "When Loki shows that he can freeze time too, He Who Remains reveals the truth: the Loom is a fail-safe. If it overloads, the branches are deleted along with the TVA, and only the Sacred Timeline survives."),
        ("2つの道",
         "ロキに残された道は2つだった。①織機をこわす。そうすれば、在り続ける者の変異体たちがマルチバース全体で大戦争を起こすかもしれない。②シルヴィを殺して在り続ける者を守り、決められた時間の流れを守る。\n"
         "在り続ける者は、シルヴィを殺して織機を救えとすすめるが、ロキはそれをこばむ。",
         "Two paths",
         "Loki has two options: destroy the Loom and risk an apocalyptic multiversal war waged by He Who Remains' variants, or kill Sylvie to protect He Who Remains and the Sacred Timeline.\n"
         "He Who Remains suggests killing Sylvie to save the Loom. Loki refuses."),
        ("メビウスとシルヴィに聞く",
         "ロキは、別々の時間のメビウスとシルヴィに会いに行き、意見を聞く。\n"
         "シーズン1の初めのころのメビウスは、大きな目的のためなら重い荷物を引き受けろと言う。第5話のころのシルヴィは、誰もが自分で選べるように在り続ける者は死なせるべきだと言う。",
         "Asking Mobius and Sylvie",
         "Loki visits Mobius and Sylvie at different points in time to ask their advice.\n"
         "Mobius, from early in Season 1, tells him to accept the burden for the greater good. Sylvie, from the time of Episode 5, urges him to let He Who Remains die so that free will survives."),
        ("ロキの選択",
         "ロキはもう一度すべり、今度はタイムリーの代わりに自分が織機へ向かって歩いていく。\n"
         "ロキは織機をこわし、魔法で死にかけた時間の枝をよみがえらせる。そして枝を両手でまとめ、自分を中心にした大きな木のような形に組みなおす。\n"
         "ロキは時間の果てに残り、1人でマルチバースの枝を見守り続ける道を選ぶ。",
         "Loki's choice",
         "Loki slips once more and this time walks to the Loom himself, in Timely's place.\n"
         "He destroys the Loom, revives the dying branches with magic, gathers them in his hands and reshapes them into a great tree-like structure with himself at its center.\n"
         "He commits himself to watching over the multiverse's branches alone at the End of Time."),
        ("新しいTVA",
         "そのあとのTVAは、終わりなく増える時間の枝を消さずに受け入れ、在り続ける者の変異体たちを見張るようになる。メビウスは、変異体の1人が、アース616の「となりの世界（量子世界）」で倒されたと報告する。\n"
         "B-15はTVAを率いる1人になる。OBは、なかよしになったミス・ミニッツの電源を入れ直し、タイムリーとの共著として新しいTVAの手引き書を書く。\n"
         "ある時間の流れでは、1868年の少年タイムリーが手引き書を受け取らない。",
         "A new TVA",
         "Afterward, the TVA accepts the endless branches and keeps watch on He Who Remains' variants. Mobius reports that one of them has been stopped in Earth-616's \"adjacent realm\" (the Quantum Realm).\n"
         "B-15 becomes one of the TVA's leaders. O.B. switches a now-friendly Miss Minutes back on and writes a new TVA Handbook, crediting Timely as co-author.\n"
         "In one timeline, the young Timely never receives the handbook in 1868."),
        ("それぞれの行き先",
         "虚無では、ラヴォーナがTVAの紋章のそばで目を覚まし、時間を食べる怪物アライオスを目にする。\n"
         "メビウスはTVAをやめる。メビウスとシルヴィは、メビウスの別の姿であるドンと息子たちを、遠くから見守る。そしてロキは、時間の果てから、みんなを見守っている。",
         "Where everyone ends up",
         "In the Void, Ravonna wakes near a TVA crest and sees Alioth, the creature that devours time.\n"
         "Mobius retires from the TVA. He and Sylvie watch his variant Don and Don's sons from afar, while Loki watches over them all from the End of Time."),
    ]),
    ("まとめ（最終話までのネタバレ）", "Summary (spoilers through the finale)", [
        ("ロキの時間のすべり",
         "①第1話：シルヴィに城から突き飛ばされたあと、ロキの体は過去・現在・未来を勝手に行き来する。OBとメビウスの抽出装置で止まる。\n"
         "②第4話：第1話の未来でロキを剪定したのは、ロキ自身だった。\n"
         "③第5話：織機の爆発のあと、時間と場所をこえてまたすべり始める。「人」に気持ちを集中させることで、ついに自分で操れるようになる。\n"
         "④第6話：その力で何度も時間をやり直し、最後は織機をこわして、時間の枝を自分で支える道を選ぶ。",
         "Loki's time slipping",
         "1) Ep. 1: After Sylvie pushes him out of the Citadel, Loki jumps between past, present and future. O.B. and Mobius stop it with the Extractor.\n"
         "2) Ep. 4: The one who pruned Loki in the future in Episode 1 was Loki himself.\n"
         "3) Ep. 5: After the Loom explodes, he slips across time and space again, and finally learns to control it by focusing on a person.\n"
         "4) Ep. 6: He uses that power to replay time again and again, and in the end destroys the Loom and holds the branches together himself."),
        ("仲間たちの元の人生（第5話）",
         "・メビウス → ドン（2022年のクリーブランド。水上バイクを売る。息子が2人）\n"
         "・B-15 → ヴェリティ・ウィリス医師（2012年のニューヨーク）\n"
         "・ケイシー → フランク・モリス（1962年のアルカトラズ刑務所の囚人）\n"
         "・OB → A.D.ダグ博士（1994年のパサデナ。作家で科学者）\n"
         "・シルヴィだけは記憶をなくさず、ブロクストンのマクドナルドで暮らしていた。",
         "Friends' original lives (Ep. 5)",
         "- Mobius → Don (Cleveland, 2022; sells jet skis; two sons)\n"
         "- B-15 → Dr. Verity Willis (New York, 2012)\n"
         "- Casey → Frank Morris (an Alcatraz prisoner, 1962)\n"
         "- O.B. → Dr. A.D. Doug (Pasadena, 1994; writer and scientist)\n"
         "- Only Sylvie kept her memories, living in Broxton at the McDonald's."),
        ("死んだ人・剪定された人（話の順に）",
         "・ドックス将軍と仲間たち（第4話）：つかまっていたところで、TVA乗っ取りへの協力をこばんだため、ミス・ミニッツに押しつぶされて殺される。\n"
         "・ハンターD-90（第4話）：ラヴォーナの側についたブラッドが、タイムリーをさらうときに剪定する。\n"
         "・過去のロキ（第4話）：時間のすべりに苦しんでいた過去の自分を、ロキが剪定する。これで第1話の出来事につながる。\n"
         "・ラヴォーナ（第4話）：タイムリーを救うため、シルヴィが魔法でブラッドをあやつって剪定させる。第6話で、虚無で目を覚ます。\n"
         "・ヴィクター・タイムリー（第4話）：織機を直そうとマルチプライヤーを持って近づき、強い時間の放射で体を引きのばされて死ぬ。\n"
         "・在り続ける者（第6話）：ロキが何度時間をもどしても、シルヴィが城で殺してしまう（シーズン1最終話の場面）。",
         "Who died or was pruned (in order)",
         "- General Dox and her loyalists (Ep. 4): while detained, they refuse to help take over the TVA, and Miss Minutes crushes them to death.\n"
         "- Hunter D-90 (Ep. 4): pruned by Brad, now on Ravonna's side, as he kidnaps Timely.\n"
         "- Loki's past self (Ep. 4): Loki prunes his own time-slipping past self, closing the loop from Episode 1.\n"
         "- Ravonna (Ep. 4): to rescue Timely, Sylvie enchants Brad into pruning her. She wakes up in the Void in Episode 6.\n"
         "- Victor Timely (Ep. 4): approaching the Loom with the Multiplier, he is stretched apart by its intense temporal radiation.\n"
         "- He Who Remains (Ep. 6): no matter how often Loki replays it, Sylvie kills him at the Citadel (the Season 1 finale scene)."),
    ]),
]
