import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xkm_Nw.IFXbHT8g932V1bosGMoouHyktYw'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

client.run(TOKEN)
