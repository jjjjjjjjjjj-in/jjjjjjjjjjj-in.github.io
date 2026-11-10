# 『X-MEN：フューチャー&パスト』（2014年）シーンごとの詳しいあらすじ
# 2026-11-10 書き直し。英語版ウィキペディアのあらすじ（今の版と、2015・2017・2019年の版）、日本語版ウィキペディアのストーリーと照らし合わせて、順番と事実を確かめた。
# 運営者の希望（あらすじの直し方）: 第1部から始め、場面ごとに起きた事実だけを書く。見出しはつながった場面でまとめる。
# 資料どうしで順番が食い違う所（サイゴンの場面がペンタゴンの脱獄の前か後か）は「そのころ」として、前後をはっきり書いていない。
# 資料で確かめられなかった所（最初のナレーションの言葉、トラスクの研究所でミスティークが見た資料の中身、未来の戦いで誰がどの順に倒れたか、など）は書いていない。
# セリフは日本語の言い回しを確かめられなかったので、日本語版はカギかっこで引用せず内容だけ書いた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 2023年、滅びかけた未来", "Part 1: 2023, a dying future", [
        ("センチネルの時代",
         "2023年。ミュータントを狩るロボット「センチネル」が、世界中でミュータントを捕まえ、殺していた。ねらわれるのはミュータントだけではない。ミュータントの子が生まれるかもしれない人間や、ミュータントを助けようとする人間も、同じように狩られている。街は焼け野原になっている。",
         "The age of Sentinels",
         "2023. Robots called Sentinels are hunting down and killing mutants all over the world. Not only mutants: humans who might one day have mutant children, and humans who try to protect mutants, are hunted too. Cities lie in ruins."),
        ("モスクワの隠れ家",
         "モスクワの隠れ家に、生き残ったX-MENの仲間たち、キティ・プライド、コロッサス、ブリンク、ウォーパス、ビショップ、アイスマン（ボビー）、サンスポットがひそんでいる。そこへセンチネルの群れが襲いかかる。\n"
         "センチネルは、相手の力に合わせて自分の体を変えられる。氷にも炎にも負けず、仲間たちは次々に倒されていく。",
         "The Moscow hideout",
         "In a hideout in Moscow, the surviving X-Men, Kitty Pryde, Colossus, Blink, Warpath, Bishop, Iceman (Bobby) and Sunspot, are hiding. A swarm of Sentinels attacks.\n"
         "The Sentinels can change their bodies to counter any power. Neither ice nor fire stops them, and the mutants fall one after another."),
        ("数日前へ送られたビショップ",
         "仲間たちが命がけで時間をかせぐあいだに、キティはビショップの心を、数日前のビショップの体へ送る。\n"
         "過去で目を覚ましたビショップは、襲撃が来ることを仲間に知らせる。皆は襲われる前に隠れ家を捨てて逃げ、全員が生き延びる。キティのこの力で、彼らはこれまで何度も生き残ってきた。",
         "Bishop is sent back",
         "While the others sacrifice themselves to buy time, Kitty sends Bishop's mind back into his own body a few days earlier.\n"
         "Waking in the past, Bishop warns the group that the attack is coming. They abandon the hideout before the Sentinels arrive, and everyone survives. Kitty's power has kept them alive this way many times."),
        ("中国の寺院",
         "一行は、中国の山奥にある寺院に逃げこむ。そこへストーム、ローガン、マグニートー、そしてプロフェッサーX（チャールズ・エグゼビア）がやって来て合流する。",
         "The temple in China",
         "The group retreats to a remote temple in the mountains of China. Storm, Logan, Magneto and Professor X (Charles Xavier) arrive and join them."),
        ("すべての始まり",
         "プロフェッサーXは、センチネルが生まれたいきさつを話す。センチネルを考え出したのは、兵器の開発者ボリバー・トラスクだった。1973年、トラスクはミスティーク（レイブン）に殺された。\n"
         "この事件をきっかけに、政府はトラスクの計画を認めた。捕まったミスティークは痛めつけられ、体を調べられた。どんな姿にも変われる彼女の体のしくみ（DNA）を使って、どんな力にも合わせられるセンチネルが作られたのだった。",
         "Where it all began",
         "Professor X explains how the Sentinels came to be. They were the idea of Bolivar Trask, a weapons designer. In 1973, Trask was assassinated by Mystique (Raven).\n"
         "After that, the government approved Trask's program. Mystique was captured, tortured and experimented on, and her shape-shifting DNA was used to build Sentinels that could adapt to any mutant power."),
        ("ローガンが行く",
         "プロフェッサーXは、キティの力で自分の心を1973年へ送り、暗殺を止めるつもりだった。しかし、何十年も前へさかのぼると、心も体も耐えられず、プロフェッサーXは死んでしまう。\n"
         "そこでローガンが、自分が行くと名乗り出る。傷がすぐに治るローガンなら耐えられる。プロフェッサーXとマグニートーは、1973年の若い自分たちを探して力を借りるようローガンに頼む。\n"
         "ローガンが横になり、キティがその頭に手をかざす。",
         "Logan goes instead",
         "Xavier planned to have Kitty send his own mind back to 1973 to stop the assassination. But going back decades would destroy him; it would kill him.\n"
         "Logan volunteers instead. His healing power will let him survive. Xavier and Magneto ask him to find their younger selves in 1973 and get their help.\n"
         "Logan lies down, and Kitty places her hands at his head."),
    ]),
    ("第2部 1973年の目覚め", "Part 2: Waking up in 1973", [
        ("1973年の朝",
         "ローガンは、1973年の自分の体で目を覚ます。このころのローガンは、マフィアのボスの娘の用心棒をしていた。\n"
         "部屋に、銃を持った男たちが押し入ってくる。ローガンは男たちを倒すが、手から出た爪は金属ではなく、骨のままだった。まだ骨に金属（アダマンチウム）を埋めこまれる前の体なのだ。ローガンは車を奪って、その場を去る。",
         "A morning in 1973",
         "Logan wakes up in his 1973 body. At this time he is working as a bodyguard for a mob boss's daughter.\n"
         "Armed men burst into the room. Logan takes them down, but the claws that come out of his hands are bone, not metal. His skeleton has not yet been laced with adamantium. He steals a car and leaves."),
        ("閉ざされた学園",
         "ローガンは、ニューヨーク州ウエストチェスターにあるエグゼビアの屋敷を訪ねる。門に出てきたのは、若いハンク・マッコイだった。\n"
         "学園は何年も前に閉じていた。先生や生徒の多くがベトナム戦争に兵隊として取られ、いなくなってしまったからだ。",
         "The closed school",
         "Logan goes to Xavier's mansion in Westchester, New York. The young Hank McCoy answers.\n"
         "The school closed years ago: most of the teachers and students were drafted into the Vietnam War and never came back."),
        ("若いチャールズ",
         "屋敷の奥にいた若いチャールズは、すっかり気力を失い、酒におぼれていた。\n"
         "チャールズは、ハンクの作った薬を使っている。この薬を打つと、足が動いて歩けるようになるが、そのかわりに心を読む力が消える。チャールズは、他人の心の声が聞こえる苦しさから逃げるために、薬を使い続けていた。",
         "The young Charles",
         "Inside, the young Charles has given up on everything and is drinking heavily.\n"
         "He is using a serum Hank made. It lets him walk, but it takes away his telepathy. Charles keeps taking it to escape the pain of hearing everyone's thoughts."),
        ("未来からの頼み",
         "ローガンは、自分が未来から来たことと、未来で何が起きるかを話す。チャールズは初めは相手にしない。\n"
         "しかし、ミスティーク（レイブン）を止めなければならないと聞き、レイブンにもう一度会いたいと思ったチャールズは、ローガンに手を貸すことにする。",
         "A request from the future",
         "Logan explains that he has come from the future, and what is going to happen. At first Charles brushes him off.\n"
         "But when he hears that Raven has to be stopped, and hoping to see her again, Charles agrees to help."),
        ("ペンタゴンの地下のエリック",
         "ローガンには、若いエリック（マグニートー）の力も必要だった。エリックは、1963年のジョン・F・ケネディ大統領の暗殺の犯人として捕まり、ペンタゴン（アメリカの国防総省）の地下深くの牢屋に入れられていた。\n"
         "金属をまったく使っていない牢屋で、エリックの力は使えない。",
         "Erik under the Pentagon",
         "Logan also needs the young Erik (Magneto). Erik was arrested for the 1963 assassination of President John F. Kennedy and is locked in a cell deep beneath the Pentagon.\n"
         "The cell contains no metal, so his power is useless there."),
    ]),
    ("第3部 ペンタゴンの脱獄", "Part 3: The Pentagon breakout", [
        ("ピーターの家",
         "ローガン、チャールズ、ハンクは、ものすごい速さで走れる少年ピーター・マキシモフ（クイックシルバー）の家を訪ね、手伝いを頼む。ピーターは引き受ける。",
         "Peter's house",
         "Logan, Charles and Hank visit Peter Maximoff (Quicksilver), a teenager who can run at superhuman speed, and ask for his help. Peter agrees."),
        ("ペンタゴンへ",
         "一行はペンタゴンに入りこむ。ピーターの速さで警備をくぐり抜け、エリックの牢屋にたどり着いて、エリックを連れ出す。",
         "Into the Pentagon",
         "The group slips into the Pentagon. Using Peter's speed to get past security, they reach Erik's cell and bring him out."),
        ("台所の一瞬",
         "逃げる途中の台所で、警備の兵士たちに囲まれ、銃を向けられる。\n"
         "兵士たちが撃った瞬間、ピーターが目にもとまらない速さで動き回り、弾の向きを変え、兵士たちを倒してしまう。ほかの者には、一瞬のできごとにしか見えない。",
         "One moment in the kitchen",
         "On the way out, guards corner them in a kitchen and open fire.\n"
         "In that instant Peter moves faster than the eye can follow, nudging the bullets off course and knocking out the guards. To everyone else, it's over in a blink."),
        ("エリックの言い分",
         "一行はペンタゴンを抜け出し、ピーターとはここで別れる。\n"
         "エリックは、自分はケネディを殺したのではなく、助けようとしたのだと話す。ケネディもミュータントだったという。",
         "Erik's side of the story",
         "They escape the Pentagon, and part ways with Peter.\n"
         "Erik says he didn't kill Kennedy: he was trying to save him. Kennedy, he says, was a mutant too."),
    ]),
    ("第4部 そのころのミスティーク", "Part 4: Meanwhile, Mystique", [
        ("議会のトラスク",
         "ワシントンでは、トラスクがアメリカの議会でミュータントの危険を訴え、センチネル計画への協力を求める。しかし議員たちは乗り気にならず、計画は認められない。",
         "Trask before Congress",
         "In Washington, Trask warns Congress about the danger of mutants and asks for support for his Sentinel program. The lawmakers are not convinced, and the program is turned down."),
        ("サイゴンの基地",
         "ベトナムのサイゴンにある米軍の基地。兵士に化けたミスティークが忍びこむ。\n"
         "基地では、ウィリアム・ストライカー少佐が、ハヴォック、トード、インクなどミュータントの兵士たちを捕らえていた。ミスティークは彼らを助け出し、彼らがトラスクの研究のために連れて行かれるところだったと知る。",
         "The base in Saigon",
         "At a U.S. Army base in Saigon, Vietnam, Mystique sneaks in disguised as a soldier.\n"
         "Major William Stryker is holding mutant soldiers, including Havok, Toad and Ink. Mystique frees them, and learns they were about to be handed over to Trask for his research."),
        ("トラスクの秘密",
         "ミスティークはトラスクの研究所に忍びこみ、トラスクがミュータントを捕まえて実験していたことを知る。\n"
         "ミスティークは、パリでの和平会談に出るトラスクを、そこで殺そうと決める。",
         "Trask's secret",
         "Mystique sneaks into Trask's facility and discovers he has been capturing mutants and experimenting on them.\n"
         "She decides to kill Trask in Paris, where he will be attending the peace talks."),
    ]),
    ("第5部 パリ和平会談", "Part 5: The Paris Peace Accords", [
        ("パリへの飛行機",
         "チャールズ、エリック、ハンク、ローガンの4人は、飛行機でパリへ向かう。パリでは、ベトナム戦争を終わらせるための和平会談が開かれている。",
         "The flight to Paris",
         "Charles, Erik, Hank and Logan fly to Paris, where peace talks to end the Vietnam War are under way."),
        ("会場のトラスク",
         "会場には、トラスクがストライカーと一緒に現れる。トラスクは、センチネルの技術をほかの国々に売りこもうとしていた。\n"
         "ミスティークは北ベトナム軍の将校に化けて会場にまぎれこむが、トラスクのミュータント探知機が反応し、正体がばれる。ミスティークは変身を解き、トラスクに襲いかかる。",
         "Trask at the talks",
         "Trask arrives at the talks with Stryker. He is trying to sell Sentinel technology to other countries.\n"
         "Mystique slips in disguised as a North Vietnamese officer, but Trask's mutant detector goes off and exposes her. She drops her disguise and goes after Trask."),
        ("止めに入った4人",
         "ミスティークがトラスクを殺そうとしたその時、チャールズたちが部屋に飛びこみ、それを止める。\n"
         "ところがエリックは、ミスティークが死ねば彼女の体がセンチネルに使われることはないと考え、ミスティークを殺そうと銃を撃つ。",
         "Four arrive to stop her",
         "Just as Mystique is about to kill Trask, Charles and the others burst in and stop her.\n"
         "But Erik decides that if Mystique dies, her DNA can never be used for the Sentinels, and he opens fire on her."),
        ("曲がる銃弾",
         "ミスティークは窓から飛び出して逃げる。エリックは力で銃弾の向きを曲げ、ミスティークの脚に命中させる。\n"
         "ハンクは獣のような青い姿に変わってエリックに飛びかかり、そのすきにミスティークは逃げのびる。",
         "The bending bullet",
         "Mystique leaps out of a window. Erik bends the bullet's path with his power and hits her in the leg.\n"
         "Hank transforms into his blue, beast-like form and tackles Erik, and in the confusion Mystique gets away."),
        ("人前での戦い",
         "戦いは外の通りにまで広がり、大勢の人やカメラの前で、ミュータントの力がむき出しになる。エリックも騒ぎにまぎれて姿を消す。\n"
         "トラスクは助かった。しかし、世界中の人がミュータントの存在を知り、おびえることになる。",
         "A fight in public",
         "The fight spills out onto the street, in front of crowds and cameras, and mutant powers are on full display. Erik also vanishes in the chaos.\n"
         "Trask survives. But now the whole world knows mutants exist, and is frightened."),
        ("未来のローガンの乱れ",
         "パリで、ローガンは若いストライカーを見かける。のちに自分の体に金属を埋めこむことになる男だった。ローガンの心は大きく乱れる。\n"
         "その乱れは2023年の寺院に横たわるローガンの体にも伝わり、両手から金属の爪が飛び出して、そばにいたキティを傷つけてしまう。それでもキティは手を離さない。",
         "Logan loses control",
         "In Paris, Logan catches sight of the young Stryker, the man who will one day put metal in his bones. Logan is badly shaken.\n"
         "The shock reaches his body lying in the temple in 2023: metal claws shoot from both hands and wound Kitty. Even so, she does not let go."),
    ]),
    ("第6部 動き出すセンチネル計画", "Part 6: The Sentinel program moves forward", [
        ("大統領の許可",
         "パリの事件を見たリチャード・ニクソン大統領は、トラスクとストライカーの説得を受けて、センチネル計画を認める。トラスクは、完成したセンチネルをホワイトハウスで披露すると約束する。",
         "The President says yes",
         "After the events in Paris, President Richard Nixon is persuaded by Trask and Stryker to approve the Sentinel program. Trask promises to unveil the finished Sentinels at the White House."),
        ("通りに残った血",
         "トラスクの部下たちは、パリの通りに残っていたミスティークの血を集めて持ち帰る。暗殺は防いだが、ミスティークの体のしくみは、こうしてトラスクの手に渡ってしまう。",
         "Blood on the street",
         "Trask's people collect the blood Mystique left on the street in Paris. The assassination was stopped, but her DNA still ends up in Trask's hands."),
        ("エリックの仕掛け",
         "エリックは、チャールズの力から心を守るヘルメットを取り戻す。\n"
         "そして、運ばれている途中のセンチネルの試作品を見つけ出す。センチネルは金属ではない素材で作られていたが、エリックはその骨組みに鉄をしみこませ、自分の力で操れるようにする。",
         "Erik's plan",
         "Erik recovers his helmet, the one that shields his mind from Charles.\n"
         "Then he tracks down the Sentinel prototypes while they are being shipped. Their frames are made of a non-metal material, but Erik laces them with steel so that he can control them."),
        ("薬をやめたチャールズ",
         "屋敷に戻ったチャールズは、薬をやめる。足は再び動かなくなるが、少しずつ心を読む力が戻ってくる。",
         "Charles quits the serum",
         "Back at the mansion, Charles stops taking the serum. He loses the use of his legs again, but slowly his telepathy returns."),
        ("未来の自分との対話",
         "チャールズは、ローガンの心の中に入りこみ、ローガンを通して、未来の年をとった自分と向き合う。\n"
         "未来の自分の言葉に励まされたチャールズは、人間とミュータントがともに生きる未来のために、もう一度立ち上がろうと決める。",
         "Talking to his future self",
         "Charles reaches into Logan's mind and, through him, comes face to face with his older self from the future.\n"
         "Inspired by his future self, Charles decides to fight once more for a future where humans and mutants live together."),
        ("セレブロ",
         "チャールズは、世界中の人の心とつながる装置セレブロを使い、ミスティークを探す。ミスティークは、ワシントンへ向かおうとしていた。\n"
         "チャールズはミスティークに直接語りかけるが、ミスティークはトラスクを殺すことがミュータントのためだと考え、聞き入れない。チャールズ、ハンク、ローガンはワシントンへ向かう。",
         "Cerebro",
         "Charles uses Cerebro, the machine that connects him to minds all over the world, to find Mystique. She is on her way to Washington.\n"
         "He speaks to her directly, but she believes killing Trask is the right thing for mutants and refuses to listen. Charles, Hank and Logan head for Washington."),
    ]),
    ("第7部 ホワイトハウスの決戦", "Part 7: Showdown at the White House", [
        ("披露の式典",
         "ホワイトハウスの庭で、ニクソン大統領がセンチネルの試作品を披露する式典が開かれる。チャールズたちは、群衆の中にまぎれたミスティークを探す。\n"
         "チャールズは心を読む力で、シークレットサービス（大統領の護衛）の一人に化けているミスティークを見つけ出す。",
         "The unveiling",
         "On the White House grounds, President Nixon holds a ceremony to unveil the Sentinel prototypes. Charles and the others search the crowd for Mystique.\n"
         "Using his telepathy, Charles spots her: she is disguised as one of the Secret Service agents guarding the President."),
        ("動き出したセンチネル",
         "そこへヘルメットをかぶったエリックが現れ、センチネルを動かして群衆を襲わせる。式典は大混乱になる。",
         "The Sentinels come alive",
         "Then Erik appears, wearing his helmet, and turns the Sentinels on the crowd. The ceremony descends into chaos."),
        ("スタジアムの壁",
         "エリックは近くの野球場、RFKスタジアムを丸ごと持ち上げて運び、ホワイトハウスのまわりに下ろして、外から入れないようにする。\n"
         "大統領とトラスク、閣僚たちは、護衛に囲まれてホワイトハウスの地下の避難室へ逃げこむ。護衛に化けたミスティークも一緒だった。",
         "A wall made of a stadium",
         "Erik lifts the nearby RFK Stadium whole, carries it through the air and sets it down around the White House, sealing it off.\n"
         "The President, Trask and the Cabinet are rushed by their guards into the underground shelter beneath the White House. Mystique, still disguised as a guard, goes with them."),
        ("ポトマック川",
         "ハンクは青い姿に変わってセンチネルと戦う。ローガンはエリックに立ち向かうが、エリックは鉄筋をローガンの体に突き刺し、ポトマック川へ投げ飛ばす。ローガンは川の底へ沈んでいく。\n"
         "チャールズは、くずれたスタジアムのがれきの下じきになり、動けなくなる。",
         "The Potomac River",
         "Hank changes into his blue form and fights a Sentinel. Logan goes after Erik, but Erik drives steel rebar into Logan's body and hurls him into the Potomac River. Logan sinks to the bottom.\n"
         "Charles is pinned under wreckage from the stadium and cannot move."),
        ("引き抜かれた避難室",
         "1973年。エリックは避難室を建物から丸ごと引き抜いて外へ出し、センチネルを使って、中にいる大統領や閣僚、トラスクを殺そうとする。\n"
         "その様子はテレビで中継され、エリックは大統領たちに銃を向けたまま、世界に向けて語りかける。",
         "The shelter torn out",
         "In 1973, Erik rips the shelter out of the building and sets out to kill everyone inside with the Sentinels: the President, the Cabinet and Trask.\n"
         "The scene is broadcast on television, and with guns trained on the President and his officials, Erik speaks to the world."),
        ("未来の最後の戦い",
         "そのころ2023年の寺院も、ついにセンチネルの大群に見つかる。仲間たちは、1973年のローガンが役目を果たすまでの時間をかせごうと戦う。\n"
         "相手の力に合わせて姿を変えるセンチネルに、ストーム、コロッサス、ボビーをはじめ、ほとんどの仲間が倒されていく。残ったのは、チャールズ、キティ、けがをしたマグニートー、眠り続けるローガンだけになる。",
         "The last stand in the future",
         "Meanwhile in 2023, a huge army of Sentinels finally finds the temple. The mutants fight to buy time for Logan to finish his mission in 1973.\n"
         "The Sentinels adapt to every power, and Storm, Colossus, Bobby and most of the others are killed. Only Charles, Kitty, a wounded Magneto and the sleeping Logan remain."),
        ("大統領の姿のミスティーク",
         "そのとき、ニクソン大統領に化けていたミスティークが、金属を使っていないプラスチックの拳銃で、エリックの首を撃つ。エリックは倒れる。",
         "Mystique as the President",
         "Then Mystique, disguised as President Nixon, shoots Erik in the neck with a plastic gun that contains no metal. Erik goes down."),
        ("ミスティークの選択",
         "ミスティークは次にトラスクに銃を向ける。チャールズは心の力でミスティークに語りかけ、撃たないでほしいと説得する。ミスティークは、トラスクを撃たずに銃を下ろす。\n"
         "その瞬間、歴史が変わる。2023年の寺院で、残った仲間たちにセンチネルが迫ったまさにそのとき、暗い未来そのものが消えていく。",
         "Mystique's choice",
         "Mystique then aims at Trask. Charles reaches her mind and pleads with her not to shoot. She lowers the gun without firing.\n"
         "In that moment, history changes. In the 2023 temple, just as the Sentinels close in on the last survivors, the dark future itself fades away."),
        ("去っていく2人",
         "ミスティークがエリックのヘルメットをはずすと、チャールズはエリックの心を操り、自分の上のがれきをどけさせる。エリックは空のかなたへ去り、ミスティークも兵士に化けて立ち去る。\n"
         "世界の人々は、ミュータントが大統領と閣僚たちの命を救ったのを目にする。センチネル計画は取りやめになり、トラスクはのちに、軍の秘密を外国に売ろうとした罪で捕まる。",
         "Two walk away",
         "When Mystique pulls off Erik's helmet, Charles takes control of Erik's mind and has him lift the wreckage off of him. Erik flies off into the sky, and Mystique, disguised as a soldier, walks away.\n"
         "The world has seen a mutant save the President and his Cabinet. The Sentinel program is shut down, and Trask is later arrested for trying to sell military secrets to foreign governments."),
    ]),
    ("第8部 新しい未来", "Part 8: A new future", [
        ("学園で目覚める",
         "ローガンは、2023年のエグゼビアの屋敷で目を覚ます。学園は生徒であふれ、にぎわっていた。",
         "Waking at the school",
         "Logan wakes up at Xavier's mansion in 2023. The school is thriving and full of students."),
        ("戻ってきた仲間",
         "屋敷には、ボビー、ローグ、コロッサス、キティ、ハンク、ストームがいて、死んだはずのジーン・グレイとスコット・サマーズ（サイクロップス）も生きていた。\n"
         "ローガンはプロフェッサーXと会い、1973年から今までに何があったのかを教えてほしいとプロフェッサーXに頼む。",
         "Friends returned",
         "Bobby, Rogue, Colossus, Kitty, Hank and Storm are all there, and so are Jean Grey and Scott Summers (Cyclops), who had died in the old history.\n"
         "Logan meets Professor X and asks him to tell him what has happened between 1973 and now."),
        ("1973年の川",
         "1973年。ポトマック川の底に沈んだローガンは、軍の船に引き上げられる。指揮をとるストライカー少佐がローガンを引き取るが、その目が黄色く光る。ストライカーに化けていたのは、ミスティークだった。",
         "The river in 1973",
         "In 1973, Logan is pulled from the bottom of the Potomac by a military boat. Major Stryker, in charge, takes custody of him, but his eyes flash yellow. It is Mystique in disguise."),
        ("エンドクレジットの後",
         "大昔のエジプト。ひれ伏す大勢の人々が、エン・サバ・ヌールという人物の名を唱えている。エン・サバ・ヌールは力で岩を浮かせてピラミッドを築き、遠くから4人の騎士がそれを見守っている。",
         "After the credits",
         "Ancient Egypt. A bowing crowd chants the name of En Sabah Nur, who raises stones with his mind to build the pyramids, while four horsemen watch from a distance."),
    ]),
    ("まとめ", "Summary", [
        ("大事な筋",
         "1) 2023年、キティの力でローガンの心が1973年の体に送られ、ミスティークがトラスクを殺す事件を止めようとする（第1部）。\n"
         "2) ローガンは、薬で力を失っていた若いチャールズとハンクを仲間にし、ピーターの力でエリックをペンタゴンから連れ出す（第2・3部）。\n"
         "3) パリでミスティークの暗殺は止めたが、エリックが彼女を撃ち、ミュータントの存在が世界に知られる。大統領はセンチネル計画を認め、トラスクはミスティークの血を手に入れる（第5・6部）。\n"
         "4) チャールズは薬をやめて力を取り戻し、ローガンの心を通して未来の自分と話し、もう一度立ち上がる（第6部）。\n"
         "5) ホワイトハウスで、エリックがセンチネルで大統領たちを殺そうとする。ミスティークがエリックを撃って大統領を救い、チャールズの説得でトラスクも撃たない。センチネル計画は取りやめになり、暗い未来は消える（第7部）。\n"
         "6) ローガンは、ジーンやスコットも生きている新しい2023年で目覚める。1973年のローガンは、ストライカーに化けたミスティークに引き取られる（第8部）。",
         "Key story points",
         "1) In 2023, Kitty sends Logan's mind into his 1973 body to stop Mystique from assassinating Trask (Part 1).\n"
         "2) Logan recruits the young Charles, who has lost his powers to the serum, and Hank, and with Peter's help they break Erik out of the Pentagon (Parts 2-3).\n"
         "3) In Paris the assassination is stopped, but Erik shoots Mystique and the world learns that mutants exist. The President approves the Sentinels, and Trask obtains Mystique's blood (Parts 5-6).\n"
         "4) Charles quits the serum, gets his powers back, speaks to his future self through Logan's mind, and finds his purpose again (Part 6).\n"
         "5) At the White House, Erik tries to kill the President and others with the Sentinels. Mystique shoots Erik and saves the President, and, persuaded by Charles, spares Trask too. The Sentinel program is cancelled and the dark future is erased (Part 7).\n"
         "6) Logan wakes in a new 2023 where Jean and Scott are alive. In 1973, Mystique, disguised as Stryker, takes custody of Logan (Part 8)."),
        ("死んだ人",
         "・トラスク（元の歴史）：1973年、ミュータントを実験に使っていたことへの怒りから、ミスティークに殺された。この事件がセンチネルを生んだ。この映画で歴史が変わり、殺されなかったことになる（第1部・第7部）。\n"
         "・モスクワの仲間たち（第1部）：センチネルの襲撃で倒されるが、ビショップが数日前に戻って知らせたので、襲撃そのものがなかったことになる。\n"
         "・寺院の仲間たち、ストーム、コロッサス、ボビーなど（第7部）：ローガンの時間をかせぐために戦い、センチネルに倒される。歴史が変わり、新しい未来では生きている。",
         "Who died",
         "- Trask (original history): killed by Mystique in 1973, out of anger at his experiments on mutants; his death led to the Sentinels. In this film history changes and he is not killed (Parts 1 and 7).\n"
         "- The mutants in Moscow (Part 1): killed in the Sentinel attack, but Bishop goes back a few days and warns them, so the attack never happens.\n"
         "- The mutants at the temple, including Storm, Colossus and Bobby (Part 7): killed by the Sentinels while buying time for Logan. History changes, and they are alive in the new future."),
    ]),
]
