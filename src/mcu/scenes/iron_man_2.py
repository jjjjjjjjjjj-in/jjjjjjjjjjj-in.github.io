# 『アイアンマン2』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじと登場人物の記事、検索で見つかった解説記事で事実を確かめた。
# 資料どうしで食い違う所（ハマーがヴァンコの死をどうやって見せかけたか、公聴会の映像がどの国のものか、など）や、
# 確かめられない細かい順番・数字・せりふは書いていない。
# 日本語版のせりふは、日本語の吹替・字幕の言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 英語版は、英語の資料で確かめた短いせりふだけを引用した。
# 人物名は相関図（relations.py）にそろえた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 モスクワとエキスポ", "Part 1: Moscow and the Expo", [
        ("父の最期",
         "ロシア、モスクワの古いアパート。テレビでは、トニー・スタークが自分こそアイアンマンだと発表したニュースが流れている。\n"
         "その前で、年老いた科学者アントン・ヴァンコが息を引き取る。アントンは昔アメリカでトニーの父ハワードと一緒に研究をしていたが、国へ送り返され、貧しいまま人生を終えた。息子のイワンが、その最期を看取る。",
         "A father's death",
         "A shabby apartment in Moscow. On TV, the news shows Tony Stark announcing that he is Iron Man.\n"
         "In front of it, the elderly scientist Anton Vanko dies. Years ago Anton worked in America with Tony's father, Howard, but he was sent back home and ended his life in poverty. His son Ivan is at his side as he dies."),
        ("イワンの工作",
         "イワンは、父が残したスターク社の古い設計図を広げる。そこには、トニーの胸にあるものと同じ小型の装置アーク・リアクターの図があった。\n"
         "イワンは部屋にこもって、その装置を自分の手で作り上げる。さらに、装置の力で電気を流す2本のムチを体につける道具も作り始める。",
         "Ivan at work",
         "Ivan spreads out old Stark Industries blueprints his father left behind. They show the same miniature arc reactor that sits in Tony's chest.\n"
         "Shut away in the apartment, Ivan builds one with his own hands, then starts on a harness with two whips charged by the reactor's power."),
        ("空から舞い降りたトニー",
         "それから半年後。ニューヨークで、父ハワードが昔開いていた未来の技術の博覧会スターク・エキスポが、トニーの手で再び開かれる。\n"
         "トニーはアイアンマンのスーツで空から舞台に降り立ち、踊り子たちに囲まれて大歓声を浴びる。トニーは、父の思いを受け継いで、世界中の会社が未来の技術を見せ合う場にするつもりだった。",
         "Tony drops in from the sky",
         "Six months later. In New York, Tony revives the Stark Expo, the fair of future technology his father Howard once held.\n"
         "Tony lands on stage from the sky in his Iron Man suit, flanked by dancers, to a roaring crowd. He wants to carry on his father's legacy and make it a place where companies from around the world show off the technology of the future."),
        ("胸の毒",
         "舞台を降りたトニーは、ひそかに小さな機械を指に当てて、血の中の毒の数値を測る。\n"
         "胸の装置の中心に使っている金属パラジウムの毒が、少しずつ体に回っていたのだ。トニーはこのことを、ペッパーにもローディにも話していない。",
         "Poison in the chest",
         "Off stage, Tony quietly presses a small device to his finger to measure the toxicity in his blood.\n"
         "The palladium at the core of his chest reactor is slowly poisoning him. He hasn't told Pepper or Rhodey."),
    ]),
    ("第2部 公聴会と毒", "Part 2: The hearing and the poison", [
        ("議会の公聴会",
         "ワシントンの議会の公聴会。スターン上院議員は、アイアンマンのスーツは兵器なのだから国に渡すべきだとトニーに迫る。\n"
         "スターンは、空軍のローディ（ジェームズ・ローズ中佐）がまとめた報告書の一部を読ませて、スーツが国の安全をおびやかすと言わせようとする。ローディは、報告書には良い点のほうが大きいとも書いてあると言いそえる。",
         "The Senate hearing",
         "A Senate hearing in Washington. Senator Stern presses Tony to hand over the Iron Man suit, arguing that it is a weapon.\n"
         "Stern has Rhodey, Air Force Lieutenant Colonel James Rhodes, read part of his own report saying the suit could threaten national security. Rhodey adds that the report also concludes the benefits outweigh the risks."),
        ("失敗作の映像",
         "ライバルの兵器会社の社長ジャスティン・ハマーも、ほかの国がスーツをまねして作っていると証言する。\n"
         "トニーは議場の画面を自分の機械で乗っ取り、まねして作ったスーツがみな失敗している映像を流す。ハマーは面目をつぶされる。トニーは、ほかの国が追いつくには何年もかかると言い、世界の平和は自分が守っていると胸を張って議場を出ていく。",
         "Footage of failures",
         "Justin Hammer, head of a rival weapons company, also testifies that other countries are copying the suit.\n"
         "Tony hijacks the screens in the chamber and plays footage of every copied suit failing, embarrassing Hammer. Tony says no one will catch up for years, declares, \"I have successfully privatized world peace,\" and walks out to applause."),
        ("見つからない代わり",
         "マリブの家の工房。トニーは、パラジウムの代わりになる材料を手当たりしだいに試すが、どれもうまくいかない。\n"
         "人工知能のジャーヴィスは、今の装置を使い続ければ毒で命が危ないと伝える。トニーの体には、胸から血管に沿って黒い線が広がり始めていた。",
         "No substitute",
         "In his workshop at his Malibu home, Tony tries every material he can think of to replace the palladium, but nothing works.\n"
         "His AI, J.A.R.V.I.S., warns that if he keeps using the reactor, the poison will kill him. Dark lines are starting to spread from his chest along his veins."),
        ("社長はペッパーに",
         "死を覚悟したトニーは、会社の社長の座を秘書のペッパーに譲る。\n"
         "書類の手続きのため、法務部からナタリー・ラッシュマンという女性がやって来る。トニーはハッピーとボクシングの練習をしていたが、ナタリーはリングに上がると、一瞬でハッピーを投げ倒す。トニーは、ナタリーを新しい秘書にすると決める。",
         "Pepper becomes CEO",
         "Expecting to die, Tony hands control of the company to his assistant, Pepper.\n"
         "Natalie Rushman from the legal department arrives to handle the paperwork. Tony is boxing with Happy, and when Natalie steps into the ring she flips Happy to the mat in an instant. Tony decides to make her his new assistant."),
    ]),
    ("第3部 モナコの襲撃", "Part 3: Attack at Monaco", [
        ("モナコのレース",
         "トニー、ペッパー、ナタリー、ハッピーは、スターク社が後押しする自動車レースのためにモナコへ行く。会場には、記者のクリスティンを連れたハマーも来ている。\n"
         "スタートの直前、トニーは急に、自分の会社の車を自分で運転すると言い出し、レースに出てしまう。ペッパーはあきれ返る。",
         "The race at Monaco",
         "Tony, Pepper, Natalie and Happy go to Monaco for a car race Stark Industries sponsors. Hammer is there too, with the reporter Christine Everhart.\n"
         "Just before the start, Tony suddenly decides to drive his company's car in the race himself. Pepper is exasperated."),
        ("電気のムチ",
         "レースの途中、コースの係員に化けたイワンがコースに出てくる。胸の装置を光らせ、電気のムチを振るって、走ってくる車を真っ二つに切り裂く。\n"
         "トニーの車も切られて大破する。トニーはぼろぼろの車のそばで、スーツもないままイワンに追いつめられる。",
         "Electric whips",
         "Mid-race, Ivan, disguised as a track worker, walks onto the course. His chest reactor glowing, he swings his electric whips and slices oncoming cars in half.\n"
         "Tony's car is cut apart and wrecked. Without a suit, Tony is cornered by Ivan beside the wreck."),
        ("かばんのスーツ",
         "ハッピーとペッパーが車でコースに飛びこみ、イワンに何度もぶつける。しかしイワンはムチで車まで切りきざむ。\n"
         "ペッパーが、かばんの形に折りたたんだ持ち運び用のスーツをトニーに投げる。トニーはかばんを開いてスーツを身につけ、イワンのムチを手に巻きつけて引き寄せ、胸の装置をもぎ取る。イワンは捕まる。",
         "The suitcase suit",
         "Happy and Pepper drive onto the track and ram Ivan again and again, but he slices up their car with his whips too.\n"
         "Pepper throws Tony a portable suit folded into a briefcase. Tony opens it, suits up, wraps the whips around his hands, pulls Ivan in and rips the reactor out of his chest. Ivan is arrested."),
        ("牢屋での話",
         "トニーは牢屋のイワンに会いに行く。イワンは、自分の父とハワードが一緒に装置を作ったのに、ハワードが父を国へ追い返したと話す。\n"
         "イワンは、神に血を流させれば、人々は神を信じなくなる、と言う。アイアンマンも負けることがあると世界に見せれば、それで十分だったのだ。そして、トニーの装置がトニー自身の体をむしばんでいることも見抜いていた。",
         "Talking in prison",
         "Tony visits Ivan in his cell. Ivan says his father and Howard built the reactor together, but Howard had his father sent back home.\n"
         "Ivan says that if you can make God bleed, people will stop believing in Him. Showing the world that Iron Man can be beaten was enough for him. He also knows that Tony's reactor is killing him."),
    ]),
    ("第4部 ハマーの企み", "Part 4: Hammer's scheme", [
        ("連れ出されたイワン",
         "イワンの戦いぶりに目をつけたハマーは、イワンが牢屋で死んだように見せかけて、ひそかに外へ連れ出す。\n"
         "ハマーはプライベートジェットの中でイワンをもてなし、トニーをしのぐスーツを自分の会社で作ってほしいと頼む。",
         "Ivan breaks out",
         "Impressed by Ivan's attack, Hammer fakes Ivan's death in prison and secretly gets him out.\n"
         "On his private jet, Hammer wines and dines Ivan and asks him to build suits for his company that will outdo Tony's."),
        ("鳥がほしい",
         "ハマーの工場で、イワンは仕事を引き受ける。そのかわりに求めたのは、ロシアに残してきた自分の鳥を連れてくることだった。\n"
         "イワンは、人が中に入るスーツより、人の乗らないロボット兵（ドローン）のほうがよいと考え、ハマーの思惑とは違うものを作り始める。",
         "He wants his bird",
         "At Hammer's factory, Ivan agrees to the job. In return, he asks for one thing: his pet bird, left behind in Russia.\n"
         "Ivan decides that unmanned drones are better than suits with people inside, and starts building something different from what Hammer wanted."),
        ("世間の声",
         "モナコの事件で、アイアンマンと同じような技術がほかにもあると世界中が知る。テレビでは、スーツを国に渡しておけばよかったのではないかという声も上がる。\n"
         "トニーはペッパーにも本当のことを言えないまま、毒の数値は上がり続けていた。",
         "Public opinion",
         "The Monaco attack shows the world that technology like Iron Man's exists elsewhere. On TV, people ask whether Tony should have handed the suit over after all.\n"
         "Tony still can't tell Pepper the truth, and his toxicity keeps rising."),
    ]),
    ("第5部 誕生日のけんか", "Part 5: The birthday fight", [
        ("荒れたパーティー",
         "マリブの家で、トニーの誕生日パーティーが開かれる。これが最後の誕生日になるかもしれないと思うトニーは、スーツを着たまま酒に酔う。\n"
         "トニーはスーツの手のひらから光線を撃って、客の前でびんや果物を壊して見せる。客は面白がるが、ペッパーはあきれ果てる。",
         "A party out of control",
         "Tony throws a birthday party at his Malibu home. Thinking it may be his last, he gets drunk while wearing his suit.\n"
         "He blasts bottles and fruit with the repulsors in his palms to show off for the guests. The guests love it, but Pepper is fed up."),
        ("親友とのけんか",
         "そこへ来たローディは、家にあった別のスーツ（マーク2）を着て、トニーを止めに入る。2人は家の中で激しく殴り合い、客は逃げ出し、家はめちゃくちゃに壊れる。\n"
         "けんかは、どちらも勝てないまま終わる。",
         "Fighting his best friend",
         "Rhodey arrives, puts on another suit kept in the house (the Mark II), and steps in to stop Tony. The two brawl through the house, the guests flee, and the place is wrecked.\n"
         "The fight ends with neither of them winning."),
        ("持ち去られたスーツ",
         "ローディは、そのスーツを着たまま空軍の基地へ飛んでいく。\n"
         "軍はスーツを取り上げ、ハマーの会社にたくさんの武器を取り付けさせることにする。ハマーは、スーツを手に入れられると大喜びする。",
         "The suit is taken",
         "Still wearing the suit, Rhodey flies to an Air Force base.\n"
         "The military seizes it and has Hammer's company load it with weapons. Hammer is thrilled to finally get his hands on a suit."),
    ]),
    ("第6部 父からの手がかり", "Part 6: A clue from his father", [
        ("ドーナツ店の上で",
         "次の朝。ロサンゼルスのドーナツ店の屋根にある巨大なドーナツの飾りの中に、スーツを着たトニーが座りこんでいる。\n"
         "そこへニック・フューリーが現れ、トニーを店の中へ呼ぶ。中で待っていたのはナタリーだった。ナタリーの本当の名前はナターシャ・ロマノフ。フューリーの組織シールドのスパイで、トニーを見張るために送りこまれていた。",
         "On top of the donut shop",
         "The next morning, Tony, still in his suit, is sitting inside the giant donut on the roof of a Los Angeles donut shop.\n"
         "Nick Fury appears and calls him inside. Natalie is waiting there. Her real name is Natasha Romanoff, a spy for Fury's agency, S.H.I.E.L.D., sent in to watch Tony."),
        ("父とシールド",
         "フューリーの指示で、ナターシャはトニーの首に薬を打つ。毒の苦しみをしばらくおさえる薬だった。\n"
         "フューリーは、ハワードがシールドを作った1人だったことを明かす。そして、アントン・ヴァンコはハワードと一緒に装置を作ったが、それを売ってもうけようとしたため、ハワードが国へ送り返したのだと話す。",
         "His father and S.H.I.E.L.D.",
         "On Fury's orders, Natasha injects Tony in the neck with lithium dioxide, which eases the poison's effects for a while.\n"
         "Fury reveals that Howard was one of the founders of S.H.I.E.L.D. He explains that Anton Vanko built the reactor with Howard but tried to sell it for profit, so Howard had him deported."),
        ("見張りつきの家",
         "フューリーは、ハワードが残した資料の箱をトニーに渡す。家にはシールドのコールソンがやって来て、トニーが家から出ないよう見張る。\n"
         "トニーはしぶしぶ、壊れた家で父の資料を調べ始める。",
         "Under watch at home",
         "Fury gives Tony a box of material Howard left behind. S.H.I.E.L.D. agent Coulson arrives to make sure Tony stays home.\n"
         "Grudgingly, Tony starts going through his father's things in his wrecked house."),
        ("古いフィルム",
         "箱の中には、エキスポの準備をしていたころのハワードを写したフィルムがあった。\n"
         "最初は、冷たい父の姿にしか見えない。しかしフィルムの終わりで、ハワードは幼いトニーに語りかける。今の技術ではできないことがあるが、お前ならいつかできる、そして自分が作った中でいちばんのものはお前だ、と。父に愛されていないと思っていたトニーは、心を動かされる。",
         "The old film",
         "In the box is film of Howard preparing for the Expo years ago.\n"
         "At first he seems as cold as Tony remembers. But at the end, Howard speaks to young Tony: the technology of his day held him back, Tony will be able to finish what he couldn't, and Tony is his greatest creation. Tony, who always believed his father didn't love him, is moved."),
    ]),
    ("第7部 新しい元素", "Part 7: A new element", [
        ("模型の中の図",
         "トニーは、父の資料に出てくる1974年のスターク・エキスポの会場の模型を、家に運ばせる。\n"
         "ジャーヴィスの力を借りて模型を立体の図にすると、会場の並びが、まだ誰も作ったことのない新しい元素のつくりを表していることが分かる。父は、当時は作れなかったこの元素を、息子に託していたのだ。",
         "The diagram in the model",
         "Tony has the model of the 1974 Stark Expo grounds, which appears in his father's material, brought to the house.\n"
         "With J.A.R.V.I.S.'s help, he turns it into a 3D image and sees that the layout of the grounds is the structure of a new element no one has ever made. His father, unable to make it back then, left it for his son."),
        ("家の中の装置",
         "トニーは家の壁を壊して、大がかりな装置（粒子加速器）を自分で作り上げる。そばにあった古い丸い盾を、装置を支える台に使う場面もある。\n"
         "装置から出た光で新しい元素が作られ、トニーはそれを三角形の新しい胸の装置に入れる。毒の数値は下がり、トニーは助かる。",
         "A machine in the house",
         "Tony breaks through the walls of his home and builds a large particle accelerator himself, even using an old round shield he finds to prop part of it up.\n"
         "Its beam creates the new element, and Tony puts it into a new triangular reactor in his chest. His toxicity drops, and he is saved."),
        ("イワンからの電話",
         "そこへイワンから電話が入る。イワンは生きていて、トニーにもう一度戦いを挑むつもりだった。\n"
         "見張りのコールソンは、この間に別の任務でニューメキシコへ向かっていた。イワンがエキスポで何かをする気だと気づいたトニーは、新しいスーツを着てエキスポへ飛ぶ。",
         "A call from Ivan",
         "Then Ivan calls. He's alive, and he means to take Tony on again.\n"
         "Coulson, his minder, has meanwhile been sent on another mission in New Mexico. Realizing Ivan is planning something at the Expo, Tony puts on a new suit and flies there."),
    ]),
    ("第8部 エキスポの戦い", "Part 8: The battle at the Expo", [
        ("ハマーの発表",
         "エキスポの会場で、ハマーは陸軍・海軍・空軍・海兵隊向けのロボット兵（ドローン）をずらりと並べて発表する。\n"
         "最後に、たくさんの武器を積んだ灰色のスーツ、ウォーマシンが登場する。中に入っているのはローディだった。",
         "Hammer's showcase",
         "At the Expo, Hammer unveils rows of drones built for the Army, Navy, Air Force and Marines.\n"
         "Last comes War Machine, a gray suit loaded with weapons. Rhodey is inside."),
        ("乗っ取られたロボット",
         "トニーが会場に降り立ち、ローディにイワンのことを知らせようとしたとき、イワンがロボットとウォーマシンをすべて遠くから乗っ取る。\n"
         "ロボットたちはアイアンマンに撃ちかかり、ローディのスーツも、本人の意思と関係なくトニーを攻撃する。トニーは観客を巻きこまないよう空へ逃げ、ロボットたちが追ってくる。",
         "Hijacked",
         "Just as Tony lands and tries to warn Rhodey about Ivan, Ivan takes remote control of all the drones and War Machine.\n"
         "The drones open fire on Iron Man, and Rhodey's suit attacks Tony against his will. Tony flies up and away to keep the crowd out of it, with the drones in pursuit."),
        ("問いつめられたハマー",
         "ナターシャたちは会場でハマーを問いつめ、すべてはハマーの会社にいるイワンのしわざだと突き止める。ハマーは、イワンを牢屋から連れ出した疑いで警察に捕まる。\n"
         "ナターシャとハッピーは車でハマーの工場へ向かう。",
         "Hammer cornered",
         "Natasha and the others confront Hammer at the Expo and work out that Ivan, hidden at Hammer's company, is behind it all. Hammer is arrested for breaking Ivan out of prison.\n"
         "Natasha and Happy drive to Hammer's facility."),
        ("ナターシャとハッピー",
         "工場では、ナターシャが警備員たちを次々と倒して奥へ進む。ハッピーも警備員の1人と殴り合い、なんとか倒す。\n"
         "イワンはすでに、自分用の強いスーツを着て工場を出たあとだった。ナターシャはコンピューターを操作して、ローディのスーツを本人の手に取り戻す。",
         "Natasha and Happy",
         "At the facility, Natasha takes down guard after guard as she moves in. Happy slugs it out with one guard and finally beats him.\n"
         "Ivan has already left in a powerful suit of his own. Natasha gets into the computers and gives Rhodey back control of his suit."),
        ("2人で戦う",
         "体が自由になったローディは、トニーと並んで戦う。2人は会場の日本庭園のような建物の中で、取り囲んだロボットたちを撃ち倒していく。\n"
         "そこへ、ムチのついた大きなスーツを着たイワンが現れる。イワンの力は強く、2人とも苦戦する。",
         "Fighting side by side",
         "Free again, Rhodey fights alongside Tony. Inside a Japanese garden pavilion at the Expo, they gun down the drones surrounding them.\n"
         "Then Ivan appears in a large armored suit with whips. He is strong, and both of them struggle."),
        ("交差する光線",
         "トニーとローディは、手のひらの光線を互いに向けて撃ち、ぶつかり合った光の大爆発でイワンを吹き飛ばす。イワンのスーツは壊れ、イワンは倒れる。\n"
         "しかしイワンのスーツと、残ったロボットには爆弾がしかけられていた。イワンはトニーたちを巻きこもうと自分のスーツを爆発させて死に、ロボットたちも次々に爆発する。",
         "Crossing the beams",
         "Tony and Rhodey fire their repulsor beams at each other, and the collision blows Ivan away. His suit is wrecked and he goes down.\n"
         "But Ivan's suit and the remaining drones are rigged to explode. Ivan blows up his suit to take them with him and dies, and the drones explode one after another."),
        ("屋上のキス",
         "まだ爆発していないロボットのそばに、ペッパーが立っていた。トニーは間一髪でペッパーを抱えて飛び、近くの屋上に降ろす。\n"
         "ペッパーは、社長の仕事の重さと、トニーが死にかけていたのを隠していたことにまいって、社長をやめると言う。言い合いの途中で、2人はキスをする。",
         "A kiss on the rooftop",
         "Pepper is standing near a drone that hasn't exploded yet. Tony scoops her up just in time and sets her down on a nearby rooftop.\n"
         "Worn out by the job and by Tony hiding that he was dying, Pepper says she quits as CEO. In the middle of their argument, they kiss."),
    ]),
    ("第9部 その後", "Part 9: Afterward", [
        ("フューリーの評価",
         "フューリーは、ナターシャがまとめたトニーの評価をトニーに見せる。アイアンマンはヒーローを集める計画（アベンジャーズ計画）にふさわしいが、トニー・スターク本人は性格に問題があるのですすめない、という内容だった。\n"
         "それでもフューリーは、トニーに相談役として手伝ってほしいと頼む。",
         "Fury's assessment",
         "Fury shows Tony the assessment Natasha wrote: Iron Man is a good fit for the hero program, the Avengers Initiative, but Tony Stark himself is not recommended because of his personality.\n"
         "Even so, Fury asks Tony to help as a consultant."),
        ("勲章",
         "トニーとローディは、ワシントンでスターン上院議員から勲章を受け取る。トニーを嫌っているスターンは、しぶしぶ勲章をかける。",
         "Medals",
         "In Washington, Tony and Rhodey receive medals from Senator Stern, who can't stand Tony and pins them on grudgingly."),
        ("エンドクレジットの後",
         "ニューメキシコ州の砂漠。コールソンが車で到着し、フューリーに、見つけたと電話で伝える。\n"
         "大きなくぼみの真ん中には、地面に刺さった不思議なハンマーがあった。（次の作品『マイティ・ソー』につながる場面）",
         "After the credits",
         "The New Mexico desert. Coulson arrives by car and calls Fury: \"Sir, we've found it.\"\n"
         "In the middle of a crater, a strange hammer is stuck in the ground. (This leads into Thor.)"),
    ]),
    ("まとめ", "Summary", [
        ("トニーの毒と答え",
         "トニーは、胸の装置のパラジウムの毒で死にかけていたが、誰にも言わなかった（第1部・第2部）。やけになって社長をペッパーに譲り、モナコでレースに出て、誕生日には酔って暴れた（第2部・第3部・第5部）。\n"
         "フューリーとナターシャに助けられ、父ハワードが残したフィルムと模型から新しい元素を見つけ、自分で作って毒を止めた（第6部・第7部）。",
         "Tony's poisoning and the cure",
         "Tony was dying from the palladium in his chest reactor but told no one (Parts 1 and 2). Reckless, he handed the company to Pepper, raced at Monaco and got drunk and destructive at his birthday party (Parts 2, 3 and 5).\n"
         "Helped by Fury and Natasha, he found a new element in the film and model his father Howard left behind, made it himself and stopped the poisoning (Parts 6 and 7)."),
        ("イワン・ヴァンコがしたこと",
         "父アントンがハワードに追い返されたと恨み、父の設計図から装置と電気のムチを作って、モナコでトニーを襲った（第1部・第3部）。\n"
         "ハマーに牢屋から連れ出されると、ハマーのためにロボット兵を作るふりをして、エキスポでロボットとローディのスーツを乗っ取り、トニーを殺そうとした（第4部・第8部）。",
         "What Ivan Vanko did",
         "Blaming Howard for sending his father Anton away, he built a reactor and electric whips from his father's blueprints and attacked Tony at Monaco (Parts 1 and 3).\n"
         "After Hammer broke him out of prison, he pretended to build drones for Hammer, then hijacked the drones and Rhodey's suit at the Expo to kill Tony (Parts 4 and 8)."),
        ("ハマーとローディ",
         "ハマーはトニーのライバルで、公聴会で恥をかかされた（第2部）。イワンを牢屋から連れ出してロボット兵を作らせ、ローディのスーツに武器を積んだが、エキスポでイワンにすべて乗っ取られ、最後は警察に捕まった（第4部・第5部・第8部）。\n"
         "ローディは、荒れるトニーを止めるためにスーツを持ち出して軍に渡したが（第5部）、最後はトニーと並んで戦い、一緒に勲章を受けた（第8部・第9部）。",
         "Hammer and Rhodey",
         "Hammer, Tony's rival, was humiliated at the hearing (Part 2). He broke Ivan out of prison to build drones and armed Rhodey's suit, but Ivan took it all over at the Expo, and Hammer ended up arrested (Parts 4, 5 and 8).\n"
         "Rhodey took a suit and gave it to the military to stop the out-of-control Tony (Part 5), but in the end fought beside him and received a medal with him (Parts 8 and 9)."),
        ("死んだ人たち（話の順に）",
         "・アントン・ヴァンコ（第1部）：モスクワのアパートで息を引き取る。息子イワンがトニーを恨むきっかけになる。\n"
         "・イワン・ヴァンコ（第8部）：エキスポでトニーとローディに倒されたあと、自分のスーツにしかけた爆弾を爆発させて死ぬ。トニーたちを巻きこむつもりでもあった。\n"
         "・トニー（第2部〜第7部）：死んではいない。パラジウムの毒で死にかけていたが、新しい元素で助かる。",
         "Who died (in order)",
         "- Anton Vanko (Part 1): dies in his Moscow apartment, which sets his son Ivan against Tony.\n"
         "- Ivan Vanko (Part 8): after Tony and Rhodey defeat him at the Expo, he sets off the bomb in his own suit and dies, hoping to take them with him.\n"
         "- Tony (Parts 2 to 7): not dead. The palladium was killing him, but the new element saves him."),
    ]),
]
