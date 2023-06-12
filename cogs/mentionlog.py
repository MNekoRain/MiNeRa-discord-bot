import discord
from discord.ext import commands
import datetime
import asyncio
import json
import random as r
import RuTi as Ran
import console


class MentionLOG(commands.Cog):

	def __init__(self, bot):
		self.bot=bot

	@commands.Cog.listener()
	async def on_message(self, message):
		with open('Stats/RAIN.json', 'r') as NRR:
			nr = json.loads(NRR.read())
		if nr["RESPONSING"] == "FALSE":
			console.error('[NOTRESPONSIN]> mentionlog.py')
		else:
			if self.bot.user.mentioned_in(message):
				with open('Stats/Noric.json', 'r') as RRR:
					rtt = json.loads(RRR.read())
				if rtt['Noric'] == 'NO':
					rw = ['Что тебе от меня нужно?', 'Нэ пингуй ;-;', 'Даааа что', 'Ты человек?', 'Вы бот?', 'Что тебе от меня нужно', 'Нэ пингуй ;-', 'Даааа чт', 'Ты человек?', 'Вы бот', 'Что тебе от меня нужн', 'Нэ пингуй ;', 'Даааа ч', 'Ты человек', 'Вы бо', 'Что тебе от меня нуж', 'Нэ пингуй', 'Даааа', 'Ты челове', 'Вы б', 'Что тебе от меня ну', 'Нэ пингу', 'Даааа', 'Ты челов', 'Вы', 'Что тебе от меня н', 'Нэ пинг', 'Ты чело', 'Что тебе от меня', 'Ты чел']
					ze = ['От тебя мне ничего не надо', 'Оцтань', 'Что?']
					on = ['***ПИНГ***', 'А йа буду', f'~~~~{message.author.mention}~~~~\n~~~~{message.author.mention}~~~~\n~~~~{message.author.mention}~~~~\n~~~~{message.author.mention}~~~~\n~~~~{message.author.mention}~~~~\n~~~~{message.author.mention}~~~~\n~~~~{message.author.mention}~~~~\n~~~~{message.author.mention}']
					tw = ['Нееет, ты ничто', 'Ничто', 'Привет']
					th = ['Вы бот', 'Вы животное', 'Я?']
					te = ['Вы человек?', 'Кто?', 'Ты?']
					zen = ['Да б##ть, что тебе надо?']
					onn = ['Йё###ый ПИНГГГГ']
					twn = ['С##а, что тебе надо?']
					thn = ['Нет б##ть извините, я КОМАР']
					ten = ['ДА, Я РОБОТ с##а']
					rr = r.randint(0, 100)
					rt = 'Y' if rr <= 95 else 'N'
					if message.content in (rw[0] or rw[5] or rw[10] or rw[15] or rw[20] or rw[25] or rw[28]):
						await message.reply(ze[r.randint(0, 2)] if rt == 'Y' else zen[0])
					if message.content in (rw[1] or rw[6] or rw[11] or rw[16] or rw[21] or rw[26]):
						await message.reply(on[r.randint(0, 2)] if rt == 'Y' else onn[0])
					if message.content in (rw[2] or rw[7] or rw[12] or rw[17] or rw[22]):
						await message.reply(tw[r.randint(0, 2)] if rt == 'Y' else twn[0])
					if message.content in (rw[3] or rw[8] or rw[13] or rw[18] or rw[23] or rw[27] or rw[29]):
						await message.reply(th[r.randint(0, 2)] if rt == 'Y' else thn[0])
					if message.content in (rw[4] or rw[9] or rw[14] or rw[19] or rw[24]):
						await message.reply(te[r.randint(0, 2)] if rt == 'Y' else ten[0])
					if message.author.bot:
						await message.send('Ботик бергамотик, что тебе от меня надо?')
					elif message.content not in rw:
						await message.reply(rw[r.randint(0, 4)])
				elif rtt['Noric'] == 'YES':
					return
			async def send_message_emb(channel, emblogg):
				ch = self.bot.get_channel(channel)
				await ch.send(embed=emblogg)
			mm = ['<@!618426320535420938>', '<@618426320535420938>', '<@!806152760650498059>', '<@806152760650498059>', '<@!859059274571579412>', '<@859059274571579412>', '<@!822482518015213568>', '<@822482518015213568>']
			chid = [928252550761832458, 915660782681878570, 915660782526660704]
			bwid = [310848622642069504, 901207485891903532, 720351927581278219]
			mg = message.guild
			mc = message.channel
			if message.content in mm:
				if message.author == self.bot.user:
					return
				if message.author.id in bwid:
					return
				if message.channel.id in chid:
					return
				if message.channel.id == 937635397834522625:
					return
				if message.channel.id == 901948229090938910:
					return
				if message.guild.id == 886289090411118653:
					channelid = 936226512762437652
					ember = discord.Embed(colour=0xFF9933)
					ember.add_field(name="⚠│ Ошибка │⚠", value=f"**Произошла ошибка**\n**Сообщение было написано на сервере {message.guild.name}**\n**Подробности в терминале**")
					return await self.bot.http.send_message(channelid, embed=ember)
				if message.channel.id == 901948229090938910 and ((message.author.id == 901951967788683355) or (message.author.id == 906884326178832384)):
					return
				else:
					if message.guild.id == 825068295840596040:
						return
					else:
						if message.author.id == 618426320535420938:
							console.info("[MENTION]> О мой создатель\n[MENTION]> Ты за чем пингуешь?")
							embmr = discord.Embed(colour=0xfd91ff)
							embmr.add_field(name="**⚠│ ПИНГ │⚠**", value="**К сожелению, некоторые пинги будут удалятся**\n*Rain, а точнее мой создатель, зачем ты пингуешь?)*")
							await message.channel.send(embed=embmr)
							await message.delete()
						elif message.author.id == 859059274571579412:
							console.info("[MENTION]> О боже...")
							embmd = discord.Embed(colour=0x3d2bff)
							embmd.add_field(name="**⚠│ ПИНГ │⚠**", value="**К сожелению, некоторые пинги будут удалятся**\n*Влад, зачем пингуешь?)*")
							await message.channel.send(embed=embmd)
							await message.delete()
						else:
							embma = discord.Embed(colour=0xc0eb34)
							embma.add_field(name="**⚠│ ПИНГ │⚠**", value="**К сожелению, некоторые пинги будут удалятся**")
							await message.channel.send(embed=embma)
							await message.delete()
			else:
				bid = [512227974893010954, 886700839757045811, 864912909809483836, 899590233077723206, 789751844821401630]
				if message.author.id == 914560181583638538:
					return
				if message.author.id in bid:
					return
				if (message.author.id == 912004004094046220) or (message.author.id == 980912659505483888):
					return
				channel = 937635397834522625
				now = datetime.datetime.now()
				wt, mt = await Ran.e.rt()
				td = now.strftime("[{}] [{} {}] [{} {}] [{}] [{}:{}:{}]".format("%Y", mt, "%d", wt, "%w", "%d", "%H", "%M", "%S"))
				if isinstance(message.reference, discord.message.MessageReference):
					msgid = message.reference.message_id
					try:
						msg = await message.channel.fetch_message(msgid)
					except discord.errors.NotFound:
						return console.error("[NOTFOUND]> Сообщение не найдено    mentionlod.py")
					if isinstance(message.channel, discord.channel.DMChannel):
						emblogg = discord.Embed(title="**💻│ ЛОГИ │💻**", description="**Сообщение написано**", colour=0x00eaff)
						emblogg.add_field(name="**Пользователь**", value=f"**{message.author.mention} ID: `{message.author.id}`**")
						emblogg.add_field(name="**Канал**", value=f"**ЛИЧНЫЕ СООБЩЕНИЯ**")
						emblogg.add_field(name="**Сервер**", value=f"**ЛИЧНЫЕ СООБЩЕНИЯ**")
						emblogg.add_field(name="**Содержание**", value=f"{message.content}")
						console.info("[MENTION]> Было отправлено сообщение в DM")
						console.info("[MENTION]> Пингов не обнаружено\n ")
						console.info(f"[LOG]> TIME:        {td}")
						console.info(f"[LOG]> MEMBERNAME:  {message.author.name}")
						console.info(f"[LOG]> MEMBERID:    {message.author.id}")
						console.info(f"[LOG]> RESMESSAGE:")
						console.log("> ")
						console.log(f"{msg.content}")
						console.log("> ")
						console.info(f"[LOG]> MESSAGEID: {message.id}")
						console.info(f"[LOG]> MESSAGE:")
						console.log("> ")
						console.log(f"{message.content}")
						console.log("> ")
						asyncio.run_coroutine_threadsafe(send_message_emb(channel, emblogg), self.bot.loop)

					else:
						emblogg = discord.Embed(title="**💻│ ЛОГИ │💻**", description="**Сообщение написано**", colour=0x00eaff)
						emblogg.add_field(name="**Пользователь**", value=f"**{message.author.mention} ID: `{message.author.id}`**")
						emblogg.add_field(name="**Канал**", value=f"**{message.channel.mention} ID: `{message.channel.id}`**")
						emblogg.add_field(name="**Сервер**", value=f"**{message.guild.name} ID: `{message.guild.id}`**")
						emblogg.add_field(name="**Содержание**", value=f"{message.content}")
						console.info("[MENTION]> Было отправлено сообщение")
						console.info("[MENTION]> Пингов не обнаружено\n ")
						console.info(f"[LOG]> TIME:        {td}")
						console.info(f"[LOG]> MEMBERNAME:  {message.author.name}")
						console.info(f"[LOG]> MEMBERID:    {message.author.id}")
						console.info(f"[LOG]> CHANNELNAME: {message.channel.name}")
						console.info(f"[LOG]> CHANNELID:   {message.channel.id}")
						console.info(f"[LOG]> SERVERNAME:  {message.guild.name}")
						console.info(f"[LOG]> SERVERID:    {message.guild.id}")
						console.info(f"[LOG]> RESMESSAGE:")
						console.log("> ")
						console.log(f"{msg.content}")
						console.log("> ")
						console.info(f"[LOG]> MESSAGEID: {message.id}")
						console.info(f"[LOG]> MESSAGE:")
						console.log("> ")
						console.log(f"{message.content}")
						console.log("> ")
						asyncio.run_coroutine_threadsafe(send_message_emb(channel, emblogg), self.bot.loop)

				else:
					if isinstance(message.channel, discord.channel.DMChannel):
						emblogg = discord.Embed(title="**💻│ ЛОГИ │💻**", description="**Сообщение написано**", colour=0x00eaff)
						emblogg.add_field(name="**Пользователь**", value=f"**{message.author.mention} ID: `{message.author.id}`**")
						emblogg.add_field(name="**Канал**", value=f"**ЛИЧНЫЕ СООБЩЕНИЯ**")
						emblogg.add_field(name="**Сервер**", value=f"**ЛИЧНЫЕ СООБЩЕНИЯ**")
						emblogg.add_field(name="**Содержание**", value=f"{message.content}")
						console.info("[MENTION]> Было отправлено сообщение в DM")
						console.info("[MENTION]> Пингов не обнаружено\n ")
						console.info(f"[LOG]> TIME:        {td}")
						console.info(f"[LOG]> MEMBERNAME:  {message.author.name}")
						console.info(f"[LOG]> MEMBERID:    {message.author.id}")
						console.info(f"[LOG]> MESSAGEID: {message.id}")
						console.info(f"[LOG]> MESSAGE:")
						console.log("> ")
						console.log(f"{message.content}")
						console.log("> ")
						asyncio.run_coroutine_threadsafe(send_message_emb(channel, emblogg), self.bot.loop)

					else:
						emblogg = discord.Embed(title="**💻│ ЛОГИ │💻**", description="**Сообщение написано**", colour=0x00eaff)
						emblogg.add_field(name="**Пользователь**", value=f"**{message.author.mention} ID: `{message.author.id}`**")
						emblogg.add_field(name="**Канал**", value=f"**{message.channel.mention} ID: `{message.channel.id}`**")
						emblogg.add_field(name="**Сервер**", value=f"**{message.guild.name} ID: `{message.guild.id}`**")
						emblogg.add_field(name="**Содержание**", value=f"{message.content}")
						console.info("[MENTION]> Было отправлено сообщение")
						console.info("[MENTION]> Пингов не обнаружено\n ")
						console.info(f"[LOG]> TIME:        {td}")
						console.info(f"[LOG]> MEMBERNAME:  {message.author.name}")
						console.info(f"[LOG]> MEMBERID:    {message.author.id}")
						console.info(f"[LOG]> CHANNELNAME: {message.channel.name}")
						console.info(f"[LOG]> CHANNELID:   {message.channel.id}")
						console.info(f"[LOG]> SERVERNAME:  {message.guild.name}")
						console.info(f"[LOG]> SERVERID:    {message.guild.id}")
						console.info(f"[LOG]> MESSAGEID: {message.id}")
						console.info(f"[LOG]> MESSAGE:")
						console.log("> ")
						console.log(f"{message.content}")
						console.log("> ")
						asyncio.run_coroutine_threadsafe(send_message_emb(channel, emblogg), self.bot.loop)

	@commands.command(aliases=['норик'])
	@commands.is_owner()
	async def noric(self, ctx):
		def n_file():
			with open('Stats/Noric.json', 'r') as RRR:
				rtt = json.loads(RRR.read())
			if rtt['Noric'] == 'NO':
				return 'YES'
			elif rtt['Noric'] == 'YES':
				return 'NO'
		ddd = {
			"Noric": f"{n_file()}"
		}
		with open('Stats/Noric.json', 'w') as DDT:
			DDT.write(json.dumps(ddd, indent=4, sort_keys=True))

async def setup(bot):
	try:
		await bot.add_cog(MentionLOG(bot))
		console.info('[COGS]> mentionlog.py                 OK')
	except BaseException:
		console.error('[COGS]> mentionlog.py              ERROR')
