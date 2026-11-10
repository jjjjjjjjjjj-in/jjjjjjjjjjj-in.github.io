# 『スパイダーマン：ホームカミング』（2017年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじと、検索で見つかった解説記事で事実を確かめた。
# 資料どうしで食い違う所や、確かめられない細かい所（倉庫からどうやって抜け出したか、
# ネッドがどうやってトゥームスの居場所を調べたか、ショッカーをどう倒したかのくわしい流れなど）は書いていない。
# 冒頭の「8年後」の字幕は、公式の年表の本が誤りとしているので、年数は書いていない。
# 日本語版のせりふは、日本語版ウィキペディアにあるものだけ短く引用し、ほかは内容だけ書いた。
# 人物名は相関図（relations.py）にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 がれきの後片づけ", "Part 1: Cleaning up the wreckage", [
        ("奪われた仕事",
         "2012年、ニューヨークの戦いのすぐ後。エイドリアン・トゥームスは、自分の会社の作業員たちと、宇宙人チタウリとの戦いで壊れた街のがれきを片づける仕事を引き受けていた。家族と部下の生活をかけて、トラックや人をそろえたばかりだった。\n"
         "そこへ、トニー・スタークと政府が一緒に作った組織「ダメージ・コントロール」がやってきて、ここからは自分たちが引き受けると告げる。トゥームスは抗議するが聞き入れられず、仕事を取り上げられてしまう。",
         "A job taken away",
         "2012, right after the Battle of New York. Adrian Toomes and his salvage crew have a contract to clear the wreckage left by the fight with the alien Chitauri. He has just invested in trucks and workers, staking his family's and his crew's livelihoods on it.\n"
         "Then the Department of Damage Control, a partnership between Tony Stark and the government, arrives and takes over the job. Toomes protests, gets nowhere, and is pushed out."),
        ("残しておいた宇宙の部品",
         "腹を立てたトゥームスは、すでに集めて手元に残っていたチタウリの部品を、政府に渡さないことにする。部下たちを説得して、その技術で強力な武器を作り、こっそり売ってもうけようと決める。",
         "The salvage they kept",
         "Furious, Toomes decides not to hand over the Chitauri tech his crew has already collected. He talks his workers into using it to build powerful weapons and sell them on the quiet."),
        ("翼のスーツ",
         "時がたち、トゥームスたちの武器の商売は続いていた。トゥームスは機械の翼をつけたスーツ（バルチャー）で空を飛び、ダメージ・コントロールの荷物から、武器の動力になるチタウリのエネルギー源を盗み出していた。",
         "The wing suit",
         "Time passes, and Toomes's weapons business keeps going. He now flies in a suit with mechanical wings, the Vulture, stealing Chitauri power cells from Damage Control shipments to run the weapons."),
    ]),
    ("第2部 ピーターのビデオ", "Part 2: Peter's video", [
        ("ドイツへの旅",
         "物語は、クイーンズに住む15歳の高校生ピーター・パーカーがスマホで撮った動画から始まる。トニーの運転手ハッピー・ホーガンが迎えに来て、ピーターは飛行機でドイツへ向かい、ホテルに泊まる。何もかも初めてのピーターは、はしゃぎながら撮り続ける。",
         "The trip to Germany",
         "The film opens with phone videos shot by Peter Parker, a 15-year-old high-schooler from Queens. Tony's driver, Happy Hogan, picks him up, and Peter flies to Germany and checks into a hotel. It's all new to him, and he films everything, giddy."),
        ("空港の戦い",
         "ピーターは、アベンジャーズどうしの争い（『シビル・ウォー』の空港の戦い）に、トニーの側で加わる。動画には、その戦いをピーターの目から見た様子が映っている。",
         "The airport fight",
         "Peter joins the fight between the Avengers, from Civil War, on Tony's side. His videos show the airport battle from his point of view."),
        ("「連絡を待て」",
         "戦いが終わると、ピーターは車でクイーンズへ送り返される。周りには「スターク社のインターンシップ」に行ったことにしてある。トニーは、新しいスーツをそのまま持っていてよいと言い、次の仕事はこちらから連絡すると伝える。ピーターは、すぐにアベンジャーズとして呼ばれると信じこむ。",
         "\"We'll call you\"",
         "After the fight, Peter is driven back to Queens. The cover story is that he was at a \"Stark Internship.\" Tony lets him keep the new suit and says they'll be in touch about the next job. Peter is sure he'll be called up as an Avenger any day."),
    ]),
    ("第3部 近所のパトロール", "Part 3: Neighborhood patrols", [
        ("ミッドタウン高校の毎日",
         "それから2か月。ピーターは、科学の得意な生徒が集まるミッドタウン高校に通っている。親友はネッド・リーズで、同級生のフラッシュにはいつもからかわれている。\n"
         "ピーターは、学業コンテスト（アカデミック・デカスロン）のチームに入っていて、チームのリーダーは、ピーターが片思いしている上級生のリズだった。しかしピーターは、スパイダーマンの活動を優先して、練習を途中で抜け出し、やがてチームをやめてしまう。",
         "Life at Midtown",
         "Two months later. Peter attends Midtown School of Science and Technology. His best friend is Ned Leeds, and classmate Flash never stops picking on him.\n"
         "Peter is on the academic decathlon team, led by Liz, the senior he has a crush on. But putting Spider-Man first, he keeps ducking out of practice, and eventually quits the team."),
        ("親愛なる隣人",
         "放課後、ピーターは路地でスーツに着がえ、近所を見回る。自転車泥棒を捕まえたり、おばあさんに道を教えてお礼に揚げ菓子をもらったりする。車を盗もうとしている男を止めたら、実は自分の車に入ろうとしていた持ち主で、近所の人たちにどなられることもあった。",
         "Friendly neighborhood",
         "After school, Peter changes in an alley and patrols the neighborhood. He catches a bike thief and gives an old woman directions, getting a churro for his trouble. Once he stops a man breaking into a car, only to learn it's the man's own car, and gets yelled at by the neighbors."),
        ("返事のない報告",
         "ピーターは毎晩のように、ハッピーに留守番電話やメッセージで、その日の活動を報告する。早く次の任務がほしいと伝えるが、ハッピーからはほとんど返事が来ない。",
         "Reports with no reply",
         "Night after night, Peter leaves Happy voicemails and messages reporting the day's patrol and asking for his next mission. Happy almost never answers."),
        ("ATM強盗",
         "ある日ピーターは、アベンジャーズのお面をかぶった強盗たちが、銀行のATMをこじ開けているところを見つける。彼らは見たこともない強力な武器を持っていた。\n"
         "ピーターは強盗たちを止めるが、武器から出た光線が通りの向かいのサンドイッチ店（デルマーの店）を吹き飛ばしてしまう。ピーターは、燃える店の中から店の主人を助け出す。",
         "The ATM robbery",
         "One day Peter spots robbers in Avengers masks breaking into a bank ATM. They're carrying powerful weapons unlike anything he's seen.\n"
         "Peter stops them, but a blast from one weapon blows up Delmar's sandwich shop across the street. He pulls the owner out of the burning shop."),
        ("ネッドにばれる",
         "その夜、ピーターが天井をつたって自分の部屋に戻ると、そこには遊びに来ていたネッドが座っていた。スーツ姿のピーターを見たネッドは、手に持っていたレゴの作品を落としてしまう。こうして親友に正体を知られる。",
         "Ned finds out",
         "That night, Peter crawls into his room across the ceiling and finds Ned sitting there, waiting for him. Seeing Peter in the suit, Ned drops the Lego model he's holding. Now his best friend knows."),
    ]),
    ("第4部 リズのパーティー", "Part 4: Liz's party", [
        ("ネッドの口すべり",
         "次の日、ネッドは正体のことで質問ぜめにする。学校では、リズたちの前で、ピーターはスパイダーマンと知り合いだとつい口をすべらせてしまう。リズは週末に自分の家で開くパーティーにピーターを誘い、スパイダーマンも連れてきてほしいと言う。",
         "Ned lets it slip",
         "The next day, Ned peppers Peter with questions. At school, in front of Liz and others, he blurts out that Peter knows Spider-Man. Liz invites Peter to her party that weekend and asks him to bring Spider-Man along."),
        ("光を見つける",
         "パーティーで、ピーターはスパイダーマンとして登場するつもりでスーツを着るが、ためらってしまう。そのとき遠くで、武器の光がひらめくのを見つけ、パーティーを抜け出してそちらへ向かう。",
         "A flash in the distance",
         "At the party, Peter suits up meaning to show up as Spider-Man, but loses his nerve. Then he sees a weapon's flash in the distance, and slips away to check it out."),
        ("高架下の取り引き",
         "高架の下では、トゥームスの部下ジャクソン・ブライス（ショッカー）とハーマン・シュルツが、地元の犯罪者アーロン・デイビスに武器を売っていた。\n"
         "ピーターが割って入ると、ブライスたちはデイビスを置いてバンで逃げる。ピーターはデイビスを助けたあと、家々の庭をこえてバンを追いかける。",
         "The deal under the overpass",
         "Under an overpass, Toomes's men Jackson Brice, the Shocker, and Herman Schultz are selling weapons to a local criminal, Aaron Davis.\n"
         "When Peter crashes the deal, Brice and Schultz flee in their van, leaving Davis behind. After saving Davis, Peter chases the van across backyards."),
        ("湖に落とされる",
         "追いかけるピーターを、空から現れたバルチャーことトゥームスがつかみ、高い空から湖に落とす。スーツのパラシュートが体にからまり、ピーターはおぼれかける。\n"
         "そこへ、トニーが遠くから操るアイアンマンのスーツが飛んできて、ピーターを引き上げる。",
         "Dropped into a lake",
         "The Vulture swoops down, grabs Peter and drops him from high in the sky into a lake. Tangled in his suit's parachute, Peter nearly drowns.\n"
         "An Iron Man suit, flown remotely by Tony, arrives and pulls him out."),
        ("トニーの警告",
         "トニーは、スーツに入れておいた仕組みでピーターの様子を見ていたと明かす。そして、こんな危ない相手には関わるな、近所の小さな事件を守っていればいいと言い聞かせる。ピーターは不満をつのらせる。",
         "Tony's warning",
         "Tony reveals he's been keeping tabs on Peter through the suit. He tells him to stay away from people this dangerous and stick to small, street-level crime. Peter is left fuming."),
        ("ブライスの死",
         "トゥームスの隠れ家。取り引きを台なしにしたうえ、目立つ武器を使ったブライスに、トゥームスは仲間から外すと告げる。ブライスは、トゥームスの家族に秘密をばらすとほのめかす。\n"
         "怒ったトゥームスは、反重力の銃のつもりで、別の武器を手に取ってブライスを撃ってしまう。ブライスは灰のようになって消える。トゥームスは、ショッカーの武器（手につける装置）をシュルツに渡し、シュルツが新しいショッカーになる。",
         "Brice dies",
         "At Toomes's hideout, he tells Brice he's out, for botching the deal and using such flashy weapons. Brice hints he might tell Toomes's family what Toomes really does.\n"
         "Angry, Toomes grabs what he thinks is an anti-gravity gun, but it's a different weapon, and he shoots Brice, who crumbles to dust. Toomes hands the Shocker gauntlet to Schultz, who becomes the new Shocker."),
    ]),
    ("第5部 ワシントンへ", "Part 5: Washington", [
        ("光る部品",
         "ピーターとネッドは、ブライスたちが落としていった武器を学校の実験室で調べ、中から紫色に光る動力の部品を取り出す。\n"
         "そこへ、部品を探しにトゥームスの部下たちが学校の近くまでやって来る。ピーターは、彼らの1人（シュルツ）に小さな発信器をつけることに成功する。",
         "The glowing core",
         "In the school lab, Peter and Ned study the weapon Brice's crew left behind and remove its glowing purple power core.\n"
         "Toomes's men come looking for it near the school. Peter manages to stick a tiny tracker on one of them, Schultz."),
        ("チームに戻る",
         "発信器はシュルツがメリーランド州へ向かうことを示していた。ちょうどデカスロンのチームが、全国大会のためワシントンD.C.へ行くことになっていたので、ピーターはチームに戻って一緒に行くことにする。リズは喜ぶ。",
         "Back on the team",
         "The tracker shows Schultz heading to Maryland. The decathlon team happens to be going to Washington, D.C., for nationals, so Peter rejoins to tag along. Liz is glad to have him back."),
        ("カレン",
         "ワシントンのホテルで、ネッドはピーターのスーツを調べ、トニーがしかけた追跡の仕組みを止め、機能を制限していた「訓練用の設定」も外してしまう。\n"
         "するとスーツに入っていた人工知能が話しかけてくる。ピーターはその声に「カレン」と名前をつける。スーツには、トニーが隠していたたくさんの機能があった。",
         "Karen",
         "At the hotel in Washington, Ned hacks the suit, disabling the tracker Tony planted and removing the \"Training Wheels Protocol\" that limited it.\n"
         "The AI inside the suit starts talking to Peter, and he names her Karen. The suit has hundreds of features Tony kept hidden."),
        ("トラックの中に閉じこめられる",
         "その夜、ピーターはホテルを抜け出し、メリーランドでトゥームスたちがダメージ・コントロールのトラックから武器を盗むのを止めようとする。\n"
         "盗みは止められたが、ピーターはトラックごとダメージ・コントロールの倉庫に運ばれ、一晩じゅう閉じこめられてしまう。そのせいで次の日の大会にも出られない。ミッドタウン高校のチームは、ピーター抜きで優勝する。",
         "Trapped in the truck",
         "That night, Peter sneaks out of the hotel to stop Toomes's crew stealing weapons from a Damage Control truck in Maryland.\n"
         "He stops the theft, but the truck carries him into a Damage Control vault, where he's locked in all night, missing the next day's competition. The Midtown team wins without him."),
        ("部品の正体",
         "倉庫の中で、カレンが調べると、ネッドが持っている紫色の部品は、不安定なチタウリの爆弾だとわかる。ピーターは倉庫から抜け出し、仲間たちのいるワシントン記念塔へ急ぐ。",
         "What the core really is",
         "Inside the vault, Karen identifies the purple core Ned has been carrying: an unstable Chitauri grenade. Peter gets out and races to the Washington Monument, where his teammates are."),
        ("記念塔の爆発",
         "優勝のお祝いに記念塔を見学していたチーム。入口の荷物検査でX線を当てられた部品が動き出し、塔の中で爆発する。エレベーターが壊れ、ネッド、リズ、ミシェルたちが中に閉じこめられ、今にも落ちそうになる。",
         "The blast in the monument",
         "The team is touring the monument to celebrate. The X-ray at the bag check sets the core off, and it explodes inside. The elevator is wrecked, trapping Ned, Liz, Michelle and others, and threatening to fall."),
        ("塔をよじ登る",
         "ワシントンには糸をかける高い建物がほとんどなく、ピーターは必死に走って塔にたどりつく。塔の外側をよじ登り、窓を割って中に入る。\n"
         "エレベーターが落ち始めるところを糸で支え、みんなを引き上げる。最後にすべり落ちかけたリズも、ぎりぎりでつかんで助ける。",
         "Climbing the monument",
         "With few tall buildings to swing from, Peter has to sprint to the monument. He climbs the outside, smashes through a window and gets in.\n"
         "As the elevator starts to drop, he holds it with his webs and pulls everyone out, catching Liz at the last second when she slips."),
    ]),
    ("第6部 フェリーの大事故", "Part 6: The ferry disaster", [
        ("デイビスを問いつめる",
         "ニューヨークに戻ったピーターは、スパイダーマンが友だちを救ったと学校で話題になったことに気をよくする。そして今度こそバルチャーを捕まえようと、駐車場でデイビスを問いつめる。\n"
         "スーツの尋問用の機能を使っても格好はつかなかったが、デイビスは、次の取り引きがスタテン島へ向かうフェリーの上で行われると教えてくれる。",
         "Questioning Davis",
         "Back in New York, Peter enjoys the buzz at school about Spider-Man saving his friends. Determined to catch the Vulture this time, he corners Davis in a parking garage.\n"
         "The suit's interrogation mode doesn't make him look very tough, but Davis tells him the next deal will happen on the Staten Island Ferry."),
        ("フェリーの上の取り引き",
         "フェリーの上で、トゥームスの部下たちは新しい買い手マック・ガーガンに武器を売ろうとしていた。ピーターは取り引きに飛びこみ、ガーガンを捕まえる。トゥームスもバルチャーのスーツで現れる。",
         "The deal on the ferry",
         "On the ferry, Toomes's men are selling weapons to a new buyer, Mac Gargan. Peter bursts in and catches Gargan. Toomes shows up in the Vulture suit."),
        ("真っ二つになったフェリー",
         "戦いの中で武器の1つが暴走し、光線がフェリーを縦に切り裂く。トゥームスは逃げてしまう。\n"
         "ピーターは、たくさんの糸で割れた船体をつなぎとめようとするが、支えきれない。そこへアイアンマンのトニーが駆けつけ、船を元どおりにつなぎ合わせて、乗客を救う。",
         "The ferry split in two",
         "In the fight, one of the weapons goes haywire and its beam slices the ferry down the middle. Toomes gets away.\n"
         "Peter tries to hold the two halves together with webbing, but it isn't enough. Tony arrives as Iron Man, fixes the ship back together and saves the passengers."),
        ("取り上げられたスーツ",
         "トニーは、ピーターの話を受けてすでにFBIに知らせ、取り引きの現場をおさえる準備をしていたと明かす。ピーターの勝手な行動が、それを台なしにし、大勢の命を危険にさらしたのだった。\n"
         "トニーはピーターからスーツを取り上げる。スーツがなければ自分には何もないと言うピーターに、トニーは、それならなおさらスーツを持つべきではないと答える。",
         "The suit taken away",
         "Tony reveals he'd already tipped off the FBI after hearing Peter out, and they were about to take down the deal. Peter's going it alone ruined that and put many lives at risk.\n"
         "Tony takes the suit back. When Peter says he's nothing without it, Tony replies that if that's so, then he shouldn't have it."),
    ]),
    ("第7部 ホームカミングの夜", "Part 7: Homecoming night", [
        ("ふつうの高校生",
         "スーツを失ったピーターは、学校生活に戻ることにする。勇気を出して、学校のダンスパーティー（ホームカミング）にリズを誘うと、リズは受けてくれる。",
         "An ordinary teenager",
         "Without the suit, Peter goes back to being a regular student. He works up the courage to ask Liz to the homecoming dance, and she says yes."),
        ("ドアを開けた男",
         "パーティーの夜、ピーターはリズの家に迎えに行く。ドアを開けたのは、リズの父親、トゥームスだった。バルチャーの正体がリズの父だと知り、ピーターは動揺する。",
         "The man at the door",
         "On the night of the dance, Peter goes to pick up Liz. The man who opens the door is her father, Toomes. Realizing the Vulture is Liz's dad, Peter is shaken."),
        ("車の中のおどし",
         "トゥームスは2人を車で会場へ送る。リズは、ピーターが大会のときやパーティーの夜にいなくなったことを話し、ワシントンでスパイダーマンに助けられたことも話す。トゥームスは、ピーターのようすとその話から、彼がスパイダーマンだと気づく。\n"
         "会場に着くと、トゥームスはリズを先に降ろし、ピーターだけを車に残す。娘の命を救ってくれたことには感謝するが、これ以上じゃまをしたら、ピーターと大切な人たちをみんな殺すと静かにおどす。",
         "The threat in the car",
         "Toomes drives them to the dance. Liz talks about Peter vanishing at nationals and at her party, and about Spider-Man saving them in Washington. From that, and from Peter's nerves, Toomes works out that Peter is Spider-Man.\n"
         "At the school, he lets Liz out first and keeps Peter in the car. He thanks Peter for saving his daughter, then calmly threatens to kill him and everyone he loves if he gets in the way again."),
        ("リズを置いて",
         "会場に入ったピーターは、トゥームスが次にねらっているのが、アベンジャーズ・タワーから新しい基地へ武器や装備を運ぶダメージ・コントロールの飛行機だと気づく。\n"
         "ピーターはリズにあやまり、ダンスの途中で会場を抜け出す。リズはひとり残される。ピーターは、学校に隠しておいた昔の手作りのスーツに着がえる。",
         "Leaving Liz behind",
         "Inside, Peter realizes Toomes's next target is a Damage Control plane moving weapons and gear from Avengers Tower to the team's new headquarters.\n"
         "He apologizes to Liz and leaves in the middle of the dance, and she's left alone. He changes into his old homemade suit, which he had hidden at school."),
        ("ショッカーとネッド",
         "外に出たピーターを、待ちぶせしていたシュルツ（ショッカー）がおそう。スーツの機能がないピーターは苦戦するが、ネッドの手助けで倒す。\n"
         "ネッドは学校のパソコンを使い、ピーターのためにトゥームスの居場所を調べる「後ろで支える役」を引き受ける。",
         "The Shocker and Ned",
         "Outside, Schultz, the Shocker, ambushes Peter. Without the Stark suit's features Peter struggles, but beats him with Ned's help.\n"
         "Using the school's computers, Ned becomes Peter's \"guy in the chair,\" helping track down Toomes."),
        ("倉庫の話し合い",
         "ピーターはトゥームスの隠れ家の倉庫にたどりつく。トゥームスは、トニーのような金持ちや権力のある人は、自分たちのような人間には目もくれないのだと語り、手を引くように言う。それでもピーターは引き下がらない。",
         "The talk in the warehouse",
         "Peter reaches Toomes's warehouse hideout. Toomes says rich and powerful people like Tony never care about people like them, and tells him to back off. Peter won't."),
        ("がれきの下",
         "トゥームスは翼のスーツで建物の柱を切りくずし、倉庫は崩れ落ちる。ピーターはがれきの下じきになって動けなくなり、恐怖のあまり泣きながら助けを呼ぶ。\n"
         "しかし、目の前の水たまりに映った、マスクが半分とれた自分の顔を見て、スーツがなくても自分はヒーローなのだと気持ちを奮い立たせる。ピーターは自分の力でがれきを持ち上げ、トゥームスを追う。",
         "Under the rubble",
         "Toomes cuts through the support columns with his wings, and the warehouse collapses. Pinned under the rubble, Peter is terrified and cries for help.\n"
         "Then he sees his half-masked face in a puddle, and pulls himself together: he's a hero even without the suit. He lifts the rubble off himself and goes after Toomes."),
    ]),
    ("第8部 空の上の戦い", "Part 8: The fight in the sky", [
        ("飛行機に飛び乗る",
         "姿を見えなくして飛ぶダメージ・コントロールの飛行機に、トゥームスが翼で取りつき、荷物を盗もうとする。ピーターも飛行機に飛び乗り、機体の上と中で、トゥームスと戦う。",
         "Leaping onto the plane",
         "Toomes latches onto the cloaked Damage Control plane to steal its cargo. Peter jumps onto it too, and they fight on top of and inside the plane."),
        ("砂浜への墜落",
         "戦いで飛行機は壊れ、墜落し始める。ピーターは機体をあやつって街に落ちるのを避け、コニーアイランドの砂浜に不時着させる。",
         "The crash on the beach",
         "The fight wrecks the plane, and it starts going down. Peter steers it away from the city and brings it down on the beach at Coney Island."),
        ("命を助ける",
         "砂浜でも2人は戦い続ける。トゥームスは荷物を持って飛び去ろうとするが、傷んでいた翼のスーツがこわれて爆発する。\n"
         "ピーターは燃える中からトゥームスを引っぱり出し、命を救う。",
         "Saving his life",
         "They keep fighting on the beach. Toomes tries to fly off with the cargo, but his damaged wing suit breaks down and explodes.\n"
         "Peter drags Toomes out of the fire and saves his life."),
        ("ハッピーへの書き置き",
         "ピーターは、トゥームスと散らばった荷物を糸でつなぎとめ、ハッピーにあてた書き置きを残して去る。トゥームスは警察に捕まる。",
         "A note for Happy",
         "Peter webs Toomes to the scattered cargo, leaves a note for Happy and goes. Toomes is arrested."),
    ]),
    ("第9部 その後", "Part 9: Afterward", [
        ("リズとの別れ",
         "父が捕まったリズは、母と一緒にニューヨークを離れ、遠くへ引っ越すことになる。何度も約束を破ったピーターに、リズは、何をしているにせよ、それをやりとげてほしいと伝えて去っていく。",
         "Goodbye to Liz",
         "With her father arrested, Liz moves away from New York with her mother. To Peter, who broke his promises again and again, she says that whatever he's doing, she hopes he sees it through, and leaves."),
        ("MJ",
         "リズの代わりに、デカスロンのチームのリーダーは同級生のミシェルが引きつぐ。ミシェルは、友だちは自分のことを「MJ」と呼ぶと言う。",
         "MJ",
         "Their classmate Michelle takes over from Liz as captain of the decathlon team. She says her friends call her \"MJ.\""),
        ("アベンジャーズの誘い",
         "ハッピーはピーターにお礼を言い、アベンジャーズの基地へ連れていく。トニーはピーターの戦いを認め、新しいスーツを用意して、アベンジャーズの正式なメンバーとして迎えると言う。記者会見の準備もできていた。\n"
         "しかしピーターは、今は近所の人々を守る「親愛なる隣人」のヒーローでいたいと言って断る。",
         "The Avengers offer",
         "Happy thanks Peter and takes him to the Avengers' headquarters. Tony praises how he handled things, shows him a new suit and offers him full membership in the Avengers, with a press conference all set.\n"
         "But Peter turns it down: for now, he wants to stay a friendly neighborhood hero."),
        ("指輪",
         "ピーターが帰ったあと、ペッパー・ポッツがやって来る。記者たちはもう集まっていた。何か発表することが必要になったトニーに、ハッピーは、2008年からずっと預かっていたという婚約指輪を取り出す。",
         "The ring",
         "After Peter leaves, Pepper Potts arrives, and the reporters are already waiting. Needing something to announce, Tony turns to Happy, who produces an engagement ring he says he's been holding onto since 2008."),
        ("メイに見られる",
         "家に帰ると、部屋に紙袋が置いてあった。中にはトニーが返してくれたスーツと手紙が入っていた。ピーターがスーツを着たところで、メイおばさんが部屋に入ってきて、その姿を見てしまう。",
         "May sees",
         "At home, Peter finds a bag in his room: the suit, returned by Tony, with a note. He puts it on just as Aunt May walks in and sees him."),
        ("エンドクレジットの途中",
         "刑務所。先に捕まっていたガーガンが、トゥームスに、スパイダーマンの正体を知っているといううわさを聞いたと話しかける。トゥームスは「知っていたら、とっくに殺している」と答え、正体を明かさない。",
         "Mid-credits",
         "In prison, Gargan, already locked up, tells Toomes he's heard Toomes knows who Spider-Man really is. Toomes denies it, and keeps Peter's secret."),
        ("エンドクレジットの後",
         "キャプテン・アメリカが学校向けに出演した古いビデオが流れ、「待つこと（忍耐）」の大切さを語る。",
         "After the credits",
         "One of Captain America's old school videos plays, a lesson on patience."),
    ]),
    ("まとめ", "Summary", [
        ("ピーターがしたこと",
         "ドイツでの戦いのあと、アベンジャーズに呼ばれる日を待ちながら近所を見回っていた（第2部・第3部）。トニーに止められても1人でバルチャーを追い、記念塔では仲間を救ったが（第5部）、フェリーでは大事故を起こしてスーツを取り上げられた（第6部）。\n"
         "手作りのスーツでトゥームスを止め、爆発する翼から命まで救った（第7部・第8部）。最後はアベンジャーズへの誘いを断り、近所のヒーローでいることを選んだ（第9部）。",
         "What Peter did",
         "After Germany, he patrolled the neighborhood waiting to be called up (Parts 2 and 3). Told by Tony to back off, he chased the Vulture alone, saving his friends at the monument (Part 5) but causing the ferry disaster and losing the suit (Part 6).\n"
         "In his homemade suit he stopped Toomes, and even saved him from his exploding wings (Parts 7 and 8). In the end he turned down the Avengers to stay a neighborhood hero (Part 9)."),
        ("トゥームスがしたこと",
         "がれきの片づけの仕事を奪われ、残していたチタウリの部品で武器を作って売るようになった（第1部）。翼のスーツでピーターを湖に落とし（第4部）、ピーターの正体に気づいておどした（第7部）。\n"
         "アベンジャーズの荷物を運ぶ飛行機をねらったが、ピーターに止められて捕まった（第8部）。刑務所では、ピーターの正体を明かさなかった（第9部）。",
         "What Toomes did",
         "Losing his cleanup job, he built and sold weapons from the Chitauri tech he'd kept (Part 1). In his wing suit he dropped Peter into a lake (Part 4), then figured out who Peter was and threatened him (Part 7).\n"
         "He went after the plane carrying the Avengers' gear, but Peter stopped him and he was arrested (Part 8). In prison, he kept Peter's secret (Part 9)."),
        ("トニーとピーター",
         "トニーはピーターにスーツを与えたが、危ないことをさせないよう機能を制限し、見守っていた（第2部・第4部）。言うことを聞かずに大勢を危険にさらしたピーターからスーツを取り上げたが（第6部）、最後はその成長を認めてアベンジャーズに誘い、スーツを返した（第9部）。",
         "Tony and Peter",
         "Tony gave Peter the suit but limited its features to keep him safe, and kept watch over him (Parts 2 and 4). When Peter ignored him and endangered many people, Tony took the suit away (Part 6), but in the end he recognized how he'd grown, offered him a place in the Avengers and gave the suit back (Part 9)."),
        ("死んだ人",
         "・ジャクソン・ブライス（第4部）：仲間から外されたことに怒り、トゥームスの家族に秘密をばらすとほのめかしたため、トゥームスが反重力の銃とまちがえて手に取った武器で撃たれ、灰のようになって消える。",
         "Who died",
         "- Jackson Brice (Part 4): angry at being cut loose, he hinted he'd tell Toomes's family the truth. Toomes shot him with a weapon he mistook for an anti-gravity gun, and Brice crumbled to dust."),
    ]),
]
