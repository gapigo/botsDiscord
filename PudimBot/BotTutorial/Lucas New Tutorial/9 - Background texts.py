import discord
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='.')
status = cycle(['I GAINED CEREBAU QUEMÇA DPS DESSA (；´∩｀；)',
                'Ɑ͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶͞ ̶ﻝﮞ',
                '┬┴┬┴┤͜ʖ ͡°) olá meu chapa├┬┴┬┴',
                '♿',
                '📞  alô valve, tem bot de hack📞📞📞     (･`д･´)'])

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.Xkm_Nw.IFXbHT8g932V1bosGMoouHyktYw'


@client.event
async def on_ready():
    change_status.start()  # inicializa o loop
    print(f'Bot {client.user.name} is ready.')


@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))  # função de passar o loop


client.run(TOKEN)
