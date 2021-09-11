import discord, os
from discord.ext import commands
from PIL import Image

import discord
from discord.ext import commands


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')

    # Events
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency * 1000)}ms')

    # Events
    @commands.command()
    async def pudim(self, ctx):
        '''
        with open('pudim.jpg', 'rb') as f:
            picture = discord.File(f)'''
        path = os.path.realpath('foto do computador.py')
        path = path[0:path.rfind('/')]
        path += '/outro/pudim.jpg'
        await ctx.send(path)

        im = Image.open(path)
        file = discord.File(path, filename="pudim.jpg")
        await ctx.send("aspodkasd", file=file)
        im.save(f'{path[:-10]}/teste.png')
        '''
        im = Image.open('../../outro/pudim.jpg')
        file = discord.File("../images/pudim.jpg", filename="pudim.jpg")
        await ctx.send("aspodkasd", file=file)'''


def setup(client):
    client.add_cog(Example(client))
