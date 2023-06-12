import discord
from discord.ext import commands
import pytimeparse
import asyncio
import json
import console


class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot=bot
    
    @commands.command( aliases=['тебан','затебанить'] )
    @commands.has_permissions( ban_members=True )
    async def teban( self, ctx, member:discord.Member ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> ban.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            yes=["да","Да","ДА","дА","yes","Yes","YEs","YES","yES","yeS","YeS","yEs","y","Y","д","Д"]
            no=["нет","Нет","НЕт","НЕТ","нЕТ","неТ","НеТ","нЕт","no","No","NO","nO","n","N","н","Н"]
            ot=console.q(f"[BAN]> Забанить {member.name}?\n[BAN]> ")
            if ot in yes:
                ti=console.q("[BAN]> Насколько забанить?\n[TIME]> ")
                PRTB=pytimeparse.parse(ti)
                embbm5=discord.Embed(colour=0xFF9933)
                embbm5.add_field(name="🔨│ Бан │🔨",value=f"**Пользователь** *{member.mention}* **забанен на** *{ti}* **секунду!**")
                await member.ban()
                console.info(f"[BAN]> Модератор {ctx.author.user.name} заблокировал {member.name}")
                await member.send(f"**Вы были забанены пользователем** *{ctx.author.mention}* **на** *{ti}* **секунду!**\n \n**Сервер:** {ctx.guild.name}")
                await ctx.reply(embed=embbm5)
                await asyncio.sleep(PRTB)
                await member.unban()
                await member.send(f'**Вы были разбанены пользователем** *{self.bot.mention}***!**\n \n**Сервер:** {ctx.guild.name}')
            elif ot in no:
                embo=discord.Embed(colour=0xFF0000)
                embo.add_field(name="⚠│ Отказ │⚠",value=f"**Терминал отказал банить пользователя {member.mention}**")
                await ctx.reply(embed=embo)
            else:
                console.info(f"[BAN]> У модератора {ctx.author.name} произошла ошибка")
                emberr=discord.Embed(colour=0xFF0000)
                emberr.add_field(name="⚠│ Ошибка │⚠",value="Вы или время ввели не правильно,\nИли команду")
                emberr.add_field(name="❔│ Помощь │❔",value="Пожалуйста, обращайтесь за помощью к создателю бота, либо к Администрации")
                await ctx.reply(embed=emberr)

    @teban.error
    async def teban_error( self, ctx, error ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> ban.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance( error, commands.errors.MissingPermissions ):
                embnp=discord.Embed(colour=0xFF0000)
                embnp.add_field(name="⚠│ Ошибка │⚠",value=f"{ctx.author.mention}, а кого ты хотел забанить?\nУ тебя ведь прав нет")
                await ctx.reply(embed=embnp)

    @commands.command( aliases=['ртебан','разтебанить'] )
    @commands.has_permissions( ban_members=True )
    async def uteban( self, ctx, *, member ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> ban.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            yes=["да","Да","ДА","дА","yes","Yes","YEs","YES","yES","yeS","YeS","yEs","y","Y","д","Д"]
            no=["нет","Нет","НЕт","НЕТ","нЕТ","неТ","НеТ","нЕт","no","No","NO","nO","n","N","н","Н"]
            yon=console.q(f"[UNBAN]> Разбанить {member}?\n[ANSWER]> ")
            if yon in yes:
                ban_users = await ctx.guild.bans()

                for ban_entry in ban_users:
                    user = ban_entry.user
                    await ctx.guild.unban(user)
                    embuby=discord.Embed(colour=0x42FF42)
                    embuby.add_field(name="♻| Разбан │♻",value=f"**Пользователь** *{member}* **разбанен!**")
                    await ctx.reply(embed=embuby)

                    return
            elif yon in no:
                embubn=discord.Embed(colour=0x42FF42)
                embubn.add_field(name="⚠│ Отказ │⚠",value=f"**Терминал запретил вам использование команды `uteban`!**")
                await ctx.reply(embed=embubn)

    @uteban.error
    async def uteban_error( self, ctx, error ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> ban.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance( error, commands.errors.MissingPermissions ):
                embunp=discord.Embed(colour=0x42FF42)
                embunp.add_field(name="⚠│ Ошибка │⚠",value=f"**Чта?**\n**Ты хотел кого-то разбанить?**\n**А права где потерял?**")
                await ctx.reply(embed=embunp)

    @commands.command( aliases=['бан','забанить'] )
    @commands.has_permissions( ban_members=True )
    async def ban( self, ctx, member:discord.Member, time, *, reason="Кара божья" ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> ban.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            console.info("[COMMAND]> Команда BAN была написана")
            pr=pytimeparse.parse(time)
            embba=discord.Embed(title="**🔨│ Бан │🔨**", colour=0xFF9933)
            embba.add_field(name="**Нарушитель**", value=f"**{member.mention}**")
            embba.add_field(name="**Модератор**",  value=f"**{ctx.author.mention}**")
            embba.add_field(name="**Причина**",    value=f"*{reason}*")
            embbn=discord.Embed(colour=0xFF9933)
            embbn.add_field(name="❗│ Оповещение │❗",
                            value=f"**Вас забанил модератор {ctx.author.mention}!**\n**Причина:** *{reason}*\n**Сервер:** {ctx.guild.name}")
            console.info(f"[BAN]> ")
            console.info(f"[MODERATOR]> {ctx.author.name}")
            console.info(f"[MEMBER]>    {member.name}")
            console.info(f"[TIME]>      {pr}")
            console.info(f"[BAN]> ")
            await member.send(embed=embbn)
            await ctx.reply(embed=embba)
            await member.ban(reason=reason)
            await asyncio.sleep(pr)
            await member.unban()
            console.info(f"[BAN]> Время бана {member} закончилось")

                #else:
                 #   inf=discord.Embed(colour=0xFF0000)
                  #  inf.add_field(name="🔨│ Бан",
                   #               value=f"**Пользователь** *{member.mention}* **забанен** *навсегда*")
                    #await member.ban()

    @ban.error
    async def ban_error( self, ctx, error ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> ban.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance( error, commands.errors.MissingPermissions ):
                embnp=discord.Embed(colour=0xFF9933)
                embnp.add_field(name="⚠│ Ошибка │⚠",value="**Сэбэ бан пропиши**\n****")
                await ctx.reply(embed=embnp)
            if isinstance( error, commands.errors.MissingRequiredArgument ):
                console.error("[BAN]> Правильно, кому нужны причины?")

    @commands.command( aliases=['разбан','рбан','uban'] )
    @commands.has_permissions( ban_members=True )
    async def unban( self, ctx, *, member):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> ban.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            ban_users = ctx.guild.bans()

            for ban_entry in ban_users:
                user = ban_entry.user
                await ctx.guild.unban(user)
                embuby=discord.Embed(title="**♻│ Разбан │♻**", colour=0x42FF42)
                embuby.add_field(name="**Пользователь**", value=f"*{member}*")
                embuby.add_field(name="**Модератор**", value=f"*{ctx.author.mention}*")
                await ctx.reply(embed=embuby)

                return

async def setup(bot):
    try:
        await bot.add_cog(Ban(bot))
        console.info('[COGS]> ban.py                        OK')
    except BaseException:
        console.error('[COGS]> ban.py                     ERROR')