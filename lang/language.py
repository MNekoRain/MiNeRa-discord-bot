from os.path import exists
from json import loads
from sys import exit
from sqlite3 import connect
from ..helpers import console


db = connect("../data/database.db")
db_cur = db.cursor()
db_cur.execute("CREATE IF NOT EXISTS CommandLanguage(guild_id INTEGER, language STRING)")
db.commit()


def get_lang_file() -> dict:
    if exists("./lang.json"):
        with open("./lang.json", "r") as ReadLangFile:
            return loads(ReadLangFile.read())
    else:
        console.error("[GETLANGFILE]> Language file is not exists. Please, reinstall lang.json")
        exit(1)


def get_lang(lang_keys: str, guild_id: int) -> str:
    """
    Returns a text from lang.json

    Arguments
    ----------------
    lang_keys: :class:`str`
        The path ot language in lang.json, exclude language code(ru, en and etc.)\n
        Example: `"bot+cogload.notfound"`
    guild_id: :class:`int`
        The guild ID
    """
    db_cur.execute("SELECT language FROM CommandLanguage WHERE guild_id = ?", (guild_id,))
    try:
        lang_ = db_cur.fetchone()
        if lang is None:
            db_cur.execute("INSERT INTO CommandLanguage(guild_id, language) VALUES(?, ?)", (guild_id, "en"))
            lang = get_lang_file()["en"]
        else:
            lang = get_lang_file()[lang_]
        for lang_key in lang_keys.split("+"):
            lang = lang[lang_key]
    except IndexError:
        console.error("[GETLANG]> Language is not found. Please, reinstall lang.json")
        exit(1)
    else:
        return lang
