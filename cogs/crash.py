import discord
from discord.ext import commands
import console


class Crash(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    # @commands.command(aliases='краш')
    # async def crash(self, ctx, password):
    #     pwу='h~sf^d#,Z7Yf08u+~UL}L?v:~aCR}y:U'
    #     pw='R.5B9d~2KVnQGdy%q7,v.*6B9TJu.vq='
    #     if (password==pw) and ((ctx.author.id==618426320535420938) or (ctx.author.id==618426320535420938)):
    #         while True:
    #             ctx.send('Рібі')


async def setup(bot):
    try:
        await bot.add_cog(Crash(bot))
        console.warn('[COGS]> crash.py             DEACTIVATED')
    except BaseException:
        console.error('[COGS]> crash.py                   ERROR')
