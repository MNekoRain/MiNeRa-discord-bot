import discord
from discord.ext import commands
import datetime
import json
import console


class OffingBot(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        now=datetime.datetime.now()
        Y=now.strftime('%Y')
        MO=now.strftime('%m')
        D=now.strftime('%d')
        H=now.strftime('%H')
        M=now.strftime('%M')
        S=now.strftime('%S')
        MM=now.strftime('%f')
        TimeNow={
            "year":       f"{Y}",
            "month":      f"{MO}",
            "day":        f"{D}",
            "hour":       f"{H}",
            "minute":     f"{M}",
            "second":     f"{S}",
            "microsecond": f"{MM}"
        }
        TimeNowJSON=json.dumps(TimeNow,indent=4,sort_keys=True)
        with open('timework.json','w') as TWjs:
            TWjs.write(TimeNowJSON)

    @commands.command(aliases=['выкл','off'])
    @commands.is_owner()
    async def off_bot(self, ctx):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> off.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            print('[WARNING]> \n[WARNING]> БЫЛА ВВЕДЕНА КОМАНДА ВЫКЛЮЧЕНИЯ\n[WARNING]> ')
            yes=["да","yes","yea","д","y","off"]
            no=["нет","no","н","n","no off","not off","nooff","notoff"]
            embd=discord.Embed(colour=0xFF0000)
            embd.add_field(name='**⏱│ Deactivate │⏱**',
                           value='**Ожидайте решения в терминале**')
            ofm=await ctx.reply(embed=embd)
            otv=str(input('[QUESTION]> Выключать бота?\n[QUESTION]> '))
            if otv in yes:
                console.warn('[DEACTIVATE]> ВЫКЛЮЧЕНИЕ БОТА')
                embde=discord.Embed(colour=0xFF0000)
                embde.add_field(name='**⭕│ DEACTIVATION │⭕**',
                                value='**ВЫКЛЮЧЕНИЕ БОТА**')
                await ofm.edit(embed=embde)
                now=datetime.datetime.now()
                yn=now.strftime('%Y')
                mon=now.strftime('%m')
                dn=now.strftime('%d')
                hn=now.strftime('%H')
                mn=now.strftime('%M')
                sn=now.strftime('%S')
                mmn=now.strftime('%f')
                with open('timework.json','r') as TBW:
                        rTBW=TBW.read()
                cft=json.loads(rTBW)
                yw=     yn-cft["year"]
                mow=    mon-cft["month"]
                dw=     dn-cft["day"]
                hw=     hn-cft["hour"]
                mw=     mn-cft["minute"]
                sw=     sn-cft["second"]
                mmw=    mmn-cft["microsecond"]
                console.info(f'[Y]>  {yw}')
                console.info(f'[MO]> {mow}')
                console.info(f'[D]>  {dw}')
                console.info(f'[H]>  {hw}')
                console.info(f'[M]>  {mw}')
                console.info(f'[S]>  {sw}')
                console.info(f'[MS]> {mmw}')
                await self.bot.close()
            elif otv in no:
                console.info('[BOT]> Бот не будет выключен!')
                embo=discord.Embed(colour=0xFF0000)
                embo.add_field(name='**❌│ ОТКАЗ │❌**',
                               value='**Вам отказано в доступе!**')
                await ofm.edit(embed=embo)
            else:
                console.error('[ERROR]> Произошла ошибка')
                embo=discord.Embed(colour=0xFF0000)
                embo.add_field(name='**❌│ ОТКАЗ │❌**',
                               value='**Бот не будет выключен из-за ошибки**')
                await ofm.edit(embed=embo)

    @off_bot.error
    async def off_bot_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> off.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance( error, commands.errors.NotOwner ):
                emb=discord.Embed(colour=0xFF0000)
                emb.add_field(name='**⛔│ Отказ в доступе │⛔**',
                              value='**Вы не владелец бота!**')
                await ctx.reply(embed=emb)

    @commands.command(aliases=['выклп', 'offp'])
    @commands.has_any_role(929151362833465446,
                           921447482507026472,
                           923096456867512391,
                           928740868448485427,
                           928744889196367913,
                           901196946478358589,
                           928273002418806834,
                           915660782182748197,
                           937552057345400852,
                           915660782182748196,
                           910472473550651403)
    async def offpr_bot(self, ctx):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> off.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            mso=self.bot.get_user(618426320535420938)
            await mso.send(f'**[ВЫКЛЮЧЕНИЕ]>** **{ctx.guild.name}**        **`{ctx.guild.id}`**\n \n**[ВЫКЛЮЧЕНИЕ]>** **{ctx.author.nick}**        **`{ctx.author.id}`**')
            console.warn('[DEACTIVATE]> ВЫКЛЮЧЕНИЕ БОТА')
            embde=discord.Embed(colour=0xFF0000)
            embde.add_field(name='**⭕│ DEACTIVATION │⭕**',
                            value='**ПРИНУДИТЕЛЬНОЕ ВЫКЛЮЧЕНИЕ БОТА**')
            await ctx.reply(embed=embde)
            now=datetime.datetime.now()
            yn=now.strftime('%Y')
            mon=now.strftime('%m')
            dn=now.strftime('%d')
            hn=now.strftime('%H')
            mn=now.strftime('%M')
            sn=now.strftime('%S')
            mmn=now.strftime('%f')
            with open('timework.json','r') as TBW:
                    rTBW=TBW.read()
            cft=json.loads(rTBW)
            yw=     int(yn)-int(cft["year"])
            mow=    int(mon)-int(cft["month"])
            dw=     int(dn)-int(cft["day"])
            hw=     int(hn)-int(cft["hour"])
            mw=     int(mn)-int(cft["minute"])
            sw=     int(sn)-int(cft["second"])
            mmw=    int(mmn)-int(cft["microsecond"])
            console.info(f'[Y]>  {yw}')
            console.info(f'[MO]> {mow}')
            console.info(f'[D]>  {dw}')
            console.info(f'[H]>  {hw}')
            console.info(f'[M]>  {mw}')
            console.info(f'[S]>  {sw}')
            console.info(f'[MS]> {mmw}')
            await self.bot.close()

    @offpr_bot.error
    async def offpr_bot_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> off.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance( error, commands.errors.CommandInvokeError ):
                embcie=discord.Embed(colour=0xFF0000)
                embcie.add_field(name='**⚠│ Ошибка в коде │⚠**',
                                 value='**Произошла ошибка в коде!**\n**Команда не может быть выполнена**')
                await ctx.reply(embed=embcie)
            if isinstance( error, commands.errors.NotOwner ):
                emb=discord.Embed(colour=0xFF0000)
                emb.add_field(name='**⛔│ Отказ в доступе │⛔**',
                              value='**Вы не владелец бота!**')
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.MissingAnyRole ):
                embr=discord.Embed(colour=0xFF0000)
                embr.add_field(name='**⛔│ Отказ в доступе │⛔**',
                               value='**У вас нет подходящей роли!**')
                await ctx.reply(embed=embr)



async def setup(bot):
    try:
        await bot.add_cog(OffingBot(bot))
        console.info('[COGS]> off.py                        OK')
    except BaseException:
        console.error('[COGS]> off.py                     ERROR')