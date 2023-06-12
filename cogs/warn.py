from lib2to3.pytree import Base
import discord
from discord.ext import commands
import asyncio
import sqlite3
import openfile as o
import json
import os
import console
import G as I


class Warn(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command(aliases=['пред','варн'])
    @commands.has_permissions( manage_roles=True, ban_members=True, kick_members=True )
    async def warn(self, ctx, member:discord.Member, *, reason="Был предупрежден(-а)!"):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> warn.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            wc="0"
            WJf={
                "USER-Nick": f"{member.nick}",
                "USER-Name": f"{member.name}",
                "LASTMODERATOR-Nick": f"{ctx.author.nick}",
                "LASTMODERATOR-Name": f"{ctx.author.name}",
                "LASTMODERATOR-Id": ctx.author.id,
                "WARNCOUNT": f"{wc}"
            }
            try:
                with open(f'Stats/Warns/{ctx.guild.id} @ {ctx.guild.name}/{member.id}.json', 'r') as RF: warn=json.loads(RF.read())
            except FileNotFoundError:
                os.mkdir(f'G:/Bots/Bot_python/Stats/Warns/{ctx.guild.id} @ {ctx.guild.name}')
                with open(f'Stats/Warns/{ctx.guild.id} @ {ctx.guild.name}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                with open(f'Stats/Warns/{ctx.guild.id} @ {ctx.guild.name}/{member.id}.json', 'r') as RF: warn=json.loads(RF.read())
            SU=[650625658766098456,886289090411118653,900817113558695966,915660782103048294,809924887543152672,995035888524468406]
            if ctx.guild.id not in SU:
                embwawr=discord.Embed(colour=0xFF9933)
                embwawr.add_field(name="❗| Предупреждение │❗",value=f"**Эта команда не сможет полноценно работать**\n**Причина:** *Нет роли мьюта*")
                embwawr.set_footer(text='Команда полноценно не заработает, даже если вы создадите роль. Попросите создателя бота')
                await ctx.author.send(embed=embwawr)
            else:
                embwa=discord.Embed(colour=0xFF9933)
                embwa.add_field(name="❗| Предупреждение │❗",value=f"**{member.mention} предупрежден!**\n**Причина:** *{reason}*")
                if warn['WARNCOUNT'] == '0':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                elif warn['WARNCOUNT'] == '1':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                    emb2m=discord.Embed(colour=0xFF4242)
                    emb2m.add_field(name=f"Вас автоматически замутило на сервере {ctx.guild.name}",value=f"**Время:** *10 минут*\n**Причина мута:** *Количество предупреждений достигло 2*")
                    emb2b=discord.Embed(colour=0x42FF42)
                    emb2b.add_field(name=f"Вас автоматически размутило на сервере {ctx.guild.name}",value="**Срок мута истек!**")
                    mr=discord.utils.get(ctx.message.guild.roles, name='🔈❌ | RMBMute')
                    await member.add_roles(mr)
                    await member.send(embed=emb2m)
                    await asyncio.sleep(600)
                    try:
                        await member.remove_roles(mr)
                        await member.send(embed=emb2b)
                    except BaseException:
                        console.error('[ERROR]> При снятии наказания/отправке сообщения произошла ошибка')
                        console.error('[ERROR]> warn.py    75 line')
                elif warn['WARNCOUNT'] == '2':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                elif warn['WARNCOUNT'] == '3':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                elif warn['WARNCOUNT'] == '4':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                    emb5m=discord.Embed(colour=0xFF4242)
                    emb5m.add_field(name=f"Вас автоматически замутило на сервере {ctx.guild.name}",
                                    value=f"**Время:** *45 минут*\n**Причина мута:** *Количество предупреждений достигло 5*")
                    emb5b=discord.Embed(colour=0x42FF42)
                    emb5b.add_field(name=f"Вас автоматически размутило на сервере {ctx.guild.name}",
                                    value="**Срок мута истек!**")
                    mr=discord.utils.get(ctx.message.guild.roles, name='🔈❌ | RMBMute')
                    await member.add_roles(mr)
                    await member.send(embed=emb5m)
                    await asyncio.sleep(2700)
                    try:
                        await member.remove_roles(mr)
                        await member.send(embed=emb5b)
                    except BaseException:
                        console.error('[ERROR]> При снятии наказания/отправке сообщения произошла ошибка')
                        console.error('[ERROR]> warn.py    96 line')
                elif (warn['WARNCOUNT'] >= '5') and (warn['WARNCOUNT'] < '9'):
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                elif warn['WARNCOUNT'] == '9':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                    emb10m=discord.Embed(colour=0xFF4242)
                    emb10m.add_field(name=f"Вас автоматически замутило на сервере {ctx.guild.name}",
                                    value=f"**Время:** *2 часа*\n**Причина мута:** *Количество предупреждений достигло 10*")
                    emb10b=discord.Embed(colour=0x42FF42)
                    emb10b.add_field(name=f"Вас автоматически размутило на сервере {ctx.guild.name}",
                                    value="**Срок мута истек!**")
                    mr=discord.utils.get(ctx.message.guild.roles, name='🔈❌ | RMBMute')
                    await member.add_roles(mr)
                    await member.send(embed=emb10m)
                    await asyncio.sleep(7200)
                    try:
                        await member.remove_roles(mr)
                        await member.send(embed=emb10b)
                    except BaseException:
                        console.error('[ERROR]> При снятии наказания/отправке сообщения произошла ошибка')
                        console.error('[ERROR]> warn.py    131 line')
                elif (warn['WARNCOUNT'] >= '10') and (warn['WARNCOUNT'] < '14'):
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                elif warn['WARNCOUNT'] == '14':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                    emb15m=discord.Embed(colour=0xFF4242)
                    emb15m.add_field(name=f"Вас автоматически замутило на сервере {ctx.guild.name}",
                                    value=f"**Время:** *5 часов*\n**Причина мута:** *Количество предупреждений достигло 15*")
                    emb15b=discord.Embed(colour=0x42FF42)
                    emb15b.add_field(name=f"Вас автоматически размутило на сервере {ctx.guild.name}",
                                    value="**Срок мута истек!**")
                    mr=discord.utils.get(ctx.message.guild.roles, name='🔈❌ | RMBMute')
                    await member.add_roles(mr)
                    await member.send(embed=emb15m)
                    await asyncio.sleep(18000)
                    try:
                        await member.remove_roles(mr)
                        await member.send(embed=emb15b)
                    except BaseException:
                        console.error('[ERROR]> При снятии наказания/отправке сообщения произошла ошибка')
                        console.error('[ERROR]> warn.py    162 line')
                elif (warn['WARNCOUNT'] >= '15') and (warn['WARNCOUNT'] < '24'):
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                elif warn['WARNCOUNT'] == '24':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                    embmm=discord.Embed(colour=0xFF4242)
                    embmm.add_field(name=f"Вас забанили на сервере {ctx.guild.name}",
                                    value=f"**Время:** *1 день*\n**Причина бана:** *Слишком большое количество предупреждений*")
                    embmb=discord.Embed(colour=0x42FF42)
                    embmb.add_field(name=f"Вас разбанили на сервере {ctx.guild.name}",
                                    value="**Срок бана истек!**")
                    await member.send(embed=embmm)
                    await member.ban()
                    await asyncio.sleep(86400)
                    try:
                        await member.unban()
                        try:
                            await member.send(embed=embmb)
                        except BaseException:
                            console.error('[ERROR]> warn.py')
                    except BaseException:
                        console.error('[ERROR]> warn.py')
                elif warn['WARNCOUNT'] >= '25':
                    wcc=int(warn['WARNCOUNT'])+1
                    WJf={"USER-Nick": f"{member.nick}","USER-Name": f"{member.name}","LASTMODERATOR-Nick": f"{ctx.author.nick}","LASTMODERATOR-Name": f"{ctx.author.name}","WARNCOUNT": f"{wcc}"}
                    with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJf, indent=4, sort_keys=True))
                    await ctx.channel.send(embed=embwa)
                    embwawrr=discord.Embed(colour=0xFF9933)
                    embwawrr.add_field(name="❗| Предупреждение │❗",value=f"**Количество предупреждений превысило 25. Выше 25 предупреждений не будет наказаний - это будут просто цифры**")
                    await ctx.reply(embwawrr)

    @commands.command(aliases=['упред','уварн','rwarn'])
    @commands.is_owner()
    @commands.has_permissions( manage_roles=True, ban_members=True, kick_members=True )
    async def rewarn(self, ctx, member:discord.Member):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> warn.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            WJF={
                "USER-Nick": f"{member.nick}",
                "USER-Name": f"{member.name}",
                "LASTMODERATOR-Nick": f"{ctx.author.nick}",
                "LASTMODERATOR-Name": f"{ctx.author.name}",
                "LASTMODERATOR-Id": ctx.author.id,
                "WARNCOUNT": "0"
            }
            with open(f'Stats/Warns/{ctx.guild.id}/{member.id}.json', 'w',) as WF: WWF=WF.write(json.dumps(WJF, indent=4, sort_keys=True))
            embrwa=discord.Embed(colour=0x99FF33)
            embrwa.add_field(name="♻| Предупреждение │♻",value=f"**Пользователю {member.mention} сняты все предупреждения!**")
            await ctx.send(embed=embrwa)



async def setup(bot):
    try:
        await bot.add_cog(Warn(bot))
        console.info('[COGS]> warn.py                       OK')
    except BaseException:
        console.error('[COGS]> warn.py                    ERROR')