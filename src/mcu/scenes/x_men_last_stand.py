# 『X-MEN：ファイナル ディシジョン』（2006年）シーンごとの詳しいあらすじ
# 2026-11-10 書き直し。英語版ウィキペディアのあらすじ（今の版と、2006・2009・2014・2018年の版）、登場人物の一覧の記事、日本語版ウィキペディア（人物名の表記）、検索結果と照らし合わせて、順番と事実を確かめた。
# 運営者の希望（あらすじの直し方）: 第1部から始め、場面ごとに起きた事実だけを書く。見出しはつながった場面でまとめる。
# 資料どうしで食い違う所（最後のチェスの場所、治療薬のことを聞いたボビーの気持ち、スコットの葬儀など）や、確かめられなかった所（ローガンが森の隠れ家へ行く場面、キティとボビーのスケートの場面、ローグが治療薬を受けに行くときのローガンとのやりとりなど）は書いていない。
# セリフは日本語の言い回しを確かめられなかったので、日本語版はカギかっこで引用せず内容だけ書いた。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
SCENE_NUMBERS = True  # 場面に「部-番号」を付ける（観ながら照らし合わせるため）
SCENES = [
    ("第1部 2つの昔の話", "Part 1: Two flashbacks", [
        ("20年前のジーン",
         "20年前。チャールズ・エグゼビア（プロフェッサーX）とエリック・レーンシャー（マグニートー）が、2人そろって少女ジーン・グレイの家を訪ねる。娘の「病気」を心配した両親に呼ばれたのだった。\n"
         "ジーンは手をふれずに、家の前の車や物をいくつも宙に浮かせてみせる。まだ友人どうしだった2人は、ジーンを自分たちの学園に誘う。",
         "Jean, twenty years ago",
         "Twenty years earlier, Charles Xavier (Professor X) and Erik Lehnsherr (Magneto) visit young Jean Grey's home together. Her parents called them, worried about what they think is an 'illness'.\n"
         "Without touching anything, Jean lifts several cars and other objects outside the house into the air. The two men, still friends at this point, invite her to their school."),
        ("10年前のウォーレン",
         "それから10年後。大企業の社長ウォーレン・ワージントン2世は、息子が、背中に生えてきた翼の羽根を必死にそり落とそうとしているのを見つける。\n"
         "息子はミュータントだった。父親は言葉を失う。",
         "Warren, ten years later",
         "Ten years later, industrialist Warren Worthington II finds his son desperately trying to shave off the feathers of the wings growing from his back.\n"
         "His son is a mutant. The father is speechless."),
    ]),
    ("第2部 治療薬の発表", "Part 2: The cure", [
        ("デンジャールームの訓練",
         "今。学園の地下の訓練室デンジャールームで、ストームとローガンが、ローグ、ボビー（アイスマン）、キティ、コロッサスたちの訓練を行っている。\n"
         "相手は、ミュータントを狩る巨大なロボット「センチネル」の立体映像。最後は、コロッサスが投げ飛ばしたローガンが、ロボットの首を切り落として終わる。",
         "Danger Room drills",
         "In the present, Storm and Logan run a training session in the Danger Room beneath the school for Rogue, Bobby (Iceman), Kitty and Colossus.\n"
         "Their opponent is a hologram of a giant mutant-hunting robot, a Sentinel. It ends when Colossus hurls Logan at the robot and Logan cuts off its head."),
        ("ジーンを失ったスコット",
         "スコット（サイクロップス）は、前の戦いでアルカリ湖に消えたジーンを失った悲しみから抜け出せずにいる。夜になると、ジーンの声が聞こえてくる。",
         "Scott in mourning",
         "Scott (Cyclops) still can't get over losing Jean, who vanished into Alkali Lake in the last battle. At night, he hears her voice."),
        ("ホワイトハウスのハンク",
         "政府でミュータントの問題を担当する長官ハンク・マッコイ（ビースト）は、青い毛におおわれたミュータントで、X-MENとは昔からのつながりがある。\n"
         "ハンクは大統領たちと会い、ワージントン社がミュータントの力を消す方法を見つけたと聞かされる。そのころミスティークは政府に捕まり、取り調べを受けていた。",
         "Hank at the White House",
         "Hank McCoy (Beast), the government's Secretary of Mutant Affairs, is a blue-furred mutant with a long history with the X-Men.\n"
         "Meeting with the President and his staff, Hank learns that Worthington Labs has found a way to remove mutant powers. Meanwhile, Mystique has been captured by the government and is being interrogated."),
        ("「治療薬」の発表",
         "ワージントン社は、ミュータントに力を与えている遺伝子のはたらきを抑える注射、つまり「治療薬（キュア）」を発表し、望むミュータントには誰にでも打つと言う。\n"
         "治療薬は、ジミーという少年のミュータントの体から作られていた。ジミーは、近くにいるミュータントの力を消してしまう。彼はサンフランシスコ湾のアルカトラズ島にある、ワージントン社の研究所にいる。",
         "The cure is announced",
         "Worthington Labs announces an injection that suppresses the gene that gives mutants their powers, a 'cure', and offers it to any mutant who wants it.\n"
         "The cure is made from a young mutant named Jimmy, whose presence switches off the powers of mutants near him. He lives at the Worthington facility on Alcatraz Island in San Francisco Bay."),
        ("分かれるミュータントたち",
         "ミュータントの間では、治療薬を受けたいという人と、ミュータントであることを病気あつかいされたと怒る人に分かれる。\n"
         "学園でも、ストームは強く反対する。いっぽう、ふれた相手の命や力を吸ってしまうローグは、恋人のボビーにもふれられない。ボビーがキティと親しくしているのを見て、ローグの心は治療薬にかたむいていく。",
         "A divided community",
         "Mutants split between those who want the cure and those outraged at being treated as if they were sick.\n"
         "At the school, Storm is firmly against it. Rogue, whose touch drains the life and powers of anyone she touches, can't even touch her boyfriend Bobby. Seeing Bobby grow close to Kitty, she finds herself drawn to the cure."),
    ]),
    ("第3部 マグニートーの軍団", "Part 3: Magneto's army", [
        ("教会の集会",
         "古い教会で、治療薬について話し合うミュータントの集会が開かれている。そこへマグニートーとパイロが現れる。\n"
         "マグニートーは、治療薬はいずれ力ずくで使われ、ミュータントを消し去るための武器になると訴える。集まったミュータントたちは、マグニートーにつき従うことを決める。",
         "The church meeting",
         "In an old church, mutants have gathered to discuss the cure. Magneto and Pyro walk in.\n"
         "Magneto warns that the cure will be forced on them and used as a weapon to wipe mutants out. The mutants there decide to follow him."),
        ("カリストたち",
         "集会にいたミュータントの1人カリストは、とても速く動けるうえ、ほかのミュータントの居場所や力の強さを感じ取ることができる。\n"
         "マグニートーはカリストや、体から鋭いトゲを出すキッド・オメガ、手をたたいて衝撃波を起こすアークライトたちを仲間にする。カリストの力で、捕まっているミスティークの居場所を探させる。",
         "Callisto and the others",
         "One of the mutants at the meeting, Callisto, is super-fast and can sense where other mutants are and how strong they are.\n"
         "Magneto recruits her along with others, like Kid Omega, who grows sharp quills, and Arclight, who makes shockwaves by clapping. He uses Callisto's power to track down the captured Mystique."),
        ("移送車の襲撃",
         "囚人のミュータントを運ぶトラックの列を、マグニートーたちが襲い、ミスティークを助け出す。\n"
         "同じトラックに閉じこめられていた、止まらずに突き進む怪力の男ジャガーノートと、自分の分身をいくらでも作れるマルチプルマンも自由になり、仲間に加わる。",
         "The convoy attack",
         "Magneto's group attacks a mobile prison carrying mutant prisoners and frees Mystique.\n"
         "Also released are Juggernaut, a super-strong man who can't be stopped once he gets moving, and Multiple Man, who can make endless copies of himself. Both join up."),
        ("ミスティークの犠牲",
         "治療薬の入った弾がマグニートーに向けて撃たれる。ミスティークがマグニートーをかばって弾を受け、力を失ってふつうの人間の姿になる。\n"
         "マグニートーは、ミスティークはもう仲間ではないと言い、その場に置き去りにする。",
         "Mystique's sacrifice",
         "A cure dart is fired at Magneto. Mystique throws herself in front of it and loses her powers, turning into an ordinary human woman.\n"
         "Magneto says she is no longer one of them and leaves her there."),
        ("ハンクの辞任",
         "治療薬を撃ちこむ銃が、ハンクの知らないところで作られていた。治療薬は望む人だけのものではなく、武器にもなっていた。\n"
         "そのことを知ったハンクは、大統領のもとで長官の職を辞める。",
         "Hank resigns",
         "Guns that fire the cure were made without Hank's knowledge. The cure isn't just for those who want it; it has become a weapon.\n"
         "Learning this, Hank resigns his cabinet post."),
    ]),
    ("第4部 湖から戻ったジーン", "Part 4: Jean returns", [
        ("アルカリ湖",
         "ジーンの声に耐えられなくなったスコットは、1人で、ジーンが消えたアルカリ湖へ向かう。\n"
         "湖のほとりで、スコットはサングラスを外し、目から出る光線を湖に向けて放つ。すると水の中から、死んだはずのジーンが現れる。\n"
         "2人は抱き合ってキスをするが、そのさなかにジーンの顔つきが変わる。",
         "Alkali Lake",
         "Unable to bear Jean's voice any longer, Scott goes alone to Alkali Lake, where she disappeared.\n"
         "At the shore he takes off his glasses and fires his optic blast across the water. Then Jean, thought dead, rises out of the lake.\n"
         "They embrace and kiss, but in the middle of it her face changes."),
        ("残されたメガネ",
         "異変を感じたプロフェッサーXは、ローガンとストームを湖へ送る。\n"
         "2人が見つけたのは、宙に浮かぶ石と、地面に落ちていたスコットのメガネ、そして気を失って倒れているジーンだった。スコットの姿はどこにもない。",
         "The glasses left behind",
         "Sensing trouble, Professor X sends Logan and Storm to the lake.\n"
         "They find rocks floating in the air, Scott's glasses on the ground, and Jean lying unconscious. Scott is nowhere to be found."),
        ("フェニックス",
         "学園に運ばれたジーンを前に、プロフェッサーXはローガンに打ち明ける。ジーンの力はあまりに強く、ジーンがまだ子どものころ、自分が心の中に壁を作って、その力を抑えてきたのだと。\n"
         "抑えこまれた力は、本能のままに暴れる別の人格になり、「フェニックス」と呼ばれていた。湖でジーンが仲間を救ったとき、その壁が外れてしまったという。\n"
         "人の心に勝手に手を加えていたと知ったローガンは、強く反発する。",
         "The Phoenix",
         "With Jean back at the school, Professor X confesses to Logan: her power was so great that when she was a child, he built walls in her mind to hold it back.\n"
         "That buried power grew into a separate, purely instinctive personality called the Phoenix. When Jean sacrificed herself at the lake, the walls came down.\n"
         "Logan is disgusted that Xavier tampered with her mind."),
        ("ジーンの目覚め",
         "目を覚ましたジーンは、前とはちがう、おかしく荒々しいふるまいを見せる。スコットはどこかと聞かれても思い出せず、自分が殺してしまったのではないかとおびえる。\n"
         "ジーンは、誰かを傷つける前に自分を殺してほしいとローガンに頼む。ローガンが断り、プロフェッサーXに助けてもらおうと言うと、フェニックスが表に出てローガンを力で壁にたたきつける。\n"
         "ジーンは学園を飛び出し、子どものころの家へ向かう。",
         "Jean wakes up",
         "When Jean wakes, she acts strange and aggressive, unlike herself. Asked where Scott is, she can't remember, and fears she killed him.\n"
         "She begs Logan to kill her before she hurts anyone else. When he refuses and says Xavier can help her, the Phoenix takes over and slams him into a wall with her mind.\n"
         "Jean flees the school and heads for her childhood home."),
    ]),
    ("第5部 ジーンの実家", "Part 5: The Grey house", [
        ("同じときに着いた2組",
         "カリストから、強い力を持つミュータントが現れたと聞いたマグニートーは、ジーンが戻ったことを知る。\n"
         "プロフェッサーXとローガン、ストームがジーンの家に着いたとき、マグニートーの一団も同じときにやって来る。プロフェッサーXとマグニートーは、2人だけで家の中に入る。",
         "Both sides arrive",
         "Through Callisto, Magneto learns of a powerful mutant and realizes Jean has returned.\n"
         "Professor X, Logan and Storm reach the Grey house at the same moment as Magneto's group. Xavier and Magneto go inside alone."),
        ("家の中の2人",
         "家の中で、プロフェッサーXとマグニートーは、それぞれジーンに語りかけ、自分の側に引き入れようとする。ジーンの心は、2人の間でゆれる。",
         "Two men, one woman",
         "Inside, Professor X and Magneto each speak to Jean, trying to win her to their side. She is torn between them."),
        ("家の外の戦い",
         "家の外では、ローガンとストームがマグニートーの仲間たちとにらみ合い、やがて戦いになる。ストームは、すばやく動くカリストを相手に戦う。",
         "Fighting outside",
         "Outside, Logan and Storm face off against Magneto's followers until a fight breaks out. Storm takes on the lightning-fast Callisto."),
        ("プロフェッサーXの最期",
         "プロフェッサーXがジーンの心に入りこもうとすると、20年も閉じこめられてきたフェニックスが怒って表に出る。\n"
         "家がくずれはじめる。心の力どうしのぶつかり合いの末、プロフェッサーXの体は、フェニックスの力でちりになって消えてしまう。\n"
         "ジーンはマグニートーと共に去っていく。",
         "Xavier's end",
         "When Professor X tries to reach into Jean's mind, the Phoenix, furious after twenty years locked away, bursts out.\n"
         "The house starts to break apart. After a battle of minds, the Phoenix disintegrates Professor X into dust.\n"
         "Jean leaves with Magneto."),
        ("お別れの会",
         "学園で、プロフェッサーXの葬儀が開かれる。X-MENは、プロフェッサーX、スコット、ジーンを一度に失った。",
         "The funeral",
         "The school holds Professor X's funeral. The X-Men have lost Xavier, Scott and Jean all at once."),
    ]),
    ("第6部 それぞれの決断", "Part 6: Choices", [
        ("翼を広げたウォーレン",
         "ワージントン社の研究所で、大人になったウォーレン（エンジェル）は、父親の前で台に固定され、治療薬を打たれようとしている。\n"
         "しかし、ウォーレンは直前で体の固定を振りほどき、窓を破って飛び出す。大きな翼を広げて空へ逃げたウォーレンは、プロフェッサーXの学園をめざす。",
         "Warren spreads his wings",
         "At the Worthington lab, the adult Warren (Angel) is strapped to a table in front of his father, about to receive the cure.\n"
         "At the last moment he breaks free and crashes through the window. Spreading his huge wings, he flies off toward Professor X's school."),
        ("ローグの決断",
         "プロフェッサーXを失い、ボビーにふれられない苦しさも続くなか、ローグは治療薬を受けることを決めて学園を出ていく。\n"
         "治療薬を配る施設の前には、治療を望むミュータントたちの長い列ができている。",
         "Rogue's choice",
         "With Professor X gone and still unable to touch Bobby, Rogue decides to take the cure and leaves the school.\n"
         "Outside the clinics handing out the cure, long lines of mutants wait for their turn."),
        ("ミスティークの告げ口",
         "マグニートーに見捨てられたミスティークは、政府の捜査官に、森の中にあるマグニートーの隠れ家の場所を教える。",
         "Mystique talks",
         "Abandoned by Magneto, Mystique tells federal agents where his hideout in the woods is."),
        ("森の中の作戦会議",
         "森の隠れ家には、ジーンを加えたマグニートーの大きな軍団が集まっている。マグニートーは、治療薬のもとになっている少年ジミーを殺して、治療薬を作れなくするため、アルカトラズ島の研究所を襲うと決める。",
         "The plan in the woods",
         "Magneto's army, now with Jean, is camped in the forest. He decides to attack the Alcatraz lab and kill Jimmy, the boy the cure is made from, so no more can be produced."),
        ("空っぽの隠れ家",
         "政府の部隊が隠れ家に踏みこむ。熱の反応からたくさんの人がいると思われたが、そこにいたのはマルチプルマンとその分身たちだけだった。マグニートーの軍団は、すでにサンフランシスコへ向かっていた。",
         "An empty camp",
         "Government teams raid the camp. Heat sensors showed many people there, but they find only Multiple Man and his copies. Magneto's army is already on its way to San Francisco."),
    ]),
    ("第7部 アルカトラズの戦い", "Part 7: The battle of Alcatraz", [
        ("動く橋",
         "マグニートーはサンフランシスコのゴールデン・ゲート・ブリッジを力で引きはがし、宙を動かしてアルカトラズ島につなげる。橋は、軍団が島へ渡るための道になる。",
         "Moving the bridge",
         "Magneto tears the Golden Gate Bridge loose, moves it through the air and sets it down against Alcatraz. It becomes a road for his army to cross to the island."),
        ("プラスチックの銃",
         "島を守る兵士たちの銃は、治療薬の弾を撃つプラスチック製のもので、金属をあやつるマグニートーには動かせない。\n"
         "マグニートーが先に送りこんだミュータントたちは、次々に治療薬を撃ちこまれて力を失う。しかし、アークライトの衝撃波で兵士たちの銃がこわされ、マグニートーの軍団が兵士たちを押しまくる。",
         "Plastic guns",
         "The soldiers guarding the island carry plastic guns that fire cure darts, which Magneto can't control with magnetism.\n"
         "The first wave of mutants he sends in is hit with the cure one after another and loses their powers. But Arclight's shockwaves wreck the soldiers' weapons, and Magneto's army begins to overrun them."),
        ("X-MENの到着",
         "そこへ、ローガン、ストーム、ハンク、ボビー、キティ、コロッサスのX-MENが駆けつける。数ではマグニートーの軍団にまったくかなわない。\n"
         "マグニートーは、人間の味方をするX-MENを裏切り者と呼び、軍団に襲いかからせる。",
         "The X-Men arrive",
         "Logan, Storm, Hank, Bobby, Kitty and Colossus arrive. They are badly outnumbered.\n"
         "Magneto calls them traitors for siding with humans and sends his army at them."),
        ("キティとジャガーノート",
         "ジャガーノートは、ジミーを殺すため、研究所の壁をいくつも突き破って進む。キティは壁をすり抜けて先回りし、ジミーを見つけて連れ出す。\n"
         "追いかけてきたジャガーノートは、ジミーのそばで力を失い、勢いのまま壁に頭からぶつかって気を失う。",
         "Kitty and Juggernaut",
         "Juggernaut smashes through wall after wall of the lab to reach and kill Jimmy. Kitty phases through the walls ahead of him, finds Jimmy and gets him out.\n"
         "When Juggernaut catches up, he loses his power near Jimmy and charges headfirst into a wall, knocking himself out."),
        ("ボビーとパイロ",
         "ボビーは、炎をあやつるパイロと1対1で戦う。ボビーは初めて全身を氷に変え、パイロの両手を凍らせて炎を止め、頭突きで打ち倒す。",
         "Bobby and Pyro",
         "Bobby fights Pyro, who controls fire, one on one. For the first time, Bobby turns his whole body to ice. He freezes Pyro's hands to stop the flames and knocks him out with a headbutt."),
        ("ストームとカリスト",
         "ストームは、すばやく動くカリストと再び戦い、カリストを雷で倒す。カリストは命を落とす。",
         "Storm and Callisto",
         "Storm faces the lightning-fast Callisto again and strikes her down with lightning. Callisto is killed."),
        ("エンジェルの救出",
         "マグニートーの仲間が、研究所の建物からワージントン2世を突き落とす。そこへ空から息子のウォーレンが飛んできて、落ちていく父親を受け止める。",
         "Angel to the rescue",
         "Magneto's followers throw Worthington II off a lab building. His son Warren swoops in from the sky and catches him as he falls."),
        ("マグニートーと治療薬",
         "ローガンはコロッサスに自分を投げさせ、マグニートーに飛びかかって気を引く。そのすきにハンクが、治療薬の注射をマグニートーに打ちこむ。\n"
         "マグニートーは力を失い、ふつうの人間になってしまう。",
         "Magneto is cured",
         "Logan has Colossus throw him at Magneto to keep him busy. Meanwhile Hank jabs Magneto with a cure syringe.\n"
         "Magneto's powers are gone. He is an ordinary man."),
    ]),
    ("第8部 フェニックス", "Part 8: The Phoenix", [
        ("撃たれたジーン",
         "ローガンがジーンに近づき、落ち着かせかけたそのとき、あとから着いた軍の部隊がジーンに向けて撃ちはじめる。\n"
         "怒ったフェニックスは、兵士たちを力でちりにして消し去る。そして研究所の建物や島全体をこわしはじめ、近くにいる人も物も次々に消えていく。マグニートーの仲間の1人も、このとき消される。",
         "Jean is shot at",
         "Just as Logan reaches Jean and begins to calm her, army reinforcements arrive and open fire on her.\n"
         "Enraged, the Phoenix disintegrates the soldiers. Then she starts tearing apart the lab and the whole island, and everyone and everything near her turns to dust, including one of Magneto's followers."),
        ("近づけるのはローガンだけ",
         "ローガンは、骨格がアダマンチウムという金属でできていて、けががすぐに治る自分だけが、フェニックスに近づけると気づく。\n"
         "ストームたちがほかの人たちを島から逃がすあいだ、ローガンは体をこわされては治りながら、一歩ずつジーンに近づいていく。",
         "Only Logan can reach her",
         "Logan realizes that with his adamantium skeleton and healing power, he alone can get near the Phoenix.\n"
         "While Storm and the others get people off the island, Logan pushes toward Jean step by step, his body torn apart and healing over and over."),
        ("最後の決断",
         "フェニックスは、ほかの人たちのために死ぬ気かとローガンにたずねる。ローガンは、ほかの人のためではなく、ジーンのためなら死ねると答える。\n"
         "その一瞬、ジーンは元の自分に戻り、自分を救ってほしいとローガンに頼む。ローガンは愛していると告げ、涙ながらに爪でジーンを刺す。ジーンはローガンの腕の中で息を引き取り、フェニックスの暴走は止まる。",
         "The hardest choice",
         "The Phoenix asks Logan whether he would die for the others. He answers that he wouldn't die for them, but he would for her.\n"
         "For a moment Jean is herself again and begs him to save her. Logan tells her he loves her and, in tears, stabs her with his claws. She dies in his arms, and the Phoenix's rampage is over."),
    ]),
    ("第9部 それぞれのその後", "Part 9: Afterward", [
        ("新しい学園",
         "しばらくのち、ミュータントの権利が認められる。学園は閉じられることなく、ストームが校長となって続けられる。\n"
         "大統領は、ハンクを国連の大使に任命する。",
         "A new chapter",
         "Some time later, mutant rights are finally won. The school stays open, with Storm as headmistress.\n"
         "The President appoints Hank as ambassador to the United Nations."),
        ("ローグとボビー",
         "治療薬を受けたローグが学園に戻り、治療薬を受けたことをボビーに告げる。力を失ったローグは、もう人にふれても相手を傷つけない。",
         "Rogue and Bobby",
         "Rogue, having taken the cure, returns to the school and tells Bobby what she did. Without her powers, she can now touch people without hurting them."),
        ("チェス盤",
         "力を失ったマグニートーは、1人でチェス盤の前に座っている。金属のチェスの駒に手をかざすと、駒がかすかに揺れる。力は完全には消えていないのかもしれない。",
         "The chessboard",
         "Magneto, powerless, sits alone at a chessboard. When he holds his hand toward a metal chess piece, it wobbles slightly. His powers may not be completely gone."),
        ("エンドクレジットの後",
         "医師のモイラ・マクタガートが、意識のない患者のようすを見ている。脳の働きを失った人の体に、死にかけた人の心を移すという話は、学園の授業でも出ていた。\n"
         "その患者が、プロフェッサーXの声でモイラにあいさつをする。モイラは驚いて、チャールズの名を呼ぶ。",
         "After the credits",
         "Dr. Moira MacTaggert checks on a patient in a coma. Moving a dying man's mind into the body of someone with no higher brain function had come up earlier in a class at the school.\n"
         "The patient greets her in Professor X's voice. Startled, she says, \"Charles?\""),
    ]),
    ("まとめ（最後までのネタバレ）", "Summary (spoilers through the end)", [
        ("治療薬の行方",
         "①ワージントン社が、少年ジミーの体から作った治療薬を発表する（第2部）\n"
         "②治療薬の弾がマグニートーをかばったミスティークに当たり、ミスティークは力を失う。治療薬が武器にされていると知ったハンクは長官を辞める（第3部）\n"
         "③ウォーレンは打たれる直前に逃げ、ローグは自分で受けることを選ぶ（第6部）\n"
         "④マグニートーはジミーを殺すためアルカトラズ島を襲うが、ハンクに治療薬を打たれて力を失う（第7部）\n"
         "⑤しかし最後に、マグニートーの力がわずかに戻りかけていることが分かる（第9部）",
         "What happened with the cure",
         "1) Worthington Labs announces a cure made from the boy Jimmy (Part 2).\n"
         "2) A cure dart meant for Magneto hits Mystique, who loses her powers. Learning the cure has been turned into a weapon, Hank resigns (Part 3).\n"
         "3) Warren escapes just before receiving it; Rogue chooses to take it (Part 6).\n"
         "4) Magneto attacks Alcatraz to kill Jimmy, but Hank injects him with the cure and his powers are gone (Part 7).\n"
         "5) In the end, Magneto's power seems to be faintly returning (Part 9)."),
        ("ジーンとフェニックス",
         "①子どものころ、プロフェッサーXがジーンの心の中に壁を作り、強すぎる力を抑えた（第1部・第4部）\n"
         "②アルカリ湖でよみがえったジーンの前で、スコットが姿を消す（第4部）\n"
         "③学園で目覚めたジーンは、自分を殺してとローガンに頼んだあと、フェニックスとなって逃げる（第4部）\n"
         "④実家でプロフェッサーXを消し、マグニートーの側につく（第5部）\n"
         "⑤アルカトラズ島で撃たれて暴走し、ローガンに命を絶たれる（第8部）",
         "Jean and the Phoenix",
         "1) When Jean was a child, Professor X walled off her overwhelming power inside her mind (Parts 1 and 4).\n"
         "2) Jean rises from Alkali Lake, and Scott disappears (Part 4).\n"
         "3) Waking at the school, she begs Logan to kill her, then the Phoenix takes over and she flees (Part 4).\n"
         "4) At her old home she destroys Professor X and joins Magneto (Part 5).\n"
         "5) Shot at on Alcatraz, she runs wild, and Logan ends her life (Part 8)."),
        ("死んだ人",
         "・スコット（第4部）：アルカリ湖で、よみがえったジーンとキスをしたあと姿を消す。のちに、ジーンに殺されていたことが分かる。\n"
         "・プロフェッサーX（第5部）：ジーンの心を抑えようとして、怒ったフェニックスの力で体をちりにされる。エンドクレジットの後、心は別の人の体で生きていることが分かる。\n"
         "・カリスト（第7部）：アルカトラズ島の戦いで、ストームの雷に打たれる。\n"
         "・兵士たちとマグニートーの仲間の1人（第8部）：ジーンを撃ったことで暴走したフェニックスの力で、ちりにされる。\n"
         "・ジーン（第8部）：フェニックスの暴走を止めるため、ローガンが、本人の願いにこたえて爪で刺す。",
         "Who died",
         "- Scott (Part 4): he vanishes after kissing the resurrected Jean at Alkali Lake. It later turns out she killed him.\n"
         "- Professor X (Part 5): trying to hold back Jean's mind, he is disintegrated by the enraged Phoenix. After the credits, his mind turns out to live on in another body.\n"
         "- Callisto (Part 7): struck by Storm's lightning in the battle of Alcatraz.\n"
         "- The soldiers and one of Magneto's followers (Part 8): disintegrated by the Phoenix after the soldiers fire on Jean.\n"
         "- Jean (Part 8): to stop the Phoenix, Logan stabs her with his claws, answering her plea."),
    ]),
]
