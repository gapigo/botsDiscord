import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xlbzhw.2UxAC2YZBXeT5VvTOku3252x9bw'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

autor = 0
@client.command()
async def pegaIp(ctx):
    global id
    await ctx.send(f'Id de {ctx.author.mention} pegado com sucesso')
    id = ctx.author

@client.command()
async def dem(ctx):
    global teste
    path = '../../imagens/monopoly/game.png'
    file = discord.File(path, filename='game.png')
    id = ctx.author.id
    user = client.get_user(id)
    await user.send('apsodkasd')
    #await ctx.autor.send(file=file)

@client.command()
async def dm(ctx):
    global teste
    await teste
client.run(TOKEN)
