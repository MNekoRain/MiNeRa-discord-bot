import discord
from discord.ext import commands
import random
import asyncio
import json
import console


class Word(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		with open('Stats/RAIN.json', 'r') as NRR:
			nr = json.loads(NRR.read())
		if nr["RESPONSING"] == "FALSE":
			console.error('[NOTRESPONSIN]> word.py')
		else:
			with open('Stats/Noric.json', 'r') as RRR:
				rtt = json.loads(RRR.read())
			if rtt['Noric'] == 'NO':
				if isinstance(message.channel, discord.channel.DMChannel):
					return
				else:
					async def send_message_emb(self, channel, ember):
						channel = self.bot.get_channel(channel)
						await channel.send(embed=ember)
					meco = message.content
					mcst = message.content.startswith
					mcen = message.content.endswith
					dug = discord.utils.get
					mgg = message.guild.get_role
					mgr = message.guild.roles
					yes = ['да', 'Да', 'ДА', 'дА', 'yes', 'Yes', 'YEs', 'YES', 'yES', 'yeS', 'yEs', 'YeS']
					yeso = ['Нет', 'Net', 'теН', 'teN', 'No', 'oN', 'Да', 'аД', 'Yes', 'seY', 'Что?', 'Зачем', 'Все понятно...', 'Ы', 'Da', 'aD']
					no = ['нет', 'Нет', 'НЕт', 'НЕТ', 'нЕТ', 'неТ', 'нЕт', 'НеТ', 'no', 'No', 'NO', 'nO']
					noo = ['Да', 'Da', 'аД', 'aD', 'Yes', 'seY', 'Нет', 'теН', 'No', 'oN', 'Ммм', 'Ага', 'Угу', 'Вычеркиваем...', 'А?', 'Jir']
					uid = ['О Rain', 'О Райн', 'О райн', 'О rain', 'о райн', 'о rain', 'орайн', 'orain']
					uiv = ['О Drakon4ik', 'О Драконе', 'О драконе', 'О drakon4ik', 'о драконе', 'о drakon4ik', 'одрак', 'odrak']
					pings = ['@everyone', '@here']
					ld = ['<@']
					ir = ['>']
					anikin = [899316511028678766, 899340430041284628, 899767792184750091]
					ignch = [901207485891903532, 901207656956567612, 901117204345528391, 901115728818761778,
								901113619956269116, 909834180907651073, 909826855140466718, 909842936034906152,
								910943103341428806, 901162955201204244, 901163991332700231, 912061048901759057,
								901164537150062632, 901165571800965200, 903007174027006032, 903007826618769508,
								925694133870424154, 921368813801439282, 921368880868380702, 921368934849056779,
								902500334759460884, 902855169799245835, 902853803966083122, 902853677411360828,
								902853304797765643, 902852286462693416, 919622004322222130, 919622718196969492,
								919623812155322418]
					ichid = [901113619956269116, 901117204345528391, 901207485891903532, 901207656956567612, 909826855140466718, 909834180907651073, 909842936034906152, 910943103341428806, 901162955201204244, 901163991332700231, 912061048901759057, 901164537150062632,
							 903007174027006032, 903007826618769508]
					ignuser = [618426320535420938, 859059274571579412, 822482518015213568, 665631306905944075, 738618208025837642]
					bwid= [310848622642069504, 901207485891903532, 720351927581278219]

					NANGELR= dug(mgr, name="▶💫◀ АНГЕЛ")
					Nown= dug(mgr, name="[ Oсновательツ ]")
					Nown2= dug(mgr, name="2.0")
					NangelR= dug(mgr, name="◢💫◣ Ангел")
					NdandelR= dug(mgr, name='◥💫◤ Ангельское "Детя"')
					NkangelR= dug(mgr, name="◀💫▶ Падший Ангел")
					NkdangelR= dug(mgr, name='◁💫▷ Падшее Ангельское "Детя"')
					NGenAdminR= dug(mgr, name="🛡┆Выс.Администрация")
					NTehAdminR= dug(mgr, name="🔨┆Тех.Админ")
					NGenModerR= dug(mgr, name="💠┆Главный Модератор")
					NModerR= dug(mgr, name="⚔┆Модератор")
					NHelperR= dug(mgr, name="💦┆ H e l p e r")

					ANGELR= mgg(929151362833465446)
					own= mgg(901196946478358589)
					own2= mgg(928273002418806834)
					angelR= mgg(921447482507026472)
					dangelR= mgg(928740868448485427)
					kangelR= mgg(923096456867512391)
					kdangelR= mgg(928744889196367913)
					GenAdminR= mgg(901189786012876800)
					TehAdminR= mgg(901189982780293131)
					GenModerR= mgg(916380887426420766)
					ModerR= mgg(901193698489024533)
					HelperR= mgg(901194203021856778)
					RolePing= [ANGELR, own, own2, angelR, dangelR, kangelR, kdangelR]
					IgnRoles= [ANGELR, own, own2, angelR, dangelR, kangelR, kdangelR, GenAdminR, TehAdminR, GenModerR]
					if message.guild.id == 825068295840596040:
						return
					if message.guild.id == 825068295840596040:
						return
					if message.channel.id in ichID:
						if message.author==self.bot.user or message.author.id in BWid:
							return console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						if message.author.id in ignUser:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						elif angelR in message.author.roles:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						elif dangelR in message.author.roles:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						elif kangelR in message.author.roles:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						elif kdangelR in message.author.roles:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						elif GenAdminR in message.author.roles:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						elif TehAdminR in message.author.roles:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						elif GenModerR in message.author.roles:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						elif ModerR in message.author.roles:
							console.info(f"[IGNORING]> {message.author}\n[IGNORING]> {message.author.id}\n[IGNORING]> {message.guild.name}\n[IGNORING]> {message.guild.id}\n[IGNORING]> {message.channel.name}\n[IGNORING]> {message.channel.id}")
						else:
							await message.delete()
							channel=936226512762437652
							ember=discord.Embed(colour=0xFF9933)
							ember.add_field(name="⚠│ Ошибка │⚠", value=f"**Произошла ошибка**\n**Сообщение написанное на сервере {message.guild.name} удалено**\n**Причина: У пользователя нет подходящей роли/Сообщение написано в запрещенном для него канале**\n**Подробности в терминале**")
							asyncio.run_coroutine_threadsafe(send_message_emb(self, channel, ember), self.bot.loop)
							console.info(f"[DELETED]> Сообщение от {message.author} удалено\n[DELETED]> {message.author.id}\n[DELETED]> {message.guild.name}\n[DELETED]> {message.guild.id}\n[DELETED]> {message.channel.name}\n[DELETED]> {message.channel.id}")
					if message.author == self.bot.user:
						return
					if message.guild.id == 886289090411118653:
						if message.channel.id == 886697334426177607:
							return
						if message.channel.id in AniKin:
							return
						else:
							channel = 936226512762437652
							ember = discord.Embed(colour=0xFF9933)
							ember.add_field(name="⚠│ Ошибка │⚠", value=f"**Произошла ошибка**\n**Сообщение было написано на сервере {message.guild.name}**\n**В канале [ {message.channel.name} ] `{message.channel.id}`**\n**Подробности в терминале**")
							asyncio.run_coroutine_threadsafe(send_message_emb(self, channel, ember), self.bot.loop)
							return
					elif meco in yes:
						ry = random.randrange(1, 16)
						if ry == 1:
							await message.channel.send("Нет")
						elif ry == 2:
							await message.channel.send("Net")
						elif ry == 3:
							await message.channel.send("теН")
						elif ry == 4:
							await message.channel.send("teN")
						elif ry == 5:
							await message.channel.send("No")
						elif ry == 6:
							await message.channel.send("oN")
						elif ry == 7:
							await message.channel.send("Да")
						elif ry == 8:
							await message.channel.send("аД")
						elif ry == 9:
							await message.channel.send("Yes")
						elif ry == 10:
							await message.channel.send("seY")
						elif ry == 11:
							await message.channel.send("Что?")
						elif ry == 12:
							await message.channel.send("Зачем")
						elif ry == 13:
							await message.channel.send("Все понятно...")
						elif ry == 14:
							await message.channel.send("Ыыыы")
						elif ry == 15:
							await message.channel.send("Da")
						elif ry == 16:
							await message.channel.send("aD")
					elif meco in no:
						ry = random.randrange(1, 16)
						if ry == 1:
							await message.channel.send("Да")
						elif ry == 2:
							await message.channel.send("Da")
						elif ry == 3:
							await message.channel.send("аД")
						elif ry == 4:
							await message.channel.send("aD")
						elif ry == 5:
							await message.channel.send("Yes")
						elif ry == 6:
							await message.channel.send("seY")
						elif ry == 7:
							await message.channel.send("Нет")
						elif ry == 8:
							await message.channel.send("теН")
						elif ry == 9:
							await message.channel.send("No")
						elif ry == 10:
							await message.channel.send("oN")
						elif ry == 11:
							await message.channel.send("Ммм")
						elif ry == 12:
							await message.channel.send("Ага)")
						elif ry == 13:
							await message.channel.send("Угу")
						elif ry == 14:
							await message.channel.send("Вычеркиваем...")
						elif ry == 15:
							await message.channel.send("А?")
						elif ry == 16:
							await message.channel.send("Jir")
					elif meco in uid:
						embuid = discord.Embed()
						embuid.add_field(name='**Ник**',     value='*Rain*')
						embuid.add_field(name='**Имя**',     value='*Даша*')
						embuid.add_field(name='**Возраст**', value='*14*')
						embuid.add_field(name='**Пол**',     value='*Девушка*')
						await message.channel.send(embed=embuid)
					elif meco in uiv:
						embuiv = discord.Embed()
						embuiv.add_field(name='**Ник**',     value='*𝕯𝖗𝖆𝖌𝖔𝖓4𝖎𝖐 シ*')
						embuiv.add_field(name='**Имя**',     value='*Влад*')
						embuiv.add_field(name='**Возраст**', value='*13*')
						embuiv.add_field(name='**Пол**',     value='*Мужчина*')
						await message.channel.send(embed=embuiv)
					elif meco in ld and meco in ir:
						chid = [915660782526660706]
						if message.channel.id in chid:
							return console.error("[ERRORMENTION]> Канал с упоминанием запрещен для меня")
						else:
							await message.channel.send(f"{message.author.name}, Не пингуй плiз")
							# await message.author.send("Можно вопрос?\nЗачем ты пингуешь?)")
					elif meco in pings:
						chid = [915660782526660706]
						for role in message.author.roles:
							if role.permissions.administrator:
								return
						if message.channel.id in chid:
							return
						else:
							await message.delete()
							await message.channel.send("**Пинги __everyone__ и __here__ запрещены для тебя!**")
				

async def setup(bot):
	try:
		await bot.add_cog(Word(bot))
		console.info('[COGS]> word.py                       OK')
	except BaseException:
		console.error('[COGS]> word.py                    ERROR')