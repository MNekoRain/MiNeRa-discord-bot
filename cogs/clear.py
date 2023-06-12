import discord
from discord.ext import commands
import json
import console


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['очистка', 'clean', 'c', 'к'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, n=0, *, msgs):
        with open('Stats/RAIN.json', 'r') as NRR:
            nr = json.loads(NRR.read())
        if nr["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> clear.py')
            nremb = discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*', colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            await ctx.message.delete()
            if n <= 0:
                await ctx.author.send("**Правильно, зачем вообще удалять сообщения?**\n**В следующий раз, вводи число сообщений для удаления**")
            else:
                sis = msgs.replace(', ', '.').replace(',', '.').replace(' ', '.').split('.')
                async for message in ctx.channel.history(limit=(n-len(sis))):
                    if message.id in sis:
                        continue
                    else:
                        print(2)
                        sss=self.bot.fetch_message(message.id)
                        print(1)
                        await self.bot.delete_message(sss)

    @clear.error
    async def clear_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR:
            nr = json.loads(NRR.read())
        if nr["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> clear.py')
            nremb = discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*', colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance(error, commands.errors.MissingPermissions):
                await ctx.reply('**Не надо так, если у тебя нет прав на эту команду,**\n**То введя ее, права у тебя не материализуются**')
            if isinstance(error, commands.errors.BadArgument):
                await ctx.reply('**Скажи чесно**\n**Ты дол###б?**\n**Как можно перепутать __цифру__ и __букву__?**')

async def setup(bot):
    try:
        await bot.add_cog(Clear(bot))
        console.info('[COGS]> clear.py                      OK')
    except BaseException:
        console.error('[COGS]> clear.py                   ERROR')
