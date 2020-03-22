import discord
import asyncio
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')

token = 'NjkxMjU5MjU2NTA2MTU1MDA4.XndXbg.Be4vuSERBjBFvQb0ihxD1lPAPuM'

@client.event
async def on_ready():
    print('Logged is as')
    await client.change_presence(activity=discord.Game(name="!a for help"))

@bot.event
async def on_ready():
    print('곧 실행됩니다...')

@bot.command()
async def 서버주소(ctx):
    await ctx.send("dgdgdgdg_sw.aternos.me")

@bot.command()
async def 이승호(ctx):
    await ctx.send("어으으으으ㅡㅡㅡㅡ씨")

@bot.command()
async def 핑(ctx):
    latency = bot.latency
    await ctx.send(f'퐁! {round(latency * 1000)}ms')

bot.run(token)
client.run(token)
