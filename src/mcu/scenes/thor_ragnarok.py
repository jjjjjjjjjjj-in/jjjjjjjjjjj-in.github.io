# 『マイティ・ソー バトルロイヤル』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじと登場人物の記事、検索で見つかった日本語の解説記事（ciatr）で事実を確かめた。
# 資料どうしで食い違う所や、確かめられない細かい順番・せりふは書いていない（スカージやトパーズの最期の細かい様子など）。
# 日本語版のせりふは、日本語のサイトで確かめられた「リベンジャーズ」「サーファーくん」「今回は引き分けかな」だけをカギかっこで引用し、ほかは内容だけ書いた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 火の国からアスガルドへ", "Part 1: From the land of fire to Asgard", [
        ("くさりにつながれたソー",
         "ウルトロンとのソコヴィアの戦いから2年。ソーは宇宙を旅していたが、火の国ムスペルヘイムで、炎の巨人スルトにつかまっている。\n"
         "くさりで天井からつるされたソーに、スルトは話す。父オーディンはもうアスガルドにいない。そして、自分の冠をオーディンの宝物庫にある「永遠の炎」に入れれば元の大きさに戻り、アスガルドを焼きつくす。それが言い伝えの「ラグナロク（終末の日）」だ、と。",
         "Thor in chains",
         "Two years after the battle against Ultron in Sokovia. Thor has been traveling the universe, and is now a prisoner of the fire demon Surtur in Muspelheim.\n"
         "As Thor hangs in chains, Surtur tells him that Odin is no longer on Asgard. Once Surtur's crown is placed in the Eternal Flame in Odin's vault, he will return to full size and burn Asgard to the ground. That is the prophesied Ragnarok."),
        ("スルトの冠を奪う",
         "ソーはくさりを外し、呼び寄せたハンマーのムジョルニアでスルトの手下たちを倒す。そしてスルトの頭から冠を奪い取る。これでラグナロクは防げたと考える。\n"
         "ソーは虹の橋ビフレストの番人ヘイムダルを呼ぶが、返事がない。炎の竜に追われながら、ソーは何度も呼びかける。",
         "Taking Surtur's crown",
         "Thor breaks free, summons his hammer Mjolnir, and smashes through Surtur's forces, tearing the crown from Surtur's head. He believes he has stopped Ragnarok.\n"
         "He calls for Heimdall, keeper of the Bifrost, but gets no answer, and keeps calling as a fire dragon chases him."),
        ("新しい番人スカージ",
         "そのころビフレストの見張り台では、新しい番人スカージが、地球で手に入れた品物を女性たちに見せびらかしていた。ソーの声に気づいたスカージがやっと橋を開き、ソーはアスガルドへ戻る。追ってきた竜は、橋が閉じたところで断ち切られる。\n"
         "ソーがヘイムダルのことを聞くと、ヘイムダルはオーディンの命令で裏切り者として職を追われ、姿を消したという。",
         "The new gatekeeper",
         "At the Bifrost observatory, the new gatekeeper Skurge is showing off things he picked up on Earth to some women. He finally hears Thor and opens the bridge, and Thor returns to Asgard. The dragon chasing him is cut off as the bridge closes.\n"
         "Thor asks about Heimdall and learns that Odin removed him as a traitor, and that he has disappeared."),
        ("ロキの劇",
         "アスガルドの町では、オーディンが、ロキを英雄としてたたえる劇を楽しそうに見ていた。ロキは『ダーク・ワールド』で死んだことになっていた。\n"
         "ソーはムジョルニアを遠くへ投げ、オーディンを押さえつける。戻ってくるハンマーがぶつかる直前、オーディンは正体を明かす。それは姿を変えたロキだった。",
         "Loki's play",
         "In Asgard, \"Odin\" is happily watching a play that honors Loki as a hero. Loki was thought to have died in The Dark World.\n"
         "Thor throws Mjolnir into the distance and pins \"Odin\" in its path. Just before the hammer returns, \"Odin\" drops the disguise: he is Loki."),
    ]),
    ("第2部 父との別れ", "Part 2: Farewell to a father", [
        ("取り壊された老人ホーム",
         "ロキは、本物のオーディンに魔法をかけて、地球のニューヨークの老人ホームに置いてきたと話す。2人が行ってみると、建物はもう取り壊されていた。\n"
         "そのとき、ロキの足元に穴が開き、ロキだけが消えてしまう。あとには、住所の書かれた名刺が落ちていた。",
         "The demolished retirement home",
         "Loki admits he put a spell on the real Odin and left him in a retirement home in New York. When they get there, the building has been torn down.\n"
         "Then a hole opens under Loki's feet and he vanishes, leaving behind a card with an address."),
        ("ドクター・ストレンジの館",
         "名刺の住所は、魔術師ドクター・ストレンジの館サンクタム・サンクトラムだった。ストレンジは、危険な者が地球に来たら見張っていると話し、ロキもその1人だと言う。\n"
         "ストレンジは、オーディンを見つけたらすぐ地球から出ていくことを条件に、居場所を教える。オーディンはノルウェーにいた。ストレンジは消えていたロキを落とし穴から戻し、2人をノルウェーへ送る。",
         "Doctor Strange's house",
         "The card leads to the Sanctum Sanctorum, home of the sorcerer Doctor Strange. He keeps watch on dangerous visitors to Earth, he says, and Loki is on his list.\n"
         "Strange agrees to help as long as they leave Earth once they find Odin, who is in Norway. He pulls Loki back out of the endless fall he had been stuck in and sends the brothers to Norway."),
        ("ノルウェーの海辺の告白",
         "海辺の崖の上で、オーディンは2人を待っていた。ロキの魔法はもう解けていた。オーディンは、自分の命がもうすぐ終わること、そしてラグナロクはすでに始まっていることを告げる。\n"
         "さらにオーディンは、2人が知らなかった姉の存在を明かす。最初の子ヘラは死の女神で、昔は自分と一緒に戦っていたが、あまりに血を好むので閉じこめた。自分の命が、その閉じこめる力を支えている、と。\n"
         "息子たちを愛していると言い残し、オーディンは金色の光になって消える。",
         "A confession on the Norwegian coast",
         "Odin is waiting on a seaside cliff, already free of Loki's spell. He tells his sons that he is dying and that Ragnarok has already begun.\n"
         "He then reveals a sister they never knew: his firstborn, Hela, the goddess of death. She once fought at his side, but she grew so bloodthirsty that he imprisoned her, and his life is what holds her prison shut.\n"
         "Telling his sons he loves them, Odin fades into golden light."),
        ("砕かれたハンマー",
         "直後に黒い穴が開き、ヘラが現れる。ヘラは2人にひざまずけと言う。\n"
         "ソーが投げたムジョルニアを、ヘラは片手で受け止め、そのまま握りつぶして粉々にする。",
         "The hammer is shattered",
         "A dark portal opens at once and Hela steps out, ordering them to kneel.\n"
         "Thor throws Mjolnir. Hela catches it with one hand and crushes it to pieces."),
        ("虹の橋から宇宙へ",
         "ロキはスカージに、橋を開いて自分たちを連れ戻すよう呼びかける。2人はビフレストの光の中へ逃げるが、ヘラも一緒に飛びこんでくる。\n"
         "ヘラは光の通り道の中でソーとロキを外へはじき飛ばし、自分だけアスガルドへ着く。",
         "Thrown off the Bifrost",
         "Loki calls on Skurge to bring them back. The brothers escape into the Bifrost, but Hela leaps in after them.\n"
         "Inside the beam she knocks Thor and Loki out into space, and arrives in Asgard alone."),
    ]),
    ("第3部 ヘラのアスガルド", "Part 3: Hela's Asgard", [
        ("ソーの仲間たちの死",
         "ビフレストの見張り台に着いたヘラの前に、ソーの昔からの仲間ヴォルスタッグとファンドラルが立ちはだかるが、2人はヘラに殺される。\n"
         "ヘラは、立ち向かってきたアスガルドの軍も、ほとんど1人で倒してしまう。仲間のホーガンもヘラに殺される。",
         "The deaths of Thor's friends",
         "When Hela arrives at the observatory, Thor's old friends Volstagg and Fandral stand against her, and she kills them both.\n"
         "She cuts down almost the whole Asgardian army by herself. Hogun, the third of Thor's companions, is also killed by her."),
        ("スカージがひざまずく",
         "スカージは、殺されないためにヘラにひざまずく。ヘラはスカージを、逆らう者の命を奪う処刑人に任命する。",
         "Skurge kneels",
         "To save his own life, Skurge kneels before Hela. She makes him her executioner."),
        ("天井の絵の下の歴史",
         "王宮に入ったヘラは、天井に描かれた平和な絵をはがす。その下からは、ヘラとオーディンが一緒に国々を攻め取っていく、本当の歴史の絵が現れる。\n"
         "ヘラはスカージに語る。アスガルドの豊かさは、2人が攻め取った国々から生まれた。それなのにオーディンは後に平和な王になろうとし、もっと広げようとした自分を閉じこめて、歴史から消したのだ、と。",
         "History beneath the ceiling",
         "In the palace, Hela tears away the peaceful murals on the ceiling. Underneath is the true history: Hela and Odin conquering realm after realm together.\n"
         "She tells Skurge that Asgard's riches came from those conquests. But Odin later chose to be a peaceful king, and when she wanted to keep expanding, he locked her away and erased her from history."),
        ("よみがえる兵士と巨大な狼",
         "ヘラはオーディンの宝物庫へ行き、インフィニティ・ガントレットを偽物だと言って払いのける。\n"
         "そして永遠の炎の力で、昔ともに戦って葬られた兵士たちと、巨大な狼フェンリスをよみがえらせる。ヘラはビフレストを使って、ほかの国々も支配しようと考える。",
         "The dead rise",
         "Hela goes to Odin's vault, dismisses the Infinity Gauntlet there as a fake, and uses the Eternal Flame to raise the ancient warriors who once fought beside her, along with her giant wolf Fenris.\n"
         "She plans to use the Bifrost to conquer the other realms."),
        ("ヘイムダルが剣を持ち去る",
         "しかし、ビフレストを動かすかぎの剣は、隠れていたヘイムダルに先に持ち去られていた。\n"
         "ヘイムダルは、ヘラから逃げてきた人々を山の中の隠れ家にかくまう。",
         "Heimdall takes the sword",
         "But the sword that controls the Bifrost has already been taken by Heimdall, who has been in hiding.\n"
         "He shelters the people fleeing Hela in a hidden refuge in the mountains."),
    ]),
    ("第4部 ごみの星サカール", "Part 4: Sakaar, the junk planet", [
        ("スクラッパー142",
         "ソーは、まわりを宇宙の穴に囲まれ、宇宙中のごみが降ってくる星サカールに落ちる。ごみの中で、ソーはごみを拾って暮らす人々にあみで捕まえられる。\n"
         "そこへ、酒を飲みながら小型の船でやってきた女性、スクラッパー142が、ほかの人々を追い払う。142はソーの首に、言うことを聞かせる装置を付けて動けなくする。",
         "Scrapper 142",
         "Thor crash-lands on Sakaar, a planet ringed by wormholes where the universe's junk rains down. Scavengers catch him in a net.\n"
         "A hard-drinking woman called Scrapper 142 arrives in a small ship and drives them off. She sticks an obedience disc on Thor's neck, leaving him helpless."),
        ("グランドマスターと先に着いていたロキ",
         "142はソーを、星の支配者グランドマスターに大金で売る。グランドマスターは気まぐれで、逆らった者を、相手を溶かす道具で消してしまう。\n"
         "グランドマスターのそばには、ロキがいた。ロキは何週間も前にサカールに落ち、すでにグランドマスターに気に入られていた。",
         "The Grandmaster, and Loki got there first",
         "142 sells Thor to Sakaar's ruler, the Grandmaster, for a fortune. The Grandmaster is whimsical, and he has a device that melts anyone who displeases him.\n"
         "Standing beside him is Loki, who fell onto Sakaar weeks earlier and is already one of the Grandmaster's favorites."),
        ("髪を切られる",
         "ソーは長い金色の髪を切られ、グランドマスターの戦いの見世物「コンテスト・オブ・チャンピオンズ」に出されることになる。グランドマスターは、チャンピオンに勝てば望みをかなえてやると約束する。\n"
         "ソーは控え室で、岩の体の戦士コーグと、その友だちミークに出会う。コーグは、前に反乱を起こそうとしたが、人が集まらずに失敗したと話す。",
         "The haircut",
         "Thor's long blond hair is cut off, and he is entered in the Grandmaster's Contest of Champions. The Grandmaster promises to grant his wish if he can beat the champion.\n"
         "In the holding area Thor meets Korg, a warrior made of rock, and his friend Miek. Korg says he once tried to start a revolution, but not enough people joined in."),
        ("ヴァルキリーだった女性",
         "試合の前、ソーは142の腕のしるしに気づき、彼女がアスガルドの女戦士の部隊「ヴァルキリー」の1人だと分かる。ヴァルキリーは昔、ヘラとの戦いで全滅したと伝えられていた。\n"
         "ソーは助けを求めるが、142は相手にしない。",
         "Once a Valkyrie",
         "Before the fight, Thor notices the mark on 142's arm and realizes she is one of the Valkyries, Asgard's legendary women warriors, said to have been wiped out fighting Hela long ago.\n"
         "He asks for her help, but she ignores him."),
        ("闘技場のチャンピオンはハルク",
         "大観衆の闘技場に現れたチャンピオンは、ソコヴィアの戦いのあと行方不明になっていたハルクだった。ソーは仕事仲間だと喜ぶが、ハルクは本気で襲いかかってくる。\n"
         "ソーは、ナターシャがハルクを落ち着かせるときの言葉をまねするが、効き目は一瞬だけだった。",
         "The champion is the Hulk",
         "In front of a roaring crowd, the champion turns out to be the Hulk, missing since the battle of Sokovia. Thor is delighted, calling him \"a friend from work,\" but the Hulk attacks for real.\n"
         "Thor tries the words Natasha used to calm him, \"The sun's getting real low,\" but they work for only a moment."),
        ("雷の力と決着",
         "追いつめられたソーの体に雷の力がよみがえり、ソーはハルクを押し返す。\n"
         "しかし勝つ直前、グランドマスターがソーの首の装置に電気を流し、ソーは動けなくなる。そこへハルクの一撃が入り、ソーは負ける。",
         "Lightning, then defeat",
         "Cornered, Thor feels lightning surge through him and starts to overpower the Hulk.\n"
         "But just before he can win, the Grandmaster shocks him through the disc on his neck, and the Hulk knocks him out."),
    ]),
    ("第5部 リベンジャーズ結成", "Part 5: The Revengers", [
        ("ハルクの部屋",
         "目を覚ましたソーは、ハルクの豪華な部屋にいた。ハルクはこの星で人気者になっていて、地球に帰る気はない。ソーは一緒に逃げようと持ちかけるが、ハルクは断る。",
         "The Hulk's quarters",
         "Thor wakes up in the Hulk's lavish quarters. The Hulk is a star here and has no wish to return to Earth. Thor suggests they escape together, but the Hulk refuses."),
        ("ヘイムダルの呼びかけ",
         "ソーは、遠くを見通せるヘイムダルの力で、アスガルドの様子を見る。ヘイムダルは人々を山の隠れ家にかくまっていた。\n"
         "ヘイムダルは、守る者がいなくなれば人々を連れてアスガルドを出るつもりだと話し、サカールを囲む宇宙の穴の1つを通って帰ってくるよう、ソーに伝える。",
         "Heimdall's message",
         "Through Heimdall's far-seeing power, Thor sees what is happening on Asgard. Heimdall is hiding the people in the mountains.\n"
         "Heimdall says he will lead them out of Asgard if its defenders fall, and tells Thor to come home through one of the wormholes around Sakaar."),
        ("ヴァルキリーの過去",
         "ソーは142に、オーディンが亡くなりヘラがアスガルドを乗っ取ったと伝え、もう一度助けを求める。\n"
         "しかし彼女は、昔ヘラとの戦いで仲間のヴァルキリーたちを全員失い、アスガルドの王家にも恨みを持っていた。彼女はまた断る。",
         "Valkyrie's past",
         "Thor tells 142 that Odin is dead and Hela has seized Asgard, and asks again for her help.\n"
         "But she lost every one of her fellow Valkyries fighting Hela long ago and resents Asgard's royal family. She refuses again."),
        ("クインジェットとブルース",
         "ソーは142のすきをついて自分の首の装置を外し、部屋を抜け出す。そして、ハルクが乗ってきたアベンジャーズのジェット機クインジェットを見つける。\n"
         "ソーは声で動かそうと合言葉を次々に試し、トニーが付けたあだ名「サーファーくん」で動き出す。止めに来たハルクは、画面に映ったナターシャの録画を見て、ソコヴィア以来はじめてブルース・バナーの姿に戻る。",
         "The Quinjet and Bruce",
         "Catching 142 off guard, Thor gets his own disc off and slips out. He finds the Quinjet, the Avengers' jet the Hulk arrived in.\n"
         "He tries voice passwords until \"Point Break,\" Tony's nickname for him, works. The Hulk comes to stop him, but a recording of Natasha on the screen turns him back into Bruce Banner for the first time since Sokovia."),
        ("2年ぶりのブルース",
         "ブルースは、まだソコヴィアの戦いの最中だと思っていた。2年たっていて、ここが遠い星だと聞いて、ひどく混乱する。\n"
         "ブルースは、またハルクになったら二度と戻れないかもしれないとおびえる。",
         "Bruce, two years later",
         "Bruce thinks he is still in the middle of the battle of Sokovia. Learning that two years have passed and that he is on a distant planet throws him into confusion.\n"
         "He fears that if he becomes the Hulk again, he may never come back."),
        ("142が仲間になる",
         "グランドマスターは、逃げたソーを捕まえるよう142とロキに命じる。ロキは魔法で142の記憶をのぞき、ヴァルキリーたちがヘラに倒された昔の戦いを見るが、142に倒されてしまう。\n"
         "142は、捕まえたロキを連れてソーの前に現れ、ヘラと戦う仲間になると言う。ソーはこのチームを「リベンジャーズ」と名づける。",
         "142 joins",
         "The Grandmaster orders 142 and Loki to bring Thor back. Loki uses magic to look into 142's memories and sees the ancient battle where Hela slaughtered the Valkyries, but 142 overpowers him.\n"
         "She brings the captured Loki to Thor and says she will fight Hela with him. Thor names the team the \"Revengers.\""),
    ]),
    ("第6部 サカールからの脱出", "Part 6: Escape from Sakaar", [
        ("兄弟の作戦",
         "ロキは、自分もサカールから出してもらう代わりに手を貸すと言う。一行は、グランドマスターの宇宙船を奪う計画を立てる。\n"
         "ソーとロキは、子どものころからの2人の作戦で、見張りの兵士たちを倒す。",
         "The brothers' plan",
         "Loki offers to help in exchange for a way off Sakaar, and the group plans to steal one of the Grandmaster's ships.\n"
         "Thor and Loki take out the guards with \"Get Help,\" a trick they say they used as kids."),
        ("ロキの裏切りを見ぬく",
         "ソーは、ロキに、もうお前とは別々の道を行くつもりだと話す。そのとおり、ロキはソーを売ろうとして兵士を呼ぶ。\n"
         "しかしソーは、前もってロキの背中に首の装置を付けていた。ロキは電気で動けなくなり、その場に置き去りにされる。",
         "Seeing through Loki",
         "Thor tells Loki he thinks it's best they go their separate ways. Sure enough, Loki tries to sell him out and calls the guards.\n"
         "But Thor has already stuck an obedience disc on Loki's back. Loki is left on the floor, twitching from the shocks."),
        ("闘技場の反乱",
         "ソーたちは、闘技場の戦士たちの首の装置を外して自由にする。コーグとミークを先頭に、戦士たちは反乱を起こし、町は大さわぎになる。\n"
         "置き去りにされたロキは、反乱するコーグたちに見つけられ、一緒に行動する。",
         "The gladiators revolt",
         "Thor's group frees the gladiators from their discs. Led by Korg and Miek, they rise up, and the city erupts.\n"
         "The abandoned Loki is found by Korg's rebels and joins them."),
        ("宇宙の穴を抜けて",
         "ソー、ブルース、142は、グランドマスターの船を奪って飛び立つ。追いかけてくる船をソーが銃でうち落とし、142が操縦でかわす。\n"
         "3人は、サカールを囲む巨大な宇宙の穴に飛びこみ、アスガルドへ向かう。",
         "Through the wormhole",
         "Thor, Bruce and 142 take off in one of the Grandmaster's ships. Thor shoots down the pursuers while 142 dodges the rest.\n"
         "They dive into a huge wormhole around Sakaar and head for Asgard."),
    ]),
    ("第7部 アスガルドの戦い", "Part 7: The battle for Asgard", [
        ("橋の上の人々",
         "アスガルドでは、ヘラが人々の隠れ家に兵士を送りこんでいた。ヘイムダルは人々を連れてビフレストの橋を渡り、逃げようとする。\n"
         "しかし、よみがえった兵士たちと狼のフェンリスに追いつかれ、人々は橋の上で追いつめられる。",
         "The people on the bridge",
         "On Asgard, Hela's soldiers have found the people's refuge. Heimdall leads them across the Bifrost bridge to escape.\n"
         "But Hela's undead army and the wolf Fenris catch up with them, trapping the people on the bridge."),
        ("ソーたちの到着",
         "そこへソーが雷とともに橋に降り立ち、兵士たちを倒していく。142もアスガルドの人々を守って戦う。\n"
         "ブルースは船から飛び降りてハルクになろうとするが、ブルースのまま橋に顔から落ちてしまう。そのあとハルクになり、フェンリスと戦う。",
         "Thor's team arrives",
         "Thor lands on the bridge in a blast of lightning and starts cutting through the army, while 142 fights to protect the people.\n"
         "Bruce leaps from the ship to transform into the Hulk, but simply face-plants on the bridge as Bruce. Later he becomes the Hulk and takes on Fenris."),
        ("ロキが戻る",
         "ヘラの兵士たちがさらに増えたとき、ロキが、コーグたち反乱の戦士を乗せた大きな宇宙船でやってくる。\n"
         "ロキは、自分が助けに来たと名乗り、人々を船へ乗せはじめる。",
         "Loki returns",
         "As Hela's army keeps coming, Loki arrives in a huge spaceship carrying Korg and the rebel gladiators.\n"
         "He announces that their savior is here and starts getting the people aboard."),
        ("スカージの決断",
         "ヘラの処刑人になっていたスカージは、逃げる人々を見て考えを変える。地球から持ち帰った2丁の銃を手に、ヘラの兵士たちに1人で立ち向かう。\n"
         "スカージは、人々が船に乗る時間をかせぎながら、命を落とす。",
         "Skurge's choice",
         "Watching the people flee, Skurge, Hela's executioner, has a change of heart. With the two rifles he brought back from Earth, he stands alone against Hela's army.\n"
         "He buys time for the people to board the ship, and dies doing it."),
    ]),
    ("第8部 ラグナロク", "Part 8: Ragnarok", [
        ("片目を失う",
         "王宮で、ソーはヘラと1対1で戦う。ハンマーのないソーはヘラに押され、右目を切られて失う。",
         "Losing an eye",
         "In the palace, Thor faces Hela alone. Without his hammer he is outmatched, and she slashes out his right eye."),
        ("父の幻",
         "倒れたソーの前に、父オーディンの幻が現れる。オーディンは、お前はハンマーの神なのかとたずね、ハンマーは力を使いこなすための道具にすぎなかったと教える。\n"
         "目を覚ましたソーの体から、これまでにない大きな雷があふれ出す。ソーは空から橋に降り立ち、ヘラの兵士たちを一気に倒す。",
         "A vision of Odin",
         "As Thor lies beaten, a vision of Odin appears. He asks, \"Are you Thor, the God of Hammers?\" and reminds him the hammer was only ever a way to help him control his power.\n"
         "Thor wakes with lightning pouring out of him like never before. He comes down on the bridge and wipes out Hela's soldiers in one blow."),
        ("アスガルドは場所ではなく民",
         "それでもヘラは倒れない。ヘラはアスガルドから力を得ていて、アスガルドにいる限り強くなり続けるからだ。\n"
         "ソーは、アスガルドとは場所ではなく、そこに生きる民のことだと気づく。そして、ヘラを止めるにはラグナロクを起こすしかないと決める。",
         "Asgard is its people",
         "Hela still won't fall. She draws her power from Asgard, and as long as she is there she keeps getting stronger.\n"
         "Thor realizes that Asgard is not a place but its people, and decides the only way to stop Hela is to let Ragnarok happen."),
        ("スルトのよみがえり",
         "ソーはロキに、スルトの冠を宝物庫の永遠の炎に入れるよう頼む。宝物庫でロキは、そこにしまわれていた四次元キューブに目をとめる。\n"
         "冠を炎に入れると、スルトは元の巨大な姿でよみがえる。ハルクがスルトに飛びかかるが、ソーはハルクを呼び戻し、みんなで船へ逃げる。",
         "Surtur rises",
         "Thor asks Loki to put Surtur's crown in the Eternal Flame. In the vault, Loki pauses at the Tesseract stored there.\n"
         "When the crown meets the flame, Surtur is reborn at full size. The Hulk leaps at him, but Thor calls him back and everyone escapes to the ship."),
        ("アスガルドの最後",
         "船の上から、人々は燃えるアスガルドを見つめる。ヘラはスルトを止めようと立ち向かうが、スルトが剣を突き立てるとアスガルドは爆発し、ヘラもその中で消える。",
         "The end of Asgard",
         "From the ship, the people watch Asgard burn. Hela tries to stop Surtur, but he drives his sword into Asgard, which explodes, taking Hela with it."),
        ("新しい王",
         "船の上でソーは、ヘイムダルたちにすすめられて王の座につく。ソーはロキに、もしここにいるなら抱きしめてもいいと言って物を投げる。ロキはそれを受け止め、自分はここにいると答える。\n"
         "ソーは、民を連れて地球へ向かうことを決める。",
         "The new king",
         "Aboard the ship, Thor takes the throne at the urging of Heimdall and the others. He tells Loki that if he were really there, he might even give him a hug, and tosses something at him. Loki catches it and says, \"I'm here.\"\n"
         "Thor decides to take his people to Earth."),
    ]),
    ("第9部 エンドクレジットの映像", "Part 9: The credit scenes", [
        ("途中の映像",
         "船の上で、ロキは地球へ行くのはいい考えなのか、と心配する。ソーは、きっとうまくいくと答える。\n"
         "そのとき、2人の目の前に巨大な宇宙船が現れる。",
         "Mid-credits",
         "On the ship, Loki wonders whether going to Earth is really a good idea. Thor says it will be fine.\n"
         "Then an enormous spaceship appears in front of them."),
        ("最後の映像",
         "反乱のあとのサカール。ごみの山にたどり着いたグランドマスターが、反乱した人々に囲まれ、「今回は引き分けかな」と言い訳をする。",
         "After the credits",
         "On Sakaar after the revolt, the Grandmaster, surrounded by the rebels on a junk heap, tries to tell them the revolution was a tie."),
    ]),
    ("まとめ", "Summary", [
        ("ラグナロクはどう起きたか",
         "スルトは、自分の冠を永遠の炎に入れるとアスガルドを焼きつくすと話した（第1部）。ソーは冠を奪って防いだつもりだった。\n"
         "しかしヘラはアスガルドから力を得ていて、そこにいる限り倒せなかった（第8部）。ソーは、アスガルドとは場所ではなく民だと考え、民を船で逃がしたうえで、ロキに冠を炎へ入れさせた。よみがえったスルトがアスガルドとヘラを滅ぼした（第8部）。",
         "How Ragnarok came about",
         "Surtur said that once his crown met the Eternal Flame, he would burn Asgard to the ground (Part 1). Thor thought he had stopped it by taking the crown.\n"
         "But Hela drew her power from Asgard and couldn't be beaten there (Part 8). Deciding that Asgard was its people, not a place, Thor got the people onto the ship and had Loki put the crown in the flame. The reborn Surtur destroyed Asgard and Hela with it (Part 8)."),
        ("仲間になった人たち",
         "・ハルク／ブルース：ソコヴィアのあと2年間サカールで戦いのチャンピオンだった。ナターシャの録画でブルースに戻り（第5部）、最後はハルクとしてフェンリスと戦った（第7部）。\n"
         "・ヴァルキリー（スクラッパー142）：ヘラに仲間を全員殺され、サカールで暮らしていた。ヘラの記憶と向き合い、ソーの仲間になった（第5部）。\n"
         "・ロキ：ソーを裏切ろうとして置き去りにされたが（第6部）、反乱の戦士たちと船で戻り、アスガルドの人々を助けた（第7部）。\n"
         "・スカージ：命が惜しくてヘラの処刑人になったが、最後は人々を守って死んだ（第3部・第7部）。",
         "Who joined Thor",
         "- Hulk / Bruce: spent two years after Sokovia as Sakaar's champion. A recording of Natasha turned him back into Bruce (Part 5), and in the end he fought Fenris as the Hulk (Part 7).\n"
         "- Valkyrie (Scrapper 142): lost all her sisters to Hela and had been living on Sakaar. She faced her memories of Hela and joined Thor (Part 5).\n"
         "- Loki: tried to betray Thor and was left behind (Part 6), but came back with the rebel gladiators in a ship and helped save the people of Asgard (Part 7).\n"
         "- Skurge: became Hela's executioner to save his own life, but died protecting the people in the end (Parts 3 and 7)."),
        ("死んだ人たち（話の順に）",
         "・オーディン（第2部）：寿命が尽きて、ノルウェーの海辺で金色の光になって消えた。その死で、閉じこめられていたヘラが自由になった。\n"
         "・ヴォルスタッグとファンドラル（第3部）：ソーの仲間。アスガルドに着いたヘラに立ち向かい、殺された。\n"
         "・ホーガン（第3部）：ソーの仲間。ヘラに立ち向かい、殺された。\n"
         "・スカージ（第7部）：人々が船に乗る時間をかせぐため、2丁の銃でヘラの兵士たちに1人で立ち向かい、命を落とした。\n"
         "・ヘラ（第8部）：ソーがロキに頼んでよみがえらせたスルトが、剣でアスガルドを突いて爆発させ、その中で消えた。",
         "Who died (in order)",
         "- Odin (Part 2): his life came to an end on the Norwegian coast and he faded into golden light. His death freed the imprisoned Hela.\n"
         "- Volstagg and Fandral (Part 3): Thor's friends, killed when they stood against Hela on her arrival in Asgard.\n"
         "- Hogun (Part 3): Thor's friend, killed standing up to Hela.\n"
         "- Skurge (Part 7): stood alone against Hela's army with his two rifles to buy time for the people to board the ship, and died.\n"
         "- Hela (Part 8): destroyed when Surtur, reborn at Thor's request through Loki, drove his sword into Asgard and blew it apart."),
    ]),
]
