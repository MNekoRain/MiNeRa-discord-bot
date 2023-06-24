from disnake import Embed, Intents, Permissions, DMChannel
from disnake.ext import commands

from traceback import format_exc
from datetime import datetime
from asyncio import run
from pathlib import Path
from os import listdir
from os.path import abspath, exists

from helpers import console
from helpers.file_manager import FileManager, File
from helpers.property import Property
from lang.language import get_lang


bot = commands.InteractionBot(intents=Intents.all())
config = Property("./data/config.cfg")

CogNames: list[str] = []
Cogs: list[File] = []


def createCogPath(path: str = None):
    return path.replace(abspath(__file__).replace(Path(abspath(__file__)).name, ''), '').replace("\\", ".").replace("/", ".")


def getAllCogs() -> list[File]:
    Cogs.extend(FileManager(dir_path=abspath(".\\cogs")).allFiles())
    return Cogs


@bot.slash_command(name="updatecogbase",
                   description="Update a cog base",
                   default_member_permissions=Permissions(administrator=True))
async def update_cog_base(ctx):
    CogNames.clear()
    Cogs.clear()
    if isinstance(ctx.channel, DMChannel):
        return await ctx.send("Данная командна не может быть использована в Личных Сообщения")
    for cogFile in getAllCogs():
        if cogFile.format == ".py":
            CogNames.append(cogFile.name.replace(cogFile.format, ""))
    
    console.info("[UPDATECOGBASE]> Cog base has been updated")
    for cog in Cogs:
        console.info(f"[UPDATECOGBASE]  {cog.name}")
    await ctx.send("База когов была обновлена")


@bot.slash_command(name="cogload",
                   description="Load an indicated cog",
                   default_member_permissions=Permissions(administrator=True))
async def cog_load(ctx, cog_name):
    embed_cogload = Embed()
    if cog_name in CogNames:
        try:
            for cog in Cogs:
                if cog.name.replace(cog.format, "") == cog_name:
                    bot.load_extension(createCogPath(cog.path.replace(cog.format, "")))
                    console.info(f"[COGLOAD]> Cog {cog_name} has been load")
                    embed_cogload.add_field(name=get_lang("bot+cogload.success.title", ctx.guild.id),
                                            value=get_lang("bot+cogload.success.message", ctx.guild.id).format(cog_name))
                    return await ctx.send(embed=embed_cogload)
        except commands.ExtensionAlreadyLoaded:
            for cog in Cogs:
                if cog.name.replace(cog.format, "") == cog_name:
                    bot.reload_extension(createCogPath(cog.path.replace(cog.format, "")))
                    console.info(f"[COGLOAD]> Cog {cog_name} has been load")
                    embed_cogload.add_field(name=get_lang("bot+cogload.success.title", ctx.guild.id),
                                            value=get_lang("bot+cogload.success.message", ctx.guild.id).format(cog_name))
                    return await ctx.send(embed=embed_cogload)
    else:
        embed_cogload.add_field(name=get_lang("bot+cogload.error.notfound.title", ctx.guild.id),
                                value=get_lang("bot+cogload.error.notfound.message", ctx.guild.id).format(cog_name))
        return await ctx.send(embed=embed_cogload)


@bot.slash_command(name="cogunload",
                   description="Unload an indicated cog",
                   default_member_permissions=Permissions(administrator=True))
async def cog_unload(ctx, cog_name):
    embed_cogunload = Embed()
    if cog_name in CogNames:
        try:
            for cog in Cogs:
                if cog.name.replace(cog.format, "") == cog_name:
                    await bot.unload_extension(createCogPath(cog.path.replace(cog.format, "")))
                    console.info(f"[COGUNLOAD]> Cog {cog_name} has been unload")
                    embed_cogunload.add_field(name=get_lang("bot+cogunload.success.title", ctx.guild.id),
                                              value=get_lang("bot+cogunload.success.message", ctx.guild.id).format(cog_name))
                    return await ctx.send(embed=embed_cogunload)
        except commands.ExtensionNotLoaded:
            embed_cogunload.add_field(name=get_lang("bot+cogunload.success.title", ctx.guild.id),
                                      value=get_lang("bot+cogunload.success.message", ctx.guild.id).format(cog_name))
            return await ctx.send(embed=embed_cogunload)
    else:
        embed_cogunload.add_field(name=get_lang("bot+cogunload.error.notfound.title", ctx.guild.id),
                                  value=get_lang("bot+cogunload.error.notfound.message", ctx.guild.id).format(cog_name))
        return await ctx.send(embed=embed_cogunload)


@bot.slash_command(name="cogreload",
                   description="Reload an indicated cog",
                   default_member_permissions=Permissions(administrator=True))
async def reload(ctx, cog_name):
    embed_cogreload = Embed()
    if cog_name in CogNames:
        try:
            for cog in Cogs:
                if cog.name.replace(cog.format, "") == cog_name:
                    await bot.reload_extension(createCogPath(cog.path.replace(cog.format, "")))
                    console.info(f"[COGRELOAD]> Cog {cog_name} has been reload")
                    embed_cogreload.add_field(name=get_lang("bot+cogreload.success.title", ctx.guild.id),
                                              value=get_lang("bot+cogreload.success.message", ctx.guild.id).format(cog_name))
                    return await ctx.send(embed=embed_cogreload)
        except commands.ExtensionNotLoaded:
            for cog in Cogs:
                if cog.name.replace(cog.format, "") == cog_name:
                    await bot.load_extension(createCogPath(cog.path.replace(cog.format, "")))
                    console.info(f"[COGRELOAD]> Cog {cog_name} has been reload")
                    embed_cogreload.add_field(name=get_lang("bot+cogreload.success.title", ctx.guild.id),
                                              value=get_lang("bot+cogreload.success.message", ctx.guild.id).format(cog_name))
                    return await ctx.send(embed=embed_cogreload)
    else:
        embed_cogreload.add_field(name=get_lang("bot+cogreload.error.notfound.title", ctx.guild.id),
                                  value=get_lang("bot+cogreload.error.notfound.message", ctx.guild.id).format(cog_name))
        await ctx.send(embed=embed_cogreload)
    
    
def cogsLoad():
    now = datetime.now()
    file_name = now.strftime("%d-%m-%Y-%H.err")
    text = ""
    for cogFile in getAllCogs():
        if cogFile.format == ".py":
            CogNames.append(cogFile.name.replace(cogFile.format, ""))
            path = cogFile.path
            try:
                bot.load_extension(createCogPath(path.replace(cogFile.format, "")))
                console.info(f"[COGSLOAD][{cogFile.name.replace(cogFile.format, '').upper()}]  OK")
            except commands.ExtensionNotFound:
                console.error(f"[COGSLOAD][{cogFile.name.replace(cogFile.format, '').upper()}]  NOT FOUND")
            except commands.ExtensionFailed as err:
                console.error(f"[COGSLOAD][{cogFile.name.replace(cogFile.format, '').upper()}]  FAIL")
                text += format_exc() + "\n"
            except commands.ExtensionNotLoaded as err:
                console.error(f"[COGSLOAD][{cogFile.name.replace(cogFile.format, '').upper()}]  NOT LOADED")
                text += format_exc() + "\n"
    if text != "":
        with open(f"./errors/{file_name}", "a" if exists(f"./errors/{file_name}") else "x") as WriteFile:
            WriteFile.write(text)
        console.error(f"[COGSLOAD]  All cogs load errors has been added in file ./errors/{file_name}")


if __name__ == "__main__":
    cogsLoad()
    bot.run(config.get("TOKEN"))
