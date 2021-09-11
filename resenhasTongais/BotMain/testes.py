import discord
import os
import json
from discord.ext import commands

"""
    1. VARIÁVEIS DE INICIALIZAÇÃO
"""

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.XlUUAQ.5B68q53Hdbt4CUrf5lSL2BUG1gE'

prefixosdir = './banco/prefixos.json'

"""
    2. PREFIXAÇÃO
"""


# Função de inicialização que seta os prefixos do arquivo para o bot quando ele abre
def get_prefix(client, message):
    with open(prefixosdir, 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix)


@client.event  # Evento de inicialização
async def on_ready():  # Emite um registro no console se o bot está
    print(f'{client.user.name} está pronto.')  # Rodando ou não


# Função de adicionar no registro prefixos.json sempre que um server entra
@client.event
async def on_guild_join(guild):
    with open(prefixosdir, 'r') as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = '.'

    with open(prefixosdir, 'w') as f:
        json.dump(prefixes, f, indent=4)


# Função de remover do registro prefixos.json sempre que um server sai
@client.event
async def on_guild_remove(guild):
    with open(prefixosdir, 'r') as f:
        prefixes = json.load(f)

    prefixes.pop(str(guild.id))

    with open(prefixosdir, 'w') as f:
        json.dump(prefixes, f, indent=4)


# Função de alteração do prefixo
@client.command(aliases=['prefixo'])
async def mudarprefixo(ctx, prefix):
    with open(prefixosdir, 'r') as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open(prefixosdir, 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefixo do comando mudado para {prefix}')


"""
    3. INICIALIZAÇÃO DE COGS
"""


# Carrega COG
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


# Descarrega COG
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


# Recarrega COG
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


# Rastreia cogs adicionadas
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

"""
    4. COMANDOS SIMPLES
"""

"""
    5. ERROS
"""




client.run(TOKEN)
