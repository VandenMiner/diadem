import discord#a
from discord.ext import commands
from discord.utils import get
import os
ds = commands.Bot(command_prefix='!')

@ds.event
async def on_ready():
	print(ds.get_all_members)
	print("Why are you gay?")
	await ds.change_presence(status=discord.Status.online, activity=discord.Game("Minecraft"))

@ds.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clean(ctx, amount = 100):
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
			role = get(message.guild.roles, name = 'Игрок')
			await channel.send(author.mention + '** подал заявку на получение роли **' + role.mention)
			vanden = ds.get_user(451826240186351616)
			await vanden.send(author.mention + '** подал заявку на получение роли **' + role.mention)
			await vanden.send('**Текст:** `' + str(message.content) + '`')
		fsendchannel = message.channel
		fchannelforaccept = ds.get_channel(715184789858287636)
		print(str(fsendchannel) + str(fchannelforaccept.name))
		if fsendchannel == fchannelforaccept:
			author = message.author
			fchannel = ds.get_channel(713368052699365456)
			fauthor = message.author
			await fchannel.send(author.mention + '** подал жалобу **')
@ds.event
async def on_member_join(member):
    emojik1 = get(member.guild.emojis, name = "vk")
    emojik2 = get(member.guild.emojis, name = "twitch")
    channel = ds.get_channel(713305916044214292)
    emb = discord.Embed(colour = discord.Color.gold())
    emb.set_author(name = "Добро пожаловать в  официальный Discord \n канал проекта Diadem", icon_url=member.avatar_url)
    emb.add_field(name = '\u200b', value = f'''**В первую очередь рекомендуем получить**
**роль для доступа ко всем каналам**
**[:closed_lock_with_key:Получить роль](https://discord.gg/f3xQBsS)**

**Для комфортного времяпрепровождения**
**рекомендуем озокомиться с**
**[:clipboard:Правилами Discord](https://discord.gg/ABppM3S)**

**Полезные ссылки:**
{emojik1}[Группа Вк](https://vk.com/diadem.mine)
{emojik1}[Правила Проекта](https://vk.com/@diadem.mine-project-rules)
{emojik2}[Twitch](https://www.twitch.tv/d1adem_)''')
    emb.set_thumbnail(url = 'https://media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif')
    role = get(member.guild.roles, name = 'Без роли')
    await member.add_roles(role)
    await channel.send(f'**Приветствую тебя, {member.mention}! :wave:**')
    await channel.send(embed = emb)
@ds.event
async def on_voice_state_update(member,before,after):
    if after.channel.id == 718359790778318918:
        for guild in ds.guilds:
            if guild.id == 701453861679792195:
                mainCategory = discord.utils.get(guild.categories, id=718359671403970620)
                channel2 = await guild.create_voice_channel(name=f"{member.display_name}",category=mainCategory)
                await member.move_to(channel2)
                await channel2.set_permissions(member,manage_channels=True)
                def check(a,b,c):
                    return len(channel2.members) == 0
                await ds.wait_for('voice_state_update', check=check)
                await channel2.delete()



@ds.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def answer(ctx, arg, member: discord.Member):
	#Жалоба рассмотрена. Нарушитель понёс наказание. n
	#Благодарим Вас за ваше обращение!:thumbsup_tone1:
	channel = ds.get_channel(715184789858287636)
	await channel.send(member.mention)
	if arg == "1":
		emb = discord.Embed(colour = discord.Color.green())
		emb.set_author(name = "Жалоба рассмотрена. Нарушитель понёс наказание.", icon_url= member.avatar_url)
		emb.set_thumbnail(url = "https://media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif")
		emb.add_field(name = "\u200b", value = """*⁣Благодарим Вас за ваше обращение!*⁣:thumbsup_tone1:""")
		await channel.send(embed = emb)
	elif arg == "2":
		emb = discord.Embed(colour = discord.Color.green())
		emb.set_author(name = "Жалоба рассмотрена. Всё ваше имущество восстановлено,  нарушитель понёс наказание.", icon_url= member.avatar_url)
		emb.set_thumbnail(url = "https://media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif")
		emb.add_field(name = "\u200b", value = """*Благодарим Вас за ваше обращение!*:thumbsup_tone1:""")
		await channel.send(embed = emb)
	elif arg == "3":
		emb = discord.Embed(colour = discord.Color.green())
		emb.set_author(name = "⁣Жалоба рассмотрена. Игрок, на которого была подана вами жалоба, получил сообщение от члена админ.состава с целью вернуть вещи/предоставить дополнительную информацию. ⁣", icon_url= member.avatar_url)
		emb.set_thumbnail(url = "https://media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif")
		emb.add_field(name = "\u200b", value = """*Благодарим Вас за ваше обращение!*⁣:thumbsup_tone1:""")
		await channel.send(embed = emb)
	elif arg == "4":
		emb = discord.Embed(colour = discord.Color.red())
		emb.set_author(name = "Отказ в рассмотрении жалобы.\nВозможные причины: «жалоба не по форме»,«нехватка/фальсификация улик».", icon_url= member.avatar_url)
		emb.set_thumbnail(url = "https://media.discordapp.net/attachments/713367810985689110/714404218777239614/anim.gif")
		emb.add_field(name = "\u200b", value = """*Рекомендуем вам пересмотреть свою жалобу.*""")
		await channel.send(embed = emb)

token = os.environ.get("BOT_TOKEN")

ds.run(token)
