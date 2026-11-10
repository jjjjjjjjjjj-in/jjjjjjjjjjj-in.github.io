# 『マーベルズ』（2023年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版ウィキペディアの作品の記事と、キャロル・カマラ・フューリー・ダー・ベンなど登場人物の記事
# （それぞれ映画の順に書かれている）を照らし合わせ、日本語版ウィキペディアと検索で見つかった解説記事で確かめた。
# 資料が1つしかない所や食い違う所（MB-418が星か月か、アラドナから跳んだのがわざとかどうかの細かい所、
# キャロルとマリアの最後の場面の中身、フラーケンの子どもの数、ターナックスで亡くなったスクラル人の数、
# ラストでキャロルがダー・ベンに何を申し出たか、ケイトとの場面のせりふ、物語の年など）は書いていない。
# 日本語版のせりふは、日本語の吹替・字幕の言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 人物名は相関図（relations.py）と日本語版ウィキペディアの配役表にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 腕輪の片割れ", "Part 1: The other bangle", [
        ("MB-418の発掘",
         "宇宙のさびれた場所、MB-418。クリーのリーダー、ダー・ベンは、部下たちと地面を掘り、大きな岩を、かつてロナンが使っていたハンマー（ユニバーサル・ウェポン）で打ちくだく。\n"
         "中から出てきたのは、腕輪の形をした伝説の道具、クォンタム・バンドの片方だった。2つで1組のこの腕輪は、昔、宇宙の遠い場所どうしをつなぐ通り道「ジャンプ・ポイント」を作るのに使われたと伝えられている。",
         "The dig on MB-418",
         "On the desolate MB-418, Kree leader Dar-Benn and her soldiers dig, and she smashes a huge rock with the hammer Ronan once wielded, the Universal Weapon.\n"
         "Inside is one of the legendary Quantum Bands. The pair of bangles is said to have been used long ago to build the jump points, the gateways linking distant places in space."),
        ("死にかけた星ハラ",
         "クリーの故郷の星ハラは、長い内戦のあいだに空気も水も失い、太陽もほとんど光を失っていた。\n"
         "ダー・ベンは腕輪の力で、むりやり新しいジャンプ・ポイントを開く。このせいで、宇宙じゅうのジャンプ・ポイントのつながりに乱れが出る。",
         "Hala, a dying world",
         "The Kree homeworld Hala has lost its air and water over a long civil war, and its sun has nearly gone dark.\n"
         "With the band, Dar-Benn forces open a new jump point. The damage ripples through the whole network of jump points."),
        ("カマラの部屋",
         "地球のジャージーシティ。高校生のカマラ・カーンは、自分の部屋で、あこがれのキャプテン・マーベルと自分が一緒に戦う絵をかいて空想にふけっている。カマラの腕にも、もう片方のクォンタム・バンドがある。",
         "Kamala's room",
         "In Jersey City, teenager Kamala Khan daydreams in her bedroom, drawing herself fighting alongside her idol Captain Marvel. On her arm is the other Quantum Band."),
    ]),
    ("第2部 入れかわる3人", "Part 2: Swapping places", [
        ("フューリーの連絡",
         "宇宙船で猫のような生き物グースと静かに暮らしていたキャロル・ダンヴァースに、ニック・フューリーから連絡が入る。ジャンプ・ポイントにおかしな乱れが出ているので、調べてほしいという。\n"
         "キャロルは、ダー・ベンが開いたジャンプ・ポイントのある、誰も住んでいない星へ向かう。",
         "Fury's call",
         "Carol Danvers, living quietly on her ship with the cat-like Goose, gets a call from Nick Fury: something is wrong with the jump points. Would she look into it?\n"
         "Carol heads to an uninhabited planet where Dar-Benn opened the new jump point."),
        ("宇宙ステーションのモニカ",
         "地球の近くには、フューリーが責任者を務める宇宙ステーションS.A.B.E.R.がある。その近くのジャンプ・ポイントも乱れていて、宇宙飛行士のモニカ・ランボーが調べに出る。\n"
         "キャロルとモニカは、それぞれ自分の前のジャンプ・ポイントに同時にふれる。",
         "Monica at the station",
         "Near Earth is S.A.B.E.R., the space station Fury runs. The jump point beside it is acting up too, and astronaut Monica Rambeau goes out to investigate.\n"
         "Carol and Monica each touch their jump point at the same moment."),
        ("最初の入れかわり",
         "その瞬間、3人の居場所が入れかわる。モニカはキャロルがいた星へ飛ばされ、そこにいたクリーの兵士たちにおそわれる。\n"
         "カマラはモニカの宇宙服を着た姿で、ステーションの外に現れる。あわてたカマラは、窓の向こうのフューリーを見つけて自己紹介をする。",
         "The first swap",
         "In that instant, three people trade places. Monica lands on Carol's planet and is attacked by Kree soldiers.\n"
         "Kamala appears outside the station in Monica's spacesuit. Panicking, she spots Fury through the window and introduces herself."),
        ("ファンの部屋のキャロル",
         "キャロルはカマラの部屋に現れる。壁じゅうに自分のポスターやグッズがあるのを見て、とまどう。\n"
         "1階に下りると、居間にカマラの家族がいる。キャロルはそのまま外へ出て飛び立つが、すぐにまたあの星へ引きもどされる。そこでクリーの兵士たちと戦い、ダー・ベンの行き先を聞き出す。",
         "Carol in a fan's bedroom",
         "Carol finds herself in Kamala's bedroom, surrounded by posters and merchandise of herself.\n"
         "Downstairs, Kamala's family is in the living room. Carol walks out and flies off, only to be pulled back to the planet, where she fights Kree soldiers and learns where Dar-Benn is headed."),
        ("止まらない入れかわり",
         "それからも、3人の居場所は何度も入れかわる。カマラは、クリーの宇宙船、フューリーの小型の乗り物、またクリーの宇宙船と、次々に飛ばされる。クリーの宇宙船ではグースに出会い、うっかり家まで連れて帰ってしまう。\n"
         "キャロルはグースと、スクラル人が暮らす星ターナックスへ行き、スクラルとクリーの和平の話し合いの場にもぐりこむが、そこでも入れかわりが起きる。",
         "The swaps keep coming",
         "The three keep switching places. Kamala is thrown onto a Kree ship, into Fury's pod, then back onto the Kree ship, where she meets Goose and accidentally brings her home.\n"
         "Carol takes Goose to the Skrull planet Tarnax and slips into peace talks between the Skrulls and the Kree, but the swapping follows her there too."),
    ]),
    ("第3部 カーン家の大さわぎ", "Part 3: Chaos at the Khans'", [
        ("こわれていく家",
         "入れかわるたびに、クリーの兵士まで一緒に飛ばされてくる。カマラの家では、カマラやキャロルが兵士たちと戦い、家族の目の前で家がめちゃくちゃにこわれていく。\n"
         "フューリーとモニカは、宇宙エレベーターで地球へ下りる。その途中にも、キャロルやカマラ、クリーの兵士が入れかわりで現れる。",
         "The house comes apart",
         "Kree soldiers get swapped along with them. At the Khan home, Kamala and Carol fight the soldiers, and the house is wrecked in front of the family.\n"
         "Fury and Monica ride a space elevator down to Earth, with Carol, Kamala and Kree soldiers popping in and out along the way."),
        ("フューリーとモニカの訪問",
         "フューリーとモニカは、ジャージーシティのカーン家に着く。フューリーは、ここにいたグースと再会する。カマラは、S.A.B.E.R.が自分のことを調べた記録を持っていると知る。\n"
         "その場にいたキャロルは、モニカにどうやって力を得たのかたずねる。モニカは、魔女が町を包んだ不思議な壁を通りぬけたときだと話す。",
         "Fury and Monica arrive",
         "Fury and Monica reach the Khans' house in Jersey City, and Fury is reunited with Goose. Kamala discovers S.A.B.E.R. has a file on her.\n"
         "Carol, there at that moment, asks Monica how she got her powers. Monica explains she passed through a witch's Hex."),
        ("3人がつながったわけ",
         "モニカは考えを話す。3人の力はどれも光に関わるもので、ジャンプ・ポイントの乱れのせいで、その力がからみ合ってしまった。だから、3人のうち誰かが同時に力を使うと、居場所が入れかわるのだ。",
         "Why they're linked",
         "Monica lays out her theory: all three have light-based powers, and the jump point disturbance has entangled them. Whenever they use their powers at the same time, they swap places."),
        ("落ちてくるカマラ",
         "カマラは、自分の力をフューリーたちに見せようとして、キャロルと入れかわり、クリーの宇宙船にもどされてしまう。\n"
         "次の入れかわりで、カマラは空から落ちてくる。フューリーにうながされたモニカが受け止めに行く。カマラは光の力で自分とモニカを固い光で包み、2人はそのままキャロルと入れかわって、ターナックスにあるクリーの宇宙船の上に出る。そこへダー・ベンが近づいてくる。",
         "Kamala falls",
         "Trying to show Fury her powers, Kamala swaps with Carol and ends up back on the Kree ship.\n"
         "With the next swap, she comes plummeting out of the sky. Urged on by Fury, Monica goes to catch her. Kamala wraps them both in hard light, and they swap with Carol, landing on a Kree ship on Tarnax as Dar-Benn closes in."),
        ("家族は宇宙ステーションへ",
         "家がこわれてしまったカーン家の両親ムニーバとユスフ、兄のアーミルは、フューリーと一緒に宇宙ステーションへ行く。フューリーはグースも連れていく。",
         "The family goes to space",
         "With their house in ruins, Kamala's parents Muneeba and Yusuf and her brother Aamir go to the space station with Fury, who takes Goose along too."),
    ]),
    ("第4部 ターナックスの悲劇", "Part 4: Tragedy on Tarnax", [
        ("スクラルの星",
         "ターナックスは、ふるさとを失ったスクラル人のために、キャロルが作るのを手伝った住まいの星だった。ここでは、ドロージ皇帝が率いるスクラルと、クリーとの和平の話し合いが開かれていた。\n"
         "キャロルが駆けつけ、カマラ、モニカと合流して、3人はキャロルの宇宙船に乗る。",
         "The Skrull planet",
         "Tarnax is a refuge Carol helped found for the homeless Skrulls. Peace talks are under way there between the Kree and the Skrulls, led by Emperor Dro'ge.\n"
         "Carol arrives, joins up with Kamala and Monica, and the three board Carol's ship."),
        ("うばわれる空気",
         "話し合いはまとまらない。ダー・ベンは新しいジャンプ・ポイントを開き、ターナックスの空気をハラへ吸い取っていく。空気をなくしたハラに、息ができる空気をもどすためだった。",
         "The air is stolen",
         "The talks collapse. Dar-Benn tears open another jump point and drains Tarnax's atmosphere into Hala, to give her homeworld breathable air again."),
        ("あわただしい避難",
         "キャロルは、スクラルの人々と皇帝に、自分の宇宙船へ乗るよう呼びかける。3人は急いで人々を運び出す。\n"
         "そのあと、キャロルはヴァルキリーに連絡する。駆けつけたヴァルキリーが、助かったスクラルの人々を地球へ連れていく。",
         "A hasty evacuation",
         "Carol tells the Skrulls and their Emperor to get aboard her ship, and the three rush to get people out.\n"
         "Afterward Carol calls Valkyrie, who comes and takes the surviving Skrulls to Earth."),
        ("チーム「マーベルズ」",
         "宇宙船の中で、キャロルはモニカと2人だけで話したあと、カマラにあらためて自己紹介をする。カマラの腕輪を見たキャロルは、それがクォンタム・バンドだと気づく。\n"
         "キャロルは説明する。ダー・ベンがジャンプ・ポイントを乱したとき、3人はそのエネルギーにふれて、つながってしまった。ダー・ベンがジャンプ・ポイントを何度も引き裂くと、通り道全体がこわれて、宇宙全体があぶなくなる。\n"
         "カマラは、3人のチームを「マーベルズ」と名づける。",
         "The Marvels",
         "On the ship, Carol talks with Monica alone, then properly introduces herself to Kamala. Seeing Kamala's bangle, she recognizes it as a Quantum Band.\n"
         "Carol explains: when Dar-Benn disrupted the jump points, the three were all touched by that energy and became entangled. If Dar-Benn keeps ripping jump points open, the whole network will break down and the universe itself will be in danger.\n"
         "Kamala names their team the Marvels."),
    ]),
    ("第5部 力を合わせる練習", "Part 5: Learning to work together", [
        ("入れかわりの練習",
         "3人は、入れかわりをうまく使えるように、宇宙船の中で練習を重ねる。縄跳びやボールの受け渡しをしながら、力を使うタイミングを合わせていく。",
         "Swap practice",
         "The three practice on the ship so they can control the swapping, timing their powers with games like double-dutch jump rope and tossing a ball."),
        ("ねらわれる星",
         "3人は、ダー・ベンがねらっているのが、キャロルにとって大切な星ばかりだと気づく。ダー・ベンは、ハラがほろびかけているのはキャロルのせいだと恨んでいた。\n"
         "カマラがダー・ベンの宇宙船で見た星の地図をもとに、次のねらいが水の星アラドナだと分かる。",
         "Targeted worlds",
         "They realize Dar-Benn is going after planets that matter to Carol. She blames Carol for Hala's ruin.\n"
         "Using a star map Kamala glimpsed on Dar-Benn's ship, they work out that her next target is the water world Aladna."),
    ]),
    ("第6部 歌の星アラドナ", "Part 6: Aladna, the planet of song", [
        ("王女キャロル",
         "アラドナの人々は、歌で話をする。キャロルは、昔ここの王子ヤンと、国どうしの約束のために結婚していた。\n"
         "キャロルは王女として人々に迎えられ、宮殿でヤン王子と再会する。3人は新しいスーツを用意してもらう。キャロルはヤンと歌いながら踊り、ダー・ベンがおそってくることを知らせる。",
         "Princess Carol",
         "The people of Aladna speak in song. Long ago, Carol married their Prince Yan as part of a diplomatic agreement.\n"
         "Carol is welcomed as a princess and reunited with Yan in his palace, where the three are given new suits. Carol dances with Yan, singing, and warns him that Dar-Benn is coming."),
        ("海をうばう",
         "ダー・ベンが兵士たちと現れ、ジャンプ・ポイントを引き裂いて、アラドナの水をハラへ吸い取りはじめる。\n"
         "マーベルズとヤン王子、アラドナの兵士たちは、ダー・ベンの軍と戦う。",
         "Stealing the sea",
         "Dar-Benn arrives with her soldiers and rips open a jump point, draining Aladna's water toward Hala.\n"
         "The Marvels, Prince Yan and Aladna's soldiers fight Dar-Benn's forces."),
        ("まちがって跳ぶ",
         "宇宙船にもどったとき、カマラがうっかり操作をしてしまい、宇宙船はジャンプ・ポイントを通って、まったく別の星へ跳んでしまう。",
         "An accidental jump",
         "Back on the ship, Kamala accidentally hits the controls, and the ship jumps through a jump point to a completely different planet."),
    ]),
    ("第7部 キャロルの告白", "Part 7: Carol's confession", [
        ("戻らなかったわけ",
         "モニカは子どものころ、母のマリアの親友キャロルを家族のように慕っていた。しかしキャロルは、その後モニカのもとへ戻ってこなかった。\n"
         "知らない星で、キャロルはモニカに、なぜ戻らなかったのかを話す。",
         "Why she stayed away",
         "As a girl, Monica adored her mother Maria's best friend Carol like family, but Carol never came back to her.\n"
         "On the strange planet, Carol tells Monica why she never returned."),
        ("ハラで起きたこと",
         "キャロルは打ち明ける。昔、キャロルはハラへ行き、ダー・ベンたちクリーの戦士をなぎ倒して、クリーを支配していた人工知能スプリーム・インテリジェンスを破壊した。\n"
         "そのせいでハラでは内戦が起き、星は空気も水も太陽の光も失っていった。キャロルは、クリーの人々から星を滅ぼした者と呼ばれ、恨まれている。そのことを、ずっと気に病んでいたのだった。",
         "What happened on Hala",
         "Carol confesses: long ago she went to Hala, cut through Kree warriors including Dar-Benn, and destroyed the Supreme Intelligence, the AI that ruled the Kree.\n"
         "That set off a civil war, and the planet lost its air, water and sunlight. The Kree call her \"the Annihilator,\" and the guilt has stayed with her ever since."),
    ]),
    ("第8部 宇宙ステーションの避難", "Part 8: Evacuating the station", [
        ("ゆれるステーション",
         "ダー・ベンが開いたジャンプ・ポイントの乱れで、宇宙ステーションS.A.B.E.R.があぶなくなる。マーベルズも助けに向かう。\n"
         "そのころステーションでは、グースがたくさんの子どもを産んでいた。グースと同じフラーケンの子どもたちだった。",
         "The station shakes",
         "The jump point disturbances Dar-Benn has caused put the S.A.B.E.R. station in danger, and the Marvels head there to help.\n"
         "Meanwhile, Goose has given birth to a litter of Flerken kittens."),
        ("フラーケンの子どもたち",
         "フラーケンは、口から大きな触手を出して、人を一時的に飲みこむことができる。フューリーはこれを使い、子どもたちにステーションの職員を飲みこませて運び出す。避難の場面には、ミュージカル『キャッツ』の歌「メモリー」が流れる。",
         "The Flerken kittens",
         "Flerkens can swallow people whole for a while with their tentacled mouths. Fury has the kittens gulp down the station's crew to carry them out, as \"Memory\" from Cats plays."),
        ("脱出用の乗り物",
         "フューリー、グース、カマラの家族は、脱出用の乗り物でステーションを出る。しかし、ダー・ベンの不安定なジャンプ・ポイントのあおりを受けて、乗り物はニューヨークに不時着する。",
         "The escape pod",
         "Fury, Goose and Kamala's family escape the station in a pod, but Dar-Benn's unstable jump point blasts it, and it crash-lands in New York City."),
    ]),
    ("第9部 太陽の前の戦い", "Part 9: Battle by the Sun", [
        ("地球の太陽をねらう",
         "ダー・ベンの最後のねらいは、地球の太陽の力をうばって、ハラの太陽パマを再び燃え上がらせることだった。\n"
         "マーベルズは、太陽の近くにいるダー・ベンの宇宙船に乗りこんで戦う。",
         "Targeting Earth's sun",
         "Dar-Benn's final plan is to siphon the energy of Earth's sun to reignite Hala's sun, Pama.\n"
         "The Marvels board Dar-Benn's ship near the Sun and fight her."),
        ("ダー・ベンの最期",
         "ダー・ベンは、カマラの腕輪をうばい取る。2つのクォンタム・バンドを両腕につけ、空間に大きな穴を開ける。\n"
         "しかし、2つの腕輪の力はあまりに強すぎた。ダー・ベンは自分が呼び出した力に耐えられず、体ごとくだけて消える。あとには、別の宇宙へつながる大きな裂け目が残る。3人の力のつながりも消えた。",
         "Dar-Benn's end",
         "Dar-Benn seizes Kamala's band. Wearing both Quantum Bands, she tears a huge hole in space.\n"
         "But the combined power is too much. Overwhelmed by the energy she unleashed, Dar-Benn disintegrates. She leaves behind a rupture opening onto another universe, and the three heroes are no longer entangled."),
        ("モニカの決断",
         "このままでは、裂け目が広がって宇宙があぶない。カマラは2つの腕輪を取りもどして両腕につける。\n"
         "モニカが、自分が行くと名乗り出る。カマラとキャロルは力を合わせてモニカに力を注ぎこみ、モニカは向こう側から裂け目を閉じる。裂け目は閉じたが、モニカは別の宇宙に取り残されてしまう。",
         "Monica's choice",
         "Left open, the rupture will threaten the universe. Kamala reclaims both bands and puts them on.\n"
         "Monica volunteers to go. Kamala and Carol pour their power into her, and she closes the rupture from the other side. It works, but Monica is stranded in another universe."),
        ("太陽をともす",
         "キャロルはカマラを地球へ帰し、ひとりハラへ向かう。そして自分の力で、消えかけていたハラの太陽を再び明るく燃え上がらせる。",
         "Relighting the sun",
         "Carol sends Kamala back to Earth and goes to Hala alone, using her own power to reignite its dying sun."),
    ]),
    ("第10部 その後とエンドクレジット", "Part 10: Afterward and the credits", [
        ("ニューヨークでの再会",
         "カマラはキャロルの宇宙船でニューヨークへ戻り、フューリーと家族に会う。カマラは、モニカが別の宇宙に取り残されたことを伝える。\n"
         "フューリーは、モニカを失った悲しみをかかえて、職員たちと宇宙ステーションへ戻る。",
         "Reunion in New York",
         "Kamala flies Carol's ship back to New York and finds Fury and her family. She tells them Monica is stranded in another universe.\n"
         "Fury returns to the station with his crew, grieving the loss of Monica."),
        ("ルイジアナの家",
         "ルイジアナにある、モニカの家。カマラの家族は、キャロルとグースがこの家に引っこすのを手伝う。",
         "The house in Louisiana",
         "At Monica's home in Louisiana, the Khans help Carol and Goose move in."),
        ("新しいチームへ",
         "マーベルズでの短い冒険をきっかけに、カマラは若いヒーローたちを集めようと考える。S.A.B.E.R.の情報をもとに、まずニューヨークに住む弓の名手ケイト・ビショップを訪ねる。\n"
         "ケイトの部屋を訪れたカマラは、チームを作っていると話してケイトをさそい、アントマンの娘キャシー・ラングのことも口にする。",
         "A new team",
         "Inspired by her short time with the Marvels, Kamala decides to gather young heroes. Using S.A.B.E.R.'s intelligence, she starts with archer Kate Bishop in New York.\n"
         "At Kate's apartment, Kamala says she's putting a team together, invites Kate to join, and mentions Ant-Man's daughter, Cassie Lang."),
        ("エンドクレジットの途中",
         "モニカは、別の宇宙の医務室のような部屋で目を覚ます。そばにいたのは、亡くなった母マリアにそっくりの女性だった。モニカは思わず母を呼ぶが、女性はモニカを知らない様子だ。この世界のマリアは、力を持つバイナリーだった。\n"
         "そこへ、青い毛のビースト（ハンク・マッコイ）が現れる。ビーストは、モニカが時空をこえて来たことを、チャールズに知らせなければと言う。",
         "Mid-credits",
         "Monica wakes in a medical room in another universe. Beside her is a woman who looks exactly like her late mother, Maria. Monica calls her Mom, but the woman doesn't seem to know her. This world's Maria is the powered Binary.\n"
         "Then the blue-furred Beast, Hank McCoy, appears and says they need to tell Charles that Monica has come across space and time."),
    ]),
    ("まとめ", "Summary", [
        ("キャロルがしたこと",
         "昔、ハラでスプリーム・インテリジェンスを破壊し、そのせいでクリーの星が内戦でほろびかけたことを気に病んでいた（第7部）。ダー・ベンを止めるためにモニカ、カマラとチームを組み（第4部）、最後は自分の力でハラの太陽をよみがえらせた（第9部）。",
         "What Carol did",
         "She destroyed the Supreme Intelligence on Hala long ago, which plunged the Kree homeworld into civil war and ruin, and she carried that guilt (Part 7). She teamed up with Monica and Kamala to stop Dar-Benn (Part 4), and in the end reignited Hala's sun with her own power (Part 9)."),
        ("ダー・ベンがしたこと",
         "クォンタム・バンドの片方を見つけ（第1部）、ジャンプ・ポイントを引き裂いて、ターナックスの空気、アラドナの水をハラへうばった（第4部・第6部）。地球の太陽までねらい、2つの腕輪を使ったことで命を落とした（第9部）。",
         "What Dar-Benn did",
         "She found one Quantum Band (Part 1) and tore open jump points to steal Tarnax's air and Aladna's water for Hala (Parts 4 and 6). She went after Earth's sun too, and using both bands killed her (Part 9)."),
        ("モニカとカマラのその後",
         "モニカは裂け目を閉じるために名乗り出て、別の宇宙に取り残され、そこでマリアにそっくりのバイナリーとビーストに出会った（第9部・第10部）。カマラは家族のもとに戻り、ケイト・ビショップをさそって若いヒーローのチームを作りはじめた（第10部）。",
         "Where Monica and Kamala end up",
         "Monica volunteered to close the rupture and was stranded in another universe, where she met Binary, who looks just like Maria, and Beast (Parts 9 and 10). Kamala went home to her family and began forming a team of young heroes, starting with Kate Bishop (Part 10)."),
        ("死んだ人たち（話の順に）",
         "・ダー・ベン（第9部）：地球の太陽の力をうばおうとした戦いの中で、カマラの腕輪をうばい、2つのクォンタム・バンドを使って空間に穴を開けたが、その強すぎる力に耐えられず、体がくだけて消えた。\n"
         "・モニカは死んでいない。裂け目を閉じたあと、別の宇宙に取り残された。",
         "Who died (in order)",
         "- Dar-Benn (Part 9): trying to steal the power of Earth's sun, she took Kamala's band and used both Quantum Bands to tear open space, but the overwhelming power disintegrated her.\n"
         "- Monica does not die. After closing the rupture, she is stranded in another universe."),
    ]),
]
