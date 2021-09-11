import random
jogo = {'1': {'cartas': [1, 2, 3],
              'nome': 'Gapigal'},
        '2': {'cartas': [6, 9, 0],
              'nome': 'Cardinal'},
        '3': {'cartas': [6, 9, 0],
              'nome': 'Boga'},
        '4': {'cartas': [6, 9, 0],
              'nome': 'QUENIA'}
        }
escolhidos = []
for jogador in jogo.keys():
    escolhidos.append(jogador)
random.shuffle(escolhidos)
i = 0
for jogador in escolhidos:
    print(f'{jogo[jogador]["nome"]} será o {i+1}º')
    i += 1

contrario = escolhidos[::-1]
print(escolhidos)
print(contrario)