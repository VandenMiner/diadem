 
import discord
from discord.ext import commands
from discord.utils import get
import os

ds = commands.Bot(command_prefix='!')


@ds.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def чич(ctx, amount = 100):
	await ctx.channel.purge(limit = amount)



@ds.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def accept(ctx, user: discord.Member):
	channel = ds.get_channel(713364415180832768)
	emb = discord.Embed(colour = discord.Color.gold())
	emb.set_footer(icon_url = 'https://media.discordapp.net/attachments/647015015211335700/713387996895903865/Ava_gruppy_vk_1.png?width=677&height=677')

	emb.add_field( name = "_Diadem_", value = "**Привет! Добро пожаловать в семью, "+ str(user.mention) +" :family: \nЖелаем тебе приятной игры!**")
	await channel.send(embed = emb)
	await user.send('''**Приветствую тебя, '''+user.mention+''' !
Поздравляю тебя с успешным получением роли "Игрок" в discord-сервере проекта Diadem! :tada:**''')
	role = get(ctx.guild.roles, name='Игрок')
	await user.add_roles(role)
	role1 = get(ctx.guild.roles, name='Без роли')
	await user.remove_roles(role1)



@ds.event
async def on_message(message):
	await ds.process_commands(message)
	if message.content.startswith('1'):
		sendchannel = message.channel
		channelforaccept = ds.get_channel(713364415180832768)
		print(str(sendchannel) + str(channelforaccept.name))
		if sendchannel == channelforaccept:
			channel = ds.get_channel(713368052699365456)
			author = message.author
			await channel.send(author.mention + '** подал заявку на сервер**')

token = os.environ.get("BOT_TOKEN")

ds.run(token)
