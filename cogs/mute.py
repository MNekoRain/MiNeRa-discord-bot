import discord
from discord.ext import commands
import asyncio
import json
import pytimeparse
import console


class Mute(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['мут','мьют'])
    @commands.has_permissions( manage_roles=True )
    async def mute(self, ctx, member:discord.Member, time, *, reason="Замолкни"):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> mute.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            console.info(f"[MUTE]> Модератором {ctx.author} была использована команда mute")
            mr = discord.utils.get(ctx.message.guild.roles, name='│ RMBMute │')
            pr=pytimeparse.parse(time)
            await member.add_roles(mr)
            console.info(f"[MUTE]> Модератор:  {ctx.author}\n[MUTE]> Нарушитель: {member}\n[MUTE]> Время:      {pr} секунд\n[MUTE]> Причина:    {reason}")
            emb=discord.Embed(title="**🔈│ МУТ │🔈**", colour=0xFF9933)
            emb.add_field(name="**Нарушитель**", value=f"**{member.mention}**")
            emb.add_field(name="**Модератор**",  value=f"**{ctx.author.mention}**")
            emb.add_field(name="**Причина**",    value=f"*{reason}*")
            await ctx.reply(embed=emb)
            await asyncio.sleep(pr)
            await member.remove_roles(mr)
            console.info(f"[MUTE]> У пользователя {member} кончилось время мута!")

    @mute.error
    async def mute_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> mute.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance( error, commands.errors.MissingPermissions):
                console.error(f'[MUTE]> У {ctx.author} недостаточно прав для выполнения команды mute')
                emb=discord.Embed(title='**⚠│ Ошибка │⚠**')
                emb.add_field(name='**У вас недостаточно прав!**',
                              value=f'\n**"Модератор": {ctx.author.mention}**')
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.MemberNotFound):
                console.error(f'[MUTE]> Пользователь, который указан модератором {ctx.author}, не найден!')
                emb=discord.Embed(title='**⚠│ Ошибка │⚠**')
                emb.add_field(name='**Пользователь не найден!**',
                              value=f'\n**Модератор: {ctx.author.mention}**')
                await ctx.reply(embed=emb)

    @commands.command(aliases=['рмут','рмьют','umute'])
    @commands.has_permissions( manage_roles=True )
    async def unmute(self, ctx, member:discord.Member):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> mute.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            mr = discord.utils.get(ctx.message.guild.roles, name='│ RMBMute │')
            await member.remove_roles(mr)
            emb=discord.Embed(title="**🔊│ МУТ │🔊**", colour=0x9999FF)
            emb.add_field(name=f"**Пользователь**", value=f"**{member.mention}**")
            emb.add_field(name=f"**Модератор**",    value=f"**{ctx.author.mention}**")
            await ctx.reply(embed=emb)

    @unmute.error
    async def unmute_error(self, ctx, error):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> mute.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance( error, commands.errors.dMissingRequiredArgument ):
                console.error(f'[UNMUTE]> {ctx.author} не указал пользователя')
                emb=discord.Embed(title='**⚠│ Ошибка │⚠**')
                emb.add_field(name='**Вы не указали пользователя!**',
                              value=f'\n**"Модератор": {ctx.author.mention}**')
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.MissingPermissions):
                console.error(f'[UNMUTE]> У {ctx.author} недостаточно прав для выполнения команды mute')
                emb=discord.Embed(title='**⚠│ Ошибка │⚠**')
                emb.add_field(name='**У вас недостаточно прав!**',
                              value=f'\n**"Модератор": {ctx.author.mention}**')
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.MemberNotFound):
                console.error(f'[UNMUTE]> Пользователь, который указан модератором {ctx.author}, не найден!')
                emb=discord.Embed(title='**⚠│ Ошибка │⚠**')
                emb.add_field(name='**Пользователь не найден!**',
                              value=f'\n**Модератор: {ctx.author.mention}**')
                await ctx.reply(embed=emb)

async def setup(bot):
    try:
        await bot.add_cog(Mute(bot))
        console.info('[COGS]> mute.py                       OK')
    except BaseException:
        console.error('[COGS]> mute.py                    ERROR')