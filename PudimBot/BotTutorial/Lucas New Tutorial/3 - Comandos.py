import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.XkjMmw.TiElLsOl0pjgHoIko47QcfAELXk'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'teste'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.',
                 'It is decidely so.',
                 'Without a doubt',
                 'Yes - definitely',
                 'You may rely on it',
                 'As I see it, yes0',
                 'Most likely',
                 'Outlook good',
                 'Yes',
                 'Signs point to yes',
                 'Reply hazy, try again',
                 'Ask again later',
                 'Better not tell you now',
                 'Cannot predict now',
                 'Concentrate and ask again',
                 "Don't count on it",
                 'My reply is no',
                 'My sources say no',
                 'Outlook not so good',
                 'Very doubtful']
    await ctx.send(f'Pergunta: {question}\n{random.choice(responses)}')

client.run(TOKEN)
