
import console

try:
	import discord
	from discord.ext import commands
	import G as I
	import os
	import asyncio
	import json
	import openfile as o


	class Zero(commands.Cog):

		def __init__(self, bot):
			self.bot=bot

		@commands.command(aliases=['зеро'])
		@commands.is_owner()
		async def zero(self, ctx, *, MoC:str, AdvArgs=None):
			MANA=int(o.u.opjsfi(f'Stats/Mana/{ctx.author.id}.json', 'r', 'MANA'))
			STMANA=int(I.y.imp('manaStandart'))
			TALL=int(I.y.imp('manaTall'))
			AVERAGE=int(I.y.imp('manaAverage'))
			SMALL=int(I.y.imp('manaSmall'))
			MINIMUM=int(I.y.imp('manaMinimum'))
			CRITICAL=int(I.y.imp('manaCritical'))
			recTA=125000
			recAV=77000
			recSM=53000
			#  MAGIC

			#  ОТМЕНА МАГИИ
			if (MoC=='Отмена магии') or (MoC=='отмена магии'):
				if int(MANA)>int(TALL) and (int(MANA)>recTA):
					I.y.rm(ctx, 120000)
					await ctx.reply('Полная отмена магии на 1500 секунд(25 минут)')
					DumpsJS=json.dumps({"MAGIC":"False"}, indent=4, sort_keys=True)
					with open(f'Stats/Mana/MagO.json', 'w') as OtFalse: OtFalse.write(DumpsJS)
					await asyncio.sleep(1200)
					DumpsJS=json.dumps({"MAGIC":"True"}, indent=4, sort_keys=True)
					with open(f'Stats/Mana/MagO.json', 'w') as OtTrue: OtTrue.write(DumpsJS)
				if int(MANA)>int(AVERAGE) and (int(MANA)>recAV):
					I.y.rm(ctx, 72000)
					await ctx.reply('Полная отмена магии на 900 секунд(15 минут)')
					DumpsJS=json.dumps({"MAGIC":"False"}, indent=4, sort_keys=True)
					with open(f'Stats/Mana/MagO.json', 'w') as OtFalse: OtFalse.write(DumpsJS)
					await asyncio.sleep(900)
					DumpsJS=json.dumps({"MAGIC":"True"}, indent=4, sort_keys=True)
					with open(f'Stats/Mana/MagO.json', 'w') as OtTrue: OtTrue.write(DumpsJS)
				if int(MANA)>int(SMALL) and (int(MANA)>recSM):
					I.y.rm(ctx, 48000)
					await ctx.reply('Полная отмена магии на 600 секунд(10 минут)')
					DumpsJS=json.dumps({"MAGIC":"False"}, indent=4, sort_keys=True)
					with open(f'Stats/Mana/MagO.json', 'w') as OtFalse: OtFalse.write(DumpsJS)
					await asyncio.sleep(900)
					DumpsJS=json.dumps({"MAGIC":"True"}, indent=4, sort_keys=True)
					with open(f'Stats/Mana/MagO.json', 'w') as OtTrue: OtTrue.write(DumpsJS)
				else:
					await ctx.reply('**!! У тебя слишком мало Маны для этой магии !!**')

			#  ЗАКЛИНАНИЕ
			# elif (MoC=='Заклинание') or (MoC=='заклинание'):
			# 	if AdvArgs==None: await ctx.reply('**Ты не указал на кого наложить заклинание**')
			# 		o.u.opjsfi(f'Stats/Mana/UsStats/Char/{ctx.author.id}.json', 'w', words={"CHAR":"None"})
			# 		if int(MANA)>int(TALL) and (int(MANA)>recTA):
			# 			ResMn=int(MANA)-43000
			# 			ResMnJ={"MANA":f"{ResMn}"}
			# 			o.u.opjsfi(f'Stats/Mana/{ctx.author.id}.json', 'w', words={"MANA":f"{ResMn}"})
			# 		if int(MANA)>int(AVERAGE) and (int(MANA)>recAV):
			# 			ResMn=int(MANA)-25800
			# 			ResMnJ={"MANA":f"{ResMn}"}
			# 			o.u.opjsfi(f'Stats/Mana/{ctx.author.id}.json', 'w', words={"MANA":f"{ResMn}"})
			# 		if int(MANA)>int(SMALL) and (int(MANA)>recSM):
			# 			ResMn=int(MANA)-17200
			# 			o.u.opjsfi(f'Stats/Mana/{ctx.author.id}.json', 'w', words={"MANA":f"{ResMn}"})

			#  СНЯТИЕ ЗАКЛИНАНИЯ
			elif (mag_or_char=='Снять заклинания') or (mag_or_char=='снять заклинания'):
				if AdvArgs==None: await ctx.reply('**Ты не указал с кого снять заклинание**')
				elif AdvArgs==None: await ctx.reply('**Ты не указал с кого снять заклинание**')
				elif AdvArgs==None: await ctx.reply('**Ты не указал с кого снять заклинание**')
				else:
					o.u.opjsfi(f'Stats/Mana/UsStats/Char/{ctx.author.id}.json', 'w', words={"CHAR":"None"})
					if int(MANA)>int(TALL) and (int(MANA)>recTA):
						ResMn=int(MANA)-33000
						ResMnJ={"MANA":f"{ResMn}"}
						o.u.opjsfi(f'Stats/Mana/{ctx.author.id}.json', 'w', words=ResMnJ)
					if int(MANA)>int(AVERAGE) and (int(MANA)>recAV):
						ResMn=int(MANA)-19800
						ResMnJ={"MANA":f"{ResMn}"}
						o.u.opjsfi(f'Stats/Mana/{ctx.author.id}.json', 'w', words=ResMnJ)
					if int(MANA)>int(SMALL) and (int(MANA)>recSM):
						ResMn=int(MANA)-13200
						ResMnJ={"MANA":f"{ResMn}"}
						o.u.opjsfi(f'Stats/Mana/{ctx.author.id}.json', 'w', words=ResMnJ)

	async def setup(bot):
		try:
			await bot.add_cog(Zero(bot))
			console.info('[COGS]> zero.py                       OK')
		except BaseException:
			console.error('[COGS]> zero.py                    ERROR')
except BaseException:
	pass
