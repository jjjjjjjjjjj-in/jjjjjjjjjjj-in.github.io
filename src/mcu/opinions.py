"""運営者のひとこと（感想・見解）。作品ガイドと、くわしいあらすじのページに出す。

- 2026-11-11 に追加。あらすじ（事実）だけでなく、運営者の感想・見解をのせるため
- 形: slug -> (日本語, 英語)。2〜3文。事実の説明ではなく「どう思うか」を書く
- 運営者が自分で話した感想（アイアンマン3作、ファルコン＆ウィンター・ソルジャー）は、その内容をもとにしている
- 「劇場で観た」などの体験は、運営者から聞いたものだけ書く。聞いていない体験は作らない
"""

OPINIONS = {
    "iron-man": (
        "最初の1本にして、今観てもとにかく面白い。ラストの「私がアイアンマンだ」は、ロバート・ダウニー・Jr. のアドリブだったと言われています。あの一言で、正体を隠すのが当たり前だったヒーロー映画の空気が変わったと思います。",
        "The first one, and still simply a great watch. The closing line, \"I am Iron Man,\" is said to have been improvised by Robert Downey Jr. I think that one line changed the mood of superhero films, where hiding your identity used to be the rule.",
    ),
    "iron-man-2": (
        "父親どうしの因縁が、そのまま息子どうしの対決になるのが面白いところ。トニーもヴァンコも同じアーク・リアクターを作れる天才で、違ったのは育った場所だけ、という見方をすると印象が変わります。",
        "What I like is that a grudge between two fathers becomes a fight between their sons. Tony and Vanko are both geniuses who can build an arc reactor; seen that way, the only difference between them is where they grew up.",
    ),
    "iron-man-3": (
        "正直、ペッパーは治さなくてよかったのでは、と思ってしまいます。エクストリミスに体がなじんで、ラスボスを倒せるほど強くなったのだから、そのままならヒーローになれたはず。それでも「元に戻す」を選ぶのが、トニーらしいところでもあります。",
        "Honestly, I can't help thinking Pepper didn't need to be cured. Her body adapted to Extremis and she became strong enough to finish off the final villain, so she could have been a hero as she was. Then again, choosing to \"put things back\" is very Tony.",
    ),
    "falcon-and-winter-soldier": (
        "サムとバッキーが、口げんかしながらだんだん相棒になっていくのがかわいい作品。盾を受け取るまでにサムがあれだけ悩むからこそ、最後の姿に納得できます。",
        "Sam and Bucky bickering their way into being partners is the charm of this one. Because Sam struggles so long before taking up the shield, his final look feels earned.",
    ),
    "captain-america-first-avenger": (
        "血清を打つ前から、スティーブはもうヒーローだった、というのがこの映画のいちばん好きなところ。手りゅう弾に飛びつく場面だけで、彼が選ばれた理由が分かります。",
        "My favourite thing here is that Steve is already a hero before the serum. The grenade scene alone tells you why he was chosen.",
    ),
    "captain-marvel": (
        "「力を証明しなくていい」と気づく終盤が気持ちいい。90年代の空気と、若いフューリーとの掛け合いも見どころで、猫のグースがいちばん得をしている映画だと思います。",
        "The late moment where she realises she has nothing to prove is satisfying. The 90s mood and her back-and-forth with a young Fury are highlights, and I think Goose the cat comes out of it best of all.",
    ),
    "incredible-hulk": (
        "MCU の中では影が薄いけれど、逃げ続けるブルースの孤独がいちばん伝わる1本。あとの作品でロス将軍が出てくるたびに、ここを観ておいてよかったと思えます。",
        "It gets overlooked in the MCU, but no other film shows Bruce's loneliness on the run this well. Every time General Ross turns up later, I'm glad I watched it.",
    ),
    "thor": (
        "えらそうな王子が、力を失って初めて人にやさしくなる話。ロキを「ただの悪役」ではなく、認められたかった弟として描いたのが、あとの人気につながったと思います。",
        "An arrogant prince learns kindness only after losing his power. I think showing Loki as a brother who wanted to be acknowledged, not just a villain, is what made him so loved later.",
    ),
    "avengers": (
        "ばらばらの6人が、円になって並ぶあの場面のためにある映画。今観ると規模は小さく感じても、「全員そろった」うれしさはこの作品がいちばんだと思います。",
        "The whole film exists for that shot of six mismatched people standing in a circle. It may look small in scale today, but I think nothing beats it for the joy of seeing everyone together.",
    ),
    "thor-dark-world": (
        "評価は高くない作品ですが、ソーとロキが手を組む中盤は別格。母フリッガを失った2人の反応の違いに、兄弟の性格がよく出ています。",
        "It isn't highly rated, but the middle stretch where Thor and Loki team up is in a different class. How each reacts to losing their mother Frigga shows the brothers' characters clearly.",
    ),
    "winter-soldier": (
        "ヒーロー映画というより、だれも信じられないスパイ映画として面白い。「最後までとことん付き合う」の一言が、あとのシビル・ウォーまでずっと効いてきます。",
        "It works less as a superhero film than as a spy thriller where no one can be trusted. \"I'm with you till the end of the line\" keeps echoing all the way to Civil War.",
    ),
    "guardians-of-the-galaxy": (
        "知らないキャラクターばかりなのに、音楽が鳴った瞬間に好きになれる。はみ出し者が家族になっていく流れは、MCU の中でもいちばん素直に泣ける部類だと思います。",
        "You don't know any of these characters, yet you like them the moment the music starts. Misfits becoming a family is, I think, among the most honest tear-jerkers in the MCU.",
    ),
    "guardians-vol2": (
        "テーマは「父親」。派手なエゴより、口の悪いヨンドゥのほうが本当の父親だったと分かる終盤は、何度観てもこたえます。",
        "The theme is fathers. The ending, where foul-mouthed Yondu turns out to be the real father rather than the dazzling Ego, gets me every time.",
    ),
    "i-am-groot-1": (
        "話のつながりを気にせず、小さなグルートのいたずらをながめるための短編集。数分で観られるので、長い作品の合間の息抜きにちょうどいいです。",
        "A set of shorts for simply watching little Groot make mischief, with no continuity to worry about. Each takes a few minutes, so it's a nice breather between longer titles.",
    ),
    "age-of-ultron": (
        "公開当時より、今のほうが面白く観られる作品だと思います。ワンダ、ヴィジョン、ワカンダ、仲間割れの種と、あとの物語の出発点がほとんどここに入っています。",
        "I think this one plays better now than it did on release. Wanda, Vision, Wakanda, the seeds of the team's split: nearly every later story starts here.",
    ),
    "ant-man": (
        "世界の危機ではなく、娘に会いたい父親の話なのがいい。おもちゃの機関車の上で戦うような「小ささ」を笑いに変えるセンスは、この作品ならではです。",
        "I like that it's about a father who wants to see his daughter, not about saving the world. Turning smallness into comedy, like a fight on a toy train, is something only this film does.",
    ),
    "civil-war": (
        "どちらの言い分も分かるから、観ていてつらい。個人的には、最後の3人の戦いは「正しさ」ではなく「友だちを守りたい」と「親を奪われた」のぶつかり合いで、だれも悪くないのがいちばん苦しいところだと思います。",
        "It hurts to watch because both sides make sense. For me, the final three-way fight isn't about who is right; it's \"I want to protect my friend\" against \"you took my parents,\" and the worst part is that no one is the bad guy.",
    ),
    "black-panther": (
        "悪役キルモンガーの言い分に、うなずいてしまうのがこの映画の強さ。ティ・チャラが相手を倒したあとで、自分の国のやり方を変えるという結末が好きです。",
        "The film's strength is that you find yourself agreeing with the villain, Killmonger. I love that T'Challa, after winning, goes on to change how his own country does things.",
    ),
    "spider-man-homecoming": (
        "世界を救うより、高校生活と両立できるかで悩むのがピーターらしい。車の中でヴァルチャーに正体を見抜かれる場面は、派手な戦いよりずっとこわいです。",
        "It's very Peter to worry less about saving the world than about fitting it around high school. The car scene where Vulture works out who he is frightens me more than any big fight.",
    ),
    "wakanda-forever": (
        "主役を失った悲しみを、ごまかさずにそのまま映画にした作品。シュリが怒りを手放すまでの時間の長さに、作り手の気持ちが出ていると思います。",
        "A film that puts the grief of losing its lead on screen without dodging it. I think how long it takes Shuri to let go of her anger shows how the makers felt.",
    ),
    "doctor-strange": (
        "なんでも自分でできると思っていた医者が、「負け続ける」ことで勝つ終盤がうまい。街が折りたたまれる映像は、今観ても新鮮です。",
        "A doctor who thought he could do anything wins by losing over and over; that ending is clever. The folding-city visuals still look fresh.",
    ),
    "thor-ragnarok": (
        "それまでのソーとは別物の、明るく笑える1本。ふざけているようで、故郷を失うという重い結末をきちんと描いているところが好きです。",
        "A bright, funny film quite unlike the earlier Thor entries. It seems to be fooling around, yet it properly delivers a heavy ending, the loss of a homeland, and I like that.",
    ),
    "ant-man-and-the-wasp": (
        "インフィニティ・ウォーの重さのあとに、ほっとできる軽さ。だからこそ、おまけ映像で急に現実に引き戻される落差が効いています。",
        "A welcome lightness after the weight of Infinity War. That's exactly why the post-credits scene, which yanks you back to reality, lands so hard.",
    ),
    "infinity-war": (
        "悪役サノスが主人公と言っていい作品。ヒーローが負けて終わるという結末は、続きがあると分かっていても言葉が出ません。",
        "You could call the villain, Thanos, the main character. Even knowing there's more to come, an ending where the heroes lose leaves me speechless.",
    ),
    "endgame": (
        "10年分の作品を観てきた人への、ごほうびのような映画。「アベンジャーズ、アッセンブル」と、トニーの最後の一言は、1作目から追ってきたからこそ重く感じます。",
        "A reward for anyone who followed ten years of films. \"Avengers, assemble\" and Tony's final line carry their weight because you've been there since the first film.",
    ),
    "loki-s1": (
        "悪役だったロキが、自分の人生を外からながめて変わっていくのが見どころ。時間や分岐の話はむずかしく見えますが、中身は「自分は何者か」という素直な話だと思います。",
        "The draw is watching Loki, once a villain, change as he sees his own life from outside. The time-and-branches talk looks hard, but at heart I think it's a simple story about who you are.",
    ),
    "loki-s2": (
        "王座がほしかったロキが、最後にひとりで全員を支える役を選ぶ結末がみごと。1作目『マイティ・ソー』から観てきた人ほど、こたえる終わり方です。",
        "Loki, who once wanted a throne, ends by choosing to hold everyone up alone, and it's beautifully done. The longer you've watched since the first Thor, the harder it hits.",
    ),
    "wandavision": (
        "昔のホームドラマのまねから始まって、だんだん「悲しみ」の話だと分かっていく作りがうまい。ワンダのしたことは許されないのに、気持ちは分かってしまうのがつらいところです。",
        "It starts as a pastiche of old sitcoms and slowly reveals itself as a story about grief; that structure is clever. What Wanda does can't be excused, and yet you understand her, which is the painful part.",
    ),
    "shang-chi": (
        "バスの中の戦いだけで、観る価値があります。『アイアンマン』から名前だけ出ていたテン・リングスの正体が、ここでやっと分かるのもうれしいところです。",
        "The bus fight alone makes it worth watching. It's also satisfying to finally learn what the Ten Rings, named since the first Iron Man, really are.",
    ),
    "spider-man-far-from-home": (
        "トニーの代わりを求められて苦しむピーターの話。うそを見せる敵という設定が、最後のおまけ映像までずっと効いているのがうまいと思います。",
        "A story about Peter struggling with being asked to replace Tony. I think it's clever how a villain who deals in lies keeps paying off right up to the post-credits scene.",
    ),
    "spider-man-no-way-home": (
        "過去のシリーズを観てきた人ほど、うれしい驚きが多い作品。その一方で、ピーターがすべてを失って終わる結末は、シリーズでいちばん大人びていると思います。",
        "The more of the earlier series you've seen, the more happy surprises there are. And yet the ending, where Peter loses everything, is I think the most grown-up in the series.",
    ),
    "multiverse-of-madness": (
        "MCU の中ではめずらしく、ホラーの味が強い1本。ワンダヴィジョンを観ているかどうかで、ワンダへの見方が大きく変わります。",
        "Unusually for the MCU, this one leans hard into horror. Whether you've seen WandaVision changes how you see Wanda a great deal.",
    ),
    "love-and-thunder": (
        "ふざけた場面が多くて好みは分かれますが、悪役ゴアの悲しみは本物。ジェーンの決断と、最後に残る「愛」の意味は素直にいい話だと思います。",
        "The constant jokes split opinion, but the villain Gorr's sorrow is real. Jane's choice, and what \"love\" turns out to mean at the end, make for an honestly good story, I think.",
    ),
    "quantumania": (
        "評判は厳しめですが、征服者カーンの落ち着いたこわさは印象に残ります。量子世界の見た目の変さを楽しむつもりで観ると、ちょうどいいです。",
        "Reviews were harsh, but Kang the Conqueror's calm menace sticks with me. It works best if you go in to enjoy how strange the Quantum Realm looks.",
    ),
    "guardians-vol3": (
        "ロケットの過去はつらくて観ていられないほどですが、だからこそ最後の全員の旅立ちが温かい。3部作のしめくくりとして、文句のない出来だと思います。",
        "Rocket's past is almost too painful to watch, which is why everyone's departure at the end feels so warm. As the close of a trilogy, I think it's hard to fault.",
    ),
    "x-men": (
        "今のヒーロー映画の流れを作った1本。プロフェッサーXとマグニートーが、敵なのに友だちでもあるという関係は、ここから最後まで変わらない魅力です。",
        "One of the films that started the modern superhero wave. Professor X and Magneto being enemies and friends at once is a charm that never changes from here on.",
    ),
    "x2": (
        "前作よりずっと出来がよく、シリーズの中でも上位だと思います。冒頭のナイトクローラーの場面と、敵どうしが手を組む流れは今観ても見ごたえがあります。",
        "Much better than the first, and near the top of the series, I think. The opening Nightcrawler scene and the enemies joining forces still hold up.",
    ),
    "x-men-last-stand": (
        "詰めこみすぎという声は分かります。それでも、「治療薬」をめぐって仲間の意見が割れるという題材そのものは、X-MEN らしくて考えさせられます。",
        "I understand the complaint that it crams in too much. Still, the idea of a \"cure\" dividing the team is very X-Men and gives you something to think about.",
    ),
    "x-men-days-of-future-past": (
        "新旧のキャストを1本につないだ、シリーズのいいとこ取り。クイックシルバーの台所の場面は、何度観ても楽しいです。",
        "It joins the old and new casts in one film and takes the best of both. Quicksilver's kitchen scene is fun however many times I see it.",
    ),
    "x-men-apocalypse": (
        "敵の強さのわりに盛り上がりきらない所はありますが、若いメンバーがそろっていく過程は楽しい。マグニートーの家族の場面は、シリーズでも指折りの悲しさです。",
        "For such a powerful villain it never quite takes off, but watching the young team come together is fun. The scene with Magneto's family is among the saddest in the series.",
    ),
    "x-men-dark-phoenix": (
        "評価は低めですが、ジーンの苦しみにしぼった小さな話として観ると印象が変わります。長く続いたシリーズの終わりとしては、もう少し派手でもよかったとは思います。",
        "It's poorly rated, but it reads differently as a small story focused on Jean's suffering. As the end of a long series, though, I do think it could have gone bigger.",
    ),
    "deadpool-and-wolverine": (
        "20世紀フォックス時代の作品への、にぎやかなお別れ会。悪ふざけの裏で、ローガンがもう一度「ヒーローになる」話をきちんとやっているのが好きです。",
        "A noisy farewell party for the 20th Century Fox era. Behind all the mischief, it properly tells a story of Logan becoming a hero once more, and I like that.",
    ),
    "agatha-all-along": (
        "悪役のはずのアガサが、だんだん憎めなくなっていく作品。「魔女の道」の歌の使い方と、ティーンの正体の明かし方がうまいと思います。",
        "Agatha is supposed to be a villain, yet she becomes harder and harder to dislike. I think the use of the Witches' Road song and the way Teen's identity is revealed are both clever.",
    ),
    "brave-new-world": (
        "血清を打っていないサムが、それでもキャプテン・アメリカをやる意味を描いた作品。ファルコン＆ウィンター・ソルジャーを観てからだと、サムの重圧がよく分かります。",
        "It's about what it means for Sam, with no serum, to be Captain America anyway. Watch The Falcon and the Winter Soldier first and the pressure on him makes much more sense.",
    ),
    "fantastic-four-first-steps": (
        "ほかの作品を知らなくても楽しめる、ひとつの家族の話。60年代ふうの明るい世界の見た目が、今までの MCU とちがっていて新鮮です。",
        "A story about one family that you can enjoy without knowing any other title. The bright 60s-style world looks unlike anything else in the MCU, which is refreshing.",
    ),
    "thunderbolts": (
        "立派ではない人たちが、それでもだれかを助けようとする話。派手な戦いより、エレーナの「むなしさ」と向き合う場面のほうが心に残ります。",
        "People who are far from admirable try to help someone anyway. Yelena facing her own emptiness stays with me more than any of the big fights.",
    ),
    "spider-man-2002": (
        "「大いなる力には、大いなる責任がともなう」は、やはりこの1本から。今の映画より素朴ですが、ピーターのさえない毎日がいちばんていねいに描かれていると思います。",
        "\"With great power comes great responsibility\" really begins here. It's plainer than today's films, but I think no other version shows Peter's unglamorous daily life with such care.",
    ),
    "spider-man-2-2004": (
        "ヒーロー映画の手本と言われるのも分かります。電車を止めたあと、乗客がピーターを守る場面は、何度観ても胸にきます。",
        "I can see why it's called a model superhero film. The passengers protecting Peter after he stops the train moves me every time.",
    ),
    "spider-man-3-2007": (
        "敵が多すぎるのは確か。それでも、サンドマンを「ゆるす」結末と、ハリーとの友情のしめ方は、3部作の終わりとして好きです。",
        "It does have too many villains. Even so, I like the ending as the close of a trilogy: forgiving Sandman, and how the friendship with Harry is resolved.",
    ),
    "venom": (
        "こわい話かと思ったら、エディとヴェノムの掛け合いを楽しむ相棒ものだった、という作品。2人の言い合いが好きになれるかどうかで評価が決まります。",
        "You expect something scary and get a buddy comedy built on Eddie and Venom's banter. Whether you enjoy their arguing decides what you think of it.",
    ),
    "venom-carnage": (
        "上映時間が短く、勢いで走りきる1本。エディとヴェノムのけんかと仲直りは、ほとんど夫婦げんかで、そこがいちばん面白いと思います。",
        "Short and carried along by sheer momentum. Eddie and Venom's fight and make-up is basically a couple's quarrel, and I think that's the most fun part.",
    ),
    "venom-last-dance": (
        "3部作の終わりとして、エディとヴェノムの別れにしぼったのは正解だと思います。話の荒さはあっても、最後の場面はしっかりさびしいです。",
        "As the end of a trilogy, I think focusing on Eddie and Venom's goodbye was the right call. The plot is rough, but the final scene is properly sad.",
    ),
    "black-widow": (
        "ナターシャの「にせものの家族」が、本物より家族らしいのがいい。妹エレーナとの掛け合いが楽しく、エンドゲームのあとに観ると少し切なくなります。",
        "I like that Natasha's fake family feels more like family than a real one. Her scenes with her sister Yelena are fun, and a little bittersweet after Endgame.",
    ),
    "eternals": (
        "好みが分かれる作品ですが、「人類を見守るだけでいいのか」という問いは MCU の中でも大きい。景色の美しさは、シリーズでいちばんだと思います。",
        "It divides people, but \"Is it enough just to watch over humanity?\" is one of the bigger questions in the MCU. For sheer beauty of scenery, I think it's the best in the series.",
    ),
    "hawkeye": (
        "クリスマスに観たくなる、ほどよい軽さのドラマ。力を持たないクリントの疲れた感じと、ケイトの元気さの組み合わせがちょうどいいです。",
        "A pleasantly light series that makes you want to watch it at Christmas. Powerless, worn-out Clint paired with energetic Kate is a good balance.",
    ),
    "moon-knight": (
        "ほかの作品とほぼつながらないので、ここから観ても大丈夫。1人で何人も演じ分けるオスカー・アイザックを観るだけで元が取れます。",
        "It barely connects to anything else, so you can start here. Watching Oscar Isaac play several people in one body is worth it on its own.",
    ),
    "echo": (
        "MCU の中では地味ですが、手話と沈黙を使った戦いの見せ方はほかにない持ち味。キングピンのこわさは、ここでもしっかり出ています。",
        "Low-key by MCU standards, but its use of sign language and silence in fights is unlike anything else. Kingpin's menace comes across here too.",
    ),
    "she-hulk": (
        "画面のこちらに話しかけてくる、MCU でいちばんふざけたドラマ。最終話のやり方は賛否がありますが、ここまでやりきるのは気持ちいいと思います。",
        "The silliest series in the MCU, talking straight to the audience. The finale splits opinion, but I think committing to it that fully is refreshing.",
    ),
    "ms-marvel": (
        "ヒーローにあこがれる高校生カマラが、とにかくかわいい。家族と地元の人たちの温かさが、ほかの作品にない魅力です。",
        "Kamala, a high-schooler who idolises heroes, is simply adorable. The warmth of her family and neighbourhood is a charm no other title has.",
    ),
    "werewolf-by-night": (
        "白黒の古い怪物映画ふうに作った、1時間ほどの特別編。短くてほかとつながらないので、気軽に観られる変わり種としておすすめです。",
        "An hour-long special made in the style of an old black-and-white monster movie. It's short and stands alone, so I'd recommend it as an easy oddity.",
    ),
    "guardians-holiday-special": (
        "ケヴィン・ベーコンを本人役でさらってくるという、ばかばかしくて楽しい短編。マンティスとピーターの関係が分かる、意外と大事な1本でもあります。",
        "A silly, fun short about kidnapping Kevin Bacon as himself. It's also surprisingly important, since it reveals how Mantis and Peter are related.",
    ),
    "secret-invasion": (
        "評判は厳しく、正直もったいない作品だと思います。それでも、年を取って弱ったフューリーという見せ方は、ほかでは見られません。",
        "Reviews were harsh and, honestly, I think it's a missed opportunity. Even so, an aged, weakened Fury is something you won't see anywhere else.",
    ),
    "the-marvels": (
        "3人が入れかわりながら戦う場面は、アイデアとして楽しい。短くて軽いので、ミズ・マーベルのカマラが好きなら観て損はないと思います。",
        "The fights where the three keep swapping places are a fun idea. It's short and light, so if you like Kamala from Ms. Marvel, I don't think you'll regret it.",
    ),
    "logan": (
        "ヒーロー映画というより、年老いた男の最後の旅を描いた西部劇。ローガンの終わり方として、これ以上のものはないと思います。",
        "Less a superhero film than a western about an old man's last journey. As an ending for Logan, I don't think it could be bettered.",
    ),
    "deadpool": (
        "悪ふざけと下品さの裏で、やっていることは素直な恋愛もの。低予算を自分で笑いにしてしまう開き直りが、この作品のいちばんの武器です。",
        "Behind the mischief and crude jokes, it's a straightforward love story. Laughing at its own low budget is the film's best weapon.",
    ),
    "deadpool-2": (
        "1作目より笑いも人数も増えた続編。ケーブルとの関係と、おまけ映像での「やり直し」は、シリーズの中でも特に好きな場面です。",
        "A sequel with more jokes and more people than the first. The relationship with Cable and the post-credits \"do-overs\" are among my favourite moments in the series.",
    ),
    "daredevil-born-again-s1": (
        "MCU の中ではかなり暗く、痛みのある作品。マットとフィスクが、表の顔を保とうとするほど裏の顔が出てくる、という並べ方が面白いです。",
        "Dark and bruising by MCU standards. I like how Matt and Fisk are set side by side: the harder each tries to keep up his public face, the more the other one shows.",
    ),
    "ironheart": (
        "トニーとちがって、お金のない天才がスーツを作る話。リリの「近道を選んでしまう弱さ」をそのまま描いているところが、人間らしくていいと思います。",
        "Unlike Tony, this is a genius with no money building a suit. I think showing Riri's weakness for shortcuts as it is makes her feel human.",
    ),
    "visionquest": (
        "ワンダヴィジョンの続きとして、ヴィジョンが「自分はだれか」を探す話。記憶はあるのに気持ちがない、という出発点が切なくて、1話ごとに追う価値があると思います。",
        "A follow-up to WandaVision in which Vision searches for who he is. Starting with memories but no feelings is a sad place to begin, and I think it's worth following week by week.",
    ),
    "amazing-spider-man": (
        "アンドリュー・ガーフィールドのピーターは、3人の中でいちばん今どきの若者らしい。グウェンとのやり取りの自然さが、この作品の強みです。",
        "Andrew Garfield's Peter feels the most like a present-day teenager of the three. How natural his scenes with Gwen are is this film's strength.",
    ),
    "amazing-spider-man-2": (
        "敵を出しすぎたのは確かですが、グウェンの結末だけは忘れられません。ノー・ウェイ・ホームを観たあとだと、あの場面の意味がさらに重くなります。",
        "It does have too many villains, but Gwen's ending is impossible to forget. After No Way Home, that scene means even more.",
    ),
}
