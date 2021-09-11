import discord
from discord.ext import commands
client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.XkjMmw.TiElLsOl0pjgHoIko47QcfAELXk'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

client.run(TOKEN)