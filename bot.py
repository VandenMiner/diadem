

from discord.ext import commands
from discord.utils import get
import os
import discord
import asyncio



ds = commands.Bot(command_prefix='.')
@ds.event
async def on_ready():
    await ds.change_presence(status=discord.Status.online, activity=discord.Game("БЭБРИКИ ЛУЧШИЕ!"))
    print("Запуск")

@ds.command(pass_context = True)
async def set(ctx, boss, hours, minutes):
	if int(minutes) <= 10 and int(hours) < 1:
		await ctx.channel.send(f"""Выставленно значение времени для босса **{boss}**
Часов: **{hours}** 
Минут: **{minutes}**""")
		time = int(minutes)*60
		print(str(time))
		await asyncio.sleep(time - 60)
		await ctx.channel.send(f"<@everyone>\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~<@everyone>\nВНИМАНИЕ! до босса **{boss}** осталось **1 минута**!\n<@everyone>\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~<@everyone>")
	else:
		await ctx.channel.send(f"""Выставленно значение времени для босса **{boss}**
Часов: **{hours}** 
Минут: **{minutes}**""")
		time = int(hours)*3600 + int(minutes)*60
		print(str(time))
		await asyncio.sleep(time - 600)
		await ctx.channel.send(f"<@everyone>\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~<@everyone>\nДо босса **{boss}** осталось **10 минут**!\n<@everyone>\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~<@everyone>")
		await asyncio.sleep(540)
		await ctx.channel.send(f"<@everyone>\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~<@everyone>\nВНИМАНИЕ! до босса **{boss}** осталось **1 минута**!\n<@everyone>\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~<@everyone>")
@ds.command(pass_context = True)


async def бустерденег(ctx):
	await ctx.channel.purge(limit = 1)
	await ctx.channel.send("@everyone")
	emb = discord.Embed()
	emb.colour = discord.Colour.lighter_gray()
	emb.add_field(name = f"Бустер", value = """_Был активирован глобальный бустер денег на 20 минут!_
**Заходи в игру!**""")
	emb.set_thumbnail(url = "https://avatanplus.com/files/resources/original/58ca980ab666015ad761e9fb.png")
	await ctx.channel.send(embed = emb)
	await ctx.channel.send("@everyone")
@ds.command(pass_context = True)
async def бустершардов(ctx):
	await ctx.channel.purge(limit = 1)
	await ctx.channel.send("@everyone")
	emb = discord.Embed()
	emb.colour = discord.Colour.lighter_gray()
	emb.add_field(name = f"Бустер", value = """_Был активирован глобальный бустер шардов на 20 минут!_
**Заходи в игру!**""")
	await ctx.channel.send(embed = emb)
	await ctx.channel.send("@everyone")

@ds.command(pass_context=True)
async def accept(ctx, user):
	await ctx.channel.purge(limit = 1)
	await ctx.channel.send(user)
	emb = discord.Embed()
	emb.add_field(name = "---", value = """**Добро пожаловать в наш клан!**
Ваша заявка успешно рассмотрена, вы приняты в наш клан

Не забудьте, что не знание правил не освобождает от ответственности,
поэтому ознокомление обязательно - #📜правила📜


Также у нас есть свой бот, комманды которого вы можете узнать
введя комманду .info


""")	
	emb.set_thumbnail(url = "https://media.discordapp.net/attachments/663074528712327189/768176828137340998/unknown.png")
	emb.set_footer(text = """Вся подробная информация по вступлению публикуется в игровом чате""", icon_url="https://media.discordapp.net/attachments/663074528712327189/768176828137340998/unknown.png")
	emb.colour = discord.Colour.lighter_gray()
	await ctx.channel.send(embed = emb)

@ds.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def bclear(ctx):
	channelboss = ds.get_channel(764454544809656341)
	await channelboss.purge()



@ds.command(pass_context = True)
async def info(ctx):
	chpb = ds.get_channel(764454544809656341)
	events = ds.get_channel(767730491067334676)
	emb = discord.Embed()
	emb.add_field(name = "---", value = f"""**Информация по коммандам**
**Комманды:**

**.info** - Выводит всю информацию о доступных коммандах

_**Синтаксис:**_ (комманда)



**.set** - Задаёт время до респавна босса, в будущем оповестит вас в этом же канале

_**Синтаксис:**_ (комманда, часы до появления босса(при отсутвии - 0), минуты до появления босса)

_**Правило:**_ использовать только в канале **[Чпб](https://discord.gg/fVGm9Hw)**



**.бустерденег** - Выводит информацию для других игроков о появлении бустера денег

_**Синтаксис:**_ (комманда)

_**Правило:**_ использовать только при появлении бустера денег и только в текстовом канале **[Ивенты](https://discord.gg/JtKtGu3)**
""")	
	emb.set_thumbnail(url = "https://media.discordapp.net/attachments/663074528712327189/768176828137340998/unknown.png")
	emb.set_footer(text = """---""", icon_url="https://media.discordapp.net/attachments/663074528712327189/768176828137340998/unknown.png")
	emb.colour = discord.Colour.lighter_gray()
	await ctx.channel.send(embed = emb)

token = os.environ.get("BOT_TOKEN")

ds.run(token)
