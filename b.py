from discord import Embed, Intents
from discord.ext import commands

from asyncio import run
from os import listdir
from json import loads
import console

with open("config.json", "r") as f:
    config_json = f.read()
cfg = loads(config_json)

console.info(f'Токен:   {cfg["TOKEN"]}')
console.info(f'Префикс: {cfg["PREFIX"]}')

bot = commands.Bot(command_prefix=f'{cfg["PREFIX"]}', case_insensitive=True, intents=Intents().all())
bot.remove_command('help')


@bot.command
async def load(ctx, extension):
    if ctx.author.id == 618426320535420938:
        await bot.load_extension(f"cogs.{extension}")
        console.info("[COGS]> ЗАГРУЗКА...")
        emblc = Embed()
        emblc.add_field(name="⚙│ Коги │⚙",
                        value="Коги загружены!")
        await ctx.reply(embed=emblc)
    else:
        embno = Embed()
        embno.add_field(name="⚠│ Ошибка │⚠",
                        value="Вы не владелец бота!")
        await ctx.reply(embed=embno)


@bot.command
async def unload(ctx, extension):
    if ctx.author.id == 618426320535420938:
        await bot.unload_extension(f"cogs.{extension}")
        console.info("[COGS]> ВЫГРУЗКА...")
        emblc = Embed()
        emblc.add_field(name="⚙│ Коги │⚙",
                        value="Коги выгружены!")
        await ctx.reply(embed=emblc)
    else:
        embno = Embed()
        embno.add_field(name="⚠│ Ошибка │⚠",
                        value="Вы не владелец бота!")
        await ctx.reply(embed=embno)


@bot.command
async def reload(ctx, extension):
    if ctx.author.id == 618426320535420938:
        await bot.unload_extension(f"cogs.{extension}")
        await bot.load_extension(f"cogs.{extension}")
        console.info("[COGS]> ПЕРЕЗАГРУЗКА...")
        emblc = Embed()
        emblc.add_field(name="⚙│ Коги │⚙",
                        value="Коги перезагружены!")
        await ctx.reply(embed=emblc)
    else:
        embno = Embed()
        embno.add_field(name="⚠│ Ошибка │⚠",
                        value="Вы не владелец бота!")
        await ctx.reply(embed=embno)


async def cogsload():
    for filename in listdir("./cogs"):
        try:
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
        except BaseException:
            console.error(f"[COGS]> {filename}        ERROR")
            console.error(f"[COGS]> {filename}        ERROR")
            console.error(f"[COGS]> {filename}        ERROR")
            console.error(f"[COGS]> {filename}        ERROR")

run(cogsload())
bot.run(f'{cfg["TOKEN"]}')
