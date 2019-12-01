import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    bid = (str(client.user.id))
    print("봇 이름 : " + bid)
    bname = client.user.name
    print("봇이름 : " + bname)
    print("MMMBot STAR")
    game = discord.Game("테스트중")
    await client.change_presence(status=discord.Status.idle, activity=game) #빨간불,노란불,초록불=offline,idle,online


@client.event
async def on_message(message):
    if message.content.startswith("!설정"):
        if message.channel.id == 650661788731572245:
            channel = 650691625818783775
            author = message.guild.get_member(int(message.author.id))
            role = discord.utils.get(message.guild.roles, name=message.content.split(" ")[1])
            job = discord.utils.get(message.guild.roles, name=message.content.split(" ")[2])
            await author.add_roles(role)
            await author.add_roles(job)
            embed = discord.Embed(color=0xFF5E00, title="프로필")
            embed.add_field(name="서버닉네임",value=message.author.display_name, inline=True)
            embed.add_field(name="서버", value=role, inline=True)
            embed.add_field(name="직업군", value=job, inline=True)
            embed.set_thumbnail(url=message.author.avatar_url)
            await author.send(embed=embed)
            await client.get_channel(channel).send("\n새로운 메이플월드의 용사 " + message.author.display_name +"님 환영합니다.")
            await client.get_channel(channel).send(embed=embed)

    if message.content.startswith("!정보"):
        embed = discord.Embed(color=0xFF5E00, title="프로필")
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="서버", value=message.author.roles[2], inline=True)
        embed.add_field(name="직업군", value=message.author.roles[1], inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

acces_token = os.environ["BOT_TOKEN"]
client.run("acces_token")
