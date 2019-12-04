import discord
import os
import requests
from bs4 import BeautifulSoup
import openpyxl

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
            try:
                role = discord.utils.get(message.guild.roles, name=message.author.display_name.split("/")[1])
            except IndexError:
                await message.channel.send("서버설정에 실패하였습니다.\n#설정관련공지 를 읽어주세요!!")
                return
            file = openpyxl.load_workbook("레벨.xlsx")
            sheet = file.active
            i = 1
            await author.add_roles(role)
            embed = discord.Embed(color=0xFF5E00, title="프로필")
            embed.add_field(name="서버닉네임", value=message.author.display_name.split("/")[0], inline=True)
            embed.add_field(name="서버", value=role, inline=True)
            embed.add_field(name="레벨", value=1, inline=True)
            embed.set_thumbnail(url=message.author.avatar_url)
            await author.send(embed=embed)
            await client.get_channel(channel).send("\n새로운 메이플월드의 용사 " + message.author.display_name.split("/")[0] + "님 환영합니다.")
            await client.get_channel(channel).send(embed=embed)

    if message.content.startswith("!정보"):
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        i = 1
        embed = discord.Embed(color=0xFF5E00, title="프로필")
        embed.add_field(name="서버닉네임", value=message.author.display_name.split("/")[0], inline=True)
        embed.add_field(name="서버", value=message.author.roles[1], inline=True)
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                embed.add_field(name="레벨", value=sheet["C" + str(i)].value, inline=True)
                break
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("") and message.author.id !=650647451560050689:
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [10, 20, 30, 40, 50,70,100,130,160,200,240,280,320,400,500,600,800,1000,1500,2000,2500,3000,4000,5000,7000,10000,15000,20000,30000]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 5
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await message.channel.send("레벨이 올랐습니다.\n 현재레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet["B" + str(i)].value))
                file.save("레벨.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("레벨.xlsx")
                break
            i += 1

    if message.content.startswith("!한강"):
        request = requests.get('https://www.wpws.kr/hangang/')
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        links = str(soup.select('#temp')).split("</i>")[1].split("</p>")[0]
        await message.channel.send("현재온도 : " + links + "\n:sos: : 1588-9191")

    if message.content.startswith("!지지"):
        request = requests.get('https://maple.gg/u/' + message.content.split(" ")[1])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        links = str(soup.select('#user-profile > section > div > div.col-lg-8 > h3'))#split("</i>")[1].split("</p>")[0]
        embed = discord.Embed(color=0xFF5E00, title=links.split("<b class=\"align-middle\" style=\"line-height: 0;\">")[1].split("</b>")[0])
        embed.add_field(name="서버", value=links.split("<img alt=\"")[1].split("\" class=")[0], inline=True)
        embed.set_thumbnail(url=links.split("src=\"")[1].split("\" width=")[0])
        await message.channel.send(embed=embed)
        #print(links.split("src=\"")[1].split("\" width=")[0])

    if message.content.startswith("!코디분석"):
        request = requests.get('https://maple.gg/u/' + message.content.split(" ")[1])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        links = str(soup.select('#user-profile > section > div > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items'))
        image = str(soup.select('#user-profile > section > div > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img'))
        embed = discord.Embed(color=0xFF5E00, title=message.content.split(" ")[1])
        embed.add_field(name="머리", value=links.split("<span class=\"character-coord__item-name\">")[1].split("</span>")[0], inline=True)
        embed.add_field(name="헤어", value=links.split("<span class=\"character-coord__item-type\">헤어</span>\n<span class=\"character-coord__item-name\">")[1].split("</span>")[0], inline=True)
        embed.add_field(name="성형", value=links.split("<span class=\"character-coord__item-type\">성형</span>\n<span class=\"character-coord__item-name\">")[1].split("</span>")[0], inline=True)
        embed.add_field(name="상의", value=links.split("<span class=\"character-coord__item-type\">상의</span>\n<span class=\"character-coord__item-name\">")[1].split("</span>")[0], inline=True)
        embed.add_field(name="하의", value=links.split("<span class=\"character-coord__item-type\">하의</span>\n<span class=\"character-coord__item-name\">")[1].split("</span>")[0], inline=True)
        embed.add_field(name="신발", value=links.split("<span class=\"character-coord__item-type\">신발</span>\n<span class=\"character-coord__item-name\">")[1].split("</span>")[0], inline=True)
        embed.add_field(name="무기", value=links.split("<span class=\"character-coord__item-type\">무기</span>\n<span class=\"character-coord__item-name\">")[1].split("</span>")[0], inline=True)
        embed.set_thumbnail(url=image.split("src=\"")[1].split("\" style")[0])
        await message.channel.send(embed=embed)

acces_token = os.environ["BOT_TOKEN"]
client.run(acces_token)
