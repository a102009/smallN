
import discord
import keep_alive
from discord.ext import commands
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Message, PartialEmoji
#intents = discord.intents.defaulf()

bot = commands.Bot(command_prefix='sn!', description='一個向用戶致意的機器人。')

#owner_id=688181698822799414,                            
    # 您的唯一用戶ID

@bot.event
async def on_ready():
    print("我準備好要上戰場了！！！")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    activity = discord.Game(name="sn!", type=3)
    activity = discord.Game(name="sn!", flixype=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    await bot.change_presence(status=discord.Status.idle, activity=activity)

@bot.event
async def on_member_join(member):
  print(f"join{member}")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(759677810674630656)
    await channel.send(f'@{member} 和我們說88 :cry: :cry: :cry: ')
    print(f"remove{member}")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="好用的機器人", description="我多默好用～～～", color=0xeee657)
    
    # 在这里提供关于您的信息
    embed.add_field(name="作者", value="<@猴子#3807>")
    
    # 显示机器人所服务的数量。
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
    await ctx.send(embed=embed)

@bot.command()
async def dc(ctx):
  await ctx.send("https://discord.gg/CPt8WZu")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}[ms]')

@bot.command()
async def youtube(ctx):
    await ctx.send("https://www.youtube.com/c/小Nsmalln")

@bot.command()
async def dog(ctx):
    await ctx.send("小N好帥對不對！！ 一定要說對歐！！！")
    await ctx.send("旺！旺！旺！")
    await ctx.send(":dog: :dog: :dog: ")
@bot.command()
async def ytgo(ctx):
    await ctx.send("https://tw.noxinfluencer.com/youtube/realtime-subs-count/UC-HfdvueCHBZ2yUhodirqmA")
  
@bot.command()
async def no(ctx):
    await ctx.send("別玩啦～～～")

@bot.command()
async def yt(ctx):
    await ctx.send("https://www.youtube.com/c/小Nsmalln")

@bot.command()
async def 粉絲專頁(ctx):
    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()
async def facebook(ctx):
    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()
async def fb(ctx):
    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()
async def ig(ctx):
    await ctx.send("https://www.instagram.com/wu_ming1/?hl=zh-tw")

@bot.command()
async def hi(ctx):
    await ctx.send("叫我嗎？ :face_with_monocle: :face_with_monocle: :face_with_monocle:")

@bot.command()
async def qq(ctx):
  await ctx.send('https://store.line.me/stickershop/product/3206865/zh-Hant')

@bot.command()
async def QQ(ctx):
  await ctx.send('https://store.line.me/stickershop/product/3206865/zh-Hant')

@bot.command()
async def hihi(ctx):
    await ctx.send("各位好")

@bot.command()
async def 贊助(ctx):
    await ctx.send("https://payment.ecpay.com.tw/Broadcaster/Donate/9B054FBC4A03403D5489B8F13F46F887")

@bot.command()
async def N(ctx):
  await ctx.send("哈囉我叫史邁恩(小N)，每周一三五禮拜日晚上6:30在Youtube遊戲頻道不定期更新！記得訂閱開小鈴鐺bell")

@bot.command()
async def n(ctx):
  await ctx.send("哈囉我叫史邁恩(小N)，每周一三五禮拜日晚上6:30在Youtube遊戲頻道不定期更新！記得訂閱開小鈴鐺bell")

@bot.command()
async def 安安(ctx):
    await ctx.send("安安")
    await ctx.send("~~~")

@bot.command()
async def say(ctx, *, arg):
    await ctx.message.delete()
    await ctx.send(arg)

@bot.command()
async def 指令製作(ctx):
    await ctx.send("猴子@3807")

@bot.command()
async def m(ctx, *, arg):
    await ctx.author.send(arg)
    await ctx.send("想和我聊天我？？")
    await ctx.send("早說麼!!")
    
@bot.command()
async def sos(ctx):
    embed=discord.Embed(title="指令說明 前綴為sn!", color=0xff0000)

    embed.add_field(name="ping", value="顯示我的延遲", inline=True)
    embed.add_field(name="youtube,yt", value="顯示小N的yt", inline=True)  
    embed.add_field(name="ytgo", value="即時定閱人數", inline=True)
    embed.add_field(name="粉絲專頁", value="顯示小N的FB", inline=True)
    embed.add_field(name="facebook", value="顯示小N的FB", inline=True)
    embed.add_field(name="fb", value="顯示小N的FB", inline=True)
    embed.add_field(name="ig", value="顯示小N的IG", inline=True)
    embed.add_field(name="贊助", value="贊助小N", inline=True)
    embed.add_field(name="QQ", value="想要小N的Q版貼圖嗎那打我吧！！", inline="True")
    embed.add_field(name="dog", value="我好狗腿", inline=True)
    embed.add_field(name="help", value="顯示help", inline=True)
    embed.add_field(name="sos", value="顯示該表", inline=True)
    embed.add_field(name="N", value="顯示小N的資料", inline=True)
    embed.add_field(name="n", value="顯示小N的資料", inline=True)
    embed.add_field(name="no", value="打打看就知道～～～", inline=True)
    embed.add_field(name="say", value="!say 加要我說的話", inline=True)
    embed.add_field(name="安安", value="和我聊天", inline=True)
    embed.add_field(name="hi", value="想和我聊天？？？", inline=True)
    embed.add_field(name="指令製作", value="顯示指令製作人", inline=True)
    embed.set_footer(text="作者：猴子@3807")

    await ctx.send(embed= embed)


keep_alive.keep_alive()
bot.run('秘密')
