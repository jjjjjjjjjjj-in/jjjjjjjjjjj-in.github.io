# 『ガーディアンズ・オブ・ギャラクシー：VOLUME 3』（2023年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじ、登場人物の記事（ロケット、ピーター、ガモーラ、ネビュラ、
# マンティス、ドラックス、グルート、コスモ、アダム、アイーシャなど）、検索で見つかった解説記事で事実を確かめた。
# 資料どうしで食い違う所や、確かめられない細かい所（ピーターを部屋に運んだのが誰か、オルゴコープへの潜入の細かい流れ、
# ウォー・ピッグとアダムとガモーラの戦いの順番、アダムがどうやってアレートに来たか、ロケットの記憶が映画のどこに
# はさまるかの正確な位置など）は書いていない。ロケットの記憶の章は、物語が分かりやすい位置にまとめて置いた。
# 日本語版のせりふは、日本語の吹替・字幕の言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 人物名は相関図（relations.py）にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 ノーウェアの襲撃", "Part 1: Attack on Knowhere", [
        ("ロケットの歩く朝",
         "巨大な生き物の頭の骨の中にある街ノーウェア。ガーディアンズはここを買い取り、拠点として建て直していた。\n"
         "ロケットは、レディオヘッドの「クリープ」の静かなアコースティック版を聴きながら、ひとりで街を歩く。",
         "Rocket's morning walk",
         "Knowhere, a city inside the skull of a giant creature. The Guardians have bought it and rebuilt it as their home base.\n"
         "Rocket walks through the town alone, listening to a quiet acoustic version of Radiohead's \"Creep.\""),
        ("酔いつぶれるピーター",
         "ピーターは、サノスに殺されたガモーラを忘れられず、毎日のように酒を飲んでいる。この日も酒場で酔いつぶれ、仲間たちに部屋まで運ばれて寝かされる。\n"
         "仲間たちは、そんなピーターにあきれながらも心配している。",
         "Peter drinks himself out",
         "Peter can't get over Gamora, killed by Thanos, and drinks nearly every day. Again he passes out at the bar, and his friends carry him to bed.\n"
         "They're fed up with him, but worried too."),
        ("金色の若者アダム",
         "そこへ、金色の肌の若者アダム・ウォーロックが空から突っこんでくる。アダムは、前の作品でガーディアンズにうらみを持ったソブリンの女王アイーシャが作り出した戦士で、ロケットを連れ去ろうとしていた。\n"
         "アダムの力は強く、ドラックスやグルートも歯が立たない。マンティスは腕を折られる。",
         "Adam, the golden youth",
         "Then a golden-skinned young man, Adam Warlock, crashes in from the sky. He was created by Ayesha, queen of the Sovereign, who has held a grudge against the Guardians since the last film, and he has come to take Rocket.\n"
         "Adam is so strong that even Drax and Groot can't stop him. Mantis's arm is broken."),
        ("ロケットの大けが",
         "戦いの中で、ロケットは大けがを負って意識を失う。それを見たピーターも戦いに飛びこむ。\n"
         "最後はネビュラが腕の刃でアダムを刺し、傷ついたアダムは逃げていく。",
         "Rocket is gravely hurt",
         "In the fight, Rocket is badly hurt and falls unconscious. Seeing this, Peter throws himself into the battle.\n"
         "In the end Nebula stabs Adam with the blade in her arm, and he flees, wounded."),
        ("治療できない体",
         "マンティスの腕は救急パックですぐに治る。ところがロケットに使おうとすると、体の中にしかけられた装置が反応し、治療すれば命が止まってしまうと分かる。\n"
         "調べると、この「キルスイッチ」は、ロケットを作ったオルゴコープという会社のものだった。止めるには、会社が持っている解除の暗号（パスキー）が必要になる。",
         "A body that can't be healed",
         "A med-pack fixes Mantis's arm at once. But when they try it on Rocket, a device inside his body reacts: treating him would kill him.\n"
         "This kill switch turns out to belong to Orgocorp, the company that made Rocket. To shut it off, they need the override code held by the company."),
        ("出発",
         "ピーターは、ロケットを助けるためにオルゴコープの本社へ行くと決める。ノーウェアの守りは、クラグリンと宇宙犬コスモに任せる。\n"
         "ガーディアンズは、眠ったままのロケットを乗せて新しい船で飛び立つ。",
         "Setting off",
         "Peter decides to go to Orgocorp's headquarters to save Rocket. He leaves Knowhere in the hands of Kraglin and Cosmo the space dog.\n"
         "The Guardians take off in their new ship with Rocket still unconscious aboard."),
    ]),
    ("第2部 ロケットの記憶（1） おりの中の友だち", "Part 2: Rocket's memories (1) Friends in cages", [
        ("子どものアライグマ",
         "眠るロケットは、昔の記憶を思い出していく。地球で生まれたアライグマの赤ちゃんだったロケットは、科学者ハイ・エボリューショナリーにとらえられ、宇宙の実験室へ連れてこられた。\n"
         "ハイ・エボリューショナリーは、動物を作り変えて「完全な生き物」と「理想の社会」を作ろうとしていた。",
         "A baby raccoon",
         "As he sleeps, Rocket remembers. Born a baby raccoon on Earth, he was captured by the scientist known as the High Evolutionary and taken to a lab in space.\n"
         "The High Evolutionary wanted to remake animals into a \"perfect\" species and build an ideal society."),
        ("89P13",
         "ロケットは体に機械を埋めこまれ、手術で作り変えられる。名前はなく、「89P13」という実験の番号で呼ばれた。",
         "89P13",
         "Rocket's body is fitted with machinery and reshaped through surgery. He has no name, only a test-subject number: 89P13."),
        ("3匹の仲間",
         "同じ実験の組（バッチ89）には、カワウソのライラ、セイウチのティーフス、ウサギのフロアがいた。みんな体の一部を機械にされていたが、明るく、ロケットとすぐに仲よくなる。\n"
         "4匹はおりの中で、いつか外に出て、空を見ようと語り合う。ロケットは、空を飛ぶ船を作りたいという夢から、自分を「ロケット」と名づける。",
         "Three friends",
         "His test batch, Batch 89, includes an otter named Lylla, a walrus named Teefs and a rabbit named Floor. All of them have been partly turned into machines, but they're cheerful and quickly become Rocket's friends.\n"
         "In their cages, the four talk about getting out someday and seeing the sky. Dreaming of building ships that fly, 89P13 names himself Rocket."),
    ]),
    ("第3部 オルゴコープへの潜入", "Part 3: Breaking into Orgocorp", [
        ("ラヴェジャーズとガモーラ",
         "ネビュラは、盗賊団ラヴェジャーズに助けを求める。やって来たラヴェジャーズの中には、ガモーラがいた。\n"
         "このガモーラは、『エンドゲーム』で2014年から来た別のガモーラで、ピーターとの思い出を持っていない。ピーターは昔のように話しかけるが、ガモーラは冷たくあしらう。",
         "The Ravagers and Gamora",
         "Nebula calls the Ravagers for help, and among the Ravagers who arrive is Gamora.\n"
         "This is the Gamora who came from 2014 in Endgame, with no memories of Peter. He talks to her as if nothing has changed; she brushes him off."),
        ("生きた本社",
         "オルゴコープの本社は、宇宙に浮かぶ、肉のような生き物でできた建物だった。入るには、同じ素材でできた専用の宇宙服を着なければならない。\n"
         "ピーターたちはガモーラと一緒に中へ向かい、グルートは船に残ってロケットを見守る。",
         "A living headquarters",
         "Orgocorp's headquarters floats in space and is made of living, fleshy material. To get in, they must wear special spacesuits made of the same stuff.\n"
         "Peter and the others head inside with Gamora; Groot stays on the ship to watch over Rocket."),
        ("受付と警備",
         "ガーディアンズは受付係のウラを人質にとって奥へ進む。マスター・カージャたち警備の者が行く手をはばみ、建物の中は大さわぎになる。",
         "Reception and security",
         "The Guardians take the receptionist, Ura, hostage and push deeper in. Master Karja and the other guards try to stop them, and the building erupts in chaos."),
        ("消えていた暗号",
         "ガーディアンズはロケットの記録を見つけ出す。ところが、肝心の解除の暗号は消されていた。消したのは、ハイ・エボリューショナリーの部下の記録係ティールだと分かる。",
         "The code is gone",
         "The Guardians find Rocket's file. But the override code has been removed, and they learn it was taken out by Theel, one of the High Evolutionary's recorders."),
        ("ジェットパックで脱出",
         "警備の者たちに追いつめられるが、ピーターは相手の宇宙服のジェットパックを遠くから動かして吹き飛ばす。グルートが船で迎えに来て、ガーディアンズはなんとか逃げ出す。",
         "Escape by jetpack",
         "Cornered by guards, Peter remotely fires their suits' jetpacks and sends them flying. Groot comes in with the ship, and the Guardians barely get away."),
    ]),
    ("第4部 ハイ・エボリューショナリーの怒り", "Part 4: The High Evolutionary's anger", [
        ("ソブリンへの脅し",
         "ハイ・エボリューショナリーは、ソブリンの人々を作った者でもあった。ロケットを連れて帰れなかったアイーシャに、ロケットを取り戻せなければソブリンを滅ぼすと脅す。\n"
         "アイーシャは、まだ育ちきっていなかったアダムを、この脅しのせいで早く目覚めさせていた。そのためアダムは、力は強いが心は子どものようだった。\n"
         "アイーシャとアダムは、ガーディアンズを追いかけることになる。",
         "A threat to the Sovereign",
         "The High Evolutionary also created the Sovereign. He threatens Ayesha: if she can't bring Rocket back, he will wipe out her people.\n"
         "Pressured by him, Ayesha had awakened Adam before he was fully developed, so Adam is powerful but childlike.\n"
         "Ayesha and Adam set out after the Guardians."),
        ("ラヴェジャーズを問いつめる",
         "アダムたちはラヴェジャーズの1人をつかまえ、ガモーラの連絡からガーディアンズの行き先を聞き出す。アダムはこの男を殺し、男が連れていた小さなペットのブラープは、アダムになついてしまう。",
         "Squeezing a Ravager",
         "Adam and Ayesha catch a Ravager and learn the Guardians' destination from Gamora's messages. Adam kills the man, and the man's small pet, Blurp, ends up attaching itself to Adam."),
        ("行き先はカウンター・アース",
         "暗号を持つティールは、ハイ・エボリューショナリーが作った星カウンター・アースにいると分かる。ガーディアンズはそこへ向かう。",
         "Next stop: Counter-Earth",
         "Theel, who has the code, turns out to be on Counter-Earth, a planet the High Evolutionary built. The Guardians head there."),
    ]),
    ("第5部 ロケットの記憶（2） 天才の89P13", "Part 5: Rocket's memories (2) The genius 89P13", [
        ("かしこくなるロケット",
         "記憶の中で、ロケットはどんどんかしこくなっていく。ハイ・エボリューショナリーは、作り変えた動物たちが乱暴になってしまう問題に悩んでいた。\n"
         "ロケットは、ハイ・エボリューショナリーにも解けなかったその欠点を見つけ出す。",
         "Rocket gets smarter",
         "In his memories, Rocket grows smarter and smarter. The High Evolutionary is stuck on a problem: his remade animals keep turning violent.\n"
         "Rocket finds the flaw that the High Evolutionary himself couldn't."),
        ("科学者の怒り",
         "ハイ・エボリューショナリーは、ロケットの考えを使って次の実験を良くしていく。しかし、自分の作った生き物が自分より先に答えを出したことに腹を立てる。",
         "The scientist's anger",
         "The High Evolutionary uses Rocket's insight to improve later batches. But he is furious that one of his own creations solved what he could not."),
        ("おそろしい計画",
         "ハイ・エボリューショナリーは、ロケットの脳を取り出して研究に使い、ほかのバッチ89の動物たちは焼いて処分すると決める。",
         "A terrible plan",
         "The High Evolutionary decides to remove Rocket's brain for further study and to incinerate the rest of Batch 89."),
    ]),
    ("第6部 カウンター・アース", "Part 6: Counter-Earth", [
        ("地球そっくりの星",
         "カウンター・アースは、アメリカの郊外のような町並みの星だった。住んでいるのは、動物から作り変えられた「アニ・メン」と呼ばれる人々。\n"
         "ガーディアンズは住民の助けを借りて、ハイ・エボリューショナリーのいるアレート研究所の場所をつきとめる。",
         "A planet like Earth",
         "Counter-Earth looks like a suburban American town. Its people are Humanimals, animals remade into people.\n"
         "With help from the locals, the Guardians track down Arête Laboratories, where the High Evolutionary is."),
        ("ガモーラとの言い争い",
         "ガモーラは、ガーディアンズが思いつきで計画を変えることや、ピーターが自分に昔のガモーラの姿を求めることにいらだち、はっきりと文句を言う。",
         "Arguing with Gamora",
         "Gamora is fed up with the Guardians changing plans on a whim, and with Peter wanting her to be the Gamora he lost, and she tells them so."),
        ("二手に分かれる",
         "ピーター、グルート、ネビュラが研究所へ向かい、ドラックスとマンティスはガモーラと一緒に船でロケットを見守る。\n"
         "研究所の入り口で、体に武器を組みこんでいるネビュラは中に入れてもらえず、外で待たされる。ピーターとグルートだけが中へ入る。",
         "Splitting up",
         "Peter, Groot and Nebula go to the lab, while Drax and Mantis stay on the ship with Gamora to watch over Rocket.\n"
         "At the entrance, the guards won't let Nebula in because of the weapons built into her body, so she has to wait outside. Only Peter and Groot go in."),
        ("ドラックスの言いわけ",
         "ドラックスは、ピーターたちを手伝いに行くべきだとマンティスを言いくるめ、2人で船を離れる。ガモーラは、ロケットと2人で残される。",
         "Drax talks Mantis into it",
         "Drax talks Mantis into going after Peter's group, and the two leave the ship. Gamora is left alone with Rocket."),
        ("ロケットを守るガモーラ",
         "ロケットをねらって、ハイ・エボリューショナリーの手下のブタの戦士ウォー・ピッグと、追ってきたアダムがやって来る。\n"
         "ガモーラはロケットを守って戦い、ロケットを乗せたまま船で飛び立つ。",
         "Gamora protects Rocket",
         "War Pig, a pig warrior serving the High Evolutionary, and Adam, still on the hunt, both come for Rocket.\n"
         "Gamora fights to protect him and flies off in the ship with Rocket aboard."),
    ]),
    ("第7部 星をこわす科学者", "Part 7: The scientist who destroys a world", [
        ("ハイ・エボリューショナリーとの対面",
         "ピーターとグルートは、ハイ・エボリューショナリーと向き合う。ピーターが、この星の人々にも暴力や悪いところがあると言うと、ハイ・エボリューショナリーもそれを認める。",
         "Face to face",
         "Peter and Groot come face to face with the High Evolutionary. When Peter says the people of this world have violence and flaws of their own, the High Evolutionary agrees."),
        ("星を消す",
         "ハイ・エボリューショナリーは、うまくいかなかったこの星を消して、作り直すことにする。空から攻撃がふりそそぎ、カウンター・アースの人々はみな死んでいく。\n"
         "アイーシャも巻きこまれ、アダムが助けようとするが間に合わず、死んでしまう。",
         "Wiping out a world",
         "The High Evolutionary decides to erase his failed world and start over. Bombardment rains down from the sky and the people of Counter-Earth are wiped out.\n"
         "Ayesha is caught in it too. Adam tries to save her, but she dies."),
        ("研究所は宇宙船",
         "アレート研究所は、じつは巨大な宇宙船だった。船は飛び立とうとする。\n"
         "外にいたネビュラのもとにドラックスとマンティスがやって来て、3人はピーターたちを助けようと船に乗りこむ。",
         "The lab is a ship",
         "Arête Laboratories is really a giant spaceship, and it begins to lift off.\n"
         "Drax and Mantis reach Nebula outside, and the three board the ship to rescue Peter and Groot."),
        ("ティールを連れて飛び降りる",
         "そのころピーターとグルートは、ハイ・エボリューショナリーの部下たちと戦い、記録係ティールをつかまえて、ティールごと船から飛び降りていた。\n"
         "ティールは2人の下じきになって地面にたたきつけられて死に、2人はティールの体から暗号を取り出す。ガモーラが船で2人を拾い上げる。",
         "Jumping with Theel",
         "Meanwhile, Peter and Groot fight the High Evolutionary's people, grab the recorder Theel and leap off the ship with him.\n"
         "Theel breaks their fall and dies, and the two pull the code from his body. Gamora picks them up in the ship."),
    ]),
    ("第8部 ロケットの記憶（3） 友だちとの別れ", "Part 8: Rocket's memories (3) Losing his friends", [
        ("おりからの脱出",
         "記憶の中で、ロケットはハイ・エボリューショナリーの計画を知る。自分で作った道具でおりを抜け出し、ライラのおりを開ける。",
         "Out of the cage",
         "In his memories, Rocket learns the High Evolutionary's plan. He breaks out of his cage with a tool he made and opens Lylla's cage."),
        ("ライラの死",
         "そこへハイ・エボリューショナリーが現れ、ライラを撃ち殺す。悲しむロケットを、ハイ・エボリューショナリーはあざ笑う。",
         "Lylla dies",
         "The High Evolutionary appears and shoots Lylla dead, then mocks Rocket's grief."),
        ("ひとりきりの旅立ち",
         "怒ったロケットはハイ・エボリューショナリーに飛びかかり、顔をずたずたに引き裂く。その混乱の中で、ティーフスとフロアは駆けつけた警備の者に撃たれて死ぬ。\n"
         "ロケットは警備の者たちを撃ち倒し、宇宙船をうばって、ひとりで逃げ出した。",
         "Leaving alone",
         "Enraged, Rocket leaps on the High Evolutionary and tears his face apart. In the chaos, guards rushing in shoot Teefs and Floor dead.\n"
         "Rocket shoots down the guards, steals a spaceship and escapes, alone."),
    ]),
    ("第9部 ロケットを救う", "Part 9: Saving Rocket", [
        ("止まる心臓",
         "船の中で、ピーターたちは暗号を使ってキルスイッチを止めようとする。しかしその途中で、ロケットの心臓が止まってしまう。",
         "His heart stops",
         "Aboard the ship, Peter and the others use the code to shut off the kill switch. But partway through, Rocket's heart stops."),
        ("光の中の再会",
         "ロケットは光に包まれた場所で、ライラ、ティーフス、フロアと再会する。ロケットは一緒にいたいと願うが、ライラは、まだロケットの来る時ではないと告げる。",
         "Reunion in the light",
         "In a place full of light, Rocket is reunited with Lylla, Teefs and Floor. He wants to stay with them, but Lylla tells him his time hasn't come yet."),
        ("目を覚ますロケット",
         "ピーターはガモーラと力を合わせてキルスイッチを止め、ロケットの心臓を動かす。ロケットは息を吹き返し、仲間たちは喜び合う。",
         "Rocket wakes",
         "Working with Gamora, Peter shuts off the kill switch and gets Rocket's heart going again. Rocket comes back, and his friends celebrate."),
    ]),
    ("第10部 アレートでの戦い", "Part 10: The battle on Arête", [
        ("おりの中の子どもたち",
         "アレートに乗りこんだネビュラ、ドラックス、マンティスは、おりに入れられたたくさんの子どもたちを見つける。ハイ・エボリューショナリーが遺伝子を作り変えた、次の実験の子どもたちだった。\n"
         "3人はピーターとの通信で、ロケットが助かったことを知って喜ぶ。",
         "Children in cages",
         "On Arête, Nebula, Drax and Mantis find many children locked in cages: the High Evolutionary's next batch of genetically modified subjects.\n"
         "Over the comms, the three hear from Peter that Rocket is alive, and they rejoice."),
        ("アビリスクの部屋",
         "しかし3人はハイ・エボリューショナリーにつかまり、怪物アビリスクのいる部屋に放りこまれる。",
         "The Abilisk chamber",
         "But the High Evolutionary captures the three and throws them into a chamber with monstrous Abilisks."),
        ("ノーウェアがやって来る",
         "ピーターはクラグリンに連絡し、ノーウェアごとアレートのそばに来てもらう。クラグリンはノーウェアからアレートを攻撃する。\n"
         "ハイ・エボリューショナリーの手下の怪物たちがノーウェアに攻めこむが、クラグリンとノーウェアの人々が戦って街を守る。コスモも念力で、アレートがノーウェアにぶつからないように食い止める。",
         "Knowhere arrives",
         "Peter calls Kraglin and has him bring Knowhere itself alongside Arête. Kraglin opens fire on Arête from Knowhere.\n"
         "The High Evolutionary's monstrous Hellspawn counterattack Knowhere, but Kraglin and the people of Knowhere fight them off. Cosmo uses her telekinesis to keep Arête from crashing into Knowhere."),
        ("手下たちの反乱",
         "負けそうになったハイ・エボリューショナリーの部下たちは、逃げようと言って逆らう。ハイ・エボリューショナリーは、その部下たちを殺してしまう。",
         "A mutiny",
         "Facing defeat, the High Evolutionary's crew wants to retreat and turns on him. He kills them."),
        ("アビリスクと脱出",
         "部屋の中では、マンティスが力でアビリスクたちをなだめて味方にする。3人はアビリスクと一緒に部屋を抜け出す。",
         "Escaping with the Abilisks",
         "In the chamber, Mantis calms the Abilisks with her powers and wins them over. The three break out with the Abilisks."),
        ("そろったガーディアンズ",
         "ピーターたちも船に乗りこみ、ガーディアンズは再び全員そろって、アレートの廊下で敵を次々に倒していく。目的は果たしたが、ガーディアンズはすぐには逃げず、子どもたちを助け出すと決める。",
         "The Guardians together",
         "Peter's group boards too, and the Guardians, reunited, fight their way down Arête's corridors. Their mission is done, but instead of leaving they decide to save the children."),
        ("コスモのトンネル",
         "コスモが念力でアレートとノーウェアの間にトンネルを作り、子どもたちはそこを通ってノーウェアへ逃げる。ネビュラはアレートを操縦して、ノーウェアから離れないようにする。",
         "Cosmo's tunnel",
         "Cosmo uses her telekinesis to make a tunnel between Arête and Knowhere, and the children escape through it. Nebula pilots Arête to keep it close to Knowhere."),
    ]),
    ("第11部 ロケットとハイ・エボリューショナリー", "Part 11: Rocket and the High Evolutionary", [
        ("とらわれた動物たち",
         "ロケットは船の中で、おりに入れられた動物たちを見つける。その中には、アライグマの赤ちゃんたちもいた。",
         "Captive animals",
         "Aboard the ship, Rocket finds animals locked in cages, including baby raccoons."),
        ("最後の対決",
         "動物たちを逃がそうとするロケットに、ハイ・エボリューショナリーが襲いかかる。ロケットは、もう番号ではなく、自分の名前はロケット・ラクーンだと言い返して戦う。\n"
         "仲間たちが駆けつけ、みんなでハイ・エボリューショナリーを打ち負かす。マスクのような顔がはがれ、昔ロケットに引き裂かれた傷があらわになる。",
         "The final showdown",
         "As Rocket tries to free the animals, the High Evolutionary attacks him. Rocket fights back, declaring that he isn't a number anymore: his name is Rocket Raccoon.\n"
         "His friends rush in and together they beat the High Evolutionary. His mask-like face comes off, showing the wounds Rocket gave him long ago."),
        ("命は取らない",
         "ロケットはハイ・エボリューショナリーを殺さずに見逃す。ガーディアンズは動物たちもノーウェアへ逃がす。ハイ・エボリューショナリーはドラックスに運び出され、のちにノーウェアにとらえられる（監督の説明による）。",
         "Sparing him",
         "Rocket chooses not to kill the High Evolutionary. The Guardians get the animals to Knowhere too. Drax carries the High Evolutionary off the ship, and he is later imprisoned on Knowhere (per the director)."),
        ("宇宙にとり残されるピーター",
         "くずれていくアレートから最後に逃げるとき、ピーターはノーウェアにたどり着けず、宇宙の寒さの中で凍えかける。\n"
         "そこへ、グルートがアレートの崩壊から助け出していたアダムが現れ、ピーターを救ってノーウェアへ運ぶ。",
         "Peter adrift",
         "Escaping last from the crumbling Arête, Peter can't reach Knowhere and begins to freeze in the cold of space.\n"
         "Adam, whom Groot had rescued from Arête's destruction, appears and carries Peter to safety on Knowhere."),
    ]),
    ("第12部 それぞれの道", "Part 12: Separate paths", [
        ("新しいキャプテン",
         "ノーウェアで、ピーターはガーディアンズをやめると打ち明け、ロケットを新しいキャプテンに指名する。グルートが仲間たちに思いを伝える言葉は、このときはじめて観客にもそのまま分かる言葉で聞こえる。",
         "A new captain",
         "On Knowhere, Peter announces he's leaving the Guardians and names Rocket the new captain. When Groot tells everyone \"I love you guys,\" the audience understands him for the first time."),
        ("別れ",
         "マンティスは、自分が何者かを探す旅にアビリスクたちと出る。ネビュラはノーウェアに残って街をまとめると決め、ドラックスにも一緒に残って、助け出した子どもたちを育ててほしいと頼む。ドラックスは引き受け、マンティスと涙の別れをする。\n"
         "ピーターとガモーラは、前のようにはいかないことを受け入れて別れ、ガモーラはラヴェジャーズに戻る。",
         "Farewells",
         "Mantis sets out with the Abilisks on a journey to find herself. Nebula decides to stay and lead Knowhere, and asks Drax to stay too and raise the rescued children. Drax agrees and shares a tearful goodbye with Mantis.\n"
         "Peter and Gamora accept that things can't be what they were and part ways, and Gamora returns to the Ravagers."),
        ("地球の祖父とノーウェアのダンス",
         "ピーターは地球に帰り、祖父ジェイソンと再会する。\n"
         "ノーウェアでは、フローレンス・アンド・ザ・マシーンの「ドッグ・デイズ・アー・オーヴァー」が流れ、ガーディアンズや子どもたち、街の人々がいっしょに踊る。",
         "Grandpa on Earth, dancing on Knowhere",
         "Peter returns to Earth and is reunited with his grandfather, Jason.\n"
         "On Knowhere, Florence and the Machine's \"Dog Days Are Over\" plays as the Guardians, the children and the townspeople dance together."),
        ("クレジットの途中と後",
         "クレジットの途中では、ロケットがひきいる新しいガーディアンズ（グルート、クラグリン、コスモ、アダム、助け出された子どもフィラ、ブラープ）が新しい仕事に取り組む。\n"
         "クレジットの後では、地球で祖父と朝ごはんの席につくピーターが映り、伝説のスター・ロードは帰ってくるという文字が出る。",
         "During and after the credits",
         "Mid-credits, Rocket's new Guardians (Groot, Kraglin, Cosmo, Adam, the rescued child Phyla and Blurp) take on a new job.\n"
         "After the credits, Peter sits down to breakfast with his grandfather on Earth, and a title promises that the legendary Star-Lord will return."),
    ]),
    ("まとめ", "Summary", [
        ("ロケットの過去",
         "ロケットは、地球のアライグマの赤ちゃんをハイ・エボリューショナリーが作り変えた実験体だった（第2部）。おりの中でライラ、ティーフス、フロアと友だちになり、天才ぶりを見せたことで脳をねらわれた（第5部）。\n"
         "逃げようとしたとき、友だち3匹は殺され、ロケットはひとりで逃げ出した（第8部）。だからロケットは、これまで過去を誰にも話さなかった。",
         "Rocket's past",
         "Rocket was a baby raccoon from Earth, remade by the High Evolutionary (Part 2). In his cage he befriended Lylla, Teefs and Floor, and his genius made the High Evolutionary want his brain (Part 5).\n"
         "When he tried to escape, his three friends were killed and he fled alone (Part 8). That's why he never told anyone about his past."),
        ("ロケットを救う旅",
         "アダムの襲撃で大けがをしたロケットは、体のキルスイッチのせいで治療できなかった（第1部）。ガーディアンズはオルゴコープで記録を盗み（第3部）、カウンター・アースでティールから暗号を手に入れ（第7部）、ロケットの命を救った（第9部）。",
         "The quest to save Rocket",
         "Badly hurt in Adam's attack, Rocket couldn't be treated because of his kill switch (Part 1). The Guardians stole his file from Orgocorp (Part 3), got the code from Theel on Counter-Earth (Part 7) and saved his life (Part 9)."),
        ("ガーディアンズのこれから",
         "ピーターはロケットをキャプテンにして地球の祖父のもとへ帰り、マンティスは旅に出て、ネビュラとドラックスはノーウェアで子どもたちを育てる。ガモーラはラヴェジャーズに戻った。\n"
         "ロケットは、グルート、クラグリン、コスモ、アダム、フィラたちと新しいガーディアンズを作った（第12部）。",
         "What becomes of the Guardians",
         "Peter makes Rocket captain and goes home to his grandfather; Mantis sets off on a journey; Nebula and Drax raise the children on Knowhere; Gamora goes back to the Ravagers.\n"
         "Rocket forms a new team of Guardians with Groot, Kraglin, Cosmo, Adam, Phyla and others (Part 12)."),
        ("死んだ人たち（話の順に）",
         "・ラヴェジャーズの1人（第4部）：ガーディアンズの行き先を聞き出したアダムに殺された。\n"
         "・ライラ（第8部、ロケットの記憶）：逃げようとしたとき、ハイ・エボリューショナリーに撃ち殺された。\n"
         "・ティーフスとフロア（第8部、ロケットの記憶）：混乱の中で、駆けつけた警備の者に撃たれた。\n"
         "・カウンター・アースの人々とアイーシャ（第7部）：失敗作だとして星ごと消そうとしたハイ・エボリューショナリーの攻撃で死んだ。\n"
         "・ティール（第7部）：ピーターとグルートに連れられてアレートから飛び降り、2人の下じきになって死んだ。\n"
         "・ハイ・エボリューショナリーの部下たち（第10部）：逃げようと逆らったため、ハイ・エボリューショナリーに殺された。\n"
         "・ハイ・エボリューショナリーは死なず、ロケットに見逃された（第11部）。",
         "Who died (in order)",
         "- A Ravager (Part 4): killed by Adam after giving up the Guardians' destination.\n"
         "- Lylla (Part 8, Rocket's memory): shot dead by the High Evolutionary during the escape.\n"
         "- Teefs and Floor (Part 8, Rocket's memory): shot by guards in the chaos.\n"
         "- The people of Counter-Earth and Ayesha (Part 7): killed when the High Evolutionary bombarded the planet he considered a failure.\n"
         "- Theel (Part 7): taken off Arête by Peter and Groot, he broke their fall and died.\n"
         "- The High Evolutionary's crew (Part 10): killed by him when they mutinied and tried to retreat.\n"
         "- The High Evolutionary survives; Rocket spares him (Part 11)."),
    ]),
]
