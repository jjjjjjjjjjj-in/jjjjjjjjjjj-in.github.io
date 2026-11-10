# 『アイアンマン』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。以前は films.py の scenes に入っていたものをここへ移した。
# 英語版・日本語版ウィキペディアのあらすじ（Plot／ストーリー）と登場人物の記事で事実を確かめた。資料どうしで食い違う所や、確かめられないせりふ・細かい順番は書いていない。
# 日本語版のカギかっこのせりふは、日本語版ウィキペディアで確かめた「私がアイアンマンだ」だけ。ほかは内容だけを書いている。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 アフガニスタンでの襲撃", "Part 1: Ambush in Afghanistan", [
        ("砂漠を走る車列",
         "アフガニスタンの砂漠を、アメリカ軍の車列が走っている。1台の車に乗っているのは、兵器会社スターク・インダストリーズの社長トニー・スタークだ。\n"
         "トニーはグラスを片手に冗談を言い、緊張している若い兵士たちを笑わせる。兵士の一人にたのまれて、一緒に写真まで撮る。",
         "The convoy",
         "A U.S. military convoy crosses the Afghan desert. In one vehicle rides Tony Stark, head of the weapons maker Stark Industries.\n"
         "Drink in hand, Tony cracks jokes with the nervous young soldiers and even poses for a photo when one of them asks."),
        ("待ち伏せ",
         "そのとき、車列が爆発に巻き込まれる。テロ組織の待ち伏せだ。トニーと同じ車の兵士たちは外へ飛び出して応戦するが、次々に撃たれて倒れていく。\n"
         "トニーは岩のかげに逃げこむ。その足もとにミサイルが落ちてくる。ミサイルには、自分の会社「スターク・インダストリーズ」の文字があった。\n"
         "ミサイルが爆発し、トニーは胸に大けがをして倒れる。",
         "The ambush",
         "Suddenly the convoy is hit by explosions. It's an ambush by a terrorist group. The soldiers in Tony's vehicle jump out to fight back and are shot down one after another.\n"
         "Tony hides behind a rock. A missile lands at his feet, stamped with his own company's name: Stark Industries.\n"
         "It explodes, and Tony goes down with a serious chest wound."),
        ("カメラの前",
         "気がつくと、トニーは頭に袋をかぶせられ、武装した男たちに囲まれてビデオカメラの前に座らされている。男たちの一人が、カメラに向かって声明を読み上げている。\n"
         "画面はここで「36時間前」にさかのぼる。",
         "On camera",
         "Tony comes to with a hood over his head, surrounded by armed men in front of a video camera while one of them reads a statement.\n"
         "The film then jumps back to \"36 hours earlier.\""),
        ("ラスベガスの授賞式",
         "ラスベガスで、トニーの功績をたたえる授賞式が開かれている。会場のスクリーンでは、天才少年として育ち、亡くなった父ハワードの会社を若くして継いだトニーの経歴が紹介される。\n"
         "賞を渡す役は、トニーの親友で空軍の軍人ローディ（ジェームズ・ローズ）。ところが本人は会場に来ない。賞は、父の代からの共同経営者オバディア・ステインが代わりに受け取る。\n"
         "トニーはカジノで遊んでいた。ローディが探しに行き、そこで賞を手渡す。",
         "An award in Las Vegas",
         "In Las Vegas, an award ceremony honors Tony. A video recaps his life: a boy genius who took over the company of his late father, Howard, at a young age.\n"
         "His best friend, Air Force officer Rhodey (James Rhodes), is there to present the award, but Tony never shows. Obadiah Stane, his father's longtime partner, accepts it for him.\n"
         "Tony is gambling in the casino. Rhodey finds him and hands him the award there."),
        ("記者クリスティン",
         "カジノを出たトニーの前に、雑誌の記者クリスティン・エヴァーハートが現れる。クリスティンは、トニーが「死の商人」と呼ばれていることをどう思うかと、厳しい質問をぶつける。\n"
         "トニーは、武器があるから平和が守られているのだと軽く言い返す。そしてその夜、彼女を家に連れて帰る。",
         "Reporter Christine",
         "Outside the casino, magazine reporter Christine Everhart confronts Tony, asking how he feels about being called a \"merchant of death.\"\n"
         "Tony breezily answers that weapons are what keep the peace, and takes her home that night."),
        ("翌朝のペッパー",
         "翌朝、家の人工知能ジャーヴィスの声で、クリスティンが目を覚ます。彼女を送り出すのは、トニーの秘書ペッパー・ポッツだ。ペッパーは、自由気ままなトニーの予定から身の回りのことまで、すべてを取り仕切っている。\n"
         "トニーは地下の工房で車いじりをしていて、出発の時間をとっくに過ぎている。ペッパーにせかされて、ようやくアフガニスタンへの出張に向かう。",
         "Pepper the next morning",
         "The next morning, the house's AI, J.A.R.V.I.S., wakes Christine. Tony's assistant, Pepper Potts, shows her out. Pepper runs everything in Tony's freewheeling life, from his schedule to his errands.\n"
         "Tony is down in his workshop tinkering with a car, long past his departure time. Pushed by Pepper, he finally leaves for his trip to Afghanistan."),
        ("待たされたローディ",
         "空港では、ローディがずっと待たされていた。会社の自家用ジェットの中で、トニーとローディは言い合いをしながらも、長い付き合いの親友らしく打ちとける。",
         "Rhodey waits",
         "At the airfield, Rhodey has been waiting for hours. On the company jet the two bicker, but they relax like the old friends they are."),
        ("新型ミサイル「ジェリコ」",
         "アフガニスタンの軍の基地。トニーは軍の人々の前で、新型ミサイル「ジェリコ」の試射を見せる。トニーは、一度撃つだけで済む武器のほうがいいと言って、売り込む。\n"
         "1発のミサイルから小さな爆弾がいくつも飛び出し、山の斜面がまるごと吹き飛ぶ。軍人たちはその威力に驚く。\n"
         "その帰り道に、冒頭の襲撃が起きたのだった。",
         "The Jericho",
         "At a base in Afghanistan, Tony demonstrates his new missile, the Jericho, for military officials, pitching it as the kind of weapon you only have to fire once.\n"
         "One missile splits into many smaller bombs and levels an entire hillside. The officers are stunned.\n"
         "On the drive back, the ambush from the opening happens."),
    ]),
    ("第2部 洞窟の捕虜", "Part 2: Prisoner in the cave", [
        ("胸の電磁石",
         "トニーが目を覚ますと、そこは洞窟の中。胸には電磁石が埋め込まれ、車のバッテリーにつながっている。\n"
         "手術をしたのは、同じく捕まっている医師のインセンだった。ミサイルの細かい破片がトニーの体に残っていて、心臓に届けば死んでしまう。電磁石は、その破片を引き止めるためのものだった。\n"
         "インセンは、昔ベルンの学会でトニーに会ったことがあると話す。トニーは酔っていて覚えていない。",
         "A magnet in his chest",
         "Tony wakes up in a cave with an electromagnet in his chest, wired to a car battery.\n"
         "The surgery was done by Yinsen, a doctor also being held prisoner. Tiny fragments from the missile are still in Tony's body and would kill him if they reached his heart. The magnet holds them back.\n"
         "Yinsen says they once met at a conference in Bern. Tony, who was drunk at the time, doesn't remember."),
        ("テン・リングスの要求",
         "トニーを捕まえたのはテロ組織「テン・リングス」の一団だ。男たちはトニーを洞窟の外へ連れ出す。そこには、スターク社の武器が山のように積まれていた。自分の会社の武器が、テロ組織の手に渡っていたのだ。\n"
         "男たちは、トニーに「ジェリコ」を作れと命じる。トニーは断るが、水の中に何度も頭を沈められる。",
         "The Ten Rings' demand",
         "Tony's captors are a cell of the terrorist group called the Ten Rings. They lead him outside the cave, where Stark weapons are piled high. His own company's weapons have ended up in terrorist hands.\n"
         "They order him to build a Jericho. When he refuses, they repeatedly dunk his head under water."),
        ("ひそかな計画",
         "トニーは、ミサイルを作っても約束どおり帰してもらえるとは思えなかった。インセンも同じ考えだった。\n"
         "そこでトニーはミサイルを作ることを引き受けたふりをして、材料を集める。本当は、ここから逃げ出すための鉄のスーツを作るつもりだった。見張りのカメラに見られながら、2人は作業を始める。",
         "A secret plan",
         "Tony doesn't believe they'll let him go even if he builds the missile, and Yinsen agrees.\n"
         "So Tony pretends to accept and gathers materials. His real plan is to build an iron suit to escape. Watched by the guards' cameras, the two get to work."),
        ("小さなアーク・リアクター",
         "トニーはまず、ミサイルから取り出した金属を使って、手のひらほどの大きさの発電装置「アーク・リアクター」を作る。会社の工場にある大きな発電装置を、小さく作り直したものだ。\n"
         "これを胸にはめると、車のバッテリーはいらなくなった。この装置は、スーツを動かす力にもなる。",
         "A small arc reactor",
         "First, using metal taken from the missiles, Tony builds a palm-sized power source, an arc reactor: a shrunk-down version of the big generator at his company's plant.\n"
         "Once it's in his chest, he no longer needs the car battery. It will also power the suit."),
        ("設計図とインセンの問い",
         "トニーは鉄のスーツの設計図を何枚かに分けて描く。1枚ずつなら、ミサイルの図に見えるようにするためだ。2人は少しずつ部品を作っていく。\n"
         "作業の合間に、インセンはトニーに家族はいるのかとたずねる。いないと答えるトニーに、インセンは、何でも持っているのに何も持っていない男だと言う。インセンは、自分の故郷はグルミラという村で、家族がいると話す。",
         "The plans, and Yinsen's question",
         "Tony draws the suit's plans in separate pieces, so that each sheet on its own looks like part of a missile. Bit by bit, the two build the parts.\n"
         "Between tasks, Yinsen asks Tony if he has a family. When Tony says no, Yinsen calls him a man who has everything and nothing. Yinsen says his own family is in his home village, Gulmira."),
        ("ラザの脅し",
         "一団のリーダー、ラザが洞窟に来る。ラザは、昔チンギス・ハンの弓が国を支配したように、今はスターク社の新しい武器を持つ者がこの地を支配するのだと話す。\n"
         "ラザは作業がなかなか進まないことにいら立ち、インセンの口に焼けた炭を入れようとして脅す。トニーはインセンが必要な助手だと言ってかばう。ラザは、残された時間は少ないと告げて去る。",
         "Raza's threat",
         "The cell's leader, Raza, visits the cave. Just as Genghis Khan's bow once ruled these lands, he says, now whoever holds the newest Stark weapons rules them.\n"
         "Frustrated with the slow progress, Raza threatens to put a hot coal in Yinsen's mouth. Tony protects him, saying he needs his assistant. Raza leaves, warning that they're running out of time."),
    ]),
    ("第3部 洞窟からの脱出", "Part 3: Escape from the cave", [
        ("スーツの起動",
         "鉄のスーツ（マーク1）が組み上がる。トニーがスーツを身につけ、インセンがパソコンで起動の作業を進める。しかし起動して動けるようになるまでには、時間がかかる。",
         "Powering up the suit",
         "The iron suit, the Mark I, is assembled. Tony climbs in while Yinsen starts it up on a computer, but it will take time before the suit can move."),
        ("気づかれた計画",
         "その間に、男たちが2人の計画に気づく。兵士たちが作業場に押し寄せ、扉を開けようとする。\n"
         "2人が扉にしかけておいた爆弾が爆発し、兵士たちは足止めされる。",
         "The plan is discovered",
         "Meanwhile, the captors realize what the two are up to. Soldiers rush the workshop and try to force the door.\n"
         "A bomb the two had rigged at the door goes off and holds the soldiers back."),
        ("インセンの犠牲",
         "インセンは、スーツが動き出すまでの時間をかせぐため、銃を手に取り、洞窟の通路へ飛び出していく。インセンは銃を撃ちながら走り、兵士たちの注意を引きつける。",
         "Yinsen's sacrifice",
         "To buy time for the suit to come online, Yinsen grabs a gun and runs out into the tunnels, firing as he goes and drawing the soldiers away."),
        ("マーク1で進む",
         "スーツが動き出す。灰色の鉄のかたまりのようなスーツで、トニーは通路を進む。兵士たちの銃弾は、スーツにはね返される。トニーは鉄の腕で兵士たちをなぎ倒していく。",
         "The Mark I moves",
         "The suit comes to life. In the bulky gray armor, Tony marches through the tunnels. Bullets bounce off, and he knocks the soldiers aside with his iron arms."),
        ("インセンの最期",
         "通路の先で、トニーは撃たれて倒れているインセンを見つける。インセンは兵士たちに撃たれていた。\n"
         "インセンは、家族はもう死んでいて、これで家族のもとへ行けるのだと話す。そしてトニーに、命を無駄にするなと言い残して息を引き取る。",
         "Yinsen's last words",
         "Further along, Tony finds Yinsen lying on the ground, shot by the soldiers.\n"
         "Yinsen says his family is already dead, and now he will see them again. He tells Tony, \"Don't waste your life,\" and dies."),
        ("武器を焼いて空へ",
         "洞窟の外へ出たトニーは、腕の火炎放射器で、積まれていたスターク社の武器を焼き払う。武器が次々に爆発する。\n"
         "トニーはスーツのロケットを点火し、空へ飛び出す。",
         "Burning the weapons",
         "Outside the cave, Tony uses the flamethrowers in the suit's arms to set the stockpile of Stark weapons ablaze, and the weapons go up in a chain of explosions.\n"
         "He fires the suit's rockets and shoots into the sky."),
        ("砂漠での救出",
         "しかしスーツはすぐに砂漠へ落ち、ばらばらに壊れる。トニーはスーツから抜け出し、何もない砂漠を歩き続ける。\n"
         "そこへ、トニーを探していたローディたちのヘリコプターが現れる。トニーが捕まってから、約3か月がたっていた。",
         "Rescued in the desert",
         "But the suit soon crashes in the desert and falls apart. Tony climbs out and walks across the empty sand.\n"
         "Then a helicopter appears: Rhodey and his team, who have been searching for him. Tony has been a prisoner for about three months."),
    ]),
    ("第4部 帰国と方針転換", "Part 4: Home, and a change of course", [
        ("3か月ぶりのアメリカ",
         "トニーを乗せた飛行機がアメリカに着く。迎えに来たペッパーの目は涙でぬれている。\n"
         "トニーは、病院へ行くより先に、チーズバーガーを食べたいと言う。そして記者会見を開くように頼む。",
         "Back in America",
         "Tony's plane lands in the U.S. Pepper is waiting, her eyes red with tears.\n"
         "Instead of going to the hospital, Tony says he wants a cheeseburger first, and asks for a press conference."),
        ("「もう兵器は作らない」",
         "会社の記者会見で、トニーは記者たちを床に座らせ、自分も床に座って話し始める。父のことを話したあと、自分の会社の武器で目の前の若い兵士たちが死んだことを語る。\n"
         "そしてトニーは、スターク・インダストリーズは兵器を作るのをやめると発表する。会場は大騒ぎになる。",
         "\"No more weapons\"",
         "At the company press conference, Tony sits down on the floor and invites the reporters to do the same. He talks about his father, then about seeing young soldiers die in front of him, killed by his own company's weapons.\n"
         "Then he announces that Stark Industries will stop making weapons. The room erupts."),
        ("オバディアと大型リアクター",
         "オバディアは、会社の株が大きく下がると反対する。オバディアは、トニーを心配する父親代わりのようにふるまう。\n"
         "トニーはオバディアと一緒に、会社の工場にある大型のアーク・リアクターを見に行く。この大きな発電装置は、周りの人を黙らせるための見せ物だと思われていたものだった。トニーは、自分の胸の小さなリアクターを見せる。\n"
         "オバディアは、取締役会がトニーを会社の仕事から外そうとするだろうと伝える。",
         "Obadiah and the big reactor",
         "Obadiah objects that the stock will plunge, while acting like a worried father figure.\n"
         "Tony takes him to see the large arc reactor at the company's plant, which most people had thought was just for show. Tony shows him the small reactor in his chest.\n"
         "Obadiah warns that the board will try to push Tony out of running the company."),
        ("胸の装置の交換",
         "家に戻ったトニーは、地下の工房で、胸のリアクターを新しく作った性能のよいものと取り替えることにする。\n"
         "トニーはペッパーに手伝ってもらう。ペッパーは怖がりながら、トニーの胸の穴に手を入れ、古い装置を取り出して新しいものと交換する。\n"
         "トニーは、古い装置は捨ててくれとペッパーに頼む。",
         "Swapping the reactor",
         "Back home in his basement workshop, Tony decides to replace his chest reactor with an improved one he has built.\n"
         "Pepper helps. Nervously, she reaches into the opening in his chest, pulls out the old device and puts in the new one.\n"
         "Tony asks her to throw the old one away."),
    ]),
    ("第5部 新しいスーツ", "Part 5: A new suit", [
        ("工房での開発",
         "トニーは工房にこもり、ジャーヴィスと一緒に新しいスーツを作り始める。まずは手足から火を噴いて浮かぶ実験だ。\n"
         "うまくいかずに壁や天井にぶつかるたび、そばで待っているロボットアームのダミーが、トニーに消火器の泡をかける。",
         "In the workshop",
         "Tony holes up in his workshop and starts building a new suit with J.A.R.V.I.S., beginning with hover tests using thrusters in his hands and feet.\n"
         "Each time he slams into a wall or the ceiling, the robot arm Dum-E, standing by, sprays him with a fire extinguisher."),
        ("銀色のスーツで初めての飛行",
         "銀色の試作スーツ（マーク2）が完成する。トニーは夜の海辺の町の上を飛び、大喜びする。",
         "First flight in the silver suit",
         "The silver test suit, the Mark II, is finished. Tony flies over the coastal city at night, thrilled."),
        ("凍りつくスーツ",
         "トニーは、どこまで高く飛べるか試して、空高く上がっていく。すると、スーツが凍りついて止まってしまい、トニーは真っ逆さまに落ちる。\n"
         "地面にぶつかる直前、氷がはがれてスーツが動き出し、トニーは助かる。家に戻ったトニーは、着地に失敗して屋根を突き破り、工房の車の上に落ちる。",
         "Icing up",
         "Testing how high he can go, Tony climbs higher and higher until the suit ices over and shuts down, and he plummets.\n"
         "Just before he hits the ground, the ice breaks off and the suit restarts. Back home, he botches the landing, crashes through the roof and lands on a car in his workshop."),
        ("オバディアの知らせ",
         "オバディアがピザを持ってトニーの家に来る。オバディアは、取締役会がトニーを会社から締め出そうとしていると伝える。\n"
         "トニーは、オバディアに新しいスーツのことを話さない。",
         "Obadiah's news",
         "Obadiah drops by Tony's house with pizza and tells him the board is moving to lock him out of the company.\n"
         "Tony keeps the new suit to himself."),
        ("赤と金のスーツ（マーク3）",
         "トニーは凍りつく問題を直し、完成版のスーツを作る。色は、金色に、車のような赤を加える。こうして赤と金のスーツ（マーク3）ができあがる。",
         "The red-and-gold Mark III",
         "Tony solves the icing problem and builds the finished suit, gold with a hot-rod red added. The red-and-gold Mark III is complete."),
        ("ペッパーの贈り物",
         "ペッパーは、トニーが捨ててくれと言った古いアーク・リアクターを捨てていなかった。それはガラスのケースに入れられ、トニーにも心があることの証だという言葉が添えられていた。",
         "Pepper's gift",
         "Pepper never threw away the old arc reactor. She has had it mounted in a glass case, inscribed \"Proof that Tony Stark has a heart.\""),
    ]),
    ("第6部 グルミラ", "Part 6: Gulmira", [
        ("慈善パーティー",
         "消防士の家族のための慈善パーティーに、トニーが突然現れる。入り口では、トニーが有名な人とまちがえて声をかける年配の客もいる（マーベル・コミックのスタン・リーが演じている）。\n"
         "会場では、政府の組織のエージェント、コールソンがトニーに話しかける。コールソンは、組織の長い名前を名乗り、トニーが捕まっていたときのことを聞きたいと言う。",
         "The charity event",
         "Tony makes a surprise appearance at a charity event for firefighters' families. At the entrance he greets an older guest as if he were someone else (a cameo by Marvel's Stan Lee).\n"
         "Inside, government agent Coulson approaches. He introduces his agency by its long name and says he wants to debrief Tony about his captivity."),
        ("ペッパーとのダンス",
         "トニーは、青いドレスのペッパーを見つけ、一緒に踊る。2人は外のテラスへ出て、いい雰囲気になる。トニーは飲み物を取りに行く。",
         "A dance with Pepper",
         "Tony finds Pepper in a blue dress and they dance. They step out onto the terrace and nearly kiss. Tony goes to get them drinks."),
        ("クリスティンの写真",
         "飲み物を取りに行ったトニーに、記者のクリスティンが写真を見せる。インセンの故郷グルミラが、スターク社の武器を持ったテン・リングスに襲われている写真だった。最近、会社の武器がテン・リングスに渡ったのだという。トニーは、何も知らなかった。",
         "Christine's photos",
         "While Tony is getting the drinks, Christine shows him photos: the Ten Rings attacking Yinsen's home village, Gulmira, with Stark weapons recently delivered to them. Tony had no idea."),
        ("オバディアの本音",
         "トニーはオバディアに問いただす。するとオバディアは、トニーを会社から締め出す手続きをしたのは自分だと明かす。トニーを守るためだと言う。",
         "Obadiah comes clean",
         "Tony confronts Obadiah, who admits he's the one who had the board lock Tony out, claiming it was to protect him."),
        ("グルミラの戦い",
         "家に帰ったトニーは、テレビで、家を追われるグルミラの人々のニュースを見る。トニーはマーク3を身につけ、アフガニスタンへ飛ぶ。\n"
         "村では、テン・リングスの兵士たちが村の人々を集め、男たちを家族から引き離していた。トニーは人々に当たらないように、兵士だけをねらって倒す。\n"
         "トニーは兵士たちのリーダーを、村の人々の前に放り出して引き渡す。戦車に撃たれても、トニーは戦車を壊し、村にあった武器を破壊する。",
         "The battle of Gulmira",
         "At home, Tony sees a news report about Gulmira's people being driven from their homes. He puts on the Mark III and flies to Afghanistan.\n"
         "In the village, Ten Rings fighters have rounded up the villagers and are dragging the men away from their families. Tony takes out only the fighters, without hitting the villagers.\n"
         "He hands their leader over to the villagers. When a tank fires on him, he destroys it, and wrecks the weapons in the village."),
        ("戦闘機に追われる",
         "帰り道、正体の分からない飛行物体として、空軍の戦闘機2機に追われる。軍の基地でこれを見ていたローディの電話に、トニーがかけてくる。\n"
         "トニーはローディに、飛んでいるのは自分だと明かす。そのあいだに戦闘機とぶつかり、1機のパイロットが脱出するが、パラシュートが開かない。トニーはパラシュートを開いてパイロットを助け、飛び去る。\n"
         "ローディは、軍には訓練だったと説明することにする。",
         "Chased by fighter jets",
         "On the way home, two Air Force fighter jets chase the unidentified flying object. Rhodey, watching from a base, gets a call from Tony.\n"
         "Tony reveals that he is the one flying. He collides with a jet, and its pilot ejects, but the parachute won't open. Tony frees it, saving the pilot, and flies off.\n"
         "Rhodey decides to tell the military it was a training exercise."),
        ("オバディアとラザ",
         "そのころ、テン・リングスのラザたちは、洞窟の近くに落ちていたマーク1の部品を集め、オバディアと会っていた。オバディアは、裏でテン・リングスに武器を売り、さらにトニーを殺すよう頼んでいた人物だった。\n"
         "ラザは、マーク1の設計図をもとに新しい取引を持ちかける。しかしオバディアは、音で体をしびれさせる装置をラザに当て、動けなくする。オバディアの部下たちが、ラザの仲間を撃ち殺す。\n"
         "オバディアは、マーク1の部品をアメリカへ持ち帰る。",
         "Obadiah and Raza",
         "Meanwhile, Raza's men have gathered the pieces of the Mark I and meet with Obadiah. Obadiah is the one who had secretly been selling weapons to the Ten Rings, and had paid them to kill Tony.\n"
         "Raza offers a new deal based on the Mark I's plans. But Obadiah paralyzes him with a sonic device, and Obadiah's men gun down Raza's fighters.\n"
         "Obadiah takes the Mark I's pieces back to the U.S."),
        ("作れないリアクター",
         "オバディアは、会社のひみつの研究室で、マーク1をもとに巨大なスーツを作らせていた。しかし研究者たちは、スーツを動かすための小さなアーク・リアクターを作れない。\n"
         "オバディアは、トニーは洞窟でがらくたからこれを作ったのだと怒鳴る。",
         "The reactor they can't build",
         "In a secret lab at the company, Obadiah has his engineers building a giant suit based on the Mark I. But they can't make a miniature arc reactor to power it.\n"
         "Obadiah yells that Tony Stark built one in a cave, with a box of scraps."),
    ]),
    ("第7部 黒幕との戦い", "Part 7: Fighting the man behind it", [
        ("ペッパーの潜入",
         "トニーは、会社の武器がどこへ流れているのか調べるため、ペッパーに会社のコンピューターからデータを盗み出してほしいと頼む。ペッパーはトニーの正体と戦いを知り、迷いながらも引き受ける。\n"
         "ペッパーはオバディアの部屋のコンピューターからデータを写す。そこで、オバディアがテン・リングスにトニーを殺すよう頼んでいたことを知る。テン・リングスは、殺す代わりにトニーに武器を作らせようと計画を変えていた。\n"
         "そこへオバディアが部屋に入ってくる。ペッパーは何とかごまかして、部屋を出る。",
         "Pepper goes in",
         "To trace where the company's weapons are going, Tony asks Pepper to copy data from the company's computers. Now knowing what he's been doing, she reluctantly agrees.\n"
         "Copying files from Obadiah's computer, she learns that he paid the Ten Rings to kill Tony, and that they changed their plan, deciding to make Tony build weapons instead.\n"
         "Obadiah walks into the office. Pepper bluffs her way out."),
        ("コールソンのもとへ",
         "会社のロビーで、ペッパーは、何度もトニーに話を聞きに来ていたエージェントのコールソンに会う。ペッパーはコールソンに、オバディアのしていたことを伝える。\n"
         "コールソンの組織の名前は、S.H.I.E.L.D.（シールド）だった。",
         "Turning to Coulson",
         "In the company lobby, Pepper finds Agent Coulson, who has kept trying to meet with Tony. She tells him what Obadiah has been doing.\n"
         "Coulson's agency is called S.H.I.E.L.D."),
        ("奪われたリアクター",
         "そのころ、オバディアはトニーの家に来ていた。オバディアは音で体をしびれさせる装置をトニーに当て、動けなくする。\n"
         "オバディアは、トニーの殺しを頼んだのは自分だったと明かし、トニーの胸からアーク・リアクターを抜き取って持ち去る。リアクターがなければ、胸の破片が心臓に届き、トニーは死んでしまう。",
         "The reactor is stolen",
         "Meanwhile, Obadiah visits Tony's house and paralyzes him with the sonic device.\n"
         "He reveals that he was the one who ordered the hit on Tony, then pulls the arc reactor out of Tony's chest and takes it. Without it, the fragments will reach Tony's heart and kill him."),
        ("ダミーが手渡したもの",
         "トニーは体をひきずって工房へ向かう。ペッパーが飾っていた古いリアクターを取りに行くためだ。しかし、手が届かない。\n"
         "そのとき、ロボットアームのダミーが、古いリアクターを手渡してくれる。トニーはそれを胸にはめ、命をつなぐ。",
         "What Dum-E handed him",
         "Tony drags himself toward the workshop to reach the old reactor Pepper had framed, but he can't get to it.\n"
         "Then Dum-E, the robot arm, hands it to him. Tony puts it in his chest and survives."),
        ("ローディと銀色のスーツ",
         "ローディがトニーの家に駆けつける。トニーはマーク3を着て、ペッパーのもとへ飛んでいく。\n"
         "工房に残ったローディは、銀色のマーク2を見つめ、次こそはとつぶやくが、その場を離れる。",
         "Rhodey and the silver suit",
         "Rhodey arrives at Tony's house. Tony puts on the Mark III and flies to Pepper.\n"
         "Left in the workshop, Rhodey eyes the silver Mark II and says, \"Next time, baby,\" before leaving it."),
        ("アイアンモンガー",
         "ペッパーとコールソンたちS.H.I.E.L.D.のエージェントは、オバディアをつかまえるため会社の工場へ行く。ひみつの研究室では、マーク1の部品を見つけるが、巨大なスーツは消えていた。\n"
         "トニーのリアクターで動く巨大なスーツ「アイアンモンガー」を着たオバディアが現れ、エージェントたちをなぎ倒し、ペッパーに迫る。",
         "Iron Monger",
         "Pepper, Coulson and S.H.I.E.L.D. agents go to the company plant to arrest Obadiah. In the secret lab they find the Mark I's pieces, but the giant suit is gone.\n"
         "Obadiah appears in the suit, Iron Monger, powered by Tony's reactor. He overpowers the agents and goes after Pepper."),
        ("古いリアクターでの戦い",
         "トニーが駆けつけ、オバディアと戦う。しかし古いリアクターでは、スーツは十分な力を出せない。\n"
         "2人の戦いは近くの道路にまで広がる。オバディアは、人の乗った車を持ち上げてトニーに投げつけようとし、トニーはその人々を守る。",
         "Fighting on old power",
         "Tony arrives and fights Obadiah, but the old reactor can't run his suit at full power.\n"
         "The fight spills onto a nearby road. Obadiah lifts a car with people inside, and Tony protects them."),
        ("空高くへ",
         "トニーは空高くへ飛び上がり、オバディアを追わせる。オバディアのスーツは高い空で凍りつき、動かなくなる。トニーが前に悩まされた弱点を、オバディアは直していなかったのだ。\n"
         "オバディアは落ちていくが、まだ倒れない。",
         "Up high",
         "Tony flies high into the sky and lures Obadiah after him. Obadiah's suit ices up and stops: he never fixed the problem Tony ran into before.\n"
         "Obadiah falls, but he isn't finished."),
        ("大型リアクターの暴走",
         "戦いは会社の建物の屋上へ移る。屋上の下には、大型のアーク・リアクターがある。トニーのスーツは力が残り少ない。\n"
         "トニーはペッパーに、大型リアクターに過負荷をかけて暴走させるよう頼む。トニーが屋上から離れられないまま、ペッパーはボタンを押す。\n"
         "大きな電気の光がオバディアを包む。オバディアは屋上から下のリアクターへ落ち、爆発に巻き込まれて死ぬ。トニーは生き残る。",
         "Overloading the big reactor",
         "The fight moves to the roof of the company building, above the large arc reactor. Tony's suit is nearly out of power.\n"
         "Tony tells Pepper to overload the big reactor. Though he can't get off the roof, she presses the button.\n"
         "A huge electrical surge engulfs Obadiah. He falls through the roof into the reactor and is killed in the explosion. Tony survives."),
    ]),
    ("第8部 私がアイアンマンだ", "Part 8: \"I am Iron Man\"", [
        ("新聞の見出し",
         "次の日の新聞には、謎の鉄のヒーローを「アイアンマン」と呼ぶ見出しがのる。",
         "The headline",
         "The next day's newspaper gives the mysterious armored hero a name: Iron Man."),
        ("用意された説明",
         "記者会見の前、コールソンはトニーに、事件の夜トニーはほかの場所にいたという説明（アリバイ）を用意して渡す。会見では、ローディが軍の発表を読み上げる。",
         "A prepared story",
         "Before the press conference, Coulson hands Tony an alibi saying he was somewhere else on the night of the fight. At the conference, Rhodey reads the military's statement."),
        ("「私がアイアンマンだ」",
         "トニーは用意されたカードを読み始めるが、記者のクリスティンの質問のあと、途中で読むのをやめる。\n"
         "そしてトニーは、自分から「私がアイアンマンだ」と明かす。会場は騒然となり、映画はここで終わる。",
         "\"I am Iron Man\"",
         "Tony starts reading the prepared cards, but after a question from Christine, he stops.\n"
         "Then he says it himself: \"The truth is... I am Iron Man.\" The room erupts, and the film ends."),
        ("エンドクレジットの後",
         "家に戻ったトニーの前に、眼帯をした男が現れる。S.H.I.E.L.D.の長官ニック・フューリーだ。\n"
         "フューリーは、世界にいるヒーローはトニーだけではないとほのめかし、「アベンジャーズ計画」の話をしに来たと告げる。",
         "After the credits",
         "Back home, Tony finds a man with an eye patch waiting: Nick Fury, director of S.H.I.E.L.D.\n"
         "Fury hints that Tony isn't the only hero in the world, and says he's there to talk about the Avengers Initiative."),
    ]),
    ("まとめ（最後までのネタバレ）", "Summary (spoilers through the end)", [
        ("オバディアのたくらみ",
         "・オバディアは、トニーに隠れてスターク社の武器をテン・リングスに売っていた。\n"
         "・会社を自分のものにするため、テン・リングスにトニーを殺すよう頼んだ（第1部の襲撃）。テン・リングスは、殺さずにトニーに武器を作らせようと計画を変えた（第2部）。\n"
         "・トニーが兵器づくりをやめると言うと、取締役会を使ってトニーを会社から締め出した（第4部〜第6部）。\n"
         "・マーク1の部品を手に入れてアイアンモンガーを作り、トニーの胸のリアクターを奪った（第6部・第7部）。",
         "Obadiah's scheme",
         "- Behind Tony's back, Obadiah sold Stark weapons to the Ten Rings.\n"
         "- To take over the company, he paid the Ten Rings to kill Tony (the Part 1 ambush). They changed plans and tried to make Tony build weapons instead (Part 2).\n"
         "- When Tony stopped making weapons, Obadiah used the board to lock him out (Parts 4-6).\n"
         "- He got the Mark I's pieces, built Iron Monger and stole the reactor from Tony's chest (Parts 6-7)."),
        ("スーツの移り変わり",
         "・マーク1（第3部）：洞窟で作った灰色のスーツ。脱出のあと砂漠で壊れ、その部品がオバディアの手に渡る。\n"
         "・マーク2（第5部）：家で作った銀色の試作品。高い空で凍りつく弱点があった。最後にローディが見つめる。\n"
         "・マーク3（第5部〜第7部）：凍りつく問題を直した、赤と金の完成版。\n"
         "・アイアンモンガー（第7部）：オバディアがマーク1をもとに作らせた巨大なスーツ。",
         "The suits",
         "- Mark I (Part 3): the gray suit built in the cave. It breaks apart in the desert after the escape, and its pieces end up with Obadiah.\n"
         "- Mark II (Part 5): the silver prototype built at home, which ices up at high altitude. Rhodey eyes it at the end.\n"
         "- Mark III (Parts 5-7): the finished red-and-gold suit, with the icing problem fixed.\n"
         "- Iron Monger (Part 7): the giant suit Obadiah has built from the Mark I."),
        ("死んだ人たち（話の順に）",
         "・トニーと一緒にいた兵士たち（第1部）：テン・リングスの待ち伏せで撃たれる。\n"
         "・インセン（第3部）：トニーのスーツが動き出すまでの時間をかせぐため、銃を持って飛び出し、テン・リングスの兵士たちに撃たれる。トニーに、命を無駄にするなと言い残す。\n"
         "・テン・リングスの兵士たち（第3部・第6部）：洞窟からの脱出とグルミラの戦いで、マーク1・マーク3のトニーに倒される。\n"
         "・ラザの仲間たち（第6部）：マーク1の部品を渡したあと、口封じのため、オバディアの部下に撃ち殺される。\n"
         "・オバディア（第7部）：トニーの頼みでペッパーが大型リアクターを暴走させ、その光に包まれて屋上からリアクターへ落ち、爆発で死ぬ。",
         "Who died (in order)",
         "- The soldiers with Tony (Part 1): shot in the Ten Rings ambush.\n"
         "- Yinsen (Part 3): runs out with a gun to buy time for Tony's suit to start, and is shot by Ten Rings fighters. His last words to Tony: don't waste your life.\n"
         "- Ten Rings fighters (Parts 3 and 6): taken down by Tony in the Mark I during the escape, and in the Mark III at Gulmira.\n"
         "- Raza's fighters (Part 6): gunned down by Obadiah's men after handing over the Mark I's pieces.\n"
         "- Obadiah (Part 7): when Pepper overloads the big reactor at Tony's request, the surge engulfs him; he falls through the roof into the reactor and is killed in the explosion."),
    ]),
]
