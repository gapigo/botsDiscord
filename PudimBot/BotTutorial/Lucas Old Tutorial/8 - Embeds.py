import discord
from discord.ext import commands

TOKEN = 'Njc4NDQ3NDY4MTI3NzE1Mzkz.XktplQ.9Fn2jCfonPj6EbXvtpQi5HOIy_M'

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
	print('Bot is ready.')

@client.command(pass_context=True)
async def clear(ctx, amount=10):
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, limit=int(amount)):
		messages.append(message)
	await client.delete_messages(messages)


@client.command(aliases=['jacaré'])
async def jacare(ctx):
	embed = discord.Embed(
		title= 'Título',
		description= 'Isso é uma descrição',
		colour = discord.Colour.blue()
	)

	embed.set_footer(text='Isso é um rodapé')
	embed.set_image(url='https://i.imgur.com/YjhFKjH.jpg')
	embed.set_thumbnail(url='https://i.ytimg.com/vi/4Pmmp-xfTd4/maxresdefault.jpg')
	embed.set_author(name='Sans', icon_url='https://i.ytimg.com/vi/wDgQdr8ZkTw/maxresdefault.jpg')
	embed.add_field(name='Nome de campo', value='Valor do campo', inline=False)
	embed.add_field(name='Nome de campo', value='Valor do campo', inline=True)
	embed.add_field(name='Nome de campo', value='Valor do campo', inline=True)

	await ctx.send(embed=embed)


client.run(TOKEN)
