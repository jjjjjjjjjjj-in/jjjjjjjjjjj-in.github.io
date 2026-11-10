# 『シークレット・インベージョン』シーンごとの詳しいあらすじ
# 2026-11-10 英語版ウィキペディアの各話の記事（Plot）とドラマの記事の各話のあらすじ、各話の解説記事（検索で読めた部分）を照らし合わせて書き直した。
# 運営者の希望: 第1話から始め、場面ごとに起きた事実だけを書く。見出しはつながった場面でまとめる。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
# 話の題は日本語版ウィキペディアの一覧（ディズニープラスの邦題）。人物名は相関図（relations.py）に合わせた。
# 日本語のセリフは確かめられなかったので、カギかっこの引用は入れていない。
# 資料で食い違う所（プレスコットの殺され方、ヒルが撃たれた場所、フェアバンクスの家での人質の様子、
# 大統領の車がひっくり返った方法、第6話のくわしい能力の順番など）は書いていない。
SCENE_NUMBERS = True  # 場面に「話-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1話 復活", "Episode 1: Resurrection", [
        ("モスクワのロスとプレスコット",
         "ロシアのモスクワ。CIAの捜査官エヴェレット・ロスが、元CIAのプレスコットと会う。プレスコットは、姿を変えられる宇宙人スクラルの過激な一派が、ロシアとアメリカの間に戦争を起こさせ、地球をうばおうとしていると調べ上げていた。\n"
         "プレスコットは、目の前のロスもスクラルではないかと疑う。2人はもみ合いになり、ロスがプレスコットを殺して、証拠を持ち去る。",
         "Ross and Prescod in Moscow",
         "In Moscow, CIA agent Everett Ross meets former CIA man Prescod, who has worked out that radical shape-shifting Skrulls plan to start a war between Russia and the U.S. and take over Earth.\n"
         "Prescod suspects Ross himself is a Skrull. They struggle, and Ross kills Prescod and leaves with the evidence."),
        ("屋根の上の追跡",
         "ロスは、マリア・ヒルに電話して迎えを頼む。そこへ、ロシア語を話す男がロスを追ってくる。ロスは建物の屋根の上を逃げるが、建物から落ち、ちょうど着いたヒルの車の前で死ぬ。\n"
         "ヒルは追ってきた男に銃を向けるが、男の正体はスクラルのタロスだった。死んだロスの体は、緑色のスクラルの姿に戻る。ロスはにせものだったのだ。ヒルは、ニック・フューリーに連絡する。",
         "Rooftop chase",
         "Ross calls Maria Hill for a pickup. A Russian-speaking man chases him across the rooftops. Ross falls from a building and dies in front of Hill's car as she arrives.\n"
         "Hill points her gun at the pursuer, who turns out to be the Skrull Talos. Ross's body changes into a green Skrull: he was an impostor. Hill calls Nick Fury."),
        ("フューリーの帰還",
         "フューリーは、指パッチンのあと、宇宙の基地セイバーで何年も働いていた。ヒルの知らせを受けて、フューリーは地球に戻る。\n"
         "隠れ家でフューリーはタロスと再会する。タロスは、フューリーがスクラルの新しい故郷を見つけられないままだったため、スクラルの評議会から追い出されたと話す。かつての仲間グラヴィクが、過激な一派のリーダーになっていた。タロスの妻ソレンも亡くなっていた。",
         "Fury comes back",
         "Since the Blip, Fury has been working in space at S.A.B.E.R. After Hill's call, he returns to Earth.\n"
         "At a safehouse he reunites with Talos, who says he was pushed off the Skrull Council because Fury never found the Skrulls a new home. Their former ally Gravik now leads the radicals. Talos's wife Soren is dead."),
        ("グラヴィクとギア",
         "グラヴィクたち過激派は、ロシアに基地を持ち、人間になりすまして動いている。その中に、タロスの娘ギアもいた。ギアはグラヴィクのそばで働いている。",
         "Gravik and G'iah",
         "Gravik's rebels have a base in Russia and operate disguised as humans. Among them is Talos's daughter G'iah, who works close to Gravik."),
        ("ソーニャ・フォルスワース",
         "フューリーが一人で町を歩いていると、男たちに頭に袋をかぶせられ、車で連れ去られる。男たちはイギリスの諜報機関MI6の人間で、フューリーは古い知り合いのソーニャ・フォルスワースのもとへ連れて行かれる。\n"
         "フューリーは、一緒にグラヴィクを止めようと持ちかけるが、ソーニャは断る。フューリーはこっそり、ソーニャの部屋に盗聴の装置をしかけていく。",
         "Sonya Falsworth",
         "Walking alone, Fury is hooded and bundled into a car by MI6 agents, who take him to his old acquaintance Sonya Falsworth.\n"
         "He proposes they work together to stop Gravik; she refuses. Fury secretly leaves a bug in her office."),
        ("ポプリシュチンと、タロスの娘",
         "盗聴で、ソーニャとイギリスの首相の話を聞いたフューリーとタロスは、過激派に汚い爆弾（放射性物質をまき散らす爆弾）を用意した男、ヴァシリー・ポプリシュチンを見つける。2人は問いつめるが、何も聞き出せないまま、フューリーがポプリシュチンを撃ち殺す。\n"
         "タロスは、過激派に加わった娘ギアと会う。タロスが、母ソレンはグラヴィクに殺されたと話すと、ギアは、過激派が「統一の日」の祝いの日に、モスクワの広場をおそう計画だと明かす。ギアは、爆弾の場所に印を付けると約束する。",
         "Poprishchin, and Talos's daughter",
         "Listening in on Sonya and the British Prime Minister, Fury and Talos find Vasily Poprishchin, who got dirty bombs for the rebels. They fail to get anything out of him, and Fury shoots him dead.\n"
         "Talos meets G'iah, who has joined the rebels. When he says Gravik killed her mother Soren, she reveals the rebels will attack a Moscow square on Unity Day, and promises to mark the bombs' locations."),
        ("チェスをする2人",
         "攻撃の前の夜、フューリーとヒルは店の奥でチェスをする。ヒルは、なぜ地球を離れたのか、なぜ戻ってきたのかをたずねる。フューリーは、タロスに借りがあるからだと答える。",
         "A game of chess",
         "The night before the attack, Fury and Hill play chess at the back of a bar. She asks why he left Earth and why he came back. He says he owes it to Talos."),
        ("統一の日の爆発",
         "祝いの日の広場。フューリー、ヒル、タロスは分かれて、印の付いた爆弾を探す。しかし、印の場所にあったのはおとりだった。グラヴィクが本物の爆弾を爆発させ、広場は大混乱になる。",
         "Unity Day bombing",
         "In the square on Unity Day, Fury, Hill and Talos split up to find the marked bombs, but the marked spots are decoys. Gravik sets off the real bombs, and the square descends into chaos."),
        ("ヒルの死",
         "混乱の中、フューリーの姿に化けたグラヴィクがヒルに近づき、ヒルを撃つ。本物のフューリーがかけつけるが、ヒルは助からない。\n"
         "タロスに引っぱられ、フューリーはヒルの体を残して、その場から逃げるしかなかった。",
         "Hill's death",
         "In the chaos, Gravik, disguised as Fury, walks up to Hill and shoots her. The real Fury reaches her, but she cannot be saved.\n"
         "Talos pulls Fury away, and they are forced to flee, leaving her body behind."),
    ]),
    ("第2話 約束", "Episode 2: Promises", [
        ("1997年の約束",
         "1997年。フューリーは、タロスやソレンと一緒に、地球にのがれてきたスクラルたちと会う。クリーとの戦争で親を失った少年のグラヴィクを、フューリーはなぐさめる。\n"
         "フューリーは、スクラルの新しい故郷を探すと約束する。そのかわりに、スクラルたちは人間になりすまし、フューリーのスパイとして地球を守る仕事をすることになる。",
         "The 1997 promise",
         "In 1997, Fury, with Talos and Soren, meets Skrull refugees on Earth. He comforts young Gravik, orphaned in the war with the Kree.\n"
         "Fury promises to find the Skrulls a new home. In return, they will pose as humans and work as his spies protecting Earth."),
        ("列車の中の告白",
         "現在。フューリーとタロスは、列車でモスクワから逃げる。フューリーは、子どものころ母と列車に乗ったときの話をする。\n"
         "タロスは、いま地球には約100万人のスクラルが人間にまぎれて暮らしていると打ち明ける。フューリーは怒り、2人は別れる。",
         "Confession on the train",
         "In the present, Fury and Talos flee Moscow by train. Fury tells a story about riding a train with his mother as a boy.\n"
         "Talos admits about a million Skrulls now live on Earth hidden among humans. Fury is furious, and they part ways."),
        ("ヒルの母",
         "爆発はアメリカのしわざだと疑われる。そう思わせるため、過激派はスクラルの一人ブローガンをアメリカ人として逮捕させていた。\n"
         "フューリーは、ヒルの母エリザベスに会い、娘が死んだいきさつを話す。マリアは、フューリーを苦しめようとした誰かに殺されたのだ。母はフューリーを責める。",
         "Hill's mother",
         "The bombing is blamed on America. To make it look that way, the rebels let a Skrull named Brogan be arrested as an American.\n"
         "Fury meets Hill's mother, Elizabeth, and explains how Maria died: someone killed her to hurt him. She blames him."),
        ("スクラルの評議会",
         "グラヴィクは、人間の大事な立場になりすましているスクラルの評議会に会う。評議会のメンバーは、爆発を起こしたことを責める。グラヴィクは、フューリーが約束を守らなかったことを思い出させる。\n"
         "多数の賛成で、グラヴィクは新しいスクラルの将軍になる。反対したメンバーのシャーリーは、こっそりタロスに連絡する。タロスは、グラヴィクと会えるよう手配を頼む。",
         "The Skrull Council",
         "Gravik meets the Skrull Council, Skrulls posing as powerful humans. They disapprove of the bombing; he reminds them Fury broke his promise.\n"
         "With majority support, Gravik becomes the new Skrull General. Dissenting member Shirley secretly contacts Talos, who asks her to arrange a meeting with Gravik."),
        ("ローディとの話",
         "ロンドン。フューリーは、アメリカ政府で働くジェームズ・ローズ（ローディ）に会い、スクラルのことを伝える。しかしローディは、爆発とヒルの死をフューリーのせいにし、フューリーを今の仕事から外すと告げる。\n"
         "フューリーは、肩書きがなくても自分は危険な男だと言い残す。",
         "Meeting Rhodey",
         "In London, Fury meets James \"Rhodey\" Rhodes, who works for the U.S. government, and warns him about the Skrulls. But Rhodes blames Fury for the bombing and Hill's death and dismisses him from his post.\n"
         "Fury tells him he's still dangerous, title or not."),
        ("ニュー・スクラロスのギア",
         "ロシアにあるグラヴィクの基地「ニュー・スクラロス」。ギアは、過激派が、力を持つ者たちのDNAで実験をしていることをこっそり知る。グルート、カル・オブシディアン、エクストリミスなどのDNAだった。",
         "G'iah at New Skrullos",
         "At Gravik's Russian base, New Skrullos, G'iah secretly learns the rebels are experimenting with DNA from powered beings, such as Groot, Cull Obsidian and Extremis."),
        ("肉屋の取り調べ",
         "ソーニャは、ロシアの情報機関が使う肉屋の奥の隠し部屋へ行き、つかまっているブローガンを取り調べる。ソーニャは指を切って血の色を確かめ、スクラルだと分かると、体の熱を上げる薬で苦しめる。\n"
         "ブローガンは、グラヴィクがスクラルを強くする機械を作っていること、ダルトンという科学者の夫婦が関わっていることを話してしまう。",
         "Interrogation at the butcher's",
         "Sonya goes to a hidden room behind a butcher shop used by Russian intelligence and questions the captured Brogan. She cuts off a finger to check his blood, and, finding he's a Skrull, tortures him with a drug that raises his body heat.\n"
         "Brogan reveals that Gravik is building a machine to make Skrulls stronger, with help from a scientist couple, the Daltons."),
        ("ブローガンの最期",
         "グラヴィクは、ギアやパゴンを連れて肉屋をおそい、見張りの男たちを撃ち殺して、ブローガンを助け出す。ソーニャは床の抜け穴から逃げる。\n"
         "しかしグラヴィクは、ブローガンが取り調べで話してしまったと疑う。一行は車で森へ向かい、ブローガンは森の中で撃ち殺される。",
         "Brogan's end",
         "Gravik, with G'iah and Pagon, raids the butcher shop, shoots the guards and frees Brogan. Sonya escapes through a hatch in the floor.\n"
         "But Gravik suspects Brogan talked. They drive into the woods, and Brogan is shot dead among the trees."),
        ("フューリーの家",
         "フューリーが家に帰ってくる。台所では、緑色のスクラルの姿の女性が野菜を切っている。女性は人間の姿に変わる。フューリーの妻、プリシラだった。\n"
         "プリシラに言われ、フューリーは結婚指輪をはめる。",
         "Fury's home",
         "Fury comes home. In the kitchen, a woman in green Skrull form is chopping vegetables. She shifts into human form: Fury's wife, Priscilla.\n"
         "At her prompting, Fury puts on his wedding ring."),
    ]),
    ("第3話 裏切り", "Episode 3: Betrayed", [
        ("1998年の出会い",
         "1998年、ある食堂。フューリーは、人間の姿のスクラル、ヴァーラと会う。ヴァーラは、ドレイコフの組織に打撃を与える情報が入った封筒をフューリーに渡す。",
         "Meeting in 1998",
         "In 1998, at a diner, Fury meets Varra, a Skrull in human form. She hands him an envelope of intelligence: \"This should put Dreykov's men on their heels.\""),
        ("朝の食卓",
         "現在のフューリーの家。朝ごはんの時間、フューリーはプリシラに、グラヴィクと連絡を取っているのではないかと遠回しにたずね、2人は言い合いになる。プリシラは、こっそりかかってきた電話を受けて出かけていく。",
         "Breakfast",
         "At home in the present, Fury hints over breakfast that Priscilla may be in contact with Gravik, and they argue. She takes a secret phone call and goes out."),
        ("スーパー・スクラルの機械",
         "ニュー・スクラロス。グラヴィクは評議会のメンバーに、科学者ローザ・ダルトンが作った機械を見せる。この機械を使うと、スクラルは姿だけでなく、ヒーローたちの能力まで手に入れられる。グラヴィクは自分で試して、成功していた。\n"
         "グラヴィクは、イギリス海軍にスクラルを入りこませ、国連の飛行機をミサイルで撃ち落とさせる計画も明かす。",
         "The Super-Skrull machine",
         "At New Skrullos, Gravik shows Council members a machine built by scientist Rosa Dalton. With it, Skrulls can take not only heroes' faces but their powers. Gravik has already succeeded on himself.\n"
         "He also reveals he has planted Skrulls in the Royal Navy to shoot down a United Nations plane with a missile."),
        ("ロンドンの店で",
         "ロンドンの店で、タロスとグラヴィクが会う。タロスは、罪のない人を殺すのをやめるよう求める。グラヴィクがギアのことでタロスをあおり、ついにはギアを殺すとおどすと、タロスはナイフでグラヴィクの手をテーブルに突き刺す。\n"
         "そのとき、店の客がみなグラヴィクの仲間だと分かる。グラヴィクは手を引き抜くが、傷は光りながらすぐに治ってしまう。グラヴィクは去っていく。",
         "The café meeting",
         "Talos and Gravik meet at a café in London. Talos asks him to stop killing innocent people. Gravik needles him about G'iah and finally threatens to kill her, and Talos stabs Gravik's hand to the table with a knife.\n"
         "The other customers turn out to be Gravik's people. Gravik pulls his hand free; the wound glows and heals at once. He leaves."),
        ("ふたたび組む2人",
         "ギアは、ミサイル攻撃の情報を、こっそりタロスに送る。\n"
         "フューリーは、こんなに多くのスクラルを地球に入れたタロスに怒っていたが、グラヴィクを止めるため、タロスに助けを頼む。\n"
         "フューリーが電話すると、ソーニャは、自分の部屋にしかけられた装置に気づいていたと文句を言う。それでも、ミサイルを担当する海軍の司令官ロバート・フェアバンクスの名前を教えてくれる。",
         "Teaming up again",
         "G'iah secretly sends Talos details of the missile strike.\n"
         "Fury is angry that Talos let so many Skrulls onto Earth, but asks him for help stopping Gravik.\n"
         "When Fury calls Sonya, she scolds him for planting a device in her office, but gives him the name of the naval officer in charge: Commodore Robert Fairbanks."),
        ("車の中の言い合い",
         "フェアバンクスの家へ向かう車の中で、フューリーとタロスは30年の付き合いについて言い合う。タロスは、スクラルの仲間の助けがなければ、フューリーが世界一のスパイになることはなかったと言う。",
         "Argument in the car",
         "On the drive to Fairbanks's house, Fury and Talos argue about their 30 years together. Talos says Fury would never have become the world's top spy without his hidden Skrull network."),
        ("フェアバンクスの家",
         "フューリーとタロスは、フェアバンクスの家に忍びこんで問いつめる。フェアバンクスは、なりすましたスクラルだった。にせのフェアバンクスはタロスをあおり、タロスは止める方法を聞き出す前に、彼を撃ち殺してしまう。\n"
         "タロスはギアに連絡する。ギアは、基地にとらえられている本物のフェアバンクスの記憶から、ミサイルを止める暗号を手に入れる。発射はぎりぎりで止められた。",
         "Fairbanks's house",
         "Fury and Talos break into Fairbanks's home and interrogate him. He is a Skrull impostor. He provokes Talos, who shoots him dead before learning how to stop the launch.\n"
         "Talos contacts G'iah. From the memories of the real Fairbanks, held prisoner at the base, she gets the abort code. The launch is stopped just in time."),
        ("ギアが撃たれる",
         "正体がばれたギアは、基地から逃げようとする。しかし、ギアの裏切りを疑っていたグラヴィクに見つかり、目の前で撃たれる。グラヴィクは、ギアをその場に置いて去る。",
         "G'iah is shot",
         "Her cover blown, G'iah tries to leave the base. Gravik, who suspected her, catches her and shoots her at point-blank range, leaving her for dead."),
        ("プリシラの電話",
         "プリシラは、銀行の貸金庫を開ける。中には銃が入っていた。プリシラは電話で、グラヴィクと話したいと言うが、断られる。",
         "Priscilla's call",
         "Priscilla opens a bank safety-deposit box with a gun inside. On the phone she asks to speak with Gravik, but is turned down."),
    ]),
    ("第4話 愛された者", "Episode 4: Beloved", [
        ("よみがえるギア",
         "道に倒れているギア。実はギアは、逃げる前にこっそりグラヴィクの機械を使い、エクストリミスの力を自分の体に入れていた。撃たれた傷は光りながら治り、ギアは起き上がる。",
         "G'iah revives",
         "G'iah lies in the road. Before trying to flee, she had secretly used Gravik's machine to give herself Extremis powers. Her wound glows and heals, and she sits up."),
        ("タロスとギア",
         "ギアは父タロスと会う。タロスは、フューリーと過激派を止めたあと、アメリカのリットソン大統領にスクラルを助けてもらうよう頼むつもりだと話す。新しい故郷を探す強い計画を期待していたギアは、がっかりして去る。",
         "Talos and G'iah",
         "G'iah meets her father. Talos says that once he and Fury stop the rebels, he plans to ask U.S. President Ritson to help the Skrulls. G'iah, hoping for a stronger plan to find a new home, walks away disappointed."),
        ("2012年のパリ",
         "2012年、ニューヨークの戦いの少しあと。パリのレストランで、フューリーとプリシラ（ヴァーラ）が食事をする。プリシラは、アベンジャーズを集めたフューリーをほめ、レイモンド・カーヴァーの詩「おしまいの断片」を口にする。",
         "Paris, 2012",
         "In 2012, shortly after the Battle of New York, Fury and Priscilla (Varra) dine in Paris. She praises him for assembling the Avengers and recites Raymond Carver's poem \"Late Fragment.\""),
        ("教会の会合",
         "現在。プリシラは教会でローディと会う。このローディは、グラヴィクの仲間のスクラルだった。ローディは、フューリーを殺すようプリシラに命じる。\n"
         "フューリーは、この会話をこっそり聞いていた。",
         "Meeting at the church",
         "In the present, Priscilla meets Rhodey at a church. This Rhodey is a Skrull working with Gravik, and orders her to kill Fury.\n"
         "Fury has been secretly listening."),
        ("妻との対決",
         "家に戻ったプリシラを、フューリーが待っている。2人は銃を向け合う。フューリーが、その顔の持ち主のことをたずねると、プリシラは本物のプリシラ・デイヴィスの話をする。\n"
         "本物のプリシラは、心臓の病気で死にかけていた。ヴァーラは彼女と親しくなり、死んだあとにその姿を使ってよいと許される。そのかわり、海に葬ること、両親を大切にすること、そして、この姿で愛した男を決して傷つけないことを約束した。だからプリシラは、フューリーを殺せない。\n"
         "2人は同時に引き金を引くが、どちらもわざと外す。去っていくフューリーに、プリシラは、本当の姿の自分でも愛してくれたかとたずねる。",
         "Showdown with his wife",
         "Fury is waiting when Priscilla gets home. They draw guns. He asks about the woman whose face she wears, and she tells him about the real Priscilla Davis.\n"
         "Dying of a heart condition, Priscilla befriended Varra and let her take her identity after death, on conditions: bury her at sea, care for her parents, and never harm the man she came to love in that form. That oath is why she cannot kill Fury.\n"
         "They fire at the same moment, both missing on purpose. As Fury leaves, she asks whether he would have loved her in her true form."),
        ("ローディとの1杯",
         "フューリーは、ローディのホテルの部屋をたずね、上等なバーボンを一緒に飲む。酒には、居場所を知らせる液体の発信機がこっそり入っていた。",
         "A drink with Rhodey",
         "Fury visits Rhodey's hotel suite with a fine bourbon and they drink together. The drink secretly contains a liquid tracker."),
        ("大統領の車列がおそわれる",
         "ローディが、リットソン大統領を迎えに行く。フューリーとタロスは、発信機でローディの後を追う。\n"
         "道の途中で、ロシアのテロリストに化けたグラヴィクたちが大統領の車列をおそう。大統領の車はひっくり返り、リットソンは気を失う。",
         "The motorcade attack",
         "Rhodey goes to pick up President Ritson. Fury and Talos follow using the tracker.\n"
         "On the road, Gravik and the rebels, disguised as Russian terrorists, attack the motorcade. The President's car is overturned and Ritson is knocked out."),
        ("タロスの死",
         "タロスは、ひっくり返った車からリットソンを助け出そうとするが、グラヴィクの右腕パゴンに撃たれ、スクラルの姿に戻る。イギリス軍がかけつけ、フューリーとタロスは、気を失ったリットソンを車から引っぱり出す。\n"
         "そこへ、イギリス兵に化けたグラヴィクが近づき、タロスをナイフで刺す。タロスはその場で死ぬ。\n"
         "フューリーはリットソンを車に乗せて逃げ、道に倒れたタロスを残していく。",
         "Talos's death",
         "Talos tries to reach Ritson in the overturned car, but Gravik's lieutenant Pagon shoots him and he reverts to Skrull form. British troops arrive, and Fury and Talos pull the unconscious Ritson out.\n"
         "Then Gravik, disguised as a British soldier, approaches and stabs Talos with a knife. Talos dies there.\n"
         "Fury drives Ritson away, leaving Talos's body on the road."),
    ]),
    ("第5話 収穫", "Episode 5: Harvest", [
        ("病院のリットソン",
         "リットソン大統領は病院に運ばれる。フューリーは、意識のない大統領のそばで、ローディを信じるなと言い聞かせる。\n"
         "そこへローディ（実はスクラル）が来る。ローディは、ヒルが撃たれた場面の映像をマスコミに流したと告げる。フューリーの姿に化けたグラヴィクの映像なので、フューリーがヒルを殺したように見える。フューリーは、世界中から追われる身になる。",
         "Ritson in hospital",
         "President Ritson is rushed to hospital. Beside his unconscious bed, Fury tells him: \"Do not trust Rhodes.\"\n"
         "Rhodey (really a Skrull) arrives and tells Fury he has leaked footage of Hill's shooting. Because it shows Gravik disguised as Fury, it looks as if Fury killed her. Fury becomes a wanted man worldwide."),
        ("パゴンとベトの反乱",
         "ニュー・スクラロス。右腕のパゴンは、仲間の前でグラヴィクを責める。フューリーを殺せなかったし、フューリーは大事なものの場所をグラヴィクに教えなかった、それなのになぜグラヴィクを信じられるのかと。グラヴィクは、木のように変えた腕でパゴンの胸をつらぬいて殺す。\n"
         "新入りのベトは、何人かの仲間と一緒にグラヴィクにおそいかかる。しかし、能力を手に入れたグラヴィクにはかなわず、全員が殺される。ベトは見せしめとして、仲間たちの前で殺される。",
         "Pagon and Beto's mutiny",
         "At New Skrullos, Pagon criticizes Gravik in front of the others: he failed to kill Fury, and Fury never trusted him with something important, so why should they trust him? Gravik turns his arm into wood and impales Pagon through the chest.\n"
         "New recruit Beto and a few others attack Gravik, but his powers overwhelm them and he kills them all, killing Beto in front of the others as a warning."),
        ("ソーニャとウェザビー",
         "グラヴィクは、ローディに化けたスクラルに、ニュー・スクラロスの写真をリットソンに見せるよう命じる。ロシアがスクラルと組んでいると思わせ、基地を攻撃させるためだ。\n"
         "ロンドンでは、ソーニャが上司のデリック・ウェザビーを撃つ。傷からスクラルだと分かったウェザビーは、科学者ローザ・ダルトンの居場所を明かす。",
         "Sonya and Weatherby",
         "Gravik orders the Skrull posing as Rhodey to show Ritson photos of New Skrullos, to make it look as if Russia is siding with the Skrulls and push for a strike on the base.\n"
         "In London, Sonya shoots her superior, Derrik Weatherby. The wound shows he's a Skrull, and he gives up the location of scientist Rosa Dalton."),
        ("ハーベスト",
         "隠れ家で、フューリーは父を亡くしたギアと会う。ギアは、グラヴィクが本当にねらっているのは「ハーベスト」というものだと話す。\n"
         "フューリーは打ち明ける。アベンジャーズが地球で最後に戦ったあと、フューリーはグラヴィクをふくむスクラルたちに、戦った者たちの血やDNAをこっそり集めさせていたのだ。",
         "The Harvest",
         "At a safehouse, Fury meets the grieving G'iah. She says what Gravik really wants is something called the Harvest.\n"
         "Fury admits that after the Avengers' final battle on Earth, he had a team of Skrulls, Gravik among them, secretly collect blood and DNA from everyone who fought."),
        ("ダルトン夫妻の研究所",
         "ソーニャは、ダルトン夫妻の研究所へ行く。ローザは、なりすましたスクラルだった。ソーニャはローザから、グラヴィクの機械のことを聞き出す。\n"
         "ヴィクターはローザに銃を向け、グラヴィクを裏切らせないと言う。ソーニャは、ヴィクターを撃ち殺す。ソーニャは研究所に火をつけ、研究の資料を持ち去る。",
         "The Daltons' lab",
         "Sonya goes to the Daltons' lab. Rosa is a Skrull impostor. Sonya gets Rosa to explain Gravik's machine.\n"
         "Victor holds a gun to Rosa, saying he won't let her betray Gravik. Sonya shoots him dead, then burns the lab and takes the research."),
        ("グラヴィクの電話",
         "グラヴィクはフューリーに電話をかけ、ニュー・スクラロスへの攻撃が近いことを伝える。ハーベストを直接持ってくれば攻撃を止めてやる、と持ちかける。",
         "Gravik's call",
         "Gravik calls Fury about the coming strike on New Skrullos and offers to have it called off if Fury brings him the Harvest in person."),
        ("タロスの葬式と、家への襲撃",
         "ギアとヴァーラ（プリシラ）は、家の外で、タロスの体を火で送る小さな葬式をする。\n"
         "そこへ、グラヴィクの送った男たちが窓から撃ちこみ、家に押し入ってくる。ギアとヴァーラは、男たちを倒す。",
         "Talos's funeral, and the attack",
         "Outside the house, G'iah and Varra (Priscilla) hold a small funeral, burning Talos's body on a pyre.\n"
         "Gravik's men shoot through the windows and break in. G'iah and Varra fight them off and kill them."),
        ("フィンランドの墓",
         "追われる身のフューリーは、昔の知り合いリック・メイソンの飛行機でフィンランドへ向かう。メイソンは、古いS.H.I.E.L.D.の道具をフューリーに渡す。\n"
         "フィンランドの墓地で、フューリーはソーニャと会う。フューリーの名前が刻まれた墓の中に、ハーベストが隠されていた。アベンジャーズの最後の戦いで戦った者たちのDNAだ。\n"
         "フューリーは、そこにしまっていた眼帯と黒いコートを身に着け、最後の戦いへ向かう。",
         "The grave in Finland",
         "Now a fugitive, Fury flies to Finland on old contact Rick Mason's jet. Mason gives him an old S.H.I.E.L.D. device.\n"
         "At a Finnish cemetery, Fury meets Sonya. Hidden in a grave bearing Fury's own name is the Harvest: DNA from those who fought in the Avengers' final battle.\n"
         "Fury puts on the eyepatch and black coat stored there and sets out for the final showdown."),
    ]),
    ("第6話 故郷", "Episode 6: Home", [
        ("別れの電話",
         "フューリーはヴァーラに電話をかける。生きて帰れるか分からない、別れのような電話だった。",
         "A farewell call",
         "Fury calls Varra in what sounds like a goodbye; he isn't sure he'll come back."),
        ("ニュー・スクラロスの話し合い",
         "眼帯のフューリーが、ニュー・スクラロスに乗りこむ。フューリーはグラヴィクにハーベストを渡し、地球を見逃して、ほかの星を手に入れるよう頼む。グラヴィクは断る。\n"
         "グラヴィクは、長い間陰で働かされたのに故郷は見つからなかったとフューリーを責める。今のグラヴィクの人間の顔は、フューリーのための最初の任務で殺した男の顔だった。",
         "Talks at New Skrullos",
         "An eyepatched Fury walks into New Skrullos. He gives Gravik the Harvest and asks him to spare Earth and take other planets instead. Gravik refuses.\n"
         "Gravik blames Fury: the Skrulls worked in the shadows for decades and never got a home. His human face belongs to the first man he killed on his first mission for Fury."),
        ("ハーベストの力",
         "グラヴィクは、ハーベストのDNAを機械に入れ、さらに強い力を手に入れる。その間、フューリーも機械の中にいて、同じ力を受けていた。\n"
         "病院では、ローディに化けたスクラル（ラーヴァ）が、ニュー・スクラロスへの核攻撃をリットソン大統領に認めさせる。",
         "The Harvest's power",
         "Gravik loads the Harvest DNA into the machine and gains even greater powers. Fury is inside the machine at the same time, receiving the same powers.\n"
         "At the hospital, the Skrull posing as Rhodey (Raava) persuades President Ritson to approve a nuclear strike on New Skrullos."),
        ("フューリーの正体",
         "力を得たグラヴィクは、フューリーを殺そうとする。しかしフューリーはその一撃を受け止め、グラヴィクを建物の外まで吹き飛ばす。フューリーの正体は、フューリーに化けたギアだった。",
         "Who \"Fury\" really is",
         "The empowered Gravik tries to kill Fury, but \"Fury\" stops the blow and sends him flying out of the building. It's G'iah, disguised as Fury."),
        ("スーパー・スクラルの戦い",
         "同じ力を持つ2人が戦う。グラヴィクはエボニー・マウの力でギアを投げ飛ばし、車を投げつける。ギアは、ゴーストの力で車をすり抜ける。2人はキャプテン・マーベルの力で空を飛ぶ。\n"
         "空中で首をしめられたギアは、マンティスの力でグラヴィクを眠らせ、地面に落とす。最後にギアは、キャプテン・マーベルの光線でグラヴィクの胸をつらぬき、倒す。",
         "Super-Skrull battle",
         "With the same powers, they fight. Gravik uses Ebony Maw's telekinesis to throw G'iah and hurls a car; she phases through it with Ghost's ability. Both fly with Captain Marvel's powers.\n"
         "Choked in mid-air, G'iah uses Mantis's power to put Gravik to sleep, and he falls. Finally she blasts through his chest with Captain Marvel's energy and kills him."),
        ("病院の本物のフューリー",
         "本物のフューリーはソーニャと一緒にいた。ソーニャはローディ（ラーヴァ）に電話し、フューリーが大統領をおそいに来ると知らせて、リットソンを病院の上の階へ移させる。\n"
         "フューリーとソーニャは、大統領の警護の人たちを眠らせる薬の矢で倒し、病室に入る。フューリーはリットソンに、ローディはスクラルで、車列の襲撃もスクラルのしわざだと伝える。\n"
         "ラーヴァがおそいかかろうとした瞬間、フューリーがラーヴァの頭を撃ち抜く。リットソンはすぐに核攻撃を取りやめる。",
         "The real Fury at the hospital",
         "The real Fury is with Sonya. She calls Rhodey (Raava), warning that Fury is coming to attack the President, and gets Ritson moved to an upper floor.\n"
         "Fury and Sonya take down the Secret Service agents with tranquilizer darts and enter the room. Fury tells Ritson that Rhodey is a Skrull and that Skrulls staged the motorcade attack.\n"
         "When Raava lunges, Fury shoots her in the head. Ritson immediately calls off the strike."),
        ("本物のローディ",
         "ニュー・スクラロスでは、ギアが、機械の中にとらえられていた人間たちを助け出す。その中には、エヴェレット・ロスと本物のジェームズ・ローズ（ローディ）もいた。病院の服のローディは、助けを借りてやっと歩く。ローディは長い間とらえられていたのだ。",
         "The real Rhodey",
         "At New Skrullos, G'iah frees the humans held in the pods, among them Everett Ross and the real James Rhodes. Wearing a hospital gown, Rhodey needs help to walk; he has been held for a long time."),
        ("大統領の宣言",
         "リットソン大統領はテレビで、スクラルが地球に入りこんでいたことを明かし、地球の外から来た者すべてを敵とする法律を進め、残ったスクラルを探し出すと宣言する。\n"
         "人々は不安にかられ、スクラルではないかと疑われた要人たちが、人前で殺される事件まで起きる。\n"
         "フューリーはリットソンに、このやり方は罪のない人を死なせると忠告するが、リットソンは聞き入れない。",
         "The President's declaration",
         "On TV, President Ritson reveals the Skrull infiltration, pushes a bill declaring all off-world beings hostile, and vows to hunt down the Skrulls left on Earth.\n"
         "Fear spreads, and people publicly murder officials they suspect of being Skrulls.\n"
         "Fury warns Ritson the policy will get innocent people killed, but Ritson won't listen."),
        ("ソーニャとギア",
         "ソーニャはギアと会い、大統領の法律からスクラルを守るため、手を組もうと持ちかける。",
         "Sonya and G'iah",
         "Sonya meets G'iah and proposes a partnership to protect the Skrulls from the President's bill."),
        ("宇宙へ",
         "フューリーはヴァーラに、クリーが平和の話し合いに応じると話し、話し合いを手伝うため一緒にセイバーへ来てほしいと頼む。\n"
         "ヴァーラは、人間の姿をやめてスクラルの本当の姿で現れ、うなずく。2人は一緒に地球を離れる。",
         "Into space",
         "Fury tells Varra the Kree are open to peace talks and asks her to come with him to S.A.B.E.R. to help negotiate.\n"
         "Varra appears in her true Skrull form and agrees. They leave Earth together."),
    ]),
    ("まとめ（最終話までのネタバレ）", "Summary (spoilers through the finale)", [
        ("なりすましていたスクラル",
         "・エヴェレット・ロス（第1話）：にせもの。死んで正体が分かる。本物は基地にとらえられていて、第6話で助け出される。\n"
         "・ローディ（ジェームズ・ローズ）：スクラルのラーヴァ。第4話で正体が分かり、第6話でフューリーに撃たれる。本物は長い間とらえられていて、第6話で助け出される。\n"
         "・プリシラ（フューリーの妻）：スクラルのヴァーラ。本物のプリシラとの約束で、フューリーを傷つけない（第4話）。最後はフューリーと宇宙へ。\n"
         "・フェアバンクス司令官（第3話）、MI6のウェザビー（第5話）、科学者のローザ・ダルトン（第5話）もスクラルだった。",
         "Skrulls in disguise",
         "- Everett Ross (Ep. 1): an impostor, exposed when he dies. The real Ross is held at the base and freed in Ep. 6.\n"
         "- Rhodey (James Rhodes): the Skrull Raava, revealed in Ep. 4 and shot by Fury in Ep. 6. The real Rhodey, held for a long time, is freed in Ep. 6.\n"
         "- Priscilla (Fury's wife): the Skrull Varra, bound by her promise to the real Priscilla never to harm Fury (Ep. 4). She leaves for space with Fury.\n"
         "- Commodore Fairbanks (Ep. 3), MI6's Weatherby (Ep. 5) and scientist Rosa Dalton (Ep. 5) were Skrulls too."),
        ("死んだ人たち（話の順に）",
         "・プレスコット（第1話）：スクラルの計画を調べていた元CIA。にせのロスに殺される。\n"
         "・にせのロス（第1話）：タロスに追われて屋根から落ちて死ぬ。\n"
         "・ポプリシュチン（第1話）：爆弾を用意した男。何も話さないまま、フューリーに撃たれる。\n"
         "・マリア・ヒル（第1話）：統一の日の爆発の混乱の中で、フューリーに化けたグラヴィクに撃たれる。広場の多くの人も爆発で亡くなる。\n"
         "・ブローガン（第2話）：取り調べで話してしまったと疑われ、グラヴィクの命令で森の中で撃たれる。\n"
         "・にせのフェアバンクス（第3話）：タロスをあおり、撃ち殺される。\n"
         "・タロス（第4話）：大統領を助け出す途中、イギリス兵に化けたグラヴィクにナイフで刺される。\n"
         "・パゴン（第5話）：グラヴィクを責めたため、木に変えた腕で胸をつらぬかれる。\n"
         "・ベトたち（第5話）：グラヴィクに反乱を起こし、全員殺される。\n"
         "・ヴィクター・ダルトン（第5話）：ローザに銃を向け、ソーニャに撃たれる。\n"
         "・グラヴィク（第6話）：ハーベストの力を得たギアと戦い、光線で胸をつらぬかれる。\n"
         "・ラーヴァ（にせのローディ、第6話）：病室でおそいかかろうとし、フューリーに撃たれる。",
         "Who died (in order)",
         "- Prescod (Ep. 1): ex-CIA man who uncovered the Skrull plot; killed by the fake Ross.\n"
         "- The fake Ross (Ep. 1): falls from a roof while chased by Talos.\n"
         "- Poprishchin (Ep. 1): the bomb supplier; shot by Fury after refusing to talk.\n"
         "- Maria Hill (Ep. 1): shot by Gravik disguised as Fury in the chaos of the Unity Day bombing, which also kills many in the square.\n"
         "- Brogan (Ep. 2): suspected of talking under interrogation; shot in the woods on Gravik's orders.\n"
         "- The fake Fairbanks (Ep. 3): provokes Talos and is shot.\n"
         "- Talos (Ep. 4): stabbed by Gravik, disguised as a British soldier, during the President's rescue.\n"
         "- Pagon (Ep. 5): impaled through the chest by Gravik's wooden arm for challenging him.\n"
         "- Beto and his group (Ep. 5): killed by Gravik after their mutiny.\n"
         "- Victor Dalton (Ep. 5): shot by Sonya after holding a gun to Rosa.\n"
         "- Gravik (Ep. 6): killed by G'iah, empowered by the Harvest, with an energy blast through the chest.\n"
         "- Raava, the fake Rhodey (Ep. 6): shot by Fury when she lunges in the hospital room."),
    ]),
]
