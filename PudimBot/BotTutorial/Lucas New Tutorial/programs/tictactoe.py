jogo = '123456789'

troca = True
p1 = False
p2 = False


def validacao(j):
    global jogo
    while True:
        opc = str(input(f'Digite a sua opção jogador {j}: ')).strip().upper()
        try:
            opc = opc[0]
        except:
            print('Valor desconhecido, digite novamente')
        else:
            if opc.isnumeric():
                if jogo[(int(opc))-1].isnumeric():
                    return opc
                else:
                    print('Valor já utilizado, digite novamente')
            else:
                print('Valor desconhecido, digite novamente')


while True:
    if jogo.isalpha():
        print('Deu velha!')
        break
    elif p1:
        print('p1 é o vencedor!')
        break
    elif p2:
        print('p2 é o vencedor!')
        break

    if troca:
        opc = validacao(1)
        jogo = jogo.replace(f'{opc}', 'X')
        troca = False
    else:
        opc = validacao(2)
        jogo = jogo.replace(f'{opc}', 'O')
        troca = True

    for i in range(0, 9):
        if jogo[i].isnumeric():
            print('_', end='')
        else:
            print(jogo[i], end='')
        if (i+1) % 3 == 0:
            print()

    # definições de vitória
    if jogo[0] == 'X' and jogo[1] == 'X' and jogo[2] == 'X':
        p1 = True
    if jogo[3] == 'X' and jogo[4] == 'X' and jogo[5] == 'X':
        p1 = True
    if jogo[6] == 'X' and jogo[7] == 'X' and jogo[8] == 'X':
        p1 = True
    if jogo[0] == 'X' and jogo[3] == 'X' and jogo[6] == 'X':
        p1 = True
    if jogo[1] == 'X' and jogo[4] == 'X' and jogo[7] == 'X':
        p1 = True
    if jogo[2] == 'X' and jogo[5] == 'X' and jogo[8] == 'X':
        p1 = True
    if jogo[0] == 'X' and jogo[4] == 'X' and jogo[8] == 'X':
        p1 = True
    if jogo[2] == 'X' and jogo[4] == 'X' and jogo[6] == 'X':
        p1 = True

    if jogo[0] == 'O' and jogo[1] == 'O' and jogo[2] == 'O':
        p2 = True
    if jogo[3] == 'O' and jogo[4] == 'O' and jogo[5] == 'O':
        p2 = True
    if jogo[6] == 'O' and jogo[7] == 'O' and jogo[8] == 'O':
        p2 = True
    if jogo[0] == 'O' and jogo[3] == 'O' and jogo[6] == 'O':
        p2 = True
    if jogo[1] == 'O' and jogo[4] == 'O' and jogo[7] == 'O':
        p2 = True
    if jogo[2] == 'O' and jogo[5] == 'O' and jogo[8] == 'O':
        p2 = True
    if jogo[0] == 'O' and jogo[4] == 'O' and jogo[8] == 'O':
        p2 = True
    if jogo[2] == 'O' and jogo[4] == 'O' and jogo[6] == 'O':
        p2 = True
