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


def setup(client):
    client.add_cog(Example(client))
