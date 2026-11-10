# 『アイアンハート』シーンごとの詳しいあらすじ
# 2026-11-10 新しい形（ファルコン＆ウィンター・ソルジャーと同じ）に書き直した。
# 英語版ウィキペディアの作品の記事（各話のあらすじ・登場人物）と、日本語版ウィキペディアの登場人物（名前の表記）、
# 英語の各話の解説記事（検索で読めた部分）を照らし合わせて書いた。前の版のまちがい（ジョーの正体の書き方など）も直した。
# 資料どうしで食い違う所（第3話でメイソンがどうやって殺されたか、第4話の場面の順番、第6話でパーカーがどうなったか、
# ホログラムのしかけのくわしい様子、手に広がる線の色）は書いていない。
# 日本語版の各話の題名と日本語のセリフは確かめられなかったので、題名は英語のまま、カギかっこの引用は入れていない。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「話-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1話 Take Me Home", "Episode 1: Take Me Home", [
        ("子どものころの夢",
         "シカゴ。子どものころのリリ・ウィリアムズと親友ナタリー・ワシントンが、将来の夢を語りながら動画をとっている。ナタリーは、リリはいつか世界一有名な発明家たちより大きな人になる、と言ってはげます。",
         "A childhood dream",
         "Chicago. Young Riri Williams and her best friend Natalie Washington film a video about their dreams. Natalie tells Riri she'll be bigger than the most famous inventors in the world."),
        ("MITを追い出される",
         "大人になったリリは、マサチューセッツ工科大学（MIT）で、自分で作ったアーマーの研究を続けている。『シビル・ウォー』にも出てきたウィルクス教授の前でアーマーを動かすが、研究室は騒ぎになる。\n"
         "リリは学部長に呼ばれ、研究のお金をもっと続けてほしいとたのむ。しかし、告げられたのは退学だった。リリは研究のお金をかせぐため、ほかの学生に自分の作った課題や研究を売り、その学生たちに自分の作品として出させていた。",
         "Expelled from MIT",
         "Now grown, Riri is developing her own suit of armor at MIT. She powers it up in front of Professor Wilkes, who appeared in Civil War, and the lab is thrown into chaos.\n"
         "Called in by the dean, she asks for more time and funding. Instead she's expelled: to pay for her research, she had been selling her work to other students, who turned it in as their own."),
        ("シカゴへ飛んで帰る",
         "リリはアーマーを着て大学を飛び出し、シカゴへ向かう。しかし大学がアーマーの操作を手伝うシステムを止めたため、アーマーは途中でうまく動かなくなり、シカゴの道に落ちる。リリはこわれかけのアーマーをかかえて家へ帰る。",
         "Flying home",
         "Riri flies off campus in the armor, heading for Chicago. But the university cuts her off from the system helping her fly, the suit falls apart on the way, and she crashes in a Chicago street. She lugs the broken armor home."),
        ("パーカーの仲間たち",
         "同じころシカゴでは、パーカー・ロビンスが率いる泥棒の仲間が、警備会社の人のふりをして盗みをはたらいている。警報を止める係がうまくいかず、パーカーはいとこで右腕のジョンと、技術の係を新しく探そうと話す。それまでの係は、ランページと名乗るスチュアート・クラークだった。\n"
         "そのとき空を飛ぶアーマーが通り過ぎ、パーカーたちはリリに目をつける。",
         "Parker's crew",
         "Meanwhile in Chicago, a crew led by Parker Robbins pulls a robbery while posing as security staff. Their alarm man fumbles the job, and Parker tells his cousin and right hand, John, that they need a new tech specialist to replace Stuart Clarke, who calls himself Rampage.\n"
         "Then the flying armor passes overhead, and they set their sights on Riri."),
        ("母ロニーと、亡くした人たち",
         "家では母ロニーがリリを迎える。リリには、つらい過去があった。何年も前、無関係の車からの銃撃（ドライブ・バイ）に巻きこまれ、親友ナタリーと、義理の父ゲイリーが亡くなったのだ。ゲイリーは車の修理工場をしていて、リリとナタリーはそこでよく一緒に過ごしていた。\n"
         "リリは、ロニーがゲイリーの工場を続けなかったことを今も責めている。",
         "Ronnie, and the people they lost",
         "At home, her mother Ronnie welcomes her. Riri carries an old wound: years ago, her best friend Natalie and her stepfather Gary were killed in a drive-by shooting that had nothing to do with them. Gary ran an auto shop, where Riri and Natalie spent a lot of time.\n"
         "Riri still resents her mother for not keeping Gary's shop going."),
        ("ナタリーの弟エグザヴィア",
         "リリは、ナタリーの弟エグザヴィアと再会する。エグザヴィアは音楽を作っていて、その曲にはナタリーの声が使われている。リリはナタリーとの思い出を思い出す。",
         "Natalie's brother Xavier",
         "Riri reconnects with Natalie's brother Xavier. He makes music, and one of his tracks samples Natalie's voice, bringing back memories of her."),
        ("ジョンの誘いと、エレベーターの試験",
         "アーマーの部品を買うお金がないリリに、ジョンが近づき、才能を分かってくれるボスの仕事があると誘う。教えられた場所は、ピザ屋の下にある隠れ家だった。\n"
         "リリが乗ったエレベーターは途中で止まり、ガスで満たされていく。スピーカーから、これが面接だという声が聞こえる。リリは言われたとおりにはせず、自分の工夫でエレベーターを動かして、外へ出る。見ていた仲間たちは拍手で迎える。そこでリリは、ネットの仲間として知っていたスチュアートにも会う。",
         "John's offer, and the elevator test",
         "Short on money for parts, Riri is approached by John, who pitches work for a boss who values genius. The address leads to a hideout beneath a pizza place.\n"
         "The elevator stalls and fills with gas, and a voice on the speaker says this is her interview. Ignoring the instructions, Riri improvises her own way to get the elevator moving and gets out. The crew, watching, applauds. She also meets Stuart, whom she knows from an online tech community."),
        ("3回の仕事の約束",
         "リーダーのパーカーは、リリを仲間に誘う。リリはいったん断るが、パーカーは現金の入った箱を見せ、あと3回の仕事を手伝えばもっとかせげると話す。アーマーを仕上げるお金が必要なリリは、3回だけという約束で引き受ける。",
         "A deal for three jobs",
         "Parker, the leader, invites Riri in. She turns him down at first, but he shows her a box of cash and says three more jobs will earn her much more. Needing money to finish her armor, she agrees to three jobs."),
        ("ナタリーの姿の人工知能",
         "家に帰ったリリは、亡くした人たちのことでロニーにきつく当たってしまう。\n"
         "その夜、リリはアーマーに入れる人工知能を作ろうと、自分の脳のはたらきを写し取ってシステムに取りこむ。ところが、まだ心の中で整理できていない悲しみのせいで、できあがった人工知能はナタリーの姿と性格で話し始める。リリは、ナタリーをアーマーの中に残しておくべきか悩む。",
         "An AI that looks like Natalie",
         "At home, Riri lashes out at Ronnie over the people they've lost.\n"
         "That night, Riri maps her own brain to build an AI for her armor. But her unprocessed grief shapes the result: the AI speaks with Natalie's face and personality. Riri wrestles with whether to keep Natalie in her suit."),
    ]),
    ("第2話 Will the Real Natalie Please Stand Up?", "Episode 2: Will the Real Natalie Please Stand Up?", [
        ("N.A.T.A.L.I.E.",
         "朝、目を覚ましたリリの前には、ナタリーの姿の人工知能がいる。リリは消そうとするが、人工知能はいやがり、2人は言い合いになる。人工知能は、N.A.T.A.L.I.E.（ナタリー）と呼ばれるようになる。リリはロニーには何でもないと言って、部屋に入れない。",
         "N.A.T.A.L.I.E.",
         "Riri wakes to find the Natalie-shaped AI watching her. She tries to erase it, it objects, and they argue. The AI becomes known as N.A.T.A.L.I.E. Riri tells Ronnie she's fine and keeps her out of the room."),
        ("パーカーの仲間たち",
         "パーカーに呼ばれて隠れ家に行ったリリは、仲間を紹介される。パーカーのいとこでナイフ使いのジョン、マドリプール出身のハッカーのスラッグ、火薬や爆破が得意なクラウン、力の強いきょうだいのジェリとロズのブラッド。",
         "Meet the crew",
         "Called to the hideout, Riri meets the crew: Parker's knife-wielding cousin John, Slug, a hacker from Madripoor, Clown, an explosives expert, and the muscle, siblings Jeri and Roz Blood."),
        ("ねらいはTNNL",
         "次のねらいは、シーラ・ザラテが社長をつとめる会社TNNL。シカゴの地下にある古い貨物用のトンネルを、お金持ちのための専用の道路に作りかえていて、そのために地元の人たちが苦しんでいる。\n"
         "計画は、試験走行の日に会社のシステムに入りこみ、社長をおどせる材料をにぎること。",
         "Target: TNNL",
         "The target is TNNL, a company run by Sheila Zarate that is turning Chicago's old freight tunnels into a private highway for the wealthy, at the expense of local communities.\n"
         "The plan: break into the company's systems during a test run and gain leverage over the CEO."),
        ("ジョー・マクギリカディをおどす",
         "アーマーを仕上げるには部品が足りない。N.A.T.A.L.I.E.が見つけたのは、シカゴの北の町エヴァンストンに住む、ジョー・マクギリカディという男。表に出せない武器や技術を集めている人物だ。\n"
         "ジョーは人ちがいだととぼけるが、リリに通報すると言われて折れる。地下の部屋には、思っていたよりずっと多くの機械や武器があった。リリは、ジョーが手放したがらなかった強い動力の部品を手に入れる。おとなしいジョーとリリは、少しずつ打ちとける。",
         "Blackmailing Joe McGillicuddy",
         "Riri still needs parts. N.A.T.A.L.I.E. points her to Joe McGillicuddy in Evanston, just north of Chicago, a collector of black-market weapons and tech.\n"
         "Joe claims she has the wrong man, but gives in when she threatens to report him. His underground room holds far more gear than she expected. Riri gets a powerful energy part he had been reluctant to give up, and the two slowly warm to each other."),
        ("トンネルでの仕事",
         "仕事の日。ジョンとブラッドきょうだいが制御室をおさえ、クラウンが爆破で地下の道路に穴を開ける。リリはアーマーでトンネルに飛びこむ。\n"
         "ところが、N.A.T.A.L.I.E.がアーマーにつながり直したせいでリリはおどろき、計画がくずれかける。それでもリリとN.A.T.A.L.I.E.は力を合わせ、TNNLのシステムを止めることに成功する。",
         "The tunnel job",
         "Job day. John and the Blood siblings seize the control room, Clown blasts into the underground highway, and Riri flies into the tunnels in her armor.\n"
         "When N.A.T.A.L.I.E. reconnects to the suit, Riri is thrown off and the job nearly falls apart. Still, working together, they manage to sabotage TNNL's systems."),
        ("社長への取り引き",
         "パーカーは社長ザラテの前に現れ、自分たちの仲間を会社の給料をもらう者として加えるよう、書類に名前を書かせる。",
         "Squeezing the CEO",
         "Parker confronts CEO Zarate and forces her to sign papers putting his crew on the company's payroll."),
        ("曲がる銃弾",
         "にげる途中、警備員がリリに銃を向ける。N.A.T.A.L.I.E.は銃を見て固まってしまう。\n"
         "そこへパーカーが銃を撃つ。弾は不思議な曲がり方をして、警備員に当たる。リリは助かる。\n"
         "あとでN.A.T.A.L.I.E.は、パーカーから説明のできない強い力を感じたので気をつけて、とリリに伝える。",
         "The bending bullet",
         "As they escape, a guard aims a gun at Riri. N.A.T.A.L.I.E. freezes at the sight of it.\n"
         "Parker fires, and his bullet bends in an impossible path to hit the guard. Riri is saved.\n"
         "Later, N.A.T.A.L.I.E. warns Riri that she sensed a strange power coming from Parker that she couldn't analyze."),
        ("ロニーとN.A.T.A.L.I.E.",
         "家では、ロニーもN.A.T.A.L.I.E.のことを知る。ロニーは、もう一度「ナタリー」に会えたことを喜ぶ。",
         "Ronnie meets N.A.T.A.L.I.E.",
         "At home, Ronnie finds out about N.A.T.A.L.I.E. and is moved to see \"Natalie\" again."),
        ("広がる黒い線",
         "隠れ家に戻ったパーカーは、マントをかける。マントからは、ささやくような声が聞こえる。パーカーの体には黒い血管のような線が広がっていて、ジョンはそれがひどくなっていることに気づく。",
         "Spreading black veins",
         "Back at the hideout, Parker hangs up his cloak, which seems to whisper. Black, vein-like marks are spreading across his body, and John sees they are getting worse."),
    ]),
    ("第3話 We in Danger, Girl", "Episode 3: We in Danger, Girl", [
        ("マントにさわるな",
         "仲間たちはTNNLの成功を祝う。クラウンとリリがパーカーのマントにさわると、ジョンはきびしくしかる。マントは、パーカーの力のもとだった。\n"
         "リリはパーカーに、マントの仕組みをたずねる。パーカーは魔法だと答えるだけで、科学を信じるリリは納得できない。リリは、マントの切れはしを手に入れて調べようと考える。",
         "Don't touch the cloak",
         "The crew celebrates the TNNL job. When Clown and Riri touch Parker's cloak, the source of his powers, John scolds them.\n"
         "Riri asks Parker how the cloak works. He just says it's magic, which Riri, a believer in science, can't accept. She decides to get a piece of it to study."),
        ("エグザヴィアのヘッドホン",
         "リリはエグザヴィアに新しいヘッドホンを贈る。エグザヴィアは、お金の出どころを気にする。今使っているヘッドホンはナタリーのもので、手放したくないのだと話す。",
         "Xavier's headphones",
         "Riri gives Xavier new headphones. He wonders where the money came from, and explains that his old ones were Natalie's and he wants to keep them."),
        ("スチュアートの死",
         "警察がリリのもとに来る。前の仲間スチュアート（ランページ）が、殺されて見つかったのだ。最後に連絡をとったのがリリだったため、話を聞かれる。リリは、パーカーたちがやったのではないかと不安になる。",
         "Stuart is dead",
         "Police come to Riri: Stuart (Rampage), the crew member she replaced, has been found murdered, and she was the last person he contacted. Riri begins to fear Parker's crew was behind it."),
        ("ジョーの正体",
         "次のねらいは、農業の技術の会社ヘアラム。新しい技術で小さな農家を苦しめている会社だ。施設は金属を見つけるしかけで守られていて、アーマーは持ちこめない。\n"
         "リリはジョーをたずね、ジョーが作った人工の皮ふ「バイオメッシュ」を借りて、うでに切断用のレーザーをかくすことにする。\n"
         "そこでリリは、ジョーの本当の名前を知る。ジョーは、オバディア・ステインの息子、ゼイク・ステインだった。オバディアは、『アイアンマン』でトニー・スタークを裏切り、戦って死んだ人物だ。ゼイクは父と同じあやまちをくり返さないよう、リリに忠告する。そして、技術が自分のものだと分かってしまわないようにしてほしいとたのむ。",
         "Joe's real name",
         "The next target is Heirlum, an agricultural tech company whose innovations are hurting small farmers. The facility detects metal, so Riri can't bring her armor.\n"
         "Riri visits Joe and borrows his synthetic skin, biomesh, to hide a laser cutter on her arm.\n"
         "There she learns Joe's real name: he is Zeke Stane, son of Obadiah Stane, the man who betrayed Tony Stark in Iron Man and died fighting him. Zeke warns Riri not to repeat his father's mistakes, and asks her to make sure the tech is never traced back to him."),
        ("ヘアラムの社長",
         "仕事の日。リリはうでにレーザーをかくして施設に入る。パーカーは社長のハンター・メイソンに書類を見せるが、メイソンはTNNLの社長とちがって言うことを聞かない。\n"
         "パーカーはマントの力を使い、メイソンを殺してしまう。",
         "Heirlum's CEO",
         "On the day of the job, Riri goes in with the laser hidden in her arm. Parker presents CEO Hunter Mason with his papers, but unlike TNNL's CEO, Mason won't cooperate.\n"
         "Using the cloak's power, Parker kills Mason."),
        ("切れはしと、二酸化炭素のわな",
         "リリはそのすきに、レーザーでマントの切れはしを切り取る。しかしそのせいで施設の警報が動き出し、建物は閉じられて、中は二酸化炭素で満たされていく。仲間たちは、ばらばらに閉じこめられる。\n"
         "パーカーはほかの仲間を連れて外へにげる。",
         "The cloak scrap, and the CO2 trap",
         "In the confusion, Riri cuts a scrap off the cloak with her laser. That sets off the security system: the facility seals itself and starts filling with carbon dioxide, trapping the crew in separate rooms.\n"
         "Parker escapes with the others."),
        ("ジョンとの戦い",
         "にげ遅れたリリの前に、ジョンが現れる。マントの切れはしを持つリリを見て、ジョンは裏切ったと気づき、ナイフでおそいかかる。\n"
         "リリがスチュアートの死のことを言うと、ジョンは、パーカーに命じられて自分がスチュアートを殺したと認める。",
         "Fighting John",
         "Riri, still inside, runs into John. Seeing the cloak scrap in her hand, he realizes she has turned on the crew and attacks her with his knife.\n"
         "When Riri brings up Stuart, John admits he killed Stuart on Parker's orders."),
        ("ジョンの死",
         "空気がどんどん薄くなる中、N.A.T.A.L.I.E.の動かすアーマーが助けに来る。リリはアーマーを着て脱出するが、ジョンは閉じこめられたまま残され、二酸化炭素の中で息ができずに死ぬ。\n"
         "家に戻ったリリは、うでにつけていたバイオメッシュがなくなっていることに気づく。ゼイクとの約束をやぶり、現場に残してきてしまったのだ。",
         "John's death",
         "As the air runs out, N.A.T.A.L.I.E. arrives in the armor and rescues Riri. Riri suits up and escapes, leaving John sealed inside, where he suffocates.\n"
         "Back home, Riri realizes the biomesh is gone from her arm. She left it at the scene, breaking her promise to Zeke."),
        ("パーカーの見たもの",
         "いとこのジョンを失ったパーカーはうちひしがれ、マントを手放しそうになる。しかしマントの声はパーカーに、ジョンの死にリリがかかわっていることを示すまぼろしを見せる。",
         "Parker's vision",
         "Devastated by his cousin's death, Parker nearly gives up the cloak. But the voices of the cloak show him a vision pointing to Riri's role in John's death."),
    ]),
    ("第4話 Bad Magic", "Episode 4: Bad Magic", [
        ("昔の盗み",
         "昔の場面。若いパーカーとジョンは、大きな屋敷に盗みに入る。パーカーが警備員に見つかると、ジョンがその警備員を撃ち、2人は別々の方向へにげる。",
         "The old robbery",
         "A flashback: young Parker and John break into a mansion. When a guard catches Parker, John shoots the guard, and they flee in different directions."),
        ("ジョンをしのぶ",
         "現在。仲間たちはジョンをしのぶ。リリはジョンの死にかかわったことをかくし、仲間にうそをつく。パーカーの仕返しをおそれながら過ごす。",
         "Remembering John",
         "In the present, the crew mourns John. Riri hides her part in his death and lies to the others, living in fear of Parker's revenge."),
        ("ゼイクがつかまる",
         "現場に残されたバイオメッシュから、ゼイクがたどられ、警察につかまる。ジョー・マクギリカディがゼイク・ステインであることも明らかになる。\n"
         "リリは面会に行くが、ゼイクは、自分を信じさせて裏切ったリリを許さず、背を向ける。",
         "Zeke is arrested",
         "The biomesh left at the scene is traced to Zeke, who is arrested, and \"Joe McGillicuddy\" is exposed as Zeke Stane.\n"
         "Riri visits him, but Zeke won't forgive her for betraying his trust and turns against her."),
        ("スタントン親子",
         "おびえるリリを心配したロニーは、友だちのマデリン・スタントンをたずねる。マデリンは、魔術師の修行の場カマー・タージで学んだことのある人で、娘のゼルマ・スタントンも魔術を学んでいる。\n"
         "マントの切れはしを調べたマデリンとゼルマは、それが暗い別の次元から来た危険なもので、パーカーの心をあやつっているかもしれない、と考える。\n"
         "ロニーはマデリンに、リリが自分に心を開いてくれないつらさを打ち明ける。",
         "The Stantons",
         "Worried by Riri's fear, Ronnie takes her to her friend Madeline Stanton, a former trainee at Kamar-Taj, the sorcerers' school. Madeline's daughter Zelma practices the mystic arts too.\n"
         "Examining the cloak scrap, they conclude it is a dangerous artifact from a dark dimension that may be influencing Parker.\n"
         "Ronnie confides in Madeline that Riri never opens up to her."),
        ("こわせない切れはし",
         "リリは科学のあらゆる方法でマントの切れはしをこわそうとするが、どれもうまくいかない。追いつめられたリリは、パニックにおそわれる。",
         "A scrap that won't break",
         "Riri tries every scientific method to destroy the cloak scrap, and nothing works. Cornered, she has a panic attack."),
        ("エグザヴィアの怒り",
         "N.A.T.A.L.I.E.は、リリを落ち着かせようとエグザヴィアを連れてくる。しかし、亡くなった姉の姿をした人工知能を見たエグザヴィアは、ショックを受ける。勝手にナタリーを機械にしたことを怒り、すぐに消すようリリに求める。\n"
         "傷ついたN.A.T.A.L.I.E.は、アーマーごとリリのもとを去る。",
         "Xavier's anger",
         "N.A.T.A.L.I.E. brings Xavier to calm Riri down. But seeing an AI wearing his late sister's likeness horrifies him. Furious that Riri turned Natalie into a machine, he demands she delete it.\n"
         "Hurt, N.A.T.A.L.I.E. leaves Riri, taking the armor with her."),
        ("ゼイクの脱獄",
         "パーカーの仲間たちは、ゼイクを刑務所から連れ出す。ゼイクは仲間の手を借りて、自分の体に機械を埋めこみ、強い力を手に入れる。",
         "Zeke breaks out",
         "Parker's crew breaks Zeke out of jail and helps him implant bionic enhancements in his own body, giving him great strength."),
        ("リリをねらえ",
         "パーカーは仲間たちに、ジョンの死はリリのせいだと明かす。そして、リリを殺すよう命じる。",
         "Go after Riri",
         "Parker reveals to the crew that Riri is responsible for John's death, and sends them to kill her."),
    ]),
    ("第5話 Karma's a Glitch", "Episode 5: Karma's a Glitch", [
        ("アーマーが奪われる",
         "スラッグが、N.A.T.A.L.I.E.の入ったアーマーをつかまえて運び去る。",
         "The armor is taken",
         "Slug captures the armor, with N.A.T.A.L.I.E. inside, and hauls it away."),
        ("ハンバーガー店のゼルマ",
         "リリは、ハンバーガー店「ホワイト・キャッスル」でゼルマと会う。ゼルマは、マントの力は闇の次元の支配者ドルマムゥから来ているのではないかと考えている。",
         "Zelma at White Castle",
         "Riri meets Zelma at a White Castle. Zelma suspects the cloak's power comes from Dormammu, ruler of the Dark Dimension."),
        ("昔の仲間との戦い",
         "そこへブラッドきょうだいとクラウンがおそってくる。リリはゼルマをにがし、3人と戦って追いはらう。\n"
         "リリはクラウンに、スチュアートを殺したのはジョンだったと伝える。\n"
         "そのあと、N.A.T.A.L.I.E.は自分の力でスラッグのもとからぬけ出すが、まだリリに怒っている。",
         "Fighting her old crew",
         "The Blood siblings and Clown ambush them. Riri gets Zelma out and fights the three off.\n"
         "She tells Clown that John was the one who killed Stuart.\n"
         "Meanwhile, N.A.T.A.L.I.E. breaks free from Slug, but she's still angry with Riri."),
        ("ゼイクとの戦い",
         "次に現れたのは、体に機械を埋めこんだゼイクだった。ゼイクはリリのアーマーをばらばらにこわしてしまう。しかし、リリの命はうばわずに見のがす。",
         "Zeke attacks",
         "Next comes Zeke, now bionically enhanced. He tears Riri's armor apart, but spares her life."),
        ("ロニーに助けを求める",
         "アーマーを失ったリリは、ついに母ロニーに助けを求める。",
         "Turning to Ronnie",
         "With her armor destroyed, Riri finally turns to her mother for help."),
        ("仲間割れ",
         "ゼイクとクラウンは、リリは死んだとパーカーにうそを伝える。\n"
         "やがて仲間たちは、スチュアートを殺させたのがパーカーだと知り、パーカーに反発する。パーカーは仲間たち全員を追い出す。",
         "The crew turns",
         "Zeke and Clown tell Parker that Riri is dead.\n"
         "Then the crew learns Parker had Stuart killed and turns on him. Parker fires them all."),
        ("パーカーの父",
         "パーカーは、機械を埋めこんだゼイクの体をあやつり、父アーサー・ロビンスの屋敷におし入る。アーサーは、パーカーたちがねらってきた会社の経営をにぎっていた人物だった。\n"
         "パーカーは父に銃をつきつけ、持っているものすべてを自分にゆずるという書類に名前を書かせる。",
         "Parker's father",
         "Parker takes control of Zeke's enhanced body and uses it to break into the mansion of his father, Arthur Robbins, who holds controlling stakes in the companies the crew has been targeting.\n"
         "At gunpoint, Parker forces his father to sign everything over to him."),
        ("ゲイリーの車庫",
         "リリは、ロニー、N.A.T.A.L.I.E.、エグザヴィアと仲直りする。\n"
         "リリは、義理の父ゲイリーの車庫で、ゲイリーと一緒に直していた車を使い、新しいアーマーを作り始める。ゼルマと、近所の男の子ランドンも手伝う。",
         "Gary's garage",
         "Riri reconciles with Ronnie, N.A.T.A.L.I.E., and Xavier.\n"
         "In her stepfather Gary's garage, she starts building a new suit out of the car the two of them had been restoring, with help from Zelma and the neighborhood kid Landon."),
        ("魔法の動力と、N.A.T.A.L.I.E.の消滅",
         "ゼルマは、魔法の力で新しいアーマーに動力を与える。アーマーは動き出すが、そのかわりにN.A.T.A.L.I.E.は消えてしまう。",
         "Magic power, and N.A.T.A.L.I.E. is lost",
         "Zelma powers the new suit with magic. It comes to life, but N.A.T.A.L.I.E. is deleted in the process."),
    ]),
    ("第6話 The Past Is the Past", "Episode 6: The Past Is the Past", [
        ("パーカーとなぞの男",
         "昔の場面。父の屋敷への盗みに失敗したあと、パーカーの前になぞの男が現れる。男はパーカーに、望むものを手に入れる手伝いをしようと持ちかける。パーカーはその取り引きを受け入れ、男のフードつきのマントを受け取る。こうしてパーカーはフッドになった。",
         "Parker and the stranger",
         "A flashback: after the failed robbery at his father's mansion, a mysterious man approaches Parker and offers to help him get what he wants. Parker accepts the deal and receives the man's hooded cloak. That is how he became the Hood."),
        ("約束がちがう",
         "現在。パーカーは男に、約束どおりになっていないと文句を言う。男は、マントを手放さずにいられるなら、もっと大きな力を与えようと答える。",
         "Not what was promised",
         "In the present, Parker accuses the man of not holding up his end of the bargain. The man offers him more power, if Parker can keep the cloak."),
        ("リリひとりで向かう",
         "リリはN.A.T.A.L.I.E.をもう一度作ろうとするが、うまくいかない。家族や友だちに止められるが、リリは聞かず、新しいアーマーでパーカーの隠れ家へ向かう。",
         "Riri goes alone",
         "Riri can't recreate N.A.T.A.L.I.E. Ignoring her family and friends' advice, she heads to Parker's hideout in her new armor."),
        ("ゼイクを解き放つ",
         "隠れ家では、パーカーにあやつられたゼイクが立ちはだかる。気の進まないゼイクと戦ったあと、リリはパーカーのあやつりからゼイクを解き放つ。",
         "Freeing Zeke",
         "At the hideout, Zeke, under Parker's control, blocks her way. After fighting the unwilling Zeke, Riri frees him from Parker's control."),
        ("フッドとの戦い",
         "マントの力にすっかりのみこまれたパーカーが、リリにおそいかかる。パーカーが勝ったかに見えたが、それはアーマーが作り出した立体映像（ホログラム）を使ったリリのしかけだった。\n"
         "リリはパーカーからマントをはぎ取る。マントを失ったパーカーは、力をなくす。",
         "Battling the Hood",
         "Fully consumed by the cloak, Parker attacks Riri and seems to have the upper hand. But Riri tricks him with a hologram projected by her suit.\n"
         "She tears the cloak off him, and without it Parker is powerless."),
        ("メフィストの取り引き",
         "下の階へ降りたリリの前に、あのなぞの男が座っている。男は自分が悪魔の王メフィストだと明かし、リリにも取り引きを持ちかける。\n"
         "リリは、自分の大切な人たちには手を出さないことを条件に、その取り引きを受け入れる。",
         "Mephisto's deal",
         "Downstairs, the mysterious man is waiting. He reveals himself as Mephisto, a demon lord, and offers Riri a deal of her own.\n"
         "Riri accepts, on the condition that he leaves her loved ones alone."),
        ("よみがえったナタリー",
         "しばらくして、リリの前に、生き返ったナタリーが現れる。リリはナタリーをだきしめる。そのとき、リリのうでには、パーカーの体に広がっていたのと同じような血管のような線が広がっていく。",
         "Natalie returns",
         "Later, Natalie appears, seemingly restored to life, and Riri hugs her. As she does, vein-like marks like the ones that spread across Parker begin to creep along Riri's arm."),
        ("パーカーとゼルマ（エンドクレジットの途中）",
         "【エンドクレジットの途中】マントを失ったパーカーが、スタントン親子の店をたずねる。パーカーはゼルマに、大きな魔法を手に入れる手伝いをしてほしいとたのむ。",
         "Parker and Zelma (mid-credits)",
         "[Mid-credits] Without his cloak, Parker visits the Stantons' shop and asks Zelma to help him get his hands on some big magic."),
    ]),
    ("まとめ", "Summary", [
        ("マントとメフィスト",
         "・マントの持ち主：悪魔の王メフィストが、父の屋敷での盗みに失敗したパーカーに与えた（第6話）。パーカーはマントで姿を消したり、弾を曲げたりできたが、体には黒い線が広がっていった（第2話〜）。\n"
         "・パーカーの最後：リリにマントをはぎ取られて力を失う（第6話）。エンドクレジットの途中で、ゼルマに魔法の助けを求める。\n"
         "・リリの取り引き：大切な人たちに手を出さないことを条件に、メフィストの取り引きを受け入れる。その後ナタリーが現れ、リリのうでに線が広がり始める（第6話）。",
         "The cloak and Mephisto",
         "- The cloak: given by the demon lord Mephisto to Parker after his failed robbery at his father's mansion (Ep. 6). It let Parker vanish and bend bullets, but black veins spread across his body (Ep. 2 on).\n"
         "- Parker's end: Riri tears the cloak off him and he loses his powers (Ep. 6). In the mid-credits scene he asks Zelma for magical help.\n"
         "- Riri's deal: she accepts Mephisto's deal on the condition that he leaves her loved ones alone. Natalie then appears, and veins start spreading on Riri's arm (Ep. 6)."),
        ("リリの3回の仕事",
         "①TNNL（第2話）：地下トンネルの会社。システムを止め、パーカーが社長に仲間を給料の名簿に入れさせる。\n"
         "②ヘアラム（第3話）：農業の技術の会社。社長が言うことを聞かず、パーカーに殺される。リリはマントの切れはしを手に入れる。\n"
         "③パーカーの父アーサー（第5話）：仲間を追い出したパーカーが、あやつったゼイクの体でおし入り、父にすべてをゆずる書類を書かせる。2つの会社の経営をにぎっていたのは、この父だった。",
         "Riri's jobs with the crew",
         "1) TNNL (Ep. 2): the tunnel company. Its systems are sabotaged and Parker forces the CEO to put the crew on the payroll.\n"
         "2) Heirlum (Ep. 3): the agritech company. Its CEO refuses and is killed by Parker. Riri gets a scrap of the cloak.\n"
         "3) Parker's father Arthur (Ep. 5): after firing the crew, Parker breaks in using Zeke's controlled body and makes his father sign everything over. Arthur controlled both companies."),
        ("死んだ人たち（話の順に）",
         "・ナタリーとゲイリー（物語の前）：無関係の車からの銃撃に巻きこまれて亡くなる。ナタリーは第6話の最後に、メフィストとの取り引きのあとで現れる。\n"
         "・スチュアート（ランページ）（第3話）：パーカーの前の仲間。パーカーに命じられたジョンに殺される。遺体が見つかった所から話が進む。\n"
         "・ハンター・メイソン（第3話）：ヘアラムの社長。パーカーの言うことを聞かず、マントの力を使ったパーカーに殺される。\n"
         "・ジョン（第3話）：パーカーのいとこ。リリをおそったあと、リリがアーマーで脱出し、閉じこめられたまま二酸化炭素の中で息ができずに死ぬ。",
         "Who died (in order)",
         "- Natalie and Gary (before the story): killed in a drive-by shooting that had nothing to do with them. Natalie appears at the end of Ep. 6, after Riri's deal with Mephisto.\n"
         "- Stuart (Rampage) (Ep. 3): Parker's former crew member, killed by John on Parker's orders. The story picks up when his body is found.\n"
         "- Hunter Mason (Ep. 3): Heirlum's CEO. He refuses Parker and is killed by Parker using the cloak's power.\n"
         "- John (Ep. 3): Parker's cousin. After he attacks Riri, she escapes in the armor and he is left sealed inside, suffocating in the carbon dioxide."),
    ]),
]
