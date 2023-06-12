import discord
from discord.ext import commands
import json
import console


class ReactWords(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('Stats/RAIN.json', 'r') as NRR:
            nr = json.loads(NRR.read())
        if nr["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> reactwords.py')
        else:
            if isinstance(message.channel, discord.channel.DMChannel):
                return
            else:
                if message.author == self.bot:
                    return
                if message.guild.id == 886289090411118653:
                    if message.channel.id == 886697334426177607:
                        return
                    elif message.channel.id != 886697334426177607:
                        return
                yes = ["да", "Да", "ДА", "yes", "Yes", "YES", "удалять"]
                no = ["нет", "Нет", "НЕТ", "no", "No", "NO", "не удалять", "Не удалять", "Не Удалять", "не Удалять", "НЕ УДАЛЯТЬ"]
                bwords = ["пид", "Пид", "ПИд", "ПИД", "пИД", "пиД", "ПиД", "пИд", "ебат", "Ебат", "ЕБат", "ЕБАт", "ЕБАТ", "еБАТ", "ебАТ", "ебаТ", "еБаТ", "ЕбАт", "еБат", "ебАт", "ЕбаТ", "еБАт", "ЕбАТ", "ЕБаТ", "бля", "Бля", "БЛя", "БЛЯ", "бЛЯ", "блЯ", "БлЯ", "бЛя", "сук", "Сук", "СУк", "СУК", "сУК", "суК",  "СуК", "сУк", "сучк", "Сучк", "СУчк", "СУЧк", "СУЧК", "сУЧК", "суЧК", "сучК", "СуЧк", "сУчК", "СучК", "сУЧк", "СуЧК", "СУчК", "сУчк", "суЧк", "гей", "Гей", "ГЕй", "ГЕЙ", "гЕЙ", "геЙ", "ГеЙ", "гЕй", "геев", "Геев", "ГЕев", "ГЕЕв", "ГЕЕВ", "гЕЕВ", "геЕВ", "гееВ", "ГеЕв", "гЕеВ", "ГееВ", "гЕЕв", "гЕев", "геЕв", "ГеЕВ", "ГЕеВ"]
                а = ['А', 'а']
                б = ['Б', 'б']
                в = ['В', 'в']
                г = ['Г', 'г']
                д = ['Д', 'д']
                е = ['Е', 'е']
                ё = ['Ё', 'ё']
                ж = ['Ж', 'ж']
                з = ['З', 'з']
                и = ['И', 'и']
                й = ['Й', 'й']
                к = ['К', 'к']
                л = ['Л', 'л']
                м = ['М', 'м']
                н = ['П', 'н']
                о = ['О', 'о']
                п = ['П', 'п']
                р = ['Р', 'р']
                с = ['С', 'с']
                т = ['Т', 'т']
                у = ['У', 'у']
                ц = ['Ц', 'ц']
                я = ['Я', 'я']
                ч = ['Ч', 'ч']
                ь = ['Ь', 'ь']
                ы = ['Ы', 'ы']
                ъ = ['Ъ', 'ъ']
                х = ['Х', 'х']
                э = ['Э', 'э']
                ю = ['Ю', 'ю']
                ф = ['Ф', 'ф']
                ш = ['Ш', 'ш']
                щ = ['Щ', 'щ']
                msg = message.content
                if msg in bwords:
                    await self.bot.process_commands(message)
                    console.warn('[WARNING]> ОБНАРУЖЕН МАТ')

async def setup(bot):
    try:
        await bot.add_cog(ReactWords(bot))
        console.warn('[COGS]> reactwords.py        DEACTIVATED')
    except BaseException:
        console.error('[COGS]> reactwords.py              ERROR')