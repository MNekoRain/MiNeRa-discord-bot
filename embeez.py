from curses.ascii import EM
import discord
import console

class D:
    def __init__(self, *, desc=None, tit=None, color=0xFFFFFF, url=None):
        self.class_='D'
        self.desc=desc
        self.tit=tit
        self.color=color
        self.url=url
        self.pictureFormats=['.png','.jpg','.jpeg','.gif','.bmp','.ecw','.ico','.ilbm','.pcx','.psd','.tga','.tiff','.jfif','.webp','.xbm','.xps','.rla','.rpf','.pnm']

    def DEmb(self):
        EMBED=discord.Embed(description=self.desc, title=self.tit, color=self.color, url=self.url)
        return EMBED
    
    def adFie(self, name="", value="", *, inline:bool):
        EMBED=D.DEmb()
        if inline==None: EMBED.add_field(name=name, value=value)
        else: EMBED.add_field(name=name, value=value, inline=inline)

    def Auth(self, name="", *, icUrl=None, url=None):
        EMBED=D.DEmb()
        if icUrl==None:
            if url==None: EMBED.set_author(name=name)
            elif url!=str: raise TypeError('Где тут текст?')
            elif (url.startswith("http://")) or (url.startswith("https://")): EMBED.set_author(name=name, url=url)
            else: console.e("> embez.py    Произошла неизвестная ошибка")
        else:
            if url==None: EMBED.set_author(name=name, icUrl=icUrl)
            elif url!=str: raise TypeError('Где тут текст?')
            elif (url.startswith("http://")) or (url.startswith("https://")): EMBED.set_author(name=name, url=url)
            else: console.e("> embez.py    Произошла неизвестная ошибка")
    
    def tbnail(self, url=""):
        EMBED=D.DEmb()
        if ((url.startswith("http://")) or (url.startswith("https://"))) and (url.endswith() in self.pictureFormats): EMBED.set_thumbnail(url=url)
        else: return console.e('Блятб, где тут ссылка/картинка?')

        
    def sFoot(self, text=""):
        EMBED=D.DEmb()
        EMBED.ser_footer(text=text)
        

if __name__=="__main__": raise SystemExit('Это модуль, а не основной файл! йинеГ')
