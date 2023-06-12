import discord
import json
import console

class OpenFileOnlyJson:
	"""-= КОНСТРУКЦИЯ =-
	-----------
	\n
	h.u.{функция()} или h.OpenFileOnlyJson().{функция()}"""

	def __init__(self):
		pass

	def opjsfi(self, way, mode, index=None, words=None):
		"""-= КОНСТРУКЦИЯ =-
		-----------
		\n
		opjsfi(way, mode, index, *words)\n
		\n
		\n
		-= ПАРАМЕТРЫ =-
		----------- 
		\n
		way   - Путь к файлу\n
		mode  - Режим, действие(r, w, a, wr, ar)\n
		index - Индекс. Используется только при режиме чтения(r, wr, ar)\n
		words - Слова, записываемые в файл. Используется только в режиме записи, добавления(w, a, wr, ar)\n

		-= РЕЖИМЫ =-
		-----------
		\n
		r  - Чтение\n
		w  - Запись\n
		a  - Добавление\n
		wr - Чтение и Запись\n
		ar - Чтение и Добавление\n
		"""
		try:
			if mode=='r':
				try:
					if index==None: console.error('> ReadError: Файл по пути {} не может быть прочитан    Причина: Не указан "index"'.format(way))
					else:
						with open(way, 'r') as ReadFile: RR=json.loads(ReadFile.read())
						return RR[index]
				except BaseException:
					return console.error('Произошла ошибка')
			elif mode=='rAD':
				try:
					with open(way, 'r') as ReadFile: OpReFi=ReadFile.read()
					return OpReFi
				except BaseException:
					return console.error('Произошла ошибка')
			elif mode=='w':
				if words==None: console.error('Строка 51 - Ошибка')
				else:
					try:
						with open(way, 'w') as WriteFile: WriteFile.write(json.dumps(words, indent=4, sort_keys=True))
						return
					except BaseException:
						return console.error('Произошла ошибка')
			elif mode=='a':
				if words==None:
					console.error('Строка 63 - Ошибка')
				else:
					try:
						with open(way, 'a') as AddFile: AddFile.write(json.dumps(words, indent=4, sort_keys=True))
						return
					except BaseException:
							return console.error('Произошла ошибка')
			elif mode=='wr':
				try:
					if words==None: console.error('Строка 74 - Ошибка')
					elif index==None: console.error('WriteReadError: Файл по пути {} не может быть прочитан    Причина: Не указан "index"'.format(way))
					else:
						with open(way, 'w') as WriteFile: WriteFile.write(json.dumps(words, indent=4, sort_keys=True))
						with open(way, 'r') as ReadFile: RR=json.loads(ReadFile.read())
						return RR[index]
				except BaseException:
					return console.error('Произошла ошибка')
			elif mode=='ar':
				try:
					if words==None: console.error('Строка 90 - Ошибка')
					if index==None: console.error('AddReadError: Файл по пути {} не может быть прочитан    Причина: Не указан "index"'.format(way))
					else:
						with open(way, 'a') as AddFile: AddFile.write(json.dumps(words, indent=4, sort_keys=True))
						with open(way, 'r') as ReadFile: RR=json.loads(ReadFile.read())
						return RR[index]
				except BaseException:
					return console.error('Произошла ошибка')
			else:
				return console.error('ModeError: Данный тип чтения/добавления/записи недопустимо')
		except BaseException:
			return console.error('Error: Произошла ошибка')

u=OpenFileOnlyJson()