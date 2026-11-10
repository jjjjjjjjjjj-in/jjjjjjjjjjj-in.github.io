# 『ブラックパンサー』シーンごとの詳しいあらすじ
# 2026-11-10 ファルコン＆ウィンター・ソルジャーと同じ形に書き直した（運営者の希望）。
# 英語版・日本語版ウィキペディアのあらすじと登場人物の記事で事実を確かめた。
# 資料どうしで食い違う所（ンジョブの死が事故か、わざとか、など）や、確かめられない細かい順番・数字は書いていない。
# 日本語のせりふは日本語のサイトで言い回しを確かめられなかったので、カギかっこで引用せず内容だけ書いた。
# 人物名は相関図（relations.py）にそろえた（クラウ、ンジョブ、ウカビ）。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 ワカンダのはじまり", "Part 1: How Wakanda began", [
        ("空から落ちた金属",
         "暗い画面の中で、子どもが父親に、故郷の話をしてほしいとせがみ、父親が昔話を語り始める。\n"
         "大昔、アフリカに、不思議な金属ヴィブラニウムでできた隕石が落ちた。その土地をめぐって5つの部族が争った。ある戦士が、ヴィブラニウムの影響を受けたハート型のハーブを口にして、超人的な力を持つ最初の「ブラックパンサー」になった。\n"
         "彼のもとに4つの部族が集まり、国ワカンダができた。山に住むジャバリ族だけは加わらなかった。",
         "Metal from the sky",
         "In darkness, a child asks his father for a story about home, and the father begins.\n"
         "Long ago, a meteorite made of the strange metal vibranium fell in Africa, and five tribes fought over the land. One warrior ate a heart-shaped herb changed by the metal and became the first Black Panther, with superhuman strength.\n"
         "Four of the tribes united under him to form the nation of Wakanda. Only the Jabari, who live in the mountains, refused to join."),
        ("隠された国",
         "何百年もかけて、ワカンダはヴィブラニウムを使ってとても進んだ技術を育てた。\n"
         "その一方で、世界の争いに巻きこまれないよう、豊かさを隠し、農業しかない貧しい国のふりをして、外の世界と関わらずに生きてきた。",
         "The hidden nation",
         "Over centuries, Wakanda used vibranium to build extraordinarily advanced technology.\n"
         "To stay out of the world's wars, it hid its wealth, posed as a poor farming country, and kept itself apart from the rest of the world."),
        ("1992年のオークランド",
         "1992年、アメリカのカリフォルニア州オークランド。アパートの一室で、ワカンダから送りこまれて暮らすンジョブが、仲間の男と銃や地図を前に計画を練っている。外では子どもたちがバスケットボールをしている。\n"
         "そこへ、ワカンダの国王でンジョブの兄、ティ・チャカが、ブラックパンサーのスーツ姿で親衛隊の女性戦士2人を連れて現れる。\n"
         "ティ・チャカは、武器商人ユリシーズ・クラウがワカンダからヴィブラニウムを盗み出した事件に、ンジョブが手を貸したと問いつめる。ンジョブは否定するが、一緒にいた男が、自分はワカンダの仲間ズリで、ンジョブを見張っていたと明かす。\n"
         "外では、子どもたちが、空に浮かんで去っていく不思議な光る船を見上げている。",
         "Oakland, 1992",
         "Oakland, California, 1992. In an apartment, N'Jobu, a Wakandan agent living undercover, plans something with a partner over guns and maps. Outside, kids are playing basketball.\n"
         "N'Jobu's older brother, King T'Chaka of Wakanda, arrives in the Black Panther suit with two warriors of his guard.\n"
         "T'Chaka accuses N'Jobu of helping the arms dealer Ulysses Klaue steal vibranium from Wakanda. N'Jobu denies it, but his partner reveals that he is Zuri, a fellow Wakandan who had been watching him.\n"
         "Outside, the kids look up as a strange glowing aircraft lifts into the sky and disappears."),
    ]),
    ("第2部 新しい国王", "Part 2: The new king", [
        ("森の救出",
         "現代。父ティ・チャカが爆破テロで亡くなったあと、息子のティ・チャラは王になるためワカンダへ帰ろうとしている。\n"
         "その前に、ティ・チャラは親衛隊ドーラ・ミラージュの隊長オコエと、ナイジェリアの森へ向かう。さらわれた女性たちを運ぶトラックの列に、ワカンダのスパイで元恋人のナキアが、女性たちの一人になりすまして潜りこんでいた。\n"
         "ティ・チャラはブラックパンサーとなってトラックをおそい、武装した男たちを倒す。ナキアを見たとたん、ティ・チャラは固まってしまい、オコエにからかわれる。ナキアは、銃を持たされていた少年兵を傷つけずに家へ帰す。\n"
         "ナキアは自分の任務をじゃまされて不満だが、ティ・チャラは、王になる儀式に来てほしいと頼み、一緒にワカンダへ連れて帰る。",
         "Rescue in the forest",
         "The present. After his father T'Chaka was killed in a bombing, his son T'Challa is about to return to Wakanda to become king.\n"
         "First, T'Challa and Okoye, leader of the royal guard the Dora Milaje, head to a forest in Nigeria. Nakia, a Wakandan spy and T'Challa's ex, has slipped into a convoy of kidnapped women, posing as one of them.\n"
         "As Black Panther, T'Challa attacks the trucks and takes down the armed men. The moment he sees Nakia he freezes, and Okoye teases him. Nakia sends a boy soldier home unharmed.\n"
         "Nakia is annoyed that her mission was cut short, but T'Challa asks her to attend his coronation and brings her back to Wakanda."),
        ("黄金の都",
         "乗り物は森に見える幻の壁をくぐりぬけ、ワカンダの都に入る。そこは高い建物が並び、空飛ぶ乗り物が行き交う、世界のどこよりも進んだ町だった。\n"
         "着いたティ・チャラを、母ラモンダと妹シュリが迎える。シュリは兄をからかいながら、儀式の準備に向かう。",
         "The golden city",
         "Their craft passes through a holographic barrier that looks like forest and enters Wakanda's capital: a city of towers and flying vehicles, more advanced than anywhere on Earth.\n"
         "His mother Ramonda and younger sister Shuri greet him. Shuri teases her brother as they get ready for the ceremony."),
        ("滝の儀式",
         "王になる儀式は、大きな滝の下の岩場で行われる。各部族の人々が崖の上から見守る。\n"
         "長老ズリが、ブラックパンサーの力を取り去る飲み物をティ・チャラに与える。ズリが王の座をかけて挑む者はいるかとたずね、どの部族も名乗り出ない。そこへ、国に加わらなかったジャバリ族が現れる。",
         "The ritual at the falls",
         "The coronation takes place on the rocks below a huge waterfall, with the tribes watching from the cliffs.\n"
         "The elder Zuri gives T'Challa a drink that takes away the Black Panther's powers. Zuri asks whether anyone will challenge for the throne, and no tribe steps forward. Then the Jabari, who never joined the nation, appear."),
        ("エムバクの挑戦",
         "ジャバリ族の長エムバクが、王の座をかけた決闘を申しこむ。ティ・チャラは力のないまま、素手と槍で戦う。\n"
         "押されて追いつめられたティ・チャラは、母ラモンダの声にはげまされて立ち上がり、エムバクを押さえこむ。ティ・チャラは、命を落とすより降参してほしいと説き、エムバクは降参する。\n"
         "ティ・チャラはワカンダの国王になる。",
         "M'Baku's challenge",
         "M'Baku, leader of the Jabari, challenges T'Challa for the throne. Without his powers, T'Challa fights with his hands and a spear.\n"
         "Pushed to the edge, he rallies when his mother Ramonda calls out to him, and pins M'Baku. T'Challa urges him to yield rather than die, and M'Baku yields.\n"
         "T'Challa becomes king of Wakanda."),
        ("祖先の世界",
         "その夜、ティ・チャラはハート型のハーブを飲み、ブラックパンサーの力を取り戻す。ズリたちは彼を赤い砂の中に横たえる。\n"
         "ティ・チャラの心は、むらさきの空の下の草原「祖先の世界」へ運ばれる。木の上にいた黒ヒョウたちの中から、亡くなった父ティ・チャカが現れる。\n"
         "ティ・チャラは、父のいない国でどう王を務めればいいか分からないと打ち明ける。父は、よい心を持つ者が王でいるのは難しいことだと語りかける。",
         "The Ancestral Plane",
         "That night T'Challa drinks the heart-shaped herb and gets the Black Panther's powers back. Zuri and the others lay him in red sand.\n"
         "His mind travels to the Ancestral Plane, a grassland under a purple sky. Among the black panthers in a tree, his late father T'Chaka appears.\n"
         "T'Challa admits he doesn't know how to rule without him. His father tells him how hard it is for a good man to be king."),
    ]),
    ("第3部 盗まれた斧", "Part 3: The stolen axe", [
        ("ロンドンの博物館",
         "イギリス・ロンドンの博物館。エリックという男が、アフリカの展示を見ながら係の女性に質問し、ある斧は別の国のものとされているが、本当はワカンダのヴィブラニウムでできていると言い当てる。\n"
         "女性は、飲んだコーヒーに入れられた毒で倒れる。救急隊員にふんした男たちはクラウとその仲間で、エリックの仲間リンダもいた。彼らは警備員を倒し、斧を盗む。エリックは展示されていた仮面も持ち去る。",
         "The London museum",
         "A museum in London. A man named Erik asks a staff member about the African exhibits and tells her that one axe, labeled as coming from another country, is really Wakandan and made of vibranium.\n"
         "She collapses, poisoned by her coffee. The men dressed as paramedics are Klaue and his crew, along with Erik's partner Linda. They take out the guards and steal the axe. Erik also takes a mask from the display."),
        ("ウカビの怒り",
         "クラウがまた現れたことは、すぐにワカンダに伝わる。国境を守る部族の長で、ティ・チャラの親友、オコエの夫でもあるウカビは怒る。クラウは昔ヴィブラニウムを盗み出したとき、ウカビの両親を殺していたからだ。\n"
         "ティ・チャラは、クラウを捕まえてワカンダへ連れ帰ると約束する。",
         "W'Kabi's anger",
         "News that Klaue has resurfaced quickly reaches Wakanda. W'Kabi, chief of the Border Tribe, T'Challa's best friend and Okoye's husband, is furious: when Klaue stole vibranium years ago, he killed W'Kabi's parents.\n"
         "T'Challa promises to bring Klaue back to Wakanda."),
        ("ナキアの願い",
         "ナキアは、世界を旅して苦しむ人々を見てきた。ワカンダはその力で、難民を受け入れたり、助けを送ったりするべきだと考えている。\n"
         "ティ・チャラは、ナキアにワカンダに残ってほしいと願うが、国を開けば守ってきたものを失うおそれがあると迷う。ウカビは、外の人を入れれば外の問題も入ってくると反対する。",
         "Nakia's wish",
         "Nakia has traveled the world and seen people suffering. She believes Wakanda should use its power to take in refugees and send aid.\n"
         "T'Challa wants her to stay in Wakanda, but worries that opening the country could cost it everything it has protected. W'Kabi argues that letting outsiders in would bring their problems too."),
        ("シュリの研究所",
         "クラウが韓国の釜山で、盗んだ斧を売ろうとしていると分かる。\n"
         "出発の前に、ティ・チャラはシュリの研究所を訪ねる。シュリは、足音を消す靴や、遠くから乗り物を操る道具、ネックレスにしまえる新しいブラックパンサーのスーツを見せる。新しいスーツは、受けた衝撃をためて、はね返すことができる。",
         "Shuri's lab",
         "They learn that Klaue plans to sell the stolen axe in Busan, South Korea.\n"
         "Before leaving, T'Challa visits Shuri's lab. She shows him shoes that silence footsteps, tools for driving vehicles remotely, and a new Black Panther suit that folds into a necklace. The suit absorbs the energy of blows and can release it back."),
    ]),
    ("第4部 釜山の夜", "Part 4: A night in Busan", [
        ("カジノに潜入",
         "ティ・チャラ、オコエ、ナキアは釜山の地下カジノに潜入する。オコエはかつらをかぶるのをいやがる。\n"
         "カジノには、CIAの捜査官エヴェレット・ロスがいた。ロスは、クラウから斧をダイヤモンドで買う客として来ていた。ティ・チャラは、前に会ったことのあるロスに、クラウは自分が連れていくと告げる。",
         "Into the casino",
         "T'Challa, Okoye and Nakia slip into an underground casino in Busan. Okoye hates having to wear a wig.\n"
         "CIA agent Everett Ross is there as Klaue's buyer, ready to pay for the axe with diamonds. T'Challa, who has met Ross before, tells him that he will be taking Klaue."),
        ("銃撃戦",
         "取り引きの最中に、クラウはワカンダの者がいると気づき、カジノで銃撃戦が始まる。オコエとナキアは、クラウの手下たちと激しく戦う。\n"
         "クラウは、義手に仕込んだ音波の大砲を撃ちながら、外へ逃げ出す。",
         "The shootout",
         "During the deal Klaue realizes Wakandans are present, and a shootout breaks out. Okoye and Nakia fight his men hard.\n"
         "Klaue escapes outside, firing the sonic cannon built into his artificial arm."),
        ("釜山の追跡",
         "クラウと手下は車で逃げる。ナキアとオコエが車で追い、ティ・チャラは別の車の屋根に乗って追う。その車は、ワカンダの研究所にいるシュリが遠くから運転している。\n"
         "クラウは音波の大砲で追っ手の車を吹き飛ばす。ティ・チャラはスーツにためた衝撃を放ってクラウの車をひっくり返し、クラウを捕まえる。",
         "The Busan chase",
         "Klaue and his men flee by car. Nakia and Okoye give chase, while T'Challa rides on the roof of a car that Shuri drives remotely from her lab in Wakanda.\n"
         "Klaue blasts the pursuing cars with his sonic cannon. T'Challa releases the energy stored in his suit to flip Klaue's car and catches him."),
        ("ロスの取り調べ",
         "まわりで人々が携帯電話で撮影している中、ティ・チャラはクラウを殺さずに、ロスに引き渡す。\n"
         "CIAの隠れ家で、ロスはクラウを取り調べる。クラウは、ワカンダは貧しい国などではなく、ヴィブラニウムで栄える、とても進んだ国だと話してしまう。",
         "Ross's interrogation",
         "With bystanders filming on their phones, T'Challa spares Klaue and hands him over to Ross.\n"
         "At a CIA safe house, Ross questions Klaue, who reveals that Wakanda is no poor country but a highly advanced civilization built on vibranium."),
        ("エリックの襲撃",
         "そこへエリックとリンダたちがおそいかかり、クラウを助け出す。ロスは、ナキアをかばって背中に弾を受け、大けがをする。\n"
         "ティ・チャラはエリックを追うが、エリックが首にかけていた指輪を見て、足が止まる。それはワカンダの王家の指輪だった。エリックとクラウは逃げ去る。",
         "Erik's attack",
         "Erik, Linda and their crew attack and break Klaue out. Ross takes a bullet in the back protecting Nakia and is badly hurt.\n"
         "T'Challa goes after Erik but stops short when he sees the ring hanging from Erik's neck: a ring of the Wakandan royal family. Erik and Klaue get away."),
        ("ロスをワカンダへ",
         "このままではロスは助からない。ティ・チャラは、クラウを追うのをやめ、ワカンダの技術で治すため、ロスを国に連れて帰る。",
         "Taking Ross to Wakanda",
         "Ross won't survive without help. T'Challa gives up the chase and takes Ross to Wakanda, where its technology can save him."),
    ]),
    ("第5部 父の秘密", "Part 5: His father's secret", [
        ("ウカビの失望",
         "シュリはロスの治療にとりかかる。\n"
         "クラウを連れて帰れなかったと知り、ウカビはティ・チャラに深く失望する。",
         "W'Kabi's disappointment",
         "Shuri begins treating Ross.\n"
         "W'Kabi, learning that T'Challa failed to bring Klaue back, is deeply disappointed in him."),
        ("ズリの告白",
         "ティ・チャラはズリのもとへ行き、問いつめる。エリックが王家の指輪を持っていたからだ。\n"
         "ズリは、1992年の本当のことを話す。ンジョブはアメリカで、世界中のアフリカ系の人々が苦しむのを見て、ワカンダの技術と武器を渡して立ち上がらせようと考え、クラウと手を組んでいた。\n"
         "ティ・チャカがンジョブを連れ帰ろうとしたとき、ンジョブはズリにおそいかかり、ティ・チャカはズリを守るためにンジョブを殺した。ティ・チャカは、ンジョブは姿を消したことにしろとズリに命じ、その話を守るため、アメリカにいたンジョブの幼い息子を置き去りにした。\n"
         "ティ・チャラは、尊敬していた父の行いに大きな衝撃を受ける。",
         "Zuri's confession",
         "T'Challa goes to Zuri and confronts him, because Erik wore the royal ring.\n"
         "Zuri tells him the truth about 1992. In America, N'Jobu saw people of African descent suffering around the world and planned, with Klaue's help, to give them Wakanda's technology and weapons so they could rise up.\n"
         "When T'Chaka moved to bring him home, N'Jobu attacked Zuri, and T'Chaka killed him to protect Zuri. T'Chaka ordered Zuri to say that N'Jobu had disappeared and, to keep that story, left N'Jobu's young son behind in America.\n"
         "T'Challa is shaken by what the father he revered had done."),
        ("リンダとクラウの最期",
         "そのころ、エリックとクラウの一味は、飛行機の待つ場所へ逃げてきていた。\n"
         "エリックがワカンダへ行くつもりだと分かり、クラウはエリックの恋人リンダを人質にして銃を向ける。エリックはためらわずにリンダを撃ち、続けてクラウも撃ち殺す。",
         "The end of Linda and Klaue",
         "Meanwhile, Erik and Klaue's crew have fled to an airfield.\n"
         "Realizing that Erik means to go to Wakanda, Klaue grabs Erik's girlfriend Linda as a shield and points a gun. Erik shoots Linda without hesitation, then shoots Klaue dead."),
        ("国境に届いたもの",
         "エリックはクラウの死体を持って、ワカンダの国境に現れる。クラウを憎んでいたウカビは、エリックを都の王の間へ連れていく。",
         "A delivery at the border",
         "Erik arrives at Wakanda's border with Klaue's body. W'Kabi, who hated Klaue, brings him to the throne room in the capital."),
        ("エリックの正体",
         "シュリの研究所で目を覚ましたロスは、エリックの姿を見て、彼を知っていると言う。アメリカの大学を出て、海軍の特殊部隊に入り、ひそかな作戦で外国の政府をくつがえすために人を殺してきた兵士で、「キルモンガー」と呼ばれていた。\n"
         "王の間で、エリックは自分の本当の名前はンジャダカで、ンジョブの息子だと名乗る。そして、王家の血を引く者として、王の座をかけた決闘を申しこむ。ティ・チャラは挑戦を受ける。",
         "Who Erik is",
         "Waking up in Shuri's lab, Ross sees Erik and recognizes him: a U.S. Navy SEAL with an American university education, who killed people in secret operations to bring down foreign governments, nicknamed Killmonger.\n"
         "In the throne room, Erik reveals that his real name is N'Jadaka and that he is N'Jobu's son. As one of royal blood, he challenges T'Challa for the throne, and T'Challa accepts."),
    ]),
    ("第6部 奪われた王座", "Part 6: The throne is taken", [
        ("滝の決闘",
         "ふたたび滝の儀式が開かれる。エリックの体には、殺した人の数だけ刻んだ傷が並んでいる。\n"
         "迷いをかかえたティ・チャラは押され続ける。ズリが止めに入ると、エリックはズリを刺し殺す。ンジョブを守らなかったズリを恨んでいたのだ。\n"
         "エリックはティ・チャラを打ち負かし、滝の上から下へ投げ落とす。ティ・チャラは死んだと思われ、エリックが国王になる。",
         "The duel at the falls",
         "The ritual at the falls is held again. Erik's body is covered in scars, one for each person he has killed.\n"
         "Shaken, T'Challa is overwhelmed. When Zuri steps in, Erik stabs him to death, blaming him for not protecting N'Jobu.\n"
         "Erik defeats T'Challa and throws him off the falls. T'Challa is presumed dead, and Erik becomes king."),
        ("エリックの祖先の世界",
         "エリックもハート型のハーブを飲み、祖先の世界へ行く。そこは草原ではなく、オークランドのあのアパートだった。\n"
         "子どものころの姿のエリックの前に、父ンジョブが現れる。子どものころのエリックは、殺された父の遺体を見つけていた。父は、自分の死で泣かない息子を悲しむ。",
         "Erik's Ancestral Plane",
         "Erik also takes the heart-shaped herb and goes to the Ancestral Plane. For him, it isn't a grassland but the Oakland apartment.\n"
         "Erik, as a boy, meets his father N'Jobu. As a child, Erik had found his father's body. N'Jobu is saddened that his son sheds no tears for him."),
        ("燃やされるハーブ",
         "目を覚ましたエリックは、ハーブの畑を全部燃やせと命じ、断ろうとした年老いた女性の首をつかむ。こうして、もう誰もブラックパンサーになれなくなる。\n"
         "エリックは、ウカビの部隊と一緒に、ワカンダの武器を世界中の街にいる仲間へ送る準備を始める。",
         "Burning the herb",
         "When he wakes, Erik orders the entire herb garden burned, grabbing the throat of the elderly woman who tries to refuse. Now no one else can become Black Panther.\n"
         "With W'Kabi's forces, Erik prepares to ship Wakandan weapons to operatives in cities around the world."),
        ("ナキアの決断",
         "ナキアは、燃やされる前にハーブを1本だけ持ち出す。\n"
         "ナキアはオコエに一緒に来てと頼むが、オコエは、自分は王座に仕える身だと言って残る。ナキア、シュリ、ラモンダ、ロスは都を逃げ出す。",
         "Nakia's choice",
         "Nakia manages to save a single herb before the rest are burned.\n"
         "She asks Okoye to come with her, but Okoye stays, saying her loyalty is to the throne. Nakia, Shuri, Ramonda and Ross flee the capital."),
        ("ジャバリの山",
         "ラモンダはナキアにハーブを飲んで戦うよう勧めるが、ナキアはエムバクに渡して戦ってもらおうと考え、4人は雪のジャバリの山へ向かう。\n"
         "エムバクは4人を、雪の中で眠るティ・チャラのところへ案内する。ジャバリの漁師が川で見つけ、決闘で命を助けてもらったお礼に、雪で冷やして命をつないでいたのだ。",
         "The Jabari mountains",
         "Ramonda urges Nakia to take the herb and fight, but Nakia plans to give it to M'Baku so he can fight, and the four head for the snowy Jabari mountains.\n"
         "M'Baku leads them to T'Challa, lying unconscious in the snow. A Jabari fisherman found him in the river, and in return for T'Challa sparing M'Baku's life, they have kept him alive packed in snow."),
        ("父への言葉",
         "ナキアの持ってきたハーブを飲ませると、ティ・チャラは祖先の世界へ行く。\n"
         "ティ・チャラは父と祖先たちに向かい、世界に背を向け、置き去りにした少年を見捨てたのはまちがいだったと告げる。そして、自分は王としてそのあやまちを正すと決める。\n"
         "ティ・チャラは目を覚まし、力を取り戻す。エムバクは一緒に戦うことを一度は断る。",
         "Words for his father",
         "Given Nakia's herb, T'Challa goes to the Ancestral Plane.\n"
         "He tells his father and the ancestors that it was wrong to turn their backs on the world and to abandon that boy, and resolves as king to set it right.\n"
         "T'Challa wakes with his powers restored. M'Baku at first declines to join the fight."),
    ]),
    ("第7部 ワカンダの戦い", "Part 7: The battle for Wakanda", [
        ("王の帰還",
         "武器を積んだ輸送機が飛び立とうとする場所に、シュリが作ったスーツを着たティ・チャラが現れ、決闘はまだ終わっていないと宣言する。\n"
         "エリックも、金色のブラックパンサーのスーツを着て迎えうつ。オコエたちドーラ・ミラージュは、生きていたティ・チャラの側につき、ウカビと国境の部族の兵士たちはエリックの側につく。",
         "The king returns",
         "As planes loaded with weapons prepare to take off, T'Challa appears in a suit Shuri made and declares that the challenge is not over.\n"
         "Erik meets him in a golden Black Panther suit. Okoye and the Dora Milaje side with the living T'Challa, while W'Kabi and the Border Tribe soldiers side with Erik."),
        ("ロスの空中戦",
         "シュリとナキアも、ドーラ・ミラージュとともに戦う。\n"
         "元空軍のパイロットだったロスは、シュリの研究所から遠くの戦闘機を操り、武器を積んだ輸送機を、ワカンダの外へ出る前に1機ずつ撃ち落としていく。",
         "Ross in the sky",
         "Shuri and Nakia fight alongside the Dora Milaje.\n"
         "Ross, a former Air Force pilot, remotely flies a fighter jet from Shuri's lab and shoots down the weapons planes one by one before they can leave Wakanda."),
        ("ジャバリの加勢",
         "押されていたティ・チャラたちのところへ、エムバクの率いるジャバリ族の戦士たちが駆けつける。",
         "The Jabari arrive",
         "As T'Challa's side is pushed back, M'Baku arrives leading the Jabari warriors."),
        ("オコエとウカビ",
         "ウカビは、よろいを着けたサイに乗ってエムバクたちを踏みつぶそうとする。オコエがウカビの前に立ちはだかり、愛より国を選ぶと槍を向ける。\n"
         "オコエを殺すことも、オコエに殺されることもできないウカビは、ひざをついて降参する。国境の部族の兵士たちもそれにならう。",
         "Okoye and W'Kabi",
         "W'Kabi charges on an armored rhino, trying to trample M'Baku and the others. Okoye stands in his way with her spear, saying she will choose her country over their love.\n"
         "Unable to kill her or be killed by her, W'Kabi kneels and surrenders, and the Border Tribe soldiers follow."),
        ("地下の決闘",
         "ティ・チャラとエリックは、地下にあるヴィブラニウムの鉱山へ落ちて戦い続ける。\n"
         "鉱山の線路が出す力で、2人のスーツは働かなくなる。ティ・チャラはそれを利用してエリックのスーツをこわし、槍の刃でエリックの胸を刺す。",
         "The duel underground",
         "T'Challa and Erik fall into the underground vibranium mine and keep fighting.\n"
         "The mine's tracks disrupt both suits. T'Challa uses this to break Erik's suit and stabs him in the chest with a spear blade."),
        ("夕日",
         "ティ・チャラは傷ついたエリックを山の上へ連れていき、エリックが子どものころ父ンジョブから聞かされていたワカンダの夕日を見せる。\n"
         "ティ・チャラは、まだ治せると言う。しかしエリックは、閉じこめられて生きるより自由に死ぬほうを選び、鎖につながれるより海へ飛びこんだ祖先と同じように海に葬ってほしいと言う。\n"
         "エリックは自分で刃を引き抜き、夕日を見ながら息を引き取る。",
         "The sunset",
         "T'Challa carries the wounded Erik up the mountain to see the Wakandan sunset Erik's father N'Jobu told him about when he was a boy.\n"
         "T'Challa says he can still be healed. But Erik chooses to die free rather than live locked up, and asks to be buried in the ocean with his ancestors who jumped from the ships, because they knew death was better than bondage.\n"
         "Erik pulls out the blade himself and dies watching the sunset."),
    ]),
    ("第8部 世界に開かれた国へ", "Part 8: Opening up to the world", [
        ("オークランドの建物",
         "しばらくして、ティ・チャラはシュリを連れてオークランドのあのアパートの前に来る。バスケットボールをしていた子どもたちが、2人の乗ってきた船に集まってくる。\n"
         "ティ・チャラは、まわりの建物を買い取ったと話す。ここをワカンダが外の世界を助ける最初の場所にして、ナキアとシュリにまかせると決める。",
         "The building in Oakland",
         "Some time later, T'Challa brings Shuri to that apartment building in Oakland. Kids who were playing basketball gather around their ship.\n"
         "T'Challa explains that he has bought the buildings. It will be Wakanda's first outreach center to the world, run by Nakia and Shuri."),
        ("エンドクレジットの途中",
         "ティ・チャラは国連で演説し、ワカンダの本当の姿を明かして、知識と技術を世界と分かち合うと発表する。",
         "Mid-credits",
         "At the United Nations, T'Challa reveals Wakanda's true nature and announces that it will share its knowledge and technology with the world."),
        ("エンドクレジットの後",
         "ワカンダの小屋で、バッキー・バーンズが目を覚ます。シュリがそばにいて、外では子どもたちが彼を「白い狼」と呼んでいる。シュリは、バッキーの回復を手伝っている。",
         "After the credits",
         "In a hut in Wakanda, Bucky Barnes wakes up with Shuri beside him, while children outside call him the White Wolf. Shuri is helping him recover."),
    ]),
    ("まとめ", "Summary", [
        ("キルモンガーの怒りと計画",
         "エリック（ンジャダカ）は、ンジョブの息子。1992年に父がティ・チャカに殺され、自分はアメリカに置き去りにされた（第1部・第5部）。\n"
         "アメリカ軍の兵士として人を殺す技を身につけ、クラウと組んでワカンダに近づき、最後はクラウを殺してその死体を手みやげに国へ入った（第3部〜第5部）。\n"
         "決闘でティ・チャラを倒して王になり、ハーブを燃やし、ワカンダの武器を世界中の仲間に送って、苦しむ人々を立ち上がらせようとした（第6部）。",
         "Killmonger's anger and plan",
         "Erik (N'Jadaka) is N'Jobu's son. In 1992 his father was killed by T'Chaka and he was left behind in America (Parts 1 and 5).\n"
         "He learned to kill as a U.S. soldier, teamed up with Klaue to get close to Wakanda, then killed Klaue and used his body to get into the country (Parts 3-5).\n"
         "He beat T'Challa in the duel, became king, burned the herbs, and set out to ship Wakandan weapons to operatives worldwide so oppressed people could rise up (Part 6)."),
        ("ティ・チャラが選んだ道",
         "ティ・チャラは、父がンジョブを殺し、その息子を見捨てたことを知って深く悩んだ（第5部）。\n"
         "祖先の世界で、世界に背を向けてきた父と祖先はまちがっていたと告げ（第6部）、エリックを倒したあと、オークランドに支援の場所を作り、国連でワカンダを世界に開くと発表した（第8部）。",
         "The path T'Challa chose",
         "T'Challa was deeply troubled to learn that his father killed N'Jobu and abandoned his son (Part 5).\n"
         "On the Ancestral Plane he told his father and ancestors they were wrong to turn their backs on the world (Part 6). After defeating Erik, he opened an outreach center in Oakland and announced at the UN that Wakanda would open up to the world (Part 8)."),
        ("死んだ人たち（話の順に）",
         "・ンジョブ（第5部、1992年の出来事）：ズリにおそいかかったため、ズリを守ろうとした兄ティ・チャカに殺された。\n"
         "・リンダ（第5部）：エリックの恋人。クラウに人質にされ、ためらわなかったエリックに撃たれた。\n"
         "・ユリシーズ・クラウ（第5部）：エリックに撃ち殺された。死体はワカンダに入るための手みやげにされた。\n"
         "・ズリ（第6部）：滝の決闘を止めようとして、エリックに刺し殺された。\n"
         "・エリック・キルモンガー（第7部）：鉱山の決闘でティ・チャラに刺され、治療を断って、夕日を見ながら亡くなった。",
         "Who died (in order)",
         "- N'Jobu (Part 5, events of 1992): killed by his brother T'Chaka, who was protecting Zuri after N'Jobu attacked him.\n"
         "- Linda (Part 5): Erik's girlfriend. Klaue took her hostage, and Erik shot her without hesitation.\n"
         "- Ulysses Klaue (Part 5): shot dead by Erik, whose body became Erik's ticket into Wakanda.\n"
         "- Zuri (Part 6): stabbed to death by Erik while trying to stop the duel at the falls.\n"
         "- Erik Killmonger (Part 7): stabbed by T'Challa in the mine duel; he refused healing and died watching the sunset."),
    ]),
]
