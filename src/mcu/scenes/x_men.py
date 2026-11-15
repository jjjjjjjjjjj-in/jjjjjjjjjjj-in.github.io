# 『X-メン』（2000年）シーンごとの詳しいあらすじ
# 2026-11-10 書き直し。英語版ウィキペディアのあらすじ（今の版と、2008・2010・2012・2015・2018年の版）、日本語版ウィキペディアのストーリー、検索結果と照らし合わせて、順番と事実を確かめた。
# 2026-11-15 運営者の指摘（観ながら読むと合わない）で、映画で流れる順番に並べ直し、抜けていた場面を足した。
# 順番と事実は、X-MEN映画のファン事典（xmenmovies.fandom.com）の作品ページと、人物ごとのページ
# （ウルヴァリン、ローグ、プロフェッサーX、ストーム、サイクロップス、ジーン、ミスティーク、セイバートゥース、トード。
# それぞれ映画の流れを最初から順に書いている）、DVDのチャプターの並び（dvd.fandom.com の一覧を検索で確認。
# 9 ケリーの新しい補佐官→10 ブラザーフッド→11 ローグの力→12→13 家出→14 襲撃→15 マグニートーの計画→16 ミュータントの死→
# 17 倒れたリーダー→18 船→19 作戦→20〜24 像の戦い）、英語版・日本語版ウィキペディアで確かめた。
# imsdb.com の台本は完成した映画とちがう古い稿（山小屋やショッピングモールの場面がある）だったので、ほとんど使っていない。
# 直した所：セイバートゥースが隠れ家に戻る場面（2-6）、ジーンの検査とスコットの場面（3-5・3-6）、駅での戦い、
# ケリーが学園に来てから死ぬまでの流れ、船の上のマグニートーとローグ（5-6）、像の中の戦いの順番
# （にせのローガン→トード→ストームに化けたミスティーク→つかまる→力を移す→セイバートゥース）。
# 以前は「ミスティークがローガンに化けてサイクロップスを襲う」「駅の外で戦う」「つかまった場面でローグの髪が白くなる」と
# 書いていたが、資料とちがっていたので直した。
# 2つ以上の資料で確かめきれず、チャプターの並びから置いた所：ジーンの検査とローガンの部屋の場面（3-5・3-6）が
# ケリーがさらわれる場面（3-4）と機械の場面（3-7）の間に入ること、ケリーの脱出と浜辺（4-3）が悪夢（4-1）の後に来ること。
# 資料どうしで食い違う所（収容所での少年の年齢、トードやセイバートゥースがその後どうなったか、ブラザーフッドの島の名前、
# 最後にプロフェッサーXがいつ目を覚ましたか、ミスティークが像からどう逃げたか）は書いていない。
# 日本語版のセリフは、日本語の吹替・字幕の言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 英語版の短いセリフは英語のファン事典から。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 2つの始まり", "Part 1: Two beginnings", [
        ("収容所の門",
         "映画は、進化と突然変異についてのプロフェッサーXの語りから始まる。\n"
         "1944年、ドイツに占領されたポーランド。雨の中、少年エリックは、強制収容所に入れられるときに両親と引き離される。\n"
         "両親のほうへ行こうとして兵士たちに押さえつけられると、両親が連れて行かれた鉄の門が、少年のほうへ引き寄せられるように曲がっていく。少年には、磁力で金属を動かす力があった。少年は兵士に殴られて気を失う。",
         "The camp gates",
         "The film opens with Professor X's narration about evolution and mutation.\n"
         "1944, German-occupied Poland. In the rain, a boy named Erik is separated from his parents as he enters a concentration camp.\n"
         "When soldiers hold him back, the iron gates his parents were taken behind begin to bend toward him, as if pulled by a magnet. The boy can move metal with magnetism. A soldier knocks him unconscious."),
        ("マリーのキス",
         "時は流れて、近い未来。ミシシッピ州メリディアンに住む17歳の少女マリーは、自分の部屋でボーイフレンドのデヴィッドに、高校を出たら遠くへ旅をしたいと話している。2人は顔を近づけて、キスをする。\n"
         "そのとたん、デヴィッドは体をふるわせて倒れ、意識が戻らなくなる。マリーの悲鳴を聞いて両親がかけつけるが、マリーは自分に触らないでと叫ぶ。マリーには、触れた人の命の力や、ミュータントの力を吸い取ってしまう力があった。",
         "Marie's kiss",
         "Years later, in the near future. In Meridian, Mississippi, 17-year-old Marie is in her room, telling her boyfriend David about the trip she wants to take after high school. They lean in and kiss.\n"
         "David starts to shake, collapses and falls into a coma. Her parents rush in at her scream, but Marie cries out for them not to touch her. Her touch drains the life force, and the powers, of anyone she touches."),
        ("議会の公聴会",
         "アメリカの議会では、ミュータントに名前と力を届け出させる「ミュータント登録法案」について、公聴会が開かれている。\n"
         "証言に立ったジーン・グレイ博士は、名前を明かさせればミュータントが敵意や暴力にさらされると訴える。しかし、法案を進めるケリー上院議員は話をさえぎり、ミュータントは危険ではないのかと問いつめる。議員は、壁を通り抜けられる少女が銀行の金庫や他人の家に入るのをどう止めるのか、人の心をあやつるミュータントもいるらしい、と話し、会場から大きな拍手を受ける。",
         "The Senate hearing",
         "In Congress, a hearing is being held on the Mutant Registration Act, a bill that would force mutants to reveal their identities and powers.\n"
         "Testifying, Dr. Jean Grey warns that exposing mutants would leave them open to hostility and violence. But Senator Robert Kelly, the bill's champion, cuts her off and demands to know whether mutants are dangerous. What is to stop a girl who can walk through walls from entering a bank vault or someone's home, he asks, and there are rumors of mutants who can control minds. The room applauds him."),
        ("2人の旧友",
         "会場で聞いていたプロフェッサーX（チャールズ・エグゼビア）は、席を立って出て行く男に気づき、車いすで廊下まで追いかける。男は、あの収容所の少年エリック。今は「マグニートー」と名乗っている。2人は昔からの友人だった。\n"
         "プロフェッサーXは、人間を見限らないでほしいと頼む。しかしマグニートーは、その話は前にも聞いたと言って取り合わない。そして、邪魔だけはしないでくれ、未来は人間ではなく自分たちミュータントのものだ、と言い残して去っていく。",
         "Two old friends",
         "Listening in the audience, Professor Charles Xavier notices a man getting up to leave and follows him into the hall in his wheelchair. The man is Erik, the boy from the camp, who now calls himself Magneto. The two are old friends.\n"
         "Xavier asks him not to give up on humans, but Magneto says he has heard these arguments before. He asks only that Xavier stay out of his way, and walks off: \"We are the future, Charles, not them.\""),
    ]),
    ("第2部 カナダでの出会い", "Part 2: A meeting in Canada", [
        ("酒場のケージファイト",
         "家を出たマリーは、トラックに乗せてもらいながら、雪の深いカナダのアルバータ州北部、ラフリン・シティという町にたどり着く。酒場では、おりの中で殴り合う試合が行われていた。\n"
         "勝ち続けているのは、ウルヴァリンと呼ばれる男だった。新しい相手に押されても、すぐに立ち直ってあっという間に倒してしまう。マリーは、その男を見つめる。",
         "The cage fight",
         "Having run away from home, Marie hitches rides until she reaches Laughlin City, a snowbound town in northern Alberta, Canada. In a bar, men are fighting inside a cage.\n"
         "The man who keeps winning is called the Wolverine. Even when a new challenger gets the better of him, he recovers and flattens the man in seconds. Marie watches him."),
        ("ナイフと爪",
         "試合のあと、男はカウンターでマリーの近くに座る。店のテレビは、近くニューヨークで開かれる世界の首脳会議と、そこでミュータントの問題も話し合われることを伝えている。\n"
         "そこへ、さっき負けた相手が金を返せと言ってくる。あれだけ殴られて傷一つないのはおかしい、というのだ。男が取り合わないと、相手はナイフを抜いて後ろから襲いかかる。マリーが叫んで知らせ、男は振り向きざまに、手の甲から3本の金属の爪を出して相手ののどに突きつける。\n"
         "店の主人が銃を向けると、男は爪で銃を切り落とし、店を出て行く。",
         "A knife and claws",
         "After the fights, the man sits down near Marie at the bar. The TV reports on the coming summit of world leaders in New York, where the mutant question will also be discussed.\n"
         "The beaten fighter comes over and demands his money back: no man takes a beating like that without a mark. Brushed off, he pulls a knife and attacks from behind. Marie shouts a warning, and the man spins around with three metal claws out of his knuckles, right at the fighter's throat.\n"
         "When the barman levels a shotgun at him, he slices it apart with his claws and walks out."),
        ("トレーラーの中のローグ",
         "マリーは、男が自分と同じミュータントだと知り、男の車が引くトレーラーにこっそり乗りこむ。走り出してから気づいた男は、いったんマリーを雪道に降ろして走り去ろうとするが、少し進んだところで車を止め、乗せてやる。\n"
         "車の中で、マリーは「ローグ」と名乗る。男が手を温めてやろうとすると、ローグは手を引っこめ、自分の肌に触れた人はけがをすると話す。爪が出るときは痛いのかとローグが聞くと、男は毎回痛いと答える。男の名はローガン。ローグも、本当の名前はマリーだと教える。",
         "Rogue in the trailer",
         "Realizing the man is a mutant like her, Marie stows away in the trailer behind his truck. He finds her once they are on the road, puts her out in the snow and starts to drive off, but stops a little way on and lets her in.\n"
         "In the cab she introduces herself as Rogue. When he reaches to warm her hands she pulls them away, explaining that people who touch her skin get hurt. She asks whether it hurts when the claws come out. \"Every time,\" he says. His name is Logan, and she tells him her real name is Marie."),
        ("雪道の襲撃",
         "シートベルトをしたほうがいいとローグが言った直後、車は道をふさいだ木にぶつかる。ローガンはフロントガラスを破って雪の上に投げ出される。その傷は、ローグの目の前でみるみるふさがっていく。\n"
         "ローグは車の中にはさまれて動けず、車は燃え始める。助けに戻ろうとしたローガンは、敵のにおいに気づく。森から大男のミュータント、セイバートゥースが飛び出し、ローガンを投げ飛ばして気を失わせる。",
         "Ambush in the snow",
         "Just after Rogue tells him he should wear his seat belt, the truck slams into a tree lying across the road. Logan is thrown through the windshield into the snow. His wounds close before Rogue's eyes.\n"
         "Rogue is pinned inside, and the truck begins to burn. Heading back to help her, Logan catches an enemy's scent. The giant mutant Sabretooth leaps out of the woods and hurls him around until he is knocked out."),
        ("サイクロップスとストーム",
         "そこへ2人のミュータントが現れる。目から光線を出すサイクロップスと、天気をあやつるストームだった。サイクロップスは光線でセイバートゥースを吹き飛ばし、はさまれていたローグを助け出す。\n"
         "2人がローガンとローグを連れて離れた直後、車は爆発する。",
         "Cyclops and Storm",
         "Two more mutants appear: Cyclops, who fires beams from his eyes, and Storm, who controls the weather. Cyclops blasts Sabretooth away and cuts Rogue free.\n"
         "They get Logan and Rogue clear seconds before the truck explodes."),
        ("マグニートーの隠れ家",
         "セイバートゥースは、海に囲まれたマグニートーの隠れ家へ戻る。長い舌を持つ仲間のトードが、大きな機械の作業をしている。\n"
         "セイバートゥースは、相手がこちらの動きを知っていたこと、ねらったミュータントは向こうの手に渡ったことを報告する。持ち帰れたのは、ローガンの認識票（ドッグタグ）だけだった。マグニートーは、首脳会議が近い、準備を急げと言う。",
         "Magneto's lair",
         "Sabretooth returns to Magneto's hideout, surrounded by sea. Toad, a mutant with a long tongue, is at work on a large machine.\n"
         "Sabretooth reports that the others knew they were coming, and that the mutant they wanted is now with them. All he has brought back is Logan's dog tags. Magneto reminds him that the summit is close and they must be ready."),
    ]),
    ("第3部 恵まれし子らの学園", "Part 3: The school for gifted youngsters", [
        ("目を覚ましたローガン",
         "ローガンは、見知らぬ医務室で目を覚ます。注射をしようとしていたのは、公聴会で証言したジーンだった。ローガンはジーンを敵だと思って押さえつけ、部屋を飛び出す。\n"
         "地下の通路で迷っていると、頭の中に声が聞こえてくる。声にみちびかれてエレベーターで上の階に出ると、そこは子どもたちが走り回る学校だった。ローガンが逃げこんだ教室では、車いすのプロフェッサーXが授業をしていた。忘れ物を取りに戻った生徒のキティは、閉まったドアを通り抜けて出て行く。",
         "Logan wakes up",
         "Logan wakes in an unfamiliar infirmary. The woman about to give him an injection is Jean, the doctor from the hearing. Taking her for an enemy, he grabs her and bolts from the room.\n"
         "Lost in the underground corridors, he hears a voice in his head. It guides him to an elevator and up into a school full of running children. The classroom he ducks into is Professor X's, teaching from his wheelchair. A student named Kitty comes back for something she forgot, then leaves by walking straight through the closed door."),
        ("プロフェッサーXの説明",
         "プロフェッサーXは、ここがニューヨーク州ウエストチェスターにあるミュータントの若者のための学校「恵まれし子らの学園」で、ローグも無事だと話す。そこへ、ローガンを助けたサイクロップス（スコット）とストーム、そしてジーンが入ってくる。\n"
         "ローガンを襲ったセイバートゥースは、強い力を持つミュータント、マグニートーの仲間だという。ローガンはばかばかしいと出て行こうとする。しかしプロフェッサーXは、ローガンが15年前より昔の記憶をなくしていることを心の力で言い当て、自分が何者なのかを探す手伝いができると話す。",
         "Professor X explains",
         "Professor X tells him this is Xavier's School for Gifted Youngsters, a school for young mutants in Westchester, New York, and that Rogue is safe. In come the two who rescued him, Cyclops (Scott) and Storm, and then Jean.\n"
         "Sabretooth, he says, works for a very powerful mutant called Magneto. Logan finds it all ridiculous and starts to leave. But Xavier, reading his mind, knows that Logan has no memory of anything before fifteen years ago, and says he can help him find out who he is."),
        ("学園と48時間の約束",
         "プロフェッサーXは学園を案内する。ここでは、行き場のないミュータントの子どもたちが、力の使い方を学んでいる。ローグもここで学び始め、氷を作り出せる少年ボビーと出会う。\n"
         "学校は表の顔で、地下にはジェット機の格納庫がある。先生のサイクロップス、ストーム、ジーンは、人間との共存のために戦うチーム「X-MEN」でもあった。プロフェッサーXは、若いころに出会った友人エリックが、人間はミュータントを受け入れないと考えてマグニートーになったことを話す。\n"
         "プロフェッサーXは、マグニートーがなぜローガンをねらうのかを48時間で調べる、その代わりに過去を探す手伝いをする、と持ちかける。",
         "The school, and 48 hours",
         "Xavier shows him around. Here, mutant children with nowhere else to go learn to use their powers. Rogue starts classes too, and meets Bobby, a boy who can make ice.\n"
         "The school is only the public face: below it is a hangar with a jet. Its teachers, Cyclops, Storm and Jean, are also the X-Men, a team that works for peace between mutants and humans. Xavier tells Logan about Erik, the friend of his youth who came to believe humanity would never accept mutants, and became Magneto.\n"
         "He offers a deal: give him 48 hours to find out why Magneto is after Logan, and in return he will help Logan uncover his past."),
        ("さらわれたケリー議員",
         "ケリー議員は、ミュータントに反対する人々の声援を受けながら、補佐官のガイリッチとヘリコプターに乗りこむ。機内で議員は、自分ならミュータントを全員閉じこめる、これは戦争だと話す。\n"
         "ふと窓の外を見ると、下は海だった。となりの補佐官の姿が、青い肌の女に変わっていく。どんな姿にも化けられるミスティークだった。ミスティークは議員をけって気を失わせる。操縦していたのはトードだった。ヘリコプターは、マグニートーの隠れ家の島へ向かう。",
         "Kelly abducted",
         "Cheered by an anti-mutant crowd, Senator Kelly boards a helicopter with his aide, Henry Gyrich. On board he says that if it were up to him he would lock every mutant away; this is a war.\n"
         "Glancing out the window, he sees only ocean. Beside him, his aide's body ripples into that of a blue-skinned woman: Mystique, who can take anyone's form. She kicks him unconscious. The pilot is Toad. The helicopter heads for Magneto's island hideout."),
        ("ローガンの体の秘密",
         "学園では、ジーンがローガンの体を調べた結果を、プロフェッサーXたちに見せる。ローガンの骨には、全身にわたって「アダマンチウム」というとても固い金属が付けられていた。\n"
         "そんな手術に耐えられたのは、けががすぐに治る力のおかげだった。その力のせいで年齢も分からない。誰が手術をしたのか、ローガン自身も覚えていない。",
         "The secret of Logan's body",
         "At the school, Jean shows Professor X and the others what her tests on Logan have found. A supposedly indestructible metal called adamantium has been bonded to his entire skeleton.\n"
         "Only his healing power could have let him survive such an operation. It also makes his age impossible to tell. Logan himself has no memory of who did it."),
        ("ジーンとスコット",
         "夜、ジーンはローガンを泊まる部屋へ案内する。ジーンは、念力で物を動かす力のほかに、少しだけ人の心を読む力もあると話す。ローガンに言われて心の中をのぞくと、ジーンの目に、炎や手術の光景が飛びこんでくる。\n"
         "そこへ、ジーンの恋人のスコットが入ってくる。ジーンが出て行ったあと、スコットとローガンは言い合いになり、スコットは彼女に近づくなとくぎを刺す。",
         "Jean and Scott",
         "That night Jean shows Logan to his room. Besides moving things with her mind, she tells him, she has some telepathic ability. At his urging she looks into his mind, and sees flashes of fire and an operation.\n"
         "Scott, her boyfriend, walks in. After Jean leaves, he and Logan trade taunts, and Scott warns him to stay away from his girl."),
        ("人間を変える機械",
         "隠れ家で、ケリー議員はいすにしばりつけられている。まわりにはミスティーク、トード、セイバートゥースが立っている。現れたマグニートーは、本物の補佐官ガイリッチはとうに死んでいて、ミスティークがなりすましていたと教える。\n"
         "マグニートーは、自分の磁力で動かす大きな機械を議員の前で動かす。機械から広がる光をあびると、ふつうの人間がミュータントに変わる。光は議員をのみこむ。\n"
         "機械を止めたマグニートーは、立っていられないほど弱り、ミスティークにささえられる。",
         "The mutation machine",
         "In the hideout, Kelly is strapped to a chair, with Mystique, Toad and Sabretooth standing around him. Magneto appears and tells him the real Gyrich has been dead for some time; Mystique has been taking his place.\n"
         "In front of the senator, Magneto starts a large machine powered by his own magnetism. The light that spreads from it turns ordinary humans into mutants. It washes over Kelly.\n"
         "When the machine stops, Magneto is so drained that Mystique has to hold him up."),
    ]),
    ("第4部 ローグの家出", "Part 4: Rogue runs away", [
        ("悪夢",
         "その夜、ローガンは、骨に金属を付けられたときの悪い夢にうなされている。眠れずにいたローグが声を聞いて部屋に入り、起こそうとする。\n"
         "飛び起きたローガンの爪が、ローグの胸に突き刺さる。われに返ったローガンは爪を引き、助けを呼ぶ。ローグは手をのばして、ローガンのほおに触れる。ローグの傷はふさがっていき、力を吸われたローガンは気を失って倒れる。\n"
         "かけつけたスコットやジーン、ストーム、生徒たちは、その様子を見ていた。ローグはわざとではないと言いながら部屋を出る。生徒たちは、おびえてローグから離れる。",
         "The nightmare",
         "That night Logan is caught in a nightmare about the metal being bonded to his bones. Rogue, unable to sleep, hears him, comes into his room and tries to wake him.\n"
         "He jolts awake and his claws go into her chest. Coming to his senses, he pulls them back and shouts for help. Rogue reaches up and touches his cheek. Her wounds close, and Logan, drained, passes out.\n"
         "Scott, Jean, Storm and the students have rushed in and seen it. Rogue leaves the room saying it was an accident. The students shrink back from her in fear."),
        ("ローグの力",
         "目を覚ましたローガンのそばには、プロフェッサーXがいた。ローグは無事だという。\n"
         "プロフェッサーXは、ローグが触れた相手の力を吸い取ること、相手がミュータントならその能力まで吸い取ることを説明する。今回は、ローガンの治る力を吸って傷をふさいだ。もう少し長く触れていたら、ローガンは死んでいたかもしれなかった。",
         "Rogue's power",
         "When Logan comes around, Professor X is sitting beside him. Rogue is all right, he says.\n"
         "He explains that Rogue absorbs the energy of anyone she touches, and with mutants, their gifts as well. This time she took Logan's ability to heal and closed her own wounds. Had she held on any longer, she could have killed him."),
        ("ケリーの脱出",
         "隠れ家の牢屋に入れられたケリー議員は、自分の体がやわらかく、どこまでも伸び縮みするようになったことに気づく。議員は、鉄格子のすき間に頭を押しこんで、外へ抜け出す。\n"
         "マグニートーとセイバートゥースが様子を見に来ると、牢屋は空だった。議員は外のがけにしがみついている。セイバートゥースが腕をつかんで引き上げようとするが、議員の手は伸びてすり抜け、議員は叫びながら海へ落ちていく。\n"
         "昼間、議員は海から浜辺に上がってくる。",
         "Kelly's escape",
         "Locked in a cell in the hideout, Kelly discovers that his body has become soft and stretchy. He pushes his head between the bars and squeezes himself out.\n"
         "When Magneto and Sabretooth come to look in on him, the cell is empty. Kelly is clinging to the cliff outside. Sabretooth grabs his arm to haul him back, but the hand stretches and slips through his grip, and Kelly falls screaming into the sea.\n"
         "In daylight, he comes up out of the water onto a beach."),
        ("ボビーに化けたミスティーク",
         "翌朝、ローグは学園の庭のベンチに一人で座っている。そこへボビーが来て、ミュータントが仲間に力を使ってはいけない、生徒たちはこわがっているし、プロフェッサーXはひどく怒っている、自分なら出て行く、と話す。ローグは泣きそうになりながら立ち去る。\n"
         "見送るボビーの目が、黄色く光る。ボビーは、学園に入りこんだミスティークが化けた姿だった。",
         "Mystique as Bobby",
         "The next morning Rogue is sitting alone on a bench in the school grounds. Bobby comes over and tells her that mutants should never use their powers on each other, that the students are scared and Professor X is furious, and that in her place he would get out. Close to tears, Rogue walks away.\n"
         "As he watches her go, Bobby's eyes flash yellow. He is Mystique, who has slipped into the school."),
        ("セレブロ",
         "プロフェッサーXとスコットは、マグニートーがローガンに何を求めているのかを考えていた。そこへローガンが来て、ローグはどこかとたずねる。プロフェッサーXが心で探すと、ローグはもう学園にいなかった。\n"
         "プロフェッサーXは、自分の力を強めて遠くのミュータントを探せる丸い部屋「セレブロ」に入る。マグニートーをこれで探せないのは、相手が身を隠す方法を知っているからだという。セレブロは、マグニートーと2人で作ったものだった。ジーンは、自分にはまだ危なくて使えないと話す。\n"
         "プロフェッサーXは、ローグが駅にいることを突き止める。ねらわれているローガンには学園に残るよう言い、スコットとストームを迎えに行かせる。ところが、スコットのバイクがなくなっていた。ローガンが乗って、先に駅へ向かったのだ。",
         "Cerebro",
         "Professor X and Scott are trying to work out what Magneto wants with Logan when Logan comes in asking where Rogue is. Xavier searches with his mind: she is no longer in the school.\n"
         "He goes into Cerebro, a round chamber that amplifies his power so he can find mutants far away. He cannot find Magneto with it, he says, because Magneto knows how to shield himself. He helped Xavier build it. Jean says it would be too dangerous for her to use.\n"
         "Xavier locates Rogue at the train station. He tells Logan, the one Magneto is after, to stay put, and sends Scott and Storm to bring her back. But Scott's motorcycle is missing. Logan has taken it and gone ahead."),
        ("ミスティークの細工",
         "学園では、本物のボビーが友だちに、ローグと昼ごはんの約束をしていたのに来なかったと話している。\n"
         "一方、ボビーの姿のミスティークは地下へ下りる。セレブロの扉の前で、目だけをプロフェッサーXの目に変えて検査を通り、中に入って装置に細工をする。",
         "Mystique's sabotage",
         "In the school, the real Bobby tells his friends that Rogue was supposed to meet him for lunch and never came.\n"
         "Meanwhile Mystique, still looking like Bobby, goes down to the basement. At Cerebro's door she changes her eyes into Professor X's to pass the scanner, goes in and tampers with the machine."),
        ("列車の中で",
         "ローグは、出発を待つ列車の席に座り、まわりの人たちが気がねなく触れ合うのを見つめている。そこへローガンが来て、となりに座る。2人はゆうべのことを互いにあやまる。\n"
         "ローグは、初めてキスをした相手が3週間も意識不明になったこと、その相手も、ローガンも、今も頭の中にいるように感じることを話す。ローガンは服の上からローグを抱き寄せ、プロフェッサーXは本気でローグを助けたいと思っている、もう一度だけ学園を信じてみよう、自分が守る、と約束する。",
         "On the train",
         "Rogue sits on a train waiting to leave, watching the people around her touch each other without a thought. Logan arrives and sits beside her. They each apologize for the night before.\n"
         "She tells him that the first boy she ever kissed was in a coma for three weeks, and that she can still feel him in her head, and Logan too. He holds her through her clothes and tells her Xavier truly wants to help her. Give these people one more chance, he says, and promises to take care of her."),
        ("マグニートーの襲撃",
         "動き出した列車が急に止まり、明かりが消える。マグニートーが磁力で車両を引き裂いて、宙に浮いたまま入ってくる。ローガンは爪を出すが、全身の骨が金属におおわれているため、磁力で体ごと持ち上げられ、動けなくなる。\n"
         "なぜ自分をねらうのかとローガンが聞くと、マグニートーは、ほしいのはお前ではないと答える。ねらいはローグだった。マグニートーはローガンを投げ飛ばし、ローグを麻酔の矢で眠らせて連れ去る。\n"
         "同じころ駅の中では、ローグを探していたストームがセイバートゥースにのどをつかまれる。助けに走ったスコットは、壁に張りついたトードの舌にバイザーをはぎ取られ、光線が天井を突き破る。ストームは雷を落として、セイバートゥースを壁の向こうへ吹き飛ばす。",
         "Magneto attacks",
         "The train starts to move, then jolts to a halt and the lights go out. Magneto tears the carriage open with magnetism and floats in. Logan pops his claws, but with metal all through his skeleton he is simply lifted off the floor and held helpless.\n"
         "Logan asks what Magneto wants with him. It isn't him he wants, Magneto answers. It is Rogue. He flings Logan aside, puts Rogue out with a tranquilizer dart and takes her.\n"
         "Meanwhile, inside the station, Storm is asking after Rogue when Sabretooth seizes her by the throat. Scott runs to help, but Toad, clinging to the wall, whips off his visor with his tongue, and Scott's beam blows a hole in the ceiling. Storm calls down lightning and sends Sabretooth flying through a wall."),
        ("連れ去られたローグ",
         "マグニートーたちがローグを連れて駅を出ると、外は警察の車に囲まれていた。マグニートーは磁力で車を持ち上げて落とし、警官たちの銃を取り上げて宙に浮かべ、警官たち自身に向ける。\n"
         "そのとき、セイバートゥースとトードが、マグニートーに向かってやめろと言い出す。近くの車の中から、プロフェッサーXが2人の心をあやつって話していた。ローグを何に使うのかと聞かれても、マグニートーは答えない。かぶっているヘルメットのせいで、プロフェッサーXにも心は読めなかった。\n"
         "マグニートーは銃を1発撃たせ、弾を警官のすぐ目の前で止めてみせる。全部は止められないだろうと言われ、プロフェッサーXは2人を放すしかなかった。ミスティークの操縦するヘリコプターが下りてきて、ブラザーフッドはローグを連れて去っていく。",
         "Rogue taken",
         "When Magneto's group walks out of the station with Rogue, police cars are all around it. He lifts cars with magnetism and drops them, then pulls the officers' guns out of their hands and hangs them in the air, pointed at the officers themselves.\n"
         "Then Sabretooth and Toad turn on him, telling him to stop. Professor X, in a car nearby, is speaking through their minds. Asked what he needs Rogue for, Magneto gives no answer, and the helmet he wears keeps Xavier out of his thoughts.\n"
         "Magneto fires one gun and stops the bullet an inch short of an officer. Xavier cannot stop them all, he says, and Xavier has no choice but to let the two go. A helicopter flown by Mystique comes down, and the Brotherhood leaves with Rogue."),
    ]),
    ("第5部 ケリーの最期と決戦の準備", "Part 5: Kelly's end and getting ready", [
        ("学園に来たケリー",
         "学園に戻ったローガンは、ねらいは自分だと言ったプロフェッサーXに怒りをぶつける。プロフェッサーXは、ひどいまちがいをしたとあやまる。ローガンは一人でローグを探しに出ようとする。ストームは一緒に戦ってほしいと頼むが、ローガンは、自分たちをきらう世界のために戦う気はないと断る。\n"
         "ローガンが玄関のドアを開けると、そこにケリー議員が立っていた。弱りきった様子の議員は、ジーン・グレイ博士に会いに来たと言う。",
         "Kelly at the school",
         "Back at the school, Logan is furious with Professor X for saying Magneto was after him. Xavier apologizes: he made a terrible mistake. Logan means to go after Rogue alone. Storm asks him to fight alongside them, but he says he won't fight for a world that hates them.\n"
         "He opens the front door, and Senator Kelly is standing there, barely on his feet, asking for Dr. Jean Grey."),
        ("マグニートーのねらい",
         "地下の医務室で、議員は、ふつうの病院に行くのがこわかったと話す。プロフェッサーXは議員の心を読み、機械で変えられたときの記憶を見る。機械を止めたあとのマグニートーは、ひどく弱っていた。\n"
         "プロフェッサーXたちは話し合う。機械の光は、ふつうの人間をミュータントに変える。しかし、むりやり変えられた議員の体はそれを受けつけず、細胞がこわれ始めていた。\n"
         "では、なぜローグなのか。スコットが気づく。機械はマグニートーの力で動き、動かせば自分が死にかける。だからローグに自分の力を吸わせ、代わりに機械を動かさせるつもりなのだ。それは、ローグの命を引きかえにすることだった。",
         "What Magneto wants",
         "In the infirmary below, Kelly says he was afraid to go to an ordinary hospital. Professor X reads his mind and sees his memory of the machine, and of how weak Magneto was once it stopped.\n"
         "Xavier and the others talk it through. The machine's radiation turns ordinary people into mutants. But Kelly's body is rejecting the forced mutation, and his cells are breaking down.\n"
         "So why Rogue? Scott sees it. The machine runs on Magneto's power, and running it nearly killed him. He means to have Rogue absorb his power and run it in his place, at the cost of her life."),
        ("議員の最期",
         "医務室では、ストームがケリー議員に付きそっている。体から水をしたたらせながら、議員は一人にしないでくれと頼む。ふつうの人間が憎いかと聞かれ、ストームは、ときどきは憎い、こわいからだと答える。議員は、こわがる相手が1人減ったな、と言う。\n"
         "そのあと議員の体は大きくふるえ、くずれて水になり、床に流れて消えてしまう。ストームは、議員が死んだことを皆に知らせる。",
         "The senator's end",
         "In the infirmary, Storm is sitting with Kelly. Water is running off his body, and he asks her not to leave him alone. Does she hate normal people, he asks. Sometimes, she says, because she is afraid of them. Then she has one less person to be afraid of, he tells her.\n"
         "His body begins to shake, breaks down into water and spills across the floor. Storm goes to tell the others that Senator Kelly is dead."),
        ("倒れたプロフェッサーX",
         "プロフェッサーXは、ローグを探すためにセレブロに入り、ヘルメットをかぶる。しかし、ミスティークの細工のせいで装置がおかしくなり、プロフェッサーXは車いすからくずれ落ちて、そのまま目を覚まさなくなる。\n"
         "ジーンは装置を調べ、仕かけられたものを取りのぞく。スコットは、眠ったままのプロフェッサーXに、これまでの感謝を伝え、何かあれば自分が学園を守ると約束する。",
         "Professor X falls",
         "Professor X goes into Cerebro to search for Rogue and puts on the helmet. But Mystique's tampering turns the machine against him. He slumps out of his wheelchair and does not wake.\n"
         "Jean examines Cerebro and removes what was planted in it. At Xavier's bedside, Scott thanks him for everything he has done, and promises to look after the school if anything happens."),
        ("ジーンがセレブロを使う",
         "ジーンは、危険を知りながら、自分でセレブロを使う。気づいたスコットが走るが、扉は目の前で閉まる。\n"
         "強すぎる力に耐えきれず、ジーンは床に倒れる。かけ寄ったスコットに、ジーンは、マグニートーの行き先が分かったと告げる。",
         "Jean uses Cerebro",
         "Knowing the danger, Jean uses Cerebro herself. Scott sees and runs, but the door closes in his face.\n"
         "The strain is too much and she collapses. When Scott reaches her, she tells him she knows where Magneto is going."),
        ("船の上のマグニートーとローグ",
         "夜、マグニートーたちは船で自由の女神像のあるリバティ島へ向かう。となりのエリス島では、世界の首脳会議が始まろうとしていた。\n"
         "船の中で、マグニートーはローグに、この像を初めて見たのは1949年だったと話す。自分は殺されるのかとローグが聞くと、マグニートーはそうだと答える。世界のリーダーたちを自分たちと同じミュータントに変える。ローグの犠牲がミュータントを生きのびさせるのだ、と。マグニートーは、ローグを機械につなぐようミスティークに命じる。機械は、像がかかげるたいまつの上にすえつけられる。",
         "Magneto and Rogue on the boat",
         "That night Magneto's group heads by boat for Liberty Island and the Statue of Liberty. On Ellis Island next to it, the summit of world leaders is about to begin.\n"
         "On the boat, Magneto tells Rogue he first saw the statue in 1949. She asks if he is going to kill her. \"Yes,\" he says. He will turn the world's leaders into mutants like themselves, and her sacrifice will mean the survival of their kind. He orders Mystique to put her in the machine, which is mounted in the statue's torch."),
        ("出撃",
         "スコット、ストーム、ジーン、ローガンの4人は作戦を立てる。マグニートーは、機械が人間を死なせることを知らない。ローグを使って大きな力で動かせば、会議のリーダーたちだけでなく、ニューヨークじゅうの人が死ぬことになる。\n"
         "ローガンも黒い制服を着る。4人は学園からジェット機で飛び立ち、ストームが呼んだ霧にまぎれて、リバティ島の近くの水の上に下りる。",
         "Heading out",
         "Scott, Storm, Jean and Logan plan the attack. Magneto does not know his machine kills. If Rogue runs it at full power, not only the leaders at the summit but everyone in New York will die.\n"
         "Logan puts on a black uniform too. The four take off from the school in the jet and, hidden in fog that Storm calls up, set down on the water by Liberty Island."),
    ]),
    ("第6部 自由の女神像の戦い", "Part 6: Battle at the Statue of Liberty", [
        ("像の中へ",
         "4人は自由の女神像の中へ入る。たいまつの上には機械が見える。入口の金属探知機がローガンの体に反応して鳴り出し、ローガンは爪で機械を突いて止める。\n"
         "展示室を進むと、ローガンが誰かのにおいに気づく。そこへ、もう一人のローガンが現れて襲いかかる。ミスティークが化けていた。2人のローガンは爪でやり合い、ほかの3人にはどちらが本物か分からない。戦ううちに、ローガンは3人と引き離される。",
         "Into the statue",
         "The four enter the Statue of Liberty. Above them, the machine sits on the torch. The metal detector at the entrance goes off at Logan, and he silences it with his claws.\n"
         "As they move through the museum hall, Logan catches someone's scent. Then a second Logan appears and attacks him: Mystique in disguise. The two Logans slash at each other, and the other three cannot tell which is real. The fight carries Logan away from them."),
        ("トードとの戦い",
         "残った3人には、トードが飛びかかる。トードはスコットを扉の向こうに閉じこめ、ストームを舌でつかんで投げ飛ばす。ジーンは念力でトードを宙に止めるが、顔にねばねばしたものをはきかけられる。それはすぐに固まって口と鼻をふさぎ、ジーンは息ができなくなる。\n"
         "スコットは光線で扉を破って出てくると、弱めた光線でジーンの顔のかたまりをはがす。\n"
         "エレベーターの穴へけり落とされていたストームも戻ってくる。ストームは強い風でトードを像の外へ吹き飛ばす。トードは舌を像に巻きつけて持ちこたえるが、ストームが雷を落とすと、海のほうへはじき飛ばされていく。",
         "Fighting Toad",
         "Toad leaps on the remaining three. He shuts Scott behind a door and throws Storm with his tongue. Jean catches him in mid-air with her telekinesis, but he spits slime over her face. It hardens at once over her mouth and nose, and she cannot breathe.\n"
         "Scott blasts his way out, then uses a low-powered beam to break the slime off Jean's face.\n"
         "Storm, who had been kicked down an elevator shaft, comes back up. She blows Toad out of the statue with a gale. He hangs on by his tongue, until she calls down a lightning bolt and he is flung away toward the water."),
        ("ミスティークを見破る",
         "ローガンとミスティークの戦いは続いている。ミスティークは元の青い姿に戻り、すばやい動きでローガンを振り回して姿を消す。\n"
         "やがて、ローガンのもとにストームが近づいてきて、みんなと合流しようと言う。ローガンはにおいをかぎ、爪でその腹を刺す。ストームの姿はミスティークに戻り、床に倒れる。\n"
         "ローガンは、スコットとジーン、本物のストームと合流する。本物だと証明しろと言うスコットに、ローガンは悪口で答え、スコットはそれで本物だと納得する。",
         "Seeing through Mystique",
         "Logan's fight with Mystique goes on. She shifts back to her own blue form, runs rings around him and vanishes.\n"
         "A little later Storm comes up to Logan and says they need to regroup. He sniffs the air, then drives his claws into her stomach. Storm's shape melts back into Mystique, and she drops to the floor.\n"
         "Logan rejoins Scott and Jean, and the real Storm. Asked to prove he is himself, he just tells Scott, \"You're a dick.\" That is proof enough."),
        ("マグニートーにつかまる",
         "4人が像の上のほうへのぼると、ローガンの体が急に動かなくなる。ローガンは宙に浮いて壁に押しつけられ、ほかの3人も、飛んできた金属で壁にしばりつけられる。マグニートーが下りてきて、ローガンの両手を胸に向けさせ、爪を出せないようにする。\n"
         "スコットはジーンと向かい合わせにされ、セイバートゥースにバイザーを取られて、目を開けられなくなる。銅でできた像の中では、ストームも雷を使えない。\n"
         "ジーンとストームは、ケリー議員が死んだこと、機械を動かせば会議の人たちも死ぬことを伝える。しかしマグニートーは信じない。ローガンは、本当に正しいと思うなら自分で機械に入るはずだと言う。マグニートーは答えず、たいまつへ飛んでいく。",
         "Caught by Magneto",
         "As the four climb higher in the statue, Logan suddenly cannot move. He is lifted and slammed against the wall, and flying metal binds the other three in place. Magneto floats down and turns Logan's fists toward his own chest so he cannot use his claws.\n"
         "Scott is pinned facing Jean, and Sabretooth takes his visor, so he has to keep his eyes shut. Inside a copper statue, Storm cannot use her lightning either.\n"
         "Jean and Storm tell Magneto that Senator Kelly is dead, and that the people at the summit will die too. He does not believe them. If he were really so righteous, Logan says, he would be the one in the machine. Magneto does not answer, and flies up to the torch."),
        ("ローグに力を移す",
         "たいまつの上で、助けを求めて叫ぶローグのほおに、マグニートーは自分から手を当て、磁力の力を吸い取らせる。\n"
         "下では、セイバートゥースがストームに近づいていく。ローガンは、自分の体が傷つくのもかまわずに爪を出し、しばっていた金属を切って抜け出す。そしてセイバートゥースに飛びかかり、2人は像の頭の上に出て戦う。",
         "Giving Rogue his power",
         "On the torch, as Rogue screams for help, Magneto lays his hand on her cheek and makes her absorb his magnetic power.\n"
         "Below, Sabretooth closes in on Storm. Logan forces his claws out even though it wounds him, cuts his bonds and gets free. He leaps at Sabretooth, and the two end up fighting on top of the statue's head."),
        ("セイバートゥースを倒す",
         "戦いの中で、ローガンは取られていた自分の認識票を取り返す。しかしセイバートゥースに投げ飛ばされ、像の外へ落ちていく。\n"
         "セイバートゥースは中に戻り、ストームにとどめを刺そうとする。そこへ、像にしがみついて助かったローガンが、スコットのバイザーを持って戻ってくる。ジーンは念力でバイザーをスコットの目の前に運び、合図をする。スコットが目を開けると、光線がセイバートゥースを壁ごと像の外へ吹き飛ばす。セイバートゥースは下の船の上に落ちる。\n"
         "ローガンは3人をしばっていた金属を切る。",
         "Defeating Sabretooth",
         "In the fight, Logan snatches back his stolen dog tags. But Sabretooth throws him, and he goes over the side of the statue.\n"
         "Sabretooth comes back in to finish Storm. Then Logan, who caught hold of the statue, returns with Scott's visor. Jean floats it in front of Scott's eyes and gives the word. He opens them, and the beam blasts Sabretooth out through the wall. He crashes onto a boat below.\n"
         "Logan cuts the other three free."),
        ("たいまつの上へ",
         "たいまつの機械が動き出し、光の輪が広がり始める。スコットの光線で機械をこわせば、中のローグも死んでしまう。\n"
         "そこで、ストームが風を起こしてローガンを持ち上げ、ジーンが念力でささえて、たいまつの上まで運ぶ。ローガンは機械に飛び移り、ローグをつなぐ鎖を切ろうとする。しかし、少し力を取り戻したマグニートーが、磁力でローガンの爪を止めてしまう。",
         "Up to the torch",
         "The machine in the torch comes to life, and a ring of light begins to spread. If Scott blasts the machine, Rogue will die with it.\n"
         "So Storm raises a wind to lift Logan, and Jean steadies him with telekinesis, carrying him up to the torch. He jumps onto the machine and tries to cut Rogue's chains. But Magneto, who has regained some strength, holds his claws back with magnetism."),
        ("機械をこわす",
         "光の輪は海をこえて、首脳会議の開かれているエリス島へ広がっていく。スコットは、ジーンに待つよう言われながらねらいを定め、すき間が見えた一瞬に光線を放って、マグニートーを打ち倒す。\n"
         "自由になったローガンは、爪で機械を切りこわす。光の輪は、誰にも届かないうちに消える。",
         "Destroying the machine",
         "The ring of light spreads over the water toward Ellis Island and the summit. Scott takes aim while Jean tells him to wait, then fires the instant he has a clear shot and blasts Magneto down.\n"
         "Freed, Logan slashes the machine apart. The ring of light dies away before it reaches anyone."),
        ("ローグを救う",
         "ローガンは鎖を切ってローグを抱きとめるが、ローグは動かない。髪の前のほうがひとふさ、白くなっていた。\n"
         "ローガンはローグのほおに手を当て、自分の治る力を吸わせようとする。しばらく何も起きず、ローガンはローグを抱きしめる。やがてローガンの顔や体に、これまでの戦いの傷が次々に開いていく。ローグは息を吹き返し、力を吸われたローガンは血を流して倒れる。",
         "Saving Rogue",
         "Logan cuts the chains and catches Rogue, but she is not moving. A streak of her hair has turned white.\n"
         "He puts his hand to her cheek so that she will absorb his healing power. For a while nothing happens, and he holds her close. Then the wounds of the night's fighting begin to open across his face and body. Rogue gasps back to life, and Logan, drained and bleeding, collapses."),
    ]),
    ("第7部 その後", "Part 7: Afterward", [
        ("目を覚ますローガン",
         "学園の医務室で、ローガンは目を覚ます。傷はすっかり治っていた。付きそっていたジーンは、ローグは無事だと教え、勇気のあることをしたと言う。\n"
         "ローガンはジーンへの気持ちを言いかけるが、ジーンの様子を見て話を変え、プロフェッサーXの具合をたずねる。プロフェッサーXも回復していた。",
         "Logan wakes",
         "Logan wakes in the school's infirmary, his wounds fully healed. Jean, who has been watching over him, tells him Rogue is fine and that what he did was very brave.\n"
         "He starts to say how he feels about her, reads her reaction, and asks after the professor instead. Xavier has recovered too."),
        ("ケリー議員のニュース",
         "X-MENは、テレビのニュースに出ているケリー議員を見る。議員は、ミュータント登録法案への支持を取り下げると話している。その目が、一瞬黄色く光る。生きのびたミスティークが、議員に化けていた。",
         "Kelly on the news",
         "The X-Men watch Senator Kelly on the TV news, announcing that he is withdrawing his support for the Mutant Registration Act. For a moment his eyes flash yellow. It is Mystique, who survived, posing as him."),
        ("ローガンの旅立ち",
         "プロフェッサーXは、約束どおりローガンに手がかりを教える。ローガンが見つかった場所の近く、カナダのロッキー山脈のアルカリ湖に、使われなくなった軍の施設があるという。\n"
         "庭でほかの生徒たちと遊んでいたローグは、出て行くローガンに気づいて追いかけ、行かないでほしいと言う。ローガンは、必ず戻ると約束して、自分の認識票をローグに預ける。そして、スコットのバイクに乗って学園を出て行く。",
         "Logan sets out",
         "As promised, Professor X gives Logan a lead: near where he was found, at Alkali Lake in the Canadian Rockies, there is an abandoned military base.\n"
         "Rogue, who has been playing with the other students, sees him leaving and runs after him. She doesn't want him to go. He promises he will be back, and leaves his dog tags with her. Then he rides away from the school on Scott's motorcycle."),
        ("プラスチックの牢屋",
         "マグニートーは、金属を一つも使わないプラスチックの牢屋に入れられている。プロフェッサーXが面会に来て、2人はチェスをする。\n"
         "マグニートーは、いつかあの法律が通ることが心配ではないのかとたずねる。プロフェッサーXは、もめごとを起こしに学園へ来る者がいたら、その者のほうが気の毒だと答える。\n"
         "去っていくプロフェッサーXに、マグニートーは、この牢屋もいつまでも自分を閉じこめてはおけない、戦いは必ず来るし自分は戦うつもりだ、と言う。プロフェッサーXは、そのときはいつでも自分が止めると答える。",
         "The plastic prison",
         "Magneto is held in a prison made entirely of plastic, with no metal at all. Professor X visits, and the two play chess.\n"
         "Magneto asks whether it doesn't worry him that they may pass that law one day. Xavier answers that he pities the poor soul who comes to his school looking for trouble.\n"
         "As Xavier leaves, Magneto tells him this plastic prison won't hold him forever; the war is still coming, and he intends to fight it. Xavier replies that he will always be there to stop him."),
    ]),
    ("まとめ（最後までのネタバレ）", "Summary (spoilers through the end)", [
        ("マグニートーの計画と結末",
         "①セイバートゥースにローグをねらわせるが、X-MENにはばまれる（第2部）\n"
         "②人間をミュータントに変える機械を、さらったケリー議員で試す。動かした自分もひどく弱る（第3部）\n"
         "③自分の代わりに機械を動かさせるため、ミスティークにローグを学園から追い出させ、駅でさらう（第4部）\n"
         "④自由の女神像のたいまつに機械を置き、エリス島の首脳会議に集まった世界のリーダーたちを変えようとする。機械が人間を死なせることは信じない（第5部〜第6部）\n"
         "⑤サイクロップスに打ち倒され、ローガンが機械をこわす（第6部）\n"
         "⑥プラスチックの牢屋に入れられる（第7部）",
         "Magneto's plan and how it ended",
         "1) He sends Sabretooth after Rogue, but the X-Men stop him (Part 2).\n"
         "2) He tests a machine that turns humans into mutants on the kidnapped Kelly, and is badly weakened by running it (Part 3).\n"
         "3) To have Rogue run the machine in his place, he has Mystique drive her out of the school and seizes her at the station (Part 4).\n"
         "4) He sets the machine in the Statue of Liberty's torch to change the world leaders at the Ellis Island summit, and refuses to believe it kills humans (Parts 5–6).\n"
         "5) Cyclops blasts him down and Logan destroys the machine (Part 6).\n"
         "6) He is locked in a plastic prison (Part 7)."),
        ("ローグとローガン",
         "①ローグはキスでボーイフレンドを意識不明にしてしまい、家を出る（第1部）\n"
         "②カナダでローガンと出会い、X-MENに助けられる（第2部）\n"
         "③ローガンの悪夢で刺されるが、ローガンの力を吸って助かる。ボビーに化けたミスティークにだまされて学園を出て、駅でマグニートーにさらわれる（第4部）\n"
         "④マグニートーの力を吸わされて機械を動かし、死にかけるが、ローガンが治る力を分けて救う（第6部）\n"
         "⑤ローガンは過去の手がかりを求めてアルカリ湖へ向かい、ローグに認識票を預ける（第7部）",
         "Rogue and Logan",
         "1) Rogue's kiss puts her boyfriend in a coma, and she runs away (Part 1).\n"
         "2) She meets Logan in Canada, and the X-Men rescue them (Part 2).\n"
         "3) Logan stabs her during a nightmare, but she survives by absorbing his power. Mystique, posing as Bobby, tricks her into leaving, and Magneto seizes her at the station (Part 4).\n"
         "4) Forced to absorb Magneto's power and run the machine, she nearly dies, but Logan saves her with his healing (Part 6).\n"
         "5) Logan heads for Alkali Lake in search of his past, leaving Rogue his dog tags (Part 7)."),
        ("ローガンの認識票",
         "①雪道の襲撃のあと、セイバートゥースが持ち去る（第2部）\n"
         "②自由の女神像の上の戦いで、ローガンが取り返す（第6部）\n"
         "③旅立つときに、また戻る約束のしるしとしてローグに渡す（第7部）",
         "Logan's dog tags",
         "1) Sabretooth carries them off after the ambush in the snow (Part 2).\n"
         "2) Logan takes them back in the fight on top of the statue (Part 6).\n"
         "3) He gives them to Rogue when he leaves, as a promise to return (Part 7)."),
        ("死んだ人",
         "・ケリー議員（第5部）：マグニートーの機械でむりやりミュータントに変えられた体がもたず、学園の医務室で、ストームの目の前で水になって消える。\n"
         "・補佐官ガイリッチ（第3部で分かる）：しばらく前に死んでいて、ミスティークがなりすましていた。",
         "Who died",
         "- Senator Kelly (Part 5): his body, forcibly mutated by Magneto's machine, can't hold together, and he dissolves into water in the school's infirmary in front of Storm.\n"
         "- His aide Gyrich (revealed in Part 3): dead for some time, with Mystique taking his place."),
    ]),
]
