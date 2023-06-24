import disnake
from disnake.ext import commands
from ..helpers import console


class Ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        console.info(f'[BOT]> BOT IS READY\n[BOT]> \n[BOT]> BOT INFORMATION\n[BOT]> NAME:    {self.bot.user.name}\n[BOT]> ID:      {self.bot.user.id}\n[BOT]> ')
        for guild in self.bot.guilds:
            console.info('[SERVERS]>', guild.name)
            console.info('[SERVERS]>', guild.id)


async def setup(bot):
    await bot.add_cog(Ready(bot))