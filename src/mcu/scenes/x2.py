# 『X-MEN2』（2003年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 2026-11-15 運営者の指摘（観ながら読むので、2もしっかり直してほしい）で、映画で流れる順番に並べ直し、抜けていた場面を足した。
# 順番と事実は、X-MEN映画のファン事典（xmenmovies.fandom.com）の作品ページのあらすじと、人物ごとのページ
# （ウルヴァリン、プロフェッサーX、ストーム、サイクロップス、ストライカー、ミスティーク、マグニートー、ローグ、アイスマン、
# パイロ、ジーン、レディ・デスストライク、ラウリオ）のこの作品の部分、英語版・日本語版ウィキペディアで確かめた。
# 台本（imsdb）と themoviespoiler.com には、この作品のページがなかった。
# 前の版からの主な直し：
#   ・アルカリ湖の場面を博物館の前に、ストライカーと大統領の場面をローガンが学園に戻る前に移した。
#   ・プロフェッサーXたちが捕まるのは「帰り道」ではなく面会の最中（ガス）。教会の場面はその前。
#   ・ミスティークが看守に近づく酒場の場面は、学園の襲撃の後。マグニートーの脱獄は、ボビーの家の場面の途中にはさまる。
#   ・ダムの中でプロフェッサーXがジェイソンに会う場面は、学園の襲撃の後・ボビーの家の前（前の版は第3部の最後に置いていた）。
#   ・ストライカーを最後にコンクリートの壁へ鎖でつないだのはマグニートー（ローガンはその前にヘリコプターにつないだ）。
#   ・ローグがつかんだのはジョンの足首。基地の中の戦いを、映画で切りかわる順に分けた。全体を5部から6部にした。
# 資料どうしで順番がはっきりしない所は、次のように置いた（どれも前後1〜2場面の差）：
#   ・ストライカーがマグニートーに薬を使う場面（1-8）と、ミスティークがストライカーの部屋に入る場面（1-9）の位置
#   ・マグニートーの脱獄（2-7）とボビーの家の場面（2-6、2-8）の前後
#   ・少女の幻の最初の場面（3-7）の位置、基地の中でジーンとサイクロップス、ローガンの場面が切りかわる細かい順
# 書かなかった所（資料が1つだけ、または食い違う）：博物館でジュビリーが力を出す場面とジーンが力でジェット機を操る場面（どちらも未公開場面）、
# セレブロの前の兵士たちがどうなったか、ストライカーがさらった子どもを生かしておく理由、ローグが火を消すのに使った力が誰のものか、
# 大統領に「見ている」と言うのが誰か、ストライカーの妻の死に方の細かい所。
# セリフは日本語の言い回しを確かめられなかったので、日本語版はカギかっこで引用せず内容だけ書いた。英語版の短い引用は英語の資料から。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 大統領の襲撃", "Part 1: Attack on the President", [
        ("ホワイトハウスの青い影",
         "ホワイトハウスで、見学ツアーが行われている。その中にまぎれていた青い肌のミュータントが、煙とともに一瞬で消えては別の場所に現れながら、警護の人たちを次々に倒していく。\n"
         "ミュータントは大統領の執務室までたどり着き、大統領を机に押さえつけてナイフを振り上げる。しかしその瞬間、倒れていた警護の人に腕を撃たれ、姿を消す。\n"
         "残されたナイフには、ミュータントの自由を求める言葉が付けられていた。",
         "A blue blur in the White House",
         "A tour is underway at the White House. A blue-skinned mutant hidden among the visitors starts vanishing in puffs of smoke and reappearing elsewhere, taking down the Secret Service agents one after another.\n"
         "He reaches the Oval Office, pins the President to his desk and raises a knife. At that moment a downed agent shoots him in the arm, and he disappears.\n"
         "The knife he leaves behind carries a message: \"Mutant Freedom Now!\""),
        ("雪のアルカリ湖",
         "カナダの山の中。ローガンは、自分の過去の手がかりを探して、雪におおわれたアルカリ湖にやって来る。プロフェッサーXに教えられた、軍の施設があった場所である。\n"
         "しかしそこにあったのは、ダムのそばの、こわれて使われなくなった建物だけだった。ローガンは何も見つけられない。",
         "Alkali Lake in the snow",
         "In the Canadian Rockies, Logan arrives at snow-covered Alkali Lake, looking for clues to his past. Professor X had told him a military facility once stood here.\n"
         "All he finds are abandoned, crumbling buildings near a dam. There is nothing left for him."),
        ("博物館の見学",
         "プロフェッサーXの学園の生徒たちが、博物館へ見学に来ている。ジーンは、まわりの人たちの心の声が一度に聞こえてきて苦しむ。サイクロップスは、前の戦い（自由の女神の事件）のあとからジーンの力がどんどん強くなっていることを心配する。ジーンは、何か悪いことが起こる気がすると打ち明ける。\n"
         "食堂では、ローグ、ボビー（アイスマン）、ジョン（パイロ）の3人に、2人の若者がからんでくる。炎を操れるジョンは、ライターの火を大きくして相手の服に火をつける。ボビーが氷の力でその火を消す。\n"
         "そのとき、まわりの人たちがみな、ぴたりと動きを止める。プロフェッサーXが現れ、力を見せびらかしたジョンをしかる。テレビでは、大統領がミュータントに襲われたニュースが流れていた。一行は博物館を出る。",
         "The museum trip",
         "Students from Professor X's school are on a museum field trip. Jean is overwhelmed as the thoughts of everyone around her flood into her head at once. Cyclops is worried: ever since the last battle at Liberty Island, her powers have kept growing. Jean admits she feels something terrible is about to happen.\n"
         "In the food court, two young men pick on Rogue, Bobby (Iceman) and John (Pyro). John, who can control fire, makes the flame of his lighter leap onto one boy's clothes. Bobby puts it out with ice.\n"
         "Suddenly everyone around them freezes in place. Professor X wheels in and scolds John for showing off. On a TV, the news reports a mutant attack on the President. The group leaves the museum."),
        ("学園での話し合い",
         "学園に戻ったX-MENは、事件について話し合う。サイクロップスはマグニートーのしわざだと考えるが、プロフェッサーXとジーンは、牢屋の中からできることではないし、マグニートーの得にもならないと言う。\n"
         "プロフェッサーXは、政府がミュータントに対してきびしい手を打ってくることを心配している。政府より先に犯人を見つけるため、居場所が分かったらジーンとストームが迎えに行くことになる。",
         "A meeting at the school",
         "Back at the school, the X-Men discuss the attack. Cyclops thinks Magneto is behind it, but Professor X and Jean point out that he couldn't arrange it from prison, and that it would only hurt his cause.\n"
         "Professor X fears the government will crack down hard on mutants. They need to reach the attacker before the authorities do, so once he has a location, Jean and Storm will go and pick him up."),
        ("ストライカーと大統領",
         "大統領の執務室に、軍の科学者ウィリアム・ストライカー大佐が来ている。そこへケリー上院議員も入ってくる（本物のケリーは前の作品で死んでいて、これはマグニートーの仲間ミスティークが化けた姿）。\n"
         "ストライカーは学園の写真を見せ、ここはただの学校ではなく、バスケットボールのコートの下にジェット機まで隠していると話す。この情報は、牢屋のマグニートーを取り調べて手に入れたものだった。大統領は、学園に入って調べることを認める。ただし、子どもの死体がニュースに出るようなことだけはするなと言う。\n"
         "廊下で、ケリー（ミスティーク）はストライカーに、マグニートーの牢屋を訪ねたいと頼むが、断られる。ストライカーのそばには、秘書のユリコがついている。",
         "Stryker and the President",
         "Colonel William Stryker, a military scientist, is in the Oval Office. Senator Kelly joins them (the real Kelly died in the last film; this is Magneto's shapeshifting ally Mystique in disguise).\n"
         "Stryker shows photos of the school and says it is no ordinary school: there is even a jet hidden under the basketball court. He got the information by interrogating the imprisoned Magneto. The President authorizes him to go in and investigate, but warns that he doesn't want to see a dead mutant child on the evening news.\n"
         "In the hallway, Kelly (Mystique) asks Stryker to arrange a visit to Magneto's prison and is refused. At Stryker's side is his assistant, Yuriko."),
        ("学園に戻ったローガン",
         "学園では、ローグとボビーがつき合い始めている。しかしローグは、触れた相手の力と命を吸い取ってしまうため、キスもできない。\n"
         "そこへ、サイクロップスのバイクに乗ったローガンが帰ってくる。ローグは喜んで抱きつく。ボビーは握手をしながら、ローガンの手を少し凍らせてみせる。\n"
         "ストームとジーンは、犯人を迎えにボストンへ出かけるところだった。ローガンはジーンに気のあるそぶりを見せ、そこへ来たサイクロップスと、とげのある言葉を交わす。",
         "Logan comes home",
         "At the school, Rogue and Bobby have started dating. But because Rogue's touch drains a person's power and life, they can't even kiss.\n"
         "Then Logan rides up on Cyclops's motorcycle. Rogue runs to hug him. Bobby shakes his hand and frosts it over a little.\n"
         "Storm and Jean are just about to leave for Boston to pick up the attacker. Logan flirts with Jean, and trades barbs with Cyclops when he walks in."),
        ("セレブロの中で",
         "プロフェッサーXは、ミュータントを探す装置セレブロで、大統領を襲った犯人を探している。ローガンが入ってくると、まわりに無数の光が浮かぶ。白い光は人間、赤い光はミュータントで、セレブロを使うと世界中の人の心とつながる。もっと強く念じれば早く見つかるが、それをすると相手を殺してしまうとプロフェッサーXは話す。\n"
         "やがて犯人が動きを止め、ドイツ語で祈る声が聞こえて、居場所がはっきりする。ローガンは、アルカリ湖には何もなかったと伝え、もう一度心を読んで過去を調べてほしいと頼む。プロフェッサーXは、自分の力で見つけなければならないこともあると答える。\n"
         "プロフェッサーXは、今夜は子どもたちを見ていてほしいとローガンに頼む。自分はサイクロップスと、古い友人に会いに行くという。",
         "Inside Cerebro",
         "Professor X is using Cerebro, the device that finds mutants, to track the President's attacker. When Logan walks in, countless lights appear around them: white for humans, red for mutants. Through Cerebro his mind is linked to everyone on Earth. He could find the attacker faster by concentrating harder, he says, but that would kill him.\n"
         "Then the attacker stops moving, a voice is heard praying in German, and Professor X has his location. Logan reports that there was nothing at Alkali Lake and asks the Professor to read his mind again. Professor X answers that some things the mind has to discover for itself.\n"
         "He asks Logan to watch the children tonight. He and Cyclops are going to visit an old friend."),
        ("牢屋のマグニートーと薬",
         "その古い友人マグニートーは、金属を一つも使っていないプラスチックの牢屋に入れられている。そこへ来たのはストライカーだった。\n"
         "看守のラウリオがマグニートーをなぐって押さえつけ、ストライカーが首の後ろに薬をたらす。これは、ミュータントを言いなりにする薬である。ストライカーは、プロフェッサーXの学園と、セレブロという装置について、すべて話すよう命じる。",
         "Magneto, drugged in his cell",
         "That old friend, Magneto, is held in a prison made entirely of plastic, with no metal anywhere. His visitor now is Stryker.\n"
         "The guard, Laurio, beats Magneto and holds him down while Stryker drips a chemical onto the back of his neck. It is a drug that makes mutants obey. Stryker orders him to tell everything about the house Xavier built and the machine called Cerebro."),
        ("ストライカーの部屋に入るミスティーク",
         "ミスティークは、今度はユリコの姿に化けて、ストライカーの部屋に入りこむ。コンピューターから、マグニートーの牢屋のくわしい情報と、もう一つのセレブロを作る計画の図面を見つける。\n"
         "そこへ本物のユリコが戻ってくる。ミスティークは掃除の人の姿に化け、ごみを持って、気づかれずに部屋を出る。",
         "Mystique in Stryker's office",
         "Now disguised as Yuriko, Mystique slips into Stryker's office. On his computer she finds the details of Magneto's prison, and plans for building a second Cerebro.\n"
         "The real Yuriko comes back. Mystique turns into a janitor and walks out with the trash, unnoticed."),
        ("教会のナイトクローラー",
         "夜。ジーンとストームは、ボストンの古い教会に着く。上のほうからドイツ語の声が聞こえるが、声の場所が次々に変わる。相手は瞬間移動ができるミュータントだった。\n"
         "ストームが雷を落として足場をこわし、落ちてきたところをジーンが力で受け止める。青い肌のミュータントはカート・ワグナーと名乗る。カートは、大統領を襲ったとき、自分のしていることが見えているのに止められず、悪い夢のようだったと話す。\n"
         "カートの首の後ろには傷あとがあった。誰かに操られていたのである。",
         "Nightcrawler in the church",
         "Night. Jean and Storm reach an old church in Boston. A voice speaks German from above, but it keeps coming from a different place: he is a teleporter.\n"
         "Storm brings down a bolt of lightning that breaks his perch, and Jean catches him in mid-air. The blue-skinned mutant gives his name as Kurt Wagner. During the attack on the President, he says, he could see what he was doing but couldn't stop himself, like a bad dream.\n"
         "On the back of his neck is a wound. Someone had been controlling him."),
        ("面会とわな",
         "プロフェッサーXは、プラスチックの車いすでマグニートーの牢屋に入る。サイクロップスは外で待つ。\n"
         "マグニートーは、ストライカーが何度も来ていたと話す。プロフェッサーXはストライカーを知っていた。息子のジェイソンが、昔、学園の生徒だったからである。マグニートーは、薬にさからえず、ストライカーにすべてを話してしまったと明かす。\n"
         "そのとき、牢屋の中にガスが流れこむ。面会そのものが、わなだった。2人は眠らされる。外では、サイクロップスが看守たちを倒すが、ユリコに飛びかかられて気を失う。プロフェッサーXとサイクロップスは連れ去られる。",
         "The visit, and the trap",
         "Professor X is wheeled into Magneto's cell in a plastic wheelchair. Cyclops waits outside.\n"
         "Magneto says Stryker has been visiting him. Professor X knows the name: Stryker's son Jason was once a student at the school. Magneto confesses that he couldn't resist the drug and told Stryker everything.\n"
         "Then gas hisses into the cell. The visit itself was the trap, and both men pass out. Outside, Cyclops takes down the guards, but Yuriko leaps on him and knocks him out. Professor X and Cyclops are taken away."),
    ]),
    ("第2部 学園の襲撃", "Part 2: The raid on the school", [
        ("眠れない夜",
         "その夜の学園。ローガンは、昔の実験の悪夢で目を覚ます。居間では、まばたきでテレビのチャンネルを変える男の子ジョーンズが起きていた。\n"
         "台所ではボビーがアイスクリームを食べている。ボビーは、ローガンのソーダのびんに息を吹きかけて冷やす。ボビーの両親は、息子がふつうの寄宿学校に通っていると思っているという。",
         "A sleepless night",
         "That night at the school, Logan wakes from a nightmare about the old experiments. In the living room a boy named Jones is still up, changing TV channels by blinking.\n"
         "In the kitchen, Bobby is eating ice cream. He chills Logan's bottle of soda with a breath. His parents, he says, think he goes to an ordinary prep school."),
        ("夜の襲撃",
         "ローガンが足音に気づく。ストライカーの兵士たちが学園に忍びこみ、眠っている生徒たちに眠り薬の矢を撃ちこんでいた。\n"
         "目を覚ました女の子サイリーンが、耳をつんざく叫び声を上げる。その声で、学園じゅうの生徒が飛び起きる。ローガンは爪で兵士たちを次々に倒す。\n"
         "体を金属に変えられる生徒ピーター（コロッサス）は一緒に戦おうとするが、ローガンに子どもたちを頼むと言われ、生徒たちを連れて隠し通路から逃げる。それでも、6人の生徒が兵士たちに連れ去られる。",
         "The night raid",
         "Logan hears footsteps. Stryker's soldiers have crept into the school and are shooting the sleeping students with tranquilizer darts.\n"
         "A girl named Siryn wakes and lets out an ear-splitting scream that rouses the whole school. Logan cuts down soldier after soldier with his claws.\n"
         "Peter (Colossus), a student who can turn his body to metal, offers to fight, but Logan tells him to look after the kids, and he leads students out through hidden tunnels. Even so, six students are captured."),
        ("ストライカーとの対面",
         "ローガンは、ローグ、ボビー、ジョンを先に行かせ、兵士たちの前に残る。そこへストライカーが現れ、撃つなと命じる。ストライカーはローガンを「ウルヴァリン」と呼び、15年ぶりだと言う。ローガンは、相手が誰なのか思い出せない。\n"
         "答えを聞こうとするローガンの前に、ボビーが厚い氷の壁を作って2人をへだてる。ローガンは3人を連れて車庫へ走り、サイクロップスの車で逃げる。\n"
         "ストライカーの兵士たちは地下のセレブロをこじ開け、必要な部品を運び出す。車の中で、ローガンは預けていた認識票をローグから返される。車には通信機があった。4人は、ストームとジーンが向かったボストンへ行くことにする。ボストンにはボビーの実家がある。",
         "Face to face with Stryker",
         "Logan sends Rogue, Bobby and John ahead and stays to face the soldiers. Stryker appears and orders them not to shoot. He calls Logan \"Wolverine\" and says it has been fifteen years. Logan can't remember who he is.\n"
         "Before Logan can get any answers, Bobby raises a thick wall of ice between the two men. Logan runs to the garage with the three kids and they escape in Cyclops's car.\n"
         "Stryker's men cut their way into Cerebro and strip out the parts they need. In the car, Rogue gives Logan back the dog tag he left with her. They find a communicator in the car and decide to head for Boston, where Storm and Jean went. Bobby's family lives there."),
        ("酒場のミスティーク",
         "ミスティークは、きれいな女の人に化けて、酒場で看守のラウリオに近づく。ビールに薬を入れ、トイレに誘いこんで眠らせる。\n"
         "そして、眠ったラウリオの体に、銀色の液体（鉄）をたっぷり注射する。",
         "Mystique at the bar",
         "Disguised as an attractive woman, Mystique approaches the guard Laurio in a bar. She drugs his beer, lures him into the restroom, and he passes out.\n"
         "Then she injects the sleeping Laurio with a large dose of a silver liquid: iron."),
        ("ダムの中のプロフェッサーX",
         "プロフェッサーXは、アルカリ湖の基地で目を覚ます。頭には、心の力を封じる装置を付けられている。サイクロップスは別の場所で、ストライカーに薬で操られようとしていた。\n"
         "ストライカーは昔、ミュータントの息子ジェイソンを「治して」もらおうと学園に入れた。しかし家に戻ったジェイソンは両親をうらみ、幻を見せて苦しめた。妻はそのせいで自ら命を絶ったと、ストライカーは話す。ユリコもまた、首の後ろの薬で操られているミュータントだった。プロフェッサーXは、大統領を襲わせたのがストライカーだと気づく。\n"
         "ストライカーは、車いすに乗った若い男を連れてくる。手術で話すこともできなくされたジェイソンだった。人を操る薬は、ジェイソンの脳から取ったものである。プロフェッサーXほどの力には薬が効かないので、ジェイソンの幻を直接使うという。",
         "Professor X inside the dam",
         "Professor X wakes up in the base at Alkali Lake. A device on his head blocks his powers. Somewhere else in the base, Cyclops is being put under Stryker's drug.\n"
         "Years ago Stryker sent his mutant son Jason to the school to be \"cured.\" When Jason came home he resented his parents and tormented them with illusions, and Stryker says that drove his wife to kill herself. Yuriko, too, is a mutant kept under control by the drug on her neck. Professor X realizes that Stryker arranged the attack on the President.\n"
         "Stryker wheels in a young man in a wheelchair: Jason, operated on so that he can no longer even speak. The mind-control drug comes from Jason's brain. It isn't strong enough for someone as powerful as Xavier, so Stryker will use Jason's illusions on him directly."),
        ("ボビーの家",
         "ローガンたち4人は、ボストンのボビーの実家に着く。家には誰もいない。ボビーは、着がえを探してローグに渡す。2人は初めてキスをするが、ローグの力が働き始め、ボビーは苦しくなって離れる。\n"
         "台所でビールを取り出したローガンは、気配を感じて爪を出す。相手は家の猫で、猫はローガンの爪をなめる。\n"
         "そこへボビーの両親と弟ロニーが帰ってきて、ローガンと鉢合わせする。ボビーはあわててローガンを学校の先生だと紹介し、話さなければならないことがあると言う。",
         "Bobby's house",
         "The four arrive at Bobby's family home in Boston. Nobody is home. Bobby finds a change of clothes for Rogue. They share their first real kiss, but her power begins to take hold and Bobby has to pull away.\n"
         "In the kitchen, Logan takes a beer and, sensing something, pops his claws. It is the family cat, which licks them.\n"
         "Then Bobby's parents and his brother Ronny come home and run right into Logan. Bobby hurries down, introduces him as \"Professor Logan,\" and says there is something he needs to tell them."),
        ("マグニートーの脱獄",
         "次の日、ラウリオがマグニートーの牢屋に食事を運んでくる。入り口の機械がわずかに反応するが、ほかの看守は気にしない。\n"
         "マグニートーは、ラウリオの体がいつもと違うことに気づく。そして力を使い、ラウリオの体から鉄を無理やり引き出す。ラウリオは死ぬ。\n"
         "マグニートーは、引き出した鉄を小さな玉にして弾丸のように飛ばし、プラスチックの牢屋をこわす。玉の一つを平らな円盤にしてその上に乗り、深い穴をこえて外へ出る。ほかの看守たちも殺される。",
         "Magneto escapes",
         "The next day, Laurio brings Magneto's meal to the cell. The scanner at the entrance gives a faint blip, but the other guards ignore it.\n"
         "Magneto notices that something about Laurio is different. Then, with his power, he rips the iron out of Laurio's body. Laurio dies.\n"
         "Magneto shapes the iron into small balls and fires them like bullets, shattering the plastic cell. He flattens one into a disc, rides it across the deep gap around the cell, and kills the other guards on his way out."),
        ("ボビーの告白",
         "居間で、ボビーは家族に、自分がミュータントだと打ち明けたところだった。母親は「ミュータント」という言葉を口にするのもためらい、ミュータントでいるのをやめてみたことはないのかとたずねる。\n"
         "ローグにうながされ、ボビーは母親のカップの中身を凍らせてみせる。それを見た弟ロニーは、怒って部屋を出ていく。\n"
         "ロニーは2階から警察に電話をかけ、ミュータントが家族を人質にしていると通報する。",
         "Bobby tells his family",
         "In the living room, Bobby has just told his family he is a mutant. His mother can hardly bring herself to say the word, and asks, \"Have you tried... not being a mutant?\"\n"
         "At Rogue's suggestion, Bobby shows them what he can do and freezes the drink in his mother's cup. His brother Ronny storms out of the room.\n"
         "From upstairs, Ronny calls the police and tells them mutants are holding his family hostage."),
        ("ジェット機の中のストームとカート",
         "ジェット機の中で、ストームはカートの体の模様についてたずねる。カートは、天使のしるしを自分で刻んだもので、罪を一つおかすたびに一つ入れていると答える。\n"
         "カートは、自分をこわがる人たちを憎まず、あわれんでいると話す。ストームは、怒りが生きる力になることもあると言い、信心深いカートは、信じることも力になると返す。\n"
         "ジーンが、通じる通信機を見つける。ボビーの家の玄関先で、ローガンが通信に出る。学園が兵士に襲われたこと、プロフェッサーXとサイクロップスに連絡がつかないことを伝え合い、ジェット機はボビーの家へ向かう。",
         "Storm and Kurt on the jet",
         "On the jet, Storm asks Kurt about the markings on his body. They are angelic symbols he carved himself, he says, one for every sin.\n"
         "Kurt says he doesn't hate the people who fear him; he pities them. Storm tells him anger can help you survive, and the devout Kurt replies that so can faith.\n"
         "Jean picks up an active communicator. On the Drakes' porch, Logan answers. They tell each other the news, that soldiers raided the school and that no one can reach Professor X or Cyclops, and the jet heads for Bobby's house."),
        ("警察との衝突と、ジェット機の迎え",
         "ローガンたちが家を出ると、警察官たちが家を取り囲んでいた。警察官は、爪を出したローガンに刃物を捨てろと命じる。ローガンが爪をしまって説明しようとしたとき、おびえた警察官がローガンの頭を撃つ。ローガンは倒れる。\n"
         "ボビーとローグは地面に伏せさせられる。ジョンは怒って炎を放ち、パトカーを次々に爆発させる。ローグがジョンの足首を素手でつかんで力を吸い取り、炎を消す。\n"
         "ローガンの傷が治り、弾が頭からこぼれ落ちる。そこへジェット機が庭に下りてくる。ボビーは、窓から見ている家族を振り返ってから乗りこむ。",
         "The police standoff, and the jet",
         "When Logan and the kids step outside, police have surrounded the house. An officer orders Logan, claws out, to drop the knives. As Logan retracts them and tries to explain, a frightened officer shoots him in the head. He drops.\n"
         "Bobby and Rogue are forced to the ground. John, furious, hurls fire and blows up one police car after another. Rogue grabs his ankle with her bare hand, drains his power and puts the flames out.\n"
         "Logan's wound heals and the bullet falls out of his forehead. The jet touches down on the lawn. Bobby looks back at his family watching from the window, then boards."),
    ]),
    ("第3部 敵と手を組む", "Part 3: An alliance with the enemy", [
        ("戦闘機の攻撃",
         "ジェット機の中で、カートはローガンに、サーカスではナイトクローラーと呼ばれていたと名乗る。\n"
         "学園の近くまで来たとき、軍の戦闘機2機が後ろにつき、下りるよう命じる。ストームは従わず、空を暗くしていくつもの竜巻を起こす。1機は操縦できなくなって落ちるが、もう1機は落ちる前にミサイルを2発撃つ。\n"
         "ジーンが目を光らせて力を使い、1発をそらす。しかしもう1発がすぐ後ろで爆発し、機体に穴が開く。ベルトをしていなかったローグが外へ吸い出される。ナイトクローラーが瞬間移動で外へ飛び、空中でローグをつかまえて連れ戻す。",
         "Fighter jets attack",
         "On the jet, Kurt introduces himself to Logan: in the circus he was known as Nightcrawler.\n"
         "As they near the school, two Air Force fighters fall in behind them and order them to descend. Storm refuses, darkens the sky and whips up a field of tornadoes. One fighter loses control and goes down, but the other fires two missiles before its pilot ejects.\n"
         "Jean, her eyes glowing, uses her power to throw one missile off course. The other explodes right behind them and tears a hole in the hull. Rogue, who wasn't strapped in, is sucked out. Nightcrawler teleports outside, catches her in mid-air and brings her back."),
        ("落ちるジェット機を止めた人",
         "ジェット機は落ちていく。地面にぶつかる直前、機体の穴がひとりでにふさがり、ジェット機は空中でぴたりと止まる。ジーンの力ではなかった。\n"
         "森の中で待っていたのは、マグニートーとミスティークだった。",
         "Who stopped the crash",
         "The jet plunges toward the ground. Just before impact, the hole in the hull seals itself and the jet stops dead in the air. It isn't Jean's doing.\n"
         "Waiting in the woods are Magneto and Mystique."),
        ("たき火のそばで",
         "その夜、一行は森でたき火を囲む。マグニートーはストライカーの計画を話す。ストライカーが学園を襲ったのは、セレブロの部品を手に入れ、自分のセレブロを作るためだった。\n"
         "セレブロを動かせるのはプロフェッサーXだけである。セレブロにつながったプロフェッサーXが、ある人たち、たとえばミュータントだけに強く念じさせられれば、世界中のミュータントを一度に殺せてしまう。\n"
         "マグニートーはローガンに、骨に金属アダマンチウムを入れたのはストライカーだと教える。ミスティークは基地の図面を手に入れていたが、基地がどこにあるのかが分からない。マグニートーは、木の上にいるナイトクローラーを見上げる。",
         "By the campfire",
         "That night they gather around a campfire in the woods, and Magneto explains Stryker's plan. Stryker raided the school to take enough of Cerebro to build one of his own.\n"
         "Only Professor X can operate Cerebro. But if he, linked to every mind on the planet, were forced to concentrate hard enough on one group, such as mutants, he could kill them all at once.\n"
         "Magneto tells Logan that Stryker is the one who put the adamantium on his bones. Mystique has found plans of Stryker's base, but they don't know where it is. Magneto looks up at Nightcrawler, perched in a tree."),
        ("ナイトクローラーの記憶",
         "ジーンはナイトクローラーの心を読む。見えたのは、ローガンの心の中にあったものとよく似た、手術の光景だった。\n"
         "基地の場所はアルカリ湖だった。そこには何もなかったと言うローガンに、ジーンは、地上には何もないが基地は地下にあると答える。",
         "Nightcrawler's memories",
         "Jean reads Nightcrawler's mind. What she sees, an operation, is very much like what she once saw in Logan's.\n"
         "The base is at Alkali Lake. When Logan says there was nothing there, Jean answers that there is nothing on the surface: the base is underground."),
        ("ローガンとジーン",
         "ローガンとジーンが2人きりになる。ジーンは、連れ去られたサイクロップスを心配している。\n"
         "ローガンはジーンにキスをする。ジーンは一度は受け入れるが、すぐに体を離し、自分が愛しているのはサイクロップスだと言って去る。",
         "Logan and Jean",
         "Logan and Jean have a moment alone. Jean is worried about the captured Cyclops.\n"
         "Logan kisses her. She lets him for a moment, then pulls away, tells him it is Cyclops she loves, and leaves."),
        ("ミスティークのいたずら",
         "ナイトクローラーはミスティークに、誰にでも化けられるのに、なぜいつもふつうの人の姿でいないのかとたずねる。ミスティークは、そんなことをしなくてよい世の中であるべきだからだ、という意味の答えを返す。\n"
         "そのあと、ローガンのテントにジーンが入ってきてキスをする。しかしローガンは、相手の体に自分がつけた爪の傷あとがあることに気づく。ジーンに化けたミスティークだった。ミスティークはストームやローグの姿にも次々に変わってみせるが、ローガンは追い出す。",
         "Mystique's trick",
         "Nightcrawler asks Mystique why, if she can look like anyone, she doesn't stay in disguise all the time. She answers, \"Because we shouldn't have to.\"\n"
         "Later, Jean comes into Logan's tent and kisses him. But Logan feels the scars his own claws once left: it is Mystique. \"No one's ever left a scar quite like you,\" she says. She shifts through Storm, Rogue and others, but Logan throws her out."),
        ("少女の幻",
         "基地では、プロフェッサーXがジェイソンの幻の中にいる。気がつくと学園の自分の部屋にいて、自分の足で立っている。幻だと気づいてジェイソンにやめるよう叫ぶが、幻は終わらない。\n"
         "次の幻では、小さな女の子が泣いている。プロフェッサーXは、ほかの生徒たちをセレブロで探そうと言い、女の子を連れてセレブロへ向かう。現実では、この女の子はジェイソンで、2人が入っていくのは、ストライカーが作ったもう一つのセレブロだった。",
         "The little girl",
         "At the base, Professor X is inside Jason's illusions. He finds himself in his study at the school, standing on his own legs. Realizing it isn't real, he shouts at Jason to stop, but the illusions go on.\n"
         "In the next one, a little girl is crying. Professor X says they will find the other students with Cerebro, and takes her there. In reality the girl is Jason, and the room they are entering is the second Cerebro Stryker has built."),
        ("出発の朝",
         "次の朝、一行はジェット機でアルカリ湖へ飛ぶ。X-MENは戦うための服に着がえる。機内でマグニートーは、ローグの髪の白い筋（前の作品で自分がつけたもの）をからかう。ジョンには、人間とは比べものにならない力を持っていることを忘れるなと声をかけ、ジョンの心をつかむ。\n"
         "基地の入り口は、ダムの水を流すための通り道（放水路）にある。中に入ったところでストライカーに水を流されれば終わりである。ナイトクローラーは、見えない場所へは瞬間移動できない。\n"
         "ローガンは、ストライカーは自分を生かしておきたいはずだから自分が行くと言う。しかしマグニートーは、中に入る者は基地の装置を動かせなければならないと言い、ミスティークを見る。",
         "The morning they set out",
         "The next morning they fly to Alkali Lake, and the X-Men suit up. On board, Magneto needles Rogue about the white streak in her hair, which he gave her in the last film. To John he says, \"You are a god among insects. Never let anyone tell you different,\" and wins him over.\n"
         "The way into the base is through the dam's spillway. If Stryker floods it while they are inside, it is over. And Nightcrawler can't teleport to a place he can't see.\n"
         "Logan volunteers, guessing Stryker wants him alive. But Magneto says whoever goes in has to be able to operate the controls, and looks at Mystique."),
    ]),
    ("第4部 アルカリ湖の基地", "Part 4: The base at Alkali Lake", [
        ("ローガンに化けたミスティーク",
         "放水路を、ローガンがひとりで歩いてきて、ストライカーの名前を叫ぶ。それを画面で見たストライカーは、水を流すのを止めさせ、兵士たちに連れてこさせる。\n"
         "基地の中に入ったとたん、ローガンはミスティークの姿に戻り、兵士たちをけり倒して奥へ逃げこむ。そしてストライカーの姿に化けて操作室に入り、中の兵士を倒して扉を閉めきる。\n"
         "ミスティークは、放水路の入り口を開ける。",
         "Mystique as Logan",
         "Logan walks alone down the spillway, shouting Stryker's name. Watching on a monitor, Stryker tells his men not to flood it and has him brought in.\n"
         "The moment they are inside the base, \"Logan\" turns back into Mystique, kicks down the soldiers around her and slips away. Then, disguised as Stryker, she walks into the control room, knocks out the operator and seals the door.\n"
         "She opens the spillway doors."),
        ("それぞれの役目",
         "X-MENとマグニートーが基地に入り、操作室に集まる。ミスティークが基地の図面を出す。大きな丸い部屋が、もう一つのセレブロだった。操作室からは止められない。\n"
         "マグニートーとミスティークがセレブロを止めに行くことになり、ジーンは見張りとして2人について行く。ストームは、画面に映ったさらわれた子どもたちを、ナイトクローラーと助けに行く。ローグ、ボビー、ジョンの3人は、ジェット機で待つように言われている。\n"
         "ローガンは、画面に映るストライカーを見つけ、黙ってひとりで姿を消す。",
         "Splitting up",
         "The X-Men and Magneto enter the base and gather in the control room. Mystique brings up a map: the large round room is the second Cerebro, and it can't be shut down from here.\n"
         "Magneto and Mystique will go and stop it, and Jean goes with them to keep an eye on them. Storm, seeing the kidnapped children on a monitor, sets off with Nightcrawler to free them. Rogue, Bobby and John have been told to wait in the jet.\n"
         "Logan spots Stryker on one of the screens and slips away on his own without a word."),
        ("ストライカーの命令",
         "ストライカーは、兵士たちにセレブロのまわりを守らせ、中に入る。そしてジェイソンの耳もとで、すべてのミュータントを探す時が来たとささやく。\n"
         "幻の中では、女の子がプロフェッサーXに同じことを言う。プロフェッサーXはうなずき、装置を頭にかぶる。\n"
         "外に出たストライカーは兵士に、ここに近づく者は、たとえ自分の姿をしていても撃てと命じる。",
         "Stryker's order",
         "Stryker posts his soldiers around Cerebro and goes inside. He leans down and whispers in Jason's ear that it is time to find all the mutants, everywhere.\n"
         "In the illusion, the little girl says the same thing to Professor X. He agrees and puts on the helmet.\n"
         "Outside, Stryker orders his men to shoot anyone who approaches, even if it looks like him."),
        ("操られたサイクロップス",
         "セレブロへ向かうジーン、マグニートー、ミスティークの前に、薬で操られたサイクロップスが現れ、光線を撃とうとする。ジーンは2人を力で突き飛ばして助け、先に行かせる。\n"
         "ジーンはサイクロップスを下の階へ吹き飛ばし、けがをしていないか心配して追いかける。",
         "Cyclops, under control",
         "On the way to Cerebro, Jean, Magneto and Mystique run into Cyclops, who is under Stryker's drug and about to fire. Jean shoves the other two out of the way with her power and tells them to go on.\n"
         "She hurls Cyclops down to a lower level, then goes after him, worried he is hurt."),
        ("さらわれた子どもたち",
         "ストームとナイトクローラーは、床の格子の下の牢屋に、さらわれた6人の子どもたちを見つける。\n"
         "ナイトクローラーが瞬間移動で中に入る。子どもたちは、急に現れた青い姿におどろいて後ずさりする。",
         "The kidnapped children",
         "Storm and Nightcrawler find the six kidnapped children in a cell beneath a grate in the floor.\n"
         "Nightcrawler teleports in. The children back away, startled by the blue figure who has appeared out of nowhere."),
        ("傷つくダム",
         "下の階で、隠れていたサイクロップスが、ジーンに全力の光線を撃つ。ジーンは力で受け止める。ジーンの目が光り、光線をはじき返す。2人とも吹き飛ばされる。\n"
         "はじかれた光線は基地の壁と機械をこわし、ダムにひびが入る。もうダムがくずれるのは止められない。\n"
         "サイクロップスは正気に戻り、ジーンを抱きしめてあやまる。ジーンは足にけがをしている。",
         "The dam is damaged",
         "On the lower level, Cyclops fires at Jean from hiding at full power. She holds the beam back with her mind; her eyes glow and she repels it. Both are thrown backward.\n"
         "The scattered blast smashes the walls and machinery of the base and cracks the dam. Its collapse can no longer be stopped.\n"
         "Cyclops comes back to himself, holds Jean and apologizes. Her leg is injured."),
        ("ローガンの過去の部屋",
         "ローガンは階段を下り、悪夢で見ていた部屋にたどり着く。壁には骨と爪のエックス線写真。まん中には水そうがあり、そばには溶けたアダマンチウムと太い注射の針がある。\n"
         "ローガンの頭に、昔の記憶が切れ切れによみがえる。ここで骨に金属を入れられ、水そうから飛び出して、はだかのまま逃げたのだった。\n"
         "そこへストライカーとユリコが入ってくる。ストライカーは、アダマンチウムは冷えるとこわせなくなるので、熱く溶かしておかなければならないと話す。そして、おまえのような者は一人だけだと思っていたが違った、と言い残して出ていく。",
         "The room from Logan's past",
         "Logan goes down a stairway and finds the room from his nightmares. X-rays of bones and claws hang on the walls. In the middle is a tank, and beside it a vat of molten adamantium and heavy injection needles.\n"
         "Fragments of memory come back to him. This is where the metal was put on his bones, and where he burst out of the tank and fled, naked.\n"
         "Stryker and Yuriko walk in. Stryker explains that adamantium has to be kept hot and liquid, because once it cools it is indestructible. He used to think Logan was one of a kind, he says as he leaves. He was wrong."),
        ("ユリコとの戦い",
         "追おうとするローガンを、ユリコがはばむ。ユリコの両手の指先から、アダマンチウムの長い爪が伸びる。ユリコはローガンと同じく、傷がすぐに治る体を持っていた。\n"
         "ローガンは何度も刺され、投げ飛ばされる。水そうの上の金網の台に乗せられ、下から刺され続けるが、台をつるす柱を爪で切って、台ごとユリコの上に落とす。それでもユリコは飛び出してきて、また刺す。\n"
         "ローガンは、そばにあった注射の針をつかんでユリコに突き刺し、溶けたアダマンチウムを体の中に流しこむ。金属はユリコの目や鼻からあふれ、体の中で固まる。ユリコは水そうに沈んで死ぬ。",
         "The fight with Yuriko",
         "Logan goes after Stryker, but Yuriko blocks his way. Long adamantium claws slide out of her fingertips. Like Logan, she heals almost instantly.\n"
         "She stabs him again and again and throws him across the room. She tosses him onto a metal grate hanging over the tank and keeps stabbing him from below, until he slices through its supports and drops the whole platform on her. She still bursts out and stabs him again.\n"
         "Logan grabs one of the injection needles, drives it into her and pumps her full of molten adamantium. The metal runs from her eyes and nose and hardens inside her. Yuriko sinks into the tank, dead."),
    ]),
    ("第5部 セレブロをめぐる戦い", "Part 5: The fight over Cerebro", [
        ("ミュータントをねらうセレブロ",
         "ジェット機では、待ちくたびれたジョンが、ローグが止めるのも聞かずに外へ出ていく。\n"
         "幻の中のプロフェッサーXが、世界中のミュータントに強く念じ始める。基地の中のX-MENも、子どもたちも、ローガンも、頭をかかえて倒れる。世界中のミュータントが同じように苦しんでいる。\n"
         "マグニートーは、心の力を通さないヘルメットをかぶってセレブロの前まで進み、力で扉をこじ開ける。セレブロが止まり、ミュータントたちの苦しみが消える。",
         "Cerebro turns on mutants",
         "On the jet, John gets tired of waiting and walks out, ignoring Rogue's protests.\n"
         "Inside the illusion, Professor X begins to concentrate on every mutant in the world. In the base, the X-Men, the children and Logan all clutch their heads and fall. Mutants everywhere are suffering the same way.\n"
         "Magneto, wearing the helmet that shields him from telepathy, reaches Cerebro and forces the doors open with his power. Cerebro stops, and the mutants' pain ends."),
        ("セレブロの向きを変える",
         "しかしマグニートーは、プロフェッサーXを助け出さない。宙に浮かび、部屋の壁の金属の板を次々に動かして、装置を組みかえる。\n"
         "ミスティークがストライカーの姿に化けて中に入り、ジェイソンに計画が変わったと告げて、耳もとでささやく。マグニートーは古い友人に別れを言い、扉を閉めて去る。\n"
         "幻の中の女の子は、プロフェッサーXに、今度は人間を全員探すようにと言う。",
         "Turning Cerebro around",
         "But Magneto doesn't rescue Professor X. He rises into the air and rearranges the metal panels on the chamber walls, reconfiguring the machine.\n"
         "Mystique, disguised as Stryker, walks in and tells Jason there has been a change of plans, whispering in his ear. Magneto says goodbye to his old friend and seals the doors behind them.\n"
         "In the illusion, the little girl tells Professor X that now they must find all the humans."),
        ("ストライカーを追って",
         "ストライカーは外に出て、ヘリコプターで逃げようとしている。そこへローガンが追いつき、なぐりつけて、爪を突き立てる。\n"
         "体を切り開いて人生をうばったと責めるローガンに、ストライカーは、おまえは自分から望んで手術を受けたのだと言う。そして、おまえは昔も今もけだもので、自分は爪を与えただけだと言う。\n"
         "そのとき警報が鳴り、ダムから水がふき出す。ストライカーは、中にいる者はもう助からない、一緒に来れば答えを教えると持ちかける。ローガンは、仲間が死ぬならおまえも死ぬと言い、ストライカーをヘリコプターにつないで、基地の中へ走って戻る。",
         "Chasing Stryker",
         "Stryker is outside, about to escape in his helicopter. Logan catches up, punches him and drives his claws into him.\n"
         "\"You cut me open. You took my life,\" Logan says. Stryker answers that Logan volunteered for the procedure, and that he was an animal then and is an animal now; Stryker only gave him claws.\n"
         "An alarm sounds and water bursts from the dam. Stryker says it is too late for anyone inside, and offers Logan the answers if he comes along. Logan replies that if they die, Stryker dies, ties him to the helicopter and runs back into the base."),
        ("ヘリコプターで去るマグニートー",
         "セレブロの力が、人間に向かい始める。今度は、世界中の人間が頭をかかえて倒れる。ストライカーも、ホワイトハウスの大統領も苦しむ。\n"
         "苦しむストライカーの前に、マグニートーとミスティークがやって来る。マグニートーは、ストライカーを近くのコンクリートの壁に鎖でつなぎ直し、ヘリコプターをうばう。\n"
         "そこへジョンが現れる。ジョンはX-MENを離れ、マグニートーたちと一緒にヘリコプターで去る。",
         "Magneto takes the helicopter",
         "Cerebro's power turns on humans. Now it is the humans, all over the world, who clutch their heads and fall. Stryker is in agony, and so is the President in the White House.\n"
         "Magneto and Mystique walk up to the suffering Stryker. Magneto chains him to a nearby concrete wall instead and takes the helicopter.\n"
         "John appears. He leaves the X-Men behind and flies away with Magneto and Mystique."),
        ("閉ざされた扉の前で",
         "子どもたちを助け出したストームとナイトクローラー、そしてジーンとサイクロップスが、セレブロの扉の前に集まる。ジーンは中の様子を心で探り、マグニートーが向きを変え、今は人間がねらわれていると気づく。\n"
         "サイクロップスが光線で扉をこわそうとするが、ジーンが止める。プロフェッサーXがセレブロにつながったまま扉をこわせば、プロフェッサーXも、心がつながっている人たちも死ぬかもしれない。\n"
         "ストームはナイトクローラーに、中へ連れて行ってほしいと頼む。見えない場所への瞬間移動は危ないが、ストームはあなたを信じていると言う。ジーンは、中で見えるものを信じてはいけないと注意する。",
         "At the sealed doors",
         "Storm and Nightcrawler, with the rescued children, meet Jean and Cyclops at Cerebro's doors. Jean scans the room with her mind and realizes that Magneto has reversed the machine: it is now targeting humans.\n"
         "Cyclops gets ready to blast the doors, but Jean stops him. With Professor X still connected to Cerebro, breaking in could kill him and everyone his mind is linked to.\n"
         "Storm asks Nightcrawler to take her inside. Teleporting somewhere he can't see is dangerous, but she tells him she has faith in him. Jean warns them not to believe anything they see in there."),
        ("セレブロの中の吹雪",
         "ナイトクローラーは祈りながらストームを抱き、2人は部屋の中に現れる。そこにプロフェッサーXの姿はなく、小さな女の子がひとり立っているだけだった。近づこうとするナイトクローラーを、ストームが止める。\n"
         "ストームは目を白く光らせ、部屋の中に強い風と、こごえる寒さを起こす。幻の女の子はやめてと叫ぶ。現実のジェイソンは寒さにたえられず、幻が切れる。\n"
         "プロフェッサーXは正気に戻り、頭の装置を外す。天井がくずれ始め、ナイトクローラーがストームとプロフェッサーXを連れて瞬間移動で外へ出る。ジェイソンは、くずれる部屋に残される。",
         "A snowstorm inside Cerebro",
         "Praying, Nightcrawler holds Storm and the two appear inside the chamber. They don't see Professor X, only a little girl standing alone. Nightcrawler starts toward her, but Storm stops him.\n"
         "Her eyes turn white, and she fills the room with fierce wind and freezing cold. The girl screams at her to stop. The real Jason can't bear the cold, and the illusion breaks.\n"
         "Professor X comes to his senses and takes off the helmet. The ceiling starts to collapse, and Nightcrawler teleports Storm and Professor X out. Jason is left behind in the crumbling chamber."),
        ("基地からの脱出",
         "一行は放水路から逃げようと走る。しかしローガンが現れ、爪で機械をこわして放水路への扉を閉める。その直後、扉のすき間から水がふき出す。ローガンは、別の出口へみんなを連れて行く。\n"
         "雪の上に出ると、ヘリコプターはもうなかった。そこへ、ふらふらと飛ぶジェット機が現れる。操縦しているのはローグで、雪の上にどうにか下りる。みんなが乗りこむ。",
         "Out of the base",
         "The group runs for the spillway. But Logan appears and slams the spillway door shut by stabbing his claws into a fuse box. A moment later, water sprays through the cracks. He leads everyone to another way out.\n"
         "Outside in the snow, the helicopter is already gone. Then the jet appears, lurching through the air. Rogue is at the controls, and she just manages to set it down in the snow. Everyone climbs aboard."),
    ]),
    ("第6部 ダムの決壊", "Part 6: The dam breaks", [
        ("ストライカーとの別れ",
         "ローガンは、男の子アーティを抱いたまま、ジェット機に乗らずに森のほうへ歩く。そこには、コンクリートの壁に鎖でつながれたストライカーがいた。\n"
         "ストライカーは、答えを知っているのは自分だけだと言う。しかしローガンは、仲間たちと生きるほうを選ぶと答え、ストライカーに付けられていた認識票を捨てて背を向ける。\n"
         "ストライカーは、いつか誰かが自分の始めたことをやりとげると叫ぶ。アーティは、ストライカーに向かって舌を出す。",
         "Leaving Stryker behind",
         "Carrying a boy named Artie, Logan walks toward the woods instead of the jet. There he finds Stryker, chained to a concrete wall.\n"
         "Stryker says he is the only one with the answers. But Logan says, \"I'll take my chances with him,\" drops the dog tags Stryker once gave him, and turns his back.\n"
         "\"One day! Someone will finish what I've started!\" Stryker shouts after him. Artie sticks out his tongue at him."),
        ("飛べないジェット機",
         "ローガンがジェット機に乗りこむ。ローグがジョンはどこかとたずね、ジーンが心で探って、マグニートーと一緒にいると答える。\n"
         "ジェット機は力を失っていて、飛び立てない。そのとき、ダムがついにくずれ、大量の水が押し寄せてくる。",
         "The jet won't fly",
         "Logan boards the jet. Rogue asks where John is; Jean searches with her mind and says he is with Magneto.\n"
         "The jet has lost power and can't take off. Then the dam finally gives way, and a wall of water comes rushing toward them."),
        ("ジーンの別れ",
         "ジーンは仲間たちの顔を見てから、誰にも気づかれないようにジェット機を降りる。プロフェッサーXが気づいたときには、ジーンは外から力で扉を閉めていた。\n"
         "ダムとともに、壁につながれたストライカーも水にのまれて死ぬ。ジーンは、片手で押し寄せる水をせき止め、もう片方の手でジェット機を動かして持ち上げる。連れ戻そうとするナイトクローラーの瞬間移動も、ジーンが止めてしまう。\n"
         "ジーンは、プロフェッサーXの口を借りて、こうするしかないと仲間に伝え、サイクロップスに別れを告げる。ジーンの体が炎のような光に包まれる。ジェット機が空へ上がると、ジーンは力をゆるめ、水の中にのみこまれる。サイクロップスは泣きくずれる。",
         "Jean's goodbye",
         "Jean looks at her friends one last time, then slips off the jet without anyone noticing. By the time Professor X realizes, she has sealed the ramp from outside with her power.\n"
         "As the dam goes, Stryker, chained to his wall, is swept away and killed. Jean holds back the flood with one hand and powers up and lifts the jet with the other. When Nightcrawler tries to teleport out to her, she blocks him too.\n"
         "Speaking through Professor X, she tells her friends this is the only way, and says goodbye to Cyclops. Her body is wrapped in a fiery glow. Once the jet is in the air, she lets go, and the water crashes down on her. Cyclops breaks down in tears."),
        ("大統領への言葉",
         "ワシントン。大統領が、ミュータントの危険について国民にテレビで話し始める。そのとき、明かりが消え、部屋の人たちが動きを止める。雷の光の中に、X-MENが立っていた。\n"
         "ローグが、ストライカーの部屋から持ち出した書類を机に置く。大統領の知らないところで、戦争を始めようとした者がいて、人間にもミュータントにも犠牲が出たことが書かれている。\n"
         "プロフェッサーXは、これはおどしではなく、機会だと言う。昔のあやまちをくり返すか、力を合わせてよりよい未来を作るか。次の一手は大統領が決めることだと伝え、X-MENは姿を消す。",
         "A message for the President",
         "Washington. The President begins a televised address about the mutant threat. The lights go out and everyone else in the room freezes. In a flash of lightning, the X-Men are standing before him.\n"
         "Rogue lays files from Stryker's private office on the desk. They show that, without the President's knowledge, someone tried to start a war, and that there were losses on both sides, human and mutant.\n"
         "This is not a threat, Professor X says, but an opportunity: to repeat the mistakes of the past, or to work together for a better future. The next move is the President's. Then the X-Men vanish."),
        ("学園で",
         "学園で、プロフェッサーX、サイクロップス、ローガンがジーンのことを話す。もっと何かできなかったのかとたずねるサイクロップスに、プロフェッサーXは、ジーンは自分で選んだのだと答える。\n"
         "部屋を出るとき、ローガンはサイクロップスに、ジーンが選んだのはおまえだったと伝える。\n"
         "生徒たちが教室に入ってくる。プロフェッサーXは授業を始める。",
         "Back at the school",
         "At the school, Professor X, Cyclops and Logan talk about Jean. Cyclops asks whether they could have done more; Professor X says she made a choice.\n"
         "As they leave the room, Logan tells Cyclops that Jean did make a choice: it was him.\n"
         "Students file into the classroom, and Professor X begins his lesson."),
        ("湖の影",
         "最後に、進化について語るジーンの声が流れる。水の底に沈んだアルカリ湖の水面に、炎の鳥のような形が浮かび上がる。",
         "A shape in the lake",
         "In the final scene, Jean's voice speaks about evolution. On the surface of the flooded Alkali Lake, a shape like a fiery bird appears."),
    ]),
    ("まとめ（最後までのネタバレ）", "Summary (spoilers through the end)", [
        ("ストライカーの計画と結末",
         "①ナイトクローラーを薬で操って大統領を襲わせ、学園を調べる許可を取る（第1部）\n"
         "②マグニートーに薬を使ってセレブロのことを聞き出し、面会に来たプロフェッサーXとサイクロップスをわなにかける（第1部）\n"
         "③学園を襲い、セレブロの部品と6人の生徒をうばう（第2部）\n"
         "④息子ジェイソンの幻でプロフェッサーXを操り、もう一つのセレブロで世界中のミュータントを殺そうとする（第3部〜第5部）\n"
         "⑤マグニートーが止めるが、ねらいを人間に変える。ストームとナイトクローラーがそれも止める（第5部）\n"
         "⑥ストライカーは、くずれたダムの水にのまれて死ぬ（第6部）",
         "Stryker's plan and how it ended",
         "1) He drugs Nightcrawler into attacking the President and wins permission to investigate the school (Part 1).\n"
         "2) He drugs Magneto to learn about Cerebro, and traps Professor X and Cyclops when they come to visit (Part 1).\n"
         "3) He raids the school and takes parts of Cerebro and six students (Part 2).\n"
         "4) Through his son Jason's illusions, he tries to make Professor X kill every mutant with a second Cerebro (Parts 3–5).\n"
         "5) Magneto stops it but turns it on humans; Storm and Nightcrawler stop that too (Part 5).\n"
         "6) Stryker is killed when the dam bursts (Part 6)."),
        ("ローガンの過去",
         "①アルカリ湖を調べるが、何も見つからない（第1部）\n"
         "②学園を襲ったストライカーが、自分を昔から知っていると分かる（第2部）\n"
         "③骨に金属を入れたのがストライカーだと、マグニートーから聞く（第3部）\n"
         "④基地の部屋で、そこで金属を入れられて逃げ出したことを思い出す（第4部）\n"
         "⑤ストライカーから、自分から望んで手術を受けたと言われる。くわしい答えは聞けない（第5部）\n"
         "⑥答えよりも仲間を選び、認識票を捨てる（第6部）",
         "Logan's past",
         "1) He searches Alkali Lake and finds nothing (Part 1).\n"
         "2) He learns that Stryker, who raids the school, has known him for years (Part 2).\n"
         "3) Magneto tells him Stryker put the metal on his bones (Part 3).\n"
         "4) In a room at the base, he remembers the procedure and his escape (Part 4).\n"
         "5) Stryker tells him he volunteered, but gives no real answers (Part 5).\n"
         "6) He chooses his friends over the answers and throws away his dog tags (Part 6)."),
        ("死んだ人たち",
         "・ラウリオ（第2部）：マグニートーの牢屋の看守。ミスティークに鉄を注射され、次の日、マグニートーにその鉄を体から引き出されて死ぬ。\n"
         "・ユリコ（第4部）：薬で操られていたストライカーの秘書。ローガンとの戦いで、溶けたアダマンチウムを体に流しこまれて死ぬ。\n"
         "・ストライカー（第6部）：ローガンにヘリコプターにつながれ、そのあとマグニートーにコンクリートの壁へ鎖でつながれる。ローガンに置いていかれ、くずれたダムの水にのまれて死ぬ。\n"
         "・ジーン（第6部）：仲間の乗ったジェット機を逃がすため、外に出て水をせき止め、そのあと水にのみこまれる。最後に、湖に炎の鳥のような形が浮かぶ。",
         "Who died",
         "- Laurio (Part 2): the guard at Magneto's prison. Mystique injects him with iron, and the next day Magneto rips it out of his body.\n"
         "- Yuriko (Part 4): Stryker's assistant, controlled by his drug. Logan pumps molten adamantium into her during their fight.\n"
         "- Stryker (Part 6): tied to the helicopter by Logan, then chained to a concrete wall by Magneto. Logan leaves him there, and he is swept away when the dam bursts.\n"
         "- Jean (Part 6): she steps outside and holds back the water so her friends' jet can escape, then is swept under. In the last shot, a shape like a fiery bird appears on the lake."),
    ]),
]
