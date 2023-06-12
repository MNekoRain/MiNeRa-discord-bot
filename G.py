"""
Основной сборник действий для бота

Тестовый, рабочий сборник
"""
import discord
from discord.ext import commands
import json
import os
import asyncio
import openfile as o
import console

try:

	class Main():
	
		def __init__(self):
			self.ErExChID=952306160361414656

# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--= #
# =--=--=--=--=- НЕ ИСПОЛЬЗУЕТСЯ --=--=--=--=--= #
# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--= #
#
#	def Glanguage(ctx):
#		"""Функция поиска файла с языком\n
#		\n
#		Используется только для бота
#		"""
#		mgid=str(ctx.guild.id)
#		for filename in os.listdir("./LANGUAGE"):
#			if filename.endswith(f"{mgid}.json"):
#				print('> 1')
#				with open(f'LANGUAGE/{mgid}.json','r') as GlangC:
#					lreadc=GlangC.read()
#				lc=json.loads(lreadc)
#				lg=lc["Language"]
#				lg=o.OpenFileOnlyJson.opjsfi(way=f'LANGUAGE/{mgid}.json', mode='r', index="Language")
#				print('> {} <[1]> {}'.format(mgid,lg))
#				return lg
#			elif not filename.endswith(f"{mgid}.json"):
#				print('> ')
#				continue
#			else:
#				print('> 2')
#				with open('LANGUAGE/deflanguage.json','r') as GlangD:
#					lreadd=GlangD.read()
#				ld=json.loads(lreadd)
#				lg=ld["Language"]
#				lg=o.OpenFileOnlyJson.opjsfi(way='LANGUAGE/deflanguage.json', mode='r', index="Language")
#				print('> {} <[2]> {}'.format(mgid,lg))
#				return lg
#
#
#	def fLanguage(ctx):
#		"""Функция определения языка\n
#		\n
#		Используется только для бота
#		"""
#		print('>> 1')
#		res=Glanguage(ctx)
#		print('>> 2')
#		ru='ru'
#		en='en'
#		uk='uk'
#		if res=='ru':
#			return ru
#		elif res=='en':
#			return en
#		elif res=='uk':
#			return uk
#		else:
#			return print('> Я не понимать ваш язык')
#
#
#	def prf(ctx):
#		"""Функция поиска файла с префиксом\n
#		\n
#		Используется только для бота
#		"""
#		print('> 35')
#		mi=str(ctx.guild.id)
#		ll=fLanguage(ctx)
#		for filename in os.listdir("./LANGUAGE/ComLan"):
#			if filename.endswith(f"ComLang.json") and ll=='ru':
#				print('> 36')
#				with open(f'LANGUAGE/ComLan/ComLang.json','r') as GlangRu:
#					lreadru=GlangRu.read()
#				lr=json.loads(lreadru)
#				lr=o.OpenFileOnlyJson.opjsfi(way='LANGUAGE/ComLan/ComLang.json', mode='r', index="RUS")
#				for ru in lr:
#					print('> 37')
#					p1=ru["1"]
#					p2=ru["2"]
#					p3=ru["3"]
#				return p1,p2,p3
#			elif filename.endswith(f"ComLang.json") and ll=='en':
#				with open(f'LANGUAGE/ComLan/ComLang.json','r') as GlangRu:
#					lreadru=GlangRu.read()
#				lr=json.loads(lreadru)
#				lr=o.OpenFileOnlyJson.opjsfi(way='LANGUAGE/ComLan/ComLang.json', mode='r', index="ENG")
#				for ru in lr:
#					p1=ru["1"]
#					p2=ru["2"]
#					p3=ru["3"]
#				return p1,p2,p3
#			elif filename.endswith(f"ComLang.json") and ll=='uk':
#				with open(f'LANGUAGE/ComLan/ComLang.json','r') as GlangRu:
#					lreadru=GlangRu.read()
#				lr=json.loads(lreadru)
#				lr=o.OpenFileOnlyJson.opjsfi(way='LANGUAGE/ComLan/ComLang.json', mode='r', index="UKR")
#				for ru in lr:
#					p1=ru["1"]
#					p2=ru["2"]
#					p3=ru["3"]
#				return p1,p2,p3
#			elif not filename.endswith(f"{mi}.json") and ll=='ru':
#				continue
#
#
# ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^ #
# =--=--=--=--=--=--=--=--=--=--=--=--=--=--=--= #



		def imp(self, imptype:str):
			"""Импорт всех необходимых данных\n
			\n
			imp(self, imptype)"""

			with open("config.json", "r") as f:
				cfgjs=f.read()
			cfg=json.loads(cfgjs)
			with open('PREFIXES/defprefix.json','r') as dp:
				dpJ=dp.read()
			defp=json.loads(dpJ)
			with open('Stats/Mana/MANA.json','r') as mn:
				mnJ=mn.read()
			SMana=json.loads(mnJ)

			if imptype=='dfpref':
				dfp=defp["prefix"]
				return dfp

			elif imptype=='owne1':
				ow=int(cfg["OWNID"])
				return ow
			elif imptype=='owne2':
				own=int(cfg["OWNEID"])
				return own

			elif imptype=='drag1':
				dr=int(cfg["DRAGID"])
				return dr
			elif imptype=='drag2':
				dra=int(cfg["DRAGOID"])
				return dra

			elif imptype=='enot':
				en=int(cfg["ENOTID"])
				return en

			elif imptype=='dont':
				do=int(cfg["DONTID"])
				return do

			elif imptype=='token':
				token=cfg["TOKEN"]
				return token

			elif imptype=='prefix':
				pref=cfg["PREFIX"]
				return pref

			elif imptype=='manaTall':
				tamana=SMana["TALL"]
				return tamana

			elif imptype=='manaAverage':
				avmana=SMana["AVERAGE"]
				return avmana
				
			elif imptype=='manaSmall':
				smmana=SMana["SMALL"]
				return smmana

			elif imptype=='manaStandart':
				stmana=SMana["STANDART"]
				return stmana
				
			elif imptype=='manaMinimum':
				mimana=SMana["MINIMUM"]
				return mimana
				
			elif imptype=='manaCritical':
				crmana=SMana["CRITICAL"]
				return crmana

		def rm(ctx, mana:int):
			MANA=int(o.u.opjsfi(f'Stats/Mana/{ctx.author.id}.json', 'r', 'MANA'))
			ResMn=int(MANA)-mana
			ResMnJ={"MANA":f"{ResMn}"}
			DumpsJS=json.dumps(ResMnJ, indent=4, sort_keys=True)
			with open(f'Stats/Mana/{ctx.author.id}.json', 'w') as OtMana: OtMana.write(DumpsJS)

		def RATH(bot, stlT):
			if stlT=='pref':
				async def stl(bot):
					await bot.http.send_message(952306160361414656, '**Ошибка при загрузке файла с командами. Проблемный файл:** *pref.py*')
				return asyncio.run(stl(bot))

			elif stlT=='log':
				async def stl(bot):
					await bot.http.send_message(952306160361414656, '**Ошибка при загрузке файла с командами. Проблемный файл:** *log.py*')
				return asyncio.run(stl(bot))

			elif stlT=='oth':
				async def stl(bot):
					await bot.http.send_message(952306160361414656, '**Ошибка при загрузке файла с командами. Проблемный файл:** *oth.py*')
				return asyncio.run(stl(bot))

			elif stlT=='ready':
				async def stl(bot):
					await bot.http.send_message(952306160361414656, '**Ошибка при загрузке файла с командами. Проблемный файл:** *ready.py*')
				return asyncio.run(stl(bot))

			elif stlT=='lang':
				async def stl(bot):
					await bot.http.send_message(952306160361414656, '**Ошибка при загрузке файла с командами. Проблемный файл:** *lang.py*')
				return asyncio.run(stl(bot))
	
	y=Main()

except BaseException:
	console.error('File: G.py        Error: Произошла неизвестная ошибка')