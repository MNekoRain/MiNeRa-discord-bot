import asyncio
import discord
from discord.ext import commands
import datetime
import json
import console


class LogFile(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> logfile.py')
        else:
            try:
                now=datetime.datetime.now()
                fn=now.strftime('%Y.%d.%w')
                tt=now.strftime('[%H:%M:%S.%f]')
                LogT=f'(\n   TIME:      {tt}\n    AUTHOR:   {message.author}\n    AUTHORID: {message.author.id}\n    MESSAGE:\n{message.content}\n)\n'
                with open(f'LOG/{fn}.txt','a+') as fLT:
                    fLT.write(LogT)
            except UnicodeError: pass


async def setup(bot):
    try:
        await bot.add_cog(LogFile(bot))
        console.info('[COGS]> logfile.py                    OK')
    except BaseException:
        console.error('[COGS]> logfile.py                 ERROR')
