# 『キャプテン・アメリカ／ウィンター・ソルジャー』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじと、登場人物の記事で事実を確かめた。資料どうしで食い違う所や、確かめられない細かい順番・せりふは書いていない。
# 日本語版のせりふは、日本語のサイトで言い回しを確かめられた「左から失礼」だけをカギかっこで引用し、ほかは内容だけ書いた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 現代のスティーブ", "Part 1: Steve in the present", [
        ("朝のランニング",
         "ニューヨークの戦いから2年後。ワシントンの朝、リンカーン記念堂の前の池のまわり。\n"
         "スティーブは同じ男性を何度も追い抜き、そのたびに「左から失礼」と声をかける。抜かれた男性はサム・ウィルソン。元アメリカ空軍の救助隊員で、いまは退役軍人の相談にのる仕事をしている。\n"
         "2人は芝生で話しこむ。サムは、氷の中から目覚めて現代に戻ってきた暮らしはどうかとたずね、おすすめのレコードを教える。スティーブはそれを、見ておくもののメモに書き足す。\n"
         "そこへナターシャが車で迎えに来て、スティーブは任務へ向かう。",
         "Morning run",
         "Two years after the battle of New York. Morning in Washington, around the Reflecting Pool by the Lincoln Memorial.\n"
         "Steve laps the same runner again and again, calling out \"On your left\" each time. The runner is Sam Wilson, a former Air Force pararescueman who now counsels veterans.\n"
         "The two get talking on the grass. Sam asks what it's like coming back after waking up from the ice, and recommends an album. Steve adds it to his list of things to catch up on.\n"
         "Then Natasha pulls up in a car, and Steve heads off on a mission."),
        ("乗っ取られた船",
         "インド洋。S.H.I.E.L.D.の船レムリアン・スターが、バトロックの率いる海賊に乗っ取られ、乗組員が人質になっている。\n"
         "スティーブは、ナターシャと、ラムロウが隊長の特殊部隊ストライクとともに、夜の空から船に乗りこむ。スティーブはパラシュートなしで飛び降り、甲板の見張りを次々に倒す。\n"
         "ストライクの隊員たちが人質を助け出し、その中には幹部のシットウェルもいた。",
         "The hijacked ship",
         "The Indian Ocean. Pirates led by Batroc have seized the S.H.I.E.L.D. ship Lemurian Star and taken the crew hostage.\n"
         "Steve, Natasha and the S.T.R.I.K.E. team, led by Rumlow, drop onto the ship by night. Steve jumps without a parachute and takes out the guards on deck one after another.\n"
         "The team frees the hostages, including agent Sitwell."),
        ("ナターシャの別の任務",
         "スティーブは船の中でバトロックと1対1で戦う。そのとき、ナターシャが人質を探さず、船のコンピュータからデータを小さな装置に写していることに気づく。\n"
         "その騒ぎの間に、バトロックは逃げてしまう。ナターシャは、フューリーから別の命令を受けていた。何も知らされていなかったスティーブは怒る。",
         "Natasha's other mission",
         "Steve fights Batroc one-on-one below deck. Then he finds that Natasha isn't looking for hostages at all: she's copying data from the ship's computers onto a drive.\n"
         "In the confusion, Batroc gets away. Natasha had separate orders from Fury, and Steve, kept in the dark, is furious."),
        ("インサイト計画",
         "S.H.I.E.L.D.の本部トリスケリオン。スティーブはフューリーに詰め寄る。フューリーは祖父の話をしながら、スティーブを地下の巨大な格納庫へ連れて行く。\n"
         "そこには3隻の新しいヘリキャリア（空を飛ぶ空母）があった。船から打ち上げた人工衛星とつながり、世界中の危険な人物を見つけて、事件を起こす前に撃つ計画だ。\n"
         "スティーブは、それは人々を守るのではなく、おびえさせるやり方だと強く反対する。",
         "Project Insight",
         "At the Triskelion, S.H.I.E.L.D.'s headquarters, Steve confronts Fury. Telling a story about his grandfather, Fury takes him down to a vast hangar.\n"
         "Inside are three new Helicarriers. Linked to satellites launched from the ship, they are meant to find dangerous people anywhere in the world and kill them before they act.\n"
         "Steve objects: this isn't freedom, it's fear."),
        ("博物館と年老いたペギー",
         "スティーブは、ふつうの服で博物館のキャプテン・アメリカの展示を見に行く。そこには、戦争のころの自分や、戦死したことになっている親友バッキーの紹介があった。\n"
         "そのあと、年を取ってベッドで暮らすペギーを訪ねる。ペギーは、スティーブが生きてきた人生を送れなかったことを気にかける。話の途中で記憶があいまいになり、スティーブが生きていたことに、初めてのように驚いて泣く。",
         "The museum and an aged Peggy",
         "In street clothes, Steve visits the Captain America exhibit at a museum, with displays about his wartime self and about Bucky, his best friend who is listed as killed in action.\n"
         "Then he visits Peggy, now elderly and bedridden. She regrets that he never got to live the life he deserved. Mid-conversation her memory slips, and she weeps with surprise all over again to see him alive."),
        ("サムの集まり",
         "スティーブは、サムが開いている退役軍人の集まりに顔を出す。\n"
         "そのあとサムは、空軍のときに背中に機械の翼をつけて飛ぶ任務をしていたこと、いっしょに飛んでいた仲間ライリーが撃ち落とされるのを目の前で見たことを話す。それからサムは戦場を離れた。",
         "Sam's group",
         "Steve drops in on the veterans' support group Sam runs.\n"
         "Afterward, Sam tells him he flew missions in the Air Force with mechanical wings strapped to his back, and that he watched his wingman Riley get shot down. After that, he got out."),
    ]),
    ("第2部 フューリーが襲われる", "Part 2: Fury is attacked", [
        ("開けないデータ",
         "フューリーは、ナターシャが持ち帰ったデータを開こうとするが、コンピュータに断られる。長官の自分でも見られないようにされていた。\n"
         "怪しいと思ったフューリーは、世界安全保障委員会の幹部ピアースに会い、インサイト計画を遅らせてほしいと頼む。ピアースはかつてフューリーを長官にした人物だった。",
         "Data he can't open",
         "Fury tries to open the data Natasha brought back, but the system refuses him. Even the director has been locked out.\n"
         "Suspicious, he meets Alexander Pierce, a senior official on the World Security Council and the man who made him director, and asks him to delay Project Insight."),
        ("街中の襲撃",
         "マリア・ヒルに会いに行く途中、フューリーの車が、警官のふりをした男たちに囲まれ、銃撃される。フューリーは防弾の車で何とか逃げ切ろうとする。\n"
         "そこへ、金属の腕を持つ覆面の暗殺者ウィンター・ソルジャーが現れ、車の下に爆弾を撃ちこんでひっくり返す。ところが近づいてみると車は空で、道路に穴が開いていた。フューリーは道路を焼き切って、地下へ逃げていた。",
         "Ambushed in the streets",
         "On his way to meet Maria Hill, Fury's car is boxed in and shot up by men posing as police. His armored SUV keeps him alive as he tries to break away.\n"
         "Then a masked assassin with a metal arm, the Winter Soldier, fires a bomb under the car and flips it. When he walks up, the car is empty, with a hole cut in the road beneath it. Fury has escaped underground."),
        ("スティーブの部屋",
         "スティーブが家に帰ると、隣に住む看護師のケイトに声をかけられる。部屋に入ると、暗い中にフューリーが座っていた。\n"
         "フューリーは、盗み聞きされているかもしれないので、口では関係のない話をしながら、携帯の画面でS.H.I.E.L.D.が乗っ取られていると伝える。\n"
         "そのとき、向かいのビルから壁ごしに撃たれ、フューリーは倒れる。倒れたフューリーは、データの入った小さな装置をスティーブに渡し、誰も信じるなと言う。",
         "Steve's apartment",
         "Back home, Steve chats with his neighbor Kate, a nurse. Inside his apartment, Fury is sitting in the dark.\n"
         "Worried the room is bugged, Fury talks about nothing out loud while using his phone screen to tell Steve that S.H.I.E.L.D. is compromised.\n"
         "Then he is shot through the wall from a building across the street. As he collapses, he presses the flash drive into Steve's hand and tells him to trust no one."),
        ("屋根の上の追いかけっこ",
         "銃声を聞いたケイトが銃を持って飛びこんでくる。彼女は実は、スティーブを見守るためにフューリーが送ったS.H.I.E.L.D.の隊員だった。\n"
         "スティーブは窓から飛び出し、屋根づたいに暗殺者を追う。投げた盾を、暗殺者は金属の腕で受け止めて投げ返し、そのまま姿を消す。",
         "The rooftop chase",
         "Kate bursts in with a gun. She is actually a S.H.I.E.L.D. agent Fury assigned to watch over Steve.\n"
         "Steve crashes through the window and chases the shooter across the rooftops. He hurls his shield; the assassin catches it with his metal arm, throws it back and vanishes."),
        ("フューリーの死",
         "病院で、フューリーは手術を受けるが、亡くなったと告げられる。ナターシャは涙を流す。\n"
         "スティーブは、フューリーから受け取った装置を、病院の廊下の自動販売機の中にこっそり隠す。",
         "Fury's death",
         "At the hospital, Fury goes into surgery and is pronounced dead. Natasha is in tears.\n"
         "Steve quietly hides the drive inside a vending machine in the hospital corridor."),
        ("エレベーターの戦い",
         "ピアースはスティーブを呼び、船を襲ったバトロックを雇ったのはフューリーだったという証拠を見せる。ピアースは、フューリーが最後に何を言ったかたずねるが、スティーブは答えない。\n"
         "帰りのガラス張りのエレベーターに、ラムロウたちストライクの隊員が次々に乗ってくる。スティーブは様子がおかしいと気づき、狭い中で全員と戦って倒す。\n"
         "エレベーターを止められたスティーブは、ガラスを割って下の階へ飛び降り、バイクで本部を脱出する。追ってきた小型の戦闘機には、バイクをぶつけて落とす。スティーブは裏切り者として追われる身になる。",
         "The elevator fight",
         "Pierce summons Steve and shows him evidence that Fury hired Batroc to hijack the ship. Pierce asks what Fury's last words were. Steve won't tell him.\n"
         "On the way out, Rumlow and other S.T.R.I.K.E. agents keep filling his glass elevator. Sensing the trap, Steve asks, \"Before we get started, does anyone want to get out?\" and then fights them all in the cramped space.\n"
         "With the elevator locked, he smashes through the glass, drops to a lower floor and escapes on his motorcycle, flinging the bike into a pursuing Quinjet to bring it down. He is now a fugitive."),
    ]),
    ("第3部 隠されていた敵", "Part 3: The enemy within", [
        ("ナターシャと組む",
         "病院に戻ると、自動販売機の装置はなくなっていた。持っていったのはナターシャだった。\n"
         "2人はショッピングモールの店のパソコンで装置を調べ、データがニュージャージー州のある場所を指していることを知る。追ってきたラムロウたちの目をごまかすため、2人はエスカレーターでキスをするふりをしてやり過ごす。",
         "Teaming up with Natasha",
         "Back at the hospital, the drive is gone from the vending machine. Natasha has it.\n"
         "At a shopping mall, they plug it into a store computer and trace the data to a location in New Jersey. To slip past Rumlow's men, they fake a kiss on the escalator."),
        ("オデッサの話",
         "車で向かう途中、ナターシャはウィンター・ソルジャーの話をする。5年前、守っていた技術者を狙われ、暗殺者は彼女の体ごと撃ち抜いた。そのときの傷が今も残っているという。\n"
         "ウィンター・ソルジャーは、多くの人が作り話だと思っている、正体の分からない伝説の暗殺者だった。",
         "The Odessa story",
         "On the drive, Natasha tells Steve about the Winter Soldier. Five years ago, he went after an engineer she was protecting near Odessa and shot him straight through her. She still has the scar.\n"
         "Most people in the spy world, she says, think he's only a ghost story."),
        ("古いキャンプの地下",
         "着いたのは、スティーブが戦争のころに訓練を受けたキャンプの跡だった。スティーブは、昔はなかった建物に気づく。\n"
         "中の隠し扉からエレベーターで地下へ降りると、古い大型コンピュータがあった。そこには、昔ヒドラの科学者だったアーニム・ゾラの心が、データとして残されていた。",
         "Beneath the old camp",
         "It's Camp Lehigh, where Steve trained during the war. He spots a building that shouldn't be there.\n"
         "A hidden elevator takes them down to an old room-sized computer that holds the mind of Arnim Zola, the former Hydra scientist, preserved as data."),
        ("ヒドラの秘密",
         "ゾラは語る。戦争のあと、S.H.I.E.L.D.は自分を科学者として迎え入れた。自分はその中で、こっそりヒドラを作り直した。\n"
         "ヒドラは何十年もかけて、世界に争いや危機を起こし、人々が安全のために自分から自由を手放すように仕向けてきた。じゃまになる人は、ウィンター・ソルジャーなどを使って事故に見せかけて消した。画面には、ハワード・スターク夫妻の死を伝える新聞なども映る。",
         "Hydra's secret",
         "Zola explains that after the war, S.H.I.E.L.D. took him on as a scientist, and from inside it he quietly rebuilt Hydra.\n"
         "For decades Hydra stirred up crises so that people would give up their freedom for security, and it removed anyone in the way, using the Winter Soldier among others, staging deaths to look like accidents. Among the images on screen is a newspaper reporting the deaths of Howard and Maria Stark."),
        ("ミサイル",
         "ゾラが話を長引かせている間に、S.H.I.E.L.D.のミサイルが飛んでくる。スティーブはナターシャを盾でかばい、床の下の穴に飛びこんで、建物ごと吹き飛ぶ爆発を生きのびる。\n"
         "ミサイルが撃たれたことで、2人はピアースがS.H.I.E.L.D.の中のヒドラの親玉だと気づく。",
         "The missile",
         "While Zola keeps them talking, a S.H.I.E.L.D. missile comes in. Steve shields Natasha and drops into a pit under the floor, and they survive the blast that levels the building.\n"
         "The strike tells them Pierce is the head of Hydra inside S.H.I.E.L.D."),
        ("ピアースの家",
         "ピアースの家に、ウィンター・ソルジャーが来ている。それを見てしまった家政婦のレナータを、ピアースはためらわずに撃ち殺す。\n"
         "ピアースは、ウィンター・ソルジャーに次の標的を伝える。",
         "Pierce's house",
         "The Winter Soldier is waiting at Pierce's house. When Pierce's housekeeper, Renata, sees him, Pierce shoots her dead without hesitation.\n"
         "Pierce gives the Winter Soldier his next targets."),
        ("サムの家",
         "スティーブとナターシャは、サムの家を訪ね、かくまってもらう。サムは2人を家に入れ、朝ごはんを作る。\n"
         "サムは、自分がかつて使っていた翼の装備「ファルコン」の資料を見せ、力を貸すと言う。装備は厳しく守られた基地にあり、3人はそれを手に入れる。",
         "Sam's house",
         "Steve and Natasha turn up at Sam's door, and he takes them in and makes breakfast.\n"
         "Sam shows them the file on the winged rig he used to fly, the Falcon, and offers to help. It's kept on a heavily guarded base, and they get it out."),
    ]),
    ("第4部 ウィンター・ソルジャー", "Part 4: The Winter Soldier", [
        ("シットウェルを問いつめる",
         "3人は、S.H.I.E.L.D.の幹部シットウェルが怪しいとにらみ、ビルの屋上で捕まえる。屋上から突き落とされ、翼で飛ぶサムに受け止められたシットウェルは、ついに話し出す。\n"
         "ゾラは、人がこれまでに残したさまざまな記録から、将来ヒドラのじゃまになりそうな人を選び出す仕組みを作っていた。インサイト計画のヘリキャリアは、選ばれた何百万人もの人を空から一度に撃つためのものだった。\n"
         "標的の例として、ニュース番組の司会者や、アイオワ州の高校生、ブルース・バナー、スティーヴン・ストレンジの名前まで挙がる。",
         "Breaking Sitwell",
         "Suspecting senior agent Jasper Sitwell, the three grab him on a rooftop. Kicked off the edge and caught in midair by Sam on his wings, Sitwell talks.\n"
         "Zola built an algorithm that sifts people's records to pick out anyone likely to threaten Hydra in the future. The Insight Helicarriers will shoot millions of those people from the sky at once.\n"
         "The targets he names include a TV anchor, a high school student in Iowa, Bruce Banner and Stephen Strange."),
        ("高速道路の襲撃",
         "シットウェルを車に乗せて移動していると、ウィンター・ソルジャーが車の屋根に飛び乗る。暗殺者はシットウェルを窓から引きずり出し、走ってくる車の列に投げ捨てて殺す。\n"
         "暗殺者が金属の腕でハンドルを引きちぎり、車は止まれなくなる。3人は外れた車のドアを盾にして、道路をすべりながら何とか助かる。",
         "Attack on the highway",
         "As they drive with Sitwell, the Winter Soldier lands on the roof of the car. He drags Sitwell out through the window and hurls him into oncoming traffic, killing him.\n"
         "Then he rips out the steering wheel with his metal arm. The three of them ride a torn-off car door down the road and make it out."),
        ("街中の戦い",
         "ウィンター・ソルジャーとその部下たちが、銃や爆弾で3人を襲い、戦いは高速道路から街中へ広がる。ナターシャは肩を撃たれる。\n"
         "サムは翼で飛んで部下たちと戦い、スティーブは盾でウィンター・ソルジャーとぶつかり合う。",
         "The street battle",
         "The Winter Soldier and his team come at them with guns and explosives, and the fight spreads from the highway into the city streets. Natasha is shot in the shoulder.\n"
         "Sam takes on the gunmen from the air while Steve battles the Winter Soldier with his shield."),
        ("仮面の下",
         "戦いの中で、暗殺者の仮面が外れる。その顔は、70年前に列車から落ちて死んだはずの親友バッキーだった。\n"
         "スティーブが名前を呼んでも、バッキーはスティーブのことが分からず、バッキーとは誰だと言う。ゾラの実験で生きのびたバッキーは、何度も記憶を消され、冷凍されて眠らされては、ヒドラの暗殺に使われていた。",
         "Behind the mask",
         "In the fight, the assassin's mask comes off. It's Bucky, the best friend Steve thought died seventy years ago when he fell from a train.\n"
         "When Steve says his name, Bucky doesn't know him: \"Who the hell is Bucky?\" Kept alive by Zola's experiments, he has been brainwashed again and again, frozen between missions and used as Hydra's assassin."),
        ("捕まった3人",
         "ストライクが駆けつけ、スティーブ、ナターシャ、サムは捕まって護送車に乗せられる。\n"
         "車の中で、ストライクの隊員の1人がヘルメットを取る。それはマリア・ヒルだった。ヒルは見張りを倒し、3人を逃がす。",
         "Captured",
         "S.T.R.I.K.E. arrives, and Steve, Natasha and Sam are arrested and loaded into a transport.\n"
         "Inside, one of the guards takes off her helmet: it's Maria Hill. She takes out the guard and gets the three of them out."),
        ("生きていたフューリー",
         "ヒルが連れて行った隠れ家には、死んだはずのフューリーがいた。心臓の動きをほとんど止める薬を使い、死んだふりをしていたのだ。\n"
         "フューリーは、ヘリキャリアに3枚の新しい装置を差しこめば、撃つ相手を変えられると話す。スティーブは、ヒドラだけでなくS.H.I.E.L.D.もなくすべきだと言い、フューリーもそれを受け入れる。",
         "Fury lives",
         "At the hideout Hill takes them to, Fury is waiting, alive. He faked his death with a drug that slows the heart almost to a stop.\n"
         "Fury explains that if they swap new chips into the three Helicarriers, they can change what the ships fire at. Steve says S.H.I.E.L.D. has to go too, not just Hydra, and Fury goes along with it."),
        ("消される記憶",
         "そのころ、ヒドラの研究所。バッキーは座ったまま、橋の上の男を知っていると言う。スティーブのことを思い出しかけていたのだ。\n"
         "ピアースはバッキーを殴り、記憶を消すよう命じる。バッキーは機械の椅子に固定され、ふたたび記憶を消される。",
         "Wiped again",
         "Meanwhile, in a Hydra lab, Bucky sits and says he knew the man on the bridge. He is beginning to remember Steve.\n"
         "Pierce strikes him and orders his mind wiped. Bucky is strapped into the machine and wiped once more."),
    ]),
    ("第5部 ヘリキャリアの戦い", "Part 5: The battle of the Helicarriers", [
        ("昔の制服",
         "スティーブは博物館の展示から、戦争のころの制服を持ち出す。サムは翼をつける。\n"
         "インサイト計画の発進の日、世界安全保障委員会の人々がトリスケリオンに集まる。",
         "The old uniform",
         "Steve takes his wartime uniform from the museum exhibit, and Sam straps on his wings.\n"
         "On launch day, members of the World Security Council gather at the Triskelion."),
        ("全職員への呼びかけ",
         "スティーブは本部の放送を乗っ取り、全職員に向けて、S.H.I.E.L.D.がヒドラに乗っ取られていることを伝える。ともに立ち上がってほしいと呼びかける。\n"
         "管制室では、ラムロウが職員に銃を向けて発進させようとする。ケイトだったシャロンがラムロウに銃を向けるが、職員たちは撃ち合いになり、本部の中は敵と味方に分かれて戦いになる。ヘリキャリアは飛び立ってしまう。",
         "A message to everyone",
         "Steve takes over the building's PA and tells every employee that Hydra has taken over S.H.I.E.L.D., asking them to stand with him.\n"
         "In the control room, Rumlow holds a technician at gunpoint to force the launch. Sharon, who was \"Kate,\" pulls her gun on him, and the building splits into a gunfight between Hydra and loyal agents. The Helicarriers lift off."),
        ("ピアースの部屋",
         "委員会の部屋では、委員の1人に化けたナターシャが、ピアースの武器を奪う。そこへフューリーが現れる。\n"
         "フューリーは、もう片方の目の記録を使ってデータの鍵を開けさせる。ナターシャは、S.H.I.E.L.D.とヒドラの秘密をすべてインターネットに公開する。その中には、ナターシャ自身の過去の記録も入っていた。\n"
         "もみ合いの末、フューリーがピアースを撃ち、ピアースは死ぬ。",
         "Pierce's room",
         "In the council chamber, Natasha, disguised as one of the council members, disarms Pierce. Then Fury walks in.\n"
         "Using a scan of his other eye, he forces the database open, and Natasha dumps all of S.H.I.E.L.D.'s and Hydra's secrets onto the internet, including her own past.\n"
         "After a struggle, Fury shoots Pierce dead."),
        ("2隻目まで",
         "スティーブとサムは空へ飛び立ったヘリキャリアに乗りこみ、1隻ずつ装置を差しかえていく。\n"
         "2隻目までは成功する。3隻目に向かうと、ウィンター・ソルジャーが待っていた。暗殺者はサムの翼をこわし、サムは地上で戦うことになる。",
         "Two down",
         "Steve and Sam storm the airborne Helicarriers and swap in the new chips one by one.\n"
         "The first two go fine. On the third, the Winter Soldier is waiting. He wrecks Sam's wings, and Sam is forced back to the ground."),
        ("3隻目の戦い",
         "3隻目で、スティーブとバッキーが激しく戦う。バッキーはスティーブを何度も撃つが、スティーブは装置を差しこむ。\n"
         "ヒルが合図を出し、3隻のヘリキャリアは、ヒドラが選んだ人々の代わりに、互いを撃ち合って崩れていく。",
         "The third carrier",
         "On the third carrier, Steve and Bucky fight hard. Bucky shoots Steve more than once, but Steve gets the chip in.\n"
         "Hill gives the command, and instead of Hydra's targets, the three Helicarriers fire on each other and start to break apart."),
        ("最後まで一緒だ",
         "崩れる船の中で、がれきの下じきになったバッキーを、スティーブが助け出す。スティーブは盾を落とし、もう戦わない、お前は友だちだと言う。\n"
         "バッキーは、お前は任務の標的だと言って殴り続ける。スティーブは、それなら最後までやれ、自分は最後まで一緒だと言う。それは昔、バッキーがスティーブにかけた言葉だった。バッキーの手が止まる。\n"
         "そのとき船が崩れ、スティーブはポトマック川へ落ちる。バッキーは川に入ってスティーブを引き上げ、気を失ったスティーブを岸に置いて、森の中へ去っていく。",
         "To the end of the line",
         "In the collapsing ship, Steve frees Bucky from under fallen beams. He drops his shield and says he won't fight: Bucky is his friend.\n"
         "Bucky keeps hitting him, insisting Steve is his mission. Steve tells him to finish it, then, \"'cause I'm with you till the end of the line\" — the words Bucky once said to him. Bucky's fist stops.\n"
         "The ship gives way and Steve falls into the Potomac. Bucky goes in after him, drags him out, leaves him unconscious on the bank and walks off into the woods."),
        ("本部の崩壊",
         "ヘリキャリアの1隻がトリスケリオンに突っこむ。中でサムと戦っていたラムロウは、崩れた建物の下じきになって大けがをする。\n"
         "フューリーとナターシャはヘリコプターで屋上から脱出し、サムを乗せて飛び去る。",
         "The fall of the Triskelion",
         "A Helicarrier crashes into the Triskelion. Rumlow, who was fighting Sam inside, is badly hurt when the building comes down on him.\n"
         "Fury and Natasha escape from the roof by helicopter and pick up Sam."),
    ]),
    ("第6部 その後", "Part 6: Afterward", [
        ("病院のベッド",
         "スティーブは病院で目を覚ます。そばにはサムがいた。スティーブは、初めて会った朝のように、サムに左から失礼と言う。",
         "The hospital bed",
         "Steve wakes up in a hospital bed with Sam beside him, and greets him the way he did the morning they met: \"On your left.\""),
        ("議会での証言",
         "S.H.I.E.L.D.はなくなる。ナターシャは議会の委員会に呼ばれ、自分たちのしたことを責められるが、自分たちがいなければ世界は守れないと言い返して堂々と出ていく。",
         "Testifying before Congress",
         "S.H.I.E.L.D. is finished. Natasha appears before a Senate subcommittee, which wants to blame them, and she answers back that the world still needs them, then walks out."),
        ("フューリーの墓",
         "フューリーの墓。人々には死んだと思わせたまま、フューリーはヒドラの残りを追ってヨーロッパへ行くと告げる。\n"
         "ナターシャは、バッキーについての資料をスティーブに渡す。スティーブとサムは、バッキーを探す旅に出ると決める。",
         "Fury's grave",
         "At Fury's grave, Fury, still officially dead, says he is going to Europe to hunt down the rest of Hydra.\n"
         "Natasha hands Steve a file on Bucky, and Steve and Sam decide to go looking for him."),
        ("エンドクレジットの途中",
         "ヒドラの秘密の研究所で、ストラッカー男爵たちが、光る杖を研究している（『アベンジャーズ』でロキが使っていた杖）。\n"
         "そこには、実験で特別な力を得た双子の兄妹が閉じこめられていた。兄はものすごい速さで動き、妹は手を使わずにものを動かす。",
         "Mid-credits",
         "In a secret Hydra lab, Baron Strucker and his scientists study a glowing scepter (the one Loki used in The Avengers).\n"
         "Held there are twins given special powers by experiments: the brother moves at incredible speed, and the sister moves things without touching them."),
        ("エンドクレジットの後",
         "博物館のキャプテン・アメリカの展示。バッキーがひとりで、自分の写真と紹介文を見つめている。",
         "After the credits",
         "At the museum's Captain America exhibit, Bucky stands alone, looking at his own photo and story."),
    ]),
    ("まとめ（結末までのネタバレ）", "Summary (spoilers through the ending)", [
        ("ヒドラの計画",
         "ヒドラは戦争のあと、ゾラを通してS.H.I.E.L.D.の中で生き残り、何十年もかけて大きくなっていた（第3部）。S.H.I.E.L.D.の中の親玉はピアースだった（第3部）。\n"
         "インサイト計画は、ゾラの仕組みで選んだ、将来ヒドラのじゃまになりそうな何百万人もの人を、3隻のヘリキャリアで一度に撃つ計画だった（第4部）。\n"
         "スティーブとサムが3隻の装置を差しかえ、ヘリキャリアは互いを撃ち合って落ちた。ナターシャが秘密をすべて公開し、ヒドラとともにS.H.I.E.L.D.もなくなった（第5部〜第6部）。",
         "Hydra's plan",
         "After the war, Hydra survived inside S.H.I.E.L.D. through Zola and grew for decades (Part 3). Its leader inside S.H.I.E.L.D. was Pierce (Part 3).\n"
         "Project Insight would use three Helicarriers to shoot, all at once, millions of people that Zola's algorithm marked as future threats to Hydra (Part 4).\n"
         "Steve and Sam swapped the chips on all three, and the ships destroyed each other. Natasha leaked every secret, and S.H.I.E.L.D. fell along with Hydra (Parts 5–6)."),
        ("バッキーのこと",
         "列車から落ちたバッキーは、ゾラの実験で生きのび、記憶を消されてはヒドラの暗殺者ウィンター・ソルジャーとして使われてきた（第4部）。\n"
         "フューリーを襲い（第2部）、シットウェルを殺し、スティーブたちと戦った（第4部）。スティーブを思い出しかけると、また記憶を消された（第4部）。\n"
         "最後は、戦おうとしないスティーブを殺せず、川から助け出して去った（第5部）。そして博物館で、自分の過去を見つめる（第6部）。",
         "About Bucky",
         "After his fall from the train, Bucky survived thanks to Zola's experiments and was used as Hydra's assassin, the Winter Soldier, his memory wiped again and again (Part 4).\n"
         "He attacked Fury (Part 2), killed Sitwell and fought Steve's team (Part 4). When he began to remember Steve, he was wiped again (Part 4).\n"
         "In the end he couldn't kill Steve, who refused to fight; he pulled him from the river and left (Part 5). Then he goes to the museum to look at his own past (Part 6)."),
        ("死んだ人・けがをした人（話の順に）",
         "・フューリー（第2部）：死んではいない。ウィンター・ソルジャーに壁ごしに撃たれ、手術中に亡くなったと発表されたが、心臓の動きを遅くする薬で死んだふりをしていた（第4部で分かる）。\n"
         "・ナターシャ（第3部の話）：5年前、ウィンター・ソルジャーに体ごと撃ち抜かれたが生きのびた。第4部でも肩を撃たれる。\n"
         "・レナータ（第3部）：ピアースの家政婦。ウィンター・ソルジャーを見てしまったため、ピアースに撃ち殺される。\n"
         "・シットウェル（第4部）：ヒドラの秘密を話したあと、車で運ばれている途中に、ウィンター・ソルジャーに窓から引きずり出され、走る車の列に投げこまれて死ぬ。\n"
         "・ピアース（第5部）：秘密を公開されたあと、もみ合いの末にフューリーに撃たれて死ぬ。\n"
         "・ラムロウ（第5部）：ヘリキャリアが本部に突っこみ、崩れた建物の下じきになって大けがをする。\n"
         "・スティーブ（第5部）：バッキーに撃たれ、川に落ちて気を失うが、バッキーに助けられ、病院で目を覚ます（第6部）。",
         "Who died or was hurt (in order)",
         "- Fury (Part 2): not killed. Shot through the wall by the Winter Soldier and declared dead in surgery, he had faked his death with a drug that slows the heart (revealed in Part 4).\n"
         "- Natasha (story told in Part 3): five years ago the Winter Soldier shot through her, and she survived. She is shot in the shoulder in Part 4.\n"
         "- Renata (Part 3): Pierce's housekeeper. Pierce shoots her dead because she saw the Winter Soldier.\n"
         "- Sitwell (Part 4): after revealing Hydra's plan, he is dragged out of the car window by the Winter Soldier and thrown into traffic.\n"
         "- Pierce (Part 5): after his secrets are leaked, Fury shoots him dead following a struggle.\n"
         "- Rumlow (Part 5): badly hurt when a Helicarrier crashes into the Triskelion and the building collapses on him.\n"
         "- Steve (Part 5): shot by Bucky and knocked out falling into the river; Bucky pulls him out, and he wakes up in hospital (Part 6)."),
    ]),
]
