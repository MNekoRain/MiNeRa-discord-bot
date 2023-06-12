import discord
from discord.ext import commands
import asyncio
import json
import console


class Role(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command( aliases=['arole','дроль'] )
    @commands.is_owner()
    async def add_role( self, ctx, role:discord.Role, member:discord.Member ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> role.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            emb=discord.Embed()
            emb.add_field(name='**✅│ Роль │✅**',
                          value=f'**Пользователю {member.mention} выдана роль {role.mention} c ID `{role.id}`**')
            console.info(f'[ROLE]> Пользователю {member.name} убрана роль {role.name} с ID {role.id}')
            await member.add_roles(role)
            await ctx.reply(embed=emb)

    @add_role.error
    async def add_role_error( self, ctx, error ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> role.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply(embed=nremb)
        else:
            if isinstance( error, commands.errors.NotOwner ):
                embv=discord.Embed()
                embv.add_field(name='**💠│ Попытка получения доступа │💠**',
                               value='**Подождите 1 минуту**')
                await ctx.reply(embed=embv)
                emb=discord.Embed()
                emb.add_field(name='**⛔│ Отказ в доступе │⛔**',
                              value='**Вы не владелец бота!**')
                await asyncio.sleep(60)
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.RoleNotFound ):
                emb=discord.Embed()
                emb.add_field(name='**⚠│ Ошибка │⚠**',
                              value='**Роль не найдена**')
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.MissingRole ):
                emb=discord.Embed()
                emb.add_field(name='**⚠│ Ошибка │⚠**',
                              value='**Роль не указана**')
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.MemberNotFound ):
                ca=ctx.author
                role:discord.Role
                emb=discord.Embed()
                emb.add_field(name='**✅│ Роль │✅**',
                              value=f'**Пользователю {ca.mention} убрана роль {role.mention} c ID `{role.id}`**')
                console.info(f'[ROLE]> Пользователю {ca.name} убрана роль {role.name} с ID {role.id}')
                await ca.add_roles(role)
                await ctx.reply(embed=emb)

    @commands.command( aliases=['rrole','уроль'] )
    @commands.is_owner()
    async def remove_role( self, ctx, role:discord.Role, member:discord.Member ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> role.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply()
        else:
            emb=discord.Embed()
            emb.add_field(name='**✅│ Роль │✅**',
                          value=f'**Пользователю {member.mention} убрана роль {role.mention} c ID `{role.id}`**')
            console.info(f'[ROLE]> Пользователю {member.name} убрана роль {role.name} с ID {role.id}')
            await member.remove_roles(role)
            await ctx.reply(embed=emb)

    @remove_role.error
    async def remove_role_error( self, ctx, error ):
        with open('Stats/RAIN.json', 'r') as NRR: NR=json.loads(NRR.read())
        if NR["RESPONSING"] == "FALSE":
            console.error('[NOTRESPONSIN]> role.py')
            nremb=discord.Embed(description='**Бот временно не будет исполнять команды или отвечать**\n***Причина:*** *R͘͢͠a̵i҉̵̷n̵͏͏ ̶͢͜҉о̧́́б̢̢͜ѝ̵д̧͘е̶̢͞л̶͘а̷̧҉с̛͟͟ь͏̛̀ н̸̧͝а̵ ̧͞к̶̢о̢͟г͡͏̧о̷̛́ ̕͜͢т̸́͟о̨͘,̡̛͠ ̛́͠и̵̢̕ ̨͠͞н̶̕͡е̛͘͟ ̧͟͡б̨́͟у̴͢͝д̸̕͟е̡̕͞т́̕͝ ͞҉̧҉о̷́т͏̵́в̕͞е̵̨͘ч̷̛͜а҉̧̛̕т̢ь́́*',colour=0xff0000)
            await ctx.reply()
        else:
            if isinstance( error, commands.errors.NotOwner ):
                embv=discord.Embed()
                embv.add_field(name='**💠│ Попытка получения доступа │💠**',
                               value='**Подождите 1 минуту**')
                await ctx.reply(embed=embv)
                emb=discord.Embed()
                emb.add_field(name='**⛔│ Отказ в доступе │⛔**',
                              value='**Вы не владелец бота!**')
                await asyncio.sleep(60)
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.RoleNotFound ):
                emb=discord.Embed()
                emb.add_field(name='**⚠│ Ошибка │⚠**',
                              value='**Роль не найдена**')
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.MissingRole ):
                emb=discord.Embed()
                emb.add_field(name='**⚠│ Ошибка │⚠**',
                              value='**Роль не указана**')
                await ctx.reply(embed=emb)
            if isinstance( error, commands.errors.MemberNotFound ):
                ca=ctx.author
                role:discord.Role
                emb=discord.Embed()
                emb.add_field(name='**✅│ Роль │✅**',
                              value=f'**Пользователю {ca.mention} убрана роль {role.mention} c ID `{role.id}`**')
                console.info(f'[ROLE]> Пользователю {ca.name} убрана роль {role.name} с ID {role.id}')
                await ca.remove_roles(role)
                await ctx.reply(embed=emb)

async def setup(bot):
    try:
        await bot.add_cog(Role(bot))
        console.info('[COGS]> role.py                       OK')
    except BaseException:
        console.error('[COGS]> role.py                    ERROR')