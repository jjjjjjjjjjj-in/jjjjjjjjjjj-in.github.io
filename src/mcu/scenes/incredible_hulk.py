# 『インクレディブル・ハルク』（2008年）シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディア（作品と登場人物の記事）と、検索で見つかった解説記事で事実を確かめた。
# 資料どうしで食い違う所や、確かめられない細かい所（変身しなかった日数の数字、リオでやられた兵士の人数、
# スターンズの実験で変身を起こした方法、ハーレムの戦いでのヘリコプターの細かい動きなど）は書いていない。
# 日本語版のせりふは、日本語の吹替・字幕の言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 人物名は相関図（relations.py）にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 事故（オープニング）", "Part 1: The accident (opening)", [
        ("カルバー大学の実験",
         "映画は、出演者の名前が流れる短い映像から始まる。バージニア州のカルバー大学。科学者ブルース・バナーは、恋人で同じ研究者のベティと一緒に、ベティの父ロス将軍に頼まれた実験をしていた。表向きは、人の体を放射線（ガンマ線）に強くするための実験だった。\n"
         "実はこれは、第二次世界大戦のころの「超人兵士」の研究を、ロスがもう一度よみがえらせようとしたものだった。",
         "The experiment at Culver University",
         "The film opens with a short montage under the credits. At Culver University in Virginia, scientist Bruce Banner is working with his girlfriend and colleague Betty on an experiment for her father, General Ross. Officially, it's meant to make people resistant to gamma radiation.\n"
         "In truth, it's Ross's attempt to revive a World War II-era \"super soldier\" program."),
        ("ハルクの誕生",
         "ブルースは自分の体で試し、ガンマ線を浴びる。しかし実験は失敗し、ブルースは緑色の大きな怪物（ハルク）に変わってしまう。それからは、怒ったり心臓の鼓動が速くなりすぎたりすると、ハルクに変わる体になった。\n"
         "ハルクは研究室をこわし、ベティとロス将軍、まわりの人たちにけがをさせる。",
         "The Hulk is born",
         "Bruce tests it on himself and is exposed to gamma radiation. The experiment fails, and he turns into a huge green monster, the Hulk. From then on, anger or a racing heart can set off the change.\n"
         "The Hulk wrecks the lab and injures Betty, General Ross and others nearby."),
        ("逃亡の始まり",
         "ブルースはその場から逃げ、軍に追われる身になる。ロス将軍は、ハルクの力を兵器にしようと、ブルースを捕まえることに力をそそぐ。映像には、ブルースの行方を追う軍の書類やニュースが次々に映る。",
         "On the run",
         "Bruce flees and becomes a fugitive. General Ross, who wants to turn the Hulk's power into a weapon, devotes himself to catching him. The montage flashes through military files and news reports tracking Bruce."),
    ]),
    ("第2部 ブラジルでの隠れ暮らし", "Part 2: Hiding in Brazil", [
        ("リオの町ホッシーニャ",
         "それから時がたち、ブラジルのリオデジャネイロ。丘の斜面に家がぎっしり並ぶ町ホッシーニャで、ブルースはひっそりと暮らしている。もう何か月もハルクに変わっていない。\n"
         "腕には心拍計をつけ、心臓の鼓動が速くなりすぎないよう、いつも気をつけている。",
         "Rocinha, Rio",
         "Time has passed. In Rocinha, a hillside neighborhood packed with houses in Rio de Janeiro, Bruce lives quietly in hiding. He hasn't transformed in months.\n"
         "He wears a heart-rate monitor on his wrist and is always careful not to let his pulse climb too high."),
        ("呼吸の練習",
         "ブルースは武道の先生のもとに通い、呼吸で気持ちをしずめる方法を習っている。怒りをおさえることが、ハルクにならないための一番の方法だからだ。",
         "Breathing lessons",
         "Bruce trains with a martial arts teacher, learning to calm himself through breathing. Controlling his anger is his best defense against becoming the Hulk."),
        ("ミスター・ブルーとのやりとり",
         "ブルースは、インターネットで「ミスター・ブルー」と名乗る科学者と、正体を隠したまま連絡を取り合っている。ブルースのほうは「ミスター・グリーン」と名乗っている。\n"
         "2人は、ブルースの体を元に戻す方法を一緒に探している。ブルースは自分の血をミスター・ブルーに送っていたが、治療はうまくいっていない。ミスター・ブルーは、最初の実験のくわしいデータがほしいと言う。",
         "Messages with Mr. Blue",
         "Online, Bruce trades messages with a scientist who calls himself \"Mr. Blue,\" without either revealing who they are. Bruce goes by \"Mr. Green.\"\n"
         "Together they're searching for a cure. Bruce has been sending Mr. Blue samples of his blood, but nothing has worked yet. Mr. Blue says he needs the detailed data from the original experiment."),
        ("飲み物の工場",
         "ブルースは、飲み物を瓶につめる工場で働いている。同じ職場の女性マルティナは親切にしてくれるが、男たちのグループは、ポルトガル語がうまく話せないブルースにいやがらせをする。",
         "The bottling plant",
         "Bruce works at a soda bottling plant. His coworker Martina is kind to him, but a gang of men there harass him because he can't speak Portuguese well."),
        ("一滴の血",
         "ある日、ブルースは工場で指を切ってしまう。血は機械の上に落ち、ブルースは急いでふき取るが、一滴だけが瓶に入ってしまう。\n"
         "その飲み物はアメリカへ運ばれ、ウィスコンシン州ミルウォーキーに住むおじいさんが飲んで、ガンマ線による病気になる。",
         "One drop of blood",
         "One day Bruce cuts his finger at the plant. He hurries to clean up the blood, but a single drop falls into a bottle.\n"
         "The soda is shipped to the U.S., where an elderly man in Milwaukee, Wisconsin, drinks it and comes down with gamma sickness."),
        ("ロス将軍が気づく",
         "ペンタゴン（アメリカ国防総省）で、ロス将軍はこの病気の知らせを受け、瓶をたどってブラジルの工場をつきとめる。ブルースがそこにいると知ったロスは、すぐに部隊を送ることにする。",
         "Ross finds him",
         "At the Pentagon, General Ross hears about the case and traces the bottle back to the factory in Brazil. Knowing Bruce is there, he moves to send in a team."),
    ]),
    ("第3部 リオの追跡", "Part 3: The chase in Rio", [
        ("ブロンスキーの部隊",
         "フロリダの軍の基地で、精鋭の兵士たちが集められる。中心は、ロシア生まれでイギリスの海兵隊員のエミル・ブロンスキーだ。腕は確かだが、もう若くはない。\n"
         "ロス将軍は、相手が何者かをくわしく話さないまま、ブロンスキーたちをブラジルへ送る。",
         "Blonsky's team",
         "At a military base in Florida, an elite team is assembled. At its center is Emil Blonsky, a Russian-born British Royal Marine, highly skilled but no longer young.\n"
         "Without telling them exactly what they're facing, General Ross sends Blonsky's team to Brazil."),
        ("夜の家に部隊が来る",
         "夜、部隊はブルースの住む家をかこむ。気づいたブルースは窓から逃げ出し、屋根から屋根へと走って逃げる。兵士たちは町の中を追いかける。",
         "The raid at night",
         "At night, the team surrounds Bruce's home. He notices, slips out a window and runs across the rooftops while the soldiers chase him through the neighborhood."),
        ("工場に追いつめられる",
         "ブルースは工場に逃げこむが、そこで、いつもいやがらせをしてきた男たちにも見つかって殴られる。兵士たちも工場に入ってきて、ブルースの心拍はどんどん上がっていく。",
         "Cornered in the factory",
         "Bruce hides in the factory, but the men who always harass him find him there and beat him. The soldiers close in, and his heart rate keeps rising."),
        ("ハルクに変わる",
         "とうとうブルースはハルクに変わる。暗い工場の中で、ハルクは男たちや兵士たちを次々に投げ飛ばし、部隊はほとんど歯が立たない。\n"
         "ブロンスキーだけは生き残り、ハルクが壁をこわして逃げていく姿を見る。ブロンスキーは、自分の力ではかなわなかったこの怪物に強い興味を持つ。",
         "The Hulk emerges",
         "At last Bruce turns into the Hulk. In the dark factory he hurls the men and the soldiers aside, and the team is helpless against him.\n"
         "Blonsky survives and watches the Hulk smash through a wall and escape. He becomes fascinated by the creature he couldn't beat."),
        ("中米で目を覚ます",
         "元に戻ったブルースは、グアテマラの森の中で目を覚ます。服はぼろぼろだ。ブルースは通りかかったトラックに乗せてもらい、メキシコの市場でわずかなお金をもらって新しい服を買う。\n"
         "ブルースは、最初の実験のデータを取りにアメリカへ戻ることにする。",
         "Waking up in Central America",
         "Back to normal, Bruce wakes up in the jungle in Guatemala, his clothes in tatters. He hitches a ride on a passing truck, and in a market in Mexico he is given a little money and buys new clothes.\n"
         "He decides to head back to the U.S. for the data from the original experiment."),
    ]),
    ("第4部 カルバー大学への帰り道", "Part 4: Back to Culver", [
        ("ロスが明かす秘密",
         "ロス将軍はブロンスキーに、あの怪物がブルースであり、超人兵士の研究の失敗から生まれたことを話す。\n"
         "もっと若く強い体で戦いたいと望んでいたブロンスキーは、研究から作られた薬を打たれることを受け入れる。",
         "Ross reveals the secret",
         "General Ross tells Blonsky that the monster is Bruce, the product of a failed super-soldier experiment.\n"
         "Blonsky, who wishes he could fight with a younger, stronger body, agrees to be injected with a serum derived from that research."),
        ("強くなったブロンスキー",
         "薬を打たれたブロンスキーは、ふつうの兵士よりもずっと速く、強く、身軽に動けるようになる。",
         "Blonsky enhanced",
         "The serum makes Blonsky far faster, stronger and more agile than any ordinary soldier."),
        ("ピザ屋のスタンリー",
         "ブルースはバージニア州のカルバー大学の町に戻る。昔からブルースとベティを知るピザ屋の主人スタンリーが、ブルースをこっそり店に置いてくれる。",
         "Stanley's pizzeria",
         "Bruce returns to the town around Culver University. Stanley, a pizzeria owner who has known Bruce and Betty for years, quietly lets Bruce stay at his place."),
        ("研究室に忍びこむ",
         "ブルースは、大学の警備員にピザを渡して見のがしてもらい、建物に入る。学生にパソコンを借りて昔の研究データを探すが、データはもう消されていた。",
         "Sneaking into the lab",
         "Bruce bribes a campus security guard with a pizza to get into the building. He borrows a student's computer to look for his old research, but the data has been erased."),
        ("ベティとの再会",
         "ベティは、心理学者のレナード・サムソンという新しい恋人と、スタンリーの店にやって来る。ベティは店を出ていくブルースに気づき、雨の中を追いかける。2人は5年ぶりに顔を合わせる。\n"
         "ブルースが生きていたことを知ったベティは喜び、ブルースを自分の家に泊める。",
         "Reunited with Betty",
         "Betty comes to Stanley's restaurant with her new boyfriend, psychiatrist Leonard Samson. She spots Bruce leaving and runs after him in the rain. They see each other for the first time in five years.\n"
         "Overjoyed that he's alive, Betty takes him to stay at her house."),
        ("ベティが持っていたデータ",
         "ベティは、ブルースの研究の記録を手元に残していて、それをブルースに渡す。ブルースはそのデータをミスター・ブルーに送る。\n"
         "一方、ブルースがベティの家にいることを知ったレナードは、ロス将軍に連絡してしまう。",
         "The data Betty kept",
         "Betty has kept a copy of Bruce's research records and gives it to him. Bruce sends the data to Mr. Blue.\n"
         "Meanwhile, Leonard realizes Bruce is staying with Betty and contacts General Ross."),
    ]),
    ("第5部 大学での戦い", "Part 5: Battle on campus", [
        ("軍が大学をかこむ",
         "次の日、ロス将軍は兵士たちとブロンスキーを連れて大学に来る。ベティと一緒にいたブルースは見つかり、追いつめられる。\n"
         "ベティは父に向かってやめるようにうったえるが、ロスは聞き入れない。",
         "The army surrounds the campus",
         "The next day, General Ross arrives at the university with his troops and Blonsky. Bruce, who is with Betty, is spotted and cornered.\n"
         "Betty pleads with her father to stop, but Ross won't listen."),
        ("音の兵器と戦車",
         "ブルースは建物の中でハルクに変わる。軍は、大きな音で相手を弱らせる兵器を積んだ車や、装甲車で攻撃する。しかしハルクはそれらを次々にこわしていく。\n"
         "大学の学生たちは、この戦いを携帯電話で撮っている。",
         "Sonic cannons and armored vehicles",
         "Bruce transforms inside a building. The army attacks with vehicles carrying sonic cannons and with armored trucks, but the Hulk tears through them one after another.\n"
         "Students film the battle on their phones."),
        ("ブロンスキーが挑む",
         "薬で強くなったブロンスキーは、たった一人でハルクに向かっていき、ハルクをあざける。しかしハルクに蹴り飛ばされて木にたたきつけられ、全身の骨が折れる大けがをする。",
         "Blonsky takes him on",
         "Enhanced by the serum, Blonsky charges at the Hulk alone and mocks him. The Hulk kicks him into a tree, breaking nearly every bone in his body."),
        ("ベティを守る",
         "攻撃用のヘリコプターがハルクを撃ち、近くにいたベティが巻きこまれそうになる。ハルクはベティをかばい、ヘリコプターを引きずり下ろしてこわす。\n"
         "ハルクはベティを抱えて、その場から去っていく。",
         "Saving Betty",
         "A helicopter gunship fires on the Hulk, nearly killing Betty in the crossfire. The Hulk shields her and pulls the helicopter down.\n"
         "Then he carries Betty away."),
        ("雨の夜の岩山",
         "雨と雷の夜、ハルクはベティを山の中の岩かげに連れていく。雷に向かってほえるハルクを、ベティはやさしくなだめる。ハルクはベティのそばでおとなしくなる。",
         "A stormy night in the hills",
         "On a night of rain and thunder, the Hulk takes Betty to a rocky shelter in the mountains. He roars at the thunder, and Betty gently calms him. He grows quiet beside her."),
        ("ブロンスキーの回復",
         "一方、大けがをしたブロンスキーは、薬の力でおどろくほど早く治っていく。ブロンスキーは、もっと強い力をほしがるようになる。",
         "Blonsky heals",
         "Meanwhile, the badly injured Blonsky heals astonishingly fast thanks to the serum, and he wants even more power."),
    ]),
    ("第6部 ミスター・ブルーの正体", "Part 6: Who Mr. Blue is", [
        ("2人の逃避行",
         "朝、元に戻ったブルースはベティと一緒に逃げることにする。2人は宿に泊まるが、気持ちが高まってブルースの心拍が上がり、それ以上近づけない。\n"
         "2人は中古のトラックを買って移動する。ブルースがミスター・ブルーに連絡すると、ニューヨークで会おうと言われる。",
         "On the road together",
         "In the morning, back to normal, Bruce goes on the run with Betty. At a motel, the moment grows tender, but his heart rate climbs and they have to stop.\n"
         "They buy a used truck. When Bruce contacts Mr. Blue, he urges them to come to New York."),
        ("ニューヨークのタクシー",
         "ニューヨークに着いた2人はタクシーに乗るが、運転がとても乱暴だ。ブルースが落ち着かなくなるのを見て、ベティは運転手を強くしかる。",
         "A New York taxi",
         "In New York, they catch a taxi with a reckless driver. Seeing Bruce get agitated, Betty tells the driver off."),
        ("スターンズ博士",
         "ミスター・ブルーの正体は、グレイバーン大学の細胞生物学者サミュエル・スターンズ博士だった。スターンズはブルースに会えて大喜びし、ハルクを消すかもしれない薬を作ったと話す。",
         "Dr. Sterns",
         "Mr. Blue turns out to be Dr. Samuel Sterns, a cellular biologist at Grayburn College. Thrilled to meet Bruce, he says he has made a possible antidote."),
        ("危険な試し",
         "薬を試すには、わざとブルースをハルクに変えて、そこで薬を打たなければならない。ブルースは台にしばりつけられ、ハルクに変わり始める。\n"
         "暴れ出しそうなハルクを、ベティが話しかけて落ち着かせ、そのあいだにスターンズが薬を打つ。ハルクはブルースの姿に戻る。",
         "A risky test",
         "To test it, they have to trigger a transformation on purpose and inject the antidote mid-change. Bruce is strapped to a table and begins to turn into the Hulk.\n"
         "Betty talks to the struggling Hulk to calm him while Sterns injects the antidote, and he turns back into Bruce."),
        ("治ったのかは分からない",
         "実験はうまくいったように見える。しかしスターンズは、この薬はその1回の変身を止めるだけで、体を完全に治せたかは分からないと話す。",
         "Not necessarily cured",
         "The test seems to work. But Sterns warns that the antidote may only reverse that one transformation, not cure Bruce for good."),
        ("ふやされた血",
         "スターンズは、ブルースがブラジルから送った血をもとに、たくさんの血を作ってためていた。スターンズは、その限りない力を医療に役立てたいと話す。\n"
         "ハルクの力が悪い者の手に渡ることを恐れたブルースは、その血をすべて捨てるよう言う。",
         "A stockpile of blood",
         "Sterns has used the blood samples Bruce sent from Brazil to synthesize a large supply. He wants to apply its \"limitless potential\" to medicine.\n"
         "Fearing the Hulk's power could fall into the wrong hands, Bruce wants the supply destroyed."),
        ("ブルースが捕まる",
         "そこへ、ブロンスキーとロス将軍の部隊がやって来て、ブルースを捕まえる。ブルースとベティは、ヘリコプターで連れていかれる。",
         "Bruce is captured",
         "Blonsky and Ross's forces arrive and take Bruce into custody. Bruce and Betty are flown away in a helicopter."),
    ]),
    ("第7部 アボミネーションとの決戦", "Part 7: Showdown with the Abomination", [
        ("ブロンスキーの頼み",
         "ブロンスキーは研究室に残り、スターンズに、ブルースの血を自分に打てと命じる。ハルクと同じ力がほしかったからだ。スターンズは言われるまま、ブロンスキーに血を打つ。",
         "Blonsky's demand",
         "Blonsky stays behind in the lab and orders Sterns to inject him with Bruce's blood, because he covets the Hulk's power. Sterns does as he is told."),
        ("怪物アボミネーションの誕生",
         "ブロンスキーの体はみるみる変わり、ハルクよりも大きく、骨がとび出したような怪物アボミネーションになる。\n"
         "アボミネーションはスターンズを殴り飛ばす。そのとき、スターンズの額の傷にブルースの血が入り、スターンズの頭がふくらみ始める。",
         "The Abomination is born",
         "Blonsky's body mutates into the Abomination, a monster bigger than the Hulk, with bone jutting from its body.\n"
         "The Abomination knocks Sterns aside. Some of Bruce's blood gets into a cut on Sterns's forehead, and his head begins to swell."),
        ("ハーレムで暴れる",
         "アボミネーションは、ニューヨークのハーレム地区で車や建物をこわし、兵士たちを襲う。ハルクを呼び出すように、大声でさけびながら暴れる。",
         "Rampage in Harlem",
         "The Abomination tears through Harlem, smashing cars and buildings and attacking soldiers, roaring as if to call the Hulk out.\n"
         "He shouts, \"Give me a real fight!\""),
        ("ヘリコプターから飛び降りる",
         "ヘリコプターの中で、ブルースは、アボミネーションを止められるのはハルクだけだとロス将軍を説得する。変身をおさえられるかは分からないが、ハルクの力を向ける先は選べるかもしれないと考えたのだ。\n"
         "ロスが許すと、ブルースは空からとび降りる。地面にたたきつけられたブルースは、ハルクに変わって立ち上がる。",
         "Jumping from the helicopter",
         "In the helicopter, Bruce convinces General Ross that only the Hulk can stop the Abomination. He can't control the change, but he might be able to aim it.\n"
         "Ross lets him go, and Bruce leaps out. He slams into the street and rises as the Hulk."),
        ("怪物どうしの戦い",
         "ハルクとアボミネーションは、通りでぶつかり合う。アボミネーションの力は強く、ハルクは何度も倒される。ハルクはパトカーを2つに引きさき、両手にはめて殴りかかる。\n"
         "戦いの中で、ハルクはベティとロス将軍を危険から守る。",
         "Monster against monster",
         "The Hulk and the Abomination clash in the streets. The Abomination is powerful and knocks the Hulk down again and again. The Hulk rips a police car in half and uses the pieces like boxing gloves.\n"
         "In the middle of the fight, he protects Betty and General Ross from danger.\n"
         "At one point he roars, \"Hulk smash!\""),
        ("くさりで追いつめる",
         "最後にハルクは、太いくさりでアボミネーションの首をしめ、殺しかける。しかしベティの声を聞いて手をゆるめ、命までは取らない。\n"
         "ハルクは、動けなくなったアボミネーションをロスの部隊に引き渡すように放り出す。",
         "The chain",
         "Finally the Hulk wraps a heavy chain around the Abomination's neck and nearly strangles him to death. But when he hears Betty's plea, he loosens his grip and spares his life.\n"
         "He tosses the beaten Abomination aside for Ross's forces to arrest."),
        ("ベティの名前",
         "ハルクはベティの前に立ち、ベティの名前を口にする。それから、ハルクはニューヨークから姿を消す。\n"
         "ロス将軍はアボミネーションを捕まえるが、ブルースはまた逃げてしまう。",
         "Betty's name",
         "The Hulk stands before Betty and says her name, \"Betty.\" Then he leaves New York behind.\n"
         "Ross captures the Abomination, but Bruce gets away again."),
    ]),
    ("第8部 その後", "Part 8: Afterward", [
        ("カナダの山小屋",
         "1か月後、カナダのブリティッシュコロンビア州ベラ・クーラ。ブルースは山小屋で、目をとじて座っている。\n"
         "心拍計の数字がどんどん上がっていき、ブルースが目を開けると、その目は緑に光っている。ブルースは小さくほほえむ。自分の意思で変身をあつかえるようになりつつあるようだ。",
         "The cabin in Canada",
         "A month later, in Bella Coola, British Columbia, Bruce sits in a cabin with his eyes closed.\n"
         "His heart-rate monitor climbs higher and higher. When he opens his eyes, they glow green, and he smiles. He seems to be learning to control the change."),
        ("酒場のトニー・スターク",
         "その後、計画を止められたロス将軍は、酒場で一人酒を飲んでいる。そこへトニー・スタークが現れる。\n"
         "トニーは、ロスの抱える問題を知っていると話し、あの計画が止められたのには理由があると言う。そして、自分たちがチームを作っていると話を持ちかける。",
         "Tony Stark at the bar",
         "Later, General Ross, his program shut down, is drinking alone in a bar when Tony Stark walks in.\n"
         "Tony says he hears Ross has an unusual problem, and that the super-soldier program was put on ice for a reason. Then he asks, \"What if I told you we were putting a team together?\" Ross asks, \"Who's 'we'?\""),
    ]),
    ("まとめ", "Summary", [
        ("ブルースがしたこと",
         "ロス将軍の実験で自分の体にガンマ線を浴び、怒るとハルクに変わる体になった。ベティたちを傷つけて逃げた（第1部）。\n"
         "ブラジルで呼吸の練習をしながら、ミスター・ブルーと治す方法を探した（第2部）。居場所を知られて逃げ、データを求めてアメリカへ戻り、ベティと再会した（第3部・第4部）。\n"
         "ニューヨークでスターンズの薬を試したが、治ったかは分からなかった（第6部）。最後は自分で選んでハルクになり、アボミネーションを止めた（第7部）。",
         "What Bruce did",
         "Exposed to gamma radiation in General Ross's experiment, he became the Hulk whenever angered. He hurt Betty and others and fled (Part 1).\n"
         "In Brazil he practiced breathing and searched for a cure with Mr. Blue (Part 2). Found by the army, he fled back to the U.S. for his data and reunited with Betty (Parts 3 and 4).\n"
         "In New York he tried Sterns's antidote, but it was unclear whether he was cured (Part 6). In the end he chose to become the Hulk and stopped the Abomination (Part 7)."),
        ("ベティとロス将軍",
         "ベティは父に逆らってでもブルースを助け、ハルクの心をしずめた（第5部・第6部）。最後には、ハルクがベティの声を聞いてアボミネーションの命を取らなかった（第7部）。\n"
         "ロス将軍は、ハルクを兵器にするためブルースを追い続け、ブロンスキーに薬を打たせた（第4部）。最後は計画を止められ、トニーに声をかけられる（第8部）。",
         "Betty and General Ross",
         "Betty stood by Bruce even against her father and calmed the Hulk (Parts 5 and 6). In the end, the Hulk spared the Abomination when he heard her voice (Part 7).\n"
         "General Ross kept hunting Bruce to turn the Hulk into a weapon, and had Blonsky injected with the serum (Part 4). In the end his program is shut down and Tony approaches him (Part 8)."),
        ("ブロンスキーとスターンズ",
         "ブロンスキーは、ハルクにかなわなかったことから力をほしがり、超人兵士の薬を打たれた（第4部）。さらにスターンズにブルースの血を打たせて、怪物アボミネーションになった（第7部）。ハーレムで暴れたが、ハルクに負けて捕まった。\n"
         "スターンズは、ブルースの血をふやしてためていた（第6部）。ブロンスキーに殴られたとき、額の傷にブルースの血が入り、頭がふくらみ始めた（第7部）。",
         "Blonsky and Sterns",
         "After failing to beat the Hulk, Blonsky craved power and took the super-soldier serum (Part 4). Then he had Sterns inject him with Bruce's blood and became the Abomination (Part 7). He rampaged through Harlem but was beaten by the Hulk and captured.\n"
         "Sterns had been stockpiling Bruce's blood (Part 6). When Blonsky struck him, Bruce's blood got into a cut on his forehead and his head began to swell (Part 7)."),
        ("名前のある人物の生死",
         "この映画では、名前のある主な人物は誰も死なない。ブロンスキーは大学でハルクに大けがをさせられたが薬の力で治り（第5部）、ハーレムでもハルクに命を助けられて捕まった（第7部）。スターンズも、殴られたが生きている（第7部）。",
         "Who lives and dies",
         "None of the main named characters die in this film. Blonsky was badly hurt by the Hulk on campus but healed thanks to the serum (Part 5), and in Harlem the Hulk spared his life and he was captured (Part 7). Sterns, too, survives being struck (Part 7)."),
    ]),
]
