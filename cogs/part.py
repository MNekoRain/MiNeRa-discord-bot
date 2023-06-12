import discord
from discord.ext import commands
import datetime
import console


class Part(commands.Cog):

	def __init__(self, bot):
		self.bot=bot

	@commands.Cog.listener()
	async def on_member_remove(self, member):
		now=datetime.datetime.now()
		t=now.strftime("[%Y] [%B %d] [%A %w] [%d] [%H:%M:%S]")
		channel=self.bot.get_channel(901612783609741333)
		AntPar=discord.Embed(colour=0xFF4646)
		AntPar.add_field(name=  "**❗📝❗│ Партнерство разорвано │❗📝❗**",
						 value= f"**Партнерство заключенное пользователем {member.mention} было разорвано!**\n**Причина:** *Нарушение условий(Выход с сервера)*")
		ParKorr=discord.Embed(colour=0xFF4646)
		ParKorr.add_field(name=  "**❗📝❗│ Коралл Блин... │❓**",
						 value= f"**<@!859059274571579412>, Кораллец вышел**\n**Может сделаешь что-то с этим?**")
		# msIDtest=935481101391106098
		# chIDtest=915660782526660704
		# if member.id == 806152760650498059:
		# 	print("[PARTNER]> ")
		# 	await self.bot.http.delete_message(chIDtest, msIDtest)


#   БОЛЬШИЕ СЕРВЕРА

		# msIDL1=

		# chIDL=921368813801439282

		# if member.id == 806152760650498059:
		# 	print(f"[PARTNER]> Партнерство с {member} разорвано")
		# 	print(f"[PARTNER]> ")
		# 	print(f"[PARTNER]> {t}")
		# 	await self.bot.http.delete_message(chIDL, msIDL1)
		# 	await channel.send(embed=AntPar)


#   СРЕДНИЕ СЕРВЕРА

		msIDM1=934755567342321675

		chIDM=921368880868380702

		if member.id == 854243688955510784:
			console.info(f"[PARTNER]> Партнерство с {member} разорвано")
			console.info(f"[PARTNER]> Сервер: Рашн Хата")
			console.info(f"[PARTNER]> {t}")
			await self.bot.http.delete_message(chIDM, msIDM1)
			await channel.send(embed=AntPar)


#   МАЛЕНЬКИЕ СЕРВЕРА

		msIDS2=928025873033089045

		chIDS=921368934849056779

		if member.id == 771115370651189288:
			console.info(f"[PARTNER]> Партнерство с {member} разорвано ERROR")
			console.info(f"[PARTNER]> ")
			console.info(f"[PARTNER]> {t}")
			# await self.bot.http.delete_message(chIDS, msIDS1)
			await channel.send(embed=ParKorr)
		if member.id == 860875700071432243:
			console.info(f"[PARTNER]> Партнерство с {member} разорвано ERROR")
			console.info(f"[PARTNER]> ")
			console.info(f"[PARTNER]> {t}")
			await self.bot.http.delete_message(chIDS, msIDS2)
			await channel.send(embed=AntPar)

async def setup(bot):
	try:
		await bot.add_cog(Part(bot))
		console.warn('[COGS]> part.py              DEACTIVATED')
	except BaseException:
		console.error('[COGS]> pern.py                    ERROR')