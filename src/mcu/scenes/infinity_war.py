# 『アベンジャーズ／インフィニティ・ウォー』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（第1部から始め、場面ごとに起きた事実だけ）。
# 英語版ウィキペディアの作品のあらすじ（Plot）と、人物ごとの記事（ガモーラ、ヴィジョン、ソー、ストレンジ、ワンダ、ネビュラなど）で事実を確かめた。
# 映画は地球と宇宙の話を行ったり来たりするので、部は話の筋（場所）ごとにまとめ、部の中は起きた順に並べている。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 アスガルドの船", "Part 1: The Asgardian ship", [
        ("救難信号",
         "宇宙に、助けを求める声が流れる。前の作品で故郷アスガルドを失った人々を乗せた船が、襲われているという知らせだ。\n"
         "船の中には、倒れたアスガルドの人々が横たわっている。襲ったのはサノスと、サノスが「子どもたち」と呼ぶ4人の手下（エボニー・マウ、カル・オブシディアン、プロキシマ・ミッドナイト、コーヴァス・グレイヴ）だった。\n"
         "サノスの手には金色のこて（ガントレット）がはめられ、そこにはすでに紫色のパワー・ストーンが光っている。惑星ザンダーから奪ってきたものだ。",
         "A distress call",
         "A call for help goes out across space: the ship carrying the survivors of Asgard, destroyed in the previous film, is under attack.\n"
         "Asgardians lie dead throughout the ship. The attackers are Thanos and the four lieutenants he calls his children: Ebony Maw, Cull Obsidian, Proxima Midnight and Corvus Glaive.\n"
         "Thanos wears a golden gauntlet that already holds the purple Power Stone, taken from the planet Xandar."),
        ("ロキとテッセラクト",
         "サノスは、つかまえたソーの頭にパワー・ストーンを押し当てて痛めつけ、ロキにテッセラクト（青い立方体）を出せと迫る。\n"
         "ロキは初め、兄など好きにしろと強がるが、兄が苦しむのを見ていられず、隠していたテッセラクトを差し出してしまう。",
         "Loki and the Tesseract",
         "Thanos tortures the captured Thor by pressing the Power Stone to his head and demands that Loki hand over the Tesseract.\n"
         "Loki first acts as if he doesn't care, but he can't bear to watch his brother suffer and produces the hidden Tesseract."),
        ("ハルクが敗れる",
         "ロキの合図で、ハルクがサノスに飛びかかる。最初は押していたが、サノスは石の力を使わずに素手でハルクを打ち負かし、床にたたきつける。\n"
         "ソーも立ち向かうが、マウの力で、こわれた船の金属に体をしばりつけられ、口もふさがれる。",
         "The Hulk is beaten",
         "At Loki's signal, the Hulk leaps at Thanos. He has the upper hand at first, but Thanos beats him with his bare hands, without using a stone, and slams him to the floor.\n"
         "Thor attacks too, but Maw binds him in the ship's twisted metal and gags him."),
        ("ヘイムダルの最後の力",
         "大けがをして倒れていた門番ヘイムダルが、最後の力をふりしぼって虹の橋（ビフレスト）を呼び、ハルクだけを地球へ送り出す。\n"
         "それを見たサノスは、手下の槍を取ってヘイムダルを刺し殺す。ソーは動けないまま、それを見ているしかない。",
         "Heimdall's last strength",
         "The badly wounded Heimdall summons the Bifrost one last time and sends the Hulk alone to Earth.\n"
         "Seeing this, Thanos takes his lieutenant's spear and stabs Heimdall to death while Thor, bound, can only watch."),
        ("2つ目の石",
         "サノスはテッセラクトを素手でにぎりつぶし、中から青いスペース・ストーンを取り出して、こてにはめる。これで石は2つになった。\n"
         "サノスは手下たちに、地球にある残り2つの石を見つけて、タイタンにいる自分のところへ持ってこいと命じる。",
         "The second stone",
         "Thanos crushes the Tesseract in his hand, takes out the blue Space Stone and sets it in the gauntlet. He now has two stones.\n"
         "He orders his children: there are two more stones on Earth; find them and bring them to him on Titan."),
        ("ロキの最期",
         "ロキは、地球に行くなら案内役が要るだろうと言ってサノスに近づき、忠誠をちかうふりをする。その名乗りの中で、自分を「オーディンの息子」と呼ぶ。\n"
         "次の瞬間、ロキは隠していた短剣でサノスを刺そうとする。しかしサノスは力で短剣を止め、ロキの首をつかんでしめ上げる。ロキは息絶え、サノスは、今度は生き返らないと言って遺体をソーの前に投げる。",
         "Loki's end",
         "Saying Thanos will need a guide on Earth, Loki steps forward and pretends to pledge loyalty, naming himself a son of Odin.\n"
         "Then he tries to stab Thanos with a hidden dagger. Thanos stops it with his power, seizes Loki by the throat and strangles him. Loki dies, and Thanos tosses the body in front of Thor, saying there will be no resurrections this time."),
        ("船の爆発",
         "サノスと手下たちは、スペース・ストーンの力で姿を消す。残された船は爆発する。\n"
         "ソーはロキの遺体のそばに倒れたまま、こわれた船とともに宇宙へ投げ出される。",
         "The ship explodes",
         "Thanos and his children vanish using the Space Stone, and the ship explodes.\n"
         "Thor, lying beside Loki's body, is flung into space with the wreckage."),
    ]),
    ("第2部 ニューヨークの襲撃", "Part 2: Attack on New York", [
        ("屋根を突き破った男",
         "ニューヨークのサンクタム（魔術師の屋敷）で、ストレンジとウォンが話していると、屋根を突き破って何かが落ちてくる。ハルクから人間の姿に戻ったブルース・バナーだった。\n"
         "ブルースは2人に、サノスが来ると伝える。サノスは宇宙の命の半分を消すつもりだという。",
         "Something crashes through the roof",
         "At the Sanctum in New York, Strange and Wong are talking when something crashes through the roof. It's Bruce Banner, back in human form.\n"
         "He warns them that Thanos is coming. Thanos means to wipe out half of all life in the universe."),
        ("公園のトニー",
         "トニーは、婚約者のペッパーとセントラルパークを歩きながら、将来の子どもの話をしている。\n"
         "そこへストレンジが魔法の出入り口から現れ、宇宙が危ないので一緒に来てほしいと言う。後ろからブルースも顔を出す。トニーとブルースは久しぶりの再会だった。",
         "Tony in the park",
         "Tony is walking in Central Park with his fiancée Pepper, talking about having a child someday.\n"
         "Strange steps out of a portal and asks him to come, because the universe is in danger. Bruce appears behind him; he and Tony haven't seen each other in years."),
        ("6つの石の話",
         "サンクタムで、ウォンとストレンジは6つのインフィニティ・ストーンの説明をする。ストレンジの首かざりの中には緑色のタイム・ストーンがあり、ストレンジはこれを命がけで守るとちかっている。\n"
         "ブルースは、2012年にロキをニューヨークへ送りこんだのもサノスだったと話す。もう1つの石、マインド・ストーンはヴィジョンの額にある。しかしヴィジョンは行方が分からなくなっていた。\n"
         "ブルースは、スティーブに連絡しようと言う。トニーはスティーブから渡された古い携帯電話を出すが、シビル・ウォーで仲たがいしたままで、かけられない。",
         "The six stones",
         "At the Sanctum, Wong and Strange explain the six Infinity Stones. Strange's amulet holds the green Time Stone, and he has sworn to protect it with his life.\n"
         "Bruce says Thanos was also behind Loki's attack on New York in 2012. Another stone, the Mind Stone, is in Vision's forehead, but Vision has gone missing.\n"
         "Bruce says they should call Steve. Tony pulls out the old flip phone Steve sent him, but after their falling-out in Civil War, he can't bring himself to call."),
        ("ブリーカー通りの船",
         "街に風が吹き荒れ、人々が逃げまどう。空には、大きなドーナツ型の宇宙船が浮かんでいる。\n"
         "通りにはサノスの手下エボニー・マウとカル・オブシディアンが降り立ち、マウはタイム・ストーンを渡せと言う。\n"
         "トニーは胸の装置から一瞬でスーツをまとう。ブルースはハルクに変わろうとするが、ハルクが出てこようとしない。",
         "A ship over Bleecker Street",
         "A wind tears through the streets and people run. A huge ring-shaped spaceship hangs overhead.\n"
         "Thanos's lieutenants Ebony Maw and Cull Obsidian land on the street, and Maw demands the Time Stone.\n"
         "Tony's suit forms around him from the device on his chest. Bruce tries to become the Hulk, but the Hulk refuses to come out."),
        ("ピーターが加わる",
         "スクールバスに乗っていたピーター・パーカーは、窓の外の宇宙船に気づく。友だちのネッドに騒ぎを起こしてもらい、そのすきにスパイダーマンになって駆けつける。\n"
         "トニーはオブシディアンと、ストレンジとウォンはマウと戦う。ウォンは魔法の出入り口を開いて、オブシディアンを遠くへ飛ばしてしまう。",
         "Peter joins in",
         "On a school bus, Peter Parker spots the spaceship. His friend Ned creates a distraction so Peter can slip away as Spider-Man.\n"
         "Tony fights Obsidian while Strange and Wong take on Maw. Wong opens a portal and sends Obsidian far away."),
        ("さらわれるストレンジ",
         "マウはストレンジの首かざりからタイム・ストーンを取ろうとするが、ストレンジのかけた魔法で手が焼け、取れない。\n"
         "そこでマウは、ストレンジを金属でしばり上げ、宇宙船へ引き上げていく。マントがストレンジを引っぱって逃がそうとするが、間に合わない。",
         "Strange is taken",
         "Maw tries to take the Time Stone from Strange's amulet, but Strange's spell burns his hand and he can't.\n"
         "So Maw binds Strange in metal and lifts him up into the ship. Strange's cloak tries to pull him free, but it's not enough."),
        ("宇宙船にしがみつく",
         "トニーとピーターは、上がっていく宇宙船を追いかける。トニーはピーターに家へ帰れと言うが、ピーターは船体にしがみついたまま空高く上がってしまう。\n"
         "空気が薄くなり、ピーターは息ができなくなる。トニーは新しいスーツ（アイアン・スパイダー）をピーターに送り、スーツがピーターの体を包む。\n"
         "トニーはペッパーと電話で話している途中で、電話が切れる。2人は宇宙船の中に乗りこみ、船は地球を離れる。",
         "Clinging to the ship",
         "Tony and Peter chase the rising ship. Tony tells Peter to go home, but Peter clings to the hull and is carried high into the sky.\n"
         "As the air thins, Peter can't breathe. Tony sends him a new suit, the Iron Spider, which wraps around him.\n"
         "Tony's call with Pepper cuts out. The two get inside the ship as it leaves Earth."),
        ("地球に残った2人",
         "ウォンは、サンクタムを守るために残る。\n"
         "がれきの中で、ブルースはトニーが落とした携帯電話を拾う。スティーブにつながる、あの電話だ。",
         "The two left on Earth",
         "Wong stays behind to guard the Sanctum.\n"
         "In the rubble, Bruce picks up the phone Tony dropped: the one that reaches Steve."),
    ]),
    ("第3部 ガーディアンズとガモーラ", "Part 3: The Guardians and Gamora", [
        ("宇宙で拾われたソー",
         "救難信号を聞いたガーディアンズ・オブ・ギャラクシーは、こわれたアスガルドの船にたどり着く。宇宙をただよっていたソーが、ガーディアンズの船の窓にぶつかる。\n"
         "船の中に引き上げられたソーを、マンティスが力で目覚めさせる。",
         "Thor picked up in space",
         "Answering the distress call, the Guardians of the Galaxy reach the wrecked Asgardian ship. Thor, drifting in space, slams into their windshield.\n"
         "They pull him aboard, and Mantis wakes him with her power."),
        ("サノスのねらい",
         "ソーは、サノスが6つの石を集めていることを話す。パワー・ストーンは、サノスが惑星ザンダーを襲って奪っていた。スペース・ストーンも今は手の中にある。\n"
         "ソーは、赤いリアリティ・ストーンがコレクターのいるノーウェアにあると話す。ガモーラはサノスの娘として育てられ、サノスのことをよく知っている。",
         "What Thanos is after",
         "Thor explains that Thanos is collecting the six stones. He took the Power Stone by attacking Xandar, and now he has the Space Stone too.\n"
         "Thor says the red Reality Stone is with the Collector on Knowhere. Gamora, raised as Thanos's daughter, knows him well."),
        ("2組に分かれる",
         "ソーは、サノスを倒せる新しい武器を作るため、伝説の鍛冶場がある星ニダベリアへ向かうと決める。ロケットとグルートが小さな船でソーについていく。\n"
         "ピーター・クイル、ガモーラ、ドラックス、マンティスは、サノスより先にリアリティ・ストーンを守るため、ノーウェアへ向かう。",
         "Splitting up",
         "Thor decides to go to Nidavellir, home of a legendary forge, to make a new weapon that can kill Thanos. Rocket and Groot go with him in a small pod.\n"
         "Peter Quill, Gamora, Drax and Mantis head to Knowhere to secure the Reality Stone before Thanos."),
        ("ガモーラの頼み",
         "ノーウェアへ向かう船の中で、ガモーラはクイルに、もしサノスに捕まったら自分を殺してほしいと約束させる。\n"
         "ガモーラは、サノスの知らない秘密を自分だけが知っていると言う。もしその秘密を話してしまえば、宇宙が危なくなる。クイルは迷いながらも約束する。",
         "Gamora's request",
         "On the way to Knowhere, Gamora makes Quill promise that if Thanos captures her, he'll kill her.\n"
         "She says she knows something Thanos doesn't, and if he learns it, the universe is in danger. Torn, Quill promises."),
        ("ノーウェアの幻",
         "ノーウェアに着くと、サノスがコレクターを痛めつけて、石のありかを聞き出そうとしていた。ガモーラはサノスに飛びかかり、剣で刺す。サノスは倒れ、ガモーラは泣き出す。\n"
         "しかしそれは、すでにリアリティ・ストーンを手に入れていたサノスが見せた幻だった。本当のノーウェアは焼けて、こわれていた。",
         "The illusion on Knowhere",
         "On Knowhere, they find Thanos torturing the Collector for the stone's location. Gamora leaps at Thanos and stabs him. He falls, and she breaks down in tears.\n"
         "But it was an illusion: Thanos already had the Reality Stone. The real Knowhere is burned and in ruins."),
        ("泡の出る銃",
         "サノスは石の力で、ドラックスの体をばらばらの積み木のように、マンティスをリボンのように変えてしまう。そしてガモーラをつかまえる。\n"
         "ガモーラに、約束したはずだと言われ、クイルは泣きながら銃を撃つ。しかしリアリティ・ストーンの力で、銃からは泡しか出ない。サノスはガモーラを連れて消える。",
         "The bubble gun",
         "Using the stone, Thanos breaks Drax into blocks and turns Mantis into ribbons, then grabs Gamora.\n"
         "Reminded of his promise, Quill tearfully fires, but the Reality Stone turns his shots into bubbles. Thanos vanishes with Gamora."),
        ("ガモーラの子ども時代",
         "サノスの船で、サノスはガモーラと話す。ガモーラの故郷の星で、サノスは住む人の半分を殺し、幼いガモーラを連れ去って育てた。そのときサノスは、左右の重さがつり合ったナイフをガモーラに渡していた。\n"
         "サノスは、ガモーラの星の生き残りは今は豊かに暮らしていると言い、自分のしたことは正しかったと話す。",
         "Gamora's childhood",
         "Aboard his ship, Thanos talks with Gamora. On her home world, he killed half the people and took the young Gamora to raise. Back then, he gave her a perfectly balanced knife.\n"
         "He tells her the survivors on her world now live in plenty, and insists that what he did was right."),
        ("ネビュラの苦しみ",
         "ガモーラは、行方不明のソウル・ストーンの場所は知らないと言う。するとサノスは、とらえて痛めつけているネビュラのところへガモーラを連れていく。ネビュラは前にサノスを殺そうとして捕まっていた。\n"
         "サノスは、ネビュラの記憶から、ガモーラがソウル・ストーンを見つけたことを知っていた。妹が苦しむのを見ていられず、ガモーラは、石は惑星ヴォーミアにあると話してしまう。",
         "Nebula's torment",
         "Gamora claims she doesn't know where the lost Soul Stone is. So Thanos takes her to Nebula, captured earlier when she tried to kill him and now being tortured.\n"
         "From Nebula's memories, Thanos knows Gamora found the Soul Stone. Unable to watch her sister suffer, Gamora reveals it is on the planet Vormir."),
        ("ヴォーミアの崖",
         "サノスとガモーラは、霧に包まれた星ヴォーミアの山の上へ行く。そこには、石の番人となったレッド・スカルがいた。番人は、この石を手に入れるには愛する者の命を差し出さなければならないと告げる。\n"
         "ガモーラは、サノスは誰も愛していないと笑う。しかしサノスは涙を流していた。ガモーラは自分のナイフで死のうとするが、ナイフは泡に変わる。\n"
         "サノスはガモーラを崖から突き落とし、ガモーラは死ぬ。サノスはオレンジ色のソウル・ストーンを手に入れる。",
         "The cliff on Vormir",
         "Thanos and Gamora climb to a mountaintop on the misty planet Vormir. The Red Skull, now the stone's keeper, tells them the Soul Stone can only be had by sacrificing someone you love.\n"
         "Gamora laughs that Thanos loves no one, but he is weeping. She tries to kill herself with her knife, but it turns to bubbles.\n"
         "Thanos throws Gamora off the cliff and she dies. He receives the orange Soul Stone."),
        ("ネビュラの脱出",
         "サノスがいない間に、ネビュラはサノスの船から逃げ出す。そしてマンティスたちに連絡し、サノスの故郷の星タイタンで会おうと伝える。",
         "Nebula escapes",
         "While Thanos is away, Nebula escapes his ship and contacts Mantis and the others, telling them to meet her on Titan, Thanos's home world."),
    ]),
    ("第4部 地球のアベンジャーズ", "Part 4: The Avengers on Earth", [
        ("エディンバラの2人",
         "スコットランドのエディンバラで、ワンダとヴィジョンはひそかに一緒に暮らしている。ヴィジョンは人間の姿に見えるようにして、ワンダと、このまま一緒にいたいと話す。\n"
         "テレビには、ニューヨークの襲撃のニュースが流れている。ヴィジョンは額の石が何かを感じていると話す。",
         "Together in Edinburgh",
         "In Edinburgh, Scotland, Wanda and Vision are secretly living together. Vision, disguised as a human, talks with her about staying together.\n"
         "News of the New York attack is on TV, and Vision says the stone in his head is sensing something."),
        ("夜の襲撃",
         "夜の街で、コーヴァス・グレイヴがヴィジョンを槍で刺す。この槍の力で、ヴィジョンは体を自由に変えられなくなり、弱っていく。\n"
         "プロキシマ・ミッドナイトとコーヴァスは、ヴィジョンの額から石を抜き取ろうとする。ワンダは力で2人と戦うが、追いつめられる。",
         "The night attack",
         "On the city streets at night, Corvus Glaive stabs Vision with his glaive. The weapon disrupts Vision's powers, and he grows weaker.\n"
         "Proxima Midnight and Corvus try to pry the stone from Vision's forehead. Wanda fights them with her powers but is overwhelmed."),
        ("駅の助け",
         "駅で2人が追いつめられたとき、スティーブ、ナターシャ、サムが現れて、プロキシマとコーヴァスを追いはらう。3人はシビル・ウォーのあと、追われる身のまま世界を回っていた。\n"
         "傷ついたヴィジョンを連れて、一行は飛行機でアベンジャーズの本部へ向かう。",
         "Help at the station",
         "At a train station, Steve, Natasha and Sam arrive and drive off Proxima and Corvus. Since Civil War, the three have been living as fugitives.\n"
         "They take the wounded Vision and fly to the Avengers compound."),
        ("ローディとロス長官",
         "本部では、ローディ（ウォーマシン）が、ロス長官と立体映像で話している。そこへスティーブたちが入ってくる。\n"
         "ロス長官は、お尋ね者たちを逮捕しろとローディに命じる。しかしローディはこれを聞かず、通信を切る。ブルースもナターシャと久しぶりに再会する。",
         "Rhodey and Secretary Ross",
         "At the compound, Rhodey (War Machine) is talking with Secretary Ross by hologram when Steve's group walks in.\n"
         "Ross orders Rhodey to arrest the fugitives. Rhodey refuses and cuts the call. Bruce also meets Natasha again after a long time."),
        ("命と石",
         "ヴィジョンは、石を壊せばサノスは集められないので、自分ごと石を壊してほしいとワンダに頼む。ワンダはそんなことはできないと断る。\n"
         "スティーブも、命を引きかえにはしないと言う。ブルースは、ヴィジョンを死なせずに石だけを取り出せるかもしれないが、すぐれた設備が要ると話す。スティーブは、心当たりがあると答える。",
         "A life and a stone",
         "Vision asks Wanda to destroy the stone, and him with it, so Thanos can't have it. Wanda refuses.\n"
         "Steve says they don't trade lives. Bruce says it might be possible to remove the stone without killing Vision, but it would take advanced technology. Steve knows a place."),
        ("ワカンダへ",
         "一行はワカンダへ飛ぶ。国王ティ・チャラが迎え、バッキーには新しい義手が渡される。\n"
         "ティ・チャラの妹シュリがヴィジョンを調べ、石を取り出す作業を始める。ただし、終わるまでには時間がかかる。ワンダは作業のそばで見守る役になる。",
         "To Wakanda",
         "They fly to Wakanda. King T'Challa welcomes them, and Bucky is given a new arm.\n"
         "T'Challa's sister Shuri examines Vision and starts work on removing the stone, but it will take time. Wanda stays nearby to guard the work."),
    ]),
    ("第5部 宇宙の3つの場所", "Part 5: Three places in space", [
        ("ロケットとソー",
         "小さな船の中で、ロケットはソーに作り物の目を渡し、ソーはそれを、前の戦いで失った目のところにはめる。\n"
         "ソーは、父も母も兄も親友も失ったことを話しながら、それでもサノスを倒すと言う。",
         "Rocket and Thor",
         "In the pod, Rocket gives Thor an artificial eye, and Thor puts it in to replace the one he lost in his last battle.\n"
         "Thor talks about losing his father, mother, brother and best friend, but says he will still take down Thanos."),
        ("マウの船で",
         "マウの船の中で、マウは針を使ってストレンジを痛めつけ、タイム・ストーンの魔法を解かせようとする。ストレンジは耐え続ける。\n"
         "トニーとピーターは船の中に隠れている。ピーターが昔の映画を思い出して考えた作戦で、トニーが船の壁に穴を開ける。マウは穴から宇宙へ吸い出されて、凍りついて死ぬ。ピーターは、吸い出されかけたストレンジを助ける。",
         "On Maw's ship",
         "Aboard his ship, Maw tortures Strange with needles to make him undo the Time Stone's spell. Strange holds out.\n"
         "Tony and Peter are hiding aboard. Using a plan Peter takes from an old movie, Tony blasts a hole in the hull. Maw is sucked out into space and freezes to death. Peter saves Strange from being sucked out too."),
        ("トニーの決断",
         "トニーは地球に戻らず、このままサノスのところへ乗りこむと決める。そしてピーターを、アベンジャーズの一員として認める。\n"
         "ストレンジは、もしトニーとピーターの命か石かを選ぶことになったら、石を守ると言い切る。",
         "Tony's decision",
         "Tony decides not to go home but to take the fight to Thanos, and he accepts Peter as an Avenger.\n"
         "Strange warns that if it comes down to their lives or the stone, he will protect the stone."),
        ("止まった鍛冶場",
         "ソーたちはニダベリアに着く。しかし星を取り囲む大きな鍛冶場の火は消えていた。そこには、大きな体の小人の王エイトリが1人だけ残っていた。\n"
         "エイトリは話す。サノスにおどされて、6つの石をはめるこてを作らされた。そのあとサノスは、ほかの小人たちを皆殺しにし、エイトリが二度と物を作れないよう両手を金属に変えてしまった。",
         "The dead forge",
         "Thor's group reaches Nidavellir, but the great forge around the star has gone dark. Only Eitri, the giant dwarf king, remains.\n"
         "Eitri tells them Thanos forced him to make the gauntlet for the six stones, then killed all the other dwarves and turned Eitri's hands to metal so he could never make anything again."),
        ("星の火を浴びる",
         "ソーは自分の力で鍛冶場の輪を回し直し、星の光を通す。しかし扉が引っかかって開かない。ソーは自分の体で扉を押さえ、星の火を直接浴び続ける。\n"
         "ソーは倒れて死にかけるが、型の中に、斧の形の新しい武器ストームブレイカーができる。",
         "Taking the star's fire",
         "Thor restarts the forge's rings himself to let the star's light through, but a shutter jams. He holds it open with his own body and takes the full blast of the star.\n"
         "Thor collapses near death, but in the mold, a new axe-shaped weapon, Stormbreaker, has formed."),
        ("グルートの腕",
         "ストームブレイカーには、持ち手がまだない。グルートが自分の腕を伸ばし、それを切って持ち手にする。\n"
         "ソーがストームブレイカーを手に取ると、力がよみがえる。ストームブレイカーで、ソーは虹の橋を呼び出せるようになる。",
         "Groot's arm",
         "Stormbreaker still has no handle. Groot grows out his own arm and cuts it off to make one.\n"
         "When Thor grips Stormbreaker, his strength returns. With it, he can summon the Bifrost."),
    ]),
    ("第6部 タイタンの戦い", "Part 6: The battle on Titan", [
        ("タイタンの出会い",
         "トニー、ピーター、ストレンジを乗せた船は、こわれた星タイタンに落ちる。そこで3人は、ネビュラの連絡で来ていたクイル、ドラックス、マンティスと出会う。\n"
         "初めはおたがいをサノスの仲間だと思って戦いかけるが、どちらもサノスと戦うつもりだと分かる。",
         "Meeting on Titan",
         "The ship carrying Tony, Peter and Strange crashes on the ruined planet Titan. There they meet Quill, Drax and Mantis, who came at Nebula's call.\n"
         "At first each side thinks the other works for Thanos, but they realize they're both there to fight him."),
        ("1400万605通りの未来",
         "ストレンジはタイム・ストーンで、先に起こりうる未来をのぞく。見た未来は1400万605通り。その中で勝てる未来は、たった1つだけだった。\n"
         "トニーたちは、サノスを押さえつけて、こてを外す作戦を立てる。",
         "14,000,605 futures",
         "Strange uses the Time Stone to look at possible futures. He sees 14,000,605 of them, and they win in only one.\n"
         "Tony's group plans to pin Thanos down and pull off the gauntlet."),
        ("サノスの故郷",
         "サノスがスペース・ストーンで現れる。サノスはストレンジに、タイタンがかつて美しい星だったことを見せる。\n"
         "人が増えすぎて食べ物が足りなくなったとき、サノスは、住む人の半分を無作為に消せば星は救われると訴えた。しかし受け入れられず、星はほろびた。だから宇宙全体の命の半分を消す、とサノスは話す。",
         "Thanos's home world",
         "Thanos appears using the Space Stone. He shows Strange how beautiful Titan once was.\n"
         "When it grew overcrowded and food ran short, Thanos proposed wiping out half its people at random to save it. They refused, and the planet died. That is why, he says, he will wipe out half of all life in the universe."),
        ("みんなでの戦い",
         "トニーたちは次々にサノスに攻めかかる。サノスは石の力で、こわれた月のかけらを雨のように降らせる。\n"
         "そこへネビュラが船で飛びこんできて、サノスにぶつける。ネビュラもサノスに斬りかかる。",
         "Everyone attacks",
         "Tony's group attacks Thanos one after another. Thanos uses the stones to rain down pieces of a shattered moon.\n"
         "Nebula then rams her ship into Thanos and joins the attack."),
        ("あと一歩",
         "ヒーローたちはサノスを押さえこみ、マンティスが力でサノスをぼんやりさせる。トニーとピーターが、こてを少しずつ引き抜いていく。\n"
         "クイルがガモーラの居場所をたずねる。ネビュラの言葉と、サノスの心を読んだマンティスの様子から、ガモーラが殺されたと分かる。",
         "So close",
         "The heroes pin Thanos down, and Mantis puts him in a daze. Tony and Peter begin working the gauntlet off his hand.\n"
         "Quill asks where Gamora is. From Nebula's words and what Mantis senses in Thanos's mind, he learns Gamora is dead."),
        ("クイルの怒り",
         "怒ったクイルはサノスをなぐり続ける。そのせいでサノスは目を覚まし、こてを取り戻してしまう。\n"
         "サノスは1人ずつヒーローたちを倒していく。ストレンジも魔法で戦うが、敗れる。",
         "Quill's rage",
         "Enraged, Quill keeps hitting Thanos, and Thanos snaps out of the daze and gets the gauntlet back.\n"
         "Thanos beats the heroes one by one. Strange fights with magic but is defeated."),
        ("ストレンジの取り引き",
         "トニーはただ1人でサノスと戦うが、サノスに刃で腹を刺される。サノスがとどめを刺そうとしたとき、ストレンジが、トニーの命を助けてくれれば石を渡すと言う。\n"
         "ストレンジはタイム・ストーンをサノスに渡す。サノスは5つ目の石をこてにはめ、地球へ消える。",
         "Strange's bargain",
         "Tony fights Thanos alone and is stabbed through the side with a blade. As Thanos moves to finish him, Strange offers the stone if he spares Tony's life.\n"
         "Strange hands Thanos the Time Stone. Thanos sets the fifth stone in the gauntlet and vanishes to Earth."),
    ]),
    ("第7部 ワカンダの戦い", "Part 7: The battle of Wakanda", [
        ("大軍がやってくる",
         "サノスの手下たちの船が、ワカンダの国を守る見えない壁の外に落ちてくる。中から、たくさんの怪物の兵（アウトライダー）があふれ出す。\n"
         "ティ・チャラ、スティーブ、ナターシャ、バッキー、サム、ローディ、ハルクバスター（大型のスーツ）に乗ったブルース、オコエたちワカンダの戦士、山の部族のエムバクが、壁の前に並ぶ。ティ・チャラは「ワカンダ・フォーエバー」と叫ぶ。",
         "The army arrives",
         "Ships from Thanos's lieutenants crash outside the invisible barrier that protects Wakanda, and hordes of monstrous Outriders pour out.\n"
         "T'Challa, Steve, Natasha, Bucky, Sam, Rhodey, Bruce in the Hulkbuster armor, Okoye and the Wakandan warriors, and M'Baku of the mountain tribe line up before the barrier. T'Challa cries, \"Wakanda forever!\""),
        ("壁を開く",
         "怪物たちは壁にぶつかり、回りこもうとする。ヴィジョンのいる場所を守るため、ティ・チャラの合図で壁の一部をわざと開き、怪物を1か所に集めて戦う。\n"
         "数が多すぎて、ヒーローたちは少しずつ押されていく。",
         "Opening the barrier",
         "The Outriders throw themselves at the barrier and try to go around it. To protect the place where Vision is, T'Challa orders them to deliberately open part of the barrier and funnel the creatures to one spot.\n"
         "There are too many, and the heroes are slowly pushed back."),
        ("ソーの到着",
         "負けそうになったそのとき、虹の橋とともにソーがストームブレイカーを持って降り立ち、怪物たちを一気に倒す。ロケットとグルートも一緒だった。\n"
         "ブルースは、久しぶりに会ったソーを見て喜ぶ。",
         "Thor arrives",
         "Just as they're about to fall, Thor lands on the Bifrost with Stormbreaker and wipes out a mass of Outriders. Rocket and Groot are with him.\n"
         "Bruce is overjoyed to see Thor again."),
        ("カル・オブシディアンの最期",
         "カル・オブシディアンは、ハルクバスターに乗ったブルースと戦う。ブルースはオブシディアンをつかんだままロケットで飛び、国を守る壁にたたきつける。オブシディアンは壁の力で体が吹き飛び、死ぬ。",
         "Cull Obsidian's end",
         "Cull Obsidian fights Bruce in the Hulkbuster. Bruce grabs him, rockets them both into the barrier, and Obsidian is blown apart by its energy and dies."),
        ("プロキシマの最期",
         "ヴィジョンのそばにいたワンダも、戦いに加わる。プロキシマ・ミッドナイトは、ナターシャとオコエと戦っていた。\n"
         "ワンダは力でプロキシマを持ち上げ、回転する刃の機械（サノスの軍の兵器）の前へ投げとばす。プロキシマは刃に巻きこまれて死ぬ。",
         "Proxima's end",
         "Wanda, who had been guarding Vision, joins the fight. Proxima Midnight is battling Natasha and Okoye.\n"
         "Wanda lifts Proxima with her powers and throws her into the path of one of the army's spinning-blade machines. Proxima is caught in the blades and dies."),
        ("コーヴァスの最期",
         "ワンダがいなくなったすきに、コーヴァス・グレイヴがシュリの研究所に入りこむ。シュリの作業は止まり、ヴィジョンは起き上がってコーヴァスと戦う。\n"
         "ヴィジョンは研究所の外へ落ちて追いつめられるが、スティーブが助けに入る。ヴィジョンはコーヴァスの槍をうばい、それでコーヴァスを刺して殺す。",
         "Corvus's end",
         "With Wanda gone, Corvus Glaive slips into Shuri's lab. Shuri's work is interrupted, and Vision gets up to fight him.\n"
         "Vision falls out of the lab and is cornered, but Steve steps in. Vision takes Corvus's own glaive and kills him with it."),
        ("サノスが来る",
         "空気が変わり、サノスが魔法の出入り口のように開いた空間から現れる。ヒーローたちは次々にサノスに向かっていくが、サノスはスティーブも、ブルースも、ティ・チャラも、石の力で簡単に退ける。\n"
         "スティーブは素手でこてを押さえこむが、サノスになぐり倒される。",
         "Thanos arrives",
         "The air shifts and Thanos steps out of a rift in space. The heroes charge him one after another, but with the stones he easily throws off Steve, Bruce, T'Challa and the rest.\n"
         "Steve holds back the gauntlet with his bare hands, but Thanos punches him down."),
        ("ワンダの涙",
         "ヴィジョンはワンダに、今しかないから石を壊してくれと頼む。ワンダは泣きながら、片手でサノスを止め、もう片方の手でヴィジョンの額の石に力を注ぐ。\n"
         "石は砕け、ヴィジョンは光とともに倒れて死ぬ。サノスは、お前の気持ちは分かるとワンダに言う。",
         "Wanda's tears",
         "Vision begs Wanda to destroy the stone now. Weeping, she holds Thanos back with one hand and pours her power into the stone with the other.\n"
         "The stone shatters, and Vision falls dead in a burst of light. Thanos tells Wanda he understands her pain."),
        ("巻き戻される時間",
         "しかしサノスはタイム・ストーンで時間を巻き戻す。石が元に戻り、ヴィジョンも生き返る。\n"
         "サノスはヴィジョンの額から石を引き抜く。ヴィジョンは色を失って倒れ、死ぬ。サノスは6つ目の石をこてにはめる。",
         "Time rewound",
         "But Thanos turns back time with the Time Stone. The stone is restored, and so is Vision.\n"
         "Thanos rips the stone from Vision's forehead. Vision turns gray, falls and dies. Thanos sets the sixth stone in the gauntlet."),
        ("頭をねらうべきだった",
         "6つの石の力があふれる中、ソーが飛んできて、ストームブレイカーをサノスの胸に突き刺す。\n"
         "サノスは大けがをしながら「頭を狙うべきだったな」と言う。そして指を鳴らす。",
         "\"You should have gone for the head\"",
         "As the power of all six stones surges, Thor flies in and drives Stormbreaker into Thanos's chest.\n"
         "Badly wounded, Thanos tells him he should have gone for the head, and snaps his fingers."),
    ]),
    ("第8部 消えていく人々", "Part 8: Those who vanish", [
        ("小さなガモーラ",
         "指を鳴らした瞬間、サノスは不思議な場所で、子どものころのガモーラに会う。ガモーラはやり終えたのかとたずね、サノスはやったと答える。何を失ったのかと聞かれ、サノスはすべてだと答える。\n"
         "我に返ったサノスは、こてが焼けこげた姿で、出入り口を開いて姿を消す。",
         "Young Gamora",
         "In the instant of the snap, Thanos finds himself in a strange place with Gamora as a child. She asks if he did it; he says yes. She asks what it cost; he answers, \"Everything.\"\n"
         "Back in the battlefield, the gauntlet scorched, Thanos opens a rift and disappears."),
        ("ワカンダで消える人々",
         "ソーが、サノスはどこへ行ったのかと叫ぶ。そのとき、バッキーがスティーブの名を呼びながら、ちりになって消える。\n"
         "続いて、オコエに声をかけたティ・チャラ、ロケットの前のグルート、ヴィジョンのそばにいたワンダ、そしてサムも、ちりになって消えていく。",
         "Vanishing in Wakanda",
         "Thor shouts, asking where Thanos went. Then Bucky, calling Steve's name, turns to dust.\n"
         "Next, T'Challa as he speaks to Okoye, Groot in front of Rocket, Wanda beside Vision, and Sam all crumble to dust."),
        ("タイタンで消える人々",
         "タイタンでは、マンティスが、何かが起きていると言って消え、ドラックス、クイルも消える。ストレンジはトニーに、これしか道はなかったと言い残して消える。\n"
         "最後に、ピーター・パーカーが、行きたくないと言いながらトニーの腕の中でちりになる。タイタンにはトニーとネビュラだけが残る。",
         "Vanishing on Titan",
         "On Titan, Mantis says something is happening and fades away, followed by Drax and Quill. Strange tells Tony there was no other way and vanishes.\n"
         "Last, Peter Parker, saying he doesn't want to go, crumbles to dust in Tony's arms. Only Tony and Nebula are left on Titan."),
        ("残された人々",
         "ワカンダの戦場には、スティーブ、ナターシャ、ソー、ブルース、ローディ、ロケット、オコエ、エムバクが残る。スティーブは、ヴィジョンの遺体のそばに座りこみ、ぼうぜんと声をもらす。",
         "Those left behind",
         "On the battlefield in Wakanda, Steve, Natasha, Thor, Bruce, Rhodey, Rocket, Okoye and M'Baku remain. Steve sinks down beside Vision's body and whispers, \"Oh, God.\""),
        ("朝日を見るサノス",
         "遠い星の静かな小屋で、サノスはけがをした体で座り、昇る朝日を見つめる。",
         "Thanos at sunrise",
         "In a quiet hut on a distant world, the wounded Thanos sits and watches the sun come up."),
        ("エンドクレジットの後",
         "地球の街で、ニック・フューリーとマリア・ヒルが車で走っている。まわりの車の運転手が消えて事故が起き、ヘリコプターがビルにぶつかる。\n"
         "ヒルがちりになって消える。フューリーは車から改造したポケベルを取り出し、誰かに合図を送りながら、ちりになって消える。落ちたポケベルの画面には、赤と青と金の星のマークが映る。",
         "After the credits",
         "In a city on Earth, Nick Fury and Maria Hill are driving when drivers around them vanish, cars crash and a helicopter hits a building.\n"
         "Hill turns to dust. Fury pulls out a modified pager and sends a signal before he too crumbles away. On the dropped pager's screen is a red, blue and gold star emblem."),
    ]),
    ("まとめ（結末までのネタバレ）", "Summary (spoilers through the ending)", [
        ("サノスが石を集めた順",
         "①パワー・ストーン（紫）：映画が始まる前に、惑星ザンダーから奪っていた。\n"
         "②スペース・ストーン（青）：アスガルドの船で、ロキが差し出したテッセラクトから取り出す（第1部）。\n"
         "③リアリティ・ストーン（赤）：ノーウェアで、コレクターから奪っていた（第3部）。\n"
         "④ソウル・ストーン（オレンジ）：ヴォーミアで、ガモーラの命と引きかえに手に入れる（第3部）。\n"
         "⑤タイム・ストーン（緑）：タイタンで、トニーの命を助けるかわりにストレンジが渡す（第6部）。\n"
         "⑥マインド・ストーン（黄）：ワカンダで、ワンダが一度壊したが、サノスが時間を巻き戻してヴィジョンの額から引き抜く（第7部）。",
         "The order Thanos got the stones",
         "1) Power (purple): taken from Xandar before the film begins.\n"
         "2) Space (blue): from the Tesseract Loki hands over on the Asgardian ship (Part 1).\n"
         "3) Reality (red): taken from the Collector on Knowhere (Part 3).\n"
         "4) Soul (orange): won on Vormir by sacrificing Gamora (Part 3).\n"
         "5) Time (green): handed over by Strange on Titan in exchange for Tony's life (Part 6).\n"
         "6) Mind (yellow): destroyed by Wanda in Wakanda, then restored when Thanos turns back time and rips it from Vision's forehead (Part 7)."),
        ("死んだ人たち（話の順に）",
         "・アスガルドの船の人々（第1部）：サノスたちに襲われる。\n"
         "・ヘイムダル（第1部）：ハルクを地球へ逃がしたため、サノスが手下の槍で刺す。\n"
         "・ロキ（第1部）：短剣でサノスを刺そうとして、首をしめられる。\n"
         "・ガモーラ（第3部）：ソウル・ストーンを手に入れるため、サノスがヴォーミアの崖から突き落とす。\n"
         "・エボニー・マウ（第5部）：トニーが船の壁に穴を開け、宇宙へ吸い出されて凍りつく。\n"
         "・カル・オブシディアン（第7部）：ハルクバスターのブルースが、ワカンダを守る壁にたたきつける。\n"
         "・プロキシマ・ミッドナイト（第7部）：ワンダが、回転する刃の機械の前へ投げとばす。\n"
         "・コーヴァス・グレイヴ（第7部）：ヴィジョンが、コーヴァス自身の槍で刺す。\n"
         "・ヴィジョン（第7部）：ワンダが本人の頼みで石を壊して一度死ぬが、サノスが時間を巻き戻し、石を引き抜いて殺す。\n"
         "（映画が始まる前に、ニダベリアの小人たちとザンダーの人々もサノスに襲われている。）",
         "Who died (in order)",
         "- People on the Asgardian ship (Part 1): attacked by Thanos's forces.\n"
         "- Heimdall (Part 1): Thanos stabs him with his lieutenant's spear for sending the Hulk to Earth.\n"
         "- Loki (Part 1): strangled after trying to stab Thanos with a dagger.\n"
         "- Gamora (Part 3): Thanos throws her off the cliff on Vormir to get the Soul Stone.\n"
         "- Ebony Maw (Part 5): sucked out into space through a hole Tony blasts in the hull, and frozen.\n"
         "- Cull Obsidian (Part 7): Bruce, in the Hulkbuster, slams him into Wakanda's barrier.\n"
         "- Proxima Midnight (Part 7): Wanda throws her into a spinning-blade machine.\n"
         "- Corvus Glaive (Part 7): Vision stabs him with his own glaive.\n"
         "- Vision (Part 7): Wanda destroys the stone at his request and he dies, but Thanos turns back time and kills him by ripping the stone out.\n"
         "(Before the film, Thanos had also attacked the dwarves of Nidavellir and the people of Xandar.)"),
        ("指パッチンで消えた人・残った人",
         "消えた人（主な人物）：バッキー、ティ・チャラ、グルート、ワンダ、サム、マンティス、ドラックス、クイル、ストレンジ、ピーター・パーカー、マリア・ヒル、ニック・フューリー。宇宙のすべての命の半分が消えた。\n"
         "残った人：タイタンにトニーとネビュラ。ワカンダにスティーブ、ナターシャ、ソー、ブルース、ローディ、ロケット、オコエ、エムバク。",
         "Who vanished in the snap, and who was left",
         "Vanished (main characters): Bucky, T'Challa, Groot, Wanda, Sam, Mantis, Drax, Quill, Strange, Peter Parker, Maria Hill and Nick Fury. Half of all life in the universe was gone.\n"
         "Left: Tony and Nebula on Titan; Steve, Natasha, Thor, Bruce, Rhodey, Rocket, Okoye and M'Baku in Wakanda."),
    ]),
]
