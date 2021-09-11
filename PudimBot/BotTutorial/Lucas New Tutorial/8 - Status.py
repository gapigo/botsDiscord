import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')
token = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xkm_Nw.IFXbHT8g932V1bosGMoouHyktYw'

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('┬┴┬┴┤͜ʖ ͡°) olá meu chapa├┬┴┬┴'))
    print(f'{client.user.name} is ready')

client.run(token)