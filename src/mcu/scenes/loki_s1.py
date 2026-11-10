# 『ロキ』シーズン1 シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（第1話から始め、場面ごとに起きた事実だけ）。
# 英語版ウィキペディアの各話のあらすじ（Plot）と制作の解説、各話の解説記事（検索）で事実と順番を確かめた。
# 資料どうしで食い違う所・確かめられない細かい所（せりふの言い回し、誰が手を下したかなど）は書いていない。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「話-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1話 栄光ある目的", "Episode 1: Glorious Purpose", [
        ("2012年のニューヨークから消えたロキ",
         "2012年のニューヨーク。アベンジャーズとの戦いに負けてつかまったロキの前に、未来から来たアベンジャーズとの騒ぎでテッセラクト（四角い青い石の箱）が転がってくる。ロキはそれを拾い、その場から消える。本当ならロキはここでアスガルドへ連れ戻されるはずだったので、この瞬間に時間の流れの「枝分かれ」が生まれる。\n"
         "ロキが着いたのは、モンゴルのゴビ砂漠だった。地元の人たちの前で、自分は王になる者だと大げさに語り始める。",
         "Loki vanishes from New York, 2012",
         "New York, 2012. Loki, defeated and captured by the Avengers, sees the Tesseract slide across the floor in the chaos caused by the time-traveling Avengers. He grabs it and vanishes. He was supposed to be taken back to Asgard, so this moment creates a branch in the flow of time.\n"
         "He lands in the Gobi Desert in Mongolia and starts grandly telling the locals he is destined to rule."),
        ("TVAに逮捕される",
         "そこへ、光の門から武装した一団が現れる。時間の流れを守る組織TVAの隊員たちだ。リーダーのハンターB-15は、時間を止める棒でロキを打ち、ゆっくりにしか動けなくする。ロキは「神聖時間軸に対する罪」で逮捕され、テッセラクトも取り上げられる。\n"
         "TVAの本部では、ロキの魔法が使えない。ロキは何人もの受付を回らされる。服を取り上げられ、機械で体を調べられ、これまでの人生の言葉をすべて記録した、とても長い書類に署名させられる。受付のケイシーの机には、取り上げたテッセラクトが置かれる。",
         "Arrested by the TVA",
         "Armed agents step out of a glowing door: the TVA, the organization that guards the flow of time. Their leader, Hunter B-15, strikes Loki with a time stick that slows him down. He is arrested for crimes against the Sacred Timeline, and the Tesseract is confiscated.\n"
         "At TVA headquarters, Loki's magic does not work. He is passed from desk to desk: his clothes are taken, a machine scans him, and he must sign an enormously long record of every word he has ever said. The Tesseract ends up on the desk of a clerk named Casey."),
        ("メビウスの事件現場",
         "そのころ、TVAの捜査官メビウス・M・メビウスは、1549年のフランス、エクス＝アン＝プロヴァンスの教会で、事件を調べている。変異体を追ってきたTVAの隊員たちが殺されていた。同じような襲撃が続いている。\n"
         "教会に入ってきた地元の子どもは、だれが殺したのかと聞かれ、悪魔のステンドグラスを指さす。子どもの歯は青く染まっていた。持っていたのは、その時代にはあるはずのない「カブルーイ」という青いお菓子だった。メビウスはそれを手がかりとして持ち帰る。",
         "Mobius's crime scene",
         "Meanwhile, TVA agent Mobius M. Mobius is investigating a church in Aix-en-Provence, France, in 1549. TVA soldiers sent after a variant have been killed there, one of a string of similar attacks.\n"
         "A local child who wanders in is asked who killed them and points to a stained-glass devil. The child's teeth are stained blue from \"Kablooie,\" a blue candy that should not exist in that era. Mobius takes it as a clue."),
        ("ミス・ミニッツの説明と裁判",
         "待合室で、TVAの案内役のアニメの時計ミス・ミニッツが映像で説明する。昔、たくさんの時間の流れどうしが争う大きな戦争があった。それを終わらせた「時間の番人」の3人が、時間の流れを1本にまとめ、それを守るためにTVAを作った。決められた流れから外れる者は「変異体」と呼ばれ、外れた時間の流れは「リセット（消去）」される。\n"
         "裁判で、判事ラヴォーナ・レンスレイヤーの前に立ったロキは、最初はまじめに取り合わない。そのあと「時間旅行をしたのはアベンジャーズのほうだ」と言い張る。ラヴォーナは、アベンジャーズの行動は決められた流れのとおりで、外れたのはロキだと退ける。ロキは有罪となり、消されることになる。\n"
         "その時、TVAに戻ってきたメビウスが割って入る。この変異体のロキは役に立つかもしれないと考え、ロキを引き取る。",
         "Miss Minutes and the trial",
         "In a waiting room, the TVA's animated clock mascot, Miss Minutes, explains in a video: long ago, timelines fought a great multiversal war. The three Time-Keepers ended it, merged time into a single flow, and created the TVA to protect it. Anyone who strays from that flow is a \"variant,\" and stray branches are \"reset.\"\n"
         "At his trial before Judge Ravonna Renslayer, Loki doesn't take it seriously at first, then insists the Avengers were the ones who time-traveled. Ravonna answers that the Avengers' actions followed the set timeline while his did not. He is found guilty and sentenced to be reset.\n"
         "Just then Mobius, back at the TVA, steps in. Thinking this variant Loki might be useful, he takes custody of him."),
        ("映像の部屋で見せられた人生",
         "メビウスは、ロキの人生の映像を見られる部屋にロキを連れていく。ニューヨークでアベンジャーズに負けた場面を見せながら、なぜ人を傷つけるのかと問う。映像には、ロキが昔の有名な飛行機強盗D・B・クーパーとして飛行機から飛び降りた場面もあった。\n"
         "ロキは「自分は王になって、人々を『まちがった選択をする苦しみ』から自由にしてやるのだ」と言い、TVAに自分の運命を決められるのは許さないと反発する。\n"
         "そこでメビウスは、ロキが本来たどるはずだった未来を見せる。ロキのせいで、育ての母フリッガが殺されてしまう場面だ。ロキは怒って取り乱す。",
         "His life on screen",
         "Mobius brings Loki to a room where scenes from his life can be replayed. He shows Loki's defeat by the Avengers in New York and asks why he hurts people. One clip even shows Loki as the famous hijacker D. B. Cooper, jumping from a plane.\n"
         "Loki says he wants to rule so he can free people from the burden of making wrong choices, and he rejects the idea that the TVA decides his fate.\n"
         "So Mobius shows him the future he was meant to have: his adoptive mother Frigga killed because of him. Loki is furious and shaken."),
        ("引き出しのインフィニティ・ストーン",
         "ロキは隙を見て逃げ出し、ケイシーの机からテッセラクトを取り返す。ところが、机の引き出しには、インフィニティ・ストーンがいくつも無造作に入っていた。TVAの中では、石の力も効かない。ここでは石もただの文鎮にすぎなかった。\n"
         "TVAの力の大きさを思い知ったロキは、映像の部屋に戻り、ひとりで自分の未来の続きを見る。兄ソーと仲直りしていくこと、父オーディンの死、そして自分がサノスに首をしめられて死ぬ場面。ロキは、元の時間の流れにはもう戻れないと悟る。",
         "Infinity Stones in a drawer",
         "Loki escapes and takes the Tesseract back from Casey's desk. But the desk drawer holds several Infinity Stones tossed in carelessly. Their power doesn't work inside the TVA; here they're just paperweights.\n"
         "Overwhelmed by the TVA's power, Loki returns to the screening room and watches the rest of his future alone: making peace with his brother Thor, the death of his father Odin, and his own death at Thanos's hands. He realizes he can never return to his timeline."),
        ("変異体を追う仕事",
         "メビウスが戻ってくる。ロキは、自分が悪いことをしてきたのは、自分の人生を思いどおりにしたかったからだと打ち明ける。\n"
         "メビウスは、ロキに仕事を持ちかける。TVAの隊員を何人も殺し、時間の流れを消すための道具を盗んでいる変異体がいる。それを捕まえるのを手伝ってほしい。その犯人は、別の時間のロキだった。",
         "The job",
         "Mobius returns. Loki admits that everything bad he has done came from wanting control over his own life.\n"
         "Mobius makes him an offer: a variant has been killing TVA soldiers and stealing the devices the TVA uses to reset timelines. He wants Loki's help catching it. The culprit is another Loki."),
        ("1858年のオクラホマ",
         "1858年のアメリカ、オクラホマ。TVAの隊員たちが、その時代にはあるはずのない物を見つけて調べている。遠くにフードをかぶった人物が現れ、隊員たちは炎に包まれる。",
         "Oklahoma, 1858",
         "Oklahoma, 1858. TVA soldiers are examining an object that should not exist in that era. A hooded figure appears in the distance, and the soldiers are engulfed in flames."),
    ]),
    ("第2話 変異体", "Episode 2: The Variant", [
        ("1985年の中世まつり",
         "1985年のアメリカ、ウィスコンシン州オシュコシュ。中世の衣装で人が集まるお祭りの会場に、TVAの部隊が来る。そこで変異体に襲われる。変異体は、人の体をのっとる魔法で隊員どうしを戦わせ、ハンターC-20を連れ去る。",
         "A Renaissance fair, 1985",
         "Oshkosh, Wisconsin, 1985. A TVA squad arrives at a Renaissance fair and is ambushed by the variant, who uses magic to possess people and turn the soldiers against each other, then takes Hunter C-20."),
        ("現場でのかけひき",
         "ロキはメビウスやB-15と一緒に、その現場へ向かう。B-15はロキの隠していたナイフを取り上げる。ロキは「変異体はまだ近くにいる」と言って時間をかせぎ、時間の番人に会わせろ、捕まえた後に自分を消さないと約束しろ、と取り引きを持ちかける。\n"
         "メビウスはロキのうそを見ぬき、TVAはその枝分かれした時間を消す。",
         "Bargaining at the scene",
         "Loki joins Mobius and B-15 at the scene. B-15 takes away the knives he has hidden. Loki stalls, claiming the variant is still nearby, and tries to bargain: let him meet the Time-Keepers, and promise not to erase him once the variant is caught.\n"
         "Mobius sees through the lie, and the TVA resets that branch."),
        ("資料を読むロキ",
         "TVAに戻ると、ラヴォーナはロキを使うことに反対する。メビウスは、もう一度だけチャンスをくれとたのむ。\n"
         "ロキは、変異体が起こした事件の資料を夜通し読みあさる。その中で、アスガルドが「ラグナロク」で滅びたことも知る。\n"
         "そしてロキは気づく。変異体は「世界が終わる直前の場所」に隠れているのではないか。どうせすぐ全部が消える場所なら、何をしても時間の流れは変わらないので、TVAに見つからないからだ。",
         "Loki reads the files",
         "Back at the TVA, Ravonna objects to using Loki. Mobius asks for one more chance.\n"
         "Loki reads the variant's case files all night, and along the way learns that Asgard was destroyed in Ragnarok.\n"
         "Then he has an idea: the variant may be hiding in places just before an apocalypse. If everything there is about to be destroyed, nothing done there changes the timeline, so the TVA never notices."),
        ("ポンペイで確かめる",
         "ロキとメビウスは、その考えを確かめるため、紀元79年のポンペイへ行く。ベスビオ火山の噴火の直前だ。ロキは町の人たちに大声で「火山が噴火するぞ」と知らせて回るが、TVAの機械には何の枝分かれも出ない。考えは正しかった。\n"
         "2人は、「すべてが決められているなら、自由な意思はあるのか」と話し合う。",
         "Testing it in Pompeii",
         "To test the idea, Loki and Mobius go to Pompeii in 79 AD, just before Mount Vesuvius erupts. Loki runs around shouting warnings to the townspeople, but the TVA's instruments register no branch. He was right.\n"
         "They debate whether free will exists if everything is already decided."),
        ("ガムの手がかり",
         "1549年のフランスの事件現場で見つかったお菓子「カブルーイ」が手がかりになる。ロキとメビウスは、変異体が、2050年のアメリカ・アラバマ州の町が大きな嵐で滅びる直前に隠れていると突きとめる。",
         "The gum clue",
         "The Kablooie candy found at the 1549 crime scene in France becomes the key. Loki and Mobius work out that the variant is hiding in a town in Alabama in 2050, just before it is destroyed by a huge hurricane."),
        ("嵐の中の大型店",
         "ロキとメビウス、B-15たちは、嵐から逃げてきた人たちが集まる大型店「ロックスカート」に入る。ロキは一人で店の中を調べる。\n"
         "変異体は、B-15の体をのっとり、次々に近くの客や店員の体へと乗り移りながら話しかけてくる。\n"
         "いっぽう隊員たちは、連れ去られていたC-20を見つける。C-20はひどくおびえていて、変異体に時間の番人の居場所を話してしまったと言う。",
         "The superstore in the storm",
         "Loki, Mobius, B-15 and the others enter Roxxcart, a superstore where people have taken shelter from the storm. Loki searches the store on his own.\n"
         "The variant possesses B-15, then jumps from body to body through nearby shoppers and staff as she talks to him.\n"
         "Meanwhile, the soldiers find the missing C-20. Terrified, she says she told the variant where the Time-Keepers are."),
        ("変異体の正体",
         "変異体はフードを取り、女性の姿のロキとして現れる。ロキは「一緒に時間の番人を倒そう」と持ちかけるが、相手は断る。\n"
         "変異体は、TVAから盗んだ爆弾（時間の流れを消すための道具）を一斉に動かし、時間の流れのあちこちへ送りこむ。いくつもの時代で一度に枝分かれが起き、TVAは大混乱になる。\n"
         "変異体は光の門をくぐって逃げる。ロキも、あとを追って飛びこむ。",
         "The variant revealed",
         "The variant lowers her hood: she is a female Loki. Loki proposes they overthrow the Time-Keepers together, but she refuses.\n"
         "She activates the stolen TVA reset charges and sends them to many points along the timeline. Branches erupt across many eras at once, throwing the TVA into chaos.\n"
         "She escapes through a time door, and Loki jumps in after her."),
    ]),
    ("第3話 ラメンティス", "Episode 3: Lamentis", [
        ("C-20の思い出",
         "アラバマの嵐の前のこと。変異体は、捕まえたC-20の頭の中に、C-20がTVAに来る前の暮らしの思い出を映し出していた。2人は店で飲み物を飲みながら話している。変異体はそうして、時間の番人の居場所を聞き出していた。",
         "C-20's memory",
         "Before Alabama: the variant had projected a memory from C-20's life before the TVA into her mind. The two chat over drinks at a bar, and that is how the variant got the Time-Keepers' location out of her."),
        ("TVAでの争いと、逃げた先",
         "アラバマから門をくぐった2人は、TVAの本部に出る。変異体は時間の番人のもとへ向かおうとし、ロキはそれを捕まえようとして、2人は争う。\n"
         "そこへラヴォーナが現れ、2人をまとめて攻撃する。ロキは変異体の持っていた、時間を移動する装置テンパッドを使い、変異体と一緒に別の場所へ飛ぶ。",
         "A fight at the TVA, and an escape",
         "Through the door from Alabama, the two arrive at TVA headquarters. The variant heads for the Time-Keepers while Loki tries to capture her, and they fight.\n"
         "Ravonna appears and attacks them both. Loki uses the variant's TemPad, a time-travel device, to jump away with her."),
        ("ラメンティス1、2077年",
         "2人が着いたのは、2077年の「ラメンティス1」。すぐ近くの星にぶつかって、もうすぐ滅びる月だった。ところがテンパッドは電池が切れていて、どこへも行けない。\n"
         "充電のしかたを知っているのは変異体だけ。いっぽうロキは、テンパッドを魔法で隠してしまう。2人は、しかたなく手を組むことにする。月から人々を逃がす宇宙船「箱舟」へ行けば、テンパッドを充電できるかもしれない。",
         "Lamentis-1, 2077",
         "They land on Lamentis-1 in 2077, a moon about to be crushed by its planet. But the TemPad's battery is dead.\n"
         "Only the variant knows how to recharge it, and Loki has hidden the TemPad with magic. Reluctantly, they team up. The Ark, a ship evacuating people from the moon, might give them the power they need."),
        ("箱舟へ向かう列車",
         "2人は、箱舟へ向かう列車にこっそり乗りこむ。最初はけんか腰だったが、少しずつ自分のことを話し合う。ロキは、母フリッガに魔法を教わったことを話す。変異体は、自分の名前を「シルヴィ」だと言い、魔法は独学で身につけたと話す。恋の話もする。",
         "The train to the Ark",
         "They sneak onto a train headed for the Ark. Hostile at first, they slowly open up. Loki talks about learning magic from his mother Frigga. The variant says her name is Sylvie and that she taught herself magic. They also talk about love."),
        ("酔ったロキの歌",
         "ロキは列車の食堂の車両で酒を飲んで酔っぱらい、アスガルドの歌を大声で歌う。乗客たちは盛り上がるが、乗る資格のない2人は目立ってしまう。\n"
         "見回りの者たちに見つかって争いになり、ロキは列車から外に放り出される。シルヴィもあとを追って飛び降りる。その時、テンパッドはこわれてしまった。",
         "Loki's drunken song",
         "In the dining car, Loki gets drunk and loudly sings an Asgardian song. The passengers love it, but the two, who have no right to be aboard, draw attention.\n"
         "Guards fight them, and Loki is thrown off the train. Sylvie jumps after him. In the process, the TemPad breaks."),
        ("隊員たちの正体",
         "2人は、歩いて箱舟をめざし、箱舟をうばって逃げようと計画を変える。\n"
         "歩きながら、シルヴィはロキに大事なことを話す。TVAで働いている人たちは、みんな、もともと時間の流れの中で暮らしていた変異体だという。記憶を消されているので、本人たちはそれを知らない。ロキは、隊員たちは時間の番人に作られたと聞かされていたので、驚く。",
         "Who the agents really are",
         "The two set out on foot, planning to steal the Ark itself.\n"
         "On the way, Sylvie tells Loki something important: everyone working at the TVA is a variant who once lived in the timeline. Their memories have been wiped, so they don't know it. Loki, told the agents were created by the Time-Keepers, is stunned."),
        ("壊れる箱舟",
         "町には空から星のかけらが降りそそぎ、逃げまどう人々であふれている。2人は見張りの者たちと戦いながら、箱舟のすぐそばまでたどり着く。\n"
         "しかし目の前で、箱舟は落ちてきた大きなかけらに当たって壊れてしまう。2人は、滅びる月に取り残される。",
         "The Ark falls",
         "Fragments rain from the sky onto a town full of panicking people. Fighting through the guards, the two get right up to the Ark.\n"
         "But before their eyes, the Ark is struck by a falling fragment and destroyed. They are stranded on the dying moon."),
    ]),
    ("第4話 ネクサス・イベント", "Episode 4: The Nexus Event", [
        ("幼いシルヴィ",
         "ずっと昔。TVAの隊員だったラヴォーナが、アスガルドにいた幼いシルヴィを「神聖時間軸に対する罪」で捕まえ、シルヴィのいた時間の流れを消す。\n"
         "TVAに連れて来られたシルヴィは、裁判の途中でラヴォーナのテンパッドを奪い、時間の流れの中へ逃げ出す。",
         "Young Sylvie",
         "Long ago. Ravonna, then a TVA hunter, arrests a young Sylvie on Asgard for crimes against the Sacred Timeline and erases her timeline.\n"
         "Brought to the TVA, Sylvie steals Ravonna's TemPad during her trial and escapes into the timeline."),
        ("C-20はどうなった",
         "今のTVA。メビウスはラヴォーナに、C-20に会わせてほしいとたのむ。ラヴォーナは「C-20は、変異体の魔法で心がこわれて死んだ」と答える。",
         "What happened to C-20",
         "At the present-day TVA, Mobius asks Ravonna to let him see C-20. Ravonna says C-20 died after her mind broke under the variant's enchantment."),
        ("滅びる月で生まれた絆",
         "ラメンティス1。降りそそぐかけらの中で、ロキとシルヴィは並んで座り、話をする。シルヴィは、ずっと世界の終わりに隠れながら逃げ続けてきたことを話す。\n"
         "2人の間に、強い気持ちのつながりが生まれる。この瞬間、時間の流れに、それまでにない大きな枝分かれ（ネクサス・イベント）が起きる。TVAはそれに気づいて2人を見つけ、連れ戻す。",
         "A bond on a dying moon",
         "On Lamentis-1, amid the falling debris, Loki and Sylvie sit side by side and talk. Sylvie describes a life spent on the run, hiding in apocalypses.\n"
         "A strong emotional bond forms between them, and in that moment it creates a huge, unprecedented branch: a Nexus Event. The TVA detects it, finds them, and brings them back."),
        ("シフの時間の牢屋",
         "TVAでロキとシルヴィは引き離される。メビウスはロキを、同じ時間がくり返される牢屋に入れる。そこでは、ロキがアスガルドでいたずらをして、戦士シフの髪をひと房切り取った場面が何度もくり返され、そのたびにシフはロキをなぐり、「お前はずっとひとりぼっちだ」と言う。\n"
         "メビウスはロキを牢屋から出して、枝分かれが起きた理由を問いつめる。ロキがシルヴィに恋をしたと気づき、自分のことが大好きなロキらしいと、からかう。\n"
         "ロキは「TVAの職員はみんな変異体だ」と伝えるが、メビウスはロキを再び牢屋にもどす。",
         "Sif's time loop",
         "At the TVA, Loki and Sylvie are separated. Mobius locks Loki in a time-loop cell, replaying the moment on Asgard when Loki cut the warrior Sif's hair as a prank. Each time, Sif beats him and tells him he will always be alone.\n"
         "Mobius pulls him out to question him about the branch. Realizing Loki has fallen for Sylvie, he mocks him for being so in love with himself.\n"
         "Loki tells him the TVA's staff are all variants, but Mobius sends him back into the loop."),
        ("メビウスが見た記録と、B-15",
         "メビウスはラヴォーナのテンパッドをこっそり持ち出し、中の記録を見る。そこには、心がこわれたはずのC-20が、ラヴォーナの取り調べにしっかり答えている姿があった。C-20は、TVAの職員は変異体だと話していた。ロキの言ったことは本当だった。\n"
         "いっぽう、変異体に体をのっとられた時にほかの記憶を見てしまっていたB-15は、シルヴィを連れ出して2050年のアラバマへ行く。そして、自分がTVAに来る前の記憶を見せてほしいとたのむ。B-15は、自分も変異体だったと知る。",
         "Mobius's discovery, and B-15",
         "Mobius secretly takes Ravonna's TemPad and finds a recording: C-20, supposedly broken, calmly answering Ravonna's questions and saying the TVA's staff are variants. Loki was telling the truth.\n"
         "Meanwhile B-15, who glimpsed memories when the variant possessed her, takes Sylvie to Alabama in 2050 and asks to see her own life before the TVA. She learns she too is a variant."),
        ("メビウスの剪定",
         "メビウスは牢屋からロキを出す。そこへラヴォーナと隊員たちが現れる。メビウスは、自分がラヴォーナを裏切ったこと、そして自分も変異体だと気づいたことを認める。\n"
         "ラヴォーナの命令で、メビウスは「剪定」（消されること）される。メビウスの体は消え、死んだように見える。",
         "Mobius is pruned",
         "Mobius frees Loki from the cell, but Ravonna and her soldiers confront them. Mobius admits he betrayed her and that he knows he is a variant.\n"
         "On Ravonna's order, Mobius is pruned. He vanishes and seems to be dead."),
        ("時間の番人の正体",
         "ラヴォーナは、ロキとシルヴィを時間の番人の前へ連れていく。途中でシルヴィは、なぜ子どもの自分を捕まえたのかとたずねるが、ラヴォーナは「覚えていない」と答える。\n"
         "時間の番人は、2人を消せと命じる。その瞬間、B-15が2人の手かせを外す。ロキとシルヴィは力を合わせ、ラヴォーナと見張りの隊員たちと戦って倒す。B-15は気を失う。\n"
         "シルヴィが時間の番人の1人の首を落とすと、それは中身のない機械の人形だった。3人とも、ただの作り物だった。",
         "The truth about the Time-Keepers",
         "Ravonna takes Loki and Sylvie before the Time-Keepers. On the way, Sylvie asks why she was arrested as a child; Ravonna says she doesn't remember.\n"
         "The Time-Keepers order them deleted. At that moment B-15 releases their restraints. Loki and Sylvie fight together and defeat Ravonna and the guards; B-15 is knocked out.\n"
         "Sylvie cuts off a Time-Keeper's head: it's an empty mechanical puppet. All three are fakes."),
        ("ロキの剪定",
         "ロキはシルヴィに自分の気持ちを伝えようとする。しかしその時、起き上がったラヴォーナがロキを剪定し、ロキは消えてしまう。\n"
         "怒ったシルヴィはラヴォーナを押さえつけ、TVAの本当のことをすべて話せと迫る。",
         "Loki is pruned",
         "Loki tries to tell Sylvie how he feels. But Ravonna gets up and prunes him, and he vanishes.\n"
         "Enraged, Sylvie overpowers Ravonna and demands the truth about the TVA."),
        ("エンドクレジットの途中",
         "消えたはずのロキが、がれきの散らばる場所で目を覚ます。目の前には、4人の別のロキたちが立っていた。彼らは、ここで生き延びたいなら一緒に来いと言う。",
         "Mid-credits",
         "Loki, supposedly erased, wakes up in a place strewn with ruins. Four other Lokis stand before him and tell him to come with them if he wants to survive."),
    ]),
    ("第5話 神秘への旅", "Episode 5: Journey into Mystery", [
        ("シルヴィとラヴォーナ",
         "TVAでは、シルヴィがラヴォーナを問いつめている。ラヴォーナは、TVAを作ったのが誰かは自分も知らないと言う。剪定されたものは消えるのではなく、時間の果ての荒れ地「ヴォイド」に送られ、そこから戻った者はいない、とも話す。2人は、TVAを作った者はヴォイドのさらに向こうに隠れているのだろうと考える。\n"
         "ラヴォーナとミス・ミニッツは時間かせぎをして、隊員たちを呼び寄せる。捕まりそうになったシルヴィは、自分で自分を剪定する。\n"
         "ラヴォーナは、牢屋に入れたB-15を問いつめたあと、TVAを作った者を探すのを手伝えとミス・ミニッツに命じる。",
         "Sylvie and Ravonna",
         "At the TVA, Sylvie interrogates Ravonna, who says even she doesn't know who created the TVA. Pruned things aren't destroyed: they're sent to the Void, a wasteland at the end of time, and no one has ever come back. They conclude that the TVA's creator must be hiding beyond the Void.\n"
         "Ravonna and Miss Minutes stall until soldiers arrive. About to be caught, Sylvie prunes herself.\n"
         "After interrogating the imprisoned B-15, Ravonna tells Miss Minutes to help her find the TVA's creator."),
        ("ヴォイドのロキたち",
         "ヴォイドで、ロキは4人の別のロキと一緒にいる。年をとった「クラシック・ロキ」、子どもの「キッド・ロキ」、自慢ばかりする「ボースタフル・ロキ」、そしてワニの姿の「アリゲーター・ロキ」だ。\n"
         "そこへ、巨大な雲のような怪物アライオスが現れる。アライオスは、ヴォイドにあるものを何でも飲みこんで消してしまう。ロキたちはアライオスから逃げる。",
         "The Lokis of the Void",
         "In the Void, Loki is with four other Lokis: the elderly Classic Loki, the child Kid Loki, the bragging Boastful Loki, and Alligator Loki.\n"
         "Then Alioth appears, a gigantic cloud-like monster that devours anything in the Void. The Lokis flee from it."),
        ("クラシック・ロキの話",
         "ロキたちは、それぞれ自分のことを話す。クラシック・ロキは、サノスに殺されそうになった時、自分が死んだように見せかけて逃げ、ひとりで隠れて暮らしていたと話す。けれど、そのうちひとりでいることがさびしくなったのだという。",
         "Classic Loki's story",
         "The Lokis share their stories. Classic Loki says that when Thanos was about to kill him, he faked his death, escaped, and lived alone in hiding, until he grew lonely."),
        ("シルヴィとメビウス",
         "ヴォイドにやって来たシルヴィは、さっそくアライオスに襲われる。シルヴィは一瞬だけアライオスに魔法をかけるが、危なくなる。そこへ、剪定されたはずのメビウスが現れ、シルヴィを助けて逃げる。メビウスは生きていた。",
         "Sylvie and Mobius",
         "Sylvie arrives in the Void and is attacked by Alioth right away. She enchants it for a moment, but is in danger until Mobius, supposedly erased, appears and helps her escape. Mobius is alive."),
        ("ロキどうしの裏切り",
         "ボースタフル・ロキは、仲間を裏切る。自分が王になるため、ほかのロキの集団（ロキのそっくりさんたちを率いる「プレジデント・ロキ」）に、ロキたちを売ったのだ。\n"
         "ところが、プレジデント・ロキの集団の中でも、ロキどうしが次々に裏切り合い、大乱闘になる。そのすきに、クラシック・ロキがロキ、キッド・ロキ、アリゲーター・ロキを連れて逃がす。4人はシルヴィとメビウスに合流する。",
         "Lokis betraying Lokis",
         "Boastful Loki betrays the group, selling them out to another gang of Lokis led by President Loki so he can rule.\n"
         "But in President Loki's gang, the Lokis start betraying one another too, and a huge brawl breaks out. In the confusion, Classic Loki helps Loki, Kid Loki and Alligator Loki escape. They meet up with Sylvie and Mobius."),
        ("メビウスはTVAへ",
         "シルヴィはラヴォーナから奪ったテンパッドを持っていた。メビウスはそれを使ってTVAに戻り、職員たちに本当のことを伝えると決める。ロキたちも一緒に来るよう誘うが、キッド・ロキたちはヴォイドに残る。\n"
         "ロキとシルヴィは、アライオスに魔法をかけて、その向こうにいる者のところへ行こうと決める。",
         "Mobius goes back",
         "Sylvie has the TemPad she took from Ravonna. Mobius uses it to return to the TVA, determined to tell its staff the truth. He invites the Lokis to come along, but Kid Loki and the others stay in the Void.\n"
         "Loki and Sylvie decide to enchant Alioth and reach whoever is beyond it."),
        ("クラシック・ロキの最期",
         "ロキはアライオスの気をひき、そのすきにシルヴィが魔法をかけようとする。しかし2人ともうまくいかず、アライオスに飲みこまれそうになる。\n"
         "そこへ、残っていたクラシック・ロキが戻ってくる。クラシック・ロキは、自分の魔法の力をふりしぼって、アスガルドの町そのものの大きな幻を作り出し、アライオスの注意を引きつける。2人は助かるが、クラシック・ロキはアライオスに飲みこまれて死ぬ。仲間を守るために、自分の命を投げ出したのだ。",
         "Classic Loki's end",
         "Loki distracts Alioth while Sylvie tries to enchant it, but both fail and they are nearly devoured.\n"
         "Then Classic Loki comes back. Straining all his magic, he conjures a life-size illusion of the city of Asgard to draw Alioth's attention. The two are saved, but Classic Loki is consumed by Alioth and dies, giving his life to protect them."),
        ("怪物の向こうの城",
         "ロキとシルヴィは力を合わせ、2人の魔法でアライオスにかける。アライオスの霧が晴れると、その向こうに時間の果ての城が見える。2人は、城へ向かって歩き出す。",
         "The citadel beyond the monster",
         "Loki and Sylvie work together and enchant Alioth with their combined magic. As the cloud clears, a citadel at the end of time appears beyond it, and they walk toward it."),
    ]),
    ("第6話 永遠に。いつまでも。", "Episode 6: For All Time. Always.", [
        ("城の入口のミス・ミニッツ",
         "時間の果ての城に入ったロキとシルヴィを、ミス・ミニッツが出迎える。ミス・ミニッツは、自分の主人「在り続ける者」からの申し出を伝える。2人を元の時間の流れに戻し、ロキには王の座を、シルヴィには幸せを与えるという。2人はそれを断る。",
         "Miss Minutes at the entrance",
         "Miss Minutes greets Loki and Sylvie as they enter the Citadel at the End of Time. She relays an offer from her master, He Who Remains: he will return them to the timeline, giving Loki sovereignty and Sylvie happiness. They refuse."),
        ("TVAのラヴォーナとメビウス、B-15",
         "TVAでは、ラヴォーナがミス・ミニッツから、在り続ける者が送ってきた情報を受け取る。メビウスはラヴォーナの前に現れ、2人はたがいに相手が裏切ったと責め合う。メビウスはラヴォーナを剪定しようとするが、ラヴォーナはそれをはねのけ、「自由な意思」を探しに行くと言い残して、どこかへ去る。\n"
         "いっぽうB-15は、2018年のアメリカ、オハイオ州フリーモントで、TVAの隊員たちに追われている。B-15は隊員たちに、ある学校の教頭先生を見せる。それはTVAに来る前のラヴォーナ、つまりラヴォーナの変異体だった。TVAの職員がみんな変異体だという証拠だった。",
         "Ravonna, Mobius and B-15",
         "At the TVA, Ravonna receives information that He Who Remains has sent through Miss Minutes. Mobius confronts her, and they accuse each other of betrayal. Mobius tries to prune her, but she overcomes him and leaves, saying she is going in search of free will.\n"
         "Meanwhile, in Fremont, Ohio, in 2018, B-15 is chased by TVA soldiers. She shows them a school vice-principal who is a variant of Ravonna from before the TVA: proof that its staff are all variants."),
        ("城の主はただの人間",
         "城の奥で、ロキとシルヴィは在り続ける者に会う。現れたのが神や怪物ではなく、ただの人間だったことに、2人は驚く。\n"
         "シルヴィが斬りかかっても、在り続ける者はテンパッドで少し先の場所へ飛んでよけてしまう。彼は、過去も今も未来もすべて見てきたので、2人が何をするかも全部分かっていると言う。2人がここへたどり着いたのも、彼が導いたからだった。",
         "The master of the Citadel is just a man",
         "Deep in the Citadel, Loki and Sylvie meet He Who Remains, and are surprised he is neither god nor monster, just a man.\n"
         "When Sylvie attacks, he dodges with a TemPad. He says he has seen all of the past, present and future, so he knows everything they will do. He even guided them here."),
        ("時間の戦争とTVAの始まり",
         "在り続ける者は、TVAが生まれたわけを話す。31世紀、別々の世界にいた彼の変異体（別の世界の自分）たちが、ほかの世界があることに気づき、たがいに連絡を取り合った。その中から、ほかの世界を自分のものにしようとする者たちが現れ、世界どうしの大戦争になった。\n"
         "彼は怪物アライオスの力を使って戦争を終わらせ、自分の時間の流れだけを残した。そして、二度と枝分かれが起きないよう見張るため、TVAを作った。",
         "The war, and the TVA's beginning",
         "He Who Remains explains why the TVA exists. In the 31st century, variants of himself in different universes discovered one another and made contact. Some of them set out to conquer other universes, and a multiversal war began.\n"
         "He used Alioth to end the war, keeping only his own timeline, and created the TVA to make sure no new branches ever formed."),
        ("2つの道",
         "在り続ける者は、もう疲れたと言い、2人に選ばせる。自分を殺せば、時間の流れは1本ではなくなり、もっと悪い自分の変異体たちが現れて、また戦争が起きるかもしれない。あるいは、自分の代わりにTVAを引き継ぎ、時間の流れを守り続けるか。\n"
         "その時、時間の流れが分かれ始める。在り続ける者は、ここから先のことはもう分からないと言う。",
         "Two paths",
         "Saying he has grown tired, He Who Remains offers them a choice. Kill him, and time will no longer be a single flow; worse variants of himself may emerge and start the war again. Or take his place running the TVA and protecting the timeline.\n"
         "Then the timeline starts to diverge, and he says he no longer knows what comes next."),
        ("ロキとシルヴィの争い",
         "シルヴィは在り続ける者を殺そうとする。ロキは、在り続ける者の言うことが本当かもしれないと恐れ、シルヴィを止めようとして戦う。ロキは、ただシルヴィを守りたいのだと伝える。\n"
         "2人はキスをする。しかしその直後、シルヴィはテンパッドでロキをTVAへ送り返してしまう。",
         "Loki and Sylvie fight",
         "Sylvie moves to kill He Who Remains. Loki, afraid he may be telling the truth, fights her to stop it, and tells her he just wants to keep her safe.\n"
         "They kiss, but right after, Sylvie uses the TemPad to send Loki back to the TVA."),
        ("在り続ける者の最期",
         "ひとり残ったシルヴィは、もう抵抗しない在り続ける者の胸を剣で刺して殺す。子どものころに自分の人生を奪ったTVAを、その大もとから終わらせるためだった。在り続ける者はほほえみ、「また会おう」と言い残して死ぬ。\n"
         "時間の流れは、数えきれない枝に分かれていく。もう剪定では止められない、たくさんの世界（マルチバース）が生まれる。",
         "The end of He Who Remains",
         "Alone with him, Sylvie drives her sword into He Who Remains, who no longer resists, to end the TVA that stole her life as a child at its source. He smiles and dies saying she'll see him soon.\n"
         "The timeline splits into countless branches. A multiverse is born that pruning can no longer contain."),
        ("ちがうTVA",
         "TVAに戻ったロキは、メビウスとB-15を見つけ、在り続ける者の変異体たちが来るかもしれないと必死に伝える。ところが2人はロキのことを知らない。メビウスは「君は誰だ」とたずねる。\n"
         "TVAの広間にあった時間の番人の像は、在り続ける者に似た男の像に変わっていた。ロキは、元とは少しちがう世界のTVAに来てしまったのだった。",
         "A different TVA",
         "Back at the TVA, Loki finds Mobius and B-15 and desperately warns them about He Who Remains' variants. But they don't know him. Mobius asks who he is.\n"
         "The statues of the Time-Keepers in the TVA's hall have been replaced by a statue of a man who looks like He Who Remains. Loki has arrived at a TVA in a slightly different world."),
    ]),
    ("まとめ（最終話までのネタバレ）", "Summary (spoilers through the finale)", [
        ("時間の番人とTVAの正体",
         "・時間の番人の3人（第4話）：機械の人形だった。本当にTVAを作ったのは、時間の果ての城にいる在り続ける者（第6話）。\n"
         "・TVAの職員（第3話〜第6話）：シルヴィが言ったとおり、もともと時間の流れの中で暮らしていた人たちで、記憶を消されていた。B-15（第4話）、メビウス（第4話）が自分でそれに気づく。B-15は第6話で、TVAに来る前のラヴォーナ（学校の教頭先生）を見つけて証拠にする。\n"
         "・剪定された者（第5話）：消えるのではなく、時間の果ての荒れ地ヴォイドに送られていた。",
         "The truth about the Time-Keepers and the TVA",
         "- The three Time-Keepers (Ep. 4): mechanical puppets. The TVA's real creator is He Who Remains in the Citadel at the End of Time (Ep. 6).\n"
         "- TVA staff (Eps. 3–6): as Sylvie said, they once lived in the timeline and had their memories wiped. B-15 (Ep. 4) and Mobius (Ep. 4) discover this. In Ep. 6, B-15 finds Ravonna's pre-TVA self, a school vice-principal, as proof.\n"
         "- The pruned (Ep. 5): not destroyed but sent to the Void, a wasteland at the end of time."),
        ("消された人・死んだ人（話の順に）",
         "・TVAの隊員たち（第1話）：変異体（シルヴィ）を追っていた隊員たちが、1549年のフランスの教会などで次々に殺されていた。1858年のオクラホマでも、隊員たちがフードの人物の前で炎に包まれる。\n"
         "・ハンターC-20（第4話）：ラヴォーナは「変異体の魔法で心がこわれて死んだ」と言う。しかし記録には、心がしっかりしたままのC-20がラヴォーナの取り調べに答える姿が残っていた。\n"
         "・メビウス（第4話）：ラヴォーナの命令で剪定されるが、ヴォイドで生きていた（第5話）。\n"
         "・ロキ（第4話）：時間の番人の前で、ラヴォーナに剪定されるが、ヴォイドで生きていた（第5話）。\n"
         "・クラシック・ロキ（第5話）：ロキとシルヴィを守るため、アスガルドの大きな幻でアライオスの気をひき、アライオスに飲みこまれて死ぬ。\n"
         "・在り続ける者（第6話）：TVAを作った男。自分の人生を奪ったTVAを終わらせるため、シルヴィが剣で刺して殺す。",
         "Who was erased or died (in order)",
         "- TVA soldiers (Ep. 1): soldiers hunting the variant (Sylvie) were killed one after another, including in a church in France in 1549. In Oklahoma in 1858, more soldiers are engulfed in flames before a hooded figure.\n"
         "- Hunter C-20 (Ep. 4): Ravonna says her mind broke under the variant's enchantment and she died. But a recording shows a clear-headed C-20 answering Ravonna's questions.\n"
         "- Mobius (Ep. 4): pruned on Ravonna's order, but alive in the Void (Ep. 5).\n"
         "- Loki (Ep. 4): pruned by Ravonna before the Time-Keepers, but alive in the Void (Ep. 5).\n"
         "- Classic Loki (Ep. 5): to protect Loki and Sylvie, he distracts Alioth with a huge illusion of Asgard and is devoured by it.\n"
         "- He Who Remains (Ep. 6): the TVA's creator. To end the TVA that stole her life, Sylvie stabs him to death with her sword."),
    ]),
]
