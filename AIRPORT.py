import discord
from datetime import datetime, timedelta
from riotwatcher import LolWatcher

client = discord.Client()
lol_watcher = LolWatcher('RGAPI-415691a1-8c13-4106-847f-cee7089f5062')
my_region = 'kr'
OKS = lol_watcher.summoner.by_name(my_region, '오크스')
LMJ = lol_watcher.summoner.by_name(my_region, '응 안할꺼야 수고')
spectator = None


def lolspect(me):
    try:
        spectator = lol_watcher.spectator.by_summoner(my_region, me['id'])
        start_time = datetime.fromtimestamp(spectator['gameStartTime'] / 1000)
        if datetime.now() - start_time < timedelta(hours=1):
            return "너 롤하잖아. Feel 받았잖아"
    except:
        return "니가 언제부터 유유자적을 매입했냐 스바시키야~! "


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
        await message.channel.send("명령어 목록 : /안녕, /잘가, /최강원딜강원, /최강로리민준, /투표, /옵")

    if message.content.startswith("/엄준식"):
        await message.channel.send(" 니.. 니가 언제부터 준식이를 매입했는데 스바 그지시키야~!")

    if message.content.startswith("/옵"):
        await message.channel.send("https://www.op.gg")

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

    if message.content.startswith("/최강원딜강원"):
        res = lolspect(OKS)
        await message.channel.send(res)

    if message.content.startswith("/최강로리민준"):
        res = lolspect(LMJ)
        await message.channel.send(res)


client.run("NzQ5MzE4MDkyOTk1Mjk3Mzgw.X0qO2w.tNLPEcuUA6tIknd0ouqmsS_3v_w")
