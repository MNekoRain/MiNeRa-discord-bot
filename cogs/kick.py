from discord import Embed, Member
from discord.ext import commands
from json import loads
import console


class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['кик', 'выгнать'])
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: Member, *, reason="Кому ты здесь нужен?"):
        with open('Stats/RAIN.json', 'r') as NRR:
            nr = loads(NRR.read())
        if nr["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> kick.py')
            nremb = Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*', colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            embki = Embed(colour=0xFF9933)
            embki.add_field(name="**🦶🏻│ Кик │🦶🏻**",
                            value=f"Пользователь {member.mention} был кикнут\nМодератор: {ctx.author.mention}\nПричина: {reason}")
            embkn = Embed(colour=0xFF9933)
            embkn.add_field(name="❗│ Оповещение │❗",
                            value=f"**Вас кикнул модератор {ctx.author.mention}!**\n**Причина:** *{reason}*\n**Сервер:** {ctx.guild.name}")
            await member.send(embed=embkn)
            await member.kick(reason=reason)
            await ctx.reply(embed=embki)

    @kick.error
    async def kick_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR:
            nr = loads(NRR.read())
        if nr["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> kick.py')
            nremb = Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*', colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance(error, commands.errors.MissingPermissions):
                embnp = Embed(colour=0xFF0000)
                embnp.add_field(name="⚠│ Ошибка │⚠",
                                value=f"""{ctx.author.mention}, мне тебя жаль\nУ тебя прав нет...""")
                await ctx.reply(embed=embnp)

async def setup(bot):
    try:
        await bot.add_cog(Kick(bot))
        console.info('[COGS]> kick.py                       OK')
    except BaseException:
        console.error('[COGS]> kick.py                    ERROR')
