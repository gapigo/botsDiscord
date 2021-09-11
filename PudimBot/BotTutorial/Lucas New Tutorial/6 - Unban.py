import discord
from discord.ext import commands

client = commands.Bot(command_prefix='.')

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.XkjMmw.TiElLsOl0pjgHoIko47QcfAELXk'

@client.event
async def on_ready():
    print(f'Bot {client.user.name} is ready.')

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    if reason is not None:
        await ctx.send(f'Banned {member.mention} by {reason}')
    else:
        await ctx.send(f'Banned {member.mention}')

@client.command()
async def unban(ctx, *, member):
    print('ok')
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
            return


client.run(TOKEN)
