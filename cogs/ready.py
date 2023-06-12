import discord
from discord.ext import commands
import asyncio
import datetime
import json
import console


class Ready(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        now=datetime.datetime.now()
        fn=now.strftime('%Y.%d.%w')
        tt=now.strftime('[%H:%M:%S.%f]')
        LogO=f'(\n    TIME:      {tt}\n    ACTION:    ВКЛЮЧЕНИЕ\n)\n'
        with open(f'LOGON/{fn}.txt','a+') as fLO:
            fLO.write(LogO)
        async def send_message_emb(self, channel, embed):
            channel = self.bot.get_channel(channel)
            await channel.send(embed=embed)
        await self.bot.change_presence(status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name="R. | Это основной бот!"))
        console.info('[BOT]> БОТ ЗАПУЩЕН')
        console.info('[BOT]> ')
        console.info('[BOT]> ИНФОРМАЦИЯ О БОТЕ')
        console.info(f'[BOT]> NAME:    {self.bot.user.name}')
        console.info(f'[BOT]> ID:      {self.bot.user.id}')
        console.info('[BOT]> OWNER:   NekoRain')
        console.info('[BOT]> OWNERID: 618426320535420938')
        console.info('[BOT]> ----------------')
        for guild in self.bot.guilds:
            console.info('[SERVERS]> {}'.format(guild.name))
            console.info('[SERVERS]> {}'.format(guild.id))
    
    async def on_disconnect(self):
        now=datetime.datetime.now()
        fn=now.strftime('%Y.%d.%w')
        tt=now.strftime('[%H:%M:%S.%f]')
        yn=int(now.strftime('%Y'))
        mon=int(now.strftime('%m'))
        dn=int(now.strftime('%d'))
        hn=int(now.strftime('%H'))
        mn=int(now.strftime('%M'))
        sn=int(now.strftime('%S'))
        mmn=int(now.strftime('%f'))
        cy=int(cft["year"])
        cmo=int(cft["month"])
        cd=int(cft["day"])
        ch=int(cft["hour"])
        cm=int(cft["minute"])
        cs=int(cft["second"])
        cmm=int(cft["microsecond"])
        yw=     yn-cy
        mow=    mon-cmo
        dw=     dn-cd
        hw=     hn-ch
        mw=     mn-cm
        sw=     sn-cs
        mmw=    mmn-cmm
        LogO=f'(\n    TIME:      {tt}\n    TIMEWORK:  {yw} {mow} {dw} {hw}:{mw}:{sw}.{mmw}\n    ACTION:    ВЫКЛЮЧЕНИЕ\n    ПРИЧИНА:   ПРОИЗОШЛА ОШИБКА НА СТОРОНЕ DISCORD)\n'
        with open(f'LOGOFF/{fn}.txt','a+') as fLO:
            fLO.write(LogO)
        with open('timework.json','r') as TBW:
                rTBW=TBW.read()
        cft=json.loads(rTBW)
        console.info(f'[TW]> {yw} {mow} {dw} {hw}:{mw}:{sw}.{mmw}')
        console.info('[CLOSING]> Завершение работы...')

    @commands.command(aliases=['createinvite','сп'])
    async def ci(self, ctx, svid: int):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> ready.py')
            nremb = discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            guild = self.bot.get_guild(svid)
            invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
            await ctx.send(f"https://discord.gg/{invite.code}")


async def setup(bot):
    try:
        await bot.add_cog(Ready(bot))
        console.info('[COGS]> ready.py                      OK')
    except BaseException:
        console.error('[COGS]> ready.py                   ERROR')