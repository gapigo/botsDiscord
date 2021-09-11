import discord, random
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

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

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

    @client.command()
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    if reason is not None:
        await ctx.send(f'Banned {member.mention} by {reason}')
    else:
        await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return

@tasks.loop(seconds=3)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))  # função de passar o loop

@client.command()
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    await ctx.send('Não foi possível apagar, pois não foi especificado o número de mensagens a ser deletado')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Comando não existente!')

client.run(TOKEN)
