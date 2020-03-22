import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        await client.change_presence(activity=discord.Game(name="도우미"))

        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        elif message.content == '!서버주소':
            embed = discord.Embed(title="서버주소", description="dgdgdgdg_sw.aternos.me", color=0x00ff00)
            await message.channel.send(embed=embed)

client = MyClient()
client.run('NjkxMTk4MzY0OTc2Njc2ODY0.Xnce-g.GwaP6H0_DS1oAi5oYYipj31o2Cs')
