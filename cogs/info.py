import discord
from discord.ext import commands
import json
import console


class Information(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['serv','серв','сервер'])
    async def server(self, ctx):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> info.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            si=discord.Embed(title=f'{ctx.guild.name}')
            si.add_field(name='ID сервера',value=f'`{ctx.guild.id}`')
            si.add_field(name='ID владельца сервера',value=f'`{ctx.guild.owner.id}`')
            si.add_field(name='Всего участников',value=f'{str(ctx.guild.member_count)}')
            await ctx.reply(embed=si)

async def setup(bot):
    try:
        await bot.add_cog(Information(bot))
        console.info('[COGS]> info.py                       OK')
    except BaseException:
        console.error('[COGS]> info.py                    ERROR')