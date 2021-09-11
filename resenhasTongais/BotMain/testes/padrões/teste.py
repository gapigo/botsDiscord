import discord
from discord.ext import commands

permitido = 0
verifica = False

class Teste(commands.Cog):
    global verifica

    def __init__(self, client):
        self.client = client
        self.batata = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot {self.client.user.name} is ready.')


    def pode(ctx):
        global permitido
        id = permitido
        permitido = 0
        return ctx.author.id == id

    @commands.command()
    async def comando(self, ctx):
        global permitido
        await ctx.send(f'Você ganhou permissão para rodar permissão uma única vez')
        permitido = ctx.author.id

    @commands.command()
    @commands.check(pode)
    async def permissao(self, ctx):
        await ctx.send(f'{ctx.author} tem permissão para rodar esse comando')

    @permissao.error
    async def permissao_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{ctx.author}, você não tem permissão para digitar esse comando!')

    @commands.command()
    async def id(self, ctx):
        await ctx.send(f'O seu id é {ctx.author.id}')

    @commands.command()
    async def comando1(self, ctx):
        await ctx.send(f'Comando 1')
        global verifica
        verifica = True

    def vertificador(ctx):
        global verifica
        if verifica:
            return True
        else:
            return False
    @commands.command()
    @commands.check(vertificador)
    async def comando2(self, ctx):
        await ctx.send(f'Comando 2')

    @commands.command()
    async def nome(self, ctx):
        await ctx.send(f'Nome de {ctx.author.name}')



def setup(client):
    client.add_cog(Teste(client))
