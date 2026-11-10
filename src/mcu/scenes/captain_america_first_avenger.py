# 『キャプテン・アメリカ／ザ・ファースト・アベンジャー』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじと、登場人物の記事で事実を確かめた。資料どうしで食い違う所（博覧会と実験の年）や、確かめられない細かい順番・せりふは書いていない。
# 日本語版のせりふは、日本語版ウィキペディアにある言い回しだけをカギかっこで使い、ほかは内容だけ書いた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 氷の中の盾と、ノルウェーの宝", "Part 1: A shield in the ice, a treasure in Norway", [
        ("現代、北極の吹雪",
         "現代。北極の雪と氷の中で、調査の人たちが大きな飛行機の残がいを見つける。\n"
         "氷をくだいて中に入ると、凍りついた人の姿らしきものと、赤・白・青に塗られた星のマークの丸い盾が氷の中にうまっていた。\n"
         "物語はここから、およそ70年前の第二次世界大戦の時代へさかのぼる。",
         "The present: an Arctic blizzard",
         "The present day. In the Arctic snow and ice, a team finds the wreck of a huge aircraft.\n"
         "Breaking into it, they find what looks like a frozen figure, and a round shield painted red, white and blue with a star, locked in the ice.\n"
         "The story then jumps back about 70 years, to World War II."),
        ("1942年、ノルウェーの小さな町",
         "1942年3月、ドイツに占領されたノルウェーのトンスベルグ。ナチスの将校で、科学部門ヒドラを率いるヨハン・シュミットの部隊が、古い教会をおそう。\n"
         "シュミットがさがしているのは、北欧の神オーディンの宝とされる青く光る立方体「テッセラクト（四次元キューブ）」だった。",
         "1942: a small town in Norway",
         "March 1942, Tønsberg in German-occupied Norway. Troops led by Johann Schmidt, a Nazi officer and head of the science division Hydra, raid an old church.\n"
         "Schmidt is hunting a glowing blue cube, the Tesseract, said to be a treasure of the Norse god Odin."),
        ("にせものと本物のキューブ",
         "墓の中にあったキューブはにせものだった。シュミットは、壁にほられた世界樹の絵の中に本物がかくされているのを見つけ出す。\n"
         "手に入れたテッセラクトを前に、シュミットは、ヒトラーが砂漠でがらくたをさがしている間に自分は本物の力を手に入れた、という意味のことを言う。シュミットのねらいは、ナチスをこえて自分が世界を支配することだった。",
         "The fake cube and the real one",
         "The cube in the tomb is a fake. Schmidt finds the real one hidden inside a carving of the world tree on the wall.\n"
         "Holding the Tesseract, he remarks that while Hitler digs for trinkets in the desert, he has found real power. His goal is to rule the world himself, beyond even the Nazis."),
    ]),
    ("第2部 ブルックリンの小さな青年", "Part 2: A small young man from Brooklyn", [
        ("また不合格",
         "ニューヨーク、ブルックリン。スティーブ・ロジャースは体が小さく、ぜんそくなど多くの病気をかかえている。\n"
         "戦争で国の役に立ちたいと、軍の入隊検査を何度も受けるが、そのたびに不合格になる。出身地を書きかえて別の会場で受け直すほど、あきらめない。",
         "Rejected again",
         "Brooklyn, New York. Steve Rogers is small and has a long list of illnesses, asthma among them.\n"
         "He wants to serve his country in the war and keeps trying to enlist, only to be rejected every time. He even lies about his hometown to try again at another office."),
        ("映画館と裏通りのけんか",
         "映画館でニュース映画の最中にさわぐ男に、スティーブは静かにしろと注意する。男に裏通りへ連れ出され、何度もなぐり倒される。\n"
         "スティーブはごみ箱のふたを盾のように持ち、倒されても立ち上がり続ける。そこへ軍服姿の親友バッキー・バーンズが来て、男を追いはらう。",
         "The theater and the alley fight",
         "In a movie theater, Steve tells a man heckling the newsreel to be quiet. The man drags him into an alley and knocks him down again and again.\n"
         "Holding a trash-can lid like a shield, Steve keeps getting up: \"I can do this all day.\" His best friend Bucky Barnes, in uniform, arrives and chases the man off."),
        ("バッキーの出発前夜",
         "バッキーは陸軍の軍曹になり、次の日にヨーロッパの戦場へ向かうことになっていた。\n"
         "バッキーは、スティーブがまた書類にうそを書いて検査を受けたことに気づいている。最後の夜をいっしょに楽しもうと、2人の女性をさそって、未来の技術を見せる博覧会へスティーブを連れていく。",
         "Bucky's last night",
         "Bucky is now an Army sergeant and ships out to the war in Europe the next day.\n"
         "He knows Steve has lied on his forms again. For one last night out, he brings two girls along and takes Steve to an expo of future technology."),
        ("スターク博覧会",
         "博覧会では、若い発明家ハワード・スタークが、車を宙にうかせてみせる。車は少しうくが、すぐに落ちてしまう。\n"
         "スティーブは会場の中にある入隊受付を見つけ、もう一度受けようとする。バッキーは止めるが、スティーブの決心は変わらない。2人はここで別れる。",
         "The Stark Expo",
         "At the expo, young inventor Howard Stark demonstrates a flying car. It lifts off for a moment, then crashes down.\n"
         "Steve spots an enlistment booth inside and decides to try again. Bucky tries to stop him, but Steve won't change his mind, and the two part ways."),
        ("アースキン博士の質問",
         "2人の話を聞いていた科学者アブラハム・アースキン博士が、検査室のスティーブに声をかける。博士は、ナチスを殺したいのかとたずねる。\n"
         "スティーブは、誰も殺したくはない、ただいじめる者が許せないのだ、と答える。博士はその答えを気に入り、スティーブを合格にして、特別な計画に加える。",
         "Dr. Erskine's question",
         "Dr. Abraham Erskine, a scientist who overheard them, comes to see Steve in the exam room and asks whether he wants to kill Nazis.\n"
         "\"I don't want to kill anyone. I don't like bullies,\" Steve answers. Erskine likes the answer, approves him, and brings him into a special program."),
    ]),
    ("第3部 スーパーソルジャー計画", "Part 3: The super-soldier program", [
        ("訓練キャンプ",
         "スティーブは、陸軍のチェスター・フィリップス大佐が指揮し、英国のペギー・カーターが加わる秘密の部隊SSR（戦略科学予備軍）の訓練キャンプに入る。\n"
         "候補の兵隊ホッジがペギーをからかうと、ペギーは一発でなぐり倒す。スティーブは走っても運んでもほかの兵隊についていけない。",
         "Training camp",
         "Steve joins a training camp for the SSR, the Strategic Scientific Reserve, a secret unit commanded by Army Colonel Chester Phillips, with British agent Peggy Carter on the staff.\n"
         "When a recruit named Hodge mocks Peggy, she knocks him flat with one punch. Steve can't keep up with the others at running or carrying anything."),
        ("旗の取り方",
         "大佐は、ポールの上の旗を取った者は車で帰れると言う。ほかの兵隊は登ろうとして失敗する。\n"
         "スティーブはポールを止めている部品を外して、ポールごと倒し、旗を手に入れる。力ではなく、頭を使ったやり方だった。",
         "Getting the flag",
         "Phillips says whoever brings down the flag from the top of a pole gets a ride back. The others try to climb it and fail.\n"
         "Steve pulls the pin holding the pole up, lets it fall, and takes the flag. It's brains, not muscle."),
        ("手りゅう弾",
         "大佐は、体の弱いスティーブを選ぶことに反対していた。アースキン博士の考えを試すように、大佐は訓練中の兵隊の中へ手りゅう弾を投げこむ。\n"
         "ホッジたちがにげる中、スティーブだけが手りゅう弾におおいかぶさり、ほかの人ににげろと叫ぶ。手りゅう弾は練習用のにせもので、爆発しなかった。この出来事で、計画の参加者はスティーブに決まる。",
         "The grenade",
         "Phillips is against choosing someone as frail as Steve. As if to test Erskine's view, he tosses a grenade into the group of recruits.\n"
         "Hodge and the others scatter, but Steve throws himself on the grenade and yells at everyone to get away. It's a dummy and doesn't go off. That settles it: Steve is chosen."),
        ("ヒドラの研究所",
         "ヨーロッパでは、シュミットの下で働く科学者アーニム・ゾラ博士が、テッセラクトの力を取り出して、新しい兵器を動かすエネルギーに変えていた。\n"
         "シュミットはアースキン博士の居場所をつかみ、博士をねらう刺客を送りこむ。",
         "Hydra's laboratory",
         "In Europe, Dr. Arnim Zola, a scientist working under Schmidt, is drawing power from the Tesseract to fuel new weapons.\n"
         "Schmidt learns where Erskine is and sends an assassin after him."),
        ("実験の前の夜",
         "実験の前の夜、アースキン博士はスティーブと酒を前に話す。博士はかつてドイツでシュミットのもとで働いていた。シュミットは完成前の血清を自分の体に使い、力を得た代わりに、見た目も心もゆがんでしまった。\n"
         "血清は、その人の中にあるものを大きくする。だから良い人はより良く、悪い人はより悪くなる。弱さを知るスティーブだからこそ選んだのだと博士は言い、「完璧でなくても善良な君のままで」いてほしいと頼む。スティーブの分の酒は、実験に差しさわるからと博士が飲みほす。",
         "The night before",
         "On the night before the procedure, Erskine sits down with Steve over a drink. He once worked under Schmidt in Germany, he says. Schmidt took an unfinished version of the serum; it gave him strength but warped both his looks and his mind.\n"
         "The serum amplifies what is already inside a person: good becomes great, bad becomes worse. Erskine chose Steve because he knows what weakness feels like, and asks him to stay who he is: \"not a perfect soldier, but a good man.\" He drinks Steve's glass himself, since Steve has the procedure in the morning."),
        ("古道具屋の地下",
         "翌朝、ペギーはスティーブを車でブルックリンの古道具屋へ連れていく。店の奥から地下へ下りると、大きな秘密の研究室があった。\n"
         "上院議員のブラントや、見学の人たちが上の窓から見守る。ハワード・スタークが装置を動かす係だった。",
         "Beneath an antique shop",
         "The next morning, Peggy drives Steve to an antique shop in Brooklyn. Through the back, a passage leads down to a huge secret lab.\n"
         "Senator Brandt and other observers watch from a booth above. Howard Stark runs the machinery."),
        ("実験",
         "スティーブは大きな容器の中に横になり、アースキン博士に血清を打たれる。容器が閉じられ、ハワードの装置が強い光（ヴィタ・レイ）を浴びせる。\n"
         "中からスティーブの叫び声が聞こえ、ペギーと博士は止めようとするが、スティーブはやめるなと言う。光が消えて容器が開くと、スティーブは背が高く、たくましい体に変わっていた。",
         "The procedure",
         "Steve lies down in a large pod and Erskine injects the serum. The pod closes and Howard's machine floods him with vita-rays.\n"
         "Steve screams, and Peggy and Erskine try to stop it, but Steve tells them not to. When the light fades and the pod opens, he is taller and powerfully built."),
    ]),
    ("第4部 博士の死と、ショーの日々", "Part 4: Erskine's death, and life on stage", [
        ("刺客クルーガー",
         "喜びもつかのま、見学者の中にまぎれていたヒドラの刺客ハインツ・クルーガーが、研究室で爆発を起こす。\n"
         "クルーガーはアースキン博士を撃ち、残っていた最後の血清を持って逃げる。博士は倒れたまま、スティーブの胸を指さして息を引き取る。",
         "The assassin Kruger",
         "The joy doesn't last. Heinz Kruger, a Hydra assassin hidden among the observers, sets off an explosion in the lab.\n"
         "He shoots Erskine and runs off with the last vial of serum. Dying, Erskine points to Steve's chest, over his heart."),
        ("ブルックリンの追跡",
         "クルーガーは車で逃げ、スティーブは新しい体で走って追いかける。ペギーは向かってくるクルーガーの車を正面から撃ち、スティーブがペギーをひかれる寸前に助ける。\n"
         "スティーブは、急に強くなった体にとまどいながらも、通りを走って追い続ける。",
         "The Brooklyn chase",
         "Kruger escapes by car, and Steve runs after him in his new body. Peggy stands in the road firing at Kruger's car, and Steve pulls her out of the way just in time.\n"
         "Still getting used to his sudden strength, Steve keeps up the chase through the streets."),
        ("港の小さな潜水艦",
         "港で追いつめられたクルーガーは、子どもを人質にとり、水の中へ投げこむ。子どもは泳げるから行ってと言い、スティーブは追跡を続ける。\n"
         "クルーガーは小さな潜水艦で逃げようとするが、スティーブは水にもぐって潜水艦をこじ開け、クルーガーを岸へ引きずり出す。追いかける間に、血清の入ったびんは割れてしまった。",
         "A tiny submarine at the docks",
         "Cornered at the docks, Kruger grabs a boy as a hostage and throws him into the water. The boy calls out that he can swim, so Steve keeps going.\n"
         "Kruger tries to escape in a small submarine, but Steve dives in, tears it open and drags him ashore. The vial of serum has been smashed during the chase."),
        ("ヒドラ万歳",
         "スティーブが問いつめると、クルーガーはヒドラの名を口にし、首を1つ切られれば代わりに2つ生えてくる、という意味のことを言う。\n"
         "そして口にかくしていた毒のカプセルをかみ、自分で命を絶つ。アースキン博士は死に、血清の作り方も失われた。超人兵士は、スティーブ1人だけになった。",
         "Hail Hydra",
         "When Steve presses him, Kruger names Hydra and says that cut off one head, two more shall take its place.\n"
         "Then he bites down on a hidden cyanide capsule and kills himself. With Erskine dead, the formula is gone too. Steve is the only super soldier there will be."),
        ("研究所行きか、ショーか",
         "フィリップス大佐は、ほしかったのは1人の超人ではなく超人の軍隊だったとして、スティーブを研究に回そうとする。\n"
         "そこへブラント上院議員が別の役目を持ちかける。星条旗の衣装を着た「キャプテン・アメリカ」として国中を回り、戦争のための債券を売るショーに出ることだった。",
         "A lab, or a stage",
         "Phillips says he wanted an army of super soldiers, not one, and plans to send Steve off to be studied.\n"
         "Senator Brandt offers another job: tour the country as \"Captain America\" in a star-spangled costume, selling war bonds in a stage show."),
        ("キャプテン・アメリカのショー",
         "スティーブは踊り子たちといっしょに歌と劇の舞台に立ち、ショーは大人気になる。映画やまんがにもなり、たくさんの債券が売れる。\n"
         "子どもたちには英雄だが、スティーブ自身は、戦場で戦う兵隊たちから遠いところで、作り物のヒーローを演じ続けていた。",
         "The Captain America show",
         "Steve performs songs and skits with a chorus line, and the show is a smash. There are movies and comic books, and the bonds sell.\n"
         "Kids see a hero, but Steve is playing a make-believe one, far from the soldiers who are actually fighting."),
    ]),
    ("第5部 たった1人の救出作戦", "Part 5: A one-man rescue", [
        ("イタリアの前線",
         "1943年、イタリアの前線の基地。スティーブは本物の兵隊たちの前でショーをするが、からかわれ、物を投げつけられてしまう。\n"
         "雨の中で落ちこむスティーブのもとへペギーが来る。ペギーは、自分はショーの人気者になるために選ばれたのではないとスティーブに気づかせる。",
         "The Italian front",
         "1943, an army camp on the Italian front. Steve performs for real soldiers, who jeer and throw things at him.\n"
         "As he sits alone in the rain, Peggy comes to find him and reminds him he was meant for more than a stage show."),
        ("バッキーの部隊",
         "ペギーは、バッキーのいる第107部隊がシュミットの軍と戦って、多くの兵隊が行方不明になったとスティーブに伝える。\n"
         "スティーブはフィリップス大佐のところへ行き、バッキーの名前を聞く。大佐は、敵の陣地の奥の工場にいるはずの捕虜を助けに行く計画はないと言い、スティーブの願いをはねつける。",
         "Bucky's unit",
         "Peggy tells Steve that Bucky's unit, the 107th, fought Schmidt's forces and many of its men are missing.\n"
         "Steve goes to Phillips and asks about Bucky. Phillips says there will be no rescue of the prisoners held at a factory deep behind enemy lines, and turns him down."),
        ("ハワードの飛行機",
         "スティーブはショーの衣装と盾のまま、1人で助けに行くと決める。ペギーはハワード・スタークにたのみ、ハワードの飛行機でスティーブを敵の陣地の近くまで運ぶ。\n"
         "飛行機は対空砲で撃たれるが、スティーブはパラシュートで飛び降りる。",
         "Howard's plane",
         "Steve decides to go alone, still in his stage costume with his prop shield. Peggy asks Howard Stark for help, and Howard flies Steve close to the enemy lines.\n"
         "The plane comes under anti-aircraft fire, and Steve parachutes out."),
        ("ヒドラの工場",
         "スティーブはトラックにまぎれてヒドラの工場にしのびこむ。見張りを倒し、とらわれていた兵隊たちを次々に檻から出す。\n"
         "兵隊たちにおまえは誰だと聞かれ、スティーブはキャプテン・アメリカだと名乗る。助け出された中には、のちに仲間になるダム・ダム・ダガンたちもいた。",
         "The Hydra factory",
         "Steve slips into the Hydra factory hidden on a truck. He takes out guards and frees the prisoners from their cages one after another.\n"
         "Asked who he is, he answers, \"Captain America.\" Among the men he frees are Dum Dum Dugan and others who will later fight beside him."),
        ("実験台のバッキー",
         "スティーブは工場の奥の実験室で、台にしばりつけられたバッキーを見つける。バッキーはゾラ博士に実験をされていて、ぼんやりしたまま自分の名前と兵隊の番号をくり返していた。\n"
         "スティーブはバッキーを助け起こし、2人で出口をさがす。",
         "Bucky on the table",
         "In a lab deep inside the factory, Steve finds Bucky strapped to a table. Zola has been experimenting on him, and he is dazed, repeating his name and serial number.\n"
         "Steve gets him up, and they look for a way out."),
        ("レッド・スカル",
         "燃え上がる工場の通路で、スティーブはシュミットと向き合う。シュミットは、血清を受けた体をスティーブと見比べる。\n"
         "そして自分の顔の皮をはがしてみせる。その下にあったのは、真っ赤などくろのような顔だった。これが「レッド・スカル」と呼ばれる理由だった。シュミットはゾラ博士とともに逃げ、工場は爆発を始める。",
         "Red Skull",
         "On a catwalk in the burning factory, Steve comes face to face with Schmidt, who sizes up the man the serum made of him.\n"
         "Then Schmidt peels off his face. Beneath it is a red, skull-like head: the reason he is called the Red Skull. He escapes with Zola, and the factory starts exploding."),
        ("炎の上を飛ぶ",
         "スティーブとバッキーは高い所にかかった細いはりを渡ってにげる。バッキーは渡りきるが、はりがこわれてスティーブは取り残される。\n"
         "バッキーは先に行けと言われてもスティーブを置いていかない。スティーブは炎の上を思い切り飛びこえ、2人は工場から脱出する。",
         "Leaping over the flames",
         "Steve and Bucky escape across a narrow beam high above the floor. Bucky makes it over, but the beam gives way and leaves Steve stranded.\n"
         "Bucky refuses to leave without him. Steve takes a running leap across the flames, and the two get out of the factory."),
        ("400人の帰還",
         "基地では、ペギーとフィリップス大佐が、スティーブは戻らないものと思っていた。そこへスティーブが、助け出したおよそ400人の兵隊を連れて歩いて帰ってくる。\n"
         "スティーブは命令を破った罰を受けるつもりだったが、大佐はその必要はないと答える。兵隊たちは歓声を上げ、バッキーの声に合わせてキャプテン・アメリカをたたえる。スティーブは本物の英雄になった。",
         "Four hundred men come home",
         "At the base, Peggy and Phillips have given Steve up for lost. Then he walks in, leading about 400 men he has rescued.\n"
         "Steve offers to accept discipline for disobeying orders, but Phillips says it won't be necessary. The soldiers cheer, led by Bucky, for Captain America. Steve is a real hero now."),
    ]),
    ("第6部 ハウリング・コマンドーズ", "Part 6: The Howling Commandos", [
        ("ロンドンの酒場",
         "ロンドン。スティーブは捕虜の工場で見たヒドラの基地の地図を覚えていて、その基地をつぶしていく部隊を作ることにする。\n"
         "酒場で、助け出した兵隊の中から腕のいいダガン、ゲイブ・ジョーンズ、ジム・モリタ、フォールズワース、デルニエをさそい、バッキーも加わる。チーム「ハウリング・コマンドーズ」ができる。",
         "A pub in London",
         "London. Steve memorized a map of Hydra's bases at the factory, and he sets out to form a unit to destroy them.\n"
         "In a pub he recruits the best of the men he rescued: Dugan, Gabe Jones, Jim Morita, Falsworth and Dernier. Bucky signs on too. The Howling Commandos are born."),
        ("赤いドレスのペギー",
         "赤いドレスのペギーが酒場に来て、スティーブとダンスの話をする。スティーブは踊ったことがないと言い、ペギーは、ふさわしい相手が見つかるまで待つつもりだと答える。\n"
         "2人の気持ちが少しずつ近づいていく。",
         "Peggy in red",
         "Peggy walks into the pub in a red dress and talks with Steve about dancing. He admits he has never danced; she says she is waiting for the right partner.\n"
         "The two are slowly growing closer."),
        ("ヴィブラニウムの盾",
         "ハワードの研究室で、スティーブは新しい盾を選ぶ。ほかの試作品の中にあった、丸い盾が気に入る。めずらしい金属ヴィブラニウムでできていて、とても丈夫で、衝撃をほとんど吸いこむ。\n"
         "その少し前、女性の職員がスティーブにキスをするのを見たペギーは怒り、盾を持つスティーブに向けて銃を撃つ。弾はすべて盾にはね返され、盾の強さが示される。",
         "The vibranium shield",
         "In Howard's lab, Steve picks out a new shield and settles on a round one among the prototypes. It is made of vibranium, a rare metal that is nearly indestructible and absorbs almost any impact.\n"
         "Just before, Peggy has seen a woman from the office kiss Steve. Annoyed, she fires a pistol at him while he holds the shield. Every bullet bounces off, proving how strong it is."),
        ("ヒドラの基地をつぶしていく",
         "新しい戦闘服と盾を手にしたスティーブは、ハウリング・コマンドーズとともに、ヨーロッパ中のヒドラの基地を次々に攻めてつぶしていく。\n"
         "一方シュミットは、ヒドラはもうナチスのかげにかくれないとして、ナチスとも手を切り、テッセラクトの兵器で世界を相手にする準備を進める。",
         "Taking down Hydra bases",
         "With a new uniform and the shield, Steve and the Howling Commandos attack Hydra bases across Europe and destroy them one by one.\n"
         "Meanwhile Schmidt declares that Hydra will no longer hide in Hitler's shadow. He breaks with the Nazis and prepares to take on the world with his Tesseract weapons."),
        ("雪山の列車",
         "1945年、アルプスの雪山。ゾラ博士が乗る列車を止めるため、スティーブ、バッキー、ゲイブはワイヤーを使って走る列車の屋根に飛び降りる。\n"
         "車両の中で、スティーブとバッキーはヒドラの兵隊と戦う。",
         "The mountain train",
         "1945, the snowy Alps. To stop a train carrying Zola, Steve, Bucky and Gabe zip-line onto its roof as it races along.\n"
         "Inside the cars, Steve and Bucky fight Hydra soldiers."),
        ("バッキーが落ちる",
         "戦いの最中、バッキーはスティーブの盾をひろって敵の攻撃を受け止めるが、その衝撃で車両の横に大きな穴があき、外へ投げ出される。\n"
         "バッキーは列車の外の手すりにぶら下がり、スティーブが手を伸ばす。しかし手すりが折れ、バッキーは叫びながら深い谷底へ落ちていく。ゾラ博士はつかまる。",
         "Bucky falls",
         "In the fight, Bucky picks up Steve's shield and takes a hit from an enemy weapon. The blast tears open the side of the car and throws him out.\n"
         "Bucky hangs from a rail on the outside of the train as Steve reaches for him. The rail snaps, and Bucky falls screaming into the deep ravine. Zola is captured."),
        ("ゾラの取り調べ",
         "つかまったゾラ博士は、フィリップス大佐の取り調べを受ける。ゾラは、シュミットがアメリカの大きな都市を爆撃で破壊しようとしていることと、ヒドラの最後の基地の場所を明かす。",
         "Zola's interrogation",
         "The captured Zola is questioned by Phillips. He reveals that Schmidt plans to bomb America's major cities, and where Hydra's last base is."),
        ("こわれた酒場で",
         "親友を失ったスティーブは、爆撃でこわれた酒場で1人で酒を飲む。しかし血清で変わった体では、いくら飲んでも酔うことができない。\n"
         "ペギーがそばに来て、バッキーの死はスティーブのせいではないとなぐさめる。スティーブは、シュミットを倒すまで戦うと決める。",
         "In a bombed-out pub",
         "Having lost his best friend, Steve drinks alone in a pub wrecked by bombing. But his changed body won't let him get drunk, however much he drinks.\n"
         "Peggy joins him and tells him Bucky's death is not his fault. Steve resolves to keep fighting until Schmidt is stopped."),
    ]),
    ("第7部 最後の戦いと、ペギーとの約束", "Part 7: The final battle, and a promise to Peggy", [
        ("正面から乗りこむ",
         "スティーブはバイクに乗り、山の中のヒドラの最後の基地へ正面から突っこむ。わざとつかまり、シュミットの前に連れていかれる。\n"
         "シュミットに、なぜおまえは特別なのかと聞かれたスティーブは、特別なことは何もない、自分はブルックリン出身のただの若者だ、と答える。",
         "Straight through the front door",
         "Steve rides a motorcycle straight into Hydra's last base in the mountains. He lets himself be captured and is brought before Schmidt.\n"
         "Asked what makes him so special, Steve says, \"Nothing. I'm just a kid from Brooklyn.\""),
        ("仲間の突入",
         "その時、ハウリング・コマンドーズがロープで飛びこんできて、フィリップス大佐とペギーの部隊も攻めこむ。基地は大きな戦いになる。\n"
         "シュミットは、爆弾を積んだ巨大な飛行機ワルキューレに乗りこみ、飛び立とうとする。",
         "The team storms in",
         "At that moment the Howling Commandos swing in on ropes, and Phillips and Peggy's forces storm the base. A full battle breaks out.\n"
         "Schmidt boards the Valkyrie, a gigantic aircraft loaded with bombs, and gets ready to take off."),
        ("キスと飛び乗り",
         "スティーブは、フィリップス大佐とペギーの乗る車で、動き出したワルキューレを追う。車の中で、ペギーはスティーブにキスをする。\n"
         "スティーブは車から飛び移り、ワルキューレの車輪にしがみついて、空へ飛び立つ機体に乗りこむ。",
         "A kiss, and a leap",
         "Steve chases the moving Valkyrie in a car with Phillips and Peggy. In the car, Peggy kisses him.\n"
         "Steve jumps from the car, grabs onto the Valkyrie's landing gear, and is carried aboard as it lifts into the sky."),
        ("都市の名前が書かれた爆弾",
         "ワルキューレの中には、ニューヨークなどアメリカの都市の名前が書かれた、爆弾つきの小さな飛行機が積まれていた。\n"
         "スティーブは機内のヒドラの兵隊と戦いながら、操縦室へ向かう。",
         "Bombs marked with city names",
         "Inside the Valkyrie are small bomb-carrying planes marked with the names of American cities, New York among them.\n"
         "Fighting off the Hydra crew, Steve makes his way toward the cockpit."),
        ("テッセラクトの光",
         "操縦室で、スティーブとシュミットがはげしく戦う。その中で、テッセラクトを収めた装置がこわれ、キューブが外へ転がり出る。\n"
         "シュミットがテッセラクトを素手でつかむと、キューブから光がふき出し、宇宙へ通じる穴が開く。シュミットは光の中へ吸いこまれて消える。テッセラクトは床を焼いて穴をあけ、海へ落ちていく。",
         "The Tesseract's light",
         "In the cockpit, Steve and Schmidt fight fiercely. The device holding the Tesseract breaks, and the cube tumbles free.\n"
         "Schmidt picks it up with his bare hand. Light pours out of the cube and opens a portal into space, and Schmidt is pulled into it and vanishes. The Tesseract burns through the floor and falls into the ocean."),
        ("北極へ",
         "ワルキューレはニューヨークへ向かっている。止める方法はなく、どこかに着陸させようとすれば爆弾が爆発するおそれがある。\n"
         "スティーブは、人のいない北極の氷に機体ごと突っこむと決める。",
         "Toward the Arctic",
         "The Valkyrie is on course for New York. There's no way to stop it, and trying to land could set off the bombs.\n"
         "Steve decides to bring it down in the empty Arctic ice."),
        ("無線の約束",
         "スティーブは無線でペギーと話す。2人は、次の土曜日の夜8時に店で会い、ダンスをする約束をする。ペギーは遅れないでと言う。\n"
         "機体が氷に近づき、スティーブの声は途切れる。ペギーは無線の雑音だけが聞こえる部屋で泣く。",
         "The radio promise",
         "Steve talks to Peggy over the radio. They make a date: Saturday night, eight o'clock, a dance at the Stork Club. \"Don't you dare be late,\" she tells him.\n"
         "The plane nears the ice and his voice cuts out. Peggy weeps, listening to nothing but static."),
        ("戦争の終わり",
         "ハワードは海で捜索を続け、海の底からテッセラクトを引き上げる。しかしワルキューレもスティーブも見つからず、スティーブは死んだものとされる。\n"
         "やがて戦争が終わり、街は喜びにわく。ハウリング・コマンドーズは静かに酒をかかげ、ペギーはスティーブの書類の写真を見つめる。",
         "The war ends",
         "Howard keeps searching the sea and recovers the Tesseract from the ocean floor. But neither the Valkyrie nor Steve is found, and Steve is presumed dead.\n"
         "The war ends and the streets erupt in celebration. The Howling Commandos raise a quiet drink, and Peggy looks at the photo in Steve's file."),
    ]),
    ("第8部 70年後の目覚め", "Part 8: Waking up 70 years later", [
        ("1940年代の部屋",
         "スティーブは、1940年代風の病室のベッドで目を覚ます。ラジオから野球の試合の中継が流れている。\n"
         "しかしそれは、1941年にスティーブが実際に球場で見た試合だった。部屋に入ってきた女性に、スティーブはここはどこだと問いつめ、ここが作られた場所だと見破る。",
         "A 1940s room",
         "Steve wakes in a 1940s-style hospital room. A baseball game is playing on the radio.\n"
         "But it is a 1941 game he went to in person. When a woman comes in, he demands to know where he is, having realized the room is a setup."),
        ("タイムズスクエア",
         "スティーブは壁を突き破って建物を飛び出し、通りを走る。たどり着いたのは、大きな画面と車と人であふれる現代のニューヨーク、タイムズスクエアだった。\n"
         "立ちつくすスティーブの前に車が止まり、S.H.I.E.L.D.の長官ニック・フューリーが現れて、彼が70年近く眠っていたことを告げる。",
         "Times Square",
         "Steve bursts through a wall and runs out into the street. He ends up in Times Square, modern New York, crowded with giant screens, traffic and people.\n"
         "As he stands frozen, cars pull up and S.H.I.E.L.D. Director Nick Fury steps out to tell him he has been asleep for almost 70 years."),
        ("デートの約束",
         "大丈夫かとたずねられたスティーブは、大丈夫だと答え、デートの約束があったのだとつぶやく。土曜の夜にペギーと会う約束は、もう果たせない。",
         "The date",
         "Asked if he's all right, Steve says he is, then adds quietly, \"I just... I had a date.\" The Saturday night with Peggy will never happen."),
        ("エンドクレジットの後",
         "ジムで1人、サンドバッグをなぐり続けるスティーブのもとへフューリーが来る。フューリーは、世界にかかわる任務をスティーブに持ちかける。\n"
         "そのあと、次の作品『アベンジャーズ』の予告映像が流れる。",
         "After the credits",
         "Steve is alone in a gym, pounding a punching bag, when Fury arrives and offers him a mission with worldwide stakes.\n"
         "A preview of the next film, The Avengers, follows."),
    ]),
    ("まとめ（最後までのネタバレ）", "Summary (full spoilers)", [
        ("スティーブの歩み",
         "体が弱く何度も不合格になったスティーブは、弱い者を守ろうとする心をアースキン博士に見こまれ、超人血清で強い体を手に入れた（第2部〜第3部）。\n"
         "しかし博士が殺され、血清の作り方が失われたため、最初は戦場に出してもらえず、宣伝のショーで「キャプテン・アメリカ」を演じた（第4部）。\n"
         "命令を破ってバッキーたち捕虜を1人で助け出したことで本物の英雄になり（第5部）、ハウリング・コマンドーズを率いてヒドラと戦った（第6部）。最後はワルキューレを北極に沈め、70年近く氷の中で眠ったあと、現代で目を覚ました（第7部〜第8部）。",
         "Steve's journey",
         "Frail and rejected again and again, Steve was chosen by Erskine for his urge to protect others, and the serum gave him a powerful body (Parts 2–3).\n"
         "But Erskine was killed and the formula lost, so at first Steve was kept off the battlefield and played \"Captain America\" in a promotional show (Part 4).\n"
         "Disobeying orders to rescue Bucky and the other prisoners on his own made him a real hero (Part 5), and he led the Howling Commandos against Hydra (Part 6). In the end he brought the Valkyrie down in the Arctic, slept in the ice for almost 70 years, and woke up in the present (Parts 7–8)."),
        ("テッセラクトのゆくえ",
         "シュミットがノルウェーで奪い（第1部）、ゾラ博士がその力で兵器を動かした（第3部）。\n"
         "最後の戦いでシュミットが素手でつかむと宇宙への穴が開き、シュミットは消えた。テッセラクトは海へ落ち、ハワードが海の底から引き上げた（第7部）。このキューブは、このあとのMCUの作品に何度も出てくる。",
         "Where the Tesseract went",
         "Schmidt took it in Norway (Part 1), and Zola used its power to run Hydra's weapons (Part 3).\n"
         "In the final fight Schmidt grabbed it bare-handed; it opened a portal into space and he vanished. The cube fell into the ocean, and Howard recovered it from the sea floor (Part 7). It turns up again and again in later MCU films."),
        ("死んだ人・いなくなった人（話の順に）",
         "・アースキン博士（第4部）：実験が成功した直後、見学者にまぎれていたヒドラの刺客クルーガーに撃たれて亡くなる。血清の作り方を知っていたのは博士だけだった。\n"
         "・クルーガー（第4部）：スティーブにつかまり、取り調べを受ける前に、かくしていた毒のカプセルをかんで自ら命を絶つ。\n"
         "・バッキー（第6部）：ゾラ博士の列車での戦いで、敵の攻撃で車両の外へ投げ出され、手すりが折れて谷底へ落ちる。この映画では死んだものとされる。\n"
         "・シュミット（第7部）：テッセラクトを素手でつかみ、光の中へ吸いこまれて消える。死んだかどうかは、この映画でははっきりしない。\n"
         "・スティーブ（第7部〜第8部）：ワルキューレを北極に沈め、死んだものとされた。実は氷の中で眠っていて、70年近くたった現代で目を覚ます。",
         "Who died or disappeared (in order)",
         "- Dr. Erskine (Part 4): shot right after the procedure succeeds by Kruger, a Hydra assassin posing as an observer. He was the only one who knew how to make the serum.\n"
         "- Kruger (Part 4): caught by Steve, he bites a hidden cyanide capsule and kills himself before he can be questioned.\n"
         "- Bucky (Part 6): during the fight on Zola's train, an enemy blast throws him out of the car; the rail he hangs from snaps and he falls into the ravine. The film treats him as dead.\n"
         "- Schmidt (Part 7): grabs the Tesseract bare-handed and is pulled into its light and vanishes. The film leaves unclear whether he died.\n"
         "- Steve (Parts 7–8): presumed dead after bringing the Valkyrie down in the Arctic. In fact he lay frozen in the ice and wakes up nearly 70 years later."),
    ]),
]
