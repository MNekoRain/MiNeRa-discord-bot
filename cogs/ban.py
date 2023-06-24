from disnake import Permissions, Option, Member, Embed
from disnake.ext import commands
from ..helpers import console
from lang.language import get_lang


class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="ban",
                            description="Ban a specified member from this server",
                            default_member_permissions=Permissions(ban_members=True),
                            options=[
                                Option(
                                    name="member",
                                    description="Member to which a need give ban",
                                    required=True,
                                    type=6
                                ),
                                Option(
                                    name="reason",
                                    description="Ban reason",
                                    required=False,
                                    type=3
                                )
                            ])
    async def ban(self, ctx, member: Member, *, reason: str = None):
        embed_ban = Embed(colour=0xFF9933)
        if member not in ctx.guild.members:
            embed_ban.add_field(name="")
            return await ctx.send()
        if reason is None or reason == "":
            reason = get_lang("ban+ban.default_reason", ctx.guild.id)
        embed_ban.add_field(name=get_lang("ban+ban.success.title", ctx.guild.id),
                            value=get_lang("ban+ban.success.message", ctx.guild.id).format(member.mention, reason))
        await ctx.guild.ban(member, reason=reason, clean_history_duration=0)
        console.info(f"[BAN]> Member {member.name}({member.id}) has banned from {ctx.guild.name}({ctx.guild.id}) for {reason}")
        await ctx.send(embed=embed_ban)

    @commands.slash_command(name="unban",
                            description="Unban a specified member from this server",
                            default_member_permissions=Permissions(ban_members=True),
                            options=[
                                Option(
                                    name="member",
                                    description="Member to which a need remove ban",
                                    required=True,
                                    type=6
                                ),
                                Option(
                                    name="reason",
                                    description="Unban reason",
                                    required=False,
                                    type=3
                                )
                            ])
    async def unban(self, ctx, member: Member, *, reason: str = None):
        if reason is None or reason == "":
            reason = get_lang("ban+unban.default_reason", ctx.guild.id)
        embed_unban = Embed(colour=0xFF9933)
        for ban_entry in ctx.guild.bans():
            if member == ban_entry.user:
                await ctx.guild.unban(member)
            embed_unban.add_field(name=get_lang("ban+unban.success.title", ctx.guild.id),
                                  value=get_lang("ban+unban.success.message", ctx.guild.id).format(member.mention, reason))
            console.info(f"[UNBAN]> Member {member.name}({member.id}) has unbanned from {ctx.guild.name}({ctx.guild.id}) for {reason}")
            return await ctx.send(embed=embed_unban)
        embed_unban.add_field(name=get_lang("ban+unban.error.notfound.title", ctx.guild.id),
                                value=get_lang("ban+unban.error.notfound.message", ctx.guild.id).format(member.mention))
        return await ctx.send(embed=embed_unban)

async def setup(bot):
    await bot.add_cog(Ban(bot))