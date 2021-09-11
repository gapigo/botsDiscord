import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xkm_Nw.IFXbHT8g932V1bosGMoouHyktYw'

jogo = '123456789'
troca = ['x', True]
p1 = False
p2 = False

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.command(aliases=['começar'])
async def comecar(ctx):
    global jogo, p1, p2, troca
    troca = ['', True]
    p1 = False
    p2 = False
    jogo = '123456789'
    await ctx.send('Jogo iniciado!')

@client.command(aliases=['X', 'p1', 'j1', 'Player1'])
async def x(ctx, jogada):
    global troca, jogo, p1
    if jogo.isnumeric():
        troca = ['x', True]
    if (troca[0] == 'x' and troca[1] is True) or (troca[0] == 'o' and troca[1] is False):
        jogada = jogada.strip()
        try:
            jogada = int(jogada)
        except:
            await ctx.send('Valor desconhecido, digite novamente')
            return
        else:
            try:
                booleano = jogo[int(jogada)-1].isnumeric()
            except:
                await ctx.send(f'{jogada} passou do intervalo de 1 a 9, tente novamente')
                return
            else:
                if jogo[int(jogada)-1].isnumeric():
                    inteiro = (int(jogada))
                    jogo = jogo.replace(f'{inteiro}', 'X')

                    string = jogo

                    ''' troca números por _ '''
                    for i in range(0, 9):
                        string = string.replace(f'{i+1}', '+')


                    await ctx.send(f'{string[0]}{string[1]}{string[2]}\n'
                                   f'{string[3]}{string[4]}{string[5]}\n'
                                   f'{string[6]}{string[7]}{string[8]}')

                else:
                    await ctx.send('Valor já utilizado, tente novamente')
                    return
    else:
        await ctx.send('Não é a vez de X jogar')
        return
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
    if p1 is True:
        await ctx.send('O JOGADOR X ganhou!')
        jogo = '123456789'
        return
    else:
        if troca[0] == 'x':
            troca[1] = False
        else:
            troca[1] = True
    if jogo.isalpha():
        await ctx.send('DEU VELHA!')
        jogo = '123456789'

@x.error
async def x_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Jogada não declarada')

@client.command(aliases=['O', 'p2', 'j2', 'Player2'])
async def o(ctx, jogada):
    global troca, jogo, p2
    if jogo.isnumeric():
        troca = ['o', True]
    if (troca[0] == 'o' and troca[1] is True) or (troca[0] == 'x' and troca[1] is False):
        jogada = jogada.strip()
        try:
            jogada = int(jogada)
        except:
            await ctx.send('Valor desconhecido, digite novamente')
            return
        else:
            try:
                booleano = jogo[int(jogada)-1].isnumeric()
            except:
                await ctx.send(f'{jogada} passou do intervalo de 1 a 9, tente novamente')
                return
            else:
                if jogo[int(jogada)-1].isnumeric():
                    inteiro = (int(jogada))
                    jogo = jogo.replace(f'{inteiro}', 'O')

                    string = jogo

                    ''' troca números por _ '''
                    for i in range(0, 9):
                        string = string.replace(f'{i+1}', '+')


                    await ctx.send(f'{string[0]}{string[1]}{string[2]}\n'
                                   f'{string[3]}{string[4]}{string[5]}\n'
                                   f'{string[6]}{string[7]}{string[8]}')

                else:
                    await ctx.send('Valor já utilizado, tente novamente')
                    return
    else:
        await ctx.send('Não é a vez de O jogar')
        return
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
    if p2 is True:
        await ctx.send('O JOGADOR O ganhou!')
        jogo = '123456789'
        return
    else:
        if troca[0] == 'o':
            troca[1] = False
        else:
            troca[1] = True
    if jogo.isalpha():
        await ctx.send('DEU VELHA!')
        jogo = '123456789'

@o.error
async def o_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Jogada não declarada')


client.run(TOKEN)
