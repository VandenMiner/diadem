

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
@commands.has_permissions(administrator = True)
async def bclear(ctx):
	channelboss = ds.get_channel(764454544809656341)
	await channelboss.purge()

token = os.environ.get("BOT_TOKEN")

ds.run(token)
