# 『ファルコン＆ウィンター・ソルジャー』シーンごとの詳しいあらすじ
# 2026-11-08 英語版ウィキペディアの各話のあらすじ（Plot）と解説記事を照らし合わせ、順番と事実を直した。
# 運営者の希望: 第1話から始め、場面ごとに起きた事実だけを書く。見出しはつながった場面でまとめる。
# 形: ("見出し", "本文", "Heading", "Text")。本文の \n は段落の区切り。文章はすべて自分の言葉で書いた。
# レマーの両親の場面は、運営者が観て確かめた位置（第5話のルイジアナの場面の次）に置いている。
SCENE_NUMBERS = True  # 場面に「話-番号」を付ける（観ながら照らし合わせるため）
SCENES = [('第1話 新しい世界',
  'Episode 1: New World Order',
  [('空の救出作戦',
    'チュニジアの上空。アメリカ空軍の飛行機が、バトロックの率いる犯罪集団LAFに乗っ取られ、空軍のヴァサント大尉が連れ去られようとしている。飛行機が隣のリビアの空に入ると国どうしの大問題になるため、その前に助け出さなければならない。サムは軍にたのまれ、大尉を助けに向かう。\n'
    '地上では、空軍のトレス中尉が無線でサムを手伝う。サムは翼で飛び、乗っ取られた飛行機を追いかける。\n'
    '飛行機を守るように、敵のヘリコプター2機が現れてサムを撃ってくる。サムは空中で弾をよけながら、ヘリコプターと戦う。\n'
    'サムは、ヴァサント大尉を救い出す。バトロックは飛行機から飛び出し、パラシュートで逃げてしまう。',
    'Rescue in the sky',
    'Over Tunisia, a U.S. Air Force plane has been hijacked by the LAF, a group led by Batroc, who are taking Captain Vassant. Sam must rescue him before the plane crosses into Libyan airspace and '
    'causes an international incident.\n'
    'On the ground, Air Force Lt. Torres supports Sam by radio as Sam flies after the plane.\n'
    'Two enemy helicopters appear and open fire on Sam. He dodges and fights them in mid-air.\n'
    'Sam rescues Captain Vassant. Batroc jumps out and escapes by parachute.'),
   ('トレスの報告と、盾を博物館へ',
    '作戦のあと、トレスはサムに、ある集団の話をする。インターネットで仲間を集め、「指パッチンのあいだのほうが世界はよかった」と考えている集団、フラッグ・スマッシャーズだ。\n'
    'ワシントンの博物館で式典が開かれる。サムはスティーブから託された盾を、スティーブを紹介する展示に飾ってもらうため、政府に預ける。\n'
    '式典のあと、友人のローディ（ウォーマシン）が「本当にいいのか」とたずねる。サムは「盾は、まだスティーブのもののような気がする」と答える。',
    "Torres's report, and the shield goes to a museum",
    'After the mission, Torres tells Sam about a group that organizes online and believes the world was better during the Blip: the Flag Smashers.\n'
    "At a ceremony in Washington, Sam hands Steve's shield to the government to be displayed in a museum exhibit about Steve.\n"
    "Afterward, his friend Rhodey (War Machine) asks if he's sure. Sam says it feels like the shield still belongs to Steve."),
   ('バッキーの悪夢とカウンセリング',
    'バッキーは、ウィンター・ソルジャーだったころの夢を見て飛び起きる。ホテルの部屋で人を殺したとき、その場面をたまたま見てしまった若い男性まで撃ち殺した記憶だ。\n'
    'バッキーは、政府に罪を許される条件として、レイナー先生のカウンセリングに通っている。先生は、償いに3つのルールを決めている。①法律をやぶらない ②誰も傷つけない ③相手に「私はもうウィンター・ソルジャーではない。これは償いだ」と伝える。\n'
    '先生は、悪夢のことや、友だちがいないことを気にかける。しかしバッキーはあまり話そうとしない。',
    "Bucky's nightmare and therapy",
    'Bucky wakes from a nightmare of his Winter Soldier days: in a hotel room he killed a target, then shot a young man who happened to see it.\n'
    'As a condition of his pardon, Bucky sees a therapist, Dr. Raynor, who has set three rules for his amends: 1) break no laws, 2) hurt no one, 3) tell the person he is no longer the Winter Soldier '
    'and is making amends.\n'
    "She asks about his nightmares and his lack of friends, but he doesn't open up much."),
   ('償い① アトウッド議員',
    'バッキーのノートには、洗脳されていたころに関わった人たちの名前が書いてある。その一人、アトウッド上院議員の車に、バッキーは忍びこむ。議員は、ライバルの議員を消すよう電話で命じていた。バッキーはその会話を録音していた。\n議員は警察につかまり、けが人は出なかった。バッキーはノートのアトウッド議員の名前に線を引いて消す。',
    'Amends #1: Senator Atwood',
    "Bucky's notebook lists people tied to his brainwashed past. One is Senator Atwood. Bucky slips into her car as she orders a rival congressman silenced, and he has recorded the conversation.\n"
    'She is arrested and no one is hurt. Bucky crosses her name off his list.'),
   ('ヨリさんとリア',
    'バッキーは毎週、近所のおじいさんヨリ・ナカジマさんとレストランで昼ごはんを食べる。ヨリさんは、亡くなった息子のRJのことを話す。RJはホテルで殺され、犯人は分からないままだ。\n'
    '実は、悪夢に出てきた若い男性がRJだった。RJは、ウィンター・ソルジャーが人を殺す場面を見てしまい、バッキーに殺されたのだ。バッキーは本当のことを言えずにいる。\n'
    'ヨリさんにすすめられ、バッキーは店員のリアとデートをする。リアもRJの死について話し、バッキーの表情がくもる。バッキーは、サムからのメッセージにも返事をしていない。',
    'Yori and Leah',
    'Every week Bucky has lunch with an elderly neighbor, Yori Nakajima. Yori talks about his son RJ, killed in a hotel; the killer was never found.\n'
    "The young man in Bucky's nightmare was RJ: he witnessed a Winter Soldier assassination and Bucky killed him. Bucky can't bring himself to tell Yori.\n"
    "Encouraged by Yori, Bucky goes on a date with the waitress Leah. She also talks about RJ's death, and Bucky's face clouds. He has been ignoring Sam's texts, too."),
   ('サムの家族と船',
    'サムは故郷ルイジアナ州デラクロワに帰る。姉サラは2人の息子を育てながら、両親から受け継いだ漁の商売を続けるのに苦労し、船を売ろうとしていた。サムは「船は家族の思い出だ」と反対する。\nサムは有名なヒーローであることを生かそうと、サラと銀行にお金を借りに行く。銀行の人はサムに会えて喜ぶが、お金は貸してくれない。商売がもうかっていないことと、サムが消えていた5年間、収入がなかったからだ。',
    "Sam's family and the boat",
    "Sam goes home to Delacroix, Louisiana. His sister Sarah, raising two sons, is struggling to keep the family fishing business going and plans to sell the boat. Sam objects: it's their family's "
    'history.\n'
    'Hoping his fame will help, Sam goes with Sarah to apply for a loan. The banker is thrilled to meet him but turns them down, because the business makes little money and Sam had no income for the '
    'five years he was gone.'),
   ('スイスのフラッグ・スマッシャーズ',
    'トレス中尉は、スイスでフラッグ・スマッシャーズを調べる。覆面のメンバーが銀行をおそう場面を見たトレスは、メンバーの一人を問いつめるが、ふつうの人間とは思えない怪力で投げ飛ばされ、気を失う。',
    'The Flag Smashers in Switzerland',
    'In Switzerland, Torres investigates the Flag Smashers and sees masked members rob a bank. He confronts one of them, but is thrown with inhuman strength and knocked unconscious.'),
   ('新しいキャプテン・アメリカ',
    'トレスは、調べたことをサムに知らせる。\nサムは姉サラと一緒にテレビのニュースを見ている。政府が「新しいキャプテン・アメリカ」を発表する。サムが預けた盾を持って現れたのは、ジョン・ウォーカーという軍人だった。サムはぼう然とする。',
    'A new Captain America',
    'Torres reports what he found to Sam.\n'
    'Sam is watching the news with his sister Sarah. The government unveils a new Captain America: a soldier named John Walker, holding the shield Sam gave away. Sam is stunned.')]),
 ('第2話 星条旗の男',
  'Episode 2: The Star-Spangled Man',
  [('ジョン・ウォーカー',
    '母校の高校の控え室で、ウォーカーは人前に出る準備をしている。妻のオリビアが来て、緊張する夫をはげます。\nウォーカーは新しいキャプテン・アメリカとして紹介され、テレビの番組に出る。「スティーブは兄弟のような存在だ」と話し、スティーブにふさわしい存在になりたいと語る。そばにはいつも親友のレマーがいる。',
    'John Walker',
    'In a locker room at his old high school, Walker gets ready for a public appearance. His wife Olivia comes in to encourage him.\n'
    "Introduced as the new Captain America, Walker appears on TV, calls Steve a brother, and says he wants to live up to Steve's legacy. His best friend Lemar is at his side."),
   ('バッキーの怒り',
    'がらんとした自分の部屋で、バッキーはウォーカーのテレビを見て、怒りをつのらせる。\nバッキーはサムに会いに来て、「なぜ盾を政府に渡した」と怒る。\n2人は言い合いをしながらも、フラッグ・スマッシャーズを一緒に追うことにする。',
    'Bucky is angry',
    'In his bare apartment, Bucky watches Walker on TV and grows angry.\nBucky confronts Sam: why did he hand the shield to the government?\nStill arguing, they team up to chase the Flag Smashers.'),
   ('ミュンヘンでの戦い',
    'サムは何も説明しないまま、飛行機から飛び降りる。バッキーはパラシュートなしで後を追って飛び降り、地面にうまく着地できない。サムのドローン「レッドウィング」の映像を頼りに、バッキーはサムを見つける。\n'
    'ドイツのミュンヘンで、フラッグ・スマッシャーズが薬などの物資を積んだトラックを走らせている。サムは、つかまっている人質のように見える若い女性を見つけるが、実はその女性こそがリーダーのカーリだった。\n'
    'サムとバッキーはトラックの上で戦う。相手は全員が超人の怪力を持っていて、2人は押されてしまう。\n'
    'そこへウォーカーとレマーが加わるが、それでもかなわず、フラッグ・スマッシャーズは逃げてしまう。サムのドローン「レッドウィング」もこわされる。\n'
    '戦いのあと、ウォーカーとレマーは「一緒にGRCを手伝おう」と誘うが、サムとバッキーは断る。',
    'The fight in Munich',
    "Without explaining his plan, Sam jumps from a plane. Bucky follows without a parachute and lands badly. Using footage from Sam's drone Redwing, Bucky finds him.\n"
    'In Munich, the Flag Smashers are smuggling medicine by truck. Sam spots what looks like a young female hostage, who turns out to be their leader, Karli.\n'
    'Sam and Bucky fight on top of the trucks. Every member has super strength, and the two are overpowered.\n'
    "Walker and Lemar join in, but the Flag Smashers still escape. Sam's drone Redwing is destroyed.\n"
    'Afterward, Walker and Lemar invite them to help the GRC, but Sam and Bucky refuse.'),
   ('カーリたちの事情',
    'カーリたちは、盗んだ物資を難民キャンプに届けている。キャンプの人々は、カーリたちを救い主のように思っている。\nカーリのスマートフォンには、「パワー・ブローカー」という相手から脅しのメッセージが届いている。',
    "Karli's side",
    'Karli and her group deliver the stolen supplies to refugee camps, where people see them as saviors.\nKarli receives a threatening message from someone called the Power Broker.'),
   ('イザイア・ブラッドリー',
    'バッキーはサムを、ボルティモアに住む老人イザイアの家に連れていく。イザイアは超人の兵士で、1951年の朝鮮戦争のころ、ウィンター・ソルジャーだったバッキーと戦ったことがあった。\nサムは、黒人の超人兵士がいたことを初めて知り、衝撃を受ける。しかしイザイアは、30年も閉じこめられて実験を受け続けたことを恨んでおり、新しい血清のことで力を貸すのを断って、2人を追い返す。',
    'Isaiah Bradley',
    'Bucky takes Sam to see Isaiah, an old man in Baltimore. Isaiah is a super soldier who fought Bucky, then the Winter Soldier, in 1951 during the Korean War.\n'
    'Sam is shocked to learn a Black super soldier ever existed. But Isaiah, bitter after 30 years of imprisonment and experiments, refuses to help with the new serum and sends them away.'),
   ('警察とカウンセリング',
    '家の前で、サムは「黒人の超人兵士のことを、なぜ黙っていた」とバッキーを責め、言い合いになる。そこへ警察官がやって来て、黒人のサムにだけ身分証を見せろと言う。サムだと分かると態度を変えるが、サムは悔しさをかみしめる。\n'
    'さらにバッキーは、カウンセリングを休んだせいで逮捕されてしまう。ウォーカーとレマーの口ききで出してもらえる。\n'
    'その代わりに、サムとバッキーは一緒にレイナー先生のカウンセリングを受ける。向かい合って話すうちに、バッキーの本音が出てくる。スティーブが盾を託したサムが盾を手放したことで、「スティーブはサムについてまちがっていたのか。それなら自分についても、まちがっていたのではないか」と不安になっていたのだ。',
    'The police and therapy',
    "Outside, Sam confronts Bucky for keeping a Black super soldier secret, and they argue. Police arrive and demand ID from Sam only, because he's Black. They change their tune when they recognize "
    'him, but Sam is left fuming.\n'
    'Then Bucky is arrested for skipping therapy. Walker and Lemar get him released.\n'
    "In return, Sam and Bucky do a session together with Dr. Raynor. Bucky's real fear comes out: if Steve was wrong about Sam, who gave up the shield, maybe Steve was wrong about Bucky too."),
   ('ウォーカーの誘いと、ジモ',
    'ウォーカーはもう一度2人を誘うが、2人はまた断る。ウォーカーは「じゃまをするな」とくぎをさす。\n'
    'いっぽうスロバキアでは、パワー・ブローカーの手下たちがフラッグ・スマッシャーズを追ってくる。仲間の一人が残って手下を食い止めるあいだに、カーリたちは逃げる。\n'
    '血清がどこから来たのかを知るため、バッキーは「血清と超人にくわしい男に聞こう」と言い出す。それは、ベルリンの刑務所にいるジモだった。',
    "Walker's offer, and Zemo",
    'Walker asks them again; they refuse again, and he warns them to stay out of his way.\n'
    "Meanwhile in Slovakia, the Power Broker's men close in on the Flag Smashers. One member stays behind to hold them off while Karli and the others escape.\n"
    'To find where the serum came from, Bucky suggests asking a man who knows super soldiers: Zemo, in prison in Berlin.')]),
 ('第3話 パワー・ブローカー',
  'Episode 3: Power Broker',
  [('ジモの脱獄',
    'サムとバッキーは、ドイツ・ベルリンの刑務所にいるジモに会い、フラッグ・スマッシャーズのことを聞く。\nジモが協力すると言うと、バッキーはサムに内緒で刑務所に騒ぎを起こさせ、そのすきにジモを逃がす。サムは「信用できない」と怒るが、しかたなく3人で動くことになる。',
    'Zemo breaks out',
    'Sam and Bucky visit Zemo in a Berlin prison to ask about the Flag Smashers.\n'
    'When Zemo agrees to help, Bucky secretly arranges a prison riot so Zemo can escape. Sam is furious but reluctantly goes along.'),
   ('ジモの飛行機',
    'ジモは大金持ちで、自分の飛行機と執事のオエズニクがいる。\n飛行機の中で、ジモはバッキーのノートを手に取り、ヨリさんの名前が気になると言う。\nジモは「超人の兵士がいるかぎり世界は危ない。血清を打った人間はいなくなるべきだ」という考えを話す。',
    "Zemo's jet",
    'Zemo is rich, with a private jet and a butler, Oeznik.\n'
    "On the jet, Zemo picks up Bucky's notebook and notes that the name Nakajima seems important.\n"
    'Zemo explains that the world is in danger as long as super soldiers exist.'),
   ('マドリプールとセルビー',
    '3人は、パワー・ブローカーが支配する犯罪者の島マドリプールへ。ジモはバッキーにウィンター・ソルジャーのふりをさせ、サムは街に出入りする悪党の金持ちになりすます。\n'
    '3人は、セルビーという女の大物に会う。ジモは、ウィンター・ソルジャーを使ってセルビーの気を引き、血清の情報を聞き出す。血清を作り直したのは、パワー・ブローカーに雇われたヒドラの科学者、ネーゲル博士だという。\n'
    'ところが、サムの姉サラから電話がかかってきたことで、サムの正体がばれてしまう。撃ち合いになり、セルビーは撃たれて死ぬ。\n'
    '3人に賞金がかけられ、街じゅうの賞金かせぎから追われる。',
    'Madripoor and Selby',
    'They fly to Madripoor, a criminal haven run by the Power Broker. Zemo has Bucky act as the Winter Soldier, and Sam poses as a gangster who frequents the city.\n'
    'They meet Selby, a powerful criminal. Using the Winter Soldier to get her attention, Zemo learns that the serum was recreated by Dr. Nagel, a Hydra scientist hired by the Power Broker.\n'
    "A call from Sam's sister Sarah blows his cover. In the shootout that follows, Selby is killed.\n"
    'With a bounty on their heads, every bounty hunter in the city comes after them.'),
   ('シャロンとの再会',
    '3人を助けたのは、シャロン・カーターだった。シャロンは『シビル・ウォー』のあと追われる身となり、マドリプールで暮らしていた。\nシャロンは街での人脈を使って、ネーゲル博士の研究所を見つけ、3人を案内する。',
    'Reunion with Sharon',
    "Sharon Carter rescues them. A fugitive since the events of Civil War, she has been living in Madripoor.\nUsing her connections, she finds Dr. Nagel's lab and takes them there."),
   ('ネーゲル博士',
    'ネーゲル博士は、昔ヒドラで血清の研究をしていた科学者。ヒドラが滅びたあとはアメリカのCIAに雇われ、昔血清を打たれたアメリカ人の血をもとに研究を続けていた。\n'
    '博士は、血清を20本作り直したが、20本ともカーリに盗まれた、と話す。\n'
    '話を聞き終えたとたん、ジモは博士を撃ち殺す。血清を作れる人間を生かしておけば、また超人が生まれるからだ。\n'
    'そこへ賞金かせぎたちが襲ってきて、研究所は壊される。3人は逃げ出す。シャロンはマドリプールに残ると言い、サムは「アメリカに帰れるよう、罪を許してもらえるようかけ合う」と約束する。',
    'Dr. Nagel',
    'Dr. Nagel once worked on the serum for Hydra. After Hydra fell, the CIA hired him to continue the work using blood from an American given the serum long ago.\n'
    'He says he recreated 20 doses, and Karli stole all of them.\n'
    'The moment he finishes, Zemo shoots him dead: anyone who can make the serum will create more super soldiers.\n'
    'Bounty hunters attack and the lab is destroyed. The three escape. Sharon chooses to stay in Madripoor, and Sam promises to get her a pardon so she can come home.'),
   ('ウォーカーの追跡と、カーリの倉庫爆破',
    'ウォーカーとレマーはベルリンに着き、ジモの脱獄にサムとバッキーが手を貸したと気づく。\nいっぽうカーリたちは、リトアニアにあるGRCの物資の倉庫をおそい、物資をうばう。カーリは「思い知らせるため」に、中に人がいるまま倉庫を爆破する。',
    "Walker's pursuit, and Karli's bombing",
    'Walker and Lemar arrive in Berlin and figure out that Sam and Bucky helped Zemo escape.\n'
    "Meanwhile, Karli's group raids a GRC supply depot in Lithuania. To send a message, Karli blows up the building with people still inside."),
   ('ラトビアとワカンダの戦士',
    '3人は、カーリを探してラトビアへ向かう。\nバッキーは、通りにワカンダの追跡装置があることに気づき、2人と別れて、自分たちをつけている相手に会いに行く。待っていたのはワカンダの戦士アヨだった。アヨは、ジモを引き渡せと言う。',
    'Latvia and a Wakandan warrior',
    'The three head to Latvia to look for Karli.\n'
    'Bucky spots Wakandan tracking devices in the street, leaves the others, and confronts whoever is following them: Ayo, a Wakandan warrior, who demands he hand over Zemo.')]),
 ('第4話 世界が見ている',
  'Episode 4: The Whole World Is Watching',
  [('ワカンダの思い出と8時間の約束',
    '6年前のワカンダ。アヨは、バッキーを殺し屋に変えてしまう「合図の言葉」を読み上げ、シュリが洗脳をといたかどうかを確かめる。バッキーは何も起きず、涙を流す。洗脳から完全に自由になった瞬間だった。\n'
    '現在。アヨは、ワカンダの先の王ティ・チャカを殺したジモを引き渡すよう求める。バッキーは「8時間だけ待ってほしい」とたのみ、アヨは受け入れる。\n'
    'サムたちは、カーリたちがGRCの倉庫を爆破し、3人が死んだことを知る。',
    'Wakanda, and eight hours',
    "Six years earlier in Wakanda, Ayo reads the trigger words to test whether Shuri's deprogramming worked. Nothing happens, and Bucky weeps. He is finally free.\n"
    "In the present, Ayo demands Zemo, who killed Wakanda's King T'Chaka. Bucky asks for eight hours, and she agrees.\n"
    "Sam and the others learn that Karli's group bombed a GRC depot, killing three people."),
   ('ドンニャおばさんの葬式',
    '3人は、ラトビアの難民キャンプを調べる。そこでは、フラッグ・スマッシャーズの味方の人々が、住む場所を失った人たちを住まわせ、勉強を教えている。\n'
    'ジモは子どもたちにお菓子（トルコのお菓子ロクム）を配りながら、ある女の子から、ドンニャという女性の葬式がどこであるかを聞き出す。\n'
    'ドンニャは、身よりのない子どもたちを育ててきた女性で、カーリの育ての母だった。キャンプで亡くなっていた。カーリは悲しみと怒りをつのらせる。',
    "Donya's funeral",
    'The three look into a refugee camp in Latvia, where Flag Smasher supporters house and teach people displaced by the Blip.\n'
    "Handing out Turkish delight to the children, Zemo gets a girl to tell him where Donya Madani's memorial will be.\n"
    "Donya raised children with nowhere else to go; she was Karli's adoptive mother. She died in the camp. Karli's grief turns to anger."),
   ('サムとカーリ',
    'そこへウォーカーとレマーが現れる。サムは「まず自分に話させてくれ」とたのみ、ひとりでカーリと話す。\nカーリは「住む場所をうばわれた人たちを救いたいだけだ」と話す。サムはその気持ちを理解しつつ、「人を傷つけるやり方はまちがっている」と説得しようとする。\nそこへ待ちきれなくなったウォーカーが乱入し、話し合いは台なしになる。カーリは「サムもあちら側の人間だ」と思いこみ、戦いになる。',
    'Sam and Karli',
    'Walker and Lemar show up. Sam convinces them to let him talk to Karli first, alone.\n'
    'Karli says she only wants to save people who lost their homes. Sam understands but argues that hurting people is wrong.\n'
    'An impatient Walker barges in and ruins it. Karli decides Sam is on the other side, and a fight breaks out.'),
   ('血清を壊す',
    '戦いの中で、ジモはカーリを銃で撃つ。カーリは血清のおかげで死なないが、持っていた血清を落としてしまう。\nジモは血清を次々と壊していく。そこへウォーカーが来てジモを倒す。ジモが壊しそこねた最後の1本を、ウォーカーは拾ってこっそりポケットに入れる。\nカーリは逃げる。',
    'Destroying the serum',
    'In the fight, Zemo shoots Karli. The serum keeps her alive, but she drops her vials.\n'
    'Zemo smashes them one after another until Walker takes him down. Walker picks up the one vial Zemo missed and quietly pockets it.\n'
    'Karli escapes.'),
   ('ドーラ・ミラージュとウォーカー',
    '約束の8時間がすぎ、アヨたちドーラ・ミラージュがジモを取りに来る。ウォーカーは「ジモは渡さない」と言い張り、戦いになる。\n'
    'ウォーカーとレマーは、アヨたちにまったく歯が立たない。サムとバッキーは、ドーラ・ミラージュがウォーカーたちを殺してしまわないよう止めに入る。みんなが戦っているすきに、ジモはそっと姿を消す。\n'
    '大勢の前で負けて恥をかいたウォーカーは、あとでレマーと血清の話をする。レマーは「打つ」と答え、ウォーカーなら正しく使えるだろうと言う。',
    'The Dora Milaje and Walker',
    'When the eight hours are up, Ayo and the Dora Milaje come for Zemo. Walker refuses to hand him over, and they fight.\n'
    "Walker and Lemar are utterly outmatched. Sam and Bucky step in so the Dora Milaje don't kill them. While everyone is fighting, Zemo quietly slips away.\n"
    "Humiliated, Walker later talks with Lemar about the serum. Lemar says he'd take it, and that Walker would make the right call."),
   ('カーリのわな',
    'カーリは、サムたちを分断する計画を立てる。サムの姉サラに電話をかけ、サラと子どもたちの身をそれとなく脅しながら、サムとバッキーを待ち合わせの場所に呼び出す。\nいっぽうウォーカーとレマーは、ほかのフラッグ・スマッシャーズを襲う。サムとバッキーは急いで駆けつけ、戦いになる。その中でサムは、ウォーカーが血清を打ったことに気づく。',
    "Karli's trap",
    "Karli plans to divide them. She calls Sam's sister Sarah and, with a veiled threat to her and her sons, lures Sam and Bucky to a meeting.\n"
    'Meanwhile Walker and Lemar attack other Flag Smashers. Sam and Bucky rush to find them, and another fight breaks out, in which Sam realizes Walker has taken the serum.'),
   ('レマーの死',
    'カーリもサムたちを追ってきて戦いに加わる。混乱の中で、カーリは向かってきたレマーを超人の力で突き飛ばす。レマーは石の柱にたたきつけられ、そのまま死んでしまう。カーリに殺すつもりはなかった。',
    "Lemar's death",
    'Karli follows Sam and Bucky and joins the fight. In the chaos, she knocks Lemar away with her super strength; he slams into a stone pillar and dies. She never meant to kill him.'),
   ('広場でのニコの死',
    '親友を失って怒りにのみこまれたウォーカーは、レマーを助けに行こうとした自分を押さえつけていたフラッグ・スマッシャーズの一人、ニコを追いかける。ニコは「レマーを殺したのはぼくじゃない！」と叫ぶ。\n'
    'それでもウォーカーは、人が大勢いる広場で、ニコを盾で何度もなぐりつけて殺してしまう。サムとバッキー、カーリも、ぼう然と見ているしかなかった。\n'
    '人々はスマートフォンで撮影し、血のついた盾を持つキャプテン・アメリカの姿は、あっという間に世界中に広まる。',
    "Nico's death in the square",
    "Consumed by rage, Walker chases Nico, the Flag Smasher who held him back from saving Lemar. Nico cries that he didn't kill Lemar.\n"
    'Walker beats him to death with the shield anyway, in a crowded square. Sam, Bucky and Karli can only watch in horror.\n'
    'People film it, and images of Captain America holding a bloody shield spread worldwide in moments.')]),
 ('第5話 真実',
  'Episode 5: Truth',
  [('盾を取り返す',
    'ニコを殺したウォーカーはその場から逃げ、工場に逃げこむ。サムとバッキーが追いつき、盾を渡すよう求める。\nウォーカーは渡さず、戦いになる。ウォーカーはサムの翼を壊してしまう。\nそれでも2人は力を合わせる。バッキーはウォーカーの腕を折って盾を放させ、2人は盾を取り返す。\nサムは、壊れた翼をトレス中尉にあずけ、フラッグ・スマッシャーズを探し続けてほしいとたのむ。',
    'Taking back the shield',
    'After killing Nico, Walker flees to a factory. Sam and Bucky catch up and demand the shield.\n'
    "He refuses and they fight. Walker wrecks Sam's wings.\n"
    "Working together, they get the shield back; Bucky breaks Walker's arm to make him let go.\n"
    'Sam leaves his damaged wings with Torres and asks him to keep looking for the Flag Smashers.'),
   ('ジモの引き渡し',
    'バッキーは、ソコヴィアの戦いで亡くなった人々の慰霊の場所で、ジモを見つける。\n'
    'バッキーは銃を向けて引き金を引くが、弾ははじめから抜いてあった。\n'
    'ジモは逃げずに、アヨたちドーラ・ミラージュに引き渡され、海の上にある特別な刑務所「ラフト」に送られることになる。\n'
    'アヨは、ジモと組んだバッキーに「しばらくワカンダには来ないほうがいい」と言う。それでも、バッキーのたのみを聞いて、ワカンダに「お願い」をしてくれることになる。',
    'Handing over Zemo',
    'Bucky finds Zemo at the memorial for those who died in Sokovia.\n'
    'Bucky aims his gun and pulls the trigger, but he had already removed the bullets.\n'
    'Zemo goes quietly and is handed to the Dora Milaje, to be sent to the Raft, a high-security prison at sea.\n'
    'Ayo tells Bucky not to come to Wakanda for a while after working with Zemo, but agrees to ask Wakanda for a favor on his behalf.'),
   ('ウォーカーへの処分とヴァレンティーナ',
    'ウォーカーは軍の審問にかけられ、キャプテン・アメリカの資格を取り上げられ、軍を不名誉なかたちで去ることになる。\nベンチに座っているウォーカーのもとに、ヴァレンティーナという謎の女性が現れる。「血清を打ったことも、あの男を殺したことも正しかった」と言い、いずれ連絡すると話して去る。',
    "Walker's punishment and Valentina",
    'At a hearing, Walker is stripped of the Captain America title and pushed out of the military in disgrace.\n'
    "A mysterious woman named Valentina approaches him on a bench. She says taking the serum and killing the Flag Smasher were the right calls, and that she'll be in touch."),
   ('イザイアが語った真実',
    'サムはもう一度ボルティモアのイザイアに会いに行く。イザイアは、自分に何があったのかをすべて話す。\n'
    '朝鮮戦争のころ、イザイアたち黒人の兵士は、血清の実験に使われた。多くの仲間は血清のせいで亡くなった。同じように実験に使われ、つかまっていた仲間たちを、イザイアはひとりで助けに行った。それなのに国は、彼を英雄としてではなく罪人として、30年も閉じこめ、実験を続けた。家族には、彼は死んだと伝えられていた。\n'
    'イザイアは「黒人をキャプテン・アメリカにする国などない。なりたいと思うべきでもない」とサムに言う。',
    'The truth Isaiah tells',
    'Sam goes back to see Isaiah in Baltimore, who tells him everything.\n'
    'In the Korean War era, he and other Black soldiers were experimented on with the serum, and many died. When fellow soldiers who had also been experimented on were held captive, Isaiah went '
    'alone to rescue them. Instead of honoring him, the country imprisoned him for 30 years and kept experimenting. His family was told he had died.\n'
    "Isaiah tells Sam a Black man will never be allowed to be Captain America, and shouldn't want to be."),
   ('ルイジアナで船と盾',
    'サムは盾を持ってルイジアナに帰り、姉サラと家族の船を直しはじめる。サムを昔から知る近所の人たちも、次々と手を貸してくれる。\n'
    'バッキーもやって来て、ワカンダから届いたケースをサムに渡す。バッキーは修理を手伝い、サムと一緒に盾を投げる練習をする。\n'
    'バッキーは、サムが盾を手放したとき「スティーブが信じたものまで捨てられ、自分の居場所もなくなった気がした」と打ち明ける。\n'
    'サムは「償いを本当に終わらせたいなら、相手に正直に向き合え」と助言する。2人は過去を乗りこえ、一緒に戦うと決める。',
    'The boat and the shield in Louisiana',
    'Sam takes the shield home to Louisiana and starts fixing the family boat with Sarah. Neighbors who have known him for years pitch in.\n'
    'Bucky arrives and hands Sam a case sent from Wakanda. He helps with the boat and trains with Sam, throwing the shield.\n'
    "Bucky admits that when Sam gave the shield away, it felt like Steve's faith was thrown out, and that he had nothing left.\n"
    'Sam tells him that to truly make amends, he has to be honest with the people he hurt. They agree to move past their pasts and work together.'),
   ('レマーの両親',
    'ウォーカーは、レマーの両親に会いに行き、「レマーを殺した相手は、自分がやっつけた」とうそをつく。\n本当は、ウォーカーが殺したニコは、レマーを殺した人ではなかった。',
    "Lemar's parents",
    "Walker visits Lemar's parents and falsely claims he killed the man who murdered their son.\nIn truth, Nico, the man Walker killed, was not the one who killed Lemar."),
   ('カーリの次の計画',
    'カーリたちは、ニューヨークで開かれるGRCの会議をねらう計画を立てる。その会議では、難民キャンプの人々を元の国に戻す決まりが話し合われる。\n第1話でサムと戦ったバトロックも、カーリの仲間に加わる。バトロックはシャロンの手で刑務所から出されていて、サムに仕返しをしたいと思っている。',
    "Karli's next plan",
    "Karli's group plans to strike a GRC conference in New York, where a plan to send refugees back to their old countries will be decided.\n"
    "Batroc, Sam's foe from Episode 1, joins them. He was released from prison by Sharon, and he wants to kill Sam."),
   ('ワカンダからのケース',
    'トレスから「フラッグ・スマッシャーズがニューヨークに現れた」と連絡が入る。サムは戦うことを決め、ワカンダのケースを開ける。中には、ワカンダで作られた新しいスーツが入っていた。',
    'The case from Wakanda',
    'Torres calls: the Flag Smashers have been spotted in New York. Sam decides to act and opens the Wakandan case. Inside is a new suit made in Wakanda.'),
   ('エンドクレジットの途中', 'ウォーカーは、くず鉄と自分の名誉勲章を使って、自分で新しい盾を作る。', 'Mid-credits', 'Walker builds a new shield of his own from scrap metal and his Medal of Honor.')]),
 ('第6話 ひとつの世界',
  'Episode 6: One World, One People',
  [('会議への襲撃',
    'ニューヨークでGRCの会議が始まる。難民キャンプの人々を元の国に戻す決まり（パッチ法）の投票が行われようとしていた。\n突然ビルの電気が消え、催涙ガスがまかれて大騒ぎになる。カーリたちの目的は、ビルに入ることではなく、中の人たちを外へ追い出すことだった。\nバッキーの前に、変装した人物が近づいてくる。変装を取ると、シャロン・カーターだった。シャロンも戦いに加わる。',
    'Attack on the council',
    'The GRC meets in New York to vote on the Patch Act, which would send refugees back to their old countries.\n'
    "The building's power goes out and tear gas sets off a panic. Karli's goal isn't to get in but to drive everyone out.\n"
    'A disguised figure approaches Bucky and reveals herself: Sharon Carter. She joins the fight.'),
   ('新しいキャプテン・アメリカ',
    'そこへ、ワカンダの新しいスーツと翼を身につけたサムが、盾を持って空から現れる。\nサムがバトロックと戦っているあいだに、フラッグ・スマッシャーズは議員たちを人質にとって連れ去る。\nサムは、人質を乗せて飛び去るヘリコプターを追いかけ、新しいドローン「レッドウィング」も使いながら、空中で人質を救い出す。',
    'The new Captain America',
    'Then Sam arrives from the sky with the shield, wearing his new Wakandan suit and wings.\n'
    'While Sam fights Batroc, the Flag Smashers take council members hostage.\n'
    'Sam chases a helicopter carrying hostages and, with a rebuilt Redwing drone, saves them in mid-air.'),
   ('トラックとウォーカー',
    'バッキーは、人質を乗せたトラックを止めに向かう。カーリはバッキーの気をそらすため、車に火をつけて逃げようとする。そこへ、手作りの盾を持ったウォーカーが現れる。\n'
    'バッキーは燃えるトラックから人質を助け出し、ウォーカーと一緒にフラッグ・スマッシャーズと戦うが、倒されてしまう。\n'
    'カーリは残ったトラックを、高いところから落ちそうな場所まで走らせる。ウォーカーは、カーリを追って仕返しをするより、人質を助けることを選び、トラックを引き戻そうとする。\n'
    'カーリたちはウォーカーに襲いかかり、みんなで下に落ちてしまう。そこへサムが飛んできて、トラックを支え、人質は助かる。',
    'The truck and Walker',
    'Bucky goes after trucks carrying hostages. Karli sets a vehicle on fire to distract him and get away, but Walker arrives with his homemade shield.\n'
    'Bucky frees the hostages from the burning truck and fights the Flag Smashers alongside Walker, but is knocked down.\n'
    'Karli drives the last truck to the edge of a drop. Walker chooses to save the truck rather than chase her for revenge.\n'
    "Karli's group attacks him and they all fall to the ground below. Sam flies in, holds the truck, and the hostages are saved."),
   ('シャロンの正体とバトロックの死',
    '人質が助け出されると、バトロックが煙幕をはり、そのすきにフラッグ・スマッシャーズは逃げる。\n'
    'シャロンは、カーリを追いつめる。実はシャロンこそが、マドリプールの裏社会の支配者パワー・ブローカーだった。シャロンは、自分を裏切ったカーリに怒っている。\n'
    'バトロックは「正体をばらされたくなければ、もっと金をよこせ」とシャロンを脅す。シャロンは、その場でバトロックを撃ち殺す。この撃ち合いの中で、シャロンもカーリに撃たれて傷を負う。',
    "Sharon's secret and Batroc's death",
    'Once the hostages are freed, Batroc sets off smoke grenades so the Flag Smashers can escape.\n'
    "Sharon corners Karli. In truth, Sharon is the Power Broker, the boss of Madripoor's underworld, and she is angry that Karli betrayed her.\n"
    'Batroc tries to blackmail her for more money. Sharon shoots him dead on the spot. In the shootout, Sharon is also wounded by Karli.'),
   ('カーリの最期',
    'サムはカーリを止めに来て、話し合おうとする。しかしカーリは聞き入れず、サムに襲いかかる。サムは反撃せず、「ほかの道がある」と語りかけ続ける。\nカーリがサムに銃を向けたとき、シャロンがカーリを撃つ。カーリはサムの腕の中で、泣きながら「ごめんなさい」と言って息をひきとる。サムはカーリの体を抱えて外へ運び出す。',
    "Karli's end",
    "Sam tries to reason with Karli, but she won't listen and attacks him. He won't fight back and keeps telling her there is another way.\n"
    "When Karli holds Sam at gunpoint, Sharon shoots her. Tearful, Karli dies in Sam's arms, saying she's sorry. Sam carries her body out."),
   ('サムの言葉',
    'カメラが集まる中で、サムはGRCの議員たちに語りかける。「あなたたちは、何百万もの人の暮らしを机の上で決めている。住む場所を失った人々の声を聞いてほしい」。\nサムの言葉で、GRCは、住む場所を失った人々を元の国に戻す投票を延期する。黒人のキャプテン・アメリカとして、サムは自分の言葉で、盾を持つ意味を示す。',
    "Sam's speech",
    'In front of the cameras, Sam tells the GRC officials they decide millions of lives from their desks and must listen to the people who lost their homes.\n'
    'He convinces the GRC to postpone the vote and help those people instead. As a Black Captain America, he shows in his own words what the shield means.'),
   ('輸送車の爆発',
    '生き残ったフラッグ・スマッシャーズの仲間たちはつかまり、ラフトへ送られることになる。ところが運ばれる途中で、車に仕掛けられた爆弾が爆発し、全員が死ぬ。爆弾を仕掛けたのは、ジモの執事オエズニクだった。\nラフトの牢屋の中で、ジモはそのニュースを聞く。',
    'The transport explodes',
    "The surviving Flag Smashers are arrested, to be sent to the Raft. On the way, a bomb planted by Zemo's butler Oeznik blows up their transport, killing them all.\n"
    'In his cell on the Raft, Zemo hears the news.'),
   ('USエージェント', 'ヴァレンティーナはウォーカーに新しいスーツを渡し、「USエージェント」という新しい名前を与える。', 'U.S. Agent', 'Valentina gives Walker a new suit and dubs him U.S. Agent.'),
   ('イザイアの像',
    'サムはイザイアと孫のイーライを、博物館のキャプテン・アメリカの展示に連れていく。そこには、イザイアの像と彼の本当の物語が加えられていた。イザイアは涙する。',
    "Isaiah's statue",
    "Sam brings Isaiah and his grandson Eli to the museum's Captain America exhibit, which now features a statue of Isaiah and his true story. Isaiah is moved to tears."),
   ('ヨリさんへの告白',
    'バッキーはヨリさんを訪ね、ついに本当のことを打ち明ける。「あなたの息子さんを殺したのは、ウィンター・ソルジャーだった私です」。ヨリさんは涙を浮かべ「なぜだ」とたずねる。バッキーは「自分では選べなかった」と答える。許してもらえたかどうかは描かれない。\nバッキーは、ノートに残っていたほかの名前もすべて線で消し、レイナー先生のもとを訪ねてノートを手渡す。償いのノートは、これで終わった。',
    'Telling Yori',
    "Bucky visits Yori and finally tells him: as the Winter Soldier, he killed Yori's son. Tearful, Yori asks why. Bucky says he didn't have a choice. Whether Yori forgives him isn't shown.\n"
    'Bucky crosses off every other name on his list and hands the notebook to Dr. Raynor. His amends are finished.'),
   ('ルイジアナのお祝い',
    'ルイジアナでは、直った家族の船のそばで、近所の人たちが集まってお祝いのパーティーが開かれる。バッキーも招かれ、サムの家族と笑い合う。\n画面に、このドラマの新しい題名『キャプテン・アメリカ＆ウィンター・ソルジャー』が映し出される。',
    'Celebration in Louisiana',
    "In Louisiana, neighbors gather for a cookout by the restored boat. Bucky is invited and laughs with Sam's family.\nThe title card changes to Captain America and the Winter Soldier."),
   ('エンドクレジットの途中',
    'シャロンは、これまでの罪をすべて許され、CIAの元の仕事に戻れることになる。そのあと、シャロンは電話で誰かに「政府の秘密に近づけるようになった」と話す。',
    'Mid-credits',
    'Sharon receives a pardon and is reinstated to her old CIA position. Afterward, she tells someone on the phone that she now has access to government secrets.')]),
 ('まとめ（最終話までのネタバレ）',
  'Summary (spoilers through the finale)',
  [('バッキーの償い（ノートの人たち）',
    '①アトウッド上院議員（第1話）：ウィンター・ソルジャーだったころに議員にしてしまった人。悪事の会話を録音し、警察につかまえさせた。\n'
    '②ヨリ・ナカジマさん（第1話〜第6話）：ホテルで殺しの場面を見てしまった息子のRJを、バッキーが殺していた。毎週昼ごはんを食べる友だちになったが言えずにいた。第6話でついに打ち明け、ヨリさんは涙を浮かべる。\n'
    '最後に、ほかの名前もすべて消したノートをレイナー先生に手渡す（第6話）。',
    "Bucky's amends (the notebook)",
    '1) Senator Atwood (Ep. 1): he helped put her in office as the Winter Soldier. He recorded her ordering a hit and got her arrested.\n'
    "2) Yori Nakajima (Eps. 1–6): Bucky killed Yori's son RJ, who witnessed a hit in a hotel. They became weekly lunch friends, but Bucky couldn't tell him until Episode 6. Yori is left in tears.\n"
    'Finally, he crosses off every other name and hands Dr. Raynor the notebook (Ep. 6).'),
   ('死んだ人たち（話の順に）',
    '・セルビー（第3話）：マドリプールの大物。サムの正体がばれて起きた撃ち合いの中で撃たれて死ぬ。\n'
    '・ネーゲル博士（第3話）：血清を作り直した科学者。また血清が作られるのを防ぐため、ジモが撃つ。\n'
    '・GRCの倉庫の3人（第3話）：カーリが、人が中にいるまま倉庫を爆破した。\n'
    '・ドンニャ（第4話）：カーリの育ての母。難民キャンプで亡くなる（葬式の場面）。\n'
    '・レマー（第4話）：ウォーカーの親友。戦いの中でカーリに突き飛ばされ、柱にぶつかって死ぬ。カーリに殺すつもりはなかった。\n'
    '・ニコ（第4話）：フラッグ・スマッシャーズの一人。レマーを殺した人ではないのに、怒ったウォーカーが広場で盾でなぐって殺す。\n'
    '・バトロック（第6話）：金をよこせと脅したため、正体を知られたシャロン（パワー・ブローカー）が撃つ。\n'
    '・カーリ（第6話）：サムに銃を向けたところを、シャロンが撃つ。サムの腕の中で亡くなる。\n'
    '・残ったフラッグ・スマッシャーズ（第6話）：ラフトへ運ばれる途中、ジモの執事オエズニクが仕掛けた爆弾で死ぬ。',
    'Who died (in order)',
    "- Selby (Ep. 3): a Madripoor crime boss, killed in the shootout after Sam's cover is blown.\n"
    '- Dr. Nagel (Ep. 3): the scientist who recreated the serum. Zemo shoots him so no more can be made.\n'
    '- Three people at the GRC depot (Ep. 3): Karli blew it up with people inside.\n'
    "- Donya (Ep. 4): Karli's adoptive mother, who died in the refugee camp (seen at her memorial).\n"
    "- Lemar (Ep. 4): Walker's best friend. Karli knocks him into a pillar during the fight, without meaning to kill him.\n"
    "- Nico (Ep. 4): a Flag Smasher. Though he didn't kill Lemar, an enraged Walker beats him to death with the shield in a square.\n"
    '- Batroc (Ep. 6): Sharon (the Power Broker) shoots him when he tries to blackmail her.\n'
    "- Karli (Ep. 6): Sharon shoots her when she holds Sam at gunpoint. She dies in Sam's arms.\n"
    "- The remaining Flag Smashers (Ep. 6): killed by a bomb planted by Zemo's butler Oeznik on the way to the Raft.")])]
