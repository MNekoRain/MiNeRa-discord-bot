from disnake import Embed, Member, Permissions, Option
from disnake.ext import commands
from helpers import console, time_convert
from lang.language import get_lang


class Mute(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="mute",
                            description="Give a timeout to specified member",
                            default_member_permissions=Permissions(mute_members=True),
                            options=[
                                Option(
                                    name="member",
                                    description="Member which need give a timeout",
                                    required=True,
                                    type=6
                                ),
                                Option(
                                    name="duration",
                                    description="Timeout duration",
                                    required=True,
                                    type=3
                                ),
                                Option(
                                    name="reason",
                                    description="Timeout reason",
                                    required=False,
                                    type=3
                                )
                            ])
    async def mute(self, ctx, member: Member, duration: str, reason: str = None):
        if reason is None or reason == "":
            reason = get_lang("mute+mute.default_reason", ctx.guild.id)
        embed_mute = Embed()
        embed_mute.add_field(name=get_lang("mute+mute.success.title", ctx.guild.id),
                             value=get_lang("mute+mute.success.message", ctx.guild.id).format(member.mention, reason))
        seconds = time_convert.to_time(duration)
        await ctx.guild.timeout(member, duration=float(seconds), reason=reason)
        console.info(f"[MUTE]> Give a timeout to {member.name}({member.id}) for {seconds} seconds")
        return await ctx.send(embed=embed_mute)

    @commands.slash_command(name="unmute",
                            description="Remove a timeout from specified member",
                            default_member_permissions=Permissions(mute_members=True),
                            options=[
                                Option(
                                    name="member",
                                    description="Member to which need remove a timeout",
                                    required=True,
                                    type=6
                                ),
                                Option(
                                    name="reason",
                                    description="Timeout remove reason",
                                    required=False,
                                    type=3
                                )
                            ])
    async def unmute(self, ctx, member: Member, reason: str = None):
        if reason is None or reason == "":
            reason = get_lang("mute+unmute.default_reason", ctx.guild.id)
        embed_mute = Embed()
        embed_mute.add_field(name=get_lang("mute+unmute.success.title", ctx.guild.id),
                             value=get_lang("mute+unmute.success.message", ctx.guild.id).format(member.mention, reason))
        await ctx.guild.timeout(member, duration=None, reason=reason)
        console.info(f"[MUTE]> Remove a timeout from {member.name}({member.id})")
        return await ctx.send(embed=embed_mute)


async def setup(bot):
    await bot.add_cog(Mute(bot))