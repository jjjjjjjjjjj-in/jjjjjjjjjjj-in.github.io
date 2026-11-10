# 『アガサ・オール・アロング』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（第1話から始め、場面ごとに起きた事実だけ）。
# 英語版ウィキペディアの各話の記事（Plot と制作の節）・人物の記事（Agatha Harkness、Death など）、
# 日本語版ウィキペディア（話の題名・人物の説明）で事実と順番を確かめた。
# 解説記事のサイトはこの環境から読めなかったので、ウィキペディアで確かめられたことだけを書いている。
# 日本語の吹替・字幕の言い回しは確かめられなかったので、日本語版ではせりふをカギかっこで引用せず、内容だけを書いている。
# 資料どうしで食い違う所（アガサが正体を思い出すきっかけの細部など）は書いていない。
# 人物名は相関図（relations.py）の表記に合わせた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「話-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1話 道を探せよ", "Episode 1: Seekest Thou the Road", [
        ("刑事アグネス・オコナー",
         "ドラマ『アグネス・オブ・ウエストビュー』の偽のオープニングから始まる。主題歌は、のちに何度も出てくる「魔女の道のバラード」の、刑事ドラマ風のアレンジだ。\n"
         "ウエストビューの町はずれで、身元の分からない女性の遺体が見つかる。現場に来たのは刑事アグネス・オコナー。正体はアガサだが、本人は自分を刑事だと思いこんでいる。\n"
         "アグネスは近くを調べてふしぎなロケット（ペンダント）を見つけ、殺されたのは別の場所だと考える。",
         "Detective Agnes O'Connor",
         "The episode opens with fake opening titles for a crime show, Agnes of Westview, set to a true-crime version of \"The Ballad of the Witches' Road,\" the song that will return again and again.\n"
         "A Jane Doe's body is found outside Westview. Detective Agnes O'Connor arrives on the scene. She is really Agatha, but she believes she is a detective.\n"
         "Searching nearby, Agnes finds a mysterious locket and decides the murder happened somewhere else."),
        ("図書館とFBIのリオ",
         "遺体が持っていたカードを手がかりに、アグネスは町の図書館へ行く。カードに記された本は3年前に盗まれていて、その本があった棚は火で焦げ、同じ本はすべて焼けていた。\n"
         "警察署では、FBI捜査官リオ・ヴィダルが現れる。昔からの知り合いで、アグネスはしぶしぶ一緒に捜査することになる。\n"
         "やがてアグネスは、盗まれた本の題名の頭文字をつなげると「ダークホールド」になることに気づく。",
         "The library and Agent Rio",
         "Following a card found on the body, Agnes goes to the town library. The book it lists was stolen three years ago, and a fire scorched the shelf where it stood, destroying every copy.\n"
         "At the station, FBI agent Rio Vidal shows up, an old acquaintance, and Agnes reluctantly teams up with her.\n"
         "Later, Agnes realizes the initials of the stolen book's title spell \"Darkhold.\""),
        ("家に忍びこんだ少年",
         "夜、リオがアグネスの家を訪ね、2人は事件について話す。アグネスは、なぜリオといがみ合うようになったのか思い出せないと言う。\n"
         "そこへ、1人の少年が家に忍びこんでくる。アグネスは少年を捕まえて覆面をはぎ、殺人事件にかかわっていると考えて取り調べる。",
         "A teen breaks in",
         "That night Rio visits Agnes at home to talk about the case. Agnes admits she can't remember why the two of them don't get along.\n"
         "A teenage burglar breaks into the house. Agnes catches him, pulls off his mask, and interrogates him about the murder."),
        ("くずれ始める世界",
         "取り調べの途中、少年はラテン語で呪文のようなものを唱える。するとアグネスは、遺体の写真だと思っていたものが花の写真で、取調室のマジックミラーがただの絵だと気づく。\n"
         "遺体安置所で遺体を確かめると、身元は「ワンダ・マキシモフ」と分かる。リオにうながされ、アグネスは自分にかけられた魔法を1枚ずつはがしていく。刑事アグネスの姿が消え、魔女アガサ・ハークネスが戻ってくる。",
         "The illusion cracks",
         "During the interrogation, the teen chants in Latin. Agnes realizes the \"crime-scene photos\" are pictures of flowers and the one-way mirror is just a painting.\n"
         "At the morgue, the victim is identified as Wanda Maximoff. Encouraged by Rio, Agnes peels away the layers of the spell. Agnes falls away, and the witch Agatha Harkness comes back."),
        ("3年ぶりのウエストビュー",
         "我に返ったアガサは、ウエストビューの自分の家にいた。魔法の力はなくなっている。\n"
         "近所のハーブから、ワンダの魔法で3年間閉じこめられていたこと、刑事としての暮らしはすべてまぼろしだったことを聞かされる。地下室へ下りると、魔法の道具はすべて持ち去られていた。\n"
         "物置の中には、しばられた少年がいた。アガサは、魔法にかかったまま自分が少年を閉じこめていたことに気づく。",
         "Back in Westview after three years",
         "Agatha comes to in her Westview home, and her magic is gone.\n"
         "Her neighbor Herb tells her she has been under Wanda's spell for three years and that her life as a detective was an illusion. In the basement, all her magical equipment has been taken.\n"
         "In a closet she finds the teen, tied up, and realizes she kidnapped him while under the spell."),
        ("リオの襲撃",
         "そこへリオがやって来る。リオは本当は魔女で、アガサに襲いかかる。\n"
         "激しい戦いの中、アガサは、力が戻るまで待ってくれれば正々堂々と戦えると頼む。リオは引き下がるが、アガサの居場所を、アガサを恨む魔女の集団「セイラム・セブン」に教えると言い残して去る。\n"
         "物置には少年がしばられたまま。アガサは、少年をどうするか決められずにいる。",
         "Rio attacks",
         "Rio arrives, revealed to be a witch, and attacks Agatha.\n"
         "As the fight escalates, Agatha asks Rio to wait until she has her powers back so it can be a fair fight. Rio backs off, but says she'll tell the Salem Seven, witches who hate Agatha, where she is.\n"
         "The teen is still tied up in the closet, and Agatha doesn't know what to do with him."),
    ]),
    ("第2話 いざ開かん 隠されし扉", "Episode 2: Circle Sewn with Fate / Unlock Thy Hidden Gate", [
        ("少年の頼み",
         "アガサはウエストビューを出ようとする。少年は、魔女の道に連れて行ってほしいと頼む。魔女の道は、いくつもの試練を乗りこえた魔女に、その人に足りないものを与えてくれるという道だ。\n"
         "アガサは初めはことわる。しかし、ワンダの魔法を解いたのは自分だと少年が明かし、さらに本人も知らないうちに、名前を言えなくする魔法がかけられていることを見せると、アガサは引き受ける。\n"
         "道に入るには魔女の仲間（カヴン）が必要だ。2人は町を出て、魔女を集めに行く。",
         "The teen's request",
         "Agatha is about to leave Westview when the teen asks her to take him down the Witches' Road, a series of trials that rewards witches with what they lack.\n"
         "She refuses at first. But he admits he undid the Scarlet Witch's spell, and he unknowingly shows a spell on him that stops him from saying his name. Agatha agrees.\n"
         "Walking the Road takes a coven, so the two leave Westview to recruit witches."),
        ("占いの魔女リリア",
         "最初に訪ねたのは占いの魔女リリア・カルデル。リリアは、アガサが魔女殺しとして知られていることを警戒する。\n"
         "アガサは、自分が力を吸い取れるのは、先に自分を攻撃してきた魔女からだけだと明かす。リリアは占いで、道を歩く運命の魔女の名前を書き出す。アガサは、その中にリリア自身の名前があると指さす。",
         "Lilia, the diviner",
         "First they visit the divination witch Lilia Calderu, who is wary of Agatha's reputation as a witch killer.\n"
         "Agatha reveals she can only absorb power from witches who attack her first. A vision leads Lilia to write a list of witches fated to join the coven, and Agatha points out Lilia's own name is on it."),
        ("薬の魔女ジェン",
         "次は薬の魔女ジェニファー（ジェン）・ケイル。ジェンは魔法を封じられていて、力を使えない。\n"
         "少年は、ジェンが売るスキンケア商品をめぐる裁判のことを持ち出す。アガサと少年は、一生刑務所に入るかもしれない状況から抜け出す道として、魔女の道を勧める。",
         "Jen, the potions witch",
         "Next is the potions witch Jennifer \"Jen\" Kale, whose magic is bound so she can't use it.\n"
         "The teen brings up a lawsuit over her skincare products, and the pair pitch the Road as her way out of a life sentence."),
        ("守りの魔女アリス",
         "ショッピングモールでは、守りの魔女アリス・ウー＝ガリヴァーを誘う。アリスの母は、「魔女の道のバラード」のいちばん有名な歌を歌ったロック歌手だった。\n"
         "アリスは、魔女の道なんて亡くなった母のファンが作った作り話だと言って、ことわる。",
         "Alice, the protection witch",
         "At a mall, they approach the protection witch Alice Wu-Gulliver, daughter of the rock singer who recorded the best-known version of the ballad.\n"
         "Alice turns them down, insisting the Road is a fiction invented by her late mother's fans."),
        ("聞こえない少年の話",
         "ウエストビューへ戻る車の中で、少年は自分のことを話す。しかしアガサには、少年の身の上の話がまったく聞き取れない。少年にかかった魔法のせいだ。",
         "Words she can't hear",
         "On the drive back to Westview, the teen talks about his life, but the spell on him means Agatha can't hear any of the personal details."),
        ("5人目は近所のシャロン",
         "アガサの家に魔女たちが集まる。来ないと思われたアリスも、やって来る。\n"
         "道には、もう1人、緑の魔女が必要だった。リリアの書き出したメモには、名前のない5人目が黒いハートの印で書かれていた。アガサが連れてきたのは、近所に住む園芸の得意な女性シャロン・デイヴィス。魔法は使えない。ワンダの魔法の中では「ハート夫人」と呼ばれていた人だ。",
         "Neighbor Sharon makes five",
         "The coven gathers at Agatha's house, and Alice unexpectedly shows up too.\n"
         "They still need a green witch. Lilia's note lists an unnamed fifth member marked with a black heart. Agatha brings in her neighbor Sharon Davis, a keen gardener with no magic, who was \"Mrs. Hart\" under Wanda's spell."),
        ("セイラム・セブンの襲撃と扉",
         "地下室で、5人は「魔女の道のバラード」を唱えて入り口を呼び出そうとする。そこへセイラム・セブンが家を襲う。\n"
         "道は現れない。アガサは魔女たちをあおるが、リリアが仲間を止める。魔女たちがアガサを攻撃すれば、アガサに力を吸い取られてしまうからだ。\n"
         "そのとき、急に扉が現れる。少年も一緒に全員が扉に飛びこみ、セイラム・セブンから逃れる。",
         "The Salem Seven and the door",
         "In the basement, the five women chant the ballad to conjure the entrance to the Road, and the Salem Seven attack the house.\n"
         "The Road doesn't appear. Agatha taunts the witches, but Lilia stops them from striking back, which would only give Agatha power to absorb.\n"
         "Suddenly a door appears. The coven and the teen go through it and escape the Seven."),
        ("魔女の道",
         "たどり着いたのは魔女の道。一行は靴をぬぎ、まわりの景色を見わたしてから、歩き始める。",
         "The Witches' Road",
         "Now on the Witches' Road, the group take off their shoes, pause to take in their surroundings, and begin the journey."),
    ]),
    ("第3話 試練が待ち受ける長き旅路", "Episode 3: Through Many Miles / Of Tricks and Trials", [
        ("名前を隠す印",
         "道の上で、シャロンは無理やり連れてこられたと怒る。少年がみんなに名乗ろうとすると、魔女たちは、少年の正体を隠している魔法が「シジル（印）」だと見抜く。どの魔女にも少年の正体が分からないようになっている。\n"
         "アガサは、それぞれの得意な魔法が、1人ずつの試練で試されると説明する。シャロンは道から外れ、泥の沼に飲まれかけるが、みんなに助けられる。",
         "A hidden name",
         "On the Road, Sharon accuses the coven of kidnapping her. When the teen tries to introduce himself, the witches recognize the spell hiding his identity as a sigil, which keeps any witch from learning who he is.\n"
         "Agatha explains that each witch's specialty will be tested in its own trial. Sharon strays off the Road and nearly sinks into a mud pool before the coven pulls her out."),
        ("海辺の家とワイン",
         "最初の試練は、海辺のおしゃれな家。中に入ると、全員の服が家の雰囲気に合わせて変わる。\n"
         "なぞかけが出され、シャロンがワインのびんを見つけて解く。少年以外の全員がワインを飲むと、時間を数えるタイマーが動き出す。\n"
         "ジェンは少年に、アガサを信じるなと小声で忠告する。アガサは、ダークホールドと引きかえに自分の子どもを手放したといううわさがあるからだ。少年とアリスが身の上話をしている間に、アガサは自分のワインをこっそり捨てる。",
         "The beach house and the wine",
         "The first trial is a stylish coastal house. Inside, everyone's clothes change to match it.\n"
         "A riddle appears, and Sharon solves it by spotting a bottle of wine. Everyone but the teen drinks, and a countdown timer starts.\n"
         "Jen privately warns the teen not to trust Agatha, who is rumored to have given up her child for the Darkhold. While the teen and Alice swap stories, Agatha secretly pours her wine away."),
        ("毒入りのワイン",
         "しばらくすると、みんなの顔が一瞬はれ上がる。ジェンは、ワインに毒が入っていたと気づき、毒の種類を言い当てる。\n"
         "アガサのグラスは魔法でまた満たされる。少年に、飲まないなら自分が代わりに飲むと言われ、アガサも飲むしかなくなる。毒が回ったシャロンは、ワンダの魔法の中で味わった苦しみをまぼろしに見て、気を失う。",
         "Poisoned",
         "After a few minutes, everyone's faces briefly swell. Jen realizes the wine was poisoned and identifies the toxin.\n"
         "Agatha's glass magically refills, and when the teen threatens to drink it for her, she has no choice but to drink. Under the poison, Sharon hallucinates the trauma she lived through under Wanda's spell and faints."),
        ("それぞれのまぼろし",
         "ジェンの指示で、2人ずつ組になって家じゅうで解毒剤の材料を探す。そのうち魔女たちは、自分の過去のまぼろしを見る。\n"
         "ジェンは魔法を封じられた時のこと。リリアは若いころの自分と、昔の師匠のそばに立つ黒い影。アリスは、母ローナ・ウーが死を迎えようとする姿。\n"
         "材料はそろうが、家はいつの間にか水の中にあった。アガサが前に逃げようとして窓にひびを入れていて、そこから水がもれ始める。",
         "Visions of the past",
         "Following Jen's instructions, they split into pairs to search the house for antidote ingredients, and each witch is hit by vivid visions of her past.\n"
         "Jen relives having her magic bound. Lilia sees her younger self and a shadowy figure over her old maestra. Alice sees her mother, Lorna Wu, about to die.\n"
         "They gather the ingredients, but the house is now underwater, and water leaks through cracks Agatha made in a window when she tried to flee earlier."),
        ("ぎりぎりの解毒剤",
         "気を失ったシャロンを台所へ運び、ジェンの指示で解毒剤を作る。アガサは、ゆりかごの中にダークホールドがあるまぼろしを見る。\n"
         "アガサにはげまされ、ジェンは時間切れの直前に解毒剤を完成させる。全員が飲み、シャロンにも飲ませる。家が水であふれる中、一行は台所のオーブンの中に開いたトンネルから逃げ出す。",
         "The antidote, just in time",
         "They move the unconscious Sharon into the kitchen and brew the antidote under Jen's direction. Agatha hallucinates a crib holding the Darkhold.\n"
         "Spurred on by Agatha, Jen finishes the antidote just before time runs out. They all drink it and give a dose to Sharon. As the house floods, they escape through a tunnel inside the kitchen oven."),
        ("シャロンの死",
         "一行は道の上に戻る。言い合いをするアガサとジェンを、リリアが止める。そのとき、シャロンが死んでいることに気づく。",
         "Sharon is dead",
         "They're back on the Road. As Lilia tells Agatha and Jen to stop arguing, the group realize Sharon is dead."),
    ]),
    ("第4話 届けこの歌 遙かなるあなたに", "Episode 4: If I Can't Reach You / Let My Song Teach You", [
        ("シャロンの墓と新しい緑の魔女",
         "アリスと少年がシャロンを埋める。アガサは先を急がせるが、仲間たちは、試練に必要な緑の魔女がいないと先へ進めないと言う。\n"
         "呪文で代わりの魔女を呼び出すと、シャロンの墓の中から現れたのはリオ・ヴィダルだった。アガサはいやがるが、ほかの魔女たちは、アガサの嫌がる相手が来たことをむしろ歓迎する。",
         "Sharon's grave and a new green witch",
         "Alice and the teen bury Sharon. Agatha wants to hurry on, but the others refuse: they need a green witch for one of the trials.\n"
         "They cast a summoning spell for a replacement, and Rio Vidal rises out of Sharon's grave. Agatha is dismayed; the rest of the coven are glad to have someone who annoys her."),
        ("アリスの家",
         "道の先に家が見えるが、アリスは入ろうとしない。別の方向へ進んでも、家はまた一行の前に現れる。\n"
         "中に入ると、そこは1970年代風のレコーディングスタジオで、全員がロックバンドの衣装になっている。家は、アリスの亡き母ローナ・ウーにつながる場所だった。ローナは有名な魔女の歌手で、ウー家に代々かけられた呪いで命を落としていた。",
         "Alice's house",
         "A house appears, and Alice won't go in. When they change direction, it reappears in their path.\n"
         "Inside is a 1970s recording studio, and they're all dressed as a rock band. The house is tied to Alice's late mother, Lorna Wu, a famous witch musician killed by the Wu family's generational curse."),
        ("録音室の会話",
         "録音ブースの中で、リオとアガサは、仲間を裏切る話を、いちゃつくような調子でする。しかし、ブースのマイクが入っていて、会話はほかの仲間に聞かれてしまう。",
         "Overheard in the booth",
         "In a sound booth, Rio and Agatha flirtatiously talk about betraying the group, but the intercom is on and the others hear every word."),
        ("よみがえる呪い",
         "少年がレコードを逆回しでかけると、呪いが解き放たれる。リリアとジェンは呪いの火に焼かれそうになるが、アリスが魔法の円で2人を守る。\n"
         "一行は気づく。この呪いなら、アリスは何年も前に死んでいたはずだ。アリスを守ってきたのは、母ローナが歌った「魔女の道のバラード」だった。この歌は守りの呪文で、くり返し流されることで効き続けていたのだ。",
         "The curse returns",
         "The teen plays a record that spins backward and unleashes the curse. Lilia and Jen are scorched until Alice protects them with a magic circle.\n"
         "The coven realizes the curse should have killed Alice years ago. Lorna's famous cover of the ballad is a protection spell, kept working by being played over and over."),
        ("バンドで歌うバラード",
         "呪いを断つため、一行はローナの版のバラードを演奏する。リオはドラムをたたく。すると呪いが、つばさのある悪魔の姿になって現れ、家に火を放つ。\n"
         "アリスは仲間と一緒に最後まで歌いきり、呪いを永遠に打ち破る。",
         "The band plays the ballad",
         "To break the curse, they perform Lorna's version of the song, with Rio on drums. The curse takes the form of a winged demon and sets the house on fire.\n"
         "Alice finishes the song with the others and destroys the curse for good."),
        ("少年のけが",
         "家を出ると、少年がたおれる。試練の間に大けがをしていたのだ。道の上で、アガサにうながされたジェンが治療し、少年は助かる。\n"
         "回復した少年は、アガサと自分の印（シジル）について話す。アガサは、誰がかけたのか知らないし、かけた魔女本人も覚えていないはずだと言う。少年がアガサの息子のことをたずねるが、アガサは答えない。",
         "The teen is hurt",
         "Outside, the teen collapses from a wound he took during the trial. On the Road, at Agatha's urging, Jen heals him.\n"
         "Recovering, he talks with Agatha about his sigil. She claims not to know who cast it, adding that even the witch who did wouldn't remember. When he asks about her son, she doesn't answer."),
        ("傷あとの話とリオの言葉",
         "ほかの仲間たちは、それぞれの過去の傷について話し、打ちとける。アガサが加わると、リオは、昔アガサを傷つけてしまったことを口にし、2人が恋人だったことをほのめかす。アガサはその場を離れる。\n"
         "リオはアガサを追ってなぐさめる。アガサがキスしようとすると、リオはそれを止め、あの少年はあなたのものではないと告げる。",
         "Scars, and Rio's warning",
         "The rest of the coven bond over the scars of their pasts. When Agatha joins them, Rio hints at their old romance and at how she once hurt Agatha. Agatha walks away.\n"
         "Rio follows to comfort her. When Agatha tries to kiss her, Rio stops her and tells her the teen is not hers."),
    ]),
    ("第5話 大地の力 目覚めさせよ", "Episode 5: Darkest Hour / Wake Thy Power", [
        ("追ってくるセイラム・セブン",
         "道で休んでいると、リリアがセイラム・セブンが迫ってくるまぼろしを見て飛び起きる。\n"
         "セイラム・セブンは、アガサが昔殺した魔女仲間たちの子どもたちだった。アガサは親たちを殺したとき、子どもたちだけは生かしていた。7人は、リオを呼び出したときに開いた入り口から道に入りこんでいた。",
         "The Salem Seven close in",
         "Resting on the Road, Lilia wakes from a vision of the Salem Seven closing in.\n"
         "She explains that the Seven are the children of Agatha's original coven, spared when Agatha killed their parents, and that they entered the Road through the gateway opened when Rio was summoned."),
        ("ほうきで空へ",
         "一行は、間に合わせのほうきで空を飛んで逃げようとする。しかし、道に地面へ引きもどされてしまう。\n"
         "セブンからぎりぎりで逃れ、一行は1980年代風の森の山小屋に入る。リオは、これはアガサの試練だと言い当てる。",
         "Brooms in the sky",
         "The coven tries to flee on makeshift flying broomsticks, but the Road drags them back to the ground.\n"
         "Narrowly escaping the Seven, they enter a 1980s-style forest cabin. Rio identifies the trial as Agatha's."),
        ("ウィジャ盤",
         "少年がウィジャ盤（死者と話すための文字盤）を見つけ、遊び方を読み上げる。一行はこれを使って死者を呼ぶ。\n"
         "アガサは初め、シャロンにとりつかれたふりをして、みんなをだます。ところが、本当に何かの霊にとりつかれる。とりつかれたアガサは少年とジェンに襲いかかるが、リリアが明かりをつけると、霊はいったん出ていく。",
         "The Ouija board",
         "The teen finds a Ouija board and reads the rules aloud, and the coven uses it to contact the dead.\n"
         "Agatha first fools everyone by pretending to be possessed by Sharon, but then a spirit truly takes her over. Possessed, she attacks the teen and Jen until Lilia turns on the lights and the ghost is briefly driven out."),
        ("母エヴァノラの霊",
         "霊の正体は、アガサの母エヴァノラ・ハークネスだった。アガサが昔、ほかの魔女仲間と一緒に殺した母だ。\n"
         "エヴァノラは、試練を終えたければアガサを置いていけと言う。リオと少年は反対する。ジェンとリリアが出て行こうとしたとき、エヴァノラはまたアガサにとりつく。",
         "Evanora's ghost",
         "The spirit is Agatha's mother, Evanora Harkness, whom Agatha murdered along with her original coven.\n"
         "Evanora demands they abandon Agatha to finish the trial. Rio and the teen object. As Jen and Lilia get ready to leave, Evanora possesses Agatha again."),
        ("アリスの死",
         "アリスが魔法でアガサを撃ち、エヴァノラをアガサの体から追い出す。しかしアガサは、そのすきにアリスの力を吸い取ってしまう。アリスは死ぬ。\n"
         "少年はウィジャ盤で「ニコラス・スクラッチ」という名前をつづる。アガサの息子の名前だ。その声が響くと、アガサは我に返る。出口が現れる。",
         "Alice dies",
         "Alice strikes Agatha with her magic and drives Evanora out of her body. But Agatha seizes the moment and absorbs Alice's power, killing her.\n"
         "The teen uses the Ouija board to spell out \"Nicholas Scratch,\" the name of Agatha's son. A disembodied voice breaks Agatha's trance, and an exit appears."),
        ("少年の怒り",
         "道に戻ると、少年はアリスを殺したことでアガサを責める。アガサは、わざとではなかったと言い張る。\n"
         "少年は、力ばかり求める魔女たちを責める。アガサは楽しそうに少年をからかい、母親にそっくりだと言う。",
         "The teen's fury",
         "Back on the Road, the teen confronts Agatha over Alice's death, which she insists was an accident.\n"
         "When he condemns the witches for chasing power, Agatha gleefully mocks him and says he takes after his mother."),
        ("泥の沼と冠",
         "怒りがあふれた少年は、リリアとジェンの心をあやつり、2人にアガサを泥の沼へ投げこませる。さらに魔法で2人も沼へふき飛ばし、3人は沈んでいく。\n"
         "少年の頭には、スカーレット・ウィッチの冠に似たものが現れる。",
         "The mud and the crown",
         "In a surge of emotion, the teen seizes control of Lilia's and Jen's minds, makes them hurl Agatha into a mud pool, and then blasts them in too. The three begin to sink.\n"
         "A crown like the Scarlet Witch's headpiece forms on his head."),
    ]),
    ("第6話 使い魔たずさえ", "Episode 6: Familiar by Thy Side", [
        ("ウィリアムのバル・ミツバ",
         "時は戻って2023年。隣町イーストビューで、13歳のウィリアム・カプランが、ユダヤ教の成人式にあたるバル・ミツバのお祝いをしている。\n"
         "パーティーには占い師としてリリアが来ていた。リリアはウィリアムの手相を見て、生命線が2つに分かれていると言う。ほかにも何かが見えたが、それは口にしない。ウィリアムがテントを出るとき、リリアは身を守る印（シジル）をかけ、そのとたんに会ったこと自体を忘れる。",
         "William's bar mitzvah",
         "In 2023, 13-year-old William Kaplan celebrates his bar mitzvah in Eastview, New Jersey.\n"
         "Lilia is there as a fortune teller. Reading his palm, she sees his lifeline split in two, and sees something more that she keeps to herself. As he leaves her tent, she casts a protective sigil on him and instantly forgets meeting him."),
        ("事故とよみがえり",
         "となり町ウエストビューの異変（ワンダが作った町）がくずれ始め、パーティーは中断される。ウィリアムは両親と車で帰る途中、異変から流れてくるラジオの電波に気を取られ、車が事故を起こす。\n"
         "ウィリアムはけがで息を引き取る。そのとき、ワンダの息子ビリー・マキシモフの魂がウィリアムの体に入り、ウィリアムはよみがえる。\n"
         "ビリーには、どちらの人生の記憶もなかった。急に人の心が読めるようになり、混乱する。",
         "The crash and a new life",
         "The party breaks up as the Westview anomaly, Wanda's town, begins to collapse. Driving home with his parents, William is distracted by a radio signal from the anomaly, and the car crashes.\n"
         "William dies of his injuries, but as he passes, the soul of Billy Maximoff, Wanda's son, enters his body and he comes back to life.\n"
         "He has no memory of either life, and his sudden ability to read minds leaves him distraught."),
        ("エディとラルフ・ボーナー",
         "3年後。ビリーは恋人のエディに、今も昔の記憶が戻らないと打ち明ける。\n"
         "ウエストビューの異変を調べていた2人は、ウエストビューに住んでいたというネットの投稿者に会う。ラルフ・ボーナーだ。ラルフは、アガサに心をあやつられていたころのことを話す。ワンダとヴィジョンには双子の息子、ビリーとトミーがいたことも。\n"
         "話を聞くうちに、ビリーは自分の本当の正体に気づく。",
         "Eddie and Ralph Bohner",
         "Three years later, Billy confesses to his boyfriend Eddie that his memories have never come back.\n"
         "Looking into the Westview anomaly, they meet an online poster who claims to have lived there: Ralph Bohner. He describes being mind-controlled by Agatha, and tells them about Wanda and Vision's twins, Billy and Tommy.\n"
         "As he listens, Billy begins to realize who he really is."),
        ("アガサのもとへ",
         "ビリーはアガサと魔女の道について調べ、ウエストビューに向かう。アガサをワンダの魔法から解き放ち、双子の弟トミーを見つけるためだ。\n"
         "まだ魔法にかかっていた刑事アグネスは、ビリーを捕まえて取り調べる（第1話の場面を、ビリーの側から見せる）。ビリーは魔法を解き、自分はウィリアム・カプランであり、ビリー・マキシモフでもあると名乗る。",
         "Going to Agatha",
         "Billy researches Agatha and the Witches' Road and goes to Westview, hoping to free her from the Scarlet Witch's spell and find his twin brother, Tommy.\n"
         "Still under the spell, \"Agnes\" captures and interrogates him (Episode 1's scenes, seen from Billy's side). Billy breaks the enchantment and introduces himself as both William Kaplan and Billy Maximoff."),
        ("泥の中から",
         "現在の道の上。アガサは泥の沼からはい上がる。印（シジル）がこわれたと気づいたアガサは、少年の正体には前から気づいていたと言う。\n"
         "アガサは、力をうまく使いこなせないビリーをからかい、ビリーの目的も言い当てる。そして、次の試練に一緒に進もうとビリーを説き伏せる。",
         "Out of the mud",
         "Back in the present on the Road, Agatha drags herself out of the mud. Realizing the sigil is broken, she claims she had an inkling of his identity all along.\n"
         "Teasing Billy for his poor control of his powers and guessing his goal, she persuades him to go on to the next trial with her."),
    ]),
    ("第7話 死と手をつなぎ", "Episode 7: Death's Hand in Mine", [
        ("暗やみに落ちるリリア",
         "この話は、リリアが体験する順番どおり、時間がばらばらに描かれる。\n"
         "最初の場面では、取り乱したリリアが、真っ暗な空間を落ちていく。",
         "Lilia falls",
         "This episode is told out of order, the way Lilia experiences it.\n"
         "It opens with a distraught Lilia falling through a black void."),
        ("城とタロットの試練",
         "道の上で、ビリーはワンダの死についてアガサに問いただす。アガサが本当に前にこの道を歩いたことがあるのか、疑い始める。\n"
         "2人は城を見つけて中に入る。昔のおとぎ話の魔女の衣装を着せられ、タロット占いの台が現れる。次の試練だ。2人はおたがいを占おうとするが、まちがったカードを引くたびに、天井から剣が1本落ちてくる。",
         "The castle and the tarot",
         "On the Road, Billy questions Agatha about Wanda's death and starts to doubt she has ever walked the Road before, as she claims.\n"
         "They find a castle and go inside. Dressed as witches from classic fairy tales, they're presented with the next trial: a tarot reading table. They try reading for each other, and every wrong card brings a sword down from the ceiling."),
        ("地下のトンネル",
         "道の下のトンネル。リリアとジェンは、リリアが教えたという道を進んでいる。リリアにはその覚えがないが、ジェンは、ついさっきリリアから聞いたことを次々に話す。\n"
         "リリアは自分の秘密を打ち明ける。子どものころから、自分の人生のいろいろな時を行き来していて、出来事を順番どおりに体験できないのだ。これまでのとんちんかんな言葉や物忘れは、そのためだった。",
         "In the tunnels",
         "In the tunnels under the Road, Lilia and Jen follow a path Jen says Lilia suggested. Lilia doesn't remember, but Jen recounts everything she says Lilia told her minutes ago.\n"
         "Lilia explains her secret: since childhood she has lived her life out of order, her mind shifting between points in her own timeline. That is why she says strange things and forgets things."),
        ("初めての占いのけいこ",
         "リリアの意識は、若いころの初めての占いのけいこの日へ飛ぶ。師匠は、リリアが自分の力に自信を持てないことをなげく。リリアは昔、最初の魔女仲間が全滅することを予知しながら、防げなかったのだ。",
         "The first lesson",
         "One shift takes Lilia to her first lesson in divination. Her maestra laments that Lilia has no faith in her own power, ever since she foresaw the end of her first coven and couldn't stop it."),
        ("落ち続ける剣",
         "時間が先へ飛ぶ。リリアとジェンは城でビリーとアガサと一緒にいる。リリアがビリーを占うが、剣は落ち続ける。\n"
         "けいこの日に戻ると、師匠は、自分の力には意味があると信じるようリリアをはげます。リリアは、暗やみを落ちていたことの意味に気づく。",
         "Swords keep falling",
         "Flash forward: Lilia and Jen are in the castle with Billy and Agatha. Lilia reads for Billy, but the swords keep falling.\n"
         "Back at the lesson, her maestra urges her to believe her gift has a purpose, and Lilia understands what falling through the void meant."),
        ("トンネルの始まりへ",
         "リリアはトンネルの旅の始まりに戻る。そして、のちにジェンが「リリアから聞いた」と言うことになる話を、すべてジェンに伝える。\n"
         "2人はセイラム・セブンをかわしながら、城のアガサとビリーのもとへ向かう。",
         "Back to the beginning",
         "Lilia finds herself at the start of the tunnels and tells Jen everything Jen will later say she learned from her.\n"
         "Evading the Salem Seven, they set off to join Agatha and Billy at the trial."),
        ("リリアの占いとリオの正体",
         "城で、リリアは、占うべき相手は自分自身だと気づく。正しい順にカードを置いて占いを終え、試練を突破する。\n"
         "リリアは、リオの正体は「死」そのものだと明かす。アガサもそれを知っていた。",
         "Lilia's reading, and Rio's secret",
         "In the castle, Lilia realizes she must do the reading for herself. She lays the cards in the right order and passes the trial.\n"
         "She reveals that Rio is Death itself, and that Agatha knew."),
        ("リリアの最期",
         "リリアはみんなに逃げるよう言い、ジェンが止めるのも聞かず、ひとりで残る。そこへセイラム・セブンが襲いかかる。\n"
         "リリアは、自分の占いの「塔」のカードを正しい向きにひっくり返す。城の上下が逆さまになり、セブンは天井の剣に突き刺される。リリアは手を離し、落ちていく。\n"
         "最後の場面では、若いリリアがうれしそうに、初めての占いのけいこに向かう。",
         "Lilia's end",
         "Lilia tells everyone to run and stays behind despite Jen's pleas. The Salem Seven ambush her.\n"
         "She turns the Tower card from her reading upright. Gravity in the castle flips, and the Seven are impaled on the swords. Lilia lets go and falls.\n"
         "In the final scene, young Lilia happily heads to her first divination lesson."),
    ]),
    ("第8話 続け友よ 栄光の地へと", "Episode 8: Follow Me My Friend / To Glory at the End", [
        ("アリスの魂",
         "アリスは、自分が死んだ山小屋で、魂として目を覚ます。リオの姿をした「死」が迎えに来て、アリスはアガサを救おうとして死んだのだと伝える。\n"
         "取り乱しながらも、アリスは運命を受け入れ、あの世へ旅立つ。",
         "Alice's spirit",
         "Alice wakes as a spirit in the cabin where she died. Death, as Rio, comes to claim her and tells her she died trying to save Agatha.\n"
         "Distraught, Alice accepts her fate and passes on."),
        ("死との取り引き",
         "道の上で、リオがアガサの前に現れる。リオはビリーの正体を知り、死んだ者がよみがえったことを許せずにいた。\n"
         "アガサは、ビリーを必ず引き渡すと約束する。その代わり、死んだ後も二度とリオに会わないという条件をつける。リオは受け入れ、道の空間を切りさいて出ていく。",
         "A deal with Death",
         "On the Road, Rio confronts Agatha. She has learned who Billy is and opposes his return from the dead.\n"
         "Agatha promises to hand Billy over, in exchange for never seeing Rio again, even in death. Rio agrees and cuts her way out of the Road."),
        ("道は輪になっていた",
         "ジェンとビリーはリリアの死を悲しみ、リオの正体について話してから、アガサと合流する。\n"
         "3人が着いたのは、最初に靴をぬいだ場所だった。道は輪になっていたのだ。アガサはもう一度歩くしかないと怒るが、ビリーは逆らうように靴をはく。",
         "The Road is a circle",
         "Jen and Billy mourn Lilia and talk about who Rio really is before rejoining Agatha.\n"
         "They reach the spot where they first took off their shoes: the Road is a circle. Agatha furiously insists they walk it again, but Billy defiantly puts his shoes back on."),
        ("最後の試練とジェンの力",
         "3人は、遺体安置所のようになったアガサの家の地下室へ移される。最後の試練は、頭上の植物用のライトが消える前に、植物を育てることだった。\n"
         "ジェンは、自分の魔法を封じたのがアガサだったと知る。アガサが依頼を受け、お金のためにかけた呪文だった。ジェンは封印を解く儀式を行い、力を取り戻す。望みをかなえたジェンは、道から消える。",
         "The last trial and Jen's power",
         "The three are taken to a morgue-like version of Agatha's basement. To pass, they must grow a plant before the grow lights overhead go out.\n"
         "Jen learns Agatha was the one who bound her magic, a spell Agatha had cast for money. Jen performs an unbinding ritual and gets her power back. Having what she came for, she vanishes from the Road."),
        ("トミーの魂",
         "アガサは、ビリーが双子の弟トミーの魂を探すのを手伝う。ビリーは見つけたトミーの魂を、おぼれかけていた少年の体に移す。そしてビリーも消える。\n"
         "時間がない中、アガサは、ロケットに入れていた種と自分の涙を使い、床のひび割れに花を咲かせる。試練を突破し、道から抜け出す。",
         "Tommy's soul",
         "Agatha helps Billy find Tommy's soul, and he moves it into the body of a drowning boy. Then Billy vanishes too.\n"
         "Out of time, Agatha uses a seed from her locket and her own tears to grow a flower in a crack in the floor, passes the trial, and escapes the Road."),
        ("死との戦い",
         "アガサが出たのは、ウエストビューの自分の家の裏庭だった。リオが現れ、ビリーを引き渡さなかったこと、自分の気持ちをはねつけたことを責める。\n"
         "ビリーが助けに来て、自分の魔法の一部をアガサに分け与える。力を取り戻したアガサはリオと戦うが、やがて「死」と戦ってもむだだと認める。リオは、アガサかビリーのどちらかが一緒に来るよう求める。",
         "Fighting Death",
         "Agatha emerges in her backyard in Westview. Rio confronts her for failing to deliver Billy and for rejecting her.\n"
         "Billy comes to the rescue and lets Agatha draw some of his magic to restore hers. She fights Rio but soon admits it is futile to fight Death. Rio demands that either Agatha or Billy go with her."),
        ("アガサの最期",
         "ビリーは自分が行くと言い、アガサはそれを受け入れる。ビリーは心の中でアガサに語りかけ、あなたの息子ニコラスもこうして死んだのかとたずねる。\n"
         "その言葉で、アガサの気持ちが変わる。アガサはリオにキスをして、死ぬ。アガサの体がたおれた所には、花が咲く。「死」は本当の姿をビリーに見せ、行けと告げる。",
         "Agatha's end",
         "Billy volunteers, and Agatha surprises him by agreeing. Speaking into her mind, Billy asks if this is how her son, Nicholas, died.\n"
         "That changes her heart. Agatha kisses Rio and dies, and flowers grow where her body falls. Death shows Billy her true form and tells him to go."),
        ("ビリーの部屋",
         "家に帰ったビリーは、自分の部屋にある物の多くが、魔女の道で見たものと同じだと気づいてがく然とする。道は、知らないうちにビリーが魔法で作り出していたのだ。\n"
         "そのとき、背後からアガサの笑い声が聞こえる。",
         "Billy's room",
         "Back home, Billy is shocked to see that many objects in his bedroom match parts of the Witches' Road. He realizes he created it with his magic without knowing.\n"
         "Then he hears Agatha laughing behind him."),
    ]),
    ("第9話 乙女 母 老婆", "Episode 9: Maiden Mother Crone", [
        ("1750年、森での出産",
         "1750年。アガサは森の中で子どもを産もうとしていた。そこへ「死」が現れ、生まれてくる子どもを連れて行こうとする。\n"
         "アガサが必死に頼むと、「死」は引き下がる。しかし、いずれその子を迎えに来ると告げる。",
         "1750: a birth in the woods",
         "In 1750, Agatha goes into labor in the wilderness, and Death appears to claim the child.\n"
         "Agatha pleads, and Death relents, but warns that she will come back for him."),
        ("ニコラスとの旅",
         "6年後。アガサは息子ニコラス・スクラッチを連れて旅をし、だまされやすい魔女たちをわなにかけて力を吸い取っていた。ニコラスもそれを手伝わされる。\n"
         "旅の中で、2人は「魔女の道のバラード」の最初の形を作る。歌はやがて民謡として広まり、アガサは人殺しのたくらみにこの歌を使う。ニコラスは、だんだんそれをいやがるようになる。",
         "Traveling with Nicholas",
         "Six years later, Agatha travels with her son, Nicholas Scratch, who helps her lure gullible witches so she can feed on their magic.\n"
         "On the road, the two come up with the first version of \"The Ballad of the Witches' Road.\" It spreads as a folk song, and Agatha uses it in her killing schemes, which Nicholas grows to oppose."),
        ("ニコラスの死",
         "ある夜、ニコラスは「死」に起こされる。眠っているアガサにお別れのキスをして、ニコラスはあの世へ旅立つ。\n"
         "翌朝、アガサはニコラスの亡きがらを見つけ、深く悲しむ。",
         "Nicholas dies",
         "One night, Death wakes Nicholas. He kisses his sleeping mother goodbye and goes with her to the afterlife.\n"
         "The next morning, Agatha finds his body and is devastated."),
        ("作り話の道",
         "ニコラスを埋めた後、1人の魔女がアガサに、魔女の道への行き方を教えてほしいと頼みに来る。\n"
         "それからの何百年、アガサは魔女の道の話で魔女たちをだまし、力を増していった。最近ねらったのが、ジェン、アリス、リリア、シャロンだった。ところが、作り話のはずの道が本当に現れ、アガサはおどろく。アガサは、道を作ったのはビリーだと見抜いていた。",
         "A made-up road",
         "After the burial, a curious witch asks Agatha how to find the Witches' Road.\n"
         "For centuries afterward, Agatha uses the Road to con witches and grow her power. Her latest marks were Jen, Alice, Lilia, and Sharon, but she was blindsided when the Road actually appeared, and she worked out that Billy had made it."),
        ("幽霊のアガサ",
         "現在。幽霊になったアガサがビリーの前に現れる。道を作ったのはビリーの魔法で、それでワンダの息子だと見当がついたのだと話す。\n"
         "ビリーは、シャロン、アリス、リリアが死んだのは自分のせいだと苦しむ。アガサは、自分は初めから3人を殺すつもりだったと言い、ジェンが生き残ったのはビリーのおかげだと言う。そのころジェンは、ウエストビューの近くで地面からはい出し、空を飛んで去っていく。",
         "Agatha's ghost",
         "In the present, Agatha's ghost confronts Billy. She explains that his magic created the Road, which tipped her off that he was Wanda's son.\n"
         "Billy is horrified to have caused the deaths of Sharon, Alice, and Lilia. Agatha points out she meant to kill them from the start, and credits him with Jen's survival. Meanwhile Jen climbs out of the ground near Westview and flies away."),
        ("追いはらう呪文",
         "ビリーはウエストビューのアガサの家に行き、地下室で呪文の本を探す。アガサをあの世へ送る呪文を唱え始めるが、アガサが止める。息子に会う覚悟がまだできていないと打ち明けるのだ。ビリーは呪文をやめる。\n"
         "幽霊のアガサは初め物にさわれないが、やがて自分のロケットを拾い上げることができる。",
         "The banishing spell",
         "Billy goes to Westview and searches Agatha's basement for his spell book. He begins a spell to send her to the afterlife, but she stops him, admitting she isn't ready to face her son. Billy relents.\n"
         "At first the ghost can't touch anything, but soon she manages to pick up her locket."),
        ("道を閉じて、トミーを探しに",
         "ビリーは魔女の道の入り口をふさぎ、死んでいった仲間たちをしのぶ言葉を刻む。\n"
         "そしてビリーとアガサは、弟トミーを探す旅に出る。",
         "Sealing the Road, and looking for Tommy",
         "Billy seals the entrance to the Witches' Road with an epitaph honoring their fallen coven.\n"
         "Then Billy and Agatha set out to find his brother, Tommy."),
    ]),
    ("まとめ（最終話までのネタバレ）", "Summary (spoilers through the finale)", [
        ("魔女の道とは何だったのか",
         "・始まり（第9話）：「魔女の道のバラード」は、1750年代にアガサと息子ニコラスが旅の中で作った歌だった。ニコラスの死後、アガサはこの歌をもとに魔女の道の話を広め、道を探す魔女たちをだまして力を吸い取ってきた。\n"
         "・本当に現れた道（第2話・第8話・第9話）：作り話だった道を、ビリーが知らないうちに魔法で作り出していた。ビリーの部屋の物が道の中に出てきたのはそのため。\n"
         "・少年の正体（第5話・第6話）：ワンダの息子ビリー・マキシモフ。ウエストビューが消えた日、事故で死にかけたウィリアム・カプランの体に魂が入った。正体を隠す印（シジル）をかけたのはリリア。\n"
         "・リオ・ヴィダル（第1話・第7話・第9話）：アガサの昔の恋人で、正体は「死」。1750年にニコラスの命をいったん見のがし、6年後に連れて行った。\n"
         "・それぞれの試練：第3話は毒入りワインの家（ジェンの解毒剤で突破）、第4話はアリス（守り）、第5話はアガサ、第7話はリリア（占い）、第8話の最後の試練はアガサが花を咲かせて突破した。\n"
         "・最後に生き残ったのは、ビリーとジェン。アガサは幽霊として、ビリーと一緒にトミーを探しに出る。",
         "What the Witches' Road really was",
         "- Origins (Ep. 9): Agatha and her son Nicholas made up the ballad on the road in the 1750s. After his death, Agatha used it to spread the legend of the Road and con witches out of their power.\n"
         "- A real Road (Eps. 2, 8, 9): Billy unknowingly brought the made-up Road into being with his magic, which is why objects from his bedroom turned up on it.\n"
         "- The teen (Eps. 5, 6): Billy Maximoff, Wanda's son, whose soul entered the dying William Kaplan the day Westview vanished. Lilia cast the sigil hiding him.\n"
         "- Rio Vidal (Eps. 1, 7, 9): Agatha's former lover, and Death. She spared Nicholas at birth in 1750 and took him six years later.\n"
         "- The trials: the poisoned-wine house in Ep. 3 (passed with Jen's antidote), Alice's protection in Ep. 4, Agatha's in Ep. 5, Lilia's divination in Ep. 7; Agatha passes the last trial in Ep. 8 by growing a flower.\n"
         "- Survivors: Billy and Jen. Agatha, now a ghost, sets out with Billy to find Tommy."),
        ("死んだ人（話の順に）",
         "・シャロン・デイヴィス（第3話）：最初の試練で毒入りのワインを飲んで気を失い、解毒剤を飲ませたが、道に戻ったときには亡くなっていた。\n"
         "・アリス・ウー＝ガリヴァー（第5話）：とりつかれたアガサを救おうと魔法で撃ち、エヴァノラの霊を追い出したが、そのすきにアガサに力を吸い取られて死んだ。第8話で「死」に連れられてあの世へ行く。\n"
         "・セイラム・セブン（第7話）：リリアを襲ったとき、リリアが城の上下を逆さにしたため、天井の剣に突き刺されて死んだ。\n"
         "・リリア・カルデル（第7話）：仲間を逃がすため城に残り、セブンを道連れにして落ちていった。\n"
         "・アガサ・ハークネス（第8話）：「死」にアガサかビリーのどちらかを求められ、ビリーを生かすため、リオにキスをして死んだ。第8話の最後から幽霊になる。\n"
         "・昔の死（第5話・第9話）：アガサの母エヴァノラは1693年にアガサに殺された。息子ニコラスは1750年代に病気で弱り、6歳のころ「死」に連れられて亡くなった。",
         "Who died (in order)",
         "- Sharon Davis (Ep. 3): drank the poisoned wine in the first trial and fainted; though given the antidote, she was found dead back on the Road.\n"
         "- Alice Wu-Gulliver (Ep. 5): struck the possessed Agatha to drive out Evanora's ghost, and Agatha absorbed her power, killing her. Death guides her spirit on in Ep. 8.\n"
         "- The Salem Seven (Ep. 7): impaled on the castle's swords when Lilia flipped the room upside down.\n"
         "- Lilia Calderu (Ep. 7): stayed behind so the others could escape, taking the Seven with her as she fell.\n"
         "- Agatha Harkness (Ep. 8): when Death demanded her or Billy, she kissed Rio and died so Billy could live. She returns as a ghost at the end of Ep. 8.\n"
         "- Earlier deaths (Eps. 5, 9): Agatha killed her mother Evanora in 1693. Her son Nicholas, sickly from birth, was taken by Death at about six."),
    ]),
]
