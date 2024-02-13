import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send(f'**Merhaba {bot.user}! Ben çevre hakkında bilgili bir botum!**')
    time.sleep(1)
    await ctx.send(f'**Çevre Hakkında Sormak İstediğin Birşey Varmı?!**')


@bot.command()
async def chat(ctx):
    await ctx.send(f'**Merhaba! Hadi Çevre hakkında konuşalım???**')

@bot.command()
async def cevre(ctx):
    await ctx.send(f'**Çevre Ve Kirlilik Hakkında bir Şey Öğrenmek istiyorsanız /bilgi Komutunu Kullanın Ve Eğer Çöplerin Doğada NE Kadar Sürede Yok Olduğunu Öğrenmek İsterseniz /zaman Komudunu Kullanın!**')

@bot.command()
async def zaman(ctx):
    await ctx.send(f'**Bir Elma Ortalama 2 Ay İçerisinde Doğada Yok Olur.**')
    time.sleep(1.5)
    await ctx.send(f'**Plastik Bir Şişe İse Ortalama 450 Yıl Sürer.**')
    time.sleep(1.5)
    await ctx.send(f'**Bebek Bezlerin Doğada Yok Olma Süresi İse 550 Yıldır.**')
    time.sleep(1.5)
    await ctx.send(f'**Aliminyum Kutular 200 ve 300 Yıllar Arasında Doğada Yok Olur.**')
    time.sleep(1.5)
    await ctx.send(f'**Ayrıca Doğada Yok Olması En Uzun Süren Malzeme İse Strafor 2 Milyon Yıl Sürer. (Bu Çok Fazla Deilmi?)**')

@bot.command()
async def bilgi(ctx):
    await ctx.send(f'**Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın')
    time.sleep(1.3)
    await ctx.send(f'**Eski eşyaları çöpe atmak yerine geri dönüştürün')
    time.sleep(1.3)
    await ctx.send(f'**Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.**')
    time.sleep(1.3)
    await ctx.send(f'**Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.**')
    time.sleep(1.3)
    await ctx.send(f'**Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.**')
    time.sleep(1.3)
    await ctx.send(f'**Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın.**')
    time.sleep(1.3)
    await ctx.send(f'**Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.**')
    time.sleep(1.3)
    await ctx.send(f'**Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve kullanmaya çalışın.**')

@bot.command()
async def resim(ctx):
    with open(r'PLant4Life\Photos\resim.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(1)
    await ctx.send(f'**Hep birlikte tercih ve alışkanlıklarımızı değiştirerek çevre kirliliği sorununu çözmeye çalışalım ve dünyamızı temiz tutalım.**')


bot.run("MTIwNzAwMTA4ODkzNTMyOTg4Mg.G7vZCW.u7PiDQ3VjtaSUUAhhs-Ro_lS-rKogBt532cJqk")
