from disnake import Permissions, Option, Embed
from disnake.ext import commands
from lang.language import db, db_cur, get_lang


class Language(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(name="changelang",
                            description="Change a bot language for this guild",
                            default_member_permissions=Permissions(administrator=True),
                            options=[
                                Option(
                                    name="lang",
                                    description="A bot language",
                                    choices=[
                                        "English",
                                        "Русский"
                                    ],
                                    required=True,
                                    type=3
                                )
                            ])
    async def change_lang(self, ctx, lang: str):
        lang_code = {"English": "en", "Русский": "ru"}[lang]
        db_cur.execute("UPDATE CommandLanguage SET language = ? WHERE guild_id = ?", (lang_code, ctx.guild.id))
        db.commit()
        db_cur.execute("SELECT language FROM CommandLanguage WHERE guild_id = ?", (ctx.guild.id))
        if db_cur.fetchone != lang_code:
            db_cur.execute("INSERT INTO CommandLanguage(id, language) VALUES(?, ?)", (ctx.guild.id, lang_code))
        embed_changelang = Embed()
        embed_changelang.add_field(name=get_lang("lang+changelang.success.title", ctx.guild.id),
                                   value=get_lang("lang+changelang.success.message", ctx.guild.id).format(lang))
        return await ctx.send(embed=embed_changelang)


def setup(bot):
    bot.add_cog(Language(bot))
