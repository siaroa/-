import discord, asyncio

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("!명령어"))

@client.event
async def on_message(message):
    if message.content == "::::": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

# 봇을 실행시키기 위한 토큰을 작성해주는 곳
client.run('OTI4NDMwMzU3NTA4OTMxNjM0.YdYqJg.kzmFgYu5sBBCG0HVPYob35S64f0')

