import discord
from discord.ext import commands
import openfile as o
import os
import console


class WelBye(commands.Cog):

	def __init__(self, bot):
		self.bot=bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel=self.bot.get_channel(915660782350532625)
		embwc=discord.Embed(title=  	 "**👋│ Добро Пожаловать │👋**",
							description= f"**Привет {member.mention}**",
							colour= 	 0x4242FF,
							url=member.avatar_url)
		embwc.add_field(name=  f"**Ты пришел на сервер {member.guild.name}**",
					    value= f"**Не забудь прочитать [Правила](https://discord.gg/eRgwtHHWeT)**\n**Канал для общения [тут](https://discord.gg/3X3rkE6wvj)**")
		embwc.set_image(url='https://a.radikal.ru/a25/2201/15/cf1ac127b38d.gif')
		await channel.send(embed=embwc)
		WarnJsonFileFT={
			"USERNAME":"{}",
			"WARNCOUNT":"0"
		}
		o.u.opjsfi(f'Stats/Warns/{member.guild.id}/{member.id}.json', 'w', words=WarnJsonFileFT)

	async def on_member_remove(self, member):
		channel=self.bot.get_channel(915660782350532626)
		embgb=discord.Embed(title=  	 "**👋│ Прощай │👋**",
							description= f"**Пока {member.mention}, надеемся ты снова зайдешь на наш сервер, или отыщешь новый :3**",
							colour= 	 0x4242FF)
		embgb.add_field(name=  "**Не забыл оставить отзыв? ;D**",
					    value= "**Ладео, __Желаем тебе удачи)__**")
		embgb.set_image(url='https://a.radikal.ru/a40/2201/cd/485fc050d3b2.gif')
		await channel.send(embed=embgb)
		os.remove(f'Stats/Warns/{member.guild.id}/{member.id}.json')

	# async def on_member_boost(self, member):
	# 	channel=self.bot.get_channel(915660782350532626)
	# 	embgb=discord.Embed(colour=0x4242FF)
	# 	embgb.add_field(name="**🚀│ Спасибо за буст │🚀"**,
	# 				   value=f"**{member.mention}, огромное спасибо тебе, за то, что помогаешь нашему серверу развиваться**\n**И продолжишь помогать нашему серверу!**")
	# 	embgb.set_image(url='https://d.radikal.ru/d08/2201/6f/03be812c0f8e.gif')
	# 	await channel.send(embed=embgb)


async def setup(bot):
	try:
		await bot.add_cog(WelBye(bot))
		console.info('[COGS]> welbye.py                     OK')
	except BaseException:
		console.error('[COGS]> welbye.py                  ERROR')