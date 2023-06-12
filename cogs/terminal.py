import discord
from discord.ext import commands
import asyncio
import json
import console


class Terminal(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['терминал','терм','term'])
    @commands.has_permissions( administrator=True )
    async def terminal(self, ctx):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            await ctx.message.delete()
            console.warn('[WARNING]> ')
            console.warn('[WARNING]> ОБНАРУЖЕНО ОТКРЫТИЕ ТЕРМИНАЛА')
            console.warn('[WARNING]> ')
            console.warn(f'[WARNING]> AUTHORNAME: {ctx.author.name}')
            console.warn(f'[WARNING]> AUTHORID:   {ctx.author.id}')
            await asyncio.sleep(1) 
            console.error('[ERROR]> Невозможно воспроизвести команды закрытия терминала')
            await asyncio.sleep(2)
            console.info('[ACTION]> Аварийное закрытие терминала...')
            await asyncio.sleep(1)
            console.error('[ERROR]> Закрытие терминала невозможно!')
            yes=["да","Да","yes","Yes","д","Д","y","Y"]
            no=["нет","Нет","no","No","н","Н","n","N"]
            while True:
                otv = input('[CHANNEL]> Сообщение отправить в этот же канал?\n[CHANNEL]> ')
                if otv in yes:
                    text=console.q('[MESSAGE]> Что написать?\n[MESSAGE]> ')
                    channel=ctx.channel.id
                    console.info(f'[CHANNELID]> {ctx.channel.id}\n[CHANNELNAME]> {ctx.channel.name}')
                    await self.bot.http.send_message(channel, text)
                    end = console.q('[QUESTION]> Написать еще что то?\n[ANSWER]> ')
                    if end in yes:
                        continue
                    elif end in no:
                        break
                    else:
                        console.error('[ERROR]> Вы ответили неправильно')
                        console.info('[ACTION]> Закрытие терминала...')
                        break
                elif otv in no:
                    channel=console.q('[CHANNEL]> В какой канал отправить сообщение?\n[CHANNEL]> ')
                    text=console.q('[MESSAGE]> Что написать?\n[MESSAGE]> ')
                    await self.bot.http.send_message(channel, text)
                    end = console.q('[QUESTION]> Написать еще что то?\n[ANSWER]> ')
                    if end in yes:
                        continue
                    elif end in no:
                        break
                    else:
                        console.error('[ERROR]> Вы ответили неправильно')
                        console.info('[ACTION]> Закрытие терминала...')
                        break
                else:
                    console.error('[ERROR]> Вы ответили неправильно')
                    console.error('[ACTION]> Закрытие терминала...')
                    end = console.q('[QUESTION]> Написать еще что то?\n[ANSWER]> ')
                    if end in yes:
                        continue
                    elif end in no:
                        break
                    else:
                        console.error('[ERROR]> Вы ответили неправильно')
                        console.info('[ACTION]> Закрытие терминала...')
                        break
            

    @commands.command(aliases=['banterm','tban','бантерм','тбан'])
    @commands.is_owner()
    async def ban_term(self, ctx, member:discord.Member, *, reason="Терминал никого не жалеет"):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            mena=member.guild.name
            meme=member.mention
            ctau=ctx.author
            console.info(f"[TERMINALBAN]> ")
            reason=str(console.q('[TERMINALBAN]> Причина\n[REASON]> '))
            embbt=discord.Embed(title="**🔨│ Бан │🔨**")
            embbt.add_field(name="**Пользователь**", value=f"**{meme}**")
            embbt.add_field(name="**Причина**",      value=f"*{reason}*")
            await ctx.reply(embed=embbt)
            await member.ban(reason=reason)
            console.info(f'[TERMINALBAN]> Модератор {ctau}')
            console.info(f'[TERMINALBAN]> Пользователь {mena} забанен')
            console.info(f'[TERMINALBAN]> Причине {reason}')

    @commands.command(aliases=['w','н','написать','write'])
    async def write_msg(self, ctx, chID:int, *, mess=None):
        with open('Stats/RAIN.json', 'r') as NRR: nr=json.loads(NRR.read())
        if nr["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            console.info('[COMMANDUSE]> Команда write была использована')
            console.info('[COMMANDUSE]> Канал:     {}'.format(str(chID)))
            console.info('[COMMANDUSE]> Сообщение: {}'.format(str(mess)))
            if mess == None:
                await ctx.send('**Ая-яй, ты что пустоту хотел написать?**')
            else:
                channel=self.bot.get_channel(chID)
                async with channel.typing():
                    await asyncio.sleep(1)
                await channel.send(mess)

    @write_msg.error
    async def write_msg_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: nr=json.loads(NRR.read())
        if nr["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance(error, commands.errors.BadArgument):
                await ctx.send('**Ті кого хочешь наибать?**')
            if isinstance(error, commands.errors.MissingRequiredArgument):
                await ctx.send('**Ті кого хочешь наибать?**')

    @commands.command(aliases=['rw','он','отвнаписать','repwrite'])
    async def reply_write_msg(self, ctx, chID:int, remsg:int, *, mess=None):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            channel=self.bot.get_channel(chID)
            remess=await channel.fetch_message(remsg)
            console.info('[COMMANDUSE]> Команда reply write была использована')
            console.info('[COMMANDUSE]> Пользователь:         {}'.format(str(chID)))
            console.info('[COMMANDUSE]> Сообщение:            {}'.format(str(mess)))
            console.info('[COMMANDUSE]> Отвечаемое сообщение:')
            console.info('{}'.format(str(remess.content)))
            if mess==None:
                await ctx.send('**Ая-яй, ты что пустоту хотел написать?**')
            else:
                async with channel.typing():
                    await asyncio.sleep(1)
                await remess.reply(mess)

    @reply_write_msg.error
    async def reply_write_msg_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance(error, commands.errors.BadArgument):
                await ctx.send('**Ті кого хочешь наибать?**')
            if isinstance(error, commands.errors.MissingRequiredArgument):
                await ctx.send('**Ті кого хочешь наибать?**')
            
    @commands.command(aliases=['l','л','лс','lc'])
    async def l_msg(self, ctx, uID:int, *, mess=None):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            console.info('[COMMANDUSE]> Команда lc была использована')
            console.info('[COMMANDUSE]> Канал:     {}'.format(str(uID)))
            console.info('[COMMANDUSE]> Сообщение: {}'.format(str(mess)))
            if mess==None:
                await ctx.send('**Ая-яй, ты что пустоту хотел написать?**')
            else:
                user=self.bot.get_user(uID)
                async with user.typing():
                    await asyncio.sleep(1)
                await user.send(mess)

    @l_msg.error
    async def l_msg_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance(error, commands.errors.BadArgument):
                await ctx.send('**Ті кого хочешь наибать?**')
            if isinstance(error, commands.errors.MissingRequiredArgument):
                await ctx.send('**Ті кого хочешь наибать?**')

    @commands.command(aliases=['rl','ол','отлс','relc'])
    async def reply_l_msg(self, ctx, uID:int, remsg:int, *, mess=None):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            channel=self.bot.get_user(uID)
            remess=await channel.fetch_message(remsg)
            console.info('[COMMANDUSE]> Команда reply lc была использована')
            console.info('[COMMANDUSE]> Пользователь:         {}'.format(str(uID)))
            console.info('[COMMANDUSE]> Сообщение:            {}'.format(str(mess)))
            console.info('[COMMANDUSE]> Отвечаемое сообщение:')
            console.info('{}'.format(str(remess.content)))
            if mess==None:
                await ctx.send('**Ая-яй, ты что пустоту хотел написать?**')
            else:
                async with channel.typing():
                    await asyncio.sleep(1)
                await remess.reply(mess)

    @reply_l_msg.error
    async def reply_l_msg_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> terminal.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance(error, commands.errors.BadArgument):
                await ctx.send('**Ті кого хочешь наибать?**')
            if isinstance(error, commands.errors.MissingRequiredArgument):
                await ctx.send('**Ті кого хочешь наибать?**')

    @commands.command(aliases=['md', 'ms', 'mede'])
    async def ms_del(self, ctx, n:int, chan:int, *, mess=None):
        ch = self.bot.get_channel(chan)
        if mess == None:
            await ch.purge(limit=n)
        else:
            ms = await ch.fetch_message(mess)
            await ms.delete()


async def setup(bot):
    try:
        await bot.add_cog(Terminal(bot))
        console.info('[COGS]> terminal.py                   OK')
    except BaseException:
        console.error('[COGS]> terminal.py                ERROR')