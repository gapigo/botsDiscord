import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xkm_Nw.IFXbHT8g932V1bosGMoouHyktYw'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author}, você não tem permissão para digitar esse comando!')

def is_it_me(ctx):
    return ctx.author.id == 325384616221474818

@client.command()
@commands.check(is_it_me)
async def permissao(ctx):
    await ctx.send(f'{ctx.author} tem permissão para rodar esse comando')

@permissao.error
async def permissao_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send(f'{ctx.author}, você não tem permissão para digitar esse comando!')

@client.command()
async def id(ctx):
    await ctx.send(f'O seu id é {ctx.author.id}')

client.run(TOKEN)
