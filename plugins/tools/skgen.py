from pyrogram import Client, filters
import requests
import time
from plugins.func.users_sql import *
import requests
import string
import os
import random
session = requests.session()

def generate_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str

@Client.on_message(filters.command('gensk'))
async def cmd_skgen(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == 'None':
            resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
            await message.reply_text(resp, message.id)
        else:
            #
            # PLAN CHECK
            await plan_expirychk(user_id)
            # PM AND AUTH CHECK
            pm = fetchinfo(user_id)
            status = pm[2]
            role = status
            GROUP = open("plugins/group.txt").read().splitlines()
            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = "⚠️ #PREMIUM_ONLY ⚠️ \n Contact @K3VIN_X To Buy Premium Access !.Else You Can Use Free Then Join @MorPhoChat !"
                await message.reply_text(resp, message.id)
            elif chat_type == "ChatType.GROUP" and chat_id not in GROUP:
                resp = "⚠️ #UNAUTHORIZED_CHAT ⚠️ \n Contact @K3VIN_X To Authorize!"
                await message.reply_text(resp, message.id)
            else:
                if message.reply_to_message:
                    sknumxx = message.reply_to_message.text
                else:
                    sknumxx = message.text[len('/gensk '):]
                    sknumxx1 = message.text[len('/gensk  '):]
                if len(sknumxx) == 0:
                    nocc = """
OPPS! WRONG FORMAT

USE :- /gensk 200 1
          """
                    return await message.reply_text(nocc, message.id)
                elif len(sknumxx1) == 1:
                    nocc = """
OPPS! WRONG FORMAT

USE :- /gensk 200 1
          """
                    return await message.reply_text(nocc, message.id)

                ress = "Generating..."
                tic = time.perf_counter()
                msg = message.text[len('/gensk '):]
                splitter = msg.split(' ')
                num = int(splitter[0])
                options = splitter[1]
                if status == 'FREE' and num > 1000:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is FREE
You Can't Gen More Than 500 SK!
Upgrade Your Plan Or Wait For Next Update!
                """
                    await message.reply_text(resp, message.id)
                elif status == 'PREMIUM' and num > 10000:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is PREMIUM But You Have Check More Than 10k SK!
                """
                    await message.reply_text(resp, message.id)
                else:
                    sk_list = []
                    firstchk = await message.reply_text(ress, message.id)
                    for _ in range(num):
                        option = random.choice(options)
                        if option == '1':
                            length = 64
                        elif option == '2':
                            length = 34
                        elif option == '3':
                            length = 24
                        random_string = generate_random_string(length)
                        skk = "sk_live_" + random_string
                        sk_list.append(skk)
                    with open(f"{num}x_SK_GEN_BY_@JoannaChkBot.txt", "w") as file:
                        file.write('\n'.join(sk_list))
                    toc = time.perf_counter()
                    chat_id = str(message.chat.id)
                    resp=f"""
GENERATED COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{num}</code>
┠ Time in Gen - {toc - tic:0.4f}sec
┠ Gen By -  <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [  ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871"> @KevinCoder ⚠️</a>
┗－－－－－－－－－－－－┛"""
                    await message.reply_document(
                    document=f"{num}x_SK_GEN_BY_@JoannaChkBot.txt",
                    caption=resp,
                    reply_to_message_id=message.id)
                    os.remove(f"{num}x_SK_GEN_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
