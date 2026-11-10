# 『ヴェノム』（2018年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版ウィキペディアの作品の記事（今の版と2019年の版）と、ヴェノム・アン・ドレイクの人物の記事、
# 日本語版ウィキペディアの登場人物の説明、ciatr の解説記事、検索で見つかった解説記事を照らし合わせた。
# 資料が1つしかない所や食い違う所（ヴェノムが名乗った場所、追いかけっこの終わり方のくわしい中身、
# 病院で離れたヴェノムがどうやってアンのもとへ行ったか、発射台でエディがどんなけがをしたか、
# 宇宙船を運んだ宇宙飛行士の名前、実験台にされた人の名前など）は書いていない。
# 日本語版のせりふは、日本語の資料2つ（日本語版ウィキペディアと ciatr）で同じ言い回しが確かめられた
# キャサディのせりふだけをカギかっこで引用し、ほかは内容だけ書いた。英語版のせりふは英語の資料から取った。
# 人物名は相関図（relations.py）と日本語版ウィキペディアの配役表にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 宇宙から来た生き物", "Part 1: Life from space", [
        ("マレーシアの墜落",
         "大企業ライフ財団は、人が住める星を探して宇宙に探査機を送っていた。探査機は、ねばねばした黒い生き物（シンビオート）におおわれたすい星を見つけ、そのうち4体を地球へ持ち帰る。\n"
         "ところが帰り道で1体が逃げ出し、宇宙船はマレーシアの森に墜落する。燃える宇宙船のまわりに救助の人たちがかけつける。",
         "The crash in Malaysia",
         "The Life Foundation, a powerful company, has been sending probes into space to look for worlds people could live on. One finds a comet covered in black, slimy life forms, symbiotes, and brings four of them back.\n"
         "On the way home one gets loose, and the ship crashes in the forests of Malaysia. Rescue workers rush to the burning wreck."),
        ("逃げた1体",
         "逃げ出したシンビオートは、救急隊員の女性の体に入りこむ。この1体が、のちに「ライオット」と呼ばれる、仲間のリーダー格のシンビオートだ。\n"
         "残りの3体はライフ財団が回収し、サンフランシスコの研究所へ運ぶ。",
         "The one that got away",
         "The escaped symbiote slips into the body of a female paramedic. This is Riot, the leader of its kind.\n"
         "The Life Foundation recovers the other three and takes them to its lab in San Francisco."),
        ("研究所の実験",
         "社長のカールトン・ドレイクは、地球はもう長くもたないと考え、人類が宇宙で生きられるようにしたいと思っている。\n"
         "研究所で分かったのは、シンビオートは酸素を吸う生き物の体に入らないと生きていけないこと。けれど、入られた人の体はたいていシンビオートを受けつけず、命を落としてしまう。ドレイクは、それでも人を使った実験を続ける。",
         "Experiments at the lab",
         "CEO Carlton Drake believes Earth won't last much longer and wants humans to be able to survive in space.\n"
         "The lab learns that symbiotes can't live without an oxygen-breathing host, but most hosts reject them and die. Drake keeps experimenting on people anyway."),
        ("記者エディとアン",
         "サンフランシスコの記者エディ・ブロックは、テレビの報道番組で、弱い人の側に立つ取材で人気がある。婚約者のアン・ウェイングは弁護士で、ちょうどライフ財団を裁判から守る仕事をしている。\n"
         "上司は、エディにドレイクへの取材を言いつける。宇宙開発の話を聞くだけの、当たりさわりのない取材のはずだった。",
         "Eddie and Anne",
         "San Francisco reporter Eddie Brock has a TV news show and is popular for standing up for ordinary people. His fiancée, Anne Weying, is a lawyer who is currently defending the Life Foundation in a lawsuit.\n"
         "Eddie's boss sends him to interview Drake. It's supposed to be a friendly piece about the company's space program."),
        ("ドレイクを問いつめる",
         "取材の前の晩、エディはアンのパソコンをこっそり見て、ライフ財団の人体実験で人が死んでいることを書いた秘密の資料を読んでしまう。\n"
         "取材の日、エディは決められた質問をやめ、ドレイクに実験で人が死んでいるのではないかと問いつめる。ドレイクは取材をすぐに打ち切らせる。",
         "Confronting Drake",
         "The night before, Eddie secretly reads a confidential file on Anne's laptop describing deadly human trials at the Life Foundation.\n"
         "At the interview, Eddie drops the planned questions and accuses Drake of killing people in experiments. Drake ends the interview at once."),
        ("すべてを失う",
         "エディは番組をクビになり、秘密の資料をもらしたことになったアンも、事務所をクビになる。\n"
         "アンは、自分の仕事を勝手に使ったエディに怒り、婚約をやめて彼のもとを去る。",
         "Losing everything",
         "Eddie is fired from his show, and Anne, blamed for the leak, loses her job at her firm too.\n"
         "Furious that Eddie used her work behind her back, Anne calls off the engagement and leaves him."),
    ]),
    ("第2部 研究所の秘密", "Part 2: The lab's secret", [
        ("半年後のエディ",
         "半年後。エディは仕事が見つからず、小さなアパートでくすぶっている。\n"
         "近所のお店では、店主のチェンさんがチンピラにお金をおどし取られているが、エディは見て見ぬふりをする。知り合いのホームレスの女性マリアとは、道ばたで言葉を交わす仲だ。",
         "Eddie, six months later",
         "Six months later, Eddie can't find work and is stuck in a small apartment.\n"
         "At the corner store, owner Mrs. Chen is being shaken down by a thug, and Eddie looks the other way. He is friendly with Maria, a homeless woman he chats with on the street."),
        ("科学者ドーラの頼み",
         "研究所では、実験がうまくいき始めていたが、扱いの不注意からシンビオートが1体死んでしまう。\n"
         "ライフ財団の科学者ドーラ・スカースは、ホームレスの人たちを実験台にするドレイクのやり方にがまんできなくなり、エディに会いに来る。実験を世の中に知らせてほしいと頼み、研究所に入る手助けをすると申し出る。",
         "Dora's request",
         "At the lab, the trials are getting closer to success, but one symbiote dies through carelessness.\n"
         "Life Foundation scientist Dora Skirth can no longer stand Drake using homeless people as test subjects. She comes to Eddie, asks him to expose the experiments, and offers to get him inside."),
        ("研究所に忍びこむ",
         "夜、ドーラが警備員の気をそらしているあいだに、エディは研究所の実験室に入り、閉じこめられた人たちを写真に撮る。\n"
         "部屋の1つに、行方が分からなくなっていたマリアがいた。助けを求められたエディは、ガラスを割って彼女を出そうとする。",
         "Breaking in",
         "At night, while Dora distracts a guard, Eddie slips into the lab and photographs the people locked up there.\n"
         "In one cell he finds Maria, who had gone missing. She begs for help, and he breaks the glass to free her."),
        ("マリアの死",
         "ところが、マリアの体にはシンビオートが入っていた。正気を失ったマリアはエディにおそいかかり、その瞬間、シンビオートがエディの体に乗りうつる。シンビオートが抜けたマリアは、その場で息を引き取る。\n"
         "警報が鳴り、エディは警備員たちを振り切って研究所から逃げ出す。自分の体に何かが入ったことには、まだ気づいていない。",
         "Maria dies",
         "But Maria is hosting a symbiote. Out of her mind, she attacks Eddie, and in that instant the symbiote jumps into him. Without it, Maria dies on the spot.\n"
         "Alarms go off and Eddie gets away from the guards. He doesn't yet realize something is inside him."),
        ("おかしな体",
         "家に帰ったエディは、ひどい空腹におそわれる。冷蔵庫の中のものを食べつくし、ゴミ箱の残り物まで口に入れる。頭の中では、知らない声が聞こえはじめる。\n"
         "アンが新しい恋人の医師ダン・ルイスと食事をしているレストランに、エディはふらふらと現れる。店の生けすに飛びこんで、生きたロブスターにかぶりつく。",
         "Something's wrong",
         "At home, Eddie is ravenously hungry. He empties the fridge and even eats scraps from the trash. He starts hearing a strange voice in his head.\n"
         "He stumbles into a restaurant where Anne is dining with her new boyfriend, Dr. Dan Lewis. He climbs into the lobster tank and bites into a live lobster."),
        ("ドーラの最期",
         "研究所では、警備の責任者ローランド・トリースが、エディを中に入れたのがドーラだと突き止め、ドレイクに知らせる。\n"
         "ドレイクは、裏切ったドーラを、最後に残っていたシンビオートといっしょの部屋に閉じこめる。ドーラは命を落とし、そのシンビオートも死ぬ。これで、生き残っているのはエディの中の1体だけになる。",
         "Dora's end",
         "At the lab, security chief Roland Treece discovers that Dora let Eddie in and tells Drake.\n"
         "Drake locks the traitor in with the last captive symbiote. Dora dies, and so does that symbiote, leaving the one inside Eddie as the only known survivor."),
        ("部屋への襲撃",
         "マリアのシンビオートがエディに移ったと見たドレイクは、トリースと部下たちをエディのアパートへ送りこむ。\n"
         "銃を向けられたとき、エディの体から黒い触手が勝手に飛び出し、男たちを次々と倒していく。",
         "The raid",
         "Guessing that Maria's symbiote is now in Eddie, Drake sends Treece and his men to Eddie's apartment.\n"
         "When they point their guns at him, black tendrils burst out of Eddie's body on their own and take the men down one by one."),
    ]),
    ("第3部 ヴェノム", "Part 3: Venom", [
        ("バイクの追いかけっこ",
         "エディはバイクで逃げ出す。トリースの部下たちが車で追いかけ、空からは小型の無人機（ドローン）が追ってくる。\n"
         "サンフランシスコの急な坂道を、エディはシンビオートの力を借りながら走りぬける。体から伸びた触手が、追っ手を振りはらう。",
         "The chase",
         "Eddie flees on a motorcycle, chased by Treece's men in cars and by drones overhead.\n"
         "He tears through San Francisco's steep streets with the symbiote's help, its tendrils fending off his pursuers."),
        ("黒い怪物の姿",
         "追いつめられたとき、シンビオートがエディの全身をおおい、大きな白い目と鋭い歯を持つ黒い怪物の姿になる。怪物は追っ手を倒し、1人の頭をかみちぎってしまう。\n"
         "エディが我に返ると、自分がしたことにぞっとする。",
         "The monster",
         "Cornered, Eddie is covered completely by the symbiote and becomes a huge black monster with big white eyes and razor teeth. It takes down the pursuers and bites one man's head off.\n"
         "When Eddie comes back to himself, he is horrified."),
        ("ヴェノムと名乗る",
         "落ち着いたところで、シンビオートはエディに話しかけ、自分を「ヴェノム」と名乗る。\n"
         "ヴェノムによると、あのすい星は、シンビオートが住民の体に入って食べつくせる星を探しているという。ヴェノムは、自分たちに協力すればエディだけは助けてやると言う。エディは怖がりながらも、体に満ちる力を少しずつ楽しむようになる。",
         "It calls itself Venom",
         "Once things calm down, the symbiote speaks to Eddie and introduces itself as Venom.\n"
         "Venom explains that the comet is looking for worlds where symbiotes can take over and devour the inhabitants, and offers to spare Eddie if he helps. Scared as he is, Eddie starts to enjoy his new strength."),
        ("元の職場へ",
         "エディは、研究所で撮った写真を元の上司に届けて、ドレイクの悪事を世の中に知らせようとする。ヴェノムの力で高いビルの壁をよじ登り、上司の部屋に写真の入った携帯電話を置いてくる。\n"
         "ビルのてっぺんで、ヴェノムはサンフランシスコの街をながめて感心する。",
         "Back to the old office",
         "Eddie wants to get his lab photos to his old boss and expose Drake. Using Venom's powers, he scales a tall building and leaves a phone with the photos in his boss's office.\n"
         "From the top of the building, Venom marvels at the San Francisco skyline."),
        ("特殊部隊との戦い",
         "ビルの下には、知らせを受けた警察の特殊部隊が待ちかまえていた。エディは再びヴェノムの姿になり、部隊の人たちをなぎ倒して逃げる。\n"
         "その姿を、エディを迎えに来ていたアンが見てしまう。",
         "Fighting the SWAT team",
         "Waiting below is a police SWAT team, called in about the break-in. Eddie turns into Venom again and fights his way out.\n"
         "Anne, who has come to pick him up, sees it all."),
        ("車の中のあやまり",
         "アンはエディを車に乗せ、ダンのいる病院へ向かう。車の中で、エディはヴェノムにうながされて、婚約していたころにアンにしたことをあやまる。",
         "An apology in the car",
         "Anne drives Eddie to Dan's hospital. On the way, prompted by Venom, Eddie apologizes for what he did to her."),
    ]),
    ("第4部 ライオット", "Part 4: Riot", [
        ("体がむしばまれている",
         "病院で調べると、シンビオートがエディの内臓を少しずつ傷めていることが分かる。エディは、シンビオートには高い音と火という2つの弱点があると話す。\n"
         "ヴェノムは、内臓の傷は治せると言うが、アンはMRIの機械を動かす。大きな音に耐えられず、ヴェノムはエディの体から引きはがされる。",
         "Eating him alive",
         "Tests at the hospital show the symbiote is slowly damaging Eddie's organs. Eddie mentions its two weaknesses: high-pitched sound and fire.\n"
         "Venom insists the damage can be fixed, but Anne switches on an MRI machine. Unable to stand the noise, Venom is torn out of Eddie's body."),
        ("つかまるエディ",
         "ヴェノムと離れたエディは、病院を出たところで、ドレイクの部下たちにつかまってしまう。",
         "Eddie is captured",
         "Separated from Venom, Eddie is grabbed by Drake's men after leaving the hospital."),
        ("ライオットの旅",
         "一方、マレーシアで逃げたライオットは、救急隊員の女性から老いた女性へと体を乗りかえ、さらに幼い女の子の体に入って、アメリカへ渡る。\n"
         "女の子の姿のまま、ライオットはサンフランシスコのライフ財団に入りこみ、ドレイクの前に現れる。",
         "Riot's journey",
         "Meanwhile, Riot, which escaped in Malaysia, moves from the paramedic to an old woman, then into a little girl, and travels to America.\n"
         "Still in the girl's body, Riot gets into the Life Foundation in San Francisco and appears before Drake."),
        ("ドレイクとライオット",
         "ライオットはドレイクの体に入る。ドレイクは、ライオットとひとつになることを受け入れ、ライフ財団の宇宙船でライオットをすい星へ連れていき、残りのシンビオートたちを地球へ連れてくると約束する。\n"
         "ドレイクは、宇宙船の打ち上げの準備を進める。",
         "Drake and Riot",
         "Riot bonds with Drake. Drake welcomes it, promising to fly Riot to the comet aboard a Life Foundation ship and bring the rest of the symbiotes back to Earth.\n"
         "He gets the launch ready."),
        ("森の中で",
         "つかまったエディは、トリースたちに森へ連れていかれる。\n"
         "森の中で、トリースはエディを殺そうとする。",
         "In the woods",
         "Treece and his men take the captured Eddie into the woods.\n"
         "There, Treece gets ready to kill him."),
        ("アンとヴェノム",
         "その時、ヴェノムが入ったアンが現れる。アンは、エディを助けるため、ヴェノムを自分の体に入れることをしぶしぶ受け入れていた。\n"
         "ヴェノムをまとったアンは男たちを倒し、トリースの頭をかみちぎって殺す。トリースはエディを殺そうとしたため、ここで命を落とす。アンは自分がしたことにおびえる。",
         "Anne and Venom",
         "Then Anne appears, bonded with Venom. To save Eddie, she reluctantly agreed to let it into her body.\n"
         "Covered in the symbiote, Anne takes down the men and bites Treece's head off, killing the man who was about to kill Eddie. Anne is shaken by what she has done."),
        ("口づけでもとどおり",
         "アンはエディに口づけをし、ヴェノムはその口からエディの体へ戻る。エディとヴェノムは再びひとつになる。",
         "Back together with a kiss",
         "Anne kisses Eddie, and Venom passes from her mouth back into him. Eddie and Venom are one again."),
        ("ヴェノムの心変わり",
         "ヴェノムは、自分も故郷の星ではエディと同じ落ちこぼれだったと打ち明ける。そして、地球とエディが気に入ったので、ここに残りたいと言う。\n"
         "2人は、ドレイクとライオットが仲間のシンビオートを連れてくるのを止めるため、ライフ財団の発射場へ向かう。",
         "Venom changes sides",
         "Venom admits that on its home world it's a loser, just like Eddie. It has come to like Earth, and Eddie, and wants to stay.\n"
         "The two head for the Life Foundation launch site to stop Drake and Riot from bringing the other symbiotes to Earth."),
    ]),
    ("第5部 発射台の戦い", "Part 5: The launch pad", [
        ("発射場への突入",
         "発射場では、宇宙船が打ち上げを待っている。エディとヴェノムは、宇宙船に乗りこもうとするドレイクを止めに向かう。\n"
         "ドレイクの体からライオットが姿を現す。ヴェノムよりも大きな怪物だ。",
         "Storming the launch site",
         "At the launch site, the spacecraft is waiting to lift off. Eddie and Venom go after Drake before he can board.\n"
         "Riot emerges from Drake's body, a monster even bigger than Venom."),
        ("ライオットとの戦い",
         "発射台の上で、ヴェノムとライオットが激しくぶつかり合う。ライオットはヴェノムより強く、ヴェノムとエディをまるごと自分の体に取りこんでしまう。\n"
         "アンが発射場のスピーカーから高い音を流し、2体のシンビオートは苦しんで引きはがされる。",
         "Battle with Riot",
         "On the launch pad, Venom and Riot clash. Riot is stronger, and at one point swallows Venom and Eddie into its own body.\n"
         "Anne blasts a high-pitched sound through the launch site's speakers, and the two symbiotes are pulled apart in pain."),
        ("宇宙船の爆発",
         "ドレイクとライオットを乗せて、宇宙船が飛び立つ。ヴェノムは飛び立つ宇宙船に飛びつき、宇宙船を壊す。\n"
         "宇宙船は空中で爆発し、ドレイクとライオットはその炎の中で死ぬ。ヴェノムは爆風からエディを包んで守り、自分は燃えつきたように見える。",
         "The explosion",
         "The ship lifts off with Drake and Riot aboard. Venom leaps onto it as it rises and wrecks it.\n"
         "The ship explodes in midair, and Drake and Riot die in the blast. Venom wraps Eddie up to shield him from the blast and seems to burn away."),
        ("生きていたヴェノム",
         "後日、エディはアンと会う。アンは、ヴェノムが死んでしまったことを残念がり、エディもうなずく。\n"
         "しかし、ヴェノムはエディの体の中で生きていた。エディとヴェノムは、だれでも食べていいわけではなく、食べるのは悪い人だけにすると約束する。",
         "Venom lives",
         "Later, Eddie meets Anne. She is sorry Venom is gone, and Eddie agrees.\n"
         "But Venom is alive inside him. Eddie and Venom agree that it can't eat just anyone, only bad guys."),
        ("チェンさんの店で",
         "エディは記者の仕事に戻る。チェンさんの店で、またあのチンピラがお金をおどし取ろうとしている。\n"
         "今度のエディは見逃さない。ヴェノムの姿になってチンピラをおどしつけ、そのまま食べてしまう。エディとヴェノムは、街の悪い人をこらしめながら生きていくことにする。",
         "At Mrs. Chen's store",
         "Eddie goes back to reporting. At Mrs. Chen's store, the same thug is shaking her down again.\n"
         "This time Eddie doesn't look away. He becomes Venom, terrifies the thug, and eats him. Eddie and Venom will protect the city by devouring its criminals."),
        ("エンドクレジットの途中",
         "記者に戻ったエディは、サン・クエンティン刑務所に呼ばれる。連続殺人犯クレタス・キャサディが、エディにだけ取材を受けたいと言ってきたのだ。\n"
         "キャサディは、エディに「俺がここを出たら、大殺戮（カーネイジ）になる」と言い残す。",
         "Mid-credits",
         "Back on the job, Eddie is called to San Quentin prison. Serial killer Cletus Kasady will talk only to him.\n"
         "Kasady promises: \"When I get out of here, and I will, there's gonna be carnage.\""),
        ("エンドクレジットの後",
         "最後に、アニメ映画『スパイダーマン：スパイダーバース』の一部が流れる。",
         "After the credits",
         "Finally, a scene from the animated film Spider-Man: Into the Spider-Verse plays."),
    ]),
    ("まとめ", "Summary", [
        ("エディがしたこと",
         "ドレイクの人体実験をあばこうとして仕事と婚約者を失った（第1部）。研究所に忍びこんでヴェノムと一体になり（第2部）、最初はとまどったが、最後はヴェノムと力を合わせてドレイクとライオットを止めた（第5部）。",
         "What Eddie did",
         "He lost his job and his fiancée trying to expose Drake's human trials (Part 1). He bonded with Venom while breaking into the lab (Part 2), and despite his fear, ended up teaming with Venom to stop Drake and Riot (Part 5)."),
        ("ヴェノムがしたこと",
         "はじめは、仲間のシンビオートが地球に来るのを手伝うつもりで、協力すればエディだけは助けると言っていた（第3部）。エディやアンと過ごすうちに地球が好きになり、仲間を呼ぶのを止める側にまわった（第4部）。最後はエディを爆風から守り、エディと「悪い人だけを食べる」と約束した（第5部）。",
         "What Venom did",
         "At first it meant to help its kind come to Earth, offering to spare Eddie if he helped (Part 3). Living with Eddie and Anne, it grew to like Earth and turned against the invasion (Part 4). It shielded Eddie from the blast and agreed to eat only bad guys (Part 5)."),
        ("アンがしたこと",
         "MRIでヴェノムをエディから離し（第4部）、エディを助けるため自分の体にヴェノムを入れ、トリースを倒して口づけでヴェノムをエディに返した（第4部）。発射台では高い音を流してライオットとの戦いを助けた（第5部）。",
         "What Anne did",
         "She used an MRI to separate Venom from Eddie (Part 4), then let Venom into her own body to save Eddie, killed Treece and passed Venom back with a kiss (Part 4). At the launch pad she blasted a high-pitched sound to help against Riot (Part 5)."),
        ("死んだ人たち（話の順に）",
         "・マリア（第2部）：ライフ財団の実験でシンビオートを入れられていた。エディが助け出そうとしたとき、シンビオートがエディに乗りうつり、抜けがらになって死んだ。\n"
         "・ドーラ・スカース（第2部）：エディを研究所に入れたことがばれ、ドレイクに、残っていたシンビオートといっしょの部屋に閉じこめられて死んだ。\n"
         "・トリースの部下（第3部）：エディを追いかけた1人が、ヴェノムに頭をかみちぎられた。\n"
         "・ローランド・トリース（第4部）：森でエディを殺そうとしたところを、ヴェノムをまとったアンに頭をかみちぎられた。\n"
         "・カールトン・ドレイクとライオット（第5部）：仲間のシンビオートを連れてくるために宇宙船で飛び立ったが、ヴェノムが宇宙船を壊し、爆発の炎の中で死んだ。\n"
         "・チンピラ（第5部）：チェンさんの店をおどしていたところを、ヴェノムに食べられた。",
         "Who died (in story order)",
         "- Maria (Part 2): A Life Foundation test subject hosting a symbiote. When Eddie tried to free her, it jumped to him and she died.\n"
         "- Dora Skirth (Part 2): Caught letting Eddie into the lab, she was locked in with the last captive symbiote by Drake and died.\n"
         "- One of Treece's men (Part 3): Chasing Eddie, he had his head bitten off by Venom.\n"
         "- Roland Treece (Part 4): About to kill Eddie in the woods, he had his head bitten off by Anne while she was bonded to Venom.\n"
         "- Carlton Drake and Riot (Part 5): They launched to bring more symbiotes to Earth, but Venom wrecked the ship and they died in the explosion.\n"
         "- The thug (Part 5): Eaten by Venom while shaking down Mrs. Chen's store."),
    ]),
]
