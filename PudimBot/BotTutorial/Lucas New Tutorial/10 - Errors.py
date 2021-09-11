import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xkm_Nw.IFXbHT8g932V1bosGMoouHyktYw'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando não existente!')

@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    await ctx.send('Não foi possível apagar, pois não foi especificado o número de mensagens a ser deletado')

client.run(TOKEN)