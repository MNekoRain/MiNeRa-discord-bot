from disnake import Role, Member, Embed, Permissions, Option
from disnake.ext import commands
from ..helpers import console
from lang.language import get_lang


class Role(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="role",
                            description="Add or remove a role to member",
                            default_member_permissions=Permissions(administrator=True),
                            options=[
                                Option(
                                    name="action",
                                    description="Add or remove role",
                                    choices=[
                                        "Add",
                                        "Remove"
                                    ],
                                    required=True,
                                    type=3
                                ),
                                Option(
                                    name="role",
                                    description="Role which need add or remove to member",
                                    required=True,
                                    type=8
                                ),
                                Option(
                                    name="member",
                                    description="Member which need add or remove a role",
                                    required=True,
                                    type=6
                                )
                            ])
    async def add_role(self, ctx, action: str, role: Role, member: Member):
        embed_role = Embed()
        if action == "Add":
            embed_role.add_field(name=get_lang("role+role.success.title", ctx.guild.id),
                                 value=get_lang("role+role.success.message.add", ctx.guild.id).format(member.mention, role.name))
            await member.add_roles(role)
            console.info(f'[ROLE]> To member {member.name} added a role {role.name} with ID {role.id} on {ctx.guild.name}({ctx.guild.id})')
            return await ctx.reply(embed=embed_role)
        else:
            embed_role.add_field(name=get_lang("role+role.success.title", ctx.guild.id),
                                 value=get_lang("role+role.success.message.remove", ctx.guild.id).format(member.mention, role.name))
            await member.remove_roles(role)
            console.info(f'[ROLE]> With member {member.name} removed a role {role.name} with ID {role.id} on {ctx.guild.name}({ctx.guild.id})')
            return await ctx.reply(embed=embed_role)


async def setup(bot):
    await bot.add_cog(Role(bot))