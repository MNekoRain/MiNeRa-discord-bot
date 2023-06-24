import asyncio
import disnake
from disnake.ext import commands
import datetime
from ..helpers import console, msglog


class LogFile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            now = datetime.now()
            file_name = now.strftime('%d-%m-%Y-%H')
            time = now.strftime('%d.%m.%y %H:%M:%S.%f')
            msg_log = '\n    TYPE: MESSAGE SEND\n    TIME:      {}\n    AUTHOR:   {}\n    AUTHORID: {}\n    MESSAGE:\n{}\n'.format(time, message.author, message.author.id, message.content)
            with open(f'../msglogs/{file_name}.txt', 'a+') as WriteMsgLog:
                WriteMsgLog.write(msg_log)
            return
        except UnicodeEncodeError:
            return console.error('> Error UnicodeEncodeError from msglog.msg_send')
        except UnicodeDecodeError:
            return console.error('> Error UnicodeDecodeError from msglog.msg_send')
        except UnicodeTranslateError:
            return console.error('> Error UnicodeTranslateError from msglog.msg_send')

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        try:
            now = datetime.now()
            file_name = now.strftime('%d-%m-%Y-%H')
            time = now.strftime('%d.%m.%y %H:%M:%S.%f')
            msg_log = '\n    TYPE: MESSAGE EDIT\n    TIME:      {}\n    BEFORE:\n{}\n    AFTER:\n{}\n'.format(time, before.content, after.content)
            with open(f'../msglogs/{file_name}.txt', 'a+') as WriteMsgLog:
                WriteMsgLog.write(msg_log)
            return
        except UnicodeEncodeError:
            return console.error('> Error UnicodeEncodeError from msglog.msg_edit')
        except UnicodeDecodeError:
            return console.error('> Error UnicodeDecodeError from msglog.msg_edit')
        except UnicodeTranslateError:
            return console.error('> Error UnicodeTranslateError from msglog.msg_edit')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        try:
            now = datetime.now()
            file_name = now.strftime('%d-%m-%Y-%H')
            time = now.strftime('%d.%m.%y %H:%M:%S.%f')
            msg_log = '\n    TYPE: MESSAGE DELETE\n    TIME:      {}\n    AUTHOR:   {}\n    AUTHORID: {}\n    CHANNEL: {}\n    CHANNELID: {}\n    MESSAGE: {}\n'.format(time, message.author, message.author.id, message.channel.name, message.channel.id, message.content)
            with open(f'../msglogs/{file_name}.txt', 'a+') as WriteMsgLog:
                WriteMsgLog.write(msg_log)
            return
        except UnicodeEncodeError:
            return console.error('> Error UnicodeEncodeError from msglog.msg_del')
        except UnicodeDecodeError:
            return console.error('> Error UnicodeDecodeError from msglog.msg_del')
        except UnicodeTranslateError:
            return console.error('> Error UnicodeTranslateError from msglog.msg_del')


async def setup(bot):
    await bot.add_cog(LogFile(bot))
