import discord

from discord.ext import commands

import keep_alive

bot = commands.Bot(command_prefix='!')

@bot.event

async def on_ready():

    print("我準備好要上戰場了！！！")

@bot.event

async def on_member_join(member):

    channel = bot.get_channel(759677671448772618)

    await channel.send(f'歡迎{member}加入小N的粉絲團!! :yum: :yum: :yum:')

@bot.event

async def on_member_remove(member):

    channel = bot.get_channel(759677810674630656)

    await channel.send(f'{member}和我們說88 :cry: :cry: :cry: ')

@bot.command()

async def hi(ctx):

    await ctx.send("叫我嗎？ :face_with_monocle: :face_with_monocle::face_with_monocle:")

@bot.command()

async def 安安(ctx):

    await ctx.send("安安")

    await ctx.send("~~~")

@bot.command()

async def yt(ctx):

    await ctx.send("https://www.youtube.com/c/小Nsmalln")

@bot.command()

async def youtube(ctx):

    await ctx.send("https://www.youtube.com/c/小Nsmalln")

@bot.command()

async def 贊助(ctx):

    await ctx.send("https://payment.ecpay.com.tw/Broadcaster/Donate/9B054FBC4A03403D5489B8F13F46F887")

@bot.command()

async def ig(ctx):

    await ctx.send("https://www.instagram.com/wu_ming1/?hl=zh-tw")

@bot.command()

async def 粉絲專頁(ctx):

    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()

async def fb(ctx):

    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()

async def facebook(ctx):

    await ctx.send("https://m.facebook.com/RMSmallN/")

@bot.command()

async def 指令製作(ctx):

    await ctx.send("猴子@3807")

@bot.command()

async def n(ctx):

  await ctx.send("哈囉我叫史邁恩(小N)，每周一三五禮拜日晚上6:30在Youtube遊戲頻道不定期更新！記得訂閱開小鈴鐺bell")

@bot.command()

async def N(ctx):

  await ctx.send("哈囉我叫史邁恩(小N)，每周一三五禮拜日晚上6:30在Youtube遊戲頻道不定期更新！記得訂閱開小鈴鐺bell")

@bot.command()

async def ping(ctx):

    await ctx.send(f'{round(bot.latency*1000)}[ms]')

@bot.command()

async def say(ctx, *, arg):

    await ctx.message.delete()

    await ctx.send(arg)

@bot.command()

async def sos(ctx):

    embed=discord.Embed(title="指令說明", color=0xff0000)

    embed.add_field(name="ping", value="顯示我的延遲", inline=True)

    embed.add_field(name="youtube", value="顯示小N的yt", inline=True)

    embed.add_field(name="yt", value="顯示小N的yt", inline=True)

    embed.add_field(name="facebook", value="顯示小N的FB", inline=True)

    embed.add_field(name="fb", value="顯示小N的FB", inline=True)

    embed.add_field(name="ig", value="顯示小N的IG", inline=True)

    embed.add_field(name="N", value="顯示小N的資料", inline=True)

    embed.add_field(name="n", value="顯示小N的資料", inline=True)

    embed.add_field(name="粉絲專頁", value="顯示小N的FB", inline=True)

    embed.add_field(name="hi", value="想和我聊天？？？", inline=True)

    embed.add_field(name="贊助", value="贊助小N", inline=True)

    embed.add_field(name="sos", value="顯示該表", inline=True)

    embed.add_field(name="help", value="顯示help", inline=True)

    embed.set_footer(text="作者：猴子@3807")

    await ctx.send(embed= embed)

keep_alive.keep_alive()

bot.run（'不告訴你勒~~~'）
