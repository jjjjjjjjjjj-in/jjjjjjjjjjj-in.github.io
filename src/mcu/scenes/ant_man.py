# 『アントマン』（2015年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじと登場人物の記事、検索で見つかった解説記事で事実を確かめた。
# 資料どうしで食い違う所や、確かめられない細かい所（金庫の開け方、クロスがハンクを撃った場所、
# 量子の世界でスコットが見たもの、パトカーから逃げたあとの移動の方法など）は書いていない。
# 日本語版のせりふは、日本語の吹替・字幕の言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 人物名は相関図（relations.py）にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 1989年の決別", "Part 1: Walking away in 1989", [
        ("建設中のトリスケリオン",
         "1989年、ワシントン。シールドの本部トリスケリオンは、まだ建てている途中だった。\n"
         "科学者ハンク・ピムが会議室に入ってくる。そこにはシールドを率いるハワード・スタークとペギー・カーター、幹部のミッチェル・カーソンがいた。ハンクは、自分が発明した、物を小さくする粒子（ピム粒子）を、シールドがひそかにまねしようとしていたことを知り、怒っていた。",
         "The Triskelion under construction",
         "Washington, 1989. S.H.I.E.L.D.'s headquarters, the Triskelion, is still being built.\n"
         "Scientist Hank Pym storms into a meeting room where S.H.I.E.L.D.'s leaders Howard Stark and Peggy Carter sit with senior official Mitchell Carson. Hank has found out that S.H.I.E.L.D. secretly tried to copy the shrinking particles he invented, the Pym Particles, and he is furious."),
        ("カーソンを机にたたきつける",
         "カーソンが、ハンクの妻ジャネットのことを持ち出してハンクをからかう。ハンクはカーソンの頭をつかんで机にたたきつけ、カーソンは鼻から血を流す。\n"
         "ハンクはシールドを辞めると言い、自分が生きているかぎり、この技術は誰にも渡さないと宣言して出ていく。",
         "Slamming Carson into the desk",
         "Carson needles Hank about his wife, Janet. Hank grabs Carson's head and slams it into the desk, leaving him with a bloody nose.\n"
         "Hank quits S.H.I.E.L.D. and vows that as long as he lives, no one will get his technology. Then he walks out."),
    ]),
    ("第2部 出所したスコット", "Part 2: Scott gets out", [
        ("刑務所でのお別れ",
         "現代。サンフランシスコの近くにあるサン・クエンティン刑務所。スコット・ラングは、刑期を終えて出所する日をむかえる。\n"
         "スコットは昔、技術者として勤めていた会社がお客をだましていたことに気づき、会社に忍びこんでお金をお客に返したため、泥棒として捕まったのだった。\n"
         "出ていく前に、仲間の囚人たちがお別れのあいさつとしてスコットをなぐり、送り出す。",
         "A prison send-off",
         "The present day. San Quentin State Prison, near San Francisco. Scott Lang finishes his sentence.\n"
         "Scott used to be an engineer. When he found out his company was cheating its customers, he broke in and gave the money back to them, and went to prison as a burglar.\n"
         "Before he leaves, his fellow inmates send him off with a farewell punch."),
        ("ルイスの迎え",
         "門の外で待っていたのは、刑務所で同じ部屋だった友だちルイスのバンだった。スコットはしばらくルイスの部屋に住むことにし、ルイスの仲間のデイヴとカートとも顔を合わせる。\n"
         "ルイスはさっそく、すごい盗みの話があると持ちかけるが、スコットは、もう泥棒はしない、まっとうに生きると断る。",
         "Luis picks him up",
         "Waiting outside the gate in his van is Luis, Scott's old cellmate. Scott moves in with him for now and meets Luis's friends Dave and Kurt.\n"
         "Luis right away pitches a big score, but Scott turns him down. He's done stealing and wants to go straight."),
        ("アイスクリーム店をクビに",
         "スコットはアイスクリームのチェーン店で働き始める。しかし店長のデイルに刑務所にいたことを知られ、すぐにクビにされてしまう。前科があると、どこでも雇ってもらえない。",
         "Fired from the ice cream shop",
         "Scott gets a job at an ice cream chain, but the manager, Dale, finds out he's been in prison and fires him on the spot. With a record, no one will keep him."),
        ("キャシーの誕生日",
         "スコットは、知らせずに、元妻マギーの家へ娘キャシーの誕生日を祝いに行く。おみやげは、わざとぶさいくに作られたウサギのぬいぐるみで、キャシーは大喜びする。\n"
         "しかし、マギーと、その婚約者で警察官のジム・パクストンは、養育費も払っていないのに来るなとスコットを責める。住む部屋と仕事を見つけ、養育費を払えるようになるまで、キャシーには会わせないと言われる。",
         "Cassie's birthday",
         "Without calling ahead, Scott shows up at his ex-wife Maggie's house for his daughter Cassie's birthday. His present is a deliberately hideous stuffed rabbit, and Cassie loves it.\n"
         "But Maggie and her fiancé, police officer Jim Paxton, scold him for not paying child support. Until he has a place, a job and the money to pay, he can't see Cassie."),
        ("クロスの発表",
         "そのころ、ハンクが作った会社ピム・テック。ハンクの元弟子で、いまは会社を動かしているダレン・クロスは、ハンクを会社に呼ぶ。役員のひとりとしてクロスのそばにいるのは、ハンクとは長く気まずい仲の娘ホープだった。ハンクは昔、このクロスとホープに会社を追い出されていた。\n"
         "クロスは役員たちの前で、着た人を小さくできる戦うためのスーツ「イエロージャケット」の計画を発表する。体を小さくする粒子を自分の手で作りかけているが、生き物を小さくする実験はまだうまくいっていなかった。ハンクは、その計画にぞっとする。",
         "Cross's presentation",
         "Meanwhile, at Pym Technologies, the company Hank founded. His former protégé Darren Cross, who now runs it, invites Hank in. At Cross's side as a board member is Hank's daughter Hope, long estranged from him. Years ago, Cross and Hope forced Hank out of his own company.\n"
         "In front of the board, Cross unveils his plan for the Yellowjacket, a combat suit that can shrink its wearer. He is close to recreating the shrinking particles himself, but his tests on living things still fail. Hank is horrified."),
        ("トイレの殺人",
         "会議のあと、クロスの研究に疑問をぶつけてきた男性フランクを、クロスはトイレで親しげに迎える。それでもフランクが研究を疑うので、クロスはまだ不完全な粒子をこめた銃でフランクを撃つ。\n"
         "フランクの体は小さく縮んで、ぐちゃぐちゃのかたまりになって死ぬ。クロスはそれを紙でふき取り、トイレに流してしまう。",
         "Murder in the restroom",
         "After the meeting, a man named Frank, who has been questioning Cross's work, runs into Cross in the restroom. Cross acts friendly, but when Frank keeps doubting the research, Cross shoots him with a gun loaded with his unstable particles.\n"
         "Frank's body shrinks into a tiny, shapeless lump and he dies. Cross wipes it up with a paper towel and flushes it away."),
    ]),
    ("第3部 金庫の中のスーツ", "Part 3: The suit in the safe", [
        ("ルイスの長い話",
         "お金がなくて娘に会えないスコットは、とうとうルイスの話にのることにする。\n"
         "ルイスは、知り合いから知り合いへと伝わってきたうわさ話を、長々と話して聞かせる。ある金持ちの老人が旅行で家を空け、その家の地下に大きな金庫があるという。",
         "Luis's long story",
         "Broke and barred from seeing his daughter, Scott finally agrees to Luis's job.\n"
         "Luis tells, at great length, how the tip passed from friend to friend to reach him: a rich old man is away on a trip, and there's a big safe in his basement."),
        ("屋敷に忍びこむ",
         "夜、デイヴが車を運転し、カートが見張りを手伝って、スコットは屋敷に忍びこむ。指紋で開く扉と、とても古い頑丈な金庫を、スコットは技術を使って開ける。\n"
         "しかし金庫の中にあったのはお金ではなく、古い革のスーツとヘルメットだけだった。スコットはがっかりしながらも、それを持ち帰る。",
         "Breaking into the house",
         "That night, with Dave driving and Kurt helping keep watch, Scott slips into the house. He gets past a fingerprint-locked door and cracks a very old, very sturdy safe.\n"
         "But there's no money inside, just an old leather suit and a helmet. Disappointed, Scott takes them home anyway."),
        ("お風呂の中で小さくなる",
         "ルイスの部屋でスーツを着てみたスコットが、手元のボタンを押すと、体がアリほどの大きさに縮む。ふつうのお風呂が大海のようになり、スコットは流れる水に追われ、床のすき間を落ち、ネズミにも追いかけられる。\n"
         "ヘルメットの中から、知らない男の声がスコットに話しかけ、逃げ方を教える。スコットはなんとか元の大きさに戻る。",
         "Shrinking in the bathtub",
         "At Luis's place, Scott tries on the suit and presses a button on the glove. He shrinks to the size of an ant. The bathtub becomes an ocean; he's chased by rushing water, falls through cracks in the floor and is pursued by a rat.\n"
         "A stranger's voice speaks to him through the helmet and talks him through it. Scott manages to return to normal size."),
        ("スーツを返しに行って捕まる",
         "こわくなったスコットは、スーツを屋敷に返しに行く。しかし屋敷を出たところで、待っていた警察に捕まる。パクストンもその場にいて、スコットは留置場に入れられる。",
         "Caught returning the suit",
         "Frightened, Scott takes the suit back to the house. On his way out, the police are waiting, Paxton among them, and Scott ends up in a holding cell."),
        ("弁護士のふりをした老人",
         "スコットに面会に来たのは、弁護士のふりをした老人、あの屋敷の主ハンクだった。ハンクはスコットに、人生を変える機会をあげようと持ちかける。\n"
         "ハンクは、こっそりスーツを留置場に届けさせる。スコットはスーツで小さくなって牢屋を抜け出し、空飛ぶアリに乗って逃げる。",
         "An old man posing as a lawyer",
         "A visitor posing as Scott's lawyer turns out to be the owner of the house: Hank. He offers Scott a chance to change his life.\n"
         "Hank has the suit smuggled into the cell. Scott shrinks, slips out of jail, and escapes on the back of a flying ant."),
        ("すべてはハンクの試験だった",
         "気がつくと、スコットはハンクの屋敷にいた。ハンクは、ルイスに伝わったうわさも、屋敷を空けたことも、すべて自分が仕組んだことだと話す。スコットの腕前を見るための試験だった。\n"
         "ハンクのそばにはホープがいた。ホープはスコットを見て、なぜ自分ではなくこの男なのかと不満を隠さない。",
         "It was all Hank's test",
         "Scott wakes up in Hank's house. Hank explains that he set it all up, from the tip that reached Luis to leaving the house empty. It was a test of Scott's skills.\n"
         "Hope is there too, and she makes no secret of her resentment: why him, and not her?"),
    ]),
    ("第4部 アントマンの訓練", "Part 4: Ant-Man training", [
        ("ハンクの頼み",
         "ハンクは、自分が昔、シールドでアントマンとして活躍していたことを明かす。そして、クロスがイエロージャケットを完成させれば、悪い者たちの手に渡って世界が危なくなると話す。\n"
         "ホープは、クロスの計画を知ってから、ひそかに父と手を組み、クロスを見張っていたのだった。ハンクはスコットに、新しいアントマンになってイエロージャケットを盗み出し、研究のデータを消してほしいと頼む。\n"
         "迷うスコットに、ハンクは、娘に顔向けできない泥棒のまま一生を終えるより、このほうがいいと説得する。",
         "Hank's request",
         "Hank reveals that he once worked for S.H.I.E.L.D. as Ant-Man. If Cross perfects the Yellowjacket, he says, it will end up with dangerous people and the world will be at risk.\n"
         "Since learning of Cross's plans, Hope has secretly been working with her father, spying on Cross. Hank asks Scott to become the new Ant-Man, steal the Yellowjacket and destroy the research.\n"
         "When Scott hesitates, Hank tells him it beats spending his life as a petty thief his daughter can't look up to."),
        ("カギ穴を通る練習",
         "スコットは、小さくなったり元に戻ったりする練習を始める。小さくなっても力は大人のままで、小さい体で強くなぐれる。\n"
         "カギ穴を小さくなって通り抜ける練習では、なかなかうまくいかず、何度も失敗する。",
         "Through the keyhole",
         "Scott practices shrinking and growing. Even tiny, he keeps a grown man's strength, so his punches pack a huge wallop.\n"
         "Practicing shrinking through a keyhole, he fails again and again."),
        ("アリたちと仲よくなる",
         "ハンクは、ヘルメットでアリの気持ちに話しかけて動かす方法を教える。電気を通すアリ、毒の強いアリ、橋になって体をつなげるアリ、空を飛ぶ大きな羽アリなど、何種類ものアリが仲間になる。\n"
         "スコットは、自分を乗せて飛ぶ羽アリの1匹に「アントニー」と名前をつける。",
         "Making friends with ants",
         "Hank teaches him to steer ants by talking to them through the helmet. Several kinds join the team: ants that conduct electricity, ants with a powerful sting, ants that link their bodies to make bridges, and big winged ants that fly.\n"
         "Scott names the flying ant he rides Antony."),
        ("ホープとの特訓",
         "ホープはスコットにけんかの技を教える。厳しいホープに、スコットは何度も投げ飛ばされ、なぐられる。\n"
         "ホープは、自分のほうがスーツをうまく使えるのに、なぜ父は自分に着せないのかと怒っていた。",
         "Sparring with Hope",
         "Hope teaches Scott to fight, and she's tough. He gets thrown and punched again and again.\n"
         "Hope is angry. She could use the suit better than Scott, so why won't her father let her wear it?"),
        ("母ジャネットの秘密",
         "ハンクは、ホープにずっと隠してきたことを打ち明ける。ホープの母ジャネットは、飛行機の事故で死んだのではなかった。ジャネットは「ワスプ」と呼ばれるヒーローで、ハンクと一緒に任務についていた。\n"
         "1987年、2人は、アメリカに向けて撃たれたソ連の核ミサイルを止めに行った。ミサイルの中に入るには、小さくなる力を止める仕組みを外して、どこまでも小さくなるしかなかった。ジャネットはそれを選んでミサイルを止めたが、そのまま縮み続けて、とても小さな「量子の世界」に消えてしまった。\n"
         "ハンクは、同じことが起きるのがこわくて、ホープにスーツを着せたくなかったのだった。ホープは父の気持ちを知り、2人はわかり合う。",
         "The secret about Janet",
         "Hank finally tells Hope what he's hidden from her. Her mother, Janet, didn't die in a plane crash. She was a hero called the Wasp and went on missions with Hank.\n"
         "In 1987, they went to stop a Soviet nuclear missile launched at the United States. The only way inside was to switch off the regulator that limits shrinking and keep getting smaller. Janet did it and stopped the missile, but she kept shrinking and vanished into the Quantum Realm.\n"
         "Hank was afraid of losing Hope the same way. Hope understands her father at last, and they reconcile."),
        ("量子の世界の警告",
         "ハンクはスコットにも、スーツの小さくなる力を止める仕組みを外せば、二度と戻れずに量子の世界に迷いこむかもしれないと注意する。",
         "A warning about the Quantum Realm",
         "Hank warns Scott too: if he ever overrides the regulator, he could be lost in the Quantum Realm and never come back."),
    ]),
    ("第5部 アベンジャーズの基地", "Part 5: The Avengers' base", [
        ("古い倉庫へ",
         "作戦には、ハンクが昔作った、相手の見張りの装置をごまかす小さな機械が必要だった。ハンクは、その機械がスターク社の古い倉庫にあると考え、スコットを取りに行かせる。\n"
         "ところが、スコットが着いてみると、そこは新しくなったアベンジャーズの基地だった。",
         "To the old warehouse",
         "The plan needs a signal decoy, a small device Hank built long ago. He believes it's in an old Stark warehouse and sends Scott to get it.\n"
         "But when Scott arrives, the place has become the new Avengers facility."),
        ("ファルコンとの対決",
         "屋根に降りたスコットを、見張っていたサム・ウィルソン（ファルコン）が見つける。スコットは、大きくなったり小さくなったりしながらサムと戦う。\n"
         "最後にスコットはサムの翼の中にもぐりこんで仕掛けを壊し、サムを飛べなくする。そのすきに機械を手に入れて逃げる。サムは、このことを誰にも知られたくないと思う。",
         "Facing the Falcon",
         "Sam Wilson, the Falcon, spots Scott landing on the roof. Scott fights him, shrinking and growing.\n"
         "Finally Scott crawls inside Sam's wing pack and wrecks its parts, grounding him, then grabs the device and gets away. Sam hopes word of this doesn't get around."),
        ("クロスの成功",
         "一方、クロスはついに、小さくする粒子を完成させる。生きた子羊を、無事に小さくして元に戻すことに成功する。\n"
         "クロスは、イエロージャケットを発表する会を会社で開くと決め、ハンクとホープも招く。お客の中には、カーソンたち、ひそかに悪の組織ヒドラとつながる者たちがいた。",
         "Cross succeeds",
         "Meanwhile, Cross finally perfects his particles: he shrinks a live lamb and brings it back unharmed.\n"
         "He schedules an unveiling of the Yellowjacket at the company and invites Hank and Hope. Among the guests are Carson and his men, who are secretly tied to Hydra."),
        ("泥棒の作戦会議",
         "ハンクの考えた作戦に、ルイス、デイヴ、カートも加わる。カートが会社の警備の仕組みに手を加え、デイヴは車で待ち、ルイスは警備員にばけて中に入る。\n"
         "スコットは小さくなって忍びこみ、会社のデータを消してイエロージャケットを盗み、建物に爆弾を仕掛けて研究ごと壊す計画だった。",
         "Planning the heist",
         "Luis, Dave and Kurt join Hank's plan. Kurt will tamper with the company's security system, Dave will wait in the van, and Luis will go in disguised as a security guard.\n"
         "Scott will sneak in at tiny size, wipe the company's data, steal the Yellowjacket and plant explosives to bring down the building, research and all."),
    ]),
    ("第6部 ピム・テックへの潜入", "Part 6: Inside Pym Tech", [
        ("発表の夜",
         "発表会の夜。ハンクとホープは招かれた客として会場にいる。スコットは小さくなり、空飛ぶアリたちと一緒に建物の中に入りこむ。\n"
         "ルイスは警備員の姿で見張り、カートとデイヴは外から助ける。",
         "The night of the unveiling",
         "On the night of the unveiling, Hank and Hope are there as invited guests. Scott shrinks and, with a swarm of flying ants, gets into the building.\n"
         "Luis keeps watch dressed as a guard, while Kurt and Dave help from outside."),
        ("データを壊し、爆弾を仕掛ける",
         "スコットは、電気を通すアリたちを使って、会社のコンピュータの大事な機械を壊し、データを消していく。そして建物のあちこちに爆弾を仕掛ける。",
         "Wrecking the servers, planting bombs",
         "Using the electricity-conducting ants, Scott wrecks the company's servers and wipes the data. Then he plants explosives throughout the building."),
        ("見破られた計画",
         "スコットはイエロージャケットのしまってある部屋にたどり着くが、クロスはすでに気づいていた。スコットは閉じこめられ、ハンクとホープも銃を向けられる。\n"
         "クロスは、イエロージャケットとアントマンのスーツの両方を、ヒドラに売るつもりだと話す。",
         "The plan is uncovered",
         "Scott reaches the room where the Yellowjacket is kept, but Cross is already onto them. Scott is trapped, and Hank and Hope are held at gunpoint.\n"
         "Cross says he plans to sell both the Yellowjacket and the Ant-Man suit to Hydra."),
        ("撃たれるハンク",
         "スコットは抜け出し、ホープと2人でヒドラの男たちを次々に倒す。しかしその中で、クロスがハンクを撃ち、ハンクは傷を負う。\n"
         "カーソンは、クロスが作った粒子の入った小さなびんを持って逃げてしまう。",
         "Hank is shot",
         "Scott breaks free, and he and Hope take down the Hydra men one after another. In the chaos, Cross shoots Hank, wounding him.\n"
         "Carson escapes with a vial of Cross's particles."),
        ("アントニーの最期",
         "イエロージャケットを持って屋上のヘリコプターへ逃げるクロスを、スコットはアントニーに乗って追いかける。しかしクロスの攻撃で、アントニーは撃ち落とされて死んでしまう。",
         "Antony's end",
         "Cross flees to the rooftop helicopter with the Yellowjacket, and Scott chases him riding Antony. Cross shoots Antony down, killing him."),
        ("崩れる建物",
         "スコットが仕掛けた爆弾が爆発し、ピム・テックの建物は内側に崩れ落ちる。研究のデータも一緒に消える。ハンクとホープは、なんとか外へ逃げ出す。",
         "The building comes down",
         "The explosives go off, and the Pym Tech building collapses inward, taking the research with it. Hank and Hope make it out."),
        ("ヘリコプターとかばんの中の戦い",
         "空を飛ぶヘリコプターの中で、クロスはイエロージャケットを着てスコットと戦う。2人は小さくなったまま、クロスのかばんの中にまで入って戦い続ける。\n"
         "ヘリコプターは、住宅の庭のプールに落ちる。",
         "Fighting in a helicopter and a briefcase",
         "Aboard the helicopter, Cross puts on the Yellowjacket and fights Scott. At tiny size, the two keep fighting even inside Cross's briefcase.\n"
         "The helicopter ends up crashing into the swimming pool of a suburban home."),
    ]),
    ("第7部 キャシーの部屋の決戦", "Part 7: Showdown in Cassie's room", [
        ("パクストンに捕まる",
         "元の大きさに戻ったスコットは、パクストンたち警察に捕まり、パトカーに乗せられる。\n"
         "クロスは、スコットの弱みがキャシーだと知り、キャシーの家へ向かう。",
         "Arrested by Paxton",
         "Back at full size, Scott is arrested by Paxton and the police and put in a patrol car.\n"
         "Cross, knowing Cassie is Scott's weak spot, heads for her house."),
        ("パトカーから抜け出す",
         "クロスがキャシーをねらっていると知ったスコットは、アリたちの助けでパトカーから抜け出し、キャシーの家へ急ぐ。パクストンもあとを追う。",
         "Out of the patrol car",
         "Learning that Cross is after Cassie, Scott escapes the patrol car with the ants' help and races to her house. Paxton follows."),
        ("おもちゃの電車の上で",
         "クロスは、キャシーの部屋でキャシーを人質にとる。スコットは小さくなってクロスと戦う。2人は、キャシーのきかんしゃトーマスの鉄道模型の上で戦う。\n"
         "小さい目で見るとすさまじい戦いだが、ふつうの大きさで見ると、おもちゃの電車がひっくり返っているだけだった。スコットがおもちゃの電車を大きくすると、電車は家の壁を突き破って外へ飛び出す。",
         "On the toy train",
         "Cross holds Cassie hostage in her bedroom. Scott shrinks down and fights him on Cassie's Thomas the Tank Engine train set.\n"
         "At ant scale it's a ferocious battle; at normal size, it's just a toy train tipping over. When Scott enlarges the toy engine, it smashes through the wall of the house."),
        ("イエロージャケットを止める",
         "クロスのスーツは固くて、ふつうの攻撃では壊せない。クロスはキャシーにせまる。\n"
         "スコットは、二度と戻れないかもしれないと知りながら、小さくなる力を止める仕組みを外す。原子よりも小さくなって、イエロージャケットの中にもぐりこみ、仕掛けを壊す。\n"
         "壊れたスーツは止まらずに縮み続け、クロスはスーツごと小さくなって消えてしまう。",
         "Stopping the Yellowjacket",
         "Cross's armor is too tough to break with ordinary blows, and he closes in on Cassie.\n"
         "Knowing he may never come back, Scott overrides his regulator. Shrinking smaller than an atom, he slips inside the Yellowjacket and wrecks its mechanism.\n"
         "The broken suit keeps shrinking uncontrollably, and Cross shrinks away and vanishes with it."),
        ("量子の世界",
         "スコットもそのまま縮み続け、量子の世界に落ちていく。そこは、時間も大きさもはっきりしない、ふしぎな光と形の世界だった。\n"
         "キャシーの呼ぶ声が聞こえたスコットは、大きくなるための粒子をスーツに入れ、なんとか元の世界へ戻ってくる。",
         "The Quantum Realm",
         "Scott keeps shrinking too, down into the Quantum Realm, a strange world of light and shapes where time and size lose their meaning.\n"
         "Hearing Cassie call for him, he loads the growth particles into his suit and manages to make his way back."),
        ("戻ってきたスコット",
         "キャシーの部屋で元の大きさに戻ったスコットに、キャシーが抱きつく。パクストンは、スコットがキャシーを守ったことを目の前で見ていた。\n"
         "ハンクの屋敷に戻ったスコットに、ホープはキスをする。ハンクは、量子の世界から戻ってきたスコットを見て、ジャネットもまだ生きていて、戻せるかもしれないと考える。",
         "Scott comes back",
         "Back at full size in Cassie's room, Scott is hugged by Cassie. Paxton saw with his own eyes that Scott saved her.\n"
         "Back at Hank's house, Hope kisses Scott. Seeing that Scott came back from the Quantum Realm, Hank begins to wonder whether Janet might still be alive, and might be brought back."),
    ]),
    ("第8部 その後", "Part 8: Afterward", [
        ("新しい家族",
         "パクストンは、スコットのしたことを見のがし、刑務所に戻らないようにかばう。スコットは、マギー、パクストン、キャシーと一緒に食事をする仲になる。\n"
         "家の庭には、スコットが戦いの中で大きくしたアリが、キャシーのペットのようにして暮らしていた。",
         "A new family",
         "Paxton covers for Scott and keeps him out of prison. Scott now shares meals with Maggie, Paxton and Cassie.\n"
         "In the yard lives an ant Scott enlarged during the fight, now something like Cassie's pet."),
        ("ルイスが聞いたうわさ",
         "スコットはルイスと会う。ルイスはまた、人から人へと伝わってきたうわさ話を長々と話す。話の中身は、翼をつけたヒーローが、アントマンを探しているというものだった。",
         "The word Luis heard",
         "Scott meets Luis, who tells another long story of how a rumor reached him from person to person: a hero with wings is looking for Ant-Man."),
        ("エンドクレジットの途中",
         "ハンクはホープを地下の部屋に連れていき、ジャネットと一緒に作っていた新しいワスプのスーツを見せる。ハンクはそのスーツをホープに託そうとし、ホープは喜んで受け取ろうとする。",
         "Mid-credits",
         "Hank takes Hope to a room downstairs and shows her a new Wasp suit he and Janet had been working on. He offers it to her, and she is glad to take it."),
        ("エンドクレジットの後",
         "どこかの建物で、スティーブ・ロジャースとサムが、金属の腕を機械に固定されたバッキーを見つめている。スティーブは、トニーには協定のことがあって連絡できないと話す。\n"
         "サムは、助けになりそうな人を知っていると言う。",
         "After the credits",
         "Somewhere, Steve Rogers and Sam stand over Bucky, whose metal arm is clamped in a machine. Steve says they can't call Tony because of the Accords.\n"
         "Sam says he knows a guy who could help."),
    ]),
    ("まとめ", "Summary", [
        ("スコットがしたこと",
         "会社の悪事をこらしめて刑務所に入っていたが、出所しても前科のせいで仕事がなく、娘キャシーに会えなかった（第2部）。\n"
         "ハンクの試験としてスーツを盗み（第3部）、新しいアントマンになってピム・テックに忍びこみ、データを壊して建物を爆破した（第6部）。最後は量子の世界に落ちる危険をおかしてクロスを止め、キャシーを守った（第7部）。",
         "What Scott did",
         "Jailed for punishing a crooked company, he couldn't find work after release because of his record, and couldn't see his daughter Cassie (Part 2).\n"
         "He stole the suit as Hank's test (Part 3), became the new Ant-Man, broke into Pym Tech, wrecked its data and blew up the building (Part 6). Finally, risking the Quantum Realm, he stopped Cross and saved Cassie (Part 7)."),
        ("ハンクとホープ",
         "ハンクは、ピム粒子が悪用されるのをおそれて1989年にシールドを去った（第1部）。ジャネットを失った過去をホープに隠していたが、打ち明けて仲直りした（第4部）。\n"
         "ホープは、クロスのそばで働きながら父と手を組み、スコットを鍛えた（第3部・第4部）。最後に父から新しいワスプのスーツを託される（第8部）。",
         "Hank and Hope",
         "Fearing misuse of the Pym Particles, Hank left S.H.I.E.L.D. in 1989 (Part 1). He had hidden the truth about losing Janet from Hope, but finally told her and they made up (Part 4).\n"
         "Hope worked beside Cross while secretly teaming with her father, and trained Scott (Parts 3 and 4). In the end her father offers her a new Wasp suit (Part 8)."),
        ("クロスがしたこと",
         "ハンクの元弟子で、ハンクを会社から追い出し、イエロージャケットを作った（第2部）。研究を疑ったフランクを殺し（第2部）、スーツをヒドラに売ろうとした（第6部）。最後はキャシーを人質にとったが、スコットにスーツを壊された（第7部）。",
         "What Cross did",
         "Hank's former protégé, he forced Hank out of the company and built the Yellowjacket (Part 2). He killed Frank for doubting his work (Part 2) and tried to sell the suit to Hydra (Part 6). In the end he took Cassie hostage, but Scott wrecked his suit (Part 7)."),
        ("死んだ人たち（話の順に）",
         "・フランク（第2部）：クロスの研究を疑ったため、クロスに不完全な粒子の銃で撃たれ、体が縮んでかたまりになって死ぬ。\n"
         "・アントニー（第6部）：スコットを乗せて飛んでいた羽アリ。逃げるクロスを追う途中、クロスの攻撃で撃ち落とされる。\n"
         "・ダレン・クロス（第7部）：スコットに壊されたイエロージャケットが縮み続け、スーツごと小さくなって消える。\n"
         "・ジャネット（第4部の話の中）：1987年にミサイルを止めるため縮み続け、量子の世界に消えた。ハンクは死んだと思っていたが、最後に生きている望みが出てくる。",
         "Who died (in order)",
         "- Frank (Part 2): for doubting Cross's work, he's shot with Cross's unstable particle gun and shrinks into a lump.\n"
         "- Antony (Part 6): the flying ant Scott rode, shot down by Cross during the chase.\n"
         "- Darren Cross (Part 7): the Yellowjacket, sabotaged by Scott, keeps shrinking, and he vanishes with it.\n"
         "- Janet (told in Part 4): in 1987 she kept shrinking to stop a missile and vanished into the Quantum Realm. Hank believed she was dead, but at the end there's hope she's alive."),
    ]),
]
