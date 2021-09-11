import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xk5msQ.WDQpv-DIC_hfzOm5k2noLAkOubE'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.command()
async def comando(ctx):
    await ctx.send(f'{ctx.author.mention}')

client.run(TOKEN)
