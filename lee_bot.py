import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    await client.change_presence(activity=discord.Game(name="이승호 염탐"))

@client.event
async def on_message(message):
    if message.content.startswith('!서버주소'):
        embed = discord.Embed(title="서버주소", description="dgdgdgdg_sw.aternos.me", color=0x00ff00)
        await message.channel.send(embed=embed)

    elif message.content.startswith('!이승호'):
        embed = discord.Embed(description="어으으으ㅡㅡㅡㅡ씨", color=0xff0000)
        await message.channel.send(embed=embed)

    elif message.content.startswith('!명령어'):
        embed = discord.Embed(title="명령어 모음")
        embed.add_field(name="!서버주소", value="마크 서버주소를 알려줍니다.", inline=False)
        embed.add_field(name="!이승호", value="말 그대로 이승호입니다.", inline=False)
        await message.channel.send(embed=embed)


client.run('NjkxMjQ3NzI3MzcxMDkyMDA4.XndMuw.yP9CaunLYMqdOQMzhSgnN9hm4qA')
