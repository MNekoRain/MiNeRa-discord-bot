from disnake import Member, Embed, Permissions, Option
from disnake.ext import commands
from ..helpers import console
from lang.language import get_lang


class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="clear",
                            description="Purge a channel for deletion messages",
                            default_member_permissions=Permissions(manage_messages=True),
                            options=[
                                Option(
                                    name="amount",
                                    description="A amount messages for deletion",
                                    required=True,
                                    type=4
                                ),
                                Option(
                                    name="member",
                                    description="Member which messages needed to delete",
                                    required=False,
                                    type=6
                                )
                            ])
    async def clear(self, ctx, amount: int = 10, *, member: Member = None):
        if member is None:
            deleted = await ctx.channel.purge(limit=amount)
        else:
            deleted = await ctx.channel.purge(limit=amount, check=lambda msg: msg.author == member)
        embed_clear = Embed()
        embed_clear.add_field(name=get_lang("clear+clear.success.title", ctx.guild.id),
                              value=get_lang("clear+clear.success.message", ctx.guild.id).format(deleted))
        console.info(f"[CLEAR]> Has been deleted {deleted} messages from {ctx.channel.name}({ctx.channel.id})")
        return await ctx.send(embed=embed_clear)


async def setup(bot):
    await bot.add_cog(Clear(bot))
