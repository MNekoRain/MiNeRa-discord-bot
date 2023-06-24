from disnake import Embed, Member, Permissions, Option
from disnake.ext import commands
from ..helpers import console
from lang.language import get_lang


class Kick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="kick",
                            description="Kick a specified member from this server",
                            default_member_permissions=Permissions(kick_members=True),
                            options=[
                                Option(
                                    name="member",
                                    description="Member which need kick from this server",
                                    required=True,
                                    type=6
                                ),
                                Option(
                                    name="reason",
                                    description="Kick reason"
                                )
                            ])
    async def kick(self, ctx, member: Member, *, reason: str = None):
        embed_kick = Embed(colour=0xFF9933)
        if member not in ctx.guild.members:
            embed_kick.add_field(name=get_lang("kick+kick.error.notfound.title", ctx.guild.id),
                                 value=get_lang("kick+kick.error.notfound.message", ctx.guild.id).format(member.mention))
            return await ctx.send(embed=embed_kick)
        if reason is None or reason == "":
            reason = get_lang("kick+kick.default_reason", ctx.guild.id)
        embed_kick.add_field(name=get_lang("kick+kick.success.title", ctx.guild.id),
                             value=get_lang("kick+kick.success.message", ctx.guild.id).format(member.mention, reason))
        await member.kick(reason=reason)
        console.info(f"[KICK]> Member {member.name}({member.id}) has kicked from {ctx.guild.name}({ctx.guild.id}) for {reason}")
        await ctx.send(embed=embed_kick)


async def setup(bot):
    await bot.add_cog(Kick(bot))
