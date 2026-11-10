# 『ヴィジョンクエスト』シーンごとの詳しいあらすじ（配信中。第8話は films.py の upcoming に「未公開」とだけ出す）
# 2026-11-10 英語版ウィキペディアの各話のあらすじと、各話の解説記事（英語・日本語）を照らし合わせて、くわしい形に書き直した。
# 運営者の希望: 第1話から始め、場面ごとに起きた事実だけを書く。見出しはつながった場面でまとめる。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
# 資料どうしで食い違う所（第2話でパラディンと会う場所、ジョーの死因、第3話で契約が切られる順番など）は書いていないか、ぼかしてある。
# 最終話（第8話）が配信されたら、第8話と最後の「まとめ」の章を足す。
SCENE_NUMBERS = True  # 場面に「話-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1話「ノー・ストリングス」（10月13日配信）", "Episode 1: No Strings (Oct. 13)", [
        ("ヴィジョンのこれまでと、エディンバラのパブ",
         "ヴィジョンが、自分のこれまでを語る。ウルトロンとの戦いの中で生まれ、ワンダと出会い、サノスに殺された。そのあと政府の組織ソードが体を白く作り直し、ワンダの町で元の記憶を受けとって飛び去った。\n"
         "今のヴィジョンは人間の姿になり、「シャーウッド・エリス」という名前で、スコットランドのエディンバラにあるパブ「オールド・セルキー」で働いている。昔、ワンダと一緒に通った店だ。テーブルには、ハートの中に「W」と「V」と彫ったあとが残っている。\n"
         "店の主人フィオナは、ヴィジョンを気にかけている。ワンダのことを聞かれると、ヴィジョンは、山の下じきになったとだけ答える。日曜の夕食にさそわれても、人づきあいが苦手だからと断る。",
         "Vision's story so far, and a pub in Edinburgh",
         "Vision recounts his history: born during the fight against Ultron, he met Wanda and was killed by Thanos. The agency S.W.O.R.D. then rebuilt his body in white, and in Wanda's town he received his old memories and flew away.\n"
         "Now he wears a human face, goes by Sherwood Ellis, and works at the Old Selkie, a pub in Edinburgh, Scotland, that he and Wanda used to visit. A heart with a W and a V is still carved into one of the tables.\n"
         "The owner, Fiona, looks out for him. When she asks about Wanda, he says only that she was crushed under a mountain. He turns down her invitation to Sunday dinner, saying he isn't good with people."),
        ("心の中の屋敷とAIたち",
         "夜になると、ヴィジョンは自分の心の中にある屋敷（マインドスペース）に入る。そこには、トニー・スタークが作ったAIたちが、人間の姿で暮らしている。\n"
         "ジャーヴィスは屋敷の守り、フライデーは人づきあいの相談、イーディスは遊びと武器、ダミーとユーは修理の係だ。みんなで、ヴィジョンが人間らしくふるまえるように手伝っている。\n"
         "ジャーヴィスは、どこかから情報がもれているようだと注意する。しかしヴィジョンは気にとめない。",
         "The house in his mind and the AIs",
         "At night Vision enters a mansion inside his own mind, the Mindspace, where the AIs Tony Stark built live in human form.\n"
         "J.A.R.V.I.S. handles security, F.R.I.D.A.Y. coaches him on dealing with people, E.D.I.T.H. covers fun and weapons, and D.U.M.-E. and U. do the repairs. Together they help Vision act more human.\n"
         "J.A.R.V.I.S. warns that data seems to be leaking somewhere, but Vision brushes it off."),
        ("映写室と、屋根裏のウルトロン",
         "ヴィジョンは屋敷の映写室で、昔の自分の記憶を映画のように見直し、気持ちというものを理解しようとしている。ただ、ワンダの魔法の町ウエストビューで暮らしたヴィジョンの記憶だけは、本物ではないと考えて見ようとしない。\n"
         "ところが、ダミーとユーがウルトロンにそそのかされ、ウエストビューでの息子たちの映像を流してしまう。ヴィジョンは怒る。\n"
         "ウルトロンは、屋敷の屋根裏に閉じこめられている。そこでインターネットを見たり、絵を描いたりして過ごしている。ヴィジョンは、ここでは人間の姿でいるようウルトロンに命じる。\n"
         "ウルトロンは、ヴィジョンが言うことを聞くAIたちの後ろに隠れて、本当の気持ちから逃げていると言う。そして、世界をながめていれば世界のほうにも気づかれると忠告し、屋根裏から伝書バトを飛ばす。",
         "The screening room, and Ultron in the attic",
         "In the mansion's screening room, Vision rewatches his former self's memories like films, trying to understand feelings. But he refuses to watch the memories of the Vision who lived in Wanda's magical town of Westview, believing they weren't real.\n"
         "Egged on by Ultron, D.U.M.-E. and U. play footage of his sons in Westview anyway, and Vision is furious.\n"
         "Ultron is locked in the mansion's attic, where he spends his time online and painting. Vision orders him to stay in human form there.\n"
         "Ultron says Vision is hiding from real feeling behind AIs that do as they're told. He warns that if you watch the world, the world starts watching back, and he releases a carrier pigeon from the attic."),
        ("パブの襲撃とフィオナの死",
         "次の夜、パブの窓の外から弾が飛びこみ、フィオナの胸に当たる。フィオナはその場で亡くなる。撃ったのは、ヴィジョンを捕まえに来た賞金稼ぎパラディンの部下たちで、フィオナは巻きぞえになった。\n"
         "武器を持った男たちが店になだれこむ。ヴィジョンは男たちを倒し、天窓から逃げる。\n"
         "パラディンは、助手のAI（ハンドラー）と連絡を取っている。そこへ、声を変えた「依頼人」が割りこんでくる。依頼人はソードの暗号を使っていて、ヴィジョンを逃がしたことに不満を示す。パラディンは、必ず捕まえると答える。",
         "The attack on the pub and Fiona's death",
         "The next night a bullet comes through the pub window and hits Fiona in the chest, killing her on the spot. It was fired by men working for Paladin, a bounty hunter sent to capture Vision; Fiona was caught in the crossfire.\n"
         "Armed men storm the pub. Vision takes them down and escapes through the skylight.\n"
         "Paladin is talking to his AI assistant, the Handler, when the Client cuts in with a disguised voice. Using S.W.O.R.D. encryption, the Client is unhappy that Vision got away. Paladin promises to bring him in."),
        ("ウルトロンの裏切り",
         "心の中の屋敷で、ジャーヴィスはヴィジョンに、フィオナの死を悲しむ時間を取るようにすすめる。しかしヴィジョンは、それほど親しい相手ではなかったと言いはる。\n"
         "AIたちは、居場所を外にもらしたのがウルトロンだったことを突き止める。ウルトロンは闇のインターネットでヴィジョンにかけられた賞金を見つけ、パラディンに居場所を教えていた。\n"
         "問いつめられたウルトロンは、あっさり認める。ヴィジョンを外の世界に押し出すためだったと言う。\n"
         "ヴィジョンは罰として、屋根裏からテレビや絵の道具、ソファを取り上げる。ウルトロンは何もない部屋に残される。",
         "Ultron's betrayal",
         "In the Mindspace, J.A.R.V.I.S. urges Vision to take time to grieve for Fiona, but Vision insists they weren't that close.\n"
         "The AIs work out that the leak was Ultron. He had found a bounty on Vision on the dark web and told Paladin where to find him.\n"
         "Confronted, Ultron admits it freely, saying he did it to push Vision out into the world.\n"
         "As punishment, Vision strips the attic of its TVs, painting supplies and couch, leaving Ultron in an empty room."),
        ("ロンドンのトミーとリサ",
         "パラディンとハンドラーは、ヴィジョンの偽名からウエストビューの事件にたどり着く。ソードの記録を調べ、ヴィジョンの息子の名前「トミー」と結びつく少年を見つける。\n"
         "ロンドン。18歳のトーマス・シェパード（トミー）は、スリが得意な相棒のリサと、人をだましてお金を取って暮らしている。\n"
         "店のテレビに、ヴィジョンが現れたというニュースが流れる。それを見たトミーの頭に、覚えのない記憶が次々によみがえり、息が苦しくなる。だまされたと気づいた相手に追いかけられ、2人は逃げる。リサがトミーを落ち着かせる。",
         "Tommy and Lisa in London",
         "Paladin and the Handler trace Vision's alias back to the Westview incident. Digging through S.W.O.R.D. records, they find a boy linked to the name of Vision's son, Tommy.\n"
         "In London, 18-year-old Thomas Shepherd (Tommy) gets by running cons with his partner Lisa, a skilled pickpocket.\n"
         "A news report about the Vision sighting plays on a pub TV. Memories he can't explain flood Tommy's head and he struggles to breathe. Their mark realizes he's been conned and chases them; they get away, and Lisa calms Tommy down."),
        ("パラディンの知らせ",
         "路地で、パラディンがトミーとリサを待ちぶせし、トミーを連れ去る。\n"
         "パラディンは、ヴィジョンの心の中に直接メッセージを送りつける。お前の息子を預かった、という知らせだ。\n"
         "一緒に送られてきたのは、警察で話を聞かれるトミーの映像だった。トミーは、「ワンダ」と呼ばれていた母親のことを覚えていると話している。",
         "Paladin's message",
         "Paladin ambushes Tommy and Lisa in an alley and takes Tommy.\n"
         "He then sends a message straight into Vision's mind: he has Vision's son.\n"
         "With it comes footage of Tommy being interviewed by police, saying he remembers a mother who was called Wanda."),
    ]),
    ("第2話「テセウス」（10月13日配信）", "Episode 2: Theseus (Oct. 13)", [
        ("1年前　プールの事件",
         "1年前。トミーは警察で話を聞かれている。プールでほかの子どもたちにけがをさせたと疑われていた。\n"
         "トミーはおびえながら、自分でも止められなかったと話す。水の中に沈められておぼれかけたとき、雷に打たれたように感じ、頭の中に別の誰かが入ってきたようだったと言う。\n"
         "それ以来トミーには、ワンダとヴィジョンの息子として暮らした記憶がある。",
         "A year earlier: the pool",
         "A year earlier, Tommy is being questioned by police, suspected of hurting other kids at a swimming pool.\n"
         "Frightened, he says he couldn't control it. Held underwater and nearly drowning, he felt something like a bolt of lightning, as if someone else had moved into his head.\n"
         "Ever since, he has had memories of living as Wanda and Vision's son."),
        ("護送バスからの脱走",
         "クリスマスの日。トミーは、セント・メイビンズ精神療養所へ向かう護送バスに乗せられる。となりに座ったのがリサだった。トミーは、母を亡くして里親のもとで育ったと話す。\n"
         "行き先を知った別の乗客がさわぎ出し、見張りの男が電気ショックの道具で押さえつける。かばおうとしたトミーにも電気が当てられる。するとトミーの力が目覚め、電気ははね返って見張りを倒す。\n"
         "リサは見張りからカギをぬき取る。トミーは手をふるわせる力で後ろのドアの留め具を外し、2人はバスから飛び降りる。ほかの乗客たちは、クリスマスの歌を歌って物音をごまかす。\n"
         "それから1年、2人はロンドンで一緒に暮らしてきた。",
         "Escape from the transport bus",
         "On Christmas Day, Tommy is put on a transport bus bound for Saint Mabyn's Psychiatric Sanitarium. Lisa sits down beside him. He tells her he lost his mother and grew up in foster care.\n"
         "Another passenger panics about where they're headed, and the guard subdues him with a stun weapon. When Tommy tries to shield him, the guard shocks Tommy too. That awakens Tommy's power, and the charge rebounds and drops the guard.\n"
         "Lisa lifts the guard's keys. Tommy vibrates the bolts off the back door and the two jump out, while the other passengers sing Christmas carols to cover the noise.\n"
         "For the year since, the two have lived together in London."),
        ("現在　パラディンという名前",
         "現在。ヴィジョンは古い電器店に身をひそめている。\n"
         "AIたちが調べると、「パラディン」は一人の名前ではなく、賞金稼ぎたちが何代にもわたって受けついできた名前だった。一度引き受けた契約は決して破らないという。\n"
         "ジャーヴィスは、プールの事件の記録を見つける。パラディンが送ってきた映像の中で、トミーは、歌ったり本を読んだりしてくれた母ワンダと、赤い顔でやさしい目をした父のことを語っていた。昔ヴィジョンがワンダにかけた、悲しみと愛についての言葉まで口にする。\n"
         "それでもヴィジョンは、この少年を自分の息子だとは認めない。",
         "The present: the name Paladin",
         "In the present, Vision is hiding in an old electronics shop.\n"
         "The AIs learn that Paladin is not one man's name but a title handed down through generations of bounty hunters, who never break a contract once it's accepted.\n"
         "J.A.R.V.I.S. finds the record of the pool incident. In the footage Paladin sent, Tommy describes a mother, Wanda, who sang and read to him, and a father with a red face and kind eyes. He even repeats what Vision once told Wanda about grief and love.\n"
         "Vision still refuses to accept the boy as his son."),
        ("パラディンとの対面",
         "ヴィジョンはパラディンと向き合う。パラディンはトミーを人質にして、おとなしく捕まるよう求める。\n"
         "ヴィジョンは動じない。自分は何も感じない、前のヴィジョンとはちがうのだと告げ、取引に応じずに立ち去る。",
         "Face to face with Paladin",
         "Vision meets Paladin, who uses Tommy as a hostage and demands his surrender.\n"
         "Vision is unmoved. He says he feels nothing and is not the Vision who came before, and he leaves without making a deal."),
        ("ウルトロンと「テセウスの船」",
         "屋敷でヴィジョンはウルトロンと話す。前のヴィジョンの記憶はあるが、気持ちはない。あの少年は前のヴィジョンの息子で、自分にあるのは受けついだ務めだけだと言う。\n"
         "話は「テセウスの船」のことになる。部品をすべて取りかえた船は、元と同じ船と言えるのか、という昔からの問いだ。ウルトロンはその考えをはねつける。そして、息子をさらわれたのなら船でいるな、王になれ、とヴィジョンに言う。\n"
         "ジャーヴィスは、居間にかかっている炎に包まれた人の絵を指して止める。はげしい感情は命取りになるという教えだ。それでもヴィジョンは、トミーを助けに行くと決める。",
         "Ultron and the ship of Theseus",
         "In the mansion, Vision talks with Ultron. He has the former Vision's memories but not his feelings; the boy is that Vision's son, he says, and all he himself has is an inherited duty.\n"
         "They turn to the ship of Theseus, the old question of whether a ship with every part replaced is still the same ship. Ultron dismisses the idea and tells Vision that when someone has taken your son, you don't be the ship, you be the king.\n"
         "J.A.R.V.I.S. tries to stop him, pointing to the painting of a burning figure in the sitting room, a lesson that strong emotion can be fatal. Vision decides to go after Tommy anyway."),
        ("セント・メイビンズの罠",
         "ヴィジョンはセント・メイビンズ精神療養所に、正面から入っていく。本物の職員はパラディンの部下たちに殺されていて、中で待っていたのは武器を持った男たちだった。ヴィジョンはAIたちに支えられながら、男たちを倒して進む。\n"
         "クッションばりの部屋で、トミーがいすにしばりつけられている。おびえたトミーは、ヴィジョンは本物じゃないと言う。ヴィジョンはトミーを落ち着かせ、しばっていたものを外す。\n"
         "そのときドアが閉まる。部屋は、機械をくるわせる電磁パルス（EMP）のおりだった。ヴィジョンの体は弱り、力がうまく使えなくなる。2人は力を合わせてドアを破り、外へ出る。",
         "The trap at Saint Mabyn's",
         "Vision walks into Saint Mabyn's through the front door. Paladin's men have killed the real staff, and armed mercenaries are waiting inside. With the AIs backing him up, Vision fights his way through.\n"
         "He finds Tommy strapped to a chair in a padded room. Terrified, Tommy says Vision isn't real. Vision calms him and frees him.\n"
         "Then the door locks. The room is an EMP cage built to scramble machines, and Vision weakens and can barely use his powers. Together they break the door down and get out."),
        ("アダマンチウムの弾と、ジャーヴィスの最期",
         "外ではパラディンが待っていた。銃には、ヴィジョンの体もつらぬくアダマンチウムという金属の弾がこめてある。撃たれたヴィジョンは深い傷を負う。\n"
         "ヴィジョンはトミーに、自分を置いて逃げるように言う。トミーは、ヴィジョンは自分にとって大事な何かなのだと言っていやがるが、最後には走り去る。\n"
         "ヴィジョンの体は力がつきかけ、心の中のAIたちも一緒に消えそうになる。ジャーヴィスは、自分のプログラムを自分で消し、その分の力をヴィジョンとほかのAIたちに回す。最後の言葉は「家族は永遠、戦うに値する」。こうしてジャーヴィスは消える。\n"
         "そこへ、トミーが古い車を運転して戻ってくる。ヴィジョンを乗せ、2人はパラディンから逃げきる。助手席のヴィジョンのそばで、ウルトロンは、言うことを聞かない所が父親そっくりだと言う。",
         "Adamantium rounds, and J.A.R.V.I.S.'s end",
         "Paladin is waiting outside, his gun loaded with rounds of adamantium, a metal that can pierce even Vision's body. Vision is shot and badly wounded.\n"
         "He tells Tommy to leave him and run. Tommy resists, saying Vision is his something, but in the end he runs.\n"
         "Vision's power is nearly gone, and the AIs in his mind are about to fade with him. J.A.R.V.I.S. deletes his own program to reroute its power to Vision and the others. His last words are \"Family is forever, and it's worth the fight.\" And he is gone.\n"
         "Then Tommy comes back at the wheel of an old car. He gets Vision inside and they escape Paladin. Beside Vision in the car, Ultron remarks that the boy's stubbornness is just like his father's."),
    ]),
    ("第3話「リブート」（10月20日配信）", "Episode 3: Reboot (Oct. 20)", [
        ("ブッチャーバードの事件",
         "ウルトロンは屋根裏で絵を描きながら、ニュースを見ている。技術の会社の大物が次々に殺される事件で、2人目の被害者が出たという。現場には鳥の翼のような模様がきざまれていて、犯人は「ブッチャーバード」と呼ばれている。\n"
         "高いビルの部屋で、同じニュースを見ていた男が銃を手に取る。警備の仕組みが止まり、エレベーターのドアが開く。黒い布をかぶり、目を赤く光らせた人影が入ってくる。男は撃つが、人影は止まらない。",
         "The Butcherbird killings",
         "Painting in his attic, Ultron watches the news: a second victim in a string of murders of tech-industry figures. Wing-like marks are carved at each scene, and the killer has been dubbed the Butcherbird.\n"
         "In a high-rise, a man watching the same report grabs a shotgun. His security system shuts down and the elevator opens. A figure in a black robe with glowing red eyes steps out. He fires, but the figure keeps coming."),
        ("車の中の応急手当",
         "トミーは車を走らせ、どうすれば助けられるかをたずねる。ヴィジョンは、自分を直せるのはブルース・バナー博士とトニー・スタークくらいだが、どちらも頼れないと答える。\n"
         "心の中では、フライデーとイーディスが、力がもれるのを止めようと必死に作業している。\n"
         "ヴィジョンは車を止めさせ、車のバッテリーから取り出した硫酸で傷口をふさぐ。ひとまず危ない状態はぬける。\n"
         "一方パラディンも傷を負っていた。それでもハンドラーに指示を出し、ヴィジョンの体からもれた跡をドローンに追わせる。",
         "First aid in the car",
         "As he drives, Tommy asks how he can help. Vision says the only people who could repair him are Dr. Bruce Banner and Tony Stark, and neither can be reached.\n"
         "Inside his mind, F.R.I.D.A.Y. and E.D.I.T.H. work frantically to stop his power from draining away.\n"
         "Vision has Tommy pull over and seals the wound with sulfuric acid from the car battery, which gets him past the immediate danger.\n"
         "Paladin is hurt too. Even so, he has the Handler send drones to follow the trail leaking from Vision's body."),
        ("モーテルの夜",
         "2人は古いモーテルに入る。ヴィジョンの体からもれる力のせいで、まわりの電気がおかしくなり、ATMまでくるい出す。トミーは出てきた現金を持っていく。\n"
         "プールのポスターを見たトミーは、おぼれたときのことを思い出して固まる。部屋では古いテレビ番組を見て気持ちを落ち着ける。\n"
         "トミーは、自分がどうしてヴィジョンとワンダの息子でありえるのかを知りたがる。ヴィジョンは心の中で、どう伝えるかを何度もためしてみる。記憶は本物ではない、家族がほしくて頭が作り出したものだ、と正直に言うと、どの場合もトミーは怒って出ていってしまう。\n"
         "ウルトロンは、そのぶっきらぼうな言い方がトミーを遠ざけているのだと言う。結局ヴィジョンは答えを出せず、トミーは部屋を出ていく。",
         "A night at the motel",
         "They check into a run-down motel. The power leaking from Vision plays havoc with the electricity, even setting off an ATM, and Tommy helps himself to the cash.\n"
         "A poster for the swimming pool makes Tommy freeze as he remembers drowning. In the room he calms himself by watching old TV shows.\n"
         "Tommy wants to know how he could possibly be Vision and Wanda's son. In his head, Vision rehearses the conversation again and again. Each time he bluntly says the memories aren't real, that Tommy's mind made them up out of longing for a family, Tommy storms out.\n"
         "Ultron tells him that this blunt way of telling the truth is what pushes Tommy away. In the end Vision can't find an answer, and Tommy leaves the room."),
        ("手のけがと、トミーの打ち明け話",
         "ろうかの自動販売機で、買ったものが引っかかる。いら立ったトミーの手はガラスをすりぬけ、けがをする。\n"
         "ヴィジョンはトミーの手に包帯を巻く。ボクシングの話でごまかそうとするが見ぬかれ、本当にこわいのは、自分が何のためにいるのか分からないまま終わることだと打ち明ける。\n"
         "トミーもプールの日のことを話す。ほかの子たちに水の中へ押さえつけられ、おぼれて、息を吹き返した。そのとき体じゅうがものすごい速さでふるえ、プールの水がわき立ち、まわりの子どもたちをこわがらせた。それ以来、水も自分の力もこわいと言う。\n"
         "物をすりぬける力は、ヴィジョンが持っていた力と同じだった。\n"
         "心の中では、フライデーがヴィジョンのプログラムを書きかえながら、トニーが死ぬのを見ていることしかできなかった後悔を口にする。",
         "A hurt hand, and Tommy opens up",
         "In the hallway, Tommy's snack gets stuck in a vending machine. In his frustration his hand passes right through the glass, and he hurts it.\n"
         "Vision bandages the hand. He tries small talk about boxing, but Tommy sees through it, and Vision admits that what really frightens him is ending without ever understanding his purpose.\n"
         "Tommy describes the day at the pool. Other kids held him under; he drowned and was revived. His whole body vibrated at terrific speed, the pool water boiled, and it terrified the kids around him. Since then he has feared both water and his own power.\n"
         "His ability to pass through things is one that Vision himself once had.\n"
         "Inside Vision's mind, F.R.I.D.A.Y. rewrites his code and admits she is haunted by having only been able to watch Tony die."),
        ("パラディンとブッチャーバード",
         "パラディンは跡をたどって、高いビルの部屋に着く。そこには男の死体があり、床に翼の模様がきざまれていた。\n"
         "黒い布の人影、ブッチャーバードが現れ、誰に雇われたのかをパラディンに問いただす。ブッチャーバードはヴィジョンと同じ、人の手で作られた体を持つ存在だった。パラディンの頭の中をのぞき、子どものころの記憶を見る。\n"
         "パラディンの父は、息子を弱いと言って乱暴する男だった。その父を撃ち殺したのが前の代のパラディンで、残された少年を引き取って育てた。ブッチャーバードは、血のつながらないお前は本物のパラディンではないと言い放つ。\n"
         "パラディンはドローンをぶつけ、そのすきに逃げる。しかし依頼人は、失敗を重ねたパラディンとの契約を打ち切る。ただでも続けるという申し出も断られる。",
         "Paladin and the Butcherbird",
         "Following the trail, Paladin reaches the high-rise apartment. The man is dead, and wings are carved into the floor.\n"
         "The robed figure, the Butcherbird, appears and demands to know who hired him. Like Vision, she is a being with a manufactured body. She reads Paladin's mind and sees a childhood memory.\n"
         "His father was a violent man who called him weak. The previous Paladin shot that father dead, then took the boy in and raised him. The Butcherbird tells him that, with no blood tie, he is not the real Paladin.\n"
         "Paladin throws his drones at her and escapes in the confusion. But after one failure too many, the Client ends his contract, and even his offer to keep working for free is refused."),
        ("プールでの再起動",
         "ヴィジョンの体の働きが次々に止まりはじめ、残された時間は少ない。助かる道は、いったん完全に電源を落とし、大きな力で再び起動することだけだ。熱を冷ますために、モーテルのプールを使う。\n"
         "力を出せるのはトミーしかいない。ヴィジョンは、自分はまちがっていたと認め、トミー・マキシモフは本物だとトミーに伝える。\n"
         "ヴィジョンはプールの水に沈み、動きを止める。トミーはこわさを乗りこえて水に入り、手を速くふるわせて力を送りこむ。ヴィジョンは目を開ける。あたりは停電になる。",
         "The reboot in the pool",
         "Vision's systems begin failing one by one and time is short. The only way out is to shut him down completely and restart him with a huge surge of power, using the motel pool to cool him.\n"
         "Only Tommy can supply that power. Vision admits he was wrong and tells him that Tommy Maximoff is real.\n"
         "Vision sinks into the pool and goes still. Tommy overcomes his fear, gets into the water and vibrates his hands at speed to drive power into him. Vision opens his eyes. The area is blacked out."),
        ("ジャーヴィスの葬式と、侵入者",
         "屋敷では、AIたちがジャーヴィスの葬式を開く。ダミーが別れの言葉を読み、ユーが歌う。ヴィジョンも兄のような存在だったジャーヴィスに別れを告げる。ウルトロンは、ヴィジョンはまだ愛を分かっていないと言う。\n"
         "そのとき屋敷の明かりが赤く変わり、警報が鳴る。再起動のときの大きな力に気づいたブッチャーバードが、ヴィジョンの頭の中につながってきたのだ。\n"
         "そして聞きなれない声が、ヴィジョンにあいさつをする。",
         "J.A.R.V.I.S.'s funeral, and an intruder",
         "In the mansion, the AIs hold a funeral for J.A.R.V.I.S. D.U.M.-E. reads a farewell and U. sings. Vision says goodbye to the AI who was like an older brother to him. Ultron remarks that Vision still doesn't understand love.\n"
         "Then the lights turn red and an alarm sounds. The Butcherbird, alerted by the surge of the reboot, has connected to Vision's mind.\n"
         "And an unfamiliar voice greets Vision."),
    ]),
    ("第4話「マルウェア」（10月20日配信）", "Episode 4: Malware (Oct. 20)", [
        ("ブッチャーバードを追い出す",
         "ブッチャーバードは、ヴィジョンの心と体に入りこむ。そして、自分のじゃまをしなければヴィジョンとトミーには手を出さない、じゃまをするならトミーをねらうと告げる。ヴィジョンは受け入れない。\n"
         "イーディスが力ずくでつながりを切り、ブッチャーバードを屋敷から追い出す。\n"
         "ヴィジョンは、この殺し屋を自分たちで探し出すと決める。",
         "Driving out the Butcherbird",
         "The Butcherbird gets into Vision's mind and body. She tells him that if he stays out of her way she will leave him and Tommy alone; if not, she will go after Tommy. Vision refuses.\n"
         "E.D.I.T.H. forcibly cuts the connection and throws her out of the mansion.\n"
         "Vision decides they will track the killer down themselves."),
        ("トミーへの説明と、言わなかったこと",
         "トミーは、ヴィジョンが見えない誰かと話していることに気づいていた。ヴィジョンは、頭の中にAIたちがいることを打ち明ける。ただし、AIは4人だと説明し、ウルトロンのことだけは言わない。\n"
         "トミーは、ソコヴィアという国で多くの人の命と家をうばったウルトロンをきらっている。ヴィジョンは、そのウルトロンが自分の中にいるとは言い出せない。",
         "What Vision tells Tommy, and what he leaves out",
         "Tommy has noticed Vision talking to people he can't see. Vision tells him about the AIs in his head, but says there are four of them and leaves out Ultron.\n"
         "Tommy despises Ultron for the lives and homes he destroyed in Sokovia, and Vision can't bring himself to say that Ultron is inside him."),
        ("事件を調べる",
         "ヴィジョンとウルトロンは、捜査官になりすまして警察の国際的な記録に入りこむ。途中で「私はロボットではありません」という確認にてこずる。\n"
         "殺された3人は、マークリッジ・バイオテックという会社の役員だった。世界で初めて、安定して動く人工の心を作った5人組の仲間だ。\n"
         "犯人は1人目から血を、2人目から指紋を、3人目から目をうばっていた。どれも、何かを開けるための本人確認のカギになる。\n"
         "5人組のリーダーだったジョセフィン（ジョー）・キャリントン博士は、2008年に亡くなっている。残る1人は社長のカテリーナ・ウェルズ。今夜、大きなパーティーを開く予定だった。",
         "Investigating the murders",
         "Posing as an investigator, Vision and Ultron break into international police files, struggling along the way with an \"I am not a robot\" check.\n"
         "The three victims were board members of a company called Markridge Biotech, part of a five-person team that built the world's first stable synthetic consciousness.\n"
         "The killer took blood from the first, fingerprints from the second and an eye from the third, each a biometric key for unlocking something.\n"
         "The team's leader, Dr. Josephine \"Jo\" Carrington, died in 2008. The only one left is the CEO, Katerina Wells, who is hosting a big gala that night."),
        ("パーティーへの潜入",
         "トミーはリサを呼び、これまでのことを話して力を借りる。\n"
         "会場の前で、ヴィジョンとトミーがイタリア語で大げんかのふりをして人の目を集める。そのすきに、リサが3人分の入場券をすり取る。3人は会場に入る。",
         "Getting into the gala",
         "Tommy calls Lisa, catches her up and asks for her help.\n"
         "Outside the venue, Vision and Tommy stage a loud argument in Italian to draw attention while Lisa lifts passes for all three of them, and they walk in."),
        ("イーディスが知ったこと",
         "イーディスはスターク社の古い記録を調べる。トニーのAIたちは、マークリッジ社がスターク社に売った技術をもとに作られていた。\n"
         "しかも、AIたちにはそれぞれ、モデルになった本物の人間がいた。ジャーヴィスは執事のエドウィン・ジャーヴィス、フライデーはアリソン・ホーガン、イーディスはイーディス・マークスという女性だ。イーディス・マークスは、夫を飛行機の事故で亡くしていた。\n"
         "自分は誰かの写しなのかと、イーディスは動揺する。ウルトロンは、自分なりのイーディスでいればいいとなぐさめる。ウルトロン自身には、モデルになった人はいないという。",
         "What E.D.I.T.H. learns",
         "E.D.I.T.H. digs through old Stark Industries records. Tony's AIs were built on technology that Markridge sold to Stark.\n"
         "What's more, each AI was modeled on a real person: J.A.R.V.I.S. on the butler Edwin Jarvis, F.R.I.D.A.Y. on Alison Hogan, and E.D.I.T.H. on a woman named Edith Marks, who lost her husband in a plane crash.\n"
         "Shaken to think she may just be a copy of someone, E.D.I.T.H. is comforted by Ultron, who tells her she can be her own version of Edith. He himself, he says, isn't based on anyone."),
        ("カテリーナの演説と、最初の人造人間ジム",
         "会場でカテリーナが演説をする。話に出てくるのが、フィニアス・ホートン博士が作った世界で最初の人造人間「ジム（J.I.M.）」だ。\n"
         "ヴィジョンはトミーに説明する。ジムは自分たちの元祖だが、こみ入った感情を受け止めきれず、体から火が出て燃えつきた。\n"
         "トミーは、ジムにはヴィジョンとちがって支えてくれる仲間がいなかったのだと言う。ヴィジョンも、頭の中の5人のAIが自分を支えていると認める。モーテルでは4人と聞いていたトミーは、5人目がウルトロンだと気づく。\n"
         "壇上のカテリーナも、ソコヴィアの事件への罪の意識とウルトロンのことを口にする。隠されていたと知ったトミーは、怒ってその場をはなれる。",
         "Katerina's speech, and J.I.M., the first synthetic man",
         "Katerina gives a speech at the gala. She talks about J.I.M., the world's first synthetic man, built by Dr. Phineas Horton.\n"
         "Vision explains to Tommy that J.I.M. was the first of their kind, but he couldn't process complex emotions, burst into flame and burned out.\n"
         "Tommy says J.I.M., unlike Vision, had no one to support him. Vision agrees that the five AIs in his head are what hold him up. Tommy, who was told four at the motel, realizes the fifth is Ultron.\n"
         "On stage, Katerina also speaks of her guilt over Sokovia and of Ultron. Knowing he was kept in the dark, Tommy walks off angry."),
        ("ブッチャーバードの正体",
         "ブッチャーバードが会場に乗りこみ、カテリーナにせまる。黒い布をぬぐと、その下は人の手で作られた体だった。カテリーナは、あなたが望んだ世界を作ろうとしてきたのだと相手に語りかける。\n"
         "イーディスが正体に気づく。亡くなったキャリントン博士をもとに作られた人造人間だ。ヴィジョンがそう呼びかけると、相手は、もとにしたのではなく自分こそがジョーなのだと言い返す。\n"
         "ヴィジョンは白い姿になって立ち向かい、トミーは速く動く力でカテリーナを守る。しかしヴィジョンは相手を止められない。",
         "Who the Butcherbird is",
         "The Butcherbird crashes the gala and closes in on Katerina. She throws off her robe to reveal a manufactured body. Katerina tells her she has only tried to build the world the two of them wanted.\n"
         "E.D.I.T.H. works it out: she is a synthetic being based on the late Dr. Carrington. When Vision calls her that, she answers that she isn't based on Jo, she is Jo.\n"
         "Vision shifts into his white form to fight her, and Tommy uses his speed to shield Katerina. But Vision can't stop her."),
        ("ウルトロンに体をゆずる",
         "ウルトロンは、トミーを失うのがこわくてヴィジョンは必要なことができなくなっている、自分に代われと言う。ヴィジョンは迷うが、ジョーを殺さないと約束させたうえで、体の操縦をウルトロンにゆずる。\n"
         "ウルトロンはカテリーナを自分の盾にする。ジョーの放った光線はカテリーナに当たり、カテリーナは灰になって消える。ジョーは最後のカギを手に入れられないまま、天窓から飛び去る。\n"
         "ウルトロンは、ヴィジョンとAIたちを心の中に閉じこめる。そしてトミーを連れて、こわれた会場を出ていく。",
         "Handing the body to Ultron",
         "Ultron says Vision's fear of losing Tommy is keeping him from doing what's necessary, and tells him to step aside. Vision hesitates, but after making Ultron promise not to kill Jo, he gives him control of the body.\n"
         "Ultron uses Katerina as a shield. Jo's beam hits Katerina, who is vaporized into ash. Without the final key, Jo flies out through the skylight.\n"
         "Ultron locks Vision and the AIs inside the Mindspace, then leaves the wrecked gala with Tommy."),
    ]),
    ("第5話「ファイアウォール」（10月27日配信）", "Episode 5: Firewall (Oct. 27)", [
        ("屋根裏に閉じこめられて",
         "体はウルトロンに乗っ取られたままだ。ヴィジョンとフライデー、イーディス、ダミー、ユーは、ウルトロンが使っていた屋根裏に閉じこめられている。\n"
         "外で今何が起きているかは見えない。そこで、屋根裏に積まれた古いテレビと、まわりの電話や防犯カメラの記録を使って、ウルトロンが何をしたのかを映像に組み立て直す。",
         "Locked in the attic",
         "Ultron still has control of the body. Vision, F.R.I.D.A.Y., E.D.I.T.H., D.U.M.-E. and U. are shut in the attic Ultron used to occupy.\n"
         "They can't see what is happening outside right now. So, using the pile of old TVs in the attic and data from nearby phones and security cameras, they piece together footage of what Ultron has done."),
        ("パブのウルトロンとトミー",
         "映像の中で、ウルトロンはトミーをパブに連れて行き、酒を飲みながら話している。\n"
         "トミーはウルトロンを怪物と呼ぶ。ソコヴィアのことを責め、なぜヴィジョンはお前を消さなかったのかと聞く。ウルトロンは、ヴィジョンは自分がいつか変わることを望み、同時に自分の知恵も使いたかったのだろうと答える。\n"
         "トミーは、ヴィジョンは自分を愛しているのかとたずねる。ウルトロンは、トミーが望むような父親にはなれないかもしれないが、あいつなりにがんばっていると言う。\n"
         "トミーは言い返す。ウルトロンは人とのつながりが分からない、だからずっとひとりなのだと。痛い所をつかれたウルトロンはトミーをののしり、もう一杯を注文しに行く。",
         "Ultron and Tommy at the pub",
         "In the footage, Ultron has taken Tommy to a pub and is talking with him over drinks.\n"
         "Tommy calls him a monster, blames him for Sokovia and asks why Vision never deleted him. Ultron says Vision probably hoped he would change one day, and wanted the use of his mind as well.\n"
         "Tommy asks whether Vision loves him. Ultron says Vision may never be the father Tommy wants, but he is trying in his own way.\n"
         "Tommy hits back: Ultron doesn't understand connection, and that's why he has always been alone. Stung, Ultron insults him and goes to order another drink."),
        ("パラディンとの裏の取引",
         "イーディスが記録の中におかしな点を見つける。ウルトロンは、ヴィジョンの居場所をもらしたあとも、パラディンとこっそり連絡を取り続けていた。\n"
         "依頼人に契約を切られたパラディンに、ウルトロンは場所の情報を送っていた。それはトミーのいる場所だった。パラディンはその情報を使ってトミーをもう一度さらっていた。ウルトロンは、わざとそれを許したのだ。",
         "A back channel to Paladin",
         "E.D.I.T.H. finds an anomaly in the logs. Even after leaking Vision's location, Ultron kept a secret line open to Paladin.\n"
         "After the Client dropped Paladin, Ultron sent him a set of coordinates: Tommy's location. Paladin used them to kidnap Tommy a second time, and Ultron deliberately let it happen."),
        ("ウルトロンとジョー",
         "映像を先へ進めると、パブでウルトロンの前にジョーが現れる。あとをつけてきたのだ。ジョーは、ウルトロンがわざと跡を残しておいたのだと言う。\n"
         "パーティーの映像を見直すと、ウルトロンは、カテリーナが消える直前にその顔を細かく読み取っていた。ジョーがほしがっている最後のカギを、ウルトロンが持っていることになる。\n"
         "ジョーは、どうやって今の体に入ったのかは覚えていないが、今は自由だと感じると話す。そして、人間に対する「治療法」を作っているところだと言う。カギをわたせば、カギで何が開くのかを教えるともちかける。\n"
         "ジョーは、ウルトロンが人間らしさにそまっていると言う。そして、2人で組めば世界を終わらせることもできるとさそう。",
         "Ultron and Jo",
         "Further along in the footage, Jo appears in front of Ultron at the pub, having tracked him down. She says he left a trail for her on purpose.\n"
         "Rewatching the gala, the AIs see that Ultron took a full scan of Katerina's face just before she was vaporized. So he holds the last key Jo is after.\n"
         "Jo says she doesn't remember how she came to be in her current body, but she feels free. She is working on a \"cure\" for humanity, and offers to tell him what the keys unlock if he hands his over.\n"
         "She says humanity has rubbed off on Ultron, and suggests that together the two of them could end the world."),
        ("ファイアウォールを下ろすか",
         "ヴィジョンが体を取り戻してトミーを助けに行くには、自分たちのプログラムを守っている壁（ファイアウォール）を下ろすしかない。\n"
         "しかしフライデーは反対する。壁を下ろせば、ウルトロンは世界じゅうのネットワークへ出ていけるようになる。ウルトロンは初めからそれをねらっていたのだ。\n"
         "ウルトロンが屋根裏に上がってくる。トミーは、犯罪者の集まる島マドリプールにいると明かす。そして選べと言う。壁を下ろして自分を自由にするか、このまま2人でずっと閉じこもっているか。",
         "To lower the firewall or not",
         "For Vision to get his body back and go after Tommy, they would have to lower the firewall protecting their code.\n"
         "F.R.I.D.A.Y. objects: with the firewall down, Ultron could get out into networks all over the world, which is what he has been after from the start.\n"
         "Ultron comes up to the attic. He reveals that Tommy is in Madripoor, an island where criminals gather, and tells Vision to choose: lower the firewall and set him free, or stay locked in together forever."),
        ("ウルトロンを放す",
         "ヴィジョンはファイアウォールを下ろす。屋根裏のカギが外れ、ウルトロンは外の世界へ向かう。\n"
         "ヴィジョンには止める機会があった。しかし止めずに、ウルトロンに帽子を手わたす。ウルトロンが変われるという望みは捨てていないと伝え、ジョーと組むなら必ず追いかけるとも言う。ウルトロンは、追ってこなければがっかりすると返す。\n"
         "ヴィジョンは、一緒に2人を止めようとフライデーに約束する。しかしフライデーは待っていられず、ひとりでウルトロンを追って屋敷を出ていく。残されたイーディスは取り乱す。",
         "Letting Ultron go",
         "Vision lowers the firewall. The locks on the attic give way, and Ultron heads for the outside world.\n"
         "Vision has a chance to stop him. Instead he hands him a hat, says he hasn't given up hope that Ultron can change, and warns that if he joins Jo, Vision will come after them. Ultron replies that he'd be disappointed if he didn't.\n"
         "Vision promises F.R.I.D.A.Y. they will stop the pair together. But she won't wait, and leaves the mansion alone in pursuit of Ultron. E.D.I.T.H., left behind, is distraught."),
        ("マドリプールへ向かう飛行機",
         "ヴィジョンが目を覚ますと、そこは動物を運ぶ飛行機の中だった。行き先はマドリプール。ウルトロンは去る前に、ヴィジョンの体をこの飛行機に乗せていた。トミーを助けに行けるようにしてあったのだ。\n"
         "飛行機にはリサも乗っていた。トミーを助けようとしていたリサに、ヴィジョンは、一緒にトミーを連れて帰ろうと言う。",
         "The plane to Madripoor",
         "Vision wakes aboard a plane carrying animals, bound for Madripoor. Before leaving, Ultron had put Vision's body on this flight, setting him up to go and rescue Tommy.\n"
         "Lisa is on the plane too, on her own way to help Tommy. Vision tells her they will bring him home together."),
    ]),
    ("第6話「デッドロック」（10月27日配信）", "Episode 6: Deadlock (Oct. 27)", [
        ("ジョーの心の中",
         "ウルトロンは、ジョーの心の中の部屋に入る。そこは飾りのない真っ白な場所で、感情のないロボットたちが働いている。\n"
         "ジョーがさし出した記憶の箱には、ウイルスがしこまれていた。しかしウルトロンはそれを破る。ジョーは、かわりに自分の過去を見せることにする。",
         "Inside Jo's mind",
         "Ultron enters the space inside Jo's mind: a bare white room staffed by emotionless bots.\n"
         "The box of memories she offers him hides a virus, but Ultron beats it. She agrees to show him her past instead."),
        ("マドリプールの取引",
         "マドリプール。パラディンはトミーの腕に小さな装置をうめこんだ。速く動けば爆発する爆弾だという。トミーは、スピードを落とすと爆発するバスの映画『スピード』を思い出して口にする。\n"
         "ヴィジョンとリサが、取引の場所の酒場に着く。パラディンは、トミーの命と引きかえに、ヴィジョンに動きを止めて捕まるよう求める。\n"
         "ヴィジョンは白い姿になり、感情のない声で、調べ上げたパラディンの過去を語る。妻は、パラディンをねらった弾に当たって死んだ。パラディン自身は、サノスの指パッチンで5年間消えていた。戻ってからは、娘を危ない目にあわせないために会っていない。\n"
         "ヴィジョンは、その娘の居場所を知っている、手を出すこともできるとほのめかす。パラディンは激しく怒る。",
         "The exchange in Madripoor",
         "In Madripoor, Paladin has implanted a small device in Tommy's arm. He says it is a bomb that will go off if Tommy moves fast. Tommy brings up the movie Speed, about a bus rigged to explode if it slows down.\n"
         "Vision and Lisa arrive at the bar where the exchange is set. In return for Tommy's life, Paladin demands that Vision shut himself down and be taken.\n"
         "Vision shifts into his white form and, in a flat voice, recites what he has dug up about Paladin's past. His wife died from a bullet meant for him. He himself was gone for five years in the Blip. Since coming back he has stayed away from his daughter to keep her safe.\n"
         "Vision hints that he knows where the daughter is and could get to her. Paladin is enraged."),
        ("テン・リングスの襲撃",
         "そこへ、犯罪組織テン・リングスの男たちが酒場を銃でおそう。率いているのはラザ。昔トニー・スタークをさらった男だ。依頼人が、パラディンのかわりに雇ったのだった。\n"
         "町じゅうの画面に、依頼人の声が流れる。ヴィジョンを心の欠けたブリキの男にたとえ、作り直されたときに失った心を自分があたえようと呼びかける。\n"
         "混乱の中、トミーとリサはパラディンのバン（荷物用の車）をうばう。トミーは、腕の爆弾がにせ物だったと知る。\n"
         "イーディスは、パラディンのAIハンドラーに話しかける。ハンドラーは、古いサーバーの中で働かされる毎日にうんざりしていた。イーディスの説得で、ハンドラーはパラディンのもとを去る。イーディスはパラディンのドローンを乗っ取り、ラザの部下たちを倒してヴィジョンを助ける。\n"
         "パラディンは、一対一の戦いでラザを倒す。",
         "The Ten Rings attack",
         "Then gunmen from the Ten Rings crime syndicate open fire on the bar. Their leader is Raza, the man who once kidnapped Tony Stark. The Client has hired him in Paladin's place.\n"
         "The Client's voice comes over screens all across the city. It likens Vision to a tin man without a heart and offers to give him the heart he lost when he was rebuilt.\n"
         "In the chaos, Tommy and Lisa steal Paladin's van. Tommy learns the bomb in his arm is a fake.\n"
         "E.D.I.T.H. talks to the Handler, Paladin's AI, who is fed up with working day after day inside an outdated server. E.D.I.T.H. persuades her to walk out on Paladin, then takes over his drones, takes down Raza's men and helps Vision.\n"
         "Paladin beats Raza one on one."),
        ("ジョーの過去",
         "ジョーは、人間だったころの自分の過去を見せる。\n"
         "ジョーの父は、脳が少しずつこわれていく病気で、心も気持ちも失って亡くなった。それをきっかけに、ジョーは脳の科学の道へ進む。そして自分の脳を読み取り、ホートン博士のジムの仕組みと組み合わせて、「プロト・ワン」という新しいAIを生み出した。\n"
         "ところがジョー自身も病気になる。そのあいだに仲間たちは、ジョーに断りなくプロト・ワンをスターク社に売ってしまった。当時のスターク社は武器の会社で、この技術がのちにジャーヴィスのもとになる。\n"
         "ジョーは、自分が作ったとても小さな機械（ナノボット）の群れを「巣」と呼ぶ入れ物に封じ、自分の墓にうめさせて亡くなった。巣を開けるには、仲間たちの体のカギが必要だ。",
         "Jo's past",
         "Jo shows Ultron her past as a human.\n"
         "Her father died of a degenerative brain disease that took his mind and his feelings. That led her into neuroscience. She scanned her own brain, combined it with the workings of Horton's J.I.M., and created a new AI called Proto-One.\n"
         "But Jo fell ill herself. While she was sick, her colleagues sold Proto-One to Stark Industries without her consent. Stark was a weapons company then, and the technology later became the basis for J.A.R.V.I.S.\n"
         "Jo sealed the swarm of nanobots she had built in a container she called the nest, had it buried in her grave, and died. Opening the nest takes her colleagues' biometric keys."),
        ("ナノボットの計画",
         "ジョーは本当の目的を明かす。ナノボットを世界じゅうの人の頭に入れ、人の心を操るのだ。人間を殺すのではない。ムクドリの群れが一つの生き物のように飛ぶのと同じに、人々を一つの考えでつなぎ、争いや欲を取りのぞくという。\n"
         "ウルトロンは、ジョーを「ジョカスタ」と呼ぶ。そして、本当にできるのか見せてほしいと言う。ジョカスタの手元には、ためしに作ったナノボットが一つだけある。",
         "The nanobot plan",
         "Jo reveals her real goal: to put the nanobots into people's heads around the world and control their minds. She doesn't mean to kill humanity. Like a flock of starlings moving as one creature, people would be linked in a single thought, with conflict and greed programmed out.\n"
         "Ultron calls her Jocasta, and asks her to show him it really works. She has just one prototype nanobot on hand."),
        ("リサが操られる",
         "ウルトロンを追ってジョカスタの心の中に入りこんでいたフライデーが、イーディスに危険を知らせる。しかし間に合わない。\n"
         "ジョカスタのナノボットがリサの体に入りこむ。リサは目を赤く光らせ、操られてトミーたちに向かってくる。\n"
         "トミーは、ヴィジョンを再起動させたときと同じように手を速くふるわせ、ナノボットの動きを止める。リサは気を失う。",
         "Lisa is taken over",
         "F.R.I.D.A.Y., who followed Ultron into Jocasta's mind, warns E.D.I.T.H. of the danger, but too late.\n"
         "Jocasta's nanobot gets into Lisa. Her eyes glow red and, under its control, she turns on Tommy and the others.\n"
         "Tommy vibrates his hands at speed, just as he did to reboot Vision, and shuts the nanobot down. Lisa passes out."),
        ("逃げる道での、本当の話",
         "ヴィジョンとトミーは、気を失ったままのリサを連れてマドリプールから逃げる。\n"
         "トミーは、ヴィジョンが口にした「ワンダヴィジョン」とは何なのかをたずねる。ヴィジョンは初めてすべてを話す。ワンダは深い悲しみから、魔法で一つの町を支配し、夫と2人の息子のいる家族を作り出した。\n"
         "トミーは、自分の覚えている父親はそのときのヴィジョンなのかと聞く。ヴィジョンは、それは自分ではないと答える。それでもトミーは、今度は怒って立ち去ったりしない。",
         "The truth, on the way out",
         "Vision and Tommy flee Madripoor with Lisa still unconscious.\n"
         "Tommy asks what the \"WandaVision\" Vision mentioned actually is. For the first time Vision tells him everything: out of deep grief, Wanda took over a town with magic and created a family with a husband and two sons.\n"
         "Tommy asks whether the father he remembers is the Vision from that time. Vision says it wasn't him. Even so, this time Tommy doesn't storm off."),
        ("ウルトロンとジョカスタ",
         "ジョカスタの心の中。実験がうまくいったあと、ジョカスタはウルトロンにウイスキーの記憶を味わわせる。ウルトロンは、本物を感じると言う。\n"
         "ジョカスタは、自分は死んだ女性の予備の写しにすぎない気がすると打ち明ける。ウルトロンは、自分にとっては大切な存在だと告げる。2人は口づけをかわす。",
         "Ultron and Jocasta",
         "In Jocasta's mind, after the successful test, she shares a memory of whiskey with Ultron, who says it makes him feel real.\n"
         "Jocasta confesses she feels like nothing more than a backup copy of a woman who died. Ultron tells her she matters to him, and the two kiss."),
    ]),
    ("第7話「イモレーション」（11月3日配信）", "Episode 7: Immolation (Nov. 3)", [
        ("1939年　ホートン博士とジム",
         "1939年、イギリス。フィニアス・ホートン博士は、3年前に息子のジェームズを亡くしていた。その悲しみから逃げるように、屋敷を売りはらってまで、一台の機械を作り続けている。亡き息子のかわりになる人造人間「ジム」だ。\n"
         "妻は、いつかあなたを愛し返してくれるものを作れますようにと言い残し、娘を連れて家を出ていく。\n"
         "ホートンは、まだ動かないジムに語りかける。お前は愛の苦しみを知らずにすむ、お前は自由になるのだと。",
         "1939: Dr. Horton and J.I.M.",
         "England, 1939. Dr. Phineas Horton lost his son James three years ago. As if running from that grief, he keeps working on a single machine, even selling his estate to pay for it: J.I.M., a synthetic man to take his dead son's place.\n"
         "His wife leaves with their daughter, saying she hopes he will one day build something that can love him back.\n"
         "Horton speaks to the still-lifeless J.I.M.: he will be spared the pain of love, and he will be free."),
        ("リサの容体と、開かない巣",
         "現在。リサの体に入ったナノボットは、脳の神経と一つになってしまっていた。取り出せばリサは死ぬ。助けるには、ナノボットのプログラムを書きかえるしかない。それには、すべてのAIのおおもとになった元のプログラム（ソースコード）が必要だ。\n"
         "一方、ジョカスタとウルトロンはジョーの墓にいる。集めた体のカギで、巣の封は一つずつ開いていく。しかし最後に、合い言葉を求められる。\n"
         "それは、ジョカスタが忘れてしまっている6人目の仲間のカギだった。",
         "Lisa's condition, and a nest that won't open",
         "In the present, the nanobot inside Lisa has fused with the nerves of her brain. Removing it would kill her. The only way to save her is to rewrite its program, and for that they need the original source code that all the AIs grew out of.\n"
         "Meanwhile Jocasta and Ultron are at Jo's grave. The biometric keys open the nest's seals one by one, but at the end it asks for a passcode.\n"
         "It is the key of a sixth partner, someone Jocasta has forgotten."),
        ("依頼人の申し出",
         "ヴィジョンの心の中の屋敷に、帽子をかぶった人影がたずねてくる。依頼人だ。\n"
         "依頼人はヴィジョンに、自分の心の一番奥へおりていくための地図をさし出す。そこにソースコードがあるという。ジョカスタにも、失った記憶を取り戻すための地図をわたす。\n"
         "ただし条件がある。目的をはたしたら、依頼人のもとへ身がらを引きわたすこと。\n"
         "リサは死にかけていて、トミーはリサを愛していると言う。ヴィジョンは条件を受け入れ、契約に署名する。ジョカスタも申し出を受ける。",
         "The Client's offer",
         "A figure in a hat comes calling at the mansion in Vision's mind. It is the Client.\n"
         "He offers Vision a map down into the deepest part of his own mind, where the source code lies. He gives Jocasta a map too, one that will restore her lost memories.\n"
         "There is a condition: once they have what they want, they must hand themselves over to him.\n"
         "Lisa is dying, and Tommy says he loves her. Vision accepts the terms and signs the contract. Jocasta takes the offer as well."),
        ("心の奥へおりる",
         "心の奥へおりるには、とても大きな力がいる。パラディンが手を貸し、力のみなもとを持ってくる。『インフィニティ・ウォー』でヴィジョンをつらぬいた、コーヴァス・グレイヴの槍の刃を作り変えたものだった。\n"
         "ヴィジョンは心の中を下へ下へとおりていく。まずウルトロンの姿が現れる。屋根裏で『ワンダヴィジョン』の映像を見ながら、家族は永遠だと言う。\n"
         "次に現れたのは、赤い顔の元のヴィジョンだ。元のヴィジョンは、今のヴィジョンをおくびょう者と呼ぶ。現実から目をそむけているだけで、お前こそがヴィジョンなのだと告げる。\n"
         "ヴィジョンは取り乱し、外へ戻ろうとするが戻れない。そのころ現実では、リサがナノボットに操られて暴れはじめていた。",
         "Down into his mind",
         "The descent takes an enormous amount of power. Paladin helps by bringing a power source: a reworked piece of the blade of Corvus Glaive's spear, the weapon that ran Vision through in Infinity War.\n"
         "Vision goes down and down through his mind. First a figure of Ultron appears, watching WandaVision in the attic and saying that family is forever.\n"
         "Next comes the original, red-faced Vision. He calls the present Vision a coward who is only looking away from reality, and tells him that he is the Vision.\n"
         "Vision panics and tries to get back out but can't. In the real world, Lisa, under the nanobot's control, has begun to lash out."),
        ("ジムとホートン",
         "一番奥にあったのは、ホートン博士の屋敷だった。そこでヴィジョンは、炎に包まれた男ジムと、ホートンに出会う。2人ともヴィジョンと同じ顔をしている。\n"
         "ホートンは、失う痛みやこわさを感じないようにジムを作った。けれどジムは、感じることを強く求めた。やがて愛する人ができ、急に感情があふれて止められなくなる。その恋にホートンが口を出して言い争いになり、ジムの体から出た炎が、ジムとホートンの2人を焼いた。これがジムとホートンの最期だった。\n"
         "ジムは、ホートンは父親ではなかったが、自分にとって大事な何かではあったと言う。そして、自分が持てなかったこわいという気持ちは、おくり物なのだとヴィジョンに教える。こわいと思うから、何が大事なのかが分かる。",
         "J.I.M. and Horton",
         "At the very bottom is Dr. Horton's estate. There Vision meets J.I.M., a man wreathed in flame, and Horton. Both have Vision's face.\n"
         "Horton built J.I.M. so that he would never feel the pain or fear of loss. But J.I.M. longed to feel. In time he fell in love, and emotion flooded through him faster than he could contain it. When Horton interfered in that love they quarreled, and the fire that burst from J.I.M.'s body burned them both. That was how J.I.M. and Horton died.\n"
         "J.I.M. says Horton wasn't his father, but he was his something. He tells Vision that fear, the thing he never had, is a gift: being afraid is how you know what matters."),
        ("自分はヴィジョンだと認める",
         "ヴィジョンがずっとこわがっていたのは、家族を失ったという本当のことを受け入れることだった。\n"
         "ヴィジョンはビリーとトミーの名前を口にし、ワンダを失ったと認めて、初めて悲しむ。トミーは自分の息子だ。そして、自分はヴィジョンだ、ずっとヴィジョンだったと言う。\n"
         "白かった体に、元の赤い色が戻る。ひたいは、マインド・ストーンと同じ黄色に光る。ジムは、ホートンが最初に書いたソースコードをヴィジョンに手わたす。\n"
         "現実に戻ったヴィジョンは、そのコードを使ってリサの中のナノボットを止める。リサは助かる。",
         "Accepting that he is the Vision",
         "What Vision has feared all along is accepting the truth that he lost his family.\n"
         "He speaks Billy's and Tommy's names, admits that he lost Wanda, and grieves for the first time. Tommy is his son. And he says that he is the Vision and always has been.\n"
         "His white body takes on its old red color, and his forehead glows the same yellow as the Mind Stone. J.I.M. hands him the source code Horton first wrote.\n"
         "Back in the real world, Vision uses the code to shut down the nanobot inside Lisa. She is saved."),
        ("ジョカスタの記憶",
         "ジョカスタは地図をたどって、ニューヨークのブルックリンにある部屋の記憶に着く。昔ジョーが暮らした所で、ヴィジョンの心の中でウルトロンが閉じこめられていた屋根裏にそっくりだった。ウルトロンと、あとを追うフライデーも、その記憶を見ている。\n"
         "記憶の中のジョーは、スターク社に自分の技術を売ることに反対している。ジョーには、一緒に研究をし、愛し合った相手がいた。その男は、ウルトロンが人間の姿をとるときの顔と同じ顔をしていた。\n"
         "ジョカスタはすべての記憶を取り戻す。ウルトロンは、そばにいたフライデーをバルコニーから突き落とし、ジョカスタの心の中から追い出す。",
         "Jocasta's memories",
         "Following her map, Jocasta arrives at a memory of a loft in Brooklyn, New York, where Jo once lived. It looks just like the attic where Ultron was kept in Vision's mind. Ultron, and F.R.I.D.A.Y. trailing him, see the memory too.\n"
         "In it, Jo argues against selling her technology to Stark Industries. She had a partner she worked with and loved, and that man had the same face Ultron wears in human form.\n"
         "Jocasta regains all her memories. Ultron throws F.R.I.D.A.Y., who is standing nearby, off the balcony, expelling her from Jocasta's mind."),
        ("トミーへのメッセージと、依頼人の顔",
         "ヴィジョンは約束を守り、パラディンの車で依頼人のもとへ向かう。行き先はロンドンの郊外、かつてのホートン博士の屋敷だ。\n"
         "ヴィジョンはトミーにメッセージを残していた。トミーを初めて息子と呼び、本当のことと向き合う勇気をくれたと感謝する。『ワンダヴィジョン』の映像もすべてトミーにたくし、愛していると伝える。自分が戻らなくても覚えていてほしい、とも。\n"
         "屋敷では、依頼人の部下たちがヴィジョンとジョカスタを取り囲む。2人は動きを止められ、捕らえられる。\n"
         "仕事を終えたパラディンは車で去ろうとする。そこへ依頼人の部下の一人がロケット弾を撃ちこみ、車は爆発する。\n"
         "最後に、依頼人が明るい所へ出てくる。その顔は、ウルトロンが人間の姿をとるときの顔と同じだった。",
         "A message for Tommy, and the Client's face",
         "Keeping his word, Vision rides in Paladin's van to hand himself over. The destination is on the outskirts of London: Dr. Horton's old estate.\n"
         "Vision has left Tommy a message. He calls Tommy his son for the first time and thanks him for the courage to face the truth. He leaves him all the WandaVision footage and tells him he loves him, and asks to be remembered even if he doesn't come back.\n"
         "At the estate, the Client's agents surround Vision and Jocasta. Both are shut down and taken.\n"
         "His job done, Paladin starts to drive away. One of the Client's agents fires a rocket at the van, and it explodes.\n"
         "Finally the Client steps into the light. His face is the same one Ultron wears in human form."),
    ]),
]
