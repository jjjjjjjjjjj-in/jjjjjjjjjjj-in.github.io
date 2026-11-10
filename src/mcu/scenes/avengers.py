# 『アベンジャーズ』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版ウィキペディアのあらすじ（Plot）と登場人物の記事、解説記事で事実を確かめた。資料どうしで食い違う所や、確かめられないせりふ・細かい順番は書いていない。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 奪われた四次元キューブ", "Part 1: The stolen Tesseract", [
        ("宇宙での取引",
         "宇宙のどこか。ロキは、宇宙の軍団チタウリを率いる使いの者（「その他」と呼ばれる）と会っている。\n"
         "約束はこうだ。ロキが地球から四次元キューブ（テッセラクト）を持ってくる。その代わりに、使いの者はロキに地球を支配するための軍団を貸す。ロキの手には、青く光る石がついた杖がある。",
         "A deal in space",
         "Somewhere in space, Loki meets the Other, the messenger who speaks for an alien army called the Chitauri.\n"
         "The deal: Loki will bring them the Tesseract from Earth, and in return the Other will lend him an army to conquer it. Loki holds a scepter with a glowing blue stone."),
        ("研究所の異変",
         "地球。秘密の組織S.H.I.E.L.D.の地下の研究所では、セルヴィグ博士たちが四次元キューブを研究している。そのキューブが、勝手に強い力を出し始める。\n"
         "長官のニック・フューリーがヘリコプターで駆けつける。部下のコールソンとマリア・ヒルもいる。フューリーは、高い場所から見張っていた弓の名手クリント・バートンにも様子を聞く。",
         "Trouble at the lab",
         "On Earth, in an underground S.H.I.E.L.D. research facility, Dr. Selvig's team is studying the Tesseract, and it starts giving off energy on its own.\n"
         "Director Nick Fury arrives by helicopter. Agents Coulson and Maria Hill are there, and Fury also checks in with master archer Clint Barton, who has been watching from up high."),
        ("ロキの登場",
         "キューブが空間に穴を開け、その中からロキが現れる。止めようとした警備の人たちを、ロキは杖で次々に倒す。\n"
         "ロキは杖の先でバートンやセルヴィグ博士の胸に触れ、心を操って自分の手下にする。キューブを持ち去ろうとしたフューリーは、操られたバートンに撃たれるが、防弾のチョッキで助かる。",
         "Loki arrives",
         "The Tesseract opens a hole in space, and Loki steps out of it. He strikes down the guards who try to stop him with his scepter.\n"
         "He touches the scepter to the chests of Barton and Selvig, taking control of their minds. Fury tries to leave with the cube and is shot by the brainwashed Barton, but his vest saves him."),
        ("崩れる基地",
         "ロキと操られた人たちは、キューブを持って車で逃げる。ヒルが追いかけるが、キューブが開いた穴が不安定になり、研究所はまるごと崩れ落ちる。\n"
         "フューリーとヒルは何とか脱出するが、ロキには逃げられてしまう。フューリーは仲間たちに、今この時から戦争が始まったと知らせる。",
         "The base collapses",
         "Loki and his brainwashed followers flee by truck with the cube. Hill gives chase, but the unstable portal brings the whole facility down.\n"
         "Fury and Hill make it out, but Loki is gone. Fury tells his people that as of now, they are at war."),
    ]),
    ("第2部 集められるヒーローたち", "Part 2: Assembling the heroes", [
        ("ロシアのナターシャ",
         "ロシア。ナターシャ・ロマノフは椅子にしばられ、尋問されている。だが実は、つかまったふりをして相手から情報を聞き出す任務の最中だった。\n"
         "コールソンから電話が入り、仲間のバートンが操られたと知らされる。ナターシャはその場の男たちをあっという間に倒し、任務を切り上げる。",
         "Natasha in Russia",
         "In Russia, Natasha Romanoff is tied to a chair and being interrogated. In fact, she's letting them think they've caught her so she can pull information out of them.\n"
         "Coulson calls to tell her that her partner Barton has been taken over. She takes down the men in the room in seconds and cuts the mission short."),
        ("インドのブルース",
         "インドのコルカタ。ブルース・バナーは名前を隠し、貧しい人たちを診る医者として暮らしている。少女に、父親が病気なので来てほしいと頼まれ、ブルースは町はずれの家へついて行く。\n"
         "そこで待っていたのはナターシャだった。キューブはガンマ線という目に見えない光を出していて、ガンマ線にくわしいブルースならキューブを探せる、と協力を頼む。\n"
         "ブルースが急に大声を出すと、ナターシャは思わず銃を向ける。ハルクになることを、誰もが恐れているのだ。ブルースは、ナターシャたちと一緒に行くことを受け入れる。",
         "Bruce in India",
         "In Kolkata, India, Bruce Banner is living under the radar as a doctor treating the poor. A little girl begs him to help her sick father, and he follows her to a house on the edge of town.\n"
         "Natasha is waiting there. The Tesseract gives off gamma radiation, she explains, and Bruce, an expert in it, could track it down.\n"
         "When Bruce suddenly shouts, Natasha pulls a gun on him: everyone is afraid of the Hulk. Bruce agrees to come with her."),
        ("ジムのスティーブ",
         "ニューヨーク。70年の眠りから覚めたスティーブ・ロジャースは、夜のジムで1人、サンドバッグを次々に殴り飛ばしている。戦争の記憶が頭から離れない。\n"
         "フューリーが来て、キューブについての資料を渡し、世界を救うために力を貸してほしいと頼む。",
         "Steve at the gym",
         "In New York, Steve Rogers, awake after 70 years, is alone in a gym at night, punching one bag after another off its chain. He can't shake his memories of the war.\n"
         "Fury arrives with files on the Tesseract and asks him to help save the world."),
        ("スターク・タワーのトニー",
         "トニー・スタークは、ニューヨークに建てた新しいビル「スターク・タワー」を、自分のアーク・リアクターの電気だけで動かせるようにしたところだ。ペッパーと2人でお祝いをしている。\n"
         "そこへコールソンが来て、資料を渡す。中にはキューブの研究と、ハルク、キャプテン・アメリカ、ソー、ロキの情報が入っていた。ペッパーはワシントンへ出かけ、トニーは資料を読みこむ。",
         "Tony at Stark Tower",
         "Tony Stark has just got his new New York skyscraper, Stark Tower, running entirely on his own arc reactor power, and he and Pepper are celebrating.\n"
         "Coulson arrives with a file: the Tesseract research, plus information on the Hulk, Captain America, Thor and Loki. Pepper heads off to Washington, and Tony digs into the files."),
        ("ヘリキャリアへ",
         "コールソンは、スティーブとナターシャを小型の飛行機クインジェットで運ぶ。コールソンはキャプテン・アメリカの大ファンで、昔のカードを集めていると照れながら話す。\n"
         "着いた先は、海の上の巨大な空母。甲板でスティーブはブルースと会う。空母は海から浮かび上がって空を飛び、姿を見えなくする。これがS.H.I.E.L.D.の空飛ぶ基地、ヘリキャリアだった。\n"
         "ブルースは研究室で、世界中のカメラや機械を使ってキューブのガンマ線を探し始める。",
         "To the Helicarrier",
         "Coulson flies Steve and Natasha out on a Quinjet. He's a huge Captain America fan and shyly mentions his collection of vintage trading cards.\n"
         "They land on a giant aircraft carrier at sea, where Steve meets Bruce on the deck. The carrier rises out of the ocean, flies, and turns invisible: it's S.H.I.E.L.D.'s flying base, the Helicarrier.\n"
         "In the lab, Bruce starts searching for the Tesseract's gamma signature using sensors around the world."),
        ("ロキの隠れ家",
         "そのころ、ロキの隠れ家では、操られたセルヴィグ博士が、キューブの力で宇宙への入口を開く機械を作っている。キューブの力を安定させるには、イリジウムという金属が必要だと分かる。\n"
         "ロキは、チタウリの使いの者とも話す。使いの者は、もしキューブを手に入れられなければ、どこへ逃げても苦しめると脅す。",
         "Loki's hideout",
         "Meanwhile, in Loki's hideout, the brainwashed Selvig is building a machine to open a portal to space with the Tesseract. To keep its power stable, he needs a metal called iridium.\n"
         "Loki also speaks with the Other, who warns him that if he fails to deliver the Tesseract, there is nowhere he can hide from their punishment."),
    ]),
    ("第3部 ロキをつかまえる", "Part 3: Capturing Loki", [
        ("シュトゥットガルトのパーティー",
         "ドイツのシュトゥットガルト。ロキはスーツ姿で美術館のパーティーに現れ、主催者の科学者を襲う。目の模様で開く保管庫を破るため、装置で科学者の目を読み取らせる。\n"
         "そのすきに、バートンがその保管庫からイリジウムを盗み出す。",
         "The gala in Stuttgart",
         "In Stuttgart, Germany, Loki shows up at a museum gala in a suit and attacks the scientist hosting it, using a device on his eye to get past an eye-scanning vault.\n"
         "While everyone is distracted, Barton steals the iridium from that vault."),
        ("ひざまずく人々",
         "ロキは外の広場に逃げた人々を、魔法の分身で囲んでひざまずかせる。人は支配されるほうが楽なのだと言い放つ。\n"
         "1人の老人だけが立ち上がり、お前のような者には従わないと逆らう。ロキが老人に光線を放つと、飛びこんできたキャプテン・アメリカが盾で防ぐ。\n"
         "ナターシャの乗るクインジェットが空から銃を向け、アイアンマンも到着する。囲まれたロキは、あっさりと降参する。",
         "The kneeling crowd",
         "Outside, Loki surrounds the fleeing crowd with copies of himself and forces them to kneel, telling them people are happier being ruled.\n"
         "One old man stands up and refuses to kneel to men like him. Loki fires at him, and Captain America leaps in and blocks the blast with his shield.\n"
         "Natasha's Quinjet takes aim from above and Iron Man arrives. Surrounded, Loki surrenders without much of a fight."),
        ("嵐の中のソー",
         "ロキを運ぶクインジェットの外で、急に雷が鳴り出す。ロキはおびえたような顔をする。\n"
         "飛行機の屋根に何者かが降り立ち、ロキをつかんで飛び去る。兄のソーだった。ソーは山の上でロキに、地球を攻める計画をやめてアスガルドへ帰ろうと説得するが、ロキは聞き入れない。",
         "Thor in the storm",
         "Outside the Quinjet carrying Loki, thunder suddenly booms, and Loki looks uneasy.\n"
         "Someone lands on the plane, grabs Loki and flies off: it's his brother Thor. On a mountaintop, Thor urges Loki to give up his plan and come home to Asgard, but Loki won't listen."),
        ("森の戦い",
         "トニーがソーに体当たりし、2人は森の中で激しく戦う。トニーは、ロキを渡すつもりはない。ソーは、弟は自分がアスガルドで裁くと言ってゆずらない。\n"
         "スティーブが止めに入るが、ソーは聞かずにハンマーを振り下ろす。ハンマーがスティーブの盾にぶつかり、まわりの木がなぎ倒されるほどの衝撃が起きる。3人は戦いをやめ、ロキをヘリキャリアへ連れて行く。",
         "The fight in the forest",
         "Tony slams into Thor, and the two fight fiercely in the forest. Tony won't hand Loki over; Thor insists that he will deal with his brother in Asgard.\n"
         "Steve steps in, but Thor brings his hammer down anyway. It strikes Steve's shield, and the shockwave flattens the trees around them. The three stop fighting and take Loki to the Helicarrier."),
        ("ガラスの牢屋",
         "ロキは、ヘリキャリアの中のガラスの牢屋に入れられる。もともとはハルクを閉じこめるために作られたものだ。\n"
         "フューリーは、ボタン1つで床が開き、牢屋ごと空から落とせることをロキに見せつける。",
         "The glass cell",
         "Loki is locked in a glass cell aboard the Helicarrier, one originally built to hold the Hulk.\n"
         "Fury shows Loki that, at the push of a button, the floor opens and the cell drops out of the sky."),
        ("研究室のトニーとブルース",
         "トニーとブルースは、研究室でキューブを探す。トニーはブルースを小さな電気の棒でつついてハルクになるか試し、スティーブを怒らせる。\n"
         "トニーは、空母の操縦室に来たときにこっそり小さな装置を仕掛け、S.H.I.E.L.D.のコンピューターから秘密を調べていた。S.H.I.E.L.D.が何かを隠していると考えたスティーブは、自分の目で倉庫を調べに行く。",
         "Tony and Bruce in the lab",
         "In the lab, Tony and Bruce hunt for the Tesseract. Tony pokes Bruce with a small electric prod to see if he'll turn into the Hulk, which angers Steve.\n"
         "When he was on the bridge, Tony secretly planted a small device to hack S.H.I.E.L.D.'s computers. Steve, suspecting S.H.I.E.L.D. is hiding something, goes to search the storage decks himself."),
        ("ナターシャとロキ",
         "ナターシャは牢屋のロキを訪ね、操られたバートンのことを聞く。ロキはナターシャが昔スパイとしてしてきたことを持ち出し、ひどい言葉で脅す。\n"
         "ナターシャは泣き崩れたように見せて、ロキが思わず口にした言葉を聞き逃さなかった。ロキの狙いは、ブルースをハルクに変えて空母の中で暴れさせることだった。",
         "Natasha and Loki",
         "Natasha visits Loki's cell and asks about Barton. Loki throws her past as a spy in her face and threatens her cruelly.\n"
         "She seems to break down in tears, but she is listening, and Loki gives away his plan: to turn Bruce into the Hulk and let him loose inside the carrier."),
    ]),
    ("第4部 ヘリキャリアの危機", "Part 4: The Helicarrier in danger", [
        ("ばらばらのチーム",
         "スティーブは倉庫で、キューブの力を使った兵器を見つける。トニーの装置でも、同じ秘密が明らかになる。S.H.I.E.L.D.は、宇宙からの敵にそなえて、キューブで強力な兵器を作ろうとしていた。\n"
         "研究室に全員が集まり、言い争いになる。フューリーは、ソーたちが地球に来たことで、地球より強い者が宇宙にいると分かったからだと説明する。ソーは、キューブがあるせいで地球がねらわれるのだと言い返す。\n"
         "部屋に置かれたロキの杖の影響もあって、言い争いはどんどん激しくなる。思わず杖を手にしたブルースのコンピューターが、そのときキューブの場所を見つける。",
         "A team at odds",
         "In storage, Steve finds weapons built with the Tesseract's power, and Tony's hack turns up the same secret: S.H.I.E.L.D. planned to use the cube to make weapons against threats from space.\n"
         "Everyone gathers in the lab and argues. Fury says Thor's arrival proved there are beings out there far stronger than Earth; Thor answers that the cube is exactly why Earth is being targeted.\n"
         "With Loki's scepter in the room, the argument grows uglier. Bruce, who has picked up the scepter without thinking, has his computer find the Tesseract just then."),
        ("ハルクが暴れる",
         "その瞬間、操られたバートンたちの飛行機がヘリキャリアを攻撃し、空母のエンジンの1つが爆発で壊れる。研究室にいたブルースとナターシャは、下の階へ落ちる。\n"
         "痛みと怒りで、ブルースはハルクに変わってしまう。ハルクはナターシャを追いかけ、駆けつけたソーと激しく戦う。最後に、ハルクは自分を撃ってきた戦闘機に飛び乗り、そのまま地上へ落ちていく。",
         "The Hulk breaks loose",
         "At that moment, Barton and other brainwashed agents attack the Helicarrier by air, and an explosion knocks out one of the carrier's engines. Bruce and Natasha fall through to the deck below.\n"
         "In pain and anger, Bruce turns into the Hulk. He chases Natasha, then fights Thor. Finally he leaps onto a fighter jet that's firing at him and falls with it to the ground."),
        ("エンジンを直す",
         "エンジンが1つ止まり、ヘリキャリアは傾いて落ち始める。トニーはアイアンマンのスーツで壊れたエンジンの外に出て、止まった羽根を自分の体で押して回す。\n"
         "スティーブは外側の足場でレバーを引き、トニーを助ける。敵に撃たれながらも、2人はエンジンを動かし、空母の墜落を防ぐ。",
         "Fixing the engine",
         "With one engine dead, the Helicarrier starts to tilt and fall. Tony goes outside in the Iron Man suit and pushes the stalled rotor around with his own body.\n"
         "Steve, out on the catwalks, pulls the lever Tony needs while dodging enemy fire. Together they get the engine running and keep the carrier in the air."),
        ("ナターシャとバートン",
         "バートンは空母の中に乗りこみ、矢で操縦室や設備をねらう。ナターシャはバートンと1対1で戦い、頭を強く打ちつけて気絶させる。\n"
         "目を覚ましたバートンは、ロキの支配から解けて元に戻っていた。",
         "Natasha vs. Barton",
         "Barton gets aboard and targets the bridge and the ship's systems with his arrows. Natasha fights him one-on-one and knocks him out with a hard blow to the head.\n"
         "When he comes to, he is free of Loki's control."),
        ("ソーの落下",
         "ロキは、ソーをだまして牢屋の中へ入らせ、閉じこめる。ロキが自分の分身を使っていたのだ。\n"
         "ロキはボタンを押し、ソーの入った牢屋を空から落とす。ソーは、地面に落ちる前に牢屋を破って抜け出す。",
         "Thor falls",
         "Loki tricks Thor into stepping into the cell using a copy of himself, and locks him in.\n"
         "Loki hits the button and drops the cell, with Thor inside, out of the sky. Thor breaks out before it hits the ground."),
        ("コールソンの死",
         "コールソンは、アスガルドの兵器デストロイヤーの部品から作られた大きな銃を持って、ロキの前に立つ。だがそれもロキの分身で、本物のロキはコールソンの後ろから杖で胸を刺す。\n"
         "倒れたコールソンは、それでもロキに、お前は負けると言い、銃を撃ってロキを壁の向こうまで吹き飛ばす。ロキは手下と一緒に空母から逃げる。\n"
         "駆けつけたフューリーに見守られながら、コールソンは息を引き取る。",
         "Coulson's death",
         "Coulson faces Loki with a big gun built from parts of the Asgardian Destroyer. But that Loki is a copy too, and the real Loki stabs Coulson through the chest from behind with the scepter.\n"
         "Down but not done, Coulson tells Loki he's going to lose, then fires and blasts Loki through a wall. Loki escapes the carrier with his followers.\n"
         "Coulson dies with Fury at his side."),
        ("戦う理由",
         "フューリーは、トニーとスティーブにコールソンの死を伝え、血のついたキャプテン・アメリカのカードを投げて見せる。コールソンが、スティーブにサインをもらいたがっていたカードだ。フューリーは、ヒーローたちが一つにまとまるきっかけが必要だったと語る。\n"
         "あとでヒルが、カードはロッカーにあったはずではと聞くと、フューリーは、彼らには一押しが必要だったと答える。\n"
         "そのころ、ブルースは空母から落ちた先の倉庫で、元の姿で目を覚ましていた。",
         "A reason to fight",
         "Fury tells Tony and Steve that Coulson is dead and tosses them the Captain America cards, stained with blood, that Coulson had wanted Steve to sign. Fury says the heroes needed something to bring them together.\n"
         "Later, when Hill points out that the cards were in Coulson's locker, Fury says they needed the push.\n"
         "Meanwhile, Bruce wakes up, human again, in the warehouse where he fell."),
    ]),
    ("第5部 ニューヨークの戦い", "Part 5: The Battle of New York", [
        ("ロキの狙い",
         "トニーは、ロキがみんなの前で目立ち、勝つところを見せつけたがっていることに気づく。セルヴィグの機械を動かせるほどの電気がある場所、スターク・タワーだ。\n"
         "トニーは傷ついたスーツで先に向かう。正気に戻ったバートン、ナターシャ、スティーブもクインジェットで後を追う。",
         "Loki's target",
         "Tony realizes Loki wants an audience: he wants to win where everyone can see. And Selvig's machine needs huge power, the kind Stark Tower has.\n"
         "Tony heads there first in his damaged suit. Barton, now himself again, Natasha and Steve follow in a Quinjet."),
        ("トニーとロキ",
         "スターク・タワーの屋上では、セルヴィグの機械が四次元キューブで動き始めていた。トニーはスーツを脱いで中に入り、ロキに酒をすすめながら話す。\n"
         "ロキは杖の先でトニーの胸に触れて操ろうとするが、胸のアーク・リアクターにはばまれて効かない。怒ったロキは、トニーを窓から投げ落とす。\n"
         "落ちていくトニーに、新しいアイアンマンのスーツが飛んできて体を包み、トニーは空中で助かる。",
         "Tony and Loki",
         "On the roof of Stark Tower, Selvig's machine is already being powered by the Tesseract. Tony takes off his suit, walks in and offers Loki a drink as they talk.\n"
         "Loki touches his scepter to Tony's chest to control him, but the arc reactor blocks it. Furious, Loki throws Tony out the window.\n"
         "As Tony falls, a new Iron Man suit flies out and wraps around him in midair."),
        ("空に開いた穴",
         "キューブの機械から光が空へ伸び、空に大きな穴が開く。そこからチタウリの兵士と乗り物が次々とニューヨークの街に入ってくる。\n"
         "ソーはタワーの屋上に降り、ロキと戦いながら説得するが、ロキは短い刃でソーを刺し、チタウリの乗り物で街へ飛び出す。キューブの機械は見えない壁に守られ、ソーのハンマーでも止められない。",
         "A hole in the sky",
         "A beam from the machine shoots into the sky and tears open a huge portal. Chitauri soldiers and flying craft pour into New York.\n"
         "Thor lands on the roof and fights Loki while trying to reason with him, but Loki stabs him with a small blade and flies off into the city on a Chitauri craft. The machine is protected by a barrier that even Thor's hammer can't break."),
        ("6人がそろう",
         "スティーブたちのクインジェットは撃たれて街に落ちる。スティーブは警察に、人々を逃がす範囲を指示する。\n"
         "そこへブルースがバイクでやって来る。空の穴からは、くじらのように大きな空飛ぶ生き物が現れる。スティーブが今こそ怒るときだと言うと、ブルースは、自分の秘密はいつも怒っていることだと明かし、その場でハルクに変わり、大きな生き物を一発で殴り止める。\n"
         "キャプテン・アメリカ、アイアンマン、ソー、ハルク、ブラック・ウィドウ、ホークアイの6人が、初めて背中合わせにそろう。",
         "All six together",
         "Steve's Quinjet is shot down in the streets. Steve tells the police how far to clear people out.\n"
         "Bruce arrives on a motorbike as a gigantic flying creature, like a whale, comes through the portal. When Steve says now might be a really good time to get angry, Bruce says his secret is that he's always angry, turns into the Hulk on the spot, and stops the creature with one punch.\n"
         "Captain America, Iron Man, Thor, the Hulk, Black Widow and Hawkeye stand back to back together for the first time."),
        ("キャプテンの作戦",
         "スティーブが作戦を指示する。バートンはビルの屋上から敵の動きを見張って矢を放ち、トニーは空の敵を引きつけ、ソーは雷で穴から入ってくる敵を食い止める。ハルクには、暴れろと一言いうだけでよかった。\n"
         "スティーブとナターシャは地上で人々を守る。ナターシャは、穴を閉じるにはタワーの上へ行くしかないと考え、スティーブの盾を足場に、飛んでいるチタウリの乗り物に飛び乗る。",
         "Captain America's plan",
         "Steve gives orders: Barton watches from a rooftop and picks off enemies with his arrows, Tony draws off the enemies in the sky, Thor uses lightning to hold back those coming through the portal, and the Hulk is simply told to smash.\n"
         "Steve and Natasha protect people on the ground. Natasha decides the only way to close the portal is to get to the top of the tower, and she uses Steve's shield as a springboard to leap onto a passing Chitauri craft."),
        ("ハルク対ロキ",
         "ロキはスターク・タワーの中に戻り、追ってきたハルクに、自分は神だと叫ぶ。\n"
         "ハルクはロキの足をつかみ、床に何度もたたきつける。動けなくなったロキを、ちっぽけな神だとばかにして去っていく。\n"
         "タワーの屋上に着いたナターシャは、ロキの支配から解けたセルヴィグ博士から、ロキの杖を使えば機械を止められると教わる。",
         "Hulk vs. Loki",
         "Loki retreats into Stark Tower and shouts at the pursuing Hulk that he is a god.\n"
         "The Hulk grabs Loki by the legs, slams him into the floor over and over, and walks away from the stunned god with a parting insult.\n"
         "On the roof, Natasha finds Selvig, freed from Loki's control, who tells her Loki's scepter can shut down the machine."),
        ("核ミサイル",
         "フューリーの上に立つ世界安全保障理事会は、敵を街ごと消すため、ニューヨークに核ミサイルを撃ちこむと決める。フューリーは反対し、飛び立とうとした1機をロケット弾で止めるが、別の1機がミサイルを撃ってしまう。\n"
         "トニーはミサイルを背中で押し上げ、空の穴へ向かって飛ぶ。2度と戻れないかもしれないと思い、ペッパーに電話をかけるが、つながらない。\n"
         "トニーは穴の向こうの宇宙へ抜け、チタウリの大きな母船へミサイルを放つ。母船が爆発すると、地上のチタウリの兵士たちも一斉に動かなくなる。",
         "The nuke",
         "The World Security Council, Fury's superiors, decides to fire a nuclear missile at New York to wipe out the enemy along with the city. Fury refuses and stops one jet with a rocket launcher, but another one launches the missile.\n"
         "Tony catches the missile and pushes it up toward the portal. Thinking he may not come back, he tries to call Pepper, but the call doesn't go through.\n"
         "Tony flies through into space and lets the missile go at the Chitauri mothership. When it explodes, the Chitauri on Earth all drop at once."),
        ("落ちてくるトニー",
         "スーツの力が尽き、トニーは気を失ったまま穴から落ちてくる。ナターシャはロキの杖で機械を止め、穴を閉じる。\n"
         "落ちてくるトニーを、ハルクが空中で受け止める。ぴくりとも動かないトニーにハルクが大声でほえると、トニーは目を覚ます。トニーは、みんなでシャワルマ（中東の料理）を食べに行こうと言い出す。",
         "Tony falls",
         "His suit out of power, Tony falls back through the portal unconscious, just as Natasha uses Loki's scepter to shut down the machine and close the portal.\n"
         "The Hulk catches Tony in midair. Tony isn't moving, but when the Hulk roars at him, he wakes up and suggests they all go get shawarma."),
    ]),
    ("第6部 戦いのあと", "Part 6: After the battle", [
        ("ロキの最後",
         "床にめりこんだロキが起き上がると、6人のヒーローが武器を向けてまわりに立っていた。\n"
         "ロキは、前にトニーにすすめられた酒についてやはり一杯もらおうと言うしかなかった。",
         "Loki's last stand",
         "Loki crawls out of the floor to find all six heroes standing over him, weapons ready.\n"
         "All he can say is that he'll take that drink after all."),
        ("それぞれの道",
         "ニューヨークの公園で、ソーは口をふさがれ手錠をかけられたロキと、四次元キューブを持ってアスガルドへ帰る。ロキは、アスガルドで罪を裁かれることになる。\n"
         "ヒーローたちは別々の道へ。トニーとブルースは一緒に車で去り、スティーブはバイクで、ナターシャとバートンも車で去っていく。\n"
         "理事会は勝手にロキとキューブを渡したフューリーを責めるが、フューリーは、必要なときにはヒーローたちがまた集まると信じている。",
         "Separate ways",
         "In a New York park, Thor takes the muzzled, handcuffed Loki and the Tesseract back to Asgard, where Loki will face judgment.\n"
         "The heroes go their own ways: Tony and Bruce drive off together, Steve leaves on his motorbike, and Natasha and Barton drive away.\n"
         "The Council criticizes Fury for letting Loki and the cube go, but Fury is sure the heroes will come back when they're needed."),
        ("エンドクレジットの途中",
         "チタウリを送りこんだ使いの者が、背後の主人に地球での失敗を報告する。地球の人間に挑むのは、死を招くことだと。\n"
         "振り返って笑みを浮かべたのは、サノスだった。",
         "Mid-credits",
         "The Other reports the failure on Earth to his master, warning that challenging the humans means courting death.\n"
         "The master turns and smiles: it is Thanos."),
        ("エンドクレジットの後",
         "戦いを終えて疲れきったヒーローたちが、壊れたシャワルマの店で、黙々と食事をしている。",
         "After the credits",
         "The exhausted heroes sit in a wrecked shawarma restaurant, eating in silence."),
    ]),
    ("まとめ（結末までのネタバレ）", "Summary (spoilers through the ending)", [
        ("ロキの計画と結末",
         "ロキは、チタウリの使いの者から地球を支配する軍団を借りる代わりに、四次元キューブを渡す約束をした（第1部）。\n"
         "キューブを奪い、杖でバートンやセルヴィグ博士を操った（第1部）。わざとつかまってヘリキャリアに入り、ハルクを暴れさせてチームを中からこわそうとした（第3部〜第4部）。\n"
         "最後はスターク・タワーから空に穴を開けてチタウリを呼びこむが、6人のヒーローに敗れ、ソーにアスガルドへ連れ帰られる（第5部〜第6部）。",
         "Loki's plan and how it ends",
         "Loki agreed to hand the Tesseract to the Other in exchange for an army to conquer Earth (Part 1).\n"
         "He stole the cube and used the scepter to control Barton and Selvig (Part 1). He let himself be captured to get aboard the Helicarrier and tried to break the team apart from the inside by unleashing the Hulk (Parts 3–4).\n"
         "In the end he opened the portal from Stark Tower and brought in the Chitauri, but the six heroes beat him, and Thor took him back to Asgard (Parts 5–6)."),
        ("操られた人たちが戻るまで",
         "・クリント・バートン：第1部でロキの杖に操られ、イリジウムを盗み、ヘリキャリアを襲った。第4部でナターシャに頭を打たれて気絶し、元に戻る。第5部ではヒーローの1人として戦う。\n"
         "・セルヴィグ博士：第1部で操られ、キューブで穴を開ける機械を作った。第5部で支配が解け、ナターシャに杖で機械を止める方法を教える。",
         "The people Loki controlled",
         "- Clint Barton: taken over by the scepter in Part 1; he stole the iridium and attacked the Helicarrier. In Part 4, Natasha knocks him out and he returns to himself. In Part 5 he fights as one of the heroes.\n"
         "- Dr. Selvig: taken over in Part 1; he built the machine that opens the portal. In Part 5 he is free again and tells Natasha the scepter can shut it down."),
        ("死んだ人たち（話の順に）",
         "・研究所の警備の人たち（第1部）：現れたロキを止めようとして、ロキに杖で倒される。\n"
         "・フィル・コールソン（第4部）：ヘリキャリアから逃げようとするロキを止めようとした。ロキが分身でだまし、後ろから杖で胸を刺した。フューリーはコールソンの死を、ヒーローたちが一つになるきっかけにする。",
         "Who died (in order)",
         "- Guards at the research facility (Part 1): struck down by Loki's scepter when they tried to stop him.\n"
         "- Phil Coulson (Part 4): he tried to stop Loki from escaping the Helicarrier. Loki fooled him with a copy of himself and stabbed him through the chest from behind with the scepter. Fury uses Coulson's death to bring the heroes together."),
    ]),
]
