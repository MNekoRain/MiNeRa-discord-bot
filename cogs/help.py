import discord
from discord.ext import commands
import json
import console


class Help(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['хелп','помощь'])
    async def help(self, ctx, arg):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> help.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            with open("config.json", "r") as f:
                config_json=f.read()
            cfg=json.loads(config_json)
            kik=["kick","кик","выгнать"]
            ban=["ban","бан","забанить"]
            uban=["unbam","uban","рбан","разбан"]
            mut=["mute","мут","мьют"]
            umut=["unmute","umute","рмут","рмьют"]
            cle=["clear","очистка","clean"]
            war=["warn","пред","варн"]
            embki=discord.Embed(title='**__Команда `kick`__**')
            embki.add_field(name=f'**Использование:**',value=f'*`{cfg["PREFIX"]}kick <Упоминание> (Причина)`*')
            embki.add_field(name='**Примеры:**',value=f'*{cfg["PREFIX"]}kick {ctx.author.mention}*\n \n*{cfg["PREFIX"]}kick {ctx.author.mention} Зачем тебе эта команда?*')
            embki.add_field(name='**Псевдонимы:**',value='`кик`,`выгнать`')
            embba=discord.Embed(title='**__Команда `ban`__**')
            embba.add_field(name=f'**Использование:**',value=f'*`{cfg["PREFIX"]}ban <Упоминание> <> (Причина)`*')
            embba.add_field(name='**Примеры:**',value=f'*{cfg["PREFIX"]}ban {ctx.author.mention}*\n \n*{cfg["PREFIX"]}ban {ctx.author.mention} БАН!*')
            embba.add_field(name='**Псевдонимы:**',value='`бан`,`забанить`')
            embba.add_field(name='**Примечание:**',value='**У это команды скоро не будет причины**\n**Заместо ей будет время нахождения в бане**')
            embuba=discord.Embed(title='**__Команда `unban`__**')
            embuba.add_field(name=f'**Использование:**',value=f'*`{cfg["PREFIX"]}unban <Никнейм#Тэг>`*')
            embuba.add_field(name='**Примеры:**',value=f'*{cfg["PREFIX"]}unban {ctx.author.name}*')
            embuba.add_field(name='**Псевдонимы:**',value='`рбан`,`разбан`,`uban`')
            embuba.set_footer(text='Эта команда скорее всего будет выключена!')
            embmu=discord.Embed(title='**__Команда `mute`__**')
            embmu.add_field(name=f'**Использование:**',value=f'*`{cfg["PREFIX"]}mute <Упоминание> <Время> (Причина) `*')
            embmu.add_field(name='**Примеры:**',value=f'*{cfg["PREFIX"]}mute {ctx.author.mention}*\n \n*{cfg["PREFIX"]}mute {ctx.author.mention} Зачем тебе писать?*')
            embmu.add_field(name='**Псевдонимы:**',value='`мут`,`мьют`')
            embumu=discord.Embed(title='**__Команда `unmute`__**')
            embumu.add_field(name=f'**Использование:**',value=f'*{cfg["PREFIX"]}unmute <Ник#Тег>`*')
            embumu.add_field(name='**Примеры:**',value=f'*{cfg["PREFIX"]}unmute {ctx.author}*')
            embumu.add_field(name='**Псевдонимы:**',value='`рмут`,`рмьют`,`umute`')
            embcl=discord.Embed(title='**__Команда `clear`__**')
            embcl.add_field(name=f'**Использование:**',value=f'*`{cfg["PREFIX"]}clear <Количество сообщений>`*')
            embcl.add_field(name='**Примеры:**',value=f'*{cfg["PREFIX"]}clear {ctx.author.mention}*')
            embcl.add_field(name='**Псевдонимы:**',value='`очистка`,`clean`')
            embcl.add_field(name='**Примечание:**',value='**Количество сообщений не может быть больше 999**')
            embwa=discord.Embed(title='**__Команда `warn`__**')
            embwa.add_field(name=f'**Использование:**',value=f'*`{cfg["PREFIX"]}warn <Упоминание> (Причина)`*')
            embwa.add_field(name='**Примеры:**',value=f'*{cfg["PREFIX"]}warn {ctx.author.mention}*\n \n*{cfg["PREFIX"]}warn {ctx.author.mention} На те варн*')
            embwa.add_field(name='**Псевдонимы:**',value='`пред`,`варн`')
            embcl.add_field(name='**Примечание:**',value='**Если вы получите 2 предупреждения, то вам выдадут мут на 10 минут**\n**Если вы получите 5 предупреждений, то вам выдадут мут на 45 минут**\n**Если вы получите 10 предупреждений, то вам выдадут мут на 2 часа**\n**Если вы получите 15 предупреждений, то вам выдадут мут на 5 часов**\n**Если вы получите 25 предупреждений, то вам выдадут бан на 1 день**')
            if arg in kik:
                await ctx.reply(embed=embki)
            if arg in ban:
                await ctx.reply(embed=embba)
            if arg in uban:
                await ctx.reply(embed=embuba)
            if arg in mut:
                await ctx.reply(embed=embmu)
            if arg in umut:
                await ctx.reply(embed=embumu)
            if arg in cle:
                await ctx.reply(embed=embcl)
            if arg in war:
                await ctx.reply(embed=embwa)

    @help.error
    async def help_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> help.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            with open("config.json", "r") as f:
                config_json=f.read()
            cfg=json.loads(config_json)
            embob=discord.Embed(title='**__Команды__**',
                                description=f'''**Префикс:** `{cfg["PREFIX"]}`
                                **Команды:**
                                `kick` **- Команда кика**
                                `ban` **- Команда бана**
                                `unban` **- Команда разбана**
                                `mute` **- Команды мьюта**
                                `unmute` **- Команда размьюта**
                                `warn` **- Команда для предупреждения**
                                `clear` **- Команда отчистки чата**''')
            embob.add_field(name='*Больше о командах*',
                            value=f'*Чтобы узнать больше о командах, напишите `{cfg["PREFIX"]}help <Команда>`*')
            embob.set_footer(text='Префикс временный!')
            if isinstance( error, commands.errors.MissingRequiredArgument ):
                await ctx.reply(embed=embob)

async def setup(bot):
    try:
        await bot.add_cog(Help(bot))
        console.info('[COGS]> help.py                       OK')
    except BaseException:
        console.error('[COGS]> help.py                    ERROR')