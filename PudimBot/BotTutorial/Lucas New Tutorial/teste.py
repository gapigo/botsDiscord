import discord
from discord.ext import commands

x = 0

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xkj4QQ.b-w7gD3W4upJ25IUxRn3wp2dVTI'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.command()
async def mudar(ctx, number):
    global x
    y = x
    x = number
    await ctx.send(f'X foi mudado de {y} para {x}')

client.run(TOKEN)


