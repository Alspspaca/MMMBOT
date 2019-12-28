import discord
import os
import requests
from bs4 import BeautifulSoup
import openpyxl
import datetime

client = discord.Client()


@client.event
async def on_ready():
    bid = (str(client.user.id))
    print("봇 이름 : " + bid)
    bname = client.user.name
    print("봇이름 : " + bname)
    print("STAR")
    game = discord.Game("!도움말")
    await client.change_presence(status=discord.Status.online, activity=game) #빨간불,노란불,초록불=offline,idle,online





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
            await author.add_roles(role)
            embed = discord.Embed(color=0xFF5E00, title="프로필")
            embed.add_field(name="서버닉네임", value=message.author.display_name.split("/")[0], inline=True)
            embed.add_field(name="서버", value=role, inline=True)
            embed.add_field(name="레벨", value=1, inline=True)
            embed.set_thumbnail(url=message.author.avatar_url)
            await author.send(embed=embed)
            await client.get_channel(channel).send("\n새로운 메이플월드의 용사 " + message.author.display_name.split("/")[0] + "님 환영합니다.")
            await client.get_channel(channel).send(embed=embed)

    """if message.content.startswith("!정보"):
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        i = 1
        embed = discord.Embed(color=0xFF5E00, title="프로필")
        embed.add_field(name="서버닉네임", value=message.author.display_name.split("/")[0], inline=True)
        embed.add_field(name="서버", value=message.author.roles[1], inline=True)
        while True:
            if sheet["A" + str(i)].value == str(message.author.id + message.guild.id):
                embed.add_field(name="레벨", value=sheet["C" + str(i)].value, inline=True)
                break
            i += 1
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("") and message.author.id!=650647451560050689 and message.author.id!=184405311681986560:
        author = message.guild.get_member(int(message.author.id))
        file = openpyxl.load_workbook("레벨.xlsx")
        sheet = file.active
        exp = [10, 20, 30, 40, 50,70,100,130,160,200,240,280,320,400,500,600,800,1000,1500,2000,2500,3000,4000,5000,7000,10000,15000,20000,30000]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id + message.guild.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 5
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    await author.send("( " + str(message.guild) + " 서버 )" + "\n레벨이 올랐습니다.\n 현재레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet["B" + str(i)].value))
                file.save("레벨.xlsx")
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id + message.guild.id)
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save("레벨.xlsx")
                break
            i += 1"""

    if message.content.startswith("!한강"):
        request = requests.get('https://www.wpws.kr/hangang/')
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        links = str(soup.select('#temp')).split("</i>")[1].split("</p>")[0]
        await message.channel.send("현재온도 : " + links + "\n:sos: : 1588-9191")

    if message.content.startswith("!정보"):
        request = requests.get('https://maple.gg/u/' + message.content.split(" ")[1])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        profile = soup.select('#user-profile > section > div > div.col-lg-8 > div.user-summary > ul > li')
        links = str(soup.select('#user-profile > section > div > div.col-lg-8 > h3'))
        imf = soup.select('#user-profile > section > div > div.col-lg-8 > div.row.row-normal.user-additional > div')
        try:
            embed = discord.Embed(color=0xFF5E00, title=message.content.split(" ")[1])
            embed.add_field(name="서버", value=links.split("<img alt=\"")[1].split("\" class=")[0], inline=True)
            embed.set_thumbnail(url=links.split("src=\"")[1].split("\" width=")[0])
            embed.add_field(name="레벨", value=profile[0].text, inline=True)
            embed.add_field(name="직업", value=profile[1].text, inline=True)
            embed.add_field(name="인기도", value=profile[2].text.split("인기도")[1], inline=True)
            embed.add_field(name="길드", value=str(imf[0].text).replace(' ', '').replace('\n', '').split("길드")[1], inline=True)
            embed.add_field(name="종합랭킹", value=str(imf[1].text).replace(' ', '').replace('\n', '').split("종합랭킹")[1], inline=True)
            embed.add_field(name="월드랭킹", value=str(imf[2].text).replace(' ', '').replace('\n', '').split("월드랭킹")[1], inline=True)
            embed.add_field(name="직업랭킹(월드)", value=str(imf[3].text).replace(' ', '').replace('\n', '').split("직업랭킹(월드)")[1], inline=True)
            embed.add_field(name="직업랭킹(전체)", value=str(imf[4].text).replace(' ', '').replace('\n', '').split("직업랭킹(전체)")[1], inline=True)
            await message.channel.send(embed=embed)
        except:
            errorembed = discord.Embed(color=0xFF5E00, title="캐릭터 정보를 찾을수 없습니다.")
            await message.channel.send(embed=errorembed)

    if message.content.startswith("!코디분석"):
        request = requests.get('https://maple.gg/u/' + message.content.split(" ")[1])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        links = str(soup.select('#user-profile > section > div > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-4.col-lg-6 > div > div.character-coord__items'))
        image = str(soup.select('#user-profile > section > div > div.col-lg-4.pt-1.pt-sm-0.pb-1.pb-sm-0.text-center.mt-2.mt-lg-0 > div > div.col-6.col-md-8.col-lg-6 > img'))
        try:
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
        except:
            errorembed = discord.Embed(color=0xFF5E00, title="캐릭터 정보를 찾을수 없습니다.")
            await message.channel.send(embed=errorembed)      
            

    if message.content.startswith("!로얄픽"):
        dday = str(datetime.datetime(2019, 12, 30, 9, 59, 59)-datetime.datetime.now())
        print(dday)
        day = dday.replace(' days', '일').split(",")[0]
        hour = dday.split(" days,")[1].split(":")[0]+"시 "
        minute = dday.split(" days,")[1].split(":")[1].split(":")[0]+"분"
        request = requests.get('https://maplestory.nexon.com/promotion/2019/20191212/BeautyAwards')
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        links = str(soup.select('#wrap > div.intro > div > span.poll_cnt'))
        embed = discord.Embed(color=0xFF5E00, title="로얄픽")
        embed.add_field(name="D-DAY", value=day+hour+minute, inline=True)
        embed.add_field(name="투표참여자", value=str(links.split(">")[1]).split("<")[0], inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("!테스트"):
        request = requests.get('https://maple.gg/u/' + message.content.split(" ")[1])
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        imf = soup.select('#user-profile > section > div > div.col-lg-8 > div.row.row-normal.user-additional > div')
        for i in imf:
            print(str(i.text).replace(' ', '').replace('\n', ''))
        """profile = soup.select('#user-profile > section > div > div.col-lg-8 > div.user-summary > ul > li')
        links = str(soup.select('#user-profile > section > div > div.col-lg-8 > h3'))
        embed = discord.Embed(color=0xFF5E00, title=message.content.split(" ")[1])
        embed.add_field(name="서버", value=links.split("<img alt=\"")[1].split("\" class=")[0], inline=True)
        embed.add_field(name="레벨", value=profile[0].text, inline=True)
        embed.add_field(name="직업", value=profile[1].text, inline=True)
        #embed.add_field(name="인기도", value=profile[2].text.split("인기도")[0], inline=True)
        embed.set_thumbnail(url=links.split("src=\"")[1].split("\" width=")[0])"""
        #await message.channel.send(embed=embed)

    if message.content.startswith("!플래그"):
        plagtime=['12:0:0', '19:0:0', '21:0:0']
        plest=['12', '7', '9']
        count=0
        now = datetime.datetime.now()
        embed = discord.Embed(color=0xFF5E00, title="플래그 남은시간")
        for i in plagtime:
            imtime = datetime.datetime.strptime(i, '%H:%M:%S')
            result=str(imtime-now).split('days, ')[1].split('.')[0]
            embed.add_field(name=plest[int(count)]+"시 플래그", value=result, inline=True)
            count=count+1
        await message.channel.send(embed=embed)

    if message.content.startswith("!길드"):
        request = requests.get('https://maple.gg/guild/croa/%EC%95%BC%EC%8D%B0')
        gmes = message.content.split(" ")[1]
        if gmes == "정보":
            html = request.text
            soup = BeautifulSoup(html, 'html.parser')
            imf = soup.select('#app > div.card.mt-0 > div.card-header.guild-header > section > div.row.mb-4 > div.col-lg-8 > div > div')
            embed = discord.Embed(color=0xFF5E00, title="야썰 길드 정보")
            embed.add_field(name="길드마스터", value="밥툰", inline=False)
            embed.add_field(name="월드랭킹", value=str(imf[1]).split('<span>')[1].split('</span>')[0], inline=True)
            embed.add_field(name="전체랭킹", value=str(imf[2]).split('<span>')[1].split('</span>')[0], inline=True)
            embed.add_field(name="길드원수", value=str(imf[3]).split('<span>')[1].split('</span>')[0], inline=True)
            embed.add_field(name="길드포인트", value=str(imf[4]).split('<span>')[1].split('</span>')[0], inline=True)
            embed.set_thumbnail(url='https://raw.githubusercontent.com/Alspspaca/MMMBOT/master/gico.jpg')
            await message.channel.send(embed=embed)
        """try:
            gmes=message.content.split(" ")[1]
            if gmes == "정보":
                html = request.text
                soup = BeautifulSoup(html, 'html.parser')
                imf = soup.select('#app > div.card.mt-0 > div.card-header.guild-header > section > div.row.mb-4 > div.col-lg-8 > div > div')
                for i in imf:
                    print(str(imf[i].text))

            #if gmes == "멤버":

        except:
            await message.channel.send("도움말")"""
    
    if message.content.startswith("!경뿌"):
        request = requests.get('https://maple.gg/megaphone/croa')
        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        imf = soup.select('#app > section > div > div.col-lg-8.col-xl-9 > section > div > div')
        count=0
        embed = discord.Embed(color=0xFF5E00, title="경뿌 검색기")
        await message.channel.send(embed=embed)
        for i in imf:
            text = i.text.replace('\n', '').replace(' ', '')
            if "경뿌" in text:
                embed.add_field(name="Result :", value=text, inline=False)
                count=1
        if count == 0:
            egb = discord.Embed(color=0xFF5E00, title="경뿌를 찾지 못했습니다.")
            await message.channel.send(embed=egb)
        else:
            await message.channel.send(embed=embed)    
    
    if message.content.startswith("!도움말"):
        author = message.guild.get_member(int(message.author.id))
        embed = discord.Embed(color=0xFF5E00, title="명령어 안내")
        embed.add_field(name="캐릭터 정보", value="!정보 [닉네임] - 캐릭터 정보를 가져와 출력한다.\n!코디분석 [닉네임] - 캐릭터의 코디 상태를 출력한다.\n", inline=False)
        embed.add_field(name="유용한 명령어", value="!플래그 - 플래그 까지 남은시간을 출력한다.\n!한강 - 한강물 온도를 출력한다.\n!경뿌 - 크로아 서버의 경뿌를 탐색해 출력한다.\n", inline=False)
        embed.add_field(name="길드 관련(미완)", value="!길드 - 길드 도움말을 출력한다.\n!길드 정보 - 길드 정보를 출력한다.\n", inline=False)
        embed.add_field(name="이벤트", value="!로얄픽 - 뷰티어워즈 정보를 가져와 출력한다.\n", inline=False)
        await author.send(embed=embed)
      

acces_token = os.environ["BOT_TOKEN"]
client.run(acces_token)
