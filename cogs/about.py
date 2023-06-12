import discord
from discord.ext import commands
import json
import console


class About(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    # @commands.command(aliases=['обо','осебе'])
    # async def about(self, ctx, *, member=None):
    # 	if member is int:
    # 		with open('','r')
    # 	elif member==None:
    # 		ctx.reply()

async def setup(bot):
    try:
        await bot.add_cog(About(bot))
        console.warn('[COGS]> about.py                 UNKNOWN')
    except BaseException:
        console.error('[COGS]> about.py                   ERROR')
