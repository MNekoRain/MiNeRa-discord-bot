import discord
from discord.ext import commands
import asyncio
import json
import pytimeparse
import console


class Tim(commands.Cog):

	def __init__(self, bot):
		self.bot=bot


	@commands.command()
	async def time(self, ctx, time):
		with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
		if NR["RESPONSING"] == "FALSE":
			console.error('[NOTRESPONSIN]> tim.py')
			nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
			await ctx.reply(embed=nremb)
		else:
			PR=pytimeparse.parse(time)
			await ctx.send(f"**Будет** *{PR} секунд*")

	@commands.command()
	async def trava(self, ctx):
		with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
		if NR["RESPONSING"] == "FALSE":
			console.error('[NOTRESPONSIN]> tim.py')
			nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
			await ctx.reply(embed=nremb)
		else:
			await ctx.send(f"К-к-к-к-рабик")

async def setup(bot):
	try:
		await bot.add_cog(Tim(bot))
		console.info('[COGS]> tim.py                        OK')
	except BaseException:
		console.error('[COGS]> tim.py                     ERROR')