from datetime import datetime
import helpers.console as console


def msg_send(message):
    try:
        now = datetime.now()
        file_name = now.strftime('%d-%m-%Y-%H')
        time = now.strftime('%d.%m.%y %H:%M:%S.%f')
        msg_log = '\n    TYPE: SEND\n    TIME:      {}\n    AUTHOR:   {}\n    AUTHORID: {}\n    MESSAGE:\n{}\n)\n'.format(time, message.author, message.author.id, message.content)
        with open(f'msglogs/{file_name}.txt', 'a+') as WriteMsgLog:
            WriteMsgLog.write(msg_log)
        return console.info('> Сообщение написано')
    except UnicodeEncodeError:
        return console.error('> Error UnicodeEncodeError from msglog.msg_send')
    except UnicodeDecodeError:
        return console.error('> Error UnicodeDecodeError from msglog.msg_send')
    except UnicodeTranslateError:
        return console.error('> Error UnicodeTranslateError from msglog.msg_send')

def msg_edit(before, after):
    try:
        now = datetime.now()
        file_name = now.strftime('%d-%m-%Y-%H')
        time = now.strftime('%d.%m.%y %H:%M:%S.%f')
        msg_log = '\n    TYPE: MESSAGE EDIT\n    TIME:      {}\n    BEFORE:\n{}\n    AFTER:\n{}\n'.format(time, before.content, after.content)
        with open(f'msglogs/{file_name}.txt', 'a+') as WriteMsgLog:
            WriteMsgLog.write(msg_log)
        return console.info('> Сообщение изменено')
    except UnicodeEncodeError:
        return console.error('> Error UnicodeEncodeError from msglog.msg_edit')
    except UnicodeDecodeError:
        return console.error('> Error UnicodeDecodeError from msglog.msg_edit')
    except UnicodeTranslateError:
        return console.error('> Error UnicodeTranslateError from msglog.msg_edit')

def typing(channel, member, when):
    try:
        now = datetime.now()
        file_name = now.strftime('%d-%m-%Y-%H')
        time = now.strftime('%d.%m.%y %H:%M:%S.%f')
        msg_log = '(\n    TYPE: TYPING\n    TIME:      {}\n    AUTHOR:   {}\n    AUTHORID: {}\n    CHANNEL: {}\n    CHANNELID: {}\n)\n'.format(time, member, member.id, channel.name, channel.id)
        with open(f'msglogs/{file_name}.txt', 'a+') as WriteMsgLog:
            WriteMsgLog.write(msg_log)
        return console.info(f'> Пользователь {member} печатает')
    except UnicodeEncodeError:
        return console.error('> Error UnicodeEncodeError from msglog.typing')
    except UnicodeDecodeError:
        return console.error('> Error UnicodeDecodeError from msglog.typing')
    except UnicodeTranslateError:
        return console.error('> Error UnicodeTranslateError from msglog.typing')

def msg_del(message):
    try:
        now = datetime.now()
        file_name = now.strftime('%d-%m-%Y-%H')
        time = now.strftime('%d.%m.%y %H:%M:%S.%f')
        msg_log = '\n    TYPE: MESSAGE DELETE\n    TIME:      {}\n    AUTHOR:   {}\n    AUTHORID: {}\n    CHANNEL: {}\n    CHANNELID: {}\n    MESSAGE: {}\n'.format(time, message.author, message.author.id, message.channel.name, message.channel.id, message.content)
        with open(f'msglogs/{file_name}.txt', 'a+') as WriteMsgLog:
            WriteMsgLog.write(msg_log)
        return console.info('> Сообщение удалено')
    except UnicodeEncodeError:
        return console.error('> Error UnicodeEncodeError from msglog.msg_del')
    except UnicodeDecodeError:
        return console.error('> Error UnicodeDecodeError from msglog.msg_del')
    except UnicodeTranslateError:
        return console.error('> Error UnicodeTranslateError from msglog.msg_del')