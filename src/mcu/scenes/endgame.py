# 『アベンジャーズ／エンドゲーム』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版ウィキペディアの映画のあらすじ（Plot）と、登場人物ごとの記事（Tony Stark / Steve Rogers / Natasha Romanoff /
# Nebula / Thanos など「(Marvel Cinematic Universe)」の記事）を照らし合わせて、順番と事実を確かめた。
# 資料どうしで食い違う所（スティーブが過去で暮らし始めた年、葬式までの日数など）は書いていない。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「章-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1章 23日後", "Part 1: Twenty-three days later", [
        ("クリントの家族が消える",
         "クリントは農場で、家族と過ごしている。娘のライラに弓矢を教え、妻のローラが昼ごはんに呼ぶ。\n"
         "クリントが目を離した一瞬のうちに、ライラの姿が消える。妻と息子たちも、ちりになって消えていた。サノスの指パッチンで、宇宙の命の半分が消えたのだ。",
         "Clint's family vanishes",
         "Clint is spending the day with his family at their farm. He teaches his daughter Lila archery, and his wife Laura calls them in for lunch.\n"
         "He looks away for a moment, and Lila is gone. His wife and sons have turned to dust too. Thanos's snap has wiped out half of all life in the universe."),
        ("宇宙をただようトニーとネビュラ",
         "惑星タイタンでの戦いのあと、トニーとネビュラは、壊れた宇宙船で宇宙をただよっていた。船の燃料の装置は戦いで壊れていて、2人で工夫して少しのあいだ飛んだものの、もう動かない。2人は紙を指ではじくゲームで時間をつぶす。\n"
         "食べ物も水もなくなり、トニーはヘルメットの録画でペッパーに別れのメッセージを残す。「酸素は明日の朝には尽きる」と話し、やせ細った体で眠りにつく。",
         "Tony and Nebula adrift",
         "After the battle on Titan, Tony and Nebula drift through space in a broken ship. Its fuel cells were damaged in the battle, and a fix bought them a little flight time, but now the ship is dead. They pass the time flicking a paper football.\n"
         "With no food or water left, Tony records a farewell message to Pepper on his helmet. He says the oxygen will run out by morning, then lies down, wasted and weak."),
        ("キャロルの救出",
         "光り輝くキャロル・ダンヴァースが現れ、宇宙船ごと地球のアベンジャーズの本部まで運ぶ。\n"
         "トニーはペッパーと抱き合って再会する。スティーブには「あの子（ピーター）を失った」と打ち明ける。",
         "Carol to the rescue",
         "A glowing Carol Danvers appears and carries the whole ship back to the Avengers Compound on Earth.\n"
         "Tony and Pepper embrace. To Steve, Tony admits that he lost the kid, Peter."),
        ("トニーの怒り",
         "本部で、残った仲間は状況を話し合う。トニーは「地球を守るスーツの仕組みが必要だと言ったのに、反対したのはお前だ」と、スティーブに怒りをぶつける。\n"
         "トニーは胸のアーク・リアクターを外してスティーブに押しつけ、その場に倒れてしまう。ブルースたちがトニーを休ませる。",
         "Tony's anger",
         "At the Compound, the survivors take stock. Tony lashes out at Steve: he said they needed armor around the world, and Steve was the one who opposed it.\n"
         "He pulls the arc reactor from his chest, shoves it at Steve, and collapses. Bruce and the others get him to rest."),
        ("サノスの居場所",
         "ネビュラは、サノスが仕事を終えたら「ガーデン」で休むと話していたことを思い出す。ロケットたちは、指パッチンと同じ大きな力が、2日前にある星で使われたのを見つける。\n"
         "石を取り戻せば、消えた人を元に戻せるかもしれない。けがをしたトニーを残し、スティーブ、ナターシャ、ブルース、ソー、ローディ、ロケット、ネビュラ、キャロルが、その星へ向かう。",
         "Where Thanos went",
         "Nebula remembers Thanos saying he would rest at \"the Garden\" when his work was done. Rocket and the others detect a burst of energy like the snap, used two days earlier on a planet.\n"
         "If they can get the stones back, maybe they can undo it. Leaving the injured Tony behind, Steve, Natasha, Bruce, Thor, Rhodey, Rocket, Nebula and Carol head there."),
        ("石のないサノス",
         "サノスは、誰もいない静かな星で、ひとり畑仕事をしていた。ヒーローたちは一斉におそいかかり、ソーがこてをはめたサノスの腕を切り落とす。\n"
         "しかし、こてには石が1つもなかった。サノスは「石を使って、石を壊した。私も死にかけた」と言う。ネビュラは「父はうそをつかない」と認める。",
         "Thanos without the stones",
         "Thanos is alone on a quiet, empty planet, farming. The heroes attack together, and Thor cuts off the arm wearing the gauntlet.\n"
         "But the gauntlet is empty. Thanos says he used the stones to destroy the stones, and it nearly killed him. Nebula confirms her father doesn't lie."),
        ("ソーの一撃",
         "もう元に戻す方法はない。怒りと後悔にかられたソーは、ストームブレイカーでサノスの首をはねる。\n"
         "前の作品の戦いで、ソーは胸をねらったために、サノスに指を鳴らされてしまった。今度は「首をねらった」とつぶやくが、何も取り戻せない。",
         "Thor's blow",
         "There's no way left to undo it. Driven by rage and regret, Thor cuts off Thanos's head with Stormbreaker.\n"
         "In the last film, Thor aimed for the chest and Thanos got to snap. This time he mutters that he went for the head, but nothing is won back."),
    ]),
    ("第2章 5年後", "Part 2: Five years later", [
        ("それぞれの5年",
         "5年がたつ。スティーブはニューヨークで、大切な人を失った人たちの集まりを開き、話を聞いている。\n"
         "ナターシャは本部に残り、画面ごしに仲間と連絡を取り続けている。宇宙のロケットとネビュラ、ワカンダのオコエ、キャロル、そしてローディ。ローディは、クリントが世界中で悪人の組織をおそい、殺して回っていると伝える。\n"
         "訪ねてきたスティーブに、ナターシャは「この仕事と仲間が、私のすべてだった」と涙を見せる。",
         "Five years on",
         "Five years pass. In New York, Steve runs a support group for people who lost loved ones.\n"
         "Natasha stays at the Compound, keeping in touch with allies by screen: Rocket and Nebula in space, Okoye in Wakanda, Carol, and Rhodey. Rhodey reports that Clint has been attacking criminal "
         "groups around the world and killing them.\n"
         "When Steve visits, Natasha tears up: this job and these people were everything she had."),
        ("スコットが戻ってくる",
         "ある倉庫で、ネズミがたまたま古いバンの機械を動かし、量子の世界に取り残されていたスコット・ラングが外に飛び出してくる。\n"
         "町には「消えた人々」の記念の壁があり、そこには自分の名前もあった。スコットは急いで家へ走り、すっかり大きくなった娘キャシーと抱き合う。",
         "Scott comes back",
         "In a storage unit, a rat happens to trigger the machinery in an old van, and Scott Lang, who had been stuck in the Quantum Realm, bursts out.\n"
         "A memorial wall for \"the vanished\" lists his own name. He rushes home and hugs his daughter Cassie, now much older."),
        ("時間旅行の思いつき",
         "スコットは本部を訪ね、スティーブとナターシャに話す。量子の世界にいたのは自分には5時間だったのに、外では5年がたっていた。\n"
         "量子の世界では時間の流れ方が違う。それなら、そこを通って過去へ行き、サノスが集める前の石を手に入れられるのではないか。",
         "The time travel idea",
         "Scott goes to the Compound and tells Steve and Natasha: for him, only five hours passed in the Quantum Realm, but five years passed outside.\n"
         "Time works differently there. So could they pass through it into the past and get the stones before Thanos collected them?"),
        ("湖の家のトニー",
         "3人は、湖のほとりの家に住むトニーを訪ねる。トニーはペッパーと結婚し、娘のモーガンが生まれていた。\n"
         "トニーは「やっと手に入れた家族を危険にさらせない」と断る。",
         "Tony at the lake house",
         "The three visit Tony at his house by a lake. He has married Pepper, and they have a daughter, Morgan.\n"
         "Tony turns them down: he can't put the family he finally has at risk."),
        ("ブルースと失敗した実験",
         "次に3人は、ブルースに会う。ブルースは18か月の研究で、ハルクの体とブルースの頭脳を1つにした姿になっていた。食堂では子どもたちと写真に写る人気者だ。\n"
         "本部でスコットのバンを使って試すが、うまくいかない。スコットは若者になり、老人になり、赤ちゃんになってしまう。",
         "Bruce, and a failed test",
         "Next, they see Bruce. After 18 months of research, he has merged the Hulk's body with his own mind, and at a diner he poses for photos with kids.\n"
         "At the Compound they try it with Scott's van, but it goes wrong: Scott turns into a teenager, an old man, and a baby."),
        ("トニーの発見",
         "その夜、トニーはピーターと一緒に写った写真を見つめる。そしてコンピューターで計算を重ね、量子の世界を安全に通る方法を見つけてしまう。\n"
         "ペッパーは「止めても、あなたは休めないでしょう」とトニーの気持ちを受け止める。トニーはモーガンを寝かしつけ、「3000回愛してる」と言われる。",
         "Tony's breakthrough",
         "That night, Tony stares at a photo of himself with Peter. Running calculation after calculation on his computer, he finds a safe way through the Quantum Realm.\n"
         "Pepper understands: even if she stopped him, he wouldn't be able to rest. Tony tucks Morgan in, and she tells him she loves him 3000."),
        ("盾を返す",
         "トニーは本部に来て、時間旅行の方法ができたと伝える。そして、昔の戦いのあとスティーブが置いていった盾を返す。\n"
         "トニーの条件は「失ったものを取り戻す。でも今あるものは失わない」こと。長いあいだ仲たがいしていた2人は、ここで仲直りする。",
         "Returning the shield",
         "Tony arrives at the Compound and says he has worked out time travel. He also hands back the shield Steve left behind after their old fight.\n"
         "His condition: bring back what they lost without losing what he has. After years apart, the two make peace."),
    ]),
    ("第3章 仲間を集める", "Part 3: Bringing the team back", [
        ("ニュー・アスガルドのソー",
         "ブルースとロケットは、ノルウェーにあるアスガルドの人々の町、ニュー・アスガルドへ行く。町を守るヴァルキリーは、ソーが家に閉じこもっていると話す。\n"
         "ソーはすっかり太り、コーグたちとテレビゲームをしながら酒を飲んで暮らしていた。サノスの名前を聞くと顔色を変える。ブルースたちは「船にビールがある」と誘い、ソーを連れ出す。",
         "Thor in New Asgard",
         "Bruce and Rocket go to New Asgard, the Asgardians' town in Norway. Valkyrie, who looks after it, says Thor keeps to himself.\n"
         "Thor has grown heavy and spends his days drinking and playing video games with Korg and others. He flinches at Thanos's name. Bruce and Rocket mention beer on the ship and bring him along."),
        ("東京のクリント",
         "ナターシャは東京へ向かう。雨の夜、クリントはヤクザの組長アキヒコとその手下を刀で斬り倒していた。家族を失ってから、悪人を殺して回っていたのだ。\n"
         "ナターシャは「希望が見つかった」と告げる。クリントは、仲間のもとへ戻ることにする。",
         "Clint in Tokyo",
         "Natasha goes to Tokyo. On a rainy night, Clint cuts down the yakuza boss Akihiko and his men with a sword. Since losing his family, he has been killing criminals.\n"
         "Natasha tells him they've found a chance. Clint agrees to come back."),
        ("クリントの試運転",
         "本部では、トニーとロケットが新しい量子トンネルを作り上げる。最初に入るのはクリントだ。\n"
         "クリントは少しのあいだだけ過去の自分の農場へ行き、娘ライラの声を聞く。戻ってきた手には、ライラの野球のグローブがあった。実験は成功だ。",
         "Clint's test run",
         "At the Compound, Tony and Rocket finish a new quantum tunnel. Clint goes first.\n"
         "For a few moments he's back at his farm in the past, and he hears Lila's voice. He returns holding her baseball glove. The test works."),
        ("6つの石はどこにあったか",
         "全員で、過去のいつ・どこに石があったかを話し合う。ブルースは、ニューヨークの戦いのとき、町に3つの石が集まっていたと気づく。ソーはジェーンの体に入ったリアリティ・ストーンのことを話す。\n"
         "ネビュラは、パワー・ストーンが惑星モラグにあったこと、そしてサノスがガモーラを連れてヴォーミアへ行き、1人で帰ってきたことを話す。",
         "Where the stones were",
         "Together they work out where each stone was, and when. Bruce realizes that three stones were in New York during the battle there. Thor talks about the Reality Stone inside Jane.\n"
         "Nebula explains the Power Stone was on the planet Morag, and that Thanos took Gamora to Vormir and came back alone."),
        ("3つのチーム",
         "過去へ行くのに必要なピム粒子は、1人1往復分しかない。チームは3つに分かれる。\n"
         "①2012年のニューヨーク：トニー、スティーブ、ブルース、スコット。②2013年のアスガルド：ソーとロケット。③2014年の宇宙：ナターシャ、クリント、ローディ、ネビュラ。ロケットは、小さく縮めた宇宙船をクリントに預ける。",
         "Three teams",
         "There are only enough Pym Particles for one round trip each. They split into three teams.\n"
         "1) New York, 2012: Tony, Steve, Bruce and Scott. 2) Asgard, 2013: Thor and Rocket. 3) Space, 2014: Natasha, Clint, Rhodey and Nebula. Rocket hands Clint a shrunken spaceship."),
        ("出発",
         "スティーブは「5年前に負けた。これが一度きりのチャンスだ。何があってもやりとげよう」と仲間に語りかける。\n"
         "全員が量子トンネルの上に立ち、それぞれの過去へ飛ぶ。",
         "Departure",
         "Steve tells the team: five years ago they lost, and this is their one chance. Whatever it takes.\n"
         "They all step onto the quantum tunnel and jump to their points in the past."),
    ]),
    ("第4章 2012年と1970年", "Part 4: 2012 and 1970", [
        ("2012年のニューヨーク",
         "着いたのは、1作目『アベンジャーズ』でロキの軍を倒した直後のニューヨーク。過去のアベンジャーズがロキをつかまえている。\n"
         "4人は分かれて動く。スティーブとトニーとスコットは、石を持ち出そうとする人たちのいるスターク・タワーへ。ブルースは、タイム・ストーンを守る魔術師の館へ向かう。",
         "New York, 2012",
         "They arrive in New York right after the first Avengers film's victory over Loki's army. The Avengers of the past have just captured Loki.\n"
         "The four split up. Steve, Tony and Scott go to Stark Tower, where the stones are being taken away. Bruce heads to the sorcerers' Sanctum, which guards the Time Stone."),
        ("エンシェント・ワンとの約束",
         "ブルースの前に、魔術師たちの長エンシェント・ワンが現れる。石を1つ持ち去れば、その時代は別の流れの世界に分かれ、危険にさらされると話し、断る。\n"
         "ブルースは「使い終わったら、すべての石を元の時代に返す」と約束する。この先の未来でストレンジが自分から石を渡したと聞いたエンシェント・ワンは、ブルースにタイム・ストーンを預ける。",
         "The Ancient One's promise",
         "The Ancient One, leader of the sorcerers, confronts Bruce. Taking a stone away would split her time into a separate branch and leave it in danger, she says, so she refuses.\n"
         "Bruce promises to return every stone to its own time when they're done. Learning that in the future Strange gave his stone away by choice, she entrusts Bruce with the Time Stone."),
        ("エレベーターの合言葉",
         "スティーブは、ロキの杖を運ぶ男たちとエレベーターに乗る。彼らが、ひそかに敵の組織ヒドラの一員だと知っているスティーブは、耳元で「ハイル・ヒドラ」とささやく。\n"
         "男たちはスティーブを仲間だと思いこみ、杖を渡してしまう。杖の中にはマインド・ストーンがある。",
         "The password in the elevator",
         "Steve rides an elevator with the men carrying Loki's scepter. Knowing they are secretly members of Hydra, he whispers \"Hail Hydra.\"\n"
         "Thinking he's one of them, they hand over the scepter, which holds the Mind Stone."),
        ("2人のキャプテン・アメリカ",
         "スティーブは、2012年の自分と鉢合わせする。過去のスティーブは、ロキが化けていると思いこみ、おそいかかってくる。\n"
         "互角の戦いの中、スティーブは「バッキーは生きている」と叫ぶ。過去の自分がおどろいて手をゆるめたすきに、杖で気を失わせる。",
         "Two Captain Americas",
         "Steve runs into his 2012 self, who thinks he's Loki in disguise and attacks.\n"
         "They're evenly matched until Steve shouts that Bucky is alive. His past self freezes in shock, and Steve knocks him out with the scepter."),
        ("テッセラクトを逃す",
         "スペース・ストーンの入ったテッセラクトのケースとロキの引き渡しをめぐって、組織の幹部ピアースと過去のトニー・ソーが言い争っている。小さくなったスコットは、過去のトニーの胸の装置にもぐりこみ、心臓の発作を起こさせる。そのすきにトニーがケースを奪う。\n"
         "ところが、階段から出てきた過去のハルクがぶつかり、ケースが落ちる。床をすべったテッセラクトを、つかまっていたロキが拾い、どこかへ消えてしまう。",
         "Losing the Tesseract",
         "The past Tony and Thor are arguing with the official Pierce over who takes Loki and the case holding the Tesseract, with the Space Stone inside. A shrunken Scott slips into the past Tony's chest device and "
         "triggers a heart attack, and in the confusion Tony grabs the case.\n"
         "But the past Hulk bursts out of a stairwell and knocks into him, and the case falls. The Tesseract slides across the floor, and the captive Loki picks it up and vanishes."),
        ("1970年へ",
         "スコットとブルースは2つの石を持って先に帰るが、トニーとスティーブには、もう一度やり直すためのピム粒子がない。トニーは、1970年にテッセラクトが軍の基地キャンプ・リーハイに保管されていたことを思い出す。\n"
         "そこには、ピム粒子を作ったハンク・ピムもいた。トニーとスティーブは、2人で1970年へ飛ぶ。",
         "To 1970",
         "Scott and Bruce head back with two stones, but Tony and Steve don't have the Pym Particles to try again. Tony remembers that in 1970 the Tesseract was kept at a military base, Camp Lehigh.\n"
         "Hank Pym, who created the particles, worked there too. Tony and Steve jump to 1970."),
        ("父ハワードとの会話",
         "トニーは基地の保管庫からテッセラクトを手に入れる。その帰り、若い父ハワードと出くわす。ハワードは、もうすぐ生まれる子どもを待っていた。その子が、トニー自身だ。\n"
         "トニーは名前を隠して話し、父親になることへの不安を聞く。別れぎわ、トニーは父を抱きしめる。基地の外の道では、スタン・リーが車から声をかける。",
         "Talking with Howard",
         "Tony takes the Tesseract from the base's vault. On his way out, he runs into his young father, Howard, who is waiting for his child to be born. That child is Tony himself.\n"
         "Hiding who he is, Tony listens to his father's worries about being a dad. Before they part, Tony hugs him. Out on the road, Stan Lee calls out from a passing car."),
        ("ピム粒子と、窓の向こうのペギー",
         "スティーブはハンク・ピムの研究室から、帰りに必要なピム粒子を手に入れる。\n"
         "人目をさけて入った部屋で、スティーブはガラス窓ごしに、昔愛したペギー・カーターの姿を見つめる。2人は手に入れたものを持って、現代へ帰る。",
         "Pym Particles, and Peggy through the window",
         "Steve takes the Pym Particles they need from Hank Pym's lab.\n"
         "Hiding in an office, he watches Peggy Carter, the woman he loved, through a glass window. Then he and Tony return to the present with what they came for."),
    ]),
    ("第5章 2013年と2014年", "Part 5: 2013 and 2014", [
        ("2013年のアスガルド",
         "ソーとロケットは、『マイティ・ソー／ダーク・ワールド』のころのアスガルドに着く。この日は、母フリッガが命を落とす日だった。\n"
         "ソーは、昔の恋人ジェーンの姿を見て取り乱す。ロケットは1人で動き、ジェーンの体に入っていたリアリティ・ストーンを、機械で吸い出して手に入れる。",
         "Asgard, 2013",
         "Thor and Rocket arrive in Asgard during the time of Thor: The Dark World. It is the day Thor's mother Frigga will die.\n"
         "Seeing his old love Jane, Thor falls apart. Rocket goes on alone and uses a device to draw the Reality Stone out of Jane's body."),
        ("母フリッガの言葉",
         "フリッガは、目の前のソーが未来から来たことに気づく。ソーは母の死を伝えて止めようとするが、フリッガは「あなたは自分の未来を正しに来たのでしょう」と聞こうとしない。\n"
         "そして「誰でも、なるべき自分になれずに失敗する。大切なのは、ありのままの自分でいられるかどうか」と語りかける。",
         "Frigga's words",
         "Frigga realizes this Thor has come from the future. He tries to warn her of her death, but she won't hear it: he's here to fix his own future, not hers.\n"
         "She tells him that everyone fails at who they're supposed to be. What matters is how well you succeed at being who you are."),
        ("ムジョルニアが戻る",
         "立ち去る前に、ソーが手をのばすと、この時代のハンマー・ムジョルニアが飛んできて手におさまる。\n"
         "「自分はまだふさわしい！」。元気を取り戻したソーは、ムジョルニアを持ち、ロケットと一緒に現代へ帰る。",
         "Mjolnir returns",
         "Before leaving, Thor holds out his hand, and this time's Mjolnir flies into it.\n"
         "\"I'm still worthy!\" His spirit restored, Thor returns to the present with Rocket, Mjolnir in hand."),
        ("2014年のモラグ",
         "ナターシャとクリントは宇宙船でヴォーミアへ向かい、ローディとネビュラは惑星モラグに残る。\n"
         "そこへ、のちのガーディアンズのリーダー、ピーター・クイルが音楽に合わせて踊りながら現れる。ローディが殴って気を失わせ、2人は遺跡からパワー・ストーンの入ったオーブを手に入れる。",
         "Morag, 2014",
         "Natasha and Clint fly to Vormir, while Rhodey and Nebula stay on the planet Morag.\n"
         "Peter Quill, the future Guardians leader, arrives dancing to his music. Rhodey knocks him out, and the two take the orb holding the Power Stone from the ruins."),
        ("2人のネビュラ",
         "同じころ、サノスの船にはこの時代のネビュラとガモーラがいた。こちらのネビュラの体の機械が、未来のネビュラの機械とつながってしまい、未来のネビュラの記憶が流れこむ。\n"
         "サノスはその記憶を映し出させ、未来の自分が勝ったこと、そしてアベンジャーズがそれを元に戻そうとしていることを知る。",
         "Two Nebulas",
         "Meanwhile, the Nebula of this time is aboard Thanos's ship with Gamora. Her cybernetics link with those of the Nebula from the future, and the future Nebula's memories flow in.\n"
         "Thanos has the memories projected and learns that his future self won, and that the Avengers are trying to undo it."),
        ("つかまったネビュラ",
         "モラグでは、未来のネビュラが体の機械の不調で倒れ、帰れなくなる。ローディだけが先に現代へ帰る。\n"
         "サノスの手下がネビュラをとらえる。サノスはこの時代のネビュラを、未来のネビュラになりすまさせて現代へ送りこみ、自分たちが来る準備をさせる。",
         "Nebula captured",
         "On Morag, the future Nebula collapses as her systems fail and can't go home. Rhodey returns to the present without her.\n"
         "Thanos's forces capture her. Thanos sends this time's Nebula to the present in her place, disguised as her future self, to prepare for his arrival."),
    ]),
    ("第6章 ヴォーミアの崖と、もう一度の指パッチン", "Part 6: Vormir, and another snap", [
        ("ソウル・ストーンの番人",
         "ナターシャとクリントは、ヴォーミアの山の頂上に着く。待っていたのは、石の番人になったレッド・スカルだった。\n"
         "番人は「石を手に入れるには、愛する者の命を差し出さなければならない」と告げる。2人は、サノスがここでガモーラを殺したことを知る。",
         "The Soul Stone's keeper",
         "Natasha and Clint reach the top of the mountain on Vormir. Waiting for them is Red Skull, now the stone's keeper.\n"
         "He tells them the stone demands the life of someone you love. They realize this is where Thanos killed Gamora."),
        ("どちらが落ちるか",
         "2人とも、相手を生かすため自分が犠牲になろうとする。クリントは、この5年で多くの人を殺した自分こそ犠牲になるべきだと考え、ナターシャは、クリントこそ家族のもとへ帰るべきだと考える。\n"
         "2人は崖のふちで取っ組み合い、先に飛び降りようと争う。",
         "Who will fall",
         "Each wants to be the one to die so the other can live. Clint feels that after all the killing of the past five years, it should be him. Natasha believes Clint must go home to his family.\n"
         "They struggle at the cliff's edge, each racing to jump first."),
        ("ナターシャの最期",
         "崖から落ちるナターシャの手を、クリントがつかむ。ナターシャは「放して。これでいいの」と言い、自分から手を放して落ちていく。\n"
         "クリントが気づくと、水の中に倒れていて、手にはソウル・ストーンがあった。",
         "Natasha's end",
         "As Natasha goes over the edge, Clint catches her hand. She tells him to let her go, that it's okay, and lets go herself.\n"
         "Clint wakes lying in water, with the Soul Stone in his hand."),
        ("帰ってきた仲間と悲しみ",
         "全員が、6つの石を持って現代の本部に戻る。ネビュラの中身が入れ替わっていることには、誰も気づかない。ナターシャの姿だけがない。\n"
         "湖のほとりで、ソーは「石の力で取り戻せる」と言うが、クリントは「取り戻せない」と答える。ブルースは怒りのあまりベンチを投げ飛ばす。",
         "Return, and grief",
         "Everyone returns to the Compound with all six stones. No one notices that Nebula has been swapped. Only Natasha is missing.\n"
         "By the lake, Thor insists the stones can bring her back, but Clint says they can't. In fury, Bruce hurls a bench."),
        ("新しいこて",
         "トニー、ブルース、ロケットは、6つの石をはめる新しいこてを作る。指を鳴らせば、体が耐えられないほどの力がかかる。\n"
         "ソーは自分がやると言い張るが、ガンマ線に強いブルースが引き受ける。消えた人を元に戻し、ほかは何も変えないと決める。",
         "A new gauntlet",
         "Tony, Bruce and Rocket build a new gauntlet to hold the six stones. Snapping with it will unleash more power than a body can bear.\n"
         "Thor insists on doing it, but Bruce, who can best withstand gamma radiation, takes it on. He will bring back everyone who vanished and change nothing else."),
        ("ブルースが指を鳴らす",
         "トニーが仲間の守りを固める中、ブルースがこてをはめる。石の力が腕を焼き、ブルースは苦しみながら指を鳴らす。腕は大やけどを負う。\n"
         "外では鳥が鳴き始め、クリントの電話が鳴る。消えたはずの妻ローラからだ。消えた人々が戻ってきた。",
         "Bruce snaps",
         "As Tony shields the team, Bruce puts on the gauntlet. The stones' power burns his arm, and in agony he snaps. His arm is badly burned.\n"
         "Outside, birds start singing, and Clint's phone rings. It's his wife Laura. Those who vanished are back."),
        ("本部の崩壊",
         "その直後、なりすましていたこの時代のネビュラが量子トンネルを動かし、2014年のサノスを、大きな船ごと現代へ呼び寄せる。\n"
         "船からミサイルが降りそそぎ、アベンジャーズの本部は崩れ落ちる。ローディ、ロケット、ブルースは、水のたまった地下でがれきの下じきになる。",
         "The Compound falls",
         "Moments later, the impostor Nebula activates the quantum tunnel and brings the 2014 Thanos, with his huge warship, into the present.\n"
         "Missiles rain down, and the Avengers Compound collapses. Rhodey, Rocket and Bruce are pinned under rubble in a flooding underground level."),
    ]),
    ("第7章 最後の戦い", "Part 7: The final battle", [
        ("がれきの下の救出",
         "地下では、ブルースが崩れかけた天井を支え、ローディとロケットが水に沈みかける。スコットが巨大な姿になって、3人を引っぱり出す。\n"
         "クリントは石の入ったこてを持って地下の通路を逃げ回り、サノスの怪物たちから守る。",
         "Rescue under the rubble",
         "Underground, Bruce holds up the collapsing ceiling as Rhodey and Rocket nearly drown. Scott grows giant and pulls them out.\n"
         "Clint runs through the tunnels with the stone-filled gauntlet, protecting it from Thanos's beasts."),
        ("ネビュラとネビュラ",
         "現代のネビュラは、サノスの船でこの時代のガモーラを説得し、仲間にする。2人は地下で、クリントからこてを奪ったこの時代のネビュラを見つける。\n"
         "現代のネビュラは「父から離れられる」と過去の自分に呼びかけるが、聞き入れない。過去のネビュラがガモーラに銃を向けたため、現代のネビュラが過去の自分を撃ち殺す。",
         "Nebula and Nebula",
         "Aboard Thanos's ship, the present-day Nebula convinces this time's Gamora to join her. Underground, they find the past Nebula, who has taken the gauntlet from Clint.\n"
         "The present Nebula tells her past self she can break free of their father, but she won't listen. When the past Nebula aims a gun at Gamora, the present Nebula shoots her past self dead."),
        ("3人とサノス",
         "がれきの上で、トニー、スティーブ、ソーの3人がサノスと向き合う。サノスは「この宇宙を原子まで壊し、私に感謝する新しい宇宙を作る」と言う。\n"
         "3人は戦うが、サノスは強い。追いつめられたソーのもとから、ムジョルニアが飛んでいき、スティーブの手におさまる。「やっぱりな！」とソーは喜ぶ。",
         "Three against Thanos",
         "On the rubble, Tony, Steve and Thor face Thanos. He says he will tear this universe down to its last atom and build a new one that will be grateful.\n"
         "They fight, but Thanos is stronger. With Thor pinned, Mjolnir flies past him into Steve's hand. Thor is thrilled: he knew it."),
        ("割られた盾",
         "スティーブはムジョルニアと盾で善戦するが、サノスは大きな剣で盾をたたき割る。トニーとソーも倒れる。\n"
         "サノスは船から大軍を呼び寄せる。傷だらけのスティーブは、割れた盾をもう一度腕にしめ、たった1人で大軍の前に立つ。",
         "The shattered shield",
         "Steve fights well with Mjolnir and his shield, but Thanos splits the shield with his huge blade. Tony and Thor are down too.\n"
         "Thanos calls down his army from the ship. Battered, Steve straps on the broken shield and stands alone before the army."),
        ("「左から失礼」",
         "スティーブの無線に「キャップ、聞こえるか？ 左から失礼」とサムの声が届く。後ろに光の輪が開き、ティ・チャラ、シュリ、オコエとワカンダの軍が現れる。\n"
         "ストレンジやウォンたち魔術師が、次々に光の輪を開く。指パッチンから戻ったヒーローたち、ガーディアンズ、ラヴェジャーズ、アスガルドの戦士、そしてペッパーもトニーのスーツで現れる。",
         "\"On your left\"",
         "Sam's voice comes over Steve's radio: \"Cap, can you hear me? On your left.\" A glowing portal opens behind him, and T'Challa, Shuri, Okoye and the armies of Wakanda step through.\n"
         "Strange, Wong and the other sorcerers open portal after portal. The heroes who came back from the snap, the Guardians, the Ravagers, Asgard's warriors, and Pepper in a suit of armor from Tony all arrive."),
        ("アベンジャーズ、アッセンブル",
         "全員がそろったところで、スティーブはムジョルニアを手に「アベンジャーズ……アッセンブル」と声をかける。最後の大きな戦いが始まる。\n"
         "石を過去に返せばサノスは手を出せない。こてをスコットのバン（量子トンネル）まで運ぼうと、クリントからティ・チャラ、ピーターへと、ヒーローたちが手から手へつないでいく。",
         "Avengers, assemble",
         "With everyone gathered, Steve raises Mjolnir and calls out: \"Avengers... assemble.\" The final battle begins.\n"
         "If the stones go back to the past, Thanos can't touch them. The heroes pass the gauntlet from hand to hand, from Clint to T'Challa to Peter, trying to get it to Scott's van with its quantum tunnel."),
        ("ワンダとキャロル",
         "ワンダはサノスに向かっていき、その力でサノスを追いつめる。サノスは、自分の兵も巻きこんで船からミサイルを撃たせる。\n"
         "そこへキャロルが飛んできて、サノスの船をつらぬいて壊す。しかし戦いの中でバンも壊されてしまう。こてを持つキャロルにサノスがつかみかかり、こてからパワー・ストーンを外して、その力でキャロルを吹き飛ばす。",
         "Wanda and Carol",
         "Wanda goes after Thanos, and her power nearly overwhelms him. Thanos orders his ship to fire on the battlefield, his own troops included.\n"
         "Then Carol flies in and smashes straight through the warship. But the van is destroyed in the fighting. Thanos grabs Carol as she holds the gauntlet, pries out the Power Stone, and blasts her away with it."),
        ("ストレンジの合図",
         "トニーはストレンジを見る。ストレンジは、1本の指を立てて見せる。前の作品で見た1400万605通りの未来のうち、勝てるのはたった1つ。今がその1つなのだ。\n"
         "トニーはサノスに組みつき、こてを奪おうとするが、投げ飛ばされる。",
         "Strange's signal",
         "Tony looks at Strange, who holds up one finger: of the 14,000,605 futures he saw in the last film, there's only one where they win, and this is it.\n"
         "Tony grapples with Thanos for the gauntlet but is thrown aside."),
        ("「私はアイアンマンだ」",
         "サノスは「私は絶対なのだ」と言って指を鳴らすが、何も起きない。こてから石がなくなっていた。\n"
         "6つの石は、組みついたときにトニーが自分のスーツの手に移していたのだ。トニーは「そして、私は……アイアンマンだ」と言って指を鳴らす。サノスの軍がちりになって消え、最後にサノスも静かに座りこんで消えていく。",
         "\"I am Iron Man\"",
         "Thanos says \"I am inevitable\" and snaps, but nothing happens. The stones are gone from the gauntlet.\n"
         "While grappling, Tony moved all six stones onto his own suit's hand. \"And I... am... Iron Man,\" he says, and snaps. Thanos's army turns to dust, and finally Thanos sits down quietly and fades away too."),
    ]),
    ("第8章 それぞれの道", "Part 8: New paths", [
        ("トニーの最期",
         "石の力で、トニーの体の右側は焼けただれていた。がれきにもたれるトニーに、ローディ、ピーター、ペッパーが寄りそう。ピーターは「勝ったんです」と泣く。\n"
         "ペッパーは「私たちは大丈夫。もう休んでいいのよ」と声をかける。トニーは静かに息を引き取る。",
         "Tony's end",
         "The stones' power has burned the right side of Tony's body. As he slumps against the rubble, Rhodey, Peter and Pepper come to his side. Peter cries that they won.\n"
         "Pepper tells him they'll be okay and he can rest now. Tony quietly dies."),
        ("残されたメッセージ",
         "トニーは、作戦の前にメッセージを録画していた。ペッパーと仲間たちがそれを見る。\n"
         "トニーは、うまくいかなかったときのことも考えていたと話し、「旅には終わりもある」と語る。最後に、娘のモーガンに「3000回愛してる」と伝える。",
         "The message he left",
         "Before the heist, Tony recorded a message. Pepper and the others watch it.\n"
         "He says he had planned for things not working out, and that part of the journey is the end. Finally, he tells Morgan he loves her 3000."),
        ("トニーの葬式",
         "湖のほとりの家で、トニーの葬式が開かれる。戻ってきた人たちを含め、多くのヒーローや仲間が集まる。\n"
         "ペッパーは、トニーが1作目『アイアンマン』で作ったアーク・リアクターを花で囲み、湖に浮かべる。\n"
         "このころ、ピーターは学校に戻り、親友のネッドと再会して抱き合う。",
         "Tony's funeral",
         "Tony's funeral is held at the lake house. Heroes and friends gather, including those who came back.\n"
         "Pepper sets the arc reactor from the first Iron Man, ringed with flowers, afloat on the lake.\n"
         "Around this time, Peter goes back to school and hugs his best friend Ned when they meet again."),
        ("ソーの旅立ち",
         "ソーはニュー・アスガルドで、ヴァルキリーに新しい王になってほしいと頼む。\n"
         "そして、ガーディアンズと一緒に宇宙へ旅立つ。ピーター・クイルは、どこかへ消えた、この時代のガモーラを探している。",
         "Thor sets out",
         "In New Asgard, Thor asks Valkyrie to be the new ruler.\n"
         "Then he leaves for space with the Guardians. Peter Quill is searching for the 2014 Gamora, who has gone off somewhere."),
        ("石を返しに",
         "スティーブは、借りてきた6つの石とムジョルニアを、それぞれの時代に返しに行く。ブルースが機械を動かし、サムとバッキーが見送る。\n"
         "予定では5秒で戻るはずが、スティーブは戻らない。",
         "Returning the stones",
         "Steve sets off to return the six stones and Mjolnir to their own times. Bruce runs the machine, and Sam and Bucky see him off.\n"
         "He's supposed to be back in five seconds, but he doesn't return."),
        ("ベンチの老人と盾",
         "バッキーが、近くのベンチに座る老人に気づく。年をとったスティーブだった。石を返したあと、過去に残って人生を送ってきたのだ。\n"
         "スティーブはサムを呼び、盾を手渡す。サムは「ほかの人の物のように感じる」と言うが、スティーブは「だから君のものなんだ」と答える。サムに過去での暮らしを聞かれても、スティーブは話さない。",
         "The old man on the bench, and the shield",
         "Bucky notices an old man on a nearby bench. It's Steve, grown old. After returning the stones, he stayed in the past and lived his life.\n"
         "Steve calls Sam over and hands him the shield. Sam says it feels like it belongs to someone else, and Steve says that's why it's his. When Sam asks about his life in the past, Steve won't say."),
        ("約束のダンス",
         "最後に、過去の家の中で、若いスティーブとペギーが2人で踊る姿が映る。『キャプテン・アメリカ／ザ・ファースト・アベンジャー』で約束していたダンスだ。",
         "The promised dance",
         "In the final scene, inside a home in the past, a young Steve and Peggy dance together, the dance he promised her in Captain America: The First Avenger."),
        ("エンドクレジットのあと",
         "エンドクレジットの最後に映像はない。1作目『アイアンマン』でトニーが洞くつでスーツを作ったときの、金づちで鉄をたたく音だけが聞こえる。",
         "After the credits",
         "There's no scene at the end of the credits, only the clang of hammering from when Tony built his first suit in a cave in Iron Man."),
    ]),
    ("まとめ（最後までのネタバレ）", "Summary (spoilers through the end)", [
        ("6つの石を、誰が・どこで手に入れたか",
         "・タイム・ストーン：ブルースが2012年のニューヨークで、エンシェント・ワンに「必ず返す」と約束して預かった（第4章）。\n"
         "・マインド・ストーン：スティーブが2012年のスターク・タワーで、ヒドラの男たちから杖ごと受け取った（第4章）。\n"
         "・スペース・ストーン：2012年は失敗し、ロキがテッセラクトを持って消えた。トニーが1970年のキャンプ・リーハイで手に入れた（第4章）。\n"
         "・リアリティ・ストーン：ロケットが2013年のアスガルドで、ジェーンの体から吸い出した（第5章）。\n"
         "・パワー・ストーン：ローディとネビュラが2014年のモラグで、クイルより先に手に入れた（第5章）。\n"
         "・ソウル・ストーン：2014年のヴォーミアで、ナターシャが命を差し出し、クリントが手に入れた（第6章）。\n"
         "使い終わった石は、最後にスティーブがすべて元の時代に返した（第8章）。",
         "The six stones: who got them, and where",
         "- Time Stone: Bruce, in New York in 2012, from the Ancient One after promising to return it (Part 4).\n"
         "- Mind Stone: Steve, at Stark Tower in 2012, handed the scepter by Hydra agents (Part 4).\n"
         "- Space Stone: the 2012 attempt failed and Loki vanished with the Tesseract. Tony got it at Camp Lehigh in 1970 (Part 4).\n"
         "- Reality Stone: Rocket, in Asgard in 2013, drawing it out of Jane (Part 5).\n"
         "- Power Stone: Rhodey and Nebula, on Morag in 2014, ahead of Quill (Part 5).\n"
         "- Soul Stone: on Vormir in 2014, Natasha gave her life and Clint got the stone (Part 6).\n"
         "In the end, Steve returned every stone to its own time (Part 8)."),
        ("死んだ人たち（話の順に）",
         "・2018年のサノス（第1章）：石をすでに壊していて元に戻す方法がないと分かり、怒ったソーがストームブレイカーで首をはねる。\n"
         "・アキヒコとヤクザの手下たち（第3章）：家族を失って悪人を殺して回っていたクリントが、東京で刀で斬る。\n"
         "・ナターシャ（第6章）：ソウル・ストーンには愛する者の命が必要なため、クリントを生かして石を手に入れさせようと、ヴォーミアの崖から自分で手を放して落ちる。\n"
         "・2014年のネビュラ（第7章）：ガモーラに銃を向けたため、現代のネビュラが撃つ。\n"
         "・2014年のサノスと、その軍（第7章）：トニーが自分のスーツに移した6つの石で指を鳴らし、ちりにして消す。\n"
         "・トニー（第8章）：6つの石の力で指を鳴らしたため、体が焼けて亡くなる。\n"
         "※最初に消えたクリントの家族など、指パッチンで消えた人々は、ブルースが指を鳴らして元に戻す（第6章）。",
         "Who died (in order)",
         "- The 2018 Thanos (Part 1): once it's clear he destroyed the stones and nothing can be undone, an enraged Thor cuts off his head with Stormbreaker.\n"
         "- Akihiko and his yakuza men (Part 3): Clint, killing criminals since losing his family, cuts them down with a sword in Tokyo.\n"
         "- Natasha (Part 6): the Soul Stone demands the life of a loved one, so to let Clint live and get the stone, she lets go and falls from the cliff on Vormir.\n"
         "- The 2014 Nebula (Part 7): the present-day Nebula shoots her when she aims a gun at Gamora.\n"
         "- The 2014 Thanos and his army (Part 7): Tony snaps with the six stones he moved onto his suit, turning them to dust.\n"
         "- Tony (Part 8): the power of snapping with all six stones burns his body, and he dies.\n"
         "Note: those erased by the snap, including Clint's family at the start, are brought back when Bruce snaps (Part 6)."),
    ]),
]
