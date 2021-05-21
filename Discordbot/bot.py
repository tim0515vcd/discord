# 導入Discord.py
import discord
import random

# client是我們與Discord連結的橋樑
client = discord.Client()


# 調用event函式庫
@client.event
# 當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('樂旗督察開始監督!')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
# 當有訊息時
async def on_message(message):
    #  人名關鍵字
    luckyname_1 = ['狗','大耳狗','柏翰','林柏翰','樂旗豆葛','xk4fu62.4ek3','lucky dog','LUCKY DOG','Lucky Dog','luckydog','LUCKYDOG','LuckyDog','樂旗鬥葛','樂奇鬥葛','樂奇豆葛']
    luckyname_2 = ['曉一','小一','曉懿','小懿','吳小一','吳小懿','吳曉一','吳曉懿','樂旗批格','樂旗披格','lucky pig','LUCKY PIG','Lucky Pig','luckypig','LUCKYPIG','LuckyPig','樂旗批隔','樂奇批隔','樂奇批格','樂旗P隔','xk4fu6qu ek6']
    luckyname_3 = ['鄭為馼','為馼','為文','鄭為文','樂旗嘎必居','lucky garbage','LUCKY GARBAGE','Lucky Garbage','luckygarbage','LUCKYGARBAGE','LuckyGarbage','樂旗嘎避居','樂奇嘎避居','樂奇嘎必居','樂旗嘎必駒','xk4fu6e8 1u4rm ']
    luckyname_4 = ['沅孝','陳沅孝','樂旗揆蒂卡','樂旗奎地卡','lucky credit card','LUCKY CREDIT CARD','Lucky Credit Card','luckycreditcard','LUCKYCREDITCARD','LuckyCreditcard','樂奇揆蒂卡','樂奇奎地卡','xk4fu6djo62u4d83']
    luckyname_5 = ['簡子嘉','樂旗巴特','樂旗八特','lucky butter','LUCKY BUTTER','Lucky Butter','luckybutter','LUCKYBUTTER','LuckyButter','樂奇巴特','樂奇八特','xk4fu618 wk4']
    luckyname_6 = ['柯承佑','樂旗伊特','樂旗一特','lucky eat','LUCKY EAT','Lucky Eat','luckyeat','LUCKYEAT','LuckyEat','樂奇一特', '樂奇伊特','樂旗P隔','xk4fu6u wk4']
    luckyname_7 = ['昨非','陳昨非','樂旗','樂旗','lucky','LUCKY','Lucky','樂奇','xk4fu6']
    #  對應人名詞慧
    answerlist_1 = ['哇!4柏翰耶!', '柏翰汪汪汪!', '大~耳狗', '樂旗家族第二把交椅!第一把是樂旗']
    answerlist_2 = ['哇!4曉懿耶!', '曉懿ㄍㄡˊㄍㄡˊㄍㄡˊ!', '大~耳狗的女友', '樂旗家族第三把交椅!第二把是樂旗豆葛']
    answerlist_3 = ['哇!4為馼耶!', '為文噁噁噁!']
    answerlist_4 = ['沅...沅孝!是你!', '要辦張信用卡嗎各位?']
    answerlist_5 = ['哇!奶油耶!', '好油好油!', '吃不到小龍欸你']
    answerlist_6 = ['哇!提摩耶!', '提摩隊長前來報到!', 'one two three four', '走啊!大吃一波阿!']
    answerlist_7 = ['哇!樂旗至尊耶!','樂旗本人','你的卡特...?Do not say so much...', '樂旗家族第一把交椅!']
    # 排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return

    # 如果以「說」開頭
    if message.content.startswith('說'):
        # 分割訊息成兩份
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要我說什麼啦？")
        else:
            await message.channel.send(tmp[1])
    if message.content.startswith('更改狀態'):
        # 分割訊息成兩份
        tmp = message.content.split(" ", 2)
        # 如果分割後串列長度只有1
        if len(tmp) == 1:
            await message.channel.send("你要改成什麼啦？")
        else:
            game = discord.Game(tmp[1])
            # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
            await client.change_presence(status=discord.Status.idle, activity=game)

    # 人名反應
    if message.content in luckyname_1:
        doganswerchoice = random.choice(answerlist_1)
        await message.channel.send(doganswerchoice)
    if message.content in luckyname_2:
        piganswerchoice2 = random.choice(answerlist_2)
        await message.channel.send(piganswerchoice2)
    if message.content in luckyname_3:
        garbageanswerchoice3 = random.choice(answerlist_3)
        await message.channel.send(garbageanswerchoice3)
    if message.content in luckyname_4:
        creditcardanswerchoice4 = random.choice(answerlist_4)
        await message.channel.send(creditcardanswerchoice4)
    if message.content in luckyname_5:
        eatanswerchoice5 = random.choice(answerlist_5)
        await message.channel.send(eatanswerchoice5)
    if message.content in luckyname_6:
        butteranswerchoice6 = random.choice(answerlist_6)
        await message.channel.send(butteranswerchoice6)
    if message.content in luckyname_7:
        answerchoice7 = random.choice(answerlist_7)
        await message.channel.send(answerchoice7)


    # 購物
    if message.content == 'momo':
        await message.channel.send('https://www.momoshop.com.tw/')
    if message.content == 'pchome':
        await message.channel.send('https://24h.pchome.com.tw/')
    if message.content == 'yahoo':
        await message.channel.send('https://tw.buy.yahoo.com/')
    if message.content == 'friday':
        await message.channel.send('https://shopping.friday.tw/')
    if message.content == '蝦皮':
        await message.channel.send('https://shopee.tw/')
    if message.content == '購物':
        await message.channel.send('https://www.momoshop.com.tw/')
        await message.channel.send('https://24h.pchome.com.tw/')
        await message.channel.send('https://tw.buy.yahoo.com/')
        await message.channel.send('https://shopping.friday.tw/')
        await message.channel.send('https://shopee.tw/')

    if message.content == '幹':
        await message.channel.send('又怎樣又怎樣?')


client.run('') #TOKEN在剛剛Discord Developer那邊「BOT」頁面裡面
