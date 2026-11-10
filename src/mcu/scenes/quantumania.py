# 『アントマン＆ワスプ：クアントマニア』（2023年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじと登場人物の記事、検索で見つかった解説記事で事実を確かめた。
# 資料が1つしかない所や食い違う所（冒頭でジャネットが襲われる怪物、コーヒー店の店員の勘違い、
# クライラー卿のその後、確率の嵐でのスコットたちの細かいやりとり、キャシーが逃げ出した方法、
# 最後にどちらがどうやってカーンをコアへ落としたか、現代の場面の年など）は書いていない。
# 以前の版の「ジャネットはコアを小さくした」「最後の映像は1901年」はまちがいだったので直した
# （資料では、ジャネットはコアを大きくして使えなくした。最後の映像は1893年のシカゴ万国博覧会）。
# 日本語版のせりふは、日本語の吹替・字幕の言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 人物名は相関図（relations.py）にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 量子の世界での出会い", "Part 1: A meeting in the Quantum Realm", [
        ("ひとりで生きるジャネット",
         "何十年も前。原子よりも小さな量子の世界に取り残されたジャネット・ヴァン・ダインは、たった1人で、危険な生き物がいる土地を生きのびていた。",
         "Janet alone",
         "Decades ago. Stranded in the subatomic Quantum Realm, Janet van Dyne is surviving on her own in a land full of dangerous creatures."),
        ("空から落ちてきた船",
         "ある日、空から乗り物が落ちてきて、近くに墜落する。ジャネットが近づくと、壊れた船のそばに1人の男がいた。\n"
         "男は、道に迷ってここに閉じこめられた旅の者だと名乗る。",
         "A ship from the sky",
         "One day a vessel falls out of the sky and crashes nearby. When Janet goes to look, she finds a man beside the wrecked ship.\n"
         "He presents himself as a traveler who lost his way and got stranded here."),
    ]),
    ("第2部 有名人になったスコット", "Part 2: Scott the celebrity", [
        ("世界を救った男",
         "現代のサンフランシスコ。サノスとの戦いで世界を救ったスコット・ラングは、すっかり有名人になっていた。自分の体験を本（原題『Look Out for the Little Guy』）にして出し、町を歩けば声をかけられる。\n"
         "恋人ホープ・ヴァン・ダインは、父ハンクの会社を買い戻して「ピム・ヴァン・ダイン財団」と名前を変え、ピム粒子の技術で、住む家や食べ物が足りない人たちを助けていた。",
         "The man who saved the world",
         "Present-day San Francisco. Having helped save the world from Thanos, Scott Lang is now a celebrity. He's written a memoir, Look Out for the Little Guy, and people recognize him everywhere.\n"
         "His partner, Hope van Dyne, has bought back her father Hank's company, renamed it the Pym van Dyne Foundation, and uses Pym Particle technology to tackle housing and food shortages."),
        ("サーティワンの「世紀の従業員」",
         "スコットは、昔クビになったアイスクリーム店のサーティワンに立ち寄る。1作目でスコットをクビにした店長デイルは、今ではスコットを「世紀の従業員」としてたたえ、店に飾っていた。",
         "Employee of the Century",
         "Scott stops by the Baskin-Robbins that once fired him. Dale, the manager who let him go in the first film, now honors him as \"Employee of the Century.\""),
        ("留置場のキャシー",
         "スコットのもとに、娘キャシーが警察に捕まったという知らせが入る。18歳になったキャシーは、指パッチンで消えた5年の間に家をなくした人たちを助ける活動をしていた。ホームレスの人たちが追い出されるのに抗議し、ピム粒子でパトカーを小さくしてしまったのだった。\n"
         "スコットとホープが迎えに行く。キャシーは、ヒーローらしいことをしなくなった父に不満を持っていて、2人の間はぎくしゃくしている。",
         "Cassie in jail",
         "Scott gets word that his daughter Cassie has been arrested. Now 18, Cassie has been helping people left homeless after the Blip. Protesting the clearing of a homeless camp, she used Pym Particles to shrink a police car.\n"
         "Scott and Hope pick her up. Cassie feels her father has stopped doing hero work, and things between them are strained."),
        ("話さないジャネット",
         "スコットとキャシーは、ホープの両親ハンク・ピムとジャネットの家で一緒に食事をする。\n"
         "ジャネットは、量子の世界で過ごした30年のことをほとんど話そうとしない。ホープは、母が何かを隠していると感じていた。",
         "Janet won't talk",
         "Scott and Cassie have dinner with Hope's parents, Hank Pym and Janet.\n"
         "Janet still refuses to say much about her 30 years in the Quantum Realm, and Hope can tell her mother is hiding something."),
        ("キャシーの装置",
         "キャシーは、ハンクとホープに手伝ってもらいながら、量子の世界に信号を送って地図を作る装置を作っていたことを打ち明け、研究室で動かして見せる。\n"
         "それを知ったジャネットはあわてて、無理やり装置を止める。",
         "Cassie's device",
         "Cassie reveals that, with help from Hank and Hope, she has built a device that sends a signal into the Quantum Realm to map it, and she switches it on in the lab.\n"
         "Janet panics and forcibly shuts it down."),
        ("吸いこまれる5人",
         "しかし信号はもう向こうに届いていた。装置の上に入り口が開き、スコット、ホープ、キャシー、ハンク、ジャネットの5人は、ハンクの研究室のアリたちと一緒に、量子の世界へ吸いこまれてしまう。",
         "Pulled in",
         "But the signal has already been received. A portal opens and sucks all five of them, Scott, Hope, Cassie, Hank and Janet, into the Quantum Realm, along with some of Hank's lab ants."),
    ]),
    ("第3部 スコットとキャシー", "Part 3: Scott and Cassie", [
        ("2組に分かれて",
         "5人は2組に分かれて落ちる。スコットとキャシーは見たこともない生き物や植物がある場所に、ホープ、ハンク、ジャネットは別の場所にいた。",
         "Split up",
         "The five land in two groups. Scott and Cassie end up among strange creatures and plants; Hope, Hank and Janet land somewhere else."),
        ("ヴェブとクアズ",
         "スコットとキャシーは、量子の世界の住人たちに捕まる。赤いゼリーのような生き物ヴェブの体から出る液を飲むと、住人たちの言葉が分かるようになる。\n"
         "人の心を読むことができるクアズは、スコットの頭の中をのぞき、2人がどこから来たのかを知る。",
         "Veb and Quaz",
         "Scott and Cassie are seized by Quantum Realm natives. Drinking ooze from Veb, a red, jelly-like creature, lets them understand the locals.\n"
         "Quaz, a telepath, reads Scott's mind and learns where the two came from."),
    ]),
    ("第4部 アクシアのクライラー卿", "Part 4: Lord Krylar of Axia", [
        ("ジャネットの案内",
         "一方、ホープ、ハンク、ジャネットの3人は、ジャネットの案内で、量子の世界の大きな街アクシアにたどり着く。",
         "Janet leads the way",
         "Meanwhile, Janet leads Hope and Hank to Axia, a sprawling city in the Quantum Realm."),
        ("昔の仲間クライラー",
         "3人は、いろいろな姿の住人でにぎわう酒場で、アクシアを治めるクライラー卿に会う。クライラーは、ジャネットが昔一緒に戦った仲間だった。2人がただの仲間ではなかったらしいと分かり、ハンクはやきもちを焼く。\n"
         "クライラーは、ジャネットがいなくなってから世界が変わったと話す。今では、量子の世界の新しい支配者に仕えていた。",
         "Krylar, an old ally",
         "In a bar packed with all kinds of locals, they meet Lord Krylar, who governs Axia. He fought alongside Janet long ago, and it's hinted they were more than friends, to Hank's jealousy.\n"
         "Krylar says things have changed since Janet left. He now serves the Realm's new ruler."),
        ("裏切りと戦い",
         "クライラーは、支配者をおそれて3人を引き渡そうとし、兵士たちが3人を取り囲む。ホープはスーツで兵士たちと戦う。",
         "Betrayal and a brawl",
         "Afraid of the ruler, Krylar tries to turn them in, and guards close in. Hope fights them off in her suit."),
        ("船を奪って逃げる",
         "3人はクライラーの生き物のような形の船を奪い、ハンクが操縦して街から逃げ出す。",
         "Stealing the ship",
         "The three steal Krylar's organic-looking ship, and Hank flies them out of the city."),
    ]),
    ("第5部 反乱軍の隠れ家", "Part 5: The rebels' hideout", [
        ("ジェントーラの反乱軍",
         "スコットとキャシーが連れていかれたのは、量子の世界を支配する者と戦う反乱軍の隠れ家だった。リーダーの女戦士ジェントーラは、征服者の軍に故郷を滅ぼされていた。\n"
         "ジェントーラは、ジャネットの名前を聞いて顔色を変える。征服者が力を持つようになったのは、かつてのジャネットの行いが元になっていると話す。",
         "Jentorra's rebels",
         "Scott and Cassie have been brought to the hideout of a rebel group fighting the Realm's ruler. Its leader, the warrior Jentorra, lost her home to the Conqueror's army.\n"
         "She reacts sharply to Janet's name, telling them that Janet's past dealings are what led to the Conqueror's rise."),
        ("モードックの襲撃",
         "そこへ、征服者の軍が攻めてくる。率いているのは、大きな頭に小さな体、空飛ぶ機械の体を持つモードックだった。モードックは反乱軍の仲間たちを撃ち倒していく。\n"
         "スコットとキャシーは戦うが、捕まってしまう。",
         "M.O.D.O.K.'s raid",
         "The Conqueror's forces attack, led by M.O.D.O.K., a figure with a huge head on a tiny body inside a flying machine. He guns down rebel fighters.\n"
         "Scott and Cassie fight back but are captured."),
        ("モードックの正体",
         "モードックの正体は、1作目でスコットと戦ったハンクの元弟子ダレン・クロスだった。クロスはあのとき死なず、ばらばらに縮んで量子の世界に落ち、頭だけが大きい姿で生きのびた。征服者の手で機械の体に作り変えられ、手下になっていたのだった。\n"
         "キャシーの装置の信号を受け取ったのも、このクロスだった。クロスは、ハンクとスコットを恨んでいる。",
         "Who M.O.D.O.K. is",
         "M.O.D.O.K. is Darren Cross, Hank's former protégé whom Scott fought in the first film. He didn't die: he shrank unevenly into the Quantum Realm and survived with a grotesquely oversized head. The Conqueror rebuilt him with a machine body and made him a henchman.\n"
         "Cross is also the one who received Cassie's signal. He holds a grudge against Hank and Scott."),
    ]),
    ("第6部 ジャネットの告白", "Part 6: Janet's confession", [
        ("船の修理",
         "船の中で、ジャネットはついに、ずっと隠していたことをホープとハンクに打ち明ける。\n"
         "量子の世界にいたころ、ジャネットは、墜落した船のそばにいたあの男と出会った。男は、船の動力のコアを直せば2人ともここから出られると言った。ジャネットは男と何年も一緒に挑み、ついにコアを動かすことに成功した。",
         "Fixing the ship",
         "Aboard the ship, Janet finally tells Hope and Hank what she's been hiding.\n"
         "During her years in the Realm she met the man by the crashed ship. He said they could both escape if she helped him rebuild his ship's multiversal power core. They worked at it for years and finally got it running."),
        ("男の正体",
         "しかし、船と心がつながったとき、ジャネットは男の頭の中を見てしまう。男は征服者カーンといい、いくつもの世界と時間の流れを、次々に征服して滅ぼしてきた者だった。\n"
         "カーンは、自分を恐れたほかの「自分たち」によって、量子の世界に追放されていたのだった。",
         "The man's true nature",
         "But when she linked with the ship, Janet saw into the man's mind. He was Kang the Conqueror, who had conquered and destroyed entire worlds and timelines.\n"
         "Kang had been exiled to the Quantum Realm by his own variants, who feared him."),
        ("コアを大きくしたジャネット",
         "ジャネットはカーンを外に出してはいけないと考え、ピム粒子でコアを大きくして、使えないようにした。そして逃げ出し、量子の世界の反乱軍に加わった。\n"
         "その後、力を取り戻したカーンは量子の世界を征服し、自分の帝国を作った。話を聞いたホープは母を受け入れ、カーンを外に出さないと心に決める。",
         "Janet enlarges the core",
         "Determined that Kang must never escape, Janet used Pym Particles to enlarge the core so it could not be used. Then she fled and joined the Realm's resistance.\n"
         "Kang later regained his power, conquered the Realm and built an empire. Hope makes peace with her mother and vows not to let Kang escape."),
    ]),
    ("第7部 カーンの取り引き", "Part 7: Kang's deal", [
        ("カーンの城",
         "スコットとキャシーは、カーンの城に連れていかれる。カーンは、スコットがアベンジャーズの一員だと知ると、前にお前を殺したことがあったかと聞き、ハンマーを持ったヒーロー（ソー）とまちがえる。",
         "Kang's citadel",
         "Scott and Cassie are brought to Kang's citadel. Learning Scott is an Avenger, Kang asks, \"Have I killed you before?\" and wonders if he's \"the one with the hammer.\" \"That's Thor,\" Scott replies."),
        ("キャシーを人質に",
         "カーンは、ジャネットが大きくしたコアを取り戻したいが、自分ではピム粒子を作れない。そこでスコットに、縮んでコアの中に入り、コアを取ってこいと命じる。\n"
         "うまくいけば家族を元の世界に帰すが、断ればキャシーを殺すと脅す。スコットは、キャシーを守るために従うしかなかった。",
         "Cassie as hostage",
         "Kang wants back the core Janet enlarged, but he can't make Pym Particles himself. So he orders Scott to shrink down inside it and retrieve it.\n"
         "If Scott succeeds, Kang promises to send the family home; if he refuses, Kang will kill Cassie. To protect her, Scott has no choice."),
    ]),
    ("第8部 確率の嵐", "Part 8: The probability storm", [
        ("増えていくスコット",
         "スコットは、大きくなったコアがある場所へ連れていかれ、縮んで中へ入る。そこは確率の嵐と呼ばれる場所だった。\n"
         "一歩動くたびに、「もしも」の別の選択をしたスコットが次々に現れ、あっという間に数えきれないほどのスコットがあふれる。スコットはそれにのみこまれそうになる。",
         "Multiplying Scotts",
         "Scott is taken to the enlarged core and shrinks down into it. It's a probability storm.\n"
         "With every move, another Scott who made a different choice appears, until there are countless Scotts and he is nearly overwhelmed."),
        ("力を合わせる",
         "スコットたちは言い争うが、キャシーを助けるという1つの目的で力を合わせる。スコットたちは積み重なって、スコットをコアのほうへ押し上げる。",
         "Working together",
         "The Scotts argue, then unite around one goal: saving Cassie. They pile on top of one another and push Scott up toward the core."),
        ("ホープが来る",
         "そこへ、クライラーの船で駆けつけたホープが飛んできて、スコットを引き上げる。2人はコアを小さくして手に入れる。",
         "Hope arrives",
         "Hope, who has arrived on Krylar's ship, flies in and pulls Scott out. Together they shrink the core and grab it."),
        ("約束を破るカーン",
         "カーンは約束を破る。コアを取り上げ、キャシーを返さず、ジャネットを捕まえる。\n"
         "モードックは、ハンクが乗っていたクライラーの船を撃ち落とす。",
         "Kang breaks his word",
         "Kang breaks his word. He takes the core, keeps Cassie and captures Janet.\n"
         "M.O.D.O.K. shoots down Krylar's ship with Hank still aboard."),
    ]),
    ("第9部 量子の世界の反乱", "Part 9: The uprising", [
        ("進化したアリたち",
         "墜落した船から、ハンクはアリたちに助け出される。一緒に量子の世界に来たハンクのアリたちは、時間の流れの違うこの世界で長い時代を過ごし、とても賢い文明を作っていた。\n"
         "みんなで助け合うアリの社会に、ハンクは感心する。ハンクはアリたちを連れて、スコットとホープのもとへ向かう。",
         "The evolved ants",
         "Hank is rescued from the wreck by ants. The lab ants pulled in with the family have lived through ages in the Realm's faster time and built a hyper-intelligent civilization.\n"
         "Hank admires their cooperative society, joking that socialism is a charged word. He leads the ants to join Scott and Hope."),
        ("ジェントーラを助ける",
         "キャシーは自分で作った紫色のスーツで小さくなり、カーンの牢に忍びこんで、ジェントーラたちを助け出す。",
         "Freeing Jentorra",
         "Cassie shrinks in her homemade purple suit, slips into Kang's prison and frees Jentorra and the other rebels."),
        ("反乱が始まる",
         "キャシーとジェントーラが呼びかけ、量子の世界の人々が立ち上がって、カーンの城と軍に向かっていく。\n"
         "スコットもキャシーも巨大化して戦う。そこへハンクが、アリの大軍を連れて現れ、カーンの兵士たちに襲いかかる。",
         "The uprising begins",
         "Rallied by Cassie and Jentorra, the people of the Realm rise up and charge Kang's citadel and army.\n"
         "Scott and Cassie both go giant to fight. Then Hank arrives with an army of ants, which swarms Kang's soldiers."),
        ("クロスが心を変える",
         "モードックはキャシーと戦うが、キャシーは、今からでも嫌なやつをやめることはできると、クロスの心に呼びかける。\n"
         "その言葉に動かされたクロスは、カーンを裏切り、スコットたちの味方につく。",
         "Cross changes sides",
         "M.O.D.O.K. goes after Cassie, but she appeals to what's left of Darren, telling him it's never too late to stop being a jerk.\n"
         "Moved, Cross turns on Kang and joins Scott's side."),
        ("クロスの最期",
         "カーンは光の盾で身を守り、アリたちも破れない。クロスは自分がダレンだと叫んで盾にまっすぐ突っこみ、機械の体の武器で盾を壊すが、自分も致命傷を負う。\n"
         "クロスは死ぬ前に、自分もアベンジャーズとして死ねるかとたずね、スコットたちはぎこちなくうなずく。クロスはそのまま息を引き取る。",
         "Cross's end",
         "Kang shields himself with a force field even the ants can't break. Declaring that he is Darren, Cross charges straight into it and blasts it apart with his chair's weapons, but is fatally wounded.\n"
         "Dying, he asks if he at least dies an Avenger, and Scott and Hope awkwardly agree. Then he dies."),
    ]),
    ("第10部 最後の戦い", "Part 10: The final battle", [
        ("帰り道の入り口",
         "ジャネットはコアを使って元の世界への入り口を開く。ジャネット、ハンク、ホープ、キャシーが先に飛びこむ。",
         "A way home",
         "Janet uses the core to open a portal home. Janet, Hank, Hope and Cassie leap through first."),
        ("カーンとスコット",
         "最後に続こうとしたスコットに、カーンがおそいかかる。1対1の戦いで、カーンはスコットをさんざんに痛めつける。\n"
         "カーンは、自分が倒れれば、自分と同じような者たちがもっとやってくると警告する。それでもスコットは、立ち上がり続ける。",
         "Kang versus Scott",
         "As Scott goes to follow, Kang attacks him. One-on-one, Kang beats him brutally.\n"
         "Kang warns that if he falls, others like him will come. Scott keeps getting back up."),
        ("戻ってきたホープ",
         "そこへ、ホープが入り口から戻ってきて加勢する。スコットとホープは、ピム粒子と一緒にカーンを、暴走するコアの中へ落とす。カーンはコアごと消える。",
         "Hope comes back",
         "Hope comes back through the portal to help. Together, Scott and Hope send Kang tumbling into the unstable core along with the Pym Particles, and Kang vanishes with it."),
        ("キャシーが開く入り口",
         "入り口は閉じてしまうが、先に帰ったキャシーが元の世界からもう一度入り口を開く。スコットとホープも、無事に家族のもとへ戻る。",
         "Cassie reopens the portal",
         "The portal closes, but Cassie, already home, reopens it from the other side, and Scott and Hope make it back to the family."),
    ]),
    ("第11部 その後とエンドクレジット", "Part 11: Afterward and the credit scenes", [
        ("いつもの毎日",
         "サンフランシスコ。スコットは、また家族と平和な毎日を送り、町の人たちに声をかけられる。\n"
         "ふと、カーンの警告を思い出し、自分たちの勝利が何か恐ろしいことの始まりではないかと考える。しかしスコットは、それを気にしないことにする。",
         "Back to normal",
         "San Francisco. Scott happily goes back to life with his family, greeted by people around town.\n"
         "He briefly wonders whether Kang's warning was true and whether their victory set something terrible in motion, then shrugs it off."),
        ("エンドクレジットの途中",
         "巨大な広間に、たくさんのカーンが集まっている。中心にいるのはイモータス、そのそばにラマ・タトとセンチュリオン。彼らは、追放したカーンが死んだことを知る。\n"
         "イモータスは、アベンジャーズたちがマルチバースにふれ始めていると警告し、カーンたちは動き出す。",
         "Mid-credits",
         "In a vast hall, a crowd of Kangs gathers, led by Immortus with Rama-Tut and Centurion. They learn that the Kang they exiled is dead.\n"
         "Immortus warns that the heroes are beginning to touch the multiverse, and the Kangs prepare to act."),
        ("エンドクレジットの後",
         "1893年、シカゴの万国博覧会。客席にいるロキとメビウスが、舞台で時間について話す発明家ヴィクター・タイムリーを見つめている。タイムリーもまた、カーンの別の姿だった。",
         "After the credits",
         "The Chicago World's Fair, 1893. In the audience, Loki and Mobius watch the inventor Victor Timely give a presentation about time. Timely is another variant of Kang."),
    ]),
    ("まとめ", "Summary", [
        ("スコットがしたこと",
         "世界を救ったヒーローとして有名人になり、娘キャシーとはぎくしゃくしていた（第2部）。量子の世界でカーンに捕まり、キャシーの命のためにコアを取りに行った（第7部・第8部）。カーンに裏切られたあと、反乱に加わり、最後はホープと2人でカーンをコアへ落とした（第9部・第10部）。",
         "What Scott did",
         "A celebrity hero, he had a strained relationship with Cassie (Part 2). Captured by Kang in the Quantum Realm, he went into the core to save Cassie's life (Parts 7 and 8). After Kang betrayed him, he joined the uprising and, with Hope, sent Kang into the core (Parts 9 and 10)."),
        ("ジャネットの秘密",
         "量子の世界にいたころ、カーンを助けて船のコアを直したが、カーンの正体を知り、ピム粒子でコアを大きくして使えなくした（第6部）。そのことを家族に隠していたが、ホープとハンクに打ち明け、最後は自分でコアを使って帰り道を開いた（第10部）。",
         "Janet's secret",
         "Years ago she helped Kang repair his ship's core, then, learning who he really was, enlarged it with Pym Particles so it couldn't be used (Part 6). She hid this from her family until she told Hope and Hank, and in the end she used the core to open the way home (Part 10)."),
        ("カーンがしたこと",
         "ほかのカーンたちに量子の世界へ追放され、ジャネットと船を直したが、ジャネットにコアを使えなくされた（第6部）。その後、量子の世界を征服し、キャシーを人質にスコットにコアを取りに行かせ、約束を破った（第7部・第8部）。",
         "What Kang did",
         "Exiled to the Quantum Realm by other Kangs, he repaired his ship with Janet, until she made the core unusable (Part 6). He then conquered the Realm, used Cassie as a hostage to make Scott retrieve the core, and broke his promise (Parts 7 and 8)."),
        ("死んだ人たち（話の順に）",
         "・反乱軍の仲間たち（第5部）：隠れ家をおそったモードックに撃たれる。\n"
         "・ダレン・クロス（モードック）（第9部）：キャシーの言葉で心を変えてカーンを裏切り、カーンの光の盾に突っこんで壊したときに致命傷を負って死ぬ。\n"
         "・カーン（第10部）：スコットとホープにピム粒子と一緒にコアへ落とされ、コアごと消える。エンドクレジットの途中で、ほかのカーンたちが彼の死を知る。",
         "Who died (in order)",
         "- Rebel fighters (Part 5): shot by M.O.D.O.K. in the raid on their hideout.\n"
         "- Darren Cross / M.O.D.O.K. (Part 9): won over by Cassie, he turned on Kang and was fatally wounded smashing through Kang's force field.\n"
         "- Kang (Part 10): sent into the core with the Pym Particles by Scott and Hope, vanishing with it. In the mid-credits scene, the other Kangs learn he is dead."),
    ]),
]
