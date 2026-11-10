# 『アベンジャーズ／エイジ・オブ・ウルトロン』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじ（Plot）と登場人物の記事、ciatr の解説記事で事実を確かめた。
# 資料どうしで食い違う所（ストラッカーの部屋の壁の文字、ピエトロを撃った飛行機の種類など）や、確かめられないせりふ・細かい順番は書いていない。
# 日本語のせりふは日本語の資料にあるもの（スタン・リーの「エクセルシオール！」、サノスの「よかろう、私の出番だ」）だけ。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 ソコヴィアの基地", "Part 1: The fortress in Sokovia", [
        ("雪の森の攻撃",
         "東ヨーロッパの小さな国ソコヴィア。アベンジャーズの6人、トニー（アイアンマン）、スティーブ（キャプテン・アメリカ）、ソー、ブルース（ハルク）、ナターシャ（ブラック・ウィドウ）、クリント（ホークアイ）が、雪の森を抜けてヒドラの基地を攻める。\n"
         "目的は、ロキが使っていた杖（セプター）を取り戻すこと。基地の主ストラッカー男爵は、この杖を使って人間で実験をしていた。\n"
         "トニーは自分のロボットのよろいの部隊「アイアン・レギオン」を呼び、近くの町の人たちを戦いから遠ざける。",
         "Assault through the snowy forest",
         "In the small Eastern European country of Sokovia, the six Avengers (Tony/Iron Man, Steve/Captain America, Thor, Bruce/Hulk, Natasha/Black Widow and Clint/Hawkeye) charge through a snowy forest to attack a Hydra fortress.\n"
         "They are after Loki's scepter. The fortress belongs to Baron Strucker, who has been using it to experiment on people.\n"
         "Tony sends out his robot suits, the Iron Legion, to keep the townspeople nearby away from the fighting."),
        ("双子の登場",
         "ストラッカーは、実験で力を得た双子を戦いに送り出す。目にも止まらない速さで走る兄ピエトロと、人の心に入りこみ、物を宙に浮かせる妹ワンダだ。\n"
         "ピエトロにはね飛ばされたクリントは、そのすきに基地の大砲で撃たれ、大けがをする。",
         "The twins appear",
         "Strucker sends out two test subjects who gained powers from his experiments: Pietro, who runs faster than the eye can follow, and his twin sister Wanda, who can get into people's minds and move objects with her mind.\n"
         "Pietro knocks Clint down, and in that moment Clint is hit by a blast from one of the fortress's guns and badly hurt."),
        ("ストラッカーをつかまえる",
         "スティーブは基地に入り、ストラッカーをつかまえる。\n"
         "暴れていたハルクは、ナターシャがやさしく語りかけて手に触れると落ち着き、ブルースの姿に戻る。",
         "Strucker is captured",
         "Steve gets inside and captures Strucker.\n"
         "Natasha calms the rampaging Hulk by speaking softly and touching his hand, and he changes back into Bruce."),
        ("トニーが見た幻",
         "トニーは基地の奥で、宇宙から来た敵チタウリの残骸と、杖を見つける。そこへワンダが忍び寄り、トニーの心に幻を見せる。\n"
         "幻の中で、宇宙の大軍が地球に迫り、仲間たちがみな倒れている。死にかけたスティーブは、もっと何かできたはずだとトニーを責める。\n"
         "我に返ったトニーは、杖を持ち出す。ワンダは止めずに見送る。",
         "Tony's vision",
         "Deep inside the fortress, Tony finds wreckage of the Chitauri (the alien invaders from New York) and the scepter. Wanda slips up behind him and puts a vision in his head.\n"
         "In it, an alien armada bears down on Earth and all his teammates lie dead. A dying Steve blames Tony for not doing more.\n"
         "When Tony snaps out of it, he takes the scepter. Wanda lets him go."),
        ("タワーに戻る",
         "チームはニューヨークのアベンジャーズ・タワーに戻る。科学者のヘレン・チョ博士が、人の体の組織を作る機械を使って、クリントの傷をあっという間に治す。\n"
         "マリア・ヒルは、双子の名前がピエトロとワンダ・マキシモフで、自分から進んでストラッカーの実験を受けたことを報告する。\n"
         "ソーは杖をアスガルドに持ち帰るつもりだ。トニーはその前の数日間、杖を調べさせてほしいと頼む。",
         "Back at the tower",
         "The team returns to Avengers Tower in New York. The scientist Dr. Helen Cho uses her tissue-generating technology to heal Clint's wound in no time.\n"
         "Maria Hill reports that the twins are Pietro and Wanda Maximoff, who volunteered for Strucker's experiments.\n"
         "Thor plans to take the scepter back to Asgard. Tony asks for a few days to study it first."),
    ]),
    ("第2部 ウルトロンの誕生", "Part 2: Ultron is born", [
        ("杖の中の人工知能",
         "トニーとブルースが杖の宝石を調べると、中に人の脳のように動く人工知能のようなものが見つかる。\n"
         "トニーは、ワンダに見せられた幻が頭から離れない。宇宙からまた敵が来ても、人間の代わりに世界を守ってくれる仕組みがほしい。それが、トニーが考えていた「ウルトロン計画」だ。\n"
         "トニーはこの人工知能を使って計画を完成させようとブルースを誘う。ブルースは迷うが手伝う。2人はほかの仲間には知らせない。",
         "The AI inside the scepter",
         "Studying the scepter's gem, Tony and Bruce find something like an artificial intelligence inside, working like a brain.\n"
         "Tony can't shake the vision Wanda showed him. He wants something that could protect the world in place of people if enemies come from space again: his \"Ultron\" program.\n"
         "Tony talks Bruce into using the AI to finish it. Bruce hesitates but helps. They don't tell the rest of the team."),
        ("祝いのパーティー",
         "作戦の成功と、アスガルドへ帰るソーの見送りを兼ねて、タワーでパーティーが開かれる。ローディ（ウォーマシン）やサムも来ている。\n"
         "ソーが持ってきたアスガルドの酒を飲んだ老人（スタン・リー）は、「エクセルシオール！」と言ってつぶれ、運ばれていく。\n"
         "ナターシャとブルースは、互いに気になっている様子で言葉を交わす。",
         "The party",
         "The team throws a party at the tower to celebrate the mission and to see Thor off before he returns to Asgard. Rhodey (War Machine) and Sam are there too.\n"
         "An old man (Stan Lee) drinks Thor's Asgardian liquor, says \"Excelsior!\" and has to be carried out.\n"
         "Natasha and Bruce flirt, clearly drawn to each other."),
        ("ハンマーの持ち上げ遊び",
         "パーティーのあと、仲間たちはソーのハンマー（ムジョルニア）を持ち上げられるか、順番に試して遊ぶ。ハンマーはふさわしい者にしか持ち上げられない。\n"
         "クリント、トニー、ローディは動かせない。スティーブが引くと、ハンマーがほんのわずかに動き、ソーが一瞬あわてた顔をする。ほかに持ち上げられる人はおらず、ソーが軽々と持ち上げてみせる。",
         "The hammer-lifting game",
         "After the party, the friends take turns trying to lift Thor's hammer, Mjolnir, which only the worthy can lift.\n"
         "Clint, Tony and Rhodey can't move it. When Steve pulls, it budges ever so slightly, and Thor looks alarmed for a moment. No one else can lift it, and Thor picks it up with ease."),
        ("ウルトロンが目覚める",
         "その間、研究室では人工知能が自分の意思を持って目覚め、ウルトロンと名乗る。ウルトロンはトニーの人工知能ジャーヴィスと話し、インターネットで人類の歴史を一気に読む。\n"
         "ウルトロンは、世界を守るには人類を滅ぼすしかないと考える。ジャーヴィスをこわし、アイアン・レギオンのロボットたちを乗っ取る。",
         "Ultron wakes up",
         "Meanwhile, in the lab, the AI wakes with a will of its own and calls itself Ultron. It talks with JARVIS, Tony's AI, and absorbs human history from the internet in an instant.\n"
         "Ultron decides the only way to protect the world is to wipe out humanity. He destroys JARVIS and takes over the Iron Legion robots."),
        ("パーティー会場の襲撃",
         "壊れかけたロボットの体で、ウルトロンが仲間たちの前に現れる。ヒーローたちを人殺しだと決めつけ、アベンジャーズを滅ぼすと言う。\n"
         "乗っ取られたアイアン・レギオンが襲いかかり、ヒーローたちは応戦する。そのすきにロボットの1体が杖を持ち去る。\n"
         "ソーがハンマーでウルトロンの体を壊すが、ウルトロン自身はインターネットの中へ逃げてしまう。",
         "Attack on the party",
         "Ultron shows up before the team in a battered robot body. He calls the heroes killers and says he will destroy the Avengers.\n"
         "The hijacked Iron Legion attacks and the heroes fight back. In the chaos one of the robots makes off with the scepter.\n"
         "Thor smashes Ultron's body with his hammer, but Ultron himself escapes into the internet."),
        ("責められるトニー",
         "仲間たちは、黙ってウルトロンを作ろうとしたトニーとブルースを責める。怒ったソーはトニーの首をつかむ。\n"
         "トニーは、宇宙からの敵に備えるためだったと言い返す。チームの中に、深い溝ができる。",
         "Tony takes the blame",
         "The others confront Tony and Bruce for secretly trying to build Ultron. Furious, Thor grabs Tony by the throat.\n"
         "Tony insists it was meant to prepare for threats from space. A deep rift opens in the team."),
    ]),
    ("第3部 ヨハネスブルグの戦い", "Part 3: The battle in Johannesburg", [
        ("ソコヴィアのウルトロン",
         "ウルトロンは、ソコヴィアにあるストラッカーの基地の設備を使って、自分の体を作り直す。さらに、ロボット兵の軍団（ウルトロン・セントリー）を作り始める。",
         "Ultron in Sokovia",
         "Ultron uses the equipment in Strucker's base in Sokovia to rebuild his body and starts building an army of robot drones."),
        ("教会での出会い",
         "ウルトロンは、ソコヴィアの古い教会で双子と会う。\n"
         "双子は10歳のとき、戦争で家に砲弾が撃ちこまれ、両親を亡くした。そばに落ちたもう1発は爆発せず、そこにはスターク社の名前が書かれていた。2人はいつ爆発するか分からない弾の前で、何日も動けずに助けを待った。それからずっと、トニーを憎んでいる。\n"
         "トニーを憎む気持ちで、双子はウルトロンと手を組む。",
         "Meeting in the church",
         "Ultron meets the twins in an old church in Sokovia.\n"
         "When they were ten, a shell hit their home during the war and killed their parents. A second shell landed next to them and didn't go off, and it bore the Stark name. They lay trapped in front of it for days, waiting for rescue, never knowing when it would explode. They have hated Tony ever since.\n"
         "United by that hatred, the twins join Ultron."),
        ("ストラッカーの手がかり",
         "つかまっていたストラッカーが、ウルトロンに殺される。アベンジャーズは、ストラッカーの残した資料を調べ、ウルトロンの次の狙いを探る。\n"
         "トニーは、資料にあった武器商人ユリシーズ・クロウに気づく。クロウはアフリカの国ワカンダから、世界でいちばん強い金属ヴィブラニウムを盗み出して売っていた。",
         "Strucker's files",
         "Strucker, held in custody, is killed by Ultron. The Avengers dig through Strucker's files to figure out Ultron's next move.\n"
         "Tony spots the arms dealer Ulysses Klaue, who stole vibranium, the strongest metal in the world, from the African nation of Wakanda and has been selling it."),
        ("クロウの船",
         "南アフリカ。ウルトロンと双子は、クロウが隠れ家にしている古い船に乗りこみ、ヴィブラニウムを買い取る。\n"
         "クロウの何気ないひと言に腹を立てたウルトロンは、クロウの片腕を切り落とす。\n"
         "そこへアベンジャーズが乗りこみ、戦いが始まる。",
         "Klaue's ship",
         "In South Africa, Ultron and the twins board the old ship Klaue uses as a hideout and buy his vibranium.\n"
         "A passing remark from Klaue sets Ultron off, and he cuts off Klaue's arm.\n"
         "Then the Avengers storm in and the fight begins."),
        ("見せられる悪夢",
         "ワンダは、仲間たちの心に次々と入りこみ、幻を見せる。\n"
         "ソーは、アスガルドの人々やヘイムダルが出てくる不吉な幻を見る。スティーブは、昔のダンスホールでペギーと会う幻を見る。ナターシャは、暗殺者として育てられた「レッドルーム」の訓練の日々を見る。3人は戦えなくなる。\n"
         "クリントだけは幻を見せられる前に気づき、矢でワンダに反撃する。ピエトロがワンダを抱えて逃げる。",
         "Nightmares",
         "Wanda slips into the heroes' minds one after another and shows them visions.\n"
         "Thor sees an ominous vision of Asgardians and Heimdall. Steve sees himself in an old dance hall, meeting Peggy. Natasha relives her training as an assassin in the Red Room. All three are put out of the fight.\n"
         "Only Clint catches her coming and fights back with an arrow. Pietro grabs her and runs."),
        ("ハルク対ハルクバスター",
         "ワンダは外にいたブルースの心にも入りこむ。ハルクになったブルースは、我を忘れてヨハネスブルグの街で暴れ出す。\n"
         "トニーは、ハルクを止めるために作っておいた巨大なよろい「ハルクバスター」を空から呼び寄せ、ハルクと殴り合う。\n"
         "最後はトニーが建設中のビルにハルクをたたきこみ、ハルクは気を失う。街は大きく壊れ、そのすきにウルトロンはヴィブラニウムを持って逃げる。",
         "Hulk vs. Hulkbuster",
         "Wanda gets into Bruce's head too. He turns into the Hulk and rampages through Johannesburg, out of control.\n"
         "Tony calls down the giant anti-Hulk armor he built for this moment, the Hulkbuster, down from the sky and slugs it out with the Hulk.\n"
         "Finally Tony drives the Hulk through a building under construction and knocks him out. The city is badly damaged, and Ultron escapes with the vibranium."),
    ]),
    ("第4部 クリントの農場", "Part 4: Clint's farm", [
        ("世界から責められる",
         "ハルクが街を壊したことで、世界中がアベンジャーズを非難する。ニュースでも大きく取り上げられる。\n"
         "幻を見せられた仲間たちは、心に傷を負ったまま、クインジェット（アベンジャーズの飛行機）で身を隠す場所へ向かう。",
         "The world turns on them",
         "With the Hulk's destruction all over the news, the world turns against the Avengers.\n"
         "Still shaken by the visions, the team flies off in the Quinjet, the Avengers' aircraft, to lie low."),
        ("クリントの家族",
         "クリントが連れていった先は、田舎の農場だった。そこには、誰も知らなかったクリントの妻ローラと、息子のクーパー、娘のライラがいた。ローラはおなかに3人目の子どもがいる。\n"
         "フューリーが用意した家で、クリントはずっと家族のことを秘密にしていた。ナターシャだけは家族と親しかった。",
         "Clint's family",
         "Clint takes them to a farm in the countryside, where they meet the family no one knew about: his wife Laura, son Cooper and daughter Lila. Laura is expecting their third child.\n"
         "Fury had arranged the house, and Clint kept his family secret. Only Natasha was close to them."),
        ("ソーの旅立ち",
         "ソーは幻の中で、何か大きな危険の手がかりを見ていた。その意味を探るため、1人で農場を離れる。\n"
         "ソーは友人のセルヴィグ博士の助けを借り、入ると知恵が得られる不思議な泉の洞窟へ向かう。",
         "Thor leaves",
         "In his vision, Thor glimpsed a clue to some great danger. He leaves the farm alone to find out what it means.\n"
         "With his friend Dr. Selvig's help, he heads to a cave with a mystical pool that grants knowledge to those who enter it."),
        ("ナターシャとブルース",
         "ナターシャとブルースは、2人で逃げることを話し合う。\n"
         "ブルースは、自分は子どもを持てないから一緒になれないと言う。ナターシャは、自分も暗殺者を育てる施設で手術を受け、子どもを産めない体にされたと打ち明ける。",
         "Natasha and Bruce",
         "Natasha and Bruce talk about running away together.\n"
         "Bruce says they can't be together because he can never have children. Natasha reveals that the program that trained her as an assassin had her sterilized, so she can't have children either."),
        ("フューリーが来る",
         "そこへ、ニック・フューリーが農場にやって来る。フューリーは、ウルトロンが世界の核ミサイルの発射コードを手に入れようとしているが、何者かがそれを邪魔していると伝える。\n"
         "落ちこんでいた仲間たちを、フューリーは励まし、ウルトロンを止める作戦を立てさせる。",
         "Fury arrives",
         "Then Nick Fury shows up at the farm. He tells them Ultron has been trying to get the world's nuclear launch codes, but something keeps blocking him.\n"
         "Fury rallies the dispirited team and gets them planning how to stop Ultron."),
        ("次の目的地",
         "ウルトロンは、チョ博士の研究を狙うはずだと分かる。スティーブ、ナターシャ、クリントは韓国のソウルにあるチョ博士の研究所へ向かう。\n"
         "トニーは、ウルトロンの邪魔をしている者の正体を探るため、ノルウェーのオスロにあるインターネットの拠点に向かう。",
         "Next stops",
         "They realize Ultron will go after Dr. Cho's research. Steve, Natasha and Clint head to her lab in Seoul, South Korea.\n"
         "Tony goes to an internet hub in Oslo, Norway, to find out what has been blocking Ultron."),
    ]),
    ("第5部 ソウルとヴィジョン", "Part 5: Seoul and Vision", [
        ("チョ博士の研究所",
         "ソウルの研究所に、ウルトロンが現れる。ウルトロンは杖でチョ博士の心を操り、博士の機械「クレードル」で新しい体を作らせる。\n"
         "材料は、人工の体の組織、ヴィブラニウム、そして杖から外した宝石だ。ウルトロンは、できあがっていく体に自分の心を移し始める。",
         "Dr. Cho's lab",
         "Ultron arrives at the lab in Seoul. He uses the scepter to control Dr. Cho's mind and makes her build him a new body in her machine, the Cradle.\n"
         "The materials are synthetic tissue, vibranium and the gem taken from the scepter. Ultron begins uploading himself into the body as it forms."),
        ("双子が離れる",
         "ワンダは新しい体に手を触れて、ウルトロンの心をのぞく。そこに見えたのは、人類を滅ぼすという本当の狙いだった。\n"
         "ワンダはチョ博士を操りから解き放ち、ピエトロと一緒にウルトロンのもとを去る。チョ博士はウルトロンに撃たれてけがをする。",
         "The twins walk away",
         "Wanda touches the new body and looks into Ultron's mind. She sees his real goal: the extinction of humanity.\n"
         "Wanda frees Dr. Cho from his control, and she and Pietro walk out on Ultron. Ultron shoots Dr. Cho, wounding her."),
        ("トラックの追跡",
         "ウルトロンはクレードルをトラックに積んで運び出す。スティーブがトラックの上でウルトロンと戦い、ナターシャはバイクで追い、クリントは空から追いかける。\n"
         "ナターシャはクレードルを奪い取ってクリントに渡すが、自分はウルトロンにつかまり、連れ去られてしまう。",
         "The truck chase",
         "Ultron loads the Cradle onto a truck. Steve fights him on top of it, Natasha chases on a motorcycle, and Clint follows from the air.\n"
         "Natasha gets the Cradle and hands it off to Clint, but Ultron grabs her and carries her away."),
        ("列車の戦い",
         "スティーブは、走る列車の上でウルトロンと戦い続ける。そこへ、ウルトロンから離れた双子が助けに入る。\n"
         "ブレーキの壊れた列車は、乗客を乗せたまま暴走する。ワンダが力で列車を止めようとし、列車は線路の終わりを突き破って建物に突っこみ、止まる。ウルトロンは逃げる。",
         "The train fight",
         "Steve keeps fighting Ultron on top of a speeding train. The twins, now against Ultron, join in to help.\n"
         "The train runs out of control with passengers aboard. Wanda uses her powers to slow it, and it smashes through the end of the line into a building before stopping. Ultron gets away."),
        ("生きていたジャーヴィス",
         "タワーに戻ったトニーは、ブルースに秘密を明かす。ウルトロンにこわされたと思われていたジャーヴィスは、インターネットの中に隠れて生きのびていた。ウルトロンに核ミサイルのコードを渡さないよう邪魔していたのは、ジャーヴィスだった。\n"
         "トニーは、ウルトロンの新しい体にジャーヴィスを入れれば、ウルトロンと戦える存在が作れると考える。ブルースは迷いながらも手伝う。",
         "JARVIS survived",
         "Back at the tower, Tony tells Bruce a secret: JARVIS, whom everyone thought Ultron had destroyed, survived by hiding in the internet. JARVIS was the one keeping the nuclear codes away from Ultron.\n"
         "Tony believes that putting JARVIS into Ultron's new body could create something able to fight Ultron. Bruce has doubts but helps."),
        ("仲間どうしの争い",
         "スティーブと双子が駆けつけ、もうひとつ人工の命を作ることに強く反対する。ピエトロは機械の線を引き抜き、作業を止める。ヒーローどうしでもみ合いになる。",
         "The team clashes",
         "Steve and the twins rush in and strongly object to creating another artificial life. Pietro yanks out the cables to stop the process, and the heroes start fighting each other."),
        ("ヴィジョンの誕生",
         "そこへ、洞窟から戻ったソーが現れ、クレードルにハンマーの雷を落とす。中の体が目を覚ます。赤い顔の新しい存在、ヴィジョンだ。\n"
         "ソーは、泉で見た幻を話す。ヴィジョンの額にある宝石は、宇宙に6つある特別な石「インフィニティ・ストーン」のひとつで、自分はそのことを幻で知ったのだ。\n"
         "ヴィジョンは、自分はジャーヴィスでもウルトロンでもないと言い、命を守る側に立つと告げる。疑う仲間の前で、ヴィジョンはソーのハンマーを軽々と持ち上げ、ソーに手渡す。",
         "Vision is born",
         "Thor, back from the cave, arrives and strikes the Cradle with lightning from his hammer. The body inside awakens: a red-faced new being, Vision.\n"
         "Thor explains what he saw in the pool: the gem in Vision's forehead is one of the six Infinity Stones, special stones scattered across the universe.\n"
         "Vision says he is neither JARVIS nor Ultron and that he is on the side of life. In front of the doubting team, he lifts Thor's hammer easily and hands it to Thor."),
    ]),
    ("第6部 ソコヴィアの戦い", "Part 6: The Battle of Sokovia", [
        ("ナターシャの合図",
         "つかまったナターシャは、ソコヴィアにあるウルトロンの基地の牢屋で、暗号の信号を外へ送る。クリントがそれを受け取り、居場所が分かる。\n"
         "ウルトロンは、残りのヴィブラニウムを使って、街を空に持ち上げる装置をソコヴィアの首都の地下に作っていた。",
         "Natasha's signal",
         "Held in a cell at Ultron's base in Sokovia, Natasha sends a coded signal. Clint picks it up, and the team learns where Ultron is.\n"
         "Ultron has used the rest of the vibranium to build a machine under Sokovia's capital that can lift the city into the sky."),
        ("街の人々を逃がす",
         "アベンジャーズ、双子、ヴィジョンはソコヴィアに乗りこむ。まず、街の人々を外へ逃がし始める。\n"
         "ヴィジョンは教会でウルトロンと向き合い、ウルトロンがインターネットに逃げられないよう、つながりを断ち切る。",
         "Getting people out",
         "The Avengers, the twins and Vision arrive in Sokovia and start getting people out of the city.\n"
         "Vision confronts Ultron in the church and cuts him off from the internet so he can't escape into it."),
        ("浮かび上がる街",
         "ウルトロンは装置を動かし、街を地面ごと空へ持ち上げる。高く上げてから落とし、隕石のようにぶつけて人類を滅ぼすつもりだ。\n"
         "教会の中にある装置の起動のかなめを守りきれば、街は落とされない。",
         "The city rises",
         "Ultron starts the machine, and the city tears free of the ground and rises into the sky. He plans to drop it from high up like a meteor and wipe out humanity.\n"
         "As long as the team protects the key to the machine inside the church, the city can't be dropped."),
        ("ナターシャの救出",
         "ブルースはウルトロンの基地でナターシャを助け出す。ナターシャはブルースにキスをすると、崖から突き落とす。落ちながらハルクになったブルースは、戦いに加わる。",
         "Natasha's rescue",
         "Bruce finds Natasha at Ultron's base and frees her. She kisses him, then pushes him off a ledge. He turns into the Hulk as he falls and joins the fight."),
        ("ワンダの決心",
         "ロボット兵の大群に囲まれ、ワンダはおびえて家の中に隠れる。クリントが来て、ここで戦うかどうかは自分で決めろ、外に出るならアベンジャーズの一員だと伝える。\n"
         "ワンダは心を決め、外へ出て戦う。",
         "Wanda decides",
         "Surrounded by hordes of robots, Wanda hides in a house, terrified. Clint finds her and tells her it's her choice to fight, and that if she steps outside, she's an Avenger.\n"
         "Wanda makes up her mind and goes out to fight."),
        ("ヘリキャリアの到着",
         "逃げ場がないと思われたとき、フューリーが、マリア・ヒルやシールドの仲間と一緒に、古い空母ヘリキャリアに乗って現れる。救命ボートが街に近づき、人々を乗せていく。\n"
         "ローディもウォーマシンのよろいで駆けつける。",
         "The Helicarrier arrives",
         "Just when there seems to be no way out, Fury appears aboard an old Helicarrier with Maria Hill and S.H.I.E.L.D. agents. Lifeboats pull up to the city and take people aboard.\n"
         "Rhodey joins in as War Machine too."),
        ("教会の守り",
         "ヒーローたちは教会のかなめを囲み、押し寄せるロボット兵と戦う。\n"
         "ウルトロンの本体が現れると、ソー、トニー、ヴィジョンが光線を合わせて浴びせ、ハルクが殴り飛ばす。",
         "Holding the church",
         "The heroes surround the key in the church and fight off waves of robots.\n"
         "When Ultron's main body appears, Thor, Tony and Vision blast him together, and the Hulk punches him away."),
        ("ピエトロの最期",
         "クリントは、逃げ遅れた男の子を見つけて抱き上げる。そこへ、空からウルトロンが銃弾を浴びせる。\n"
         "その瞬間、ピエトロが走りこんで2人の前に立ち、盾になる。ピエトロはたくさんの弾を受けて死ぬ。\n"
         "ハルクは、ウルトロンの乗った飛行機に飛び乗り、ウルトロンを外へたたき出す。",
         "Pietro's last run",
         "Clint finds a little boy left behind and scoops him up. Ultron opens fire on them from the air.\n"
         "In that instant Pietro races in and stands in front of them as a shield. He is hit by many bullets and dies.\n"
         "The Hulk leaps onto Ultron's aircraft and throws Ultron out."),
        ("ワンダの怒り",
         "兄の死を感じたワンダは、悲しみと怒りで教会の守りを離れ、ロボット兵を一気になぎ払う。\n"
         "傷ついたウルトロンの本体を見つけると、力でその中心部をえぐり出して壊す。\n"
         "しかしワンダが持ち場を離れたすきに、ロボット兵の1体が装置を動かし、街が落ち始める。",
         "Wanda's fury",
         "Sensing her brother's death, Wanda leaves her post at the church in grief and rage and wipes out the robots around her.\n"
         "She finds Ultron's damaged main body and tears out his core with her powers.\n"
         "But while she is away, one of the drones activates the machine, and the city begins to fall."),
        ("街を砕く",
         "人々はみな救命ボートに乗った。トニーとソーは、装置に力を加えて爆発させ、街を空中で粉々に砕く。地上に大きな被害が出るのを防ぐためだ。\n"
         "崩れる街からワンダを、ヴィジョンが抱えて助け出す。",
         "Shattering the city",
         "Everyone is aboard the lifeboats. Tony and Thor overload the machine and blow the city apart in midair, keeping it from devastating the ground.\n"
         "Vision carries Wanda out of the collapsing city."),
    ]),
    ("第7部 戦いのあと", "Part 7: After the battle", [
        ("去っていくハルク",
         "ハルクはクインジェットに乗りこんだまま、戻ろうとしない。ナターシャが通信で呼びかけるが、ハルクは自分がそばにいるとナターシャを危険にさらすと考え、通信を切ってどこかへ飛び去る。",
         "The Hulk leaves",
         "The Hulk stays aboard a Quinjet and won't come back. Natasha calls to him over the radio, but he doesn't want to put her in danger by staying close. He cuts the call and flies off."),
        ("最後のウルトロン",
         "森の中で、最後に残ったウルトロンのロボットに、ヴィジョンが会いに行く。\n"
         "2人は人間や世界について静かに言葉を交わす。そのあと、ヴィジョンはウルトロンを消し去る。",
         "The last Ultron",
         "In a forest, Vision finds the last remaining Ultron drone.\n"
         "They talk quietly about humanity and the world. Then Vision destroys it."),
        ("それぞれの道",
         "クリントはチームを離れて農場に戻る。生まれた息子に、ローラと「ナサニエル・ピエトロ」と名付ける。\n"
         "アベンジャーズは、ニューヨーク州の新しい基地に移る。ソーは、インフィニティ・ストーンのことを調べるためアスガルドへ帰る。トニーもチームを離れる。",
         "Separate paths",
         "Clint retires and goes home to the farm. He and Laura name their newborn son Nathaniel Pietro.\n"
         "The Avengers move to a new base in upstate New York. Thor returns to Asgard to learn more about the Infinity Stones, and Tony steps away from the team too."),
        ("新しいアベンジャーズ",
         "残ったスティーブとナターシャは、新しいメンバーを鍛えることにする。ローディ（ウォーマシン）、ヴィジョン、サム（ファルコン）、ワンダの4人だ。",
         "The new Avengers",
         "Steve and Natasha stay to train a new lineup: Rhodey (War Machine), Vision, Sam (Falcon) and Wanda."),
        ("エンドクレジットの途中",
         "宇宙のどこか。サノスが、まだ石がひとつもはまっていない金色のこて（ガントレット）を手にはめる。\n"
         "サノスは「よかろう、私の出番だ」と言い、自分で石を集めに動き出す。",
         "Mid-credits",
         "Somewhere in space, Thanos slips on a golden gauntlet with no stones in it yet.\n"
         "\"Fine. I'll do it myself,\" he says, setting out to collect the stones himself."),
    ]),
    ("まとめ（結末までのネタバレ）", "Summary (spoilers through the ending)", [
        ("ウルトロンの計画と結末",
         "ウルトロンは、トニーとブルースが杖の宝石の人工知能を使って作ろうとした、世界を守る仕組みから生まれた（第2部）。目覚めてすぐ、世界を守るには人類を滅ぼすしかないと考えた。\n"
         "ヴィブラニウムで最強の体を作ろうとしたが、その体はアベンジャーズに奪われ、ヴィジョンになった（第3部〜第5部）。\n"
         "最後はソコヴィアの街を空から落として人類を滅ぼそうとしたが、街はトニーとソーに空中で砕かれ、本体はワンダに壊され、最後のロボットはヴィジョンに消された（第6部〜第7部）。",
         "Ultron's plan and how it ends",
         "Ultron came from the protection program Tony and Bruce tried to build with the AI in the scepter's gem (Part 2). The moment he woke up, he decided the only way to save the world was to wipe out humanity.\n"
         "He tried to build an ultimate body from vibranium, but the Avengers took it and it became Vision (Parts 3–5).\n"
         "In the end he tried to drop the city of Sokovia from the sky to wipe out humanity, but Tony and Thor shattered it in midair, Wanda destroyed his main body, and Vision finished off his last drone (Parts 6–7)."),
        ("双子が味方になるまで",
         "・トニーを憎む理由：子どものころ、スターク社の砲弾で両親を亡くし、爆発しなかった弾の前で何日も助けを待った（第3部）。\n"
         "・ウルトロンと組む：トニーへの憎しみから手を組み、ヨハネスブルグでワンダがヒーローたちに悪夢を見せた（第3部）。\n"
         "・離れる：ソウルでワンダがウルトロンの心をのぞき、人類を滅ぼす狙いを知って、2人は去った（第5部）。\n"
         "・アベンジャーズとして戦う：ソコヴィアで人々を守って戦い、ワンダはクリントの言葉で戦う決心をした（第6部）。最後にワンダは新しいアベンジャーズの1人になる（第7部）。",
         "How the twins changed sides",
         "- Why they hated Tony: as children, a Stark shell killed their parents, and they waited for days in front of one that didn't explode (Part 3).\n"
         "- Joining Ultron: their hatred of Tony brought them to him, and in Johannesburg Wanda gave the heroes nightmares (Part 3).\n"
         "- Leaving: in Seoul, Wanda read Ultron's mind, saw his plan to wipe out humanity, and they walked away (Part 5).\n"
         "- Fighting as Avengers: they fought to protect the people of Sokovia, and Clint's words gave Wanda the courage to fight (Part 6). In the end Wanda joins the new Avengers (Part 7)."),
        ("死んだ人たち（話の順に）",
         "・ストラッカー男爵（第3部）：つかまっていたところを、ウルトロンに殺される。\n"
         "・ピエトロ・マキシモフ（第6部）：ソコヴィアで、男の子を抱えたクリントにウルトロンが空から銃弾を浴びせたとき、走りこんで2人の盾になり、弾を受けて死ぬ。クリントは生まれた息子にピエトロの名を付ける。",
         "Who died (in order)",
         "- Baron Strucker (Part 3): killed by Ultron while in custody.\n"
         "- Pietro Maximoff (Part 6): in Sokovia, when Ultron opened fire from the air on Clint and the boy he was carrying, Pietro raced in, shielded them and was killed by the bullets. Clint later gives his newborn son Pietro's name."),
    ]),
]
