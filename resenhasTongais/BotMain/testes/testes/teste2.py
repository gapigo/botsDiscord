from PIL import Image
im = Image.open('../../imagens/monopoly/game.png')
im.show()

mensagens = ['Toma esses $2M\nAgora vê se para de cair em lugar que não era (╯‵□′)╯︵┴─┴',
                 'Lugar onde muitas mães foram acusadas de rodar a bolsinha ヽ(´Д`;)ﾉ',
                 'De **BOSTA PURA** à **gold**, reze antes de abrir (・ωｰ)～☆',
                 'É..\n**É... MENTIRA (　〇□〇）**',
                 'MALDITO ESTADO! CADÊ OS ANCAPS NESSA PORRA? (ノಠ益ಠ)ノ彡┻━┻',
                 'AMO TECLAR NO MEU APARELHO COMPUTADORIZADO... ( ဖ‿ဖ)_/\n\nPerai, tenho que **PAGAR QUANTO?** ゞ◎Д◎ヾ',
                 'Achas que tens o que é preciso para esmagares a minha rata? **CLICA AQUI**\n（￣ε￣ʃƪ）\n~~le scam\n(;ﾟдﾟ)',
                 'o gapigo fala: VAI SE BENZER GUARDIÃO!!! ＼(´◓Д◔`)／',
                 '"BIG, SE VOCÊ IR TAPETE DE MAG 7 VAI MORRER"\n"roger that"\n"ENTÃO SAI DAI IMBECIL"\n"Negattive"\n~~Big morre\n"IMBECIL!!!" (╬♛ 益♛ )',
                 'if eco is true:\n    buy **R8**\n    go **mid**\n    empty **ammunition** till **FUCKING DIE**\n\nif died:\n    say **BYATTTT! NEIN, NEIN, NEIN, NEIN, NEIN, NEIN!!!!!\n(◞≼◉ื≽◟ ;益;◞≼◉ื≽◟)Ψ',
                 'Cantinho da depressão, apenas visitantes\nApenas vendo como funciona a vida ( ･ω･)ﾉ',
                 'Prefeito de **não-me-toque** é afastado por assédio ಠ_ರೃ',
                 f'**TOCOFOMEEEEEEEEE\nCOM FOMEEEEEEEEEEEEEEE\nCOM A PORRAAAAA DE FOMEEEEEEEEEEE\n{"T" + "O" * 10 + " C" + "O"*10 + "M" + " FOM" + "E"*200}\n\nvítimas: (((ﾟДﾟДﾟДﾟ)))**',
                 'Dizem que o Acre é um estado\nTo começando a achar que é uma cidade Hm... :hm:\nAcho que o gleison lima concorda (￣ー￣)ｂ',
                 'A transformação secreta de São Paulo para lutar contra o Jiren\nDando leptospirose para ele\n\n**OUTSTANDING MOVE SÃO PAULO! (☉∀☉)**',
                 'eu sou o passaro Quetzalcoatlus\ne eu dubido vc nao fala\n\n        ***carpe diem***\n\npelos proximo 5 sem gundo\n⊹⋛⋋(◐⊝◑)⋌⋚⊹',
                 'lá foi achado o integrante honesto do PT\n\n\n- pera, você disse "hones..? **(ʘ言ʘ╬)??!!!**',
                 'cuidado com o guardião e suas caixas de pandora ༼つಠ益ಠ༽つ ─=≡ΣO))     ⊃゜Д゜）⊃',
                 '✌.ʕʘ‿ʘʔ.✌\n\n...\n\n(╬ﾟ◥益◤ﾟ) GROELÂNDIA SUA GRANDISSÍSMA FILHA DA PUTA, ESCUTA AQUI SEU TERRITÓRIO VERM... \n         - gapigo, 2018, definitivamente não em um de seus melhores momentos (︶︹︺)',
                 'basicamente um scam\n**EU POSSO EXPLICAR!**\nVeja bem: se você comprar, você tá comprando algo que não existe\nse você for obrigado a pagar, você tá pagando para nada, ou seja, sendo roubado que nem quando paga imposto ☜╮(´ิ∀´ิ☜╮)',
                 'Parabéns, você ganhou um sugar daddy para te sustentar\nNa próxima vez que você tiver que pagar algo, você terá a opção "USAR"\n\nPera, você ganhou o que? HMMMMMM **paitola**\n'
                        '( ͡ʘ╭͜ʖ╮͡ʘ) ( ͡⚆ ͜ʖ ͡⚆)  ( ͡☉ ͜ʖ ͡☉)   (つ ͡° ͜ʖ ͡°)つ',
                 'asdoipk',
                 'ᕕ༼✿•̀︿•́༽ᕗ -> sorte do guardião quando ele começa uma partida de CSGO',
                 'O CARA BOTOU UMA MÁSCARA!!! (ʘ言ʘ╬)\n**CHAMA BULLDOZER!!!!** ┻━┻彡(┛◉Д◉)┛彡┻━┻',
                 'basicamente o real motivo do gapigo ter dropado o warframe (゜Д゜*)（´皿｀；）',
                 '**so o nuevo canser\ncurativo esijo dinero**',
                 'E o qu  ée ess? (ʘдʘ╬)\nVOC ACH QU ISS É NORMALA? (ಠ⌣ಠ)\nOlha iss áqui gent (ಠ ∩ಠ)\nParace a Chernobyle (╬ಠ益ಠ)\n_(´ཀ`」 ∠)_ blé',
                 'PERANHAS...(ﾟДﾟ;)\n\n**PERANHAS EVERYWHEREE!!!!! 三ᕕ(◉Д◉ )ᕗ**',
                 'Cuidado com o Chupa Cu de goianinha,\nele pode aparecer a qualquer hora em qualq..\nPERA... que molhadinho é esse na minha bunda? ⑉ႣỏႣ⑉\n\n...\n\n **CORRE LADRÃO! 三ᕕ(◉Д◉ )ᕗ**',
                 'TENHO CARA DE ENQUEDITA MEU\nPORRA MEU\nTODO DIA ISSO MEU\nSÓ PORQUE SO CANHOTO MEU\nTODO DIAS ESSES ENQUEDITA\nMATA ESSES ENQUEDITA LOGO\nE ME DEXA SE CANHOTO EM PAZ MEU\nPORA MEU\nTODO DIA\nTODO DIA\nNUM E POSSIVEL MEU\nTODO DIA ENQUEDITA FAZENDO MERDA MEU\nACABA LOGO COM ESSES FIOS DA PUTA MEU\n	- honestamente, zezoia, 2020 （πーπ)',
                 'É meu chapa, parece que você ganhou a famosa,\nA TEMIDA,\nA QUE O GUARDIÃO SEMPRE FALA\n...\n**YOU GAINED CRIPPLING DEPRESSION (；´∩｀；)**',
                 'ele que criou o coronga virus\nÉ o capeta reencarnado, ele cuspiu fogo e incendiou a Austrália\nEle atirou de lança-chamas pro céu e pegou na Amazônia e fez as queimadas dos últimos 20 anos\nEle deu um peido e criou a radiação de Chernobyl\no terremoto do japão foi uma tentativa homofobica de nego ney de eliminar os niponicos do mundo\nÉ ele que forçou as mulheres na 2ª guerra a trabalhar mais de 24 horas por dia\nEle que criou o fascismo e ensinou Mussolini\nele ensinou hitler a queimar judeu apenas pq gostava do aroma\nEle que ensinou os espartanos a atacar os defeituosos no fundo do poço só pra fazer a famosa "sopa de macaco"\n\n**  - Guardião e gapigo comentando as atrocidades do maligno Nego Ney 屮(ఠ𐤃ఠ)屮**',
                 f'**DORIMEEE** :musical_note:\nINTERINO ADAPARE\n**DORIME**\nAMENO, AMENO\nLATIRE\nLATIREMO\n**DORIME**\n',
                 "Rolando pra ver se dá sorte...\n(ﾟ∀ﾟ)( ﾟ∀)(　ﾟ)(　　)(ﾟ　)(∀ﾟ )(ﾟ∀ﾟ)",
                 'ears: U got that\neyes: Anime\nbrain: Ricardo\nMind: Moto Moto\nHands: meme\nhotel: trivago\nme: got that\ngapigo:   ┬┴┬┴┤͜ʖ ͡°) olá meu chapa├┬┴┬┴',
                 'oq q ele fes\n\n**- ELE COME** conta **COOL**rente **DE CURIOSO**',
                 "༼;´༎ຶ ༎ຶ༽ -> sanidade mental do guardião após a sorte dele dar um alô\n**(´༎ຶ༎ຶ) -> guardião não podendo discordar**",
                 '(（ლ ^ิ౪^ิ）ლ) - Posso ir já?\n((ಠ ∩ಠ)) - Não\n(（ლ ^ิ౪^ิ）ლ) - Mas é minha casa\n((ಠ ∩ಠ)) - Já disse que não\n(（ლ ^ิ౪^ิ）ლ) - Onde vou ficar então?\n -(ლಠ益ಠ)ლ) **SEI LÁ SEU FILHO DA PUTA, SÓ SEI QUE VOCÊ NÃO MORREU ENTÃO NÃO VAI PRA LÁ**\n\n - Guardião conversando com a Morte',
                 'Parece difícil para a maioria das pessoas entender **princípios econômicos básicos** e as repercussões óbvias do uso da coerção estatal no mercado. Eu acho tudo isso muito simples, basta entendermos que **a coerção não muda os princípios econômicos**, ela apenas **interfere nos seus resultados, normalmente para pior**.\n\nOs princípios econômicos fundamentais que precisamos ter em mente quando vemos o **governo intervindo no mercado através da coerção** são poucos, listo abaixo alguns:\n\n1. Gastos\n**Governo não cria valor algum**, para ele poder trocar os valores que não possui por aqueles que ele deseja, **precisará, antes, subtrair valor** já criado de quem os criou. **Isso só é possível com o uso da coerção**. Quando o governo se intromete na economia é apenas uma **infernal máquina de redistribuição violenta de recursos**. **Suga o valor existente no mercado**, retém parte para si e **distribui para aqueles que ele pretende favorecer com privilégios**. Parece difícil para a maioria das pessoas entender princípios econômicos básicos e as **repercussões óbvias do uso da coerção estatal no mercado**. Eu acho tudo isso muito simples, basta entendermos que **a coerção** não muda os princípios econômicos, ela **apenas interfere nos seus resultados, normalmente para pior**.\n\nOs princípios econômicos fundamentais que precisamos ter em mente quando vemos o governo intervindo no mercado através da coerção são poucos, listo abaixo alguns:\n\n2. Tributação\n**Sempre que o governo decidir gastar, não adianta espernear, ele terá que tributar**. **Cada centavo** despendido pelo governo **será retirado de alguém**, queira essa pessoa ou não. Ou vocês não sabem **o significado de coerção?** Governos não tributam porque não têm mais o que fazer, **governos tributam para gastar**. E tem **mais, governos** podem seguir gastando mesmo quando não conseguem **mais tributar.** (´・＿・`)',
                 'Quem diria que visitar o cu dos outros é tão caro? (*´Д｀)=з'
                 ]

print(len(mensagens))

print('I GAINED CRIPPLING DEPRESSOR DPS DESSA ♿(；´∩｀；)')