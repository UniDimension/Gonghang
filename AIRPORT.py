import discord
import os
from datetime import datetime, timedelta


client = discord.Client()



@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("인천공항 매입")
    await client.change_presence(status=discord.Status.online, activity=game)




@client.event
async def on_message(message):

    if message.content.startswith("/안녕"):
        await message.channel.send("뭐 이 스바시키야~!")

    if message.content.startswith("/잘가"):
        await message.channel.send("너 삘 받았어? 삘 받았잖아")

    if message.content.startswith("/도움말"):
        await message.channel.send("명령어 목록 : /안녕, /잘가, /투표, /자기소개, /채널메시지, /DM, ... 이외의 재밌는 요소들")

    if message.content.startswith("/엄준식"):
        await message.channel.send(" 니.. 니가 언제부터 준식이를 매입했는데 스바 그지시키야~!")

    if message.content.startswith("/옵"):
        await message.channel.send("https://www.op.gg")
    
    if message.content.startswith("/뿅"):
        await message.channel.send(file=discord.File("뿅.png"))

    if message.content.startswith("/ㅅㅂ"):
        await message.channel.send(file=discord.File("ㅅㅂ.png"))

    if message.content.startswith("/삼위일체"):
        await message.channel.send(file=discord.File("삼위일체.png"))

    if message.content.startswith("/ㄱㅎ"):
        await message.channel.send(file=discord.File("같행.png"))

    if message.content.startswith("/빠다"):
        await message.channel.send(file=discord.File("나비.png"))

    if message.content.startswith("/자기소개"):
        embed = discord.Embed(title="공항도둑", description="뭘 꼬라봐 스바시키야~!", color=0x00ff56)
        embed.set_author(name="이름", url="https://www.youtube.com/watch?v=PjyvA6jaKtI",
                         icon_url="https://cdn.discordapp.com/attachments/749322138472677500/750245520643194930/cb4678071e68371b.jpeg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/749322138472677500/750245518415757312/07eda5bf1fd558d3.jpeg")
        embed.add_field(name="사는 곳", value="인천국제공항", inline=True)
        embed.add_field(name="생년월일", value="2014년 4월 13일", inline=True)
        embed.add_field(name="학력", value="초등학교 졸업", inline=True)
        embed.add_field(name="기분", value="FEEL 받았잖아", inline=True)
        embed.set_footer(text="(ㄴ.. 니가 언제 내 정보를 매입했는데)")
        await message.channel.send(embed=embed)

    if message.content.startswith("/채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("/투표"):
        vote = message.content[4:].split("/")
        await message.channel.send("★투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            await choose.add_reaction('👍')

    

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
