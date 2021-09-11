import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.XkjMmw.TiElLsOl0pjgHoIko47QcfAELXk'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


client.run(TOKEN)
