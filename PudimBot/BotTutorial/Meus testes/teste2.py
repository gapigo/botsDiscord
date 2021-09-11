import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xk5msQ.WDQpv-DIC_hfzOm5k2noLAkOubE'


@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'diretório.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'diretório.{extension}')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'diretório.{extension}')
    client.load_extension(f'diretório.{extension}')


for filename in os.listdir('./diretório'):
    if filename.endswith('.py'):
        client.load_extension(f'diretório.{filename[:-3]}')
    print()

client.run(TOKEN)