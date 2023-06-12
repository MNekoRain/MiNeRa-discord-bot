import discord
import datetime
import console


def msg_send(message):
        if message.channel.id==854430505037987871:
            return
        else:
            try:
                now=datetime.datetime.now()
                fn=now.strftime('%Y.%d.%w')
                tt=now.strftime('[%H:%M:%S.%f]')
                LogT='(\n    TYPE: SEND\n    TIME:      {}\n    AUTHOR:   {}\n    AUTHORID: {}\n    MESSAGE:\n{}\n)\n'.format(tt,message.author,message.author.id,message.content)
                with open(f'LOG/{fn}.txt','a+') as fLT:
                    fLT.write(LogT)
                return console.info('> Сообщение написано')
            except UnicodeEncodeError:
                return console.error('> Action: Send    ERROR: UnicodeEncodeError')
            except UnicodeDecodeError:
                return console.error('> Action: Send    ERROR: UnicodeDecodeError')
            except UnicodeTranslateError:
                return console.error('> Action: Send    ERROR: UnicodeTranslateError')

def msg_edit(before, after):
    try:
        now=datetime.datetime.now()
        fn=now.strftime('%Y.%d.%w')
        tt=now.strftime('[%H:%M:%S.%f]')
        LogT='(\n    TYPE: EDIT\n    TIME:      {}\n    BEFORE:\n{}\n    AFTER:\n{}\n)\n'.format(tt,before.content,after.content)
        with open(f'LOG/{fn}.txt','a+') as fLT:
            fLT.write(LogT)
        return console.info('> Сообщение изменено')
    except UnicodeEncodeError:
        return console.error('> Action: Edit    ERROR: UnicodeEncodeError')
    except UnicodeDecodeError:
        return console.error('> Action: Edit    ERROR: UnicodeDecodeError')
    except UnicodeTranslateError:
        return console.error('> Action: Edit    ERROR: UnicodeTranslateError')

def typing(channel, member, when):
    if channel.id==854430505037987871:
        return
    else:
        try:
            now=datetime.datetime.now()
            fn=now.strftime('%Y.%d.%w')
            tt=now.strftime('[%H:%M:%S.%f]')
            LogT='(\n    TYPE: TYPING\n    TIME:      {}\n    AUTHOR:   {}\n    AUTHORID: {}\n    CHANNEL: {}\n    CHANNELID: {}\n)\n'.format(tt,member,member.id,channel.name,channel.id)
            with open(f'LOG/{fn}.txt','a+') as fLT:
                fLT.write(LogT)
            return console.info(f'> Пользователь {member} печатает')
        except UnicodeEncodeError:
            return console.error('> Action: Typing    ERROR: UnicodeEncodeError')
        except UnicodeDecodeError:
            return console.error('> Action: Typing    ERROR: UnicodeDecodeError')
        except UnicodeTranslateError:
            return console.error('> Action: Typing    ERROR: UnicodeTranslateError')

def msg_del(message):
        if message.channel.id==854430505037987871:
            return
        else:
            try:
                now=datetime.datetime.now()
                fn=now.strftime('%Y.%d.%w')
                tt=now.strftime('[%H:%M:%S.%f]')
                LogT='(\n    TYPE: DELETE\n    TIME:      {}\n    AUTHOR:   {}\n    AUTHORID: {}\n    CHANNEL: {}\n    CHANNELID: {}\n    MESSAGE: {}\n)\n'.format(tt,message.author,message.author.id,message.channel.name,message.channel.id,message.content)
                with open(f'LOG/{fn}.txt','a+') as fLT:
                    fLT.write(LogT)
                return console.info('> Сообщение удалено')
            except UnicodeEncodeError:
                return console.error('> Action: Delete    ERROR: UnicodeEncodeError')
            except UnicodeDecodeError:
                return console.error('> Action: Delete    ERROR: UnicodeDecodeError')
            except UnicodeTranslateError:
                return console.error('> Action: Delete    ERROR: UnicodeTranslateError')