# 『ブラック・ウィドウ』（2021年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじ、登場人物・乗り物・場所の説明、検索で見つかった解説記事で事実を確かめた。
# 資料どうしで食い違う所や、確かめられない細かい所（モロッコの場面とノルウェーの場面の細かい前後、
# ブダペストの任務の回想が出てくる位置、エレーナがドレイコフの飛行機を爆破した方法、
# ベストをゆずった場面など）は書いていない。
# 日本語版のせりふは、日本語の吹替・字幕の言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 人物名は相関図（relations.py）にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 1995年 オハイオの家族", "Part 1: Ohio, 1995", [
        ("ホタルの夕方",
         "1995年、アメリカ・オハイオ州の静かな住宅地。少女ナターシャと妹のエレーナは、父アレクセイ、母メリーナと4人で暮らしている。\n"
         "夕方、外で遊んでいたエレーナとナターシャに、メリーナがホタルの光るしくみを教える。どこにでもいる仲のよい家族に見える。",
         "Fireflies at dusk",
         "Ohio, 1995. In a quiet suburb, young Natasha and her little sister Yelena live with their father Alexei and mother Melina.\n"
         "At dusk, Melina explains to the girls how fireflies make their light. They look like any happy family."),
        ("突然の出発",
         "しかし4人は、ロシアから送られたスパイが家族のふりをしている偽の家族だった。父役のアレクセイはソ連のスーパー兵士、母役のメリーナはレッドルームで育ったウィドウだ。幼いエレーナだけが、そのことを知らない。\n"
         "アレクセイは、アメリカの組織シールドの研究所から、ねらっていた研究のデータを盗み出した。3年続いた任務は終わり、一家はその夜のうちに家を出ることになる。",
         "A sudden departure",
         "But they're a fake family: spies sent from Russia. Alexei, the 'dad,' is a Soviet super soldier; Melina, the 'mom,' is a Widow trained in the Red Room. Only little Yelena doesn't know.\n"
         "Alexei has stolen the research data he was after from a S.H.I.E.L.D. facility. Their three-year mission is over, and the family leaves home that very night."),
        ("小さな飛行機で国外へ",
         "車の中で、アレクセイはこわがるエレーナのために『アメリカン・パイ』の曲をかけてやる。\n"
         "町はずれのビニールハウスには、小さな飛行機がかくしてあった。シールドの車が追いかけてきて銃を撃つ。アレクセイは追っ手を食い止めてから、動き出した飛行機にしがみついて乗りこむ。\n"
         "操縦していたメリーナが撃たれてけがをする。メリーナに教わりながら、ナターシャが操縦かんをにぎり、飛行機はなんとか飛び立つ。",
         "Escape by plane",
         "In the car, Alexei plays \"American Pie\" for the frightened Yelena.\n"
         "A small plane is hidden in a greenhouse at the edge of town. S.H.I.E.L.D. vehicles chase them, firing. Alexei holds them off, then grabs onto the moving plane and climbs aboard.\n"
         "Melina, at the controls, is shot. With Melina talking her through it, Natasha takes the controls and gets the plane into the air."),
        ("キューバで引きさかれる",
         "一家はキューバの滑走路に着く。待っていたのは、レッドルームを率いるドレイコフとロシアの兵士たちだった。\n"
         "ナターシャとエレーナは、アレクセイとメリーナから引き離され、連れて行かれる。偽の家族は、この日ばらばらになった。",
         "Torn apart in Cuba",
         "The family lands on an airstrip in Cuba. Waiting for them are Dreykov, head of the Red Room, and Russian soldiers.\n"
         "Natasha and Yelena are separated from Alexei and Melina and taken away. The fake family is broken up that day."),
        ("タイトルの映像",
         "タイトルが出るあいだ、世界中から集められた少女たちが、トラックで運ばれ、ドレイコフの兵士たちに厳しく扱われて、スパイ（ウィドウ）になる訓練を受けていく様子が映される。その中に、ナターシャとエレーナもいる。",
         "The opening titles",
         "Over the titles, girls are trucked away, mistreated by Dreykov's soldiers, and trained to become spies called Widows. Natasha and Yelena are among them."),
    ]),
    ("第2部 逃亡中のナターシャ", "Part 2: Natasha on the run", [
        ("ロス長官の追跡",
         "2016年。『シビル・ウォー』でキャプテン・アメリカの側についたナターシャは、ソコヴィア協定に違反したとして、ロス国務長官に追われていた。\n"
         "ナターシャはロスの部隊をかわし、アメリカから姿を消す。",
         "Ross gives chase",
         "2016. Having sided with Captain America in Civil War, Natasha is wanted by Secretary of State Ross for violating the Sokovia Accords.\n"
         "She slips past Ross's people and disappears."),
        ("ノルウェーのトレーラーハウス",
         "ナターシャがたどり着いたのは、ノルウェーの入り江に置かれたトレーラーハウス。中では、昔なじみの調達屋リック・メイソンがベッドに寝ころんで待っていた。\n"
         "メイソンは、パスポートや入国の書類、何人分もの免許証、発電機を用意してくれる。ブダペストの隠れ家にとどいていた郵便物も、まとめて届けてくれた。\n"
         "一人になったナターシャは、ビールを飲みながら、何度も観ているらしいスパイ映画『007 ムーンレイカー』を、せりふを口にしながら観る。",
         "A trailer in Norway",
         "Natasha arrives at a trailer by a Norwegian fjord, where her old contact, the fixer Rick Mason, is waiting, lying on the bed.\n"
         "He brings her passports, visas, a stack of driver's licenses and a generator, plus the mail that piled up at her old Budapest safe house.\n"
         "Alone, she drinks a beer and watches the Bond film Moonraker, reciting the lines along with it."),
        ("モロッコのエレーナ",
         "同じころ、モロッコの町タンジェ。大人になったエレーナは、ウィドウとしてレッドルームに心をあやつられたまま働いていた。この日の任務は、組織から逃げた元ウィドウのオクサナを追うことだった。\n"
         "エレーナはオクサナに致命傷を負わせる。しかしオクサナは、エレーナに赤いガスを浴びせる。ウィドウの心のあやつりを解く薬だった。\n"
         "正気に戻ったエレーナに、オクサナはほかのウィドウたちを自由にしてほしいと託して息を引き取る。エレーナは自分の脚に入れられていた発信機を切り出し、姿を消す。",
         "Yelena in Morocco",
         "Meanwhile, in Tangier, Morocco, the grown-up Yelena is still working as a mind-controlled Red Room Widow. Her target is Oksana, a Widow who went rogue.\n"
         "Yelena fatally wounds Oksana, but Oksana sprays her with a red gas: an antidote that undoes the Widows' mind control.\n"
         "Freed, Yelena hears Oksana's dying plea to free the others. She cuts the tracker out of her own leg and goes into hiding."),
        ("荷物の中の小びん",
         "エレーナは、赤いガスの入った小びんを、ナターシャのブダペストの隠れ家へ送っていた。ナターシャやアベンジャーズが、残りのウィドウたちを救ってくれると信じたのだ。この小びんが、メイソンの届けた郵便物の中にまぎれていた。\n"
         "発電機のガソリンを買いに出たナターシャは、小びんが車の中にあることを知らないまま走っていた。",
         "Vials in the mail",
         "Yelena had mailed vials of the red gas to Natasha's Budapest safe house, trusting that Natasha and the Avengers would free the remaining Widows. The vials were in the mail Mason brought.\n"
         "Natasha drives out to buy gas for the generator, unaware the vials are in her car."),
        ("タスクマスターの襲撃",
         "走るナターシャの車を、マスクの戦士タスクマスターが襲う。ナターシャは戦うが、相手はナターシャ自身の技までそっくりまねしてくる。\n"
         "ナターシャはなんとか逃げきり、タスクマスターのねらいが小びんだと気づく。荷物がブダペストから来たことを知り、ナターシャはブダペストへ向かう。",
         "Taskmaster attacks",
         "The masked fighter Taskmaster attacks Natasha's car. As they fight, Taskmaster copies even Natasha's own moves.\n"
         "Natasha barely escapes and realizes Taskmaster was after the vials. Seeing they came from Budapest, she heads there."),
    ]),
    ("第3部 ブダペストの再会", "Part 3: Reunion in Budapest", [
        ("昔の隠れ家",
         "ブダペストは、ナターシャがクリント（ホークアイ）と昔の任務で戦った町だ。ナターシャは、かつてクリントと使った隠れ家のアパートに入る。台所の壁には、昔の矢のあとが残っていた。\n"
         "部屋には、エレーナが待ちかまえていた。",
         "The old safe house",
         "Budapest is where Natasha and Clint (Hawkeye) once fought on an old mission. Natasha enters the apartment safe house she used with Clint; arrow holes from back then still mark the kitchen wall.\n"
         "Yelena is waiting for her."),
        ("姉妹の大げんか",
         "久しぶりに会った2人は、言葉より先に戦い始める。部屋の物がこわれ、皿が割れ、最後はナイフまで持ち出すが、決着はつかない。\n"
         "やっと落ち着いた2人は、酒をつぎあいながら話す。エレーナは、ナターシャが自分たちを置いてレッドルームから一人で逃げたことを責める。",
         "A sisterly brawl",
         "The sisters fight before they talk. Furniture breaks, plates shatter, and knives come out, but neither wins.\n"
         "Finally calm, they pour drinks and talk. Yelena resents Natasha for escaping the Red Room alone and leaving the rest behind."),
        ("生きていたドレイコフ",
         "ナターシャは、昔ブダペストでドレイコフを爆弾で殺し、レッドルームを終わらせたと思っていた。それがシールドに入るための最後の試験だった。\n"
         "しかしエレーナは、ドレイコフは生きていて、レッドルームは今も世界中にウィドウを送りこんでいると話す。赤いガスがあれば、あやつられているウィドウたちを救える。",
         "Dreykov is alive",
         "Natasha believed she'd killed Dreykov with a bomb in Budapest years ago, ending the Red Room. It was her final test to join S.H.I.E.L.D.\n"
         "But Yelena tells her Dreykov is alive, and the Red Room still sends Widows all over the world. With the red gas, the controlled Widows could be saved."),
        ("ウィドウたちの襲撃",
         "そこへ、小びんを取り返しに来たウィドウたちが襲いかかる。エレーナは隠れ家にしかけていた爆弾で部屋を爆破し、2人は屋根づたいに逃げる。",
         "The Widows strike",
         "Widows sent to recover the vials burst in. Yelena blows up the safe house with the explosives she rigged, and the sisters flee across the rooftops."),
        ("ブダペストの追いかけっこ",
         "2人はエレーナのバイクで逃げる。ナターシャは、エレーナのポケットからこっそり鍵を取っていて、自分が運転する。後ろから、タスクマスターの装甲車が街の車を押しつぶしながら追ってくる。\n"
         "ウィドウに撃たれたバイクは壁にぶつかり、2人は通りがかりの人から車を奪って逃げる。エレーナは助手席のドアをけり飛ばしてウィドウにぶつける。\n"
         "しかしタスクマスターの矢で車はひっくり返り、地下鉄の駅の中へ転がり落ちる。",
         "Chase through Budapest",
         "They flee on Yelena's motorcycle; Natasha has pickpocketed the key and drives. Taskmaster follows in an armored vehicle, crushing cars along the way.\n"
         "A Widow's shots send the bike into a wall, and they grab a passerby's car. Yelena kicks off the passenger door into a Widow.\n"
         "Then Taskmaster's arrow flips the car, and it tumbles down into a subway station."),
        ("通気口の中",
         "2人は駅の通気口にもぐりこんで、追っ手をやりすごす。ナターシャは、昔ここにクリントと2日間かくれていたと話す。中には、2人が遊んだ三目並べのあとが残っていた。",
         "Inside the vent",
         "They crawl into a ventilation shaft in the station and wait out their hunters. Natasha says she once hid there with Clint for two days; their old tic-tac-toe games are still scratched inside."),
    ]),
    ("第4部 父を連れ出す", "Part 4: Breaking Dad out", [
        ("メイソンのヘリコプター",
         "レッドルームの場所を知るため、2人は父役だったアレクセイに会うことにする。アレクセイは、ロシアの雪原にある刑務所に入れられていた。\n"
         "ナターシャがジェット機がほしいと言うと、メイソンは、それにはもっと時間とお金がいると答え、ヘリコプターを用意する。真っ白な戦闘服も2人分そろえてくれた。",
         "Mason's helicopter",
         "To find the Red Room, the sisters decide to find Alexei, their old 'dad,' who is locked up in a prison in the Russian snowfields.\n"
         "When Natasha asks Mason for a jet, he says that would take more time and money, and gets them a helicopter instead. He also supplies two white combat suits."),
        ("刑務所の腕相撲",
         "刑務所のアレクセイは、ひげを伸ばし、すっかり太っていた。囚人のウルサ・メジャーと腕相撲をしながら、昔キャプテン・アメリカと戦ったと自慢する。その頃キャプテン・アメリカは氷の中にいたはずだと言われ、アレクセイは相手の腕を痛めつける。\n"
         "そこへ、レッド・ガーディアンの人形が届く。中には、ナターシャたちと話すための小さな無線機がかくしてあった。",
         "Arm wrestling in prison",
         "Alexei, now bearded and heavy, arm-wrestles inmate Ursa Major while bragging he once fought Captain America. Told that Cap was frozen in ice back then, Alexei hurts the man's arm.\n"
         "Then a Red Guardian action figure arrives for him. Hidden inside is a tiny earpiece so the sisters can talk to him."),
        ("脱獄と雪崩",
         "ナターシャたちが外から遠隔操作で刑務所の扉を開け、アレクセイは南側の扉をけやぶって外へ出る。囚人と看守が入り乱れる大さわぎの中、ナターシャが降りてきて戦い、アレクセイを助ける。\n"
         "エレーナがやぐらを壊した衝撃で雪崩が起き、刑務所をのみこむ。アレクセイはぎりぎりでヘリコプターに引き上げられ、脱獄に成功する。",
         "Breakout and avalanche",
         "The sisters open the prison's doors remotely, and Alexei kicks his way out through the south door. In the chaos of inmates and guards, Natasha drops in to fight her way to him.\n"
         "Yelena destroys a guard tower, setting off an avalanche that buries the prison. Alexei is hauled into the helicopter at the last second."),
        ("ヘリコプターの中",
         "アレクセイは、任務のあとドレイコフに刑務所へ送られていた。レッドルームが今どこにあるかは知らず、母役だったメリーナなら知っているはずだと言う。",
         "In the helicopter",
         "Dreykov had sent him to prison after the mission. He doesn't know where the Red Room is now, but says Melina, their old 'mom,' would."),
        ("紫の花畑",
         "ヘリコプターは燃料が切れ、サンクトペテルブルクの近く、紫の花が一面に咲く草原に落ちる。3人は無事で、そこから歩いてメリーナの家へ向かう。",
         "A field of purple flowers",
         "The helicopter runs out of fuel and crashes in a field of purple flowers outside Saint Petersburg. All three walk away and head for Melina's home."),
    ]),
    ("第5部 母の農場", "Part 5: Mom's farm", [
        ("豚とメリーナ",
         "メリーナは、草原の中の農場で豚を飼っていた。じつは豚を使って、心をあやつる薬のしくみを研究していた。メリーナは、今もドレイコフとつながっていた。",
         "Melina and the pigs",
         "Melina lives on a farm in the fields, raising pigs. In fact, she uses them to refine the Red Room's mind-control process. She is still connected to Dreykov."),
        ("気まずい家族の食卓",
         "21年ぶりに4人がそろい、食卓を囲む。アレクセイは、昔のレッド・ガーディアンのスーツを苦労して着こんでみせる。\n"
         "しかし話はかみ合わない。エレーナは、自分にとってオハイオの家族は本物だったのに、みんなにとっては任務だったことに怒り、席を立つ。",
         "An awkward family dinner",
         "For the first time in 21 years, the four sit down to dinner together. Alexei squeezes into his old Red Guardian suit.\n"
         "But nothing goes right. Yelena is furious that the Ohio family was real to her but just a mission to the others, and she leaves the table."),
        ("『アメリカン・パイ』",
         "アレクセイは、部屋に行ったエレーナを追いかける。うまく言葉が出ないアレクセイが『アメリカン・パイ』を歌いだすと、エレーナも一緒に歌う。幼いころ、逃げる車の中で2人で歌った曲だった。",
         "\"American Pie\"",
         "Alexei follows Yelena to her room. At a loss for words, he starts singing \"American Pie,\" and Yelena joins in: the song they sang together in the getaway car when she was little."),
        ("ドレイコフへの通報",
         "メリーナは、ナターシャたちが来たことを、すでにドレイコフに知らせていた。ドレイコフの部隊が農場に着き、ナターシャたち3人は捕まって連れ去られる。",
         "A call to Dreykov",
         "Melina has already told Dreykov that Natasha and the others are there. Dreykov's forces arrive at the farm, and the three are captured and taken away."),
    ]),
    ("第6部 空のレッドルーム", "Part 6: The Red Room in the sky", [
        ("空に浮かぶ本部",
         "レッドルームの本部は、空に浮かんで世界を回る巨大な基地だった。メリーナはドレイコフの前に立ち、ナターシャたちを見つけたことをほめられる。\n"
         "しかしドレイコフは、それがメリーナではないと見破る。顔のマスクの下にいたのはナターシャだった。農場でナターシャとメリーナは手を組み、マスクで顔を入れかえて、わざと捕まっていたのだ。",
         "The flying headquarters",
         "The Red Room's headquarters is a huge base flying around the world. 'Melina' stands before Dreykov, who praises her for finding Natasha and the others.\n"
         "But Dreykov sees through it: under a face mask is Natasha. At the farm, Natasha and Melina teamed up, swapped faces with masks, and let themselves be captured."),
        ("入れかわっていたメリーナ",
         "閉じこめられていたナターシャの正体は、メリーナだった。メリーナは、つかまっていたアレクセイとエレーナを自由にする。",
         "Melina, in disguise",
         "The 'Natasha' in the cell is really Melina. She frees Alexei and Yelena."),
        ("ドレイコフの話",
         "ドレイコフは、世界中で動いているウィドウたちを、ここの装置から指図していることを得意げに語る。ナターシャは、レッドルームの少女たちが、親のいない子ではなく、さらわれてきた子どもたちだったと知る。\n"
         "ドレイコフの体からは、ウィドウが彼に手を出せなくなるにおい（フェロモン）が出ていた。ナターシャもドレイコフに殴りかかることができない。",
         "Dreykov talks",
         "Dreykov boasts that he directs Widows all over the world from his control desk here. Natasha learns the Red Room girls weren't orphans: they were stolen children.\n"
         "Dreykov gives off a pheromone that makes it impossible for any Widow to harm him. Natasha can't strike him either."),
        ("タスクマスターの正体",
         "ドレイコフは、タスクマスターの正体を明かす。ブダペストの爆破で死んだと思われていた、ドレイコフの娘アントニアだった。\n"
         "ナターシャはあのとき、ドレイコフの事務所にまだ幼い娘がいると知りながら、クリントと爆破を実行していた。生き残ったアントニアはひどいけがを負い、ドレイコフは命を救うために頭に機械を入れた。そのため、見た相手の動きをそっくりまねできる兵士になり、父に心をあやつられていた。",
         "Taskmaster unmasked",
         "Dreykov reveals who Taskmaster is: his daughter Antonia, thought killed in the Budapest bombing.\n"
         "Back then, Natasha went ahead with the bombing with Clint, knowing Dreykov's young daughter was in the office. Antonia survived, terribly injured, and Dreykov saved her by putting technology in her head. It made her a soldier who can copy anyone's moves, under her father's control."),
        ("自分の鼻を折る",
         "得意になったドレイコフは、手の内を明かしすぎていた。ナターシャは自分の鼻を思いきりぶつけて折り、においを感じる神経を断ち切る。\n"
         "においが効かなくなったナターシャは、ドレイコフに襲いかかる。",
         "Breaking her own nose",
         "Dreykov, overconfident, has revealed too much. Natasha smashes her own nose, breaking it and severing the nerve that lets her smell.\n"
         "No longer bound by the scent, she goes after Dreykov."),
        ("エンジンと独房",
         "メリーナは基地のエンジンの一つを止め、基地はかたむき始める。\n"
         "アレクセイはタスクマスターと戦うが、押されてしまう。ナターシャが助けに飛びこみ、いつもの決めポーズで着地すると、エレーナが大喜びする。アレクセイたちは、タスクマスターを独房に閉じこめる。",
         "The engine and the cell",
         "Melina takes out one of the base's engines, and it starts to tilt.\n"
         "Alexei fights Taskmaster and is losing. Natasha leaps in to help and lands in her signature pose, to Yelena's delight. Together they lock Taskmaster in a cell."),
    ]),
    ("第7部 落ちる基地", "Part 7: The base falls", [
        ("ウィドウたちが自由に",
         "ドレイコフは逃げ出し、ウィドウたちがナターシャを取り囲んで痛めつける。そこへエレーナが来て、赤いガスを爆発させる。ガスを浴びたウィドウたちは、心のあやつりから解き放たれる。",
         "The Widows are freed",
         "Dreykov escapes as Widows surround Natasha and beat her down. Yelena arrives and sets off the red gas. The Widows are freed from mind control."),
        ("データと2本の小びん",
         "ナターシャは、世界中にいるウィドウたちの居場所を、ドレイコフの装置から小さな記録装置に写す。そのあいだに基地は爆発を起こし、空から落ち始める。\n"
         "ナターシャは、こわれずに残った赤いガスの小びん2本を拾う。そして、閉じこめられたタスクマスターを独房から出してやる。",
         "The data and two vials",
         "Natasha copies the locations of Widows around the world from Dreykov's system onto a drive as the base starts exploding and falling from the sky.\n"
         "She picks up the two vials of the red gas that survived, then lets Taskmaster out of the locked cell."),
        ("ドレイコフの最期",
         "メリーナとアレクセイは、飛行機で基地から脱出する。\n"
         "ドレイコフは自分の飛行機で逃げようとする。エレーナは、その飛行機を爆発させ、ドレイコフは死ぬ。エレーナはそのまま空に投げ出される。",
         "Dreykov's end",
         "Melina and Alexei escape the base in a plane.\n"
         "Dreykov tries to flee in his own aircraft. Yelena blows it up, killing him, and is thrown into the open sky."),
        ("空中の戦い",
         "落ちていく基地のかけらの中、ナターシャはパラシュートのないエレーナを追って飛び、空中でパラシュートを渡す。\n"
         "そのあとナターシャは、追ってきたタスクマスターと、落ちながら戦う。",
         "Battle in freefall",
         "Amid the falling wreckage, Natasha dives after Yelena, who has no parachute, and hands her one in midair.\n"
         "Then Natasha fights Taskmaster, who has followed her, as they fall."),
        ("アントニアを自由に",
         "地上に降りたナターシャは、小びんの1本をタスクマスターに使う。心のあやつりが解け、アントニアはやっと自分を取り戻す。",
         "Antonia is freed",
         "On the ground, Natasha uses one vial on Taskmaster. The mind control lifts, and Antonia is finally herself again."),
        ("家族の別れ",
         "自由になったウィドウたちが集まり、メリーナとアレクセイもやって来る。そこへ、ロス長官の部隊が近づいてくる。\n"
         "ナターシャは、最後の小びんと、ウィドウたちの居場所が入った記録装置をエレーナに渡し、残りのウィドウたちを救ってほしいと頼む。家族と別れのあいさつをかわし、エレーナたちはアントニアとウィドウたちを連れて去る。ナターシャは一人残る。",
         "The family says goodbye",
         "The freed Widows gather, and Melina and Alexei arrive. Then Ross's forces approach.\n"
         "Natasha gives Yelena the last vial and the drive with the Widows' locations, asking her to free the rest. After their goodbyes, Yelena, Melina and Alexei leave with Antonia and the Widows, and Natasha stays behind alone."),
    ]),
    ("第8部 その後", "Part 8: Afterward", [
        ("2週間後",
         "2週間後。ナターシャは、エレーナからもらったポケットだらけのベストを着て、髪も新しくしている。メイソンは、今度はアベンジャーズの飛行機クインジェットを用意していた。\n"
         "ナターシャは、つかまっているアベンジャーズの仲間たちを救うため、飛び立つ。",
         "Two weeks later",
         "Two weeks later, Natasha wears Yelena's many-pocketed vest and has a new hairstyle. This time, Mason has gotten her a Quinjet.\n"
         "She flies off to free her captured Avengers teammates."),
        ("エンドクレジットの後",
         "『エンドゲーム』のあと。犬を連れたエレーナが、オハイオにあるナターシャの墓を訪れる。\n"
         "そこにヴァレンティーナが現れ、ナターシャが死んだのはクリント・バートン（ホークアイ）のせいだと告げる。そして、次にねらう相手としてクリントの写真を見せる。",
         "After the credits",
         "After Endgame, Yelena visits Natasha's grave in Ohio with a dog.\n"
         "Valentina shows up and tells her Clint Barton (Hawkeye) is to blame for Natasha's death, then hands her Clint's photo as her next target."),
    ]),
    ("まとめ", "Summary", [
        ("ナターシャがしたこと",
         "子どものころ偽の家族としてオハイオで暮らし、レッドルームでスパイに育てられた（第1部）。昔ブダペストで、幼い娘がいると知りながらドレイコフの事務所を爆破していた（第6部）。\n"
         "協定違反で追われる中、エレーナと再会してドレイコフが生きていると知り（第3部）、家族を集め直して（第4部・第5部）、自分の鼻を折ってドレイコフのしかけを破った（第6部）。最後はアントニアを自由にし、エレーナにウィドウたちを託した（第7部）。",
         "What Natasha did",
         "As a child she lived in Ohio as part of a fake family, then was trained as a spy in the Red Room (Part 1). Years ago in Budapest, she bombed Dreykov's office knowing his young daughter was there (Part 6).\n"
         "On the run, she reunited with Yelena and learned Dreykov was alive (Part 3), brought the family back together (Parts 4 and 5), and broke her own nose to defeat Dreykov's lock (Part 6). In the end she freed Antonia and entrusted the Widows to Yelena (Part 7)."),
        ("エレーナと「両親」",
         "エレーナは、赤いガスで心のあやつりが解け（第2部）、ナターシャに小びんを送った。最後はドレイコフの飛行機を爆破し（第7部）、残りのウィドウたちを救う役目を引き受けた。\n"
         "アレクセイは任務のあとドレイコフに刑務所へ送られていた（第4部）。メリーナはドレイコフの下で研究を続けていたが、ナターシャと手を組んで顔を入れかえ、基地のエンジンを止めた（第5部・第6部）。",
         "Yelena and the 'parents'",
         "Freed by the red gas (Part 2), Yelena mailed the vials to Natasha. In the end she blew up Dreykov's aircraft (Part 7) and took on the job of freeing the remaining Widows.\n"
         "Alexei had been sent to prison by Dreykov after the mission (Part 4). Melina kept working for Dreykov, but teamed up with Natasha, swapped faces with her, and took out the base's engine (Parts 5 and 6)."),
        ("ドレイコフとアントニア",
         "ドレイコフは、さらってきた少女たちを薬とにおいのしかけで支配し、世界中でウィドウとして使っていた（第6部）。娘アントニアも、頭の機械と薬であやつり、タスクマスターとして戦わせていた。\n"
         "アントニアは、ナターシャに赤いガスを使われて自由になり（第7部）、エレーナたちと一緒に去った。",
         "Dreykov and Antonia",
         "Dreykov controlled kidnapped girls with drugs and a pheromone lock, using them as Widows worldwide (Part 6). He controlled his own daughter Antonia too, making her fight as Taskmaster.\n"
         "Natasha freed Antonia with the red gas (Part 7), and she left with Yelena and the others."),
        ("死んだ人たち（話の順に）",
         "・オクサナ（第2部）：レッドルームから逃げた元ウィドウ。あやつられたエレーナに襲われて致命傷を負い、エレーナに赤いガスを浴びせて自由にしたあと、息を引き取る。\n"
         "・ドレイコフ（第7部）：落ちる基地から自分の飛行機で逃げようとしたが、エレーナにその飛行機を爆破されて死ぬ。\n"
         "・ナターシャ（エンドクレジットの後で語られる）：『エンドゲーム』で亡くなっている。ヴァレンティーナは、それをクリントのせいだとエレーナに言う。",
         "Who died (in order)",
         "- Oksana (Part 2): a Widow who escaped the Red Room. Fatally wounded by the mind-controlled Yelena, she frees Yelena with the red gas before she dies.\n"
         "- Dreykov (Part 7): fleeing the falling base in his aircraft, he dies when Yelena blows it up.\n"
         "- Natasha (mentioned after the credits): she died in Endgame. Valentina tells Yelena that Clint is to blame."),
    ]),
]
