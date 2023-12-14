from pyrogram import Client, filters
import requests
import time
from plugins.func.users_sql import *
import requests
import random
import os
import ipaddress
session = requests.session()


@Client.on_message(filters.command('ips'))
async def cmd_ipgen(Client, message):
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
                    bin = message.reply_to_message.text

                else:
                    bin = message.text[len('/ips '):]
                    sknumxx1 = message.text[len('/ips  '):]
                if len(bin) == 0:
                    nocc = """
OPPS! WRONG FORMAT

USE :- /ips 200 ipv4|ipv6
          """
                    return await message.reply_text(nocc, message.id)
                elif len(sknumxx1) == 1:
                    nocc = """
OPPS! WRONG FORMAT

USE :- /ips 200 ipv4|ipv6
          """
                    return await message.reply_text(nocc, message.id)
                ress = "Generating..."
                firstchk = await message.reply_text(ress, message.id)
                tic = time.perf_counter()
                msg = message.text[len('/ips '):]
                splitter = msg.split(' ')
                num = int(splitter[0])
                ip_type = splitter[1]
                ips = []
                generated_ips = []
                if status == 'FREE' and num > 1000:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is FREE
You Can't Gen More Than 1000 SK!
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
                    for _ in range(num):
                        if ip_type == 'ipv4':
                            generated_ips.append(str(ipaddress.IPv4Address(random.randint(0, 2**32-1))))
                        elif ip_type == 'ipv6':
                            generated_ips.append(str(ipaddress.IPv6Address(random.randint(0, 2**128-1))))
                    with open(f"{num}x_IP_BY_@JoannaChkBot.txt", 'w') as file:
                        file.write('\n'.join(generated_ips))
                    toc = time.perf_counter()
                    chat_id = str(message.chat.id)
                    resp=f"""
GENERATED COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{num}</code>
┠ Type - <code>{ip_type}</code>
┠ Time in Gen - {toc - tic:0.4f}sec
┠ Gen By -  <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [  ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871"> @KevinCoder ⚠️</a>
┗－－－－－－－－－－－－┛"""
                    await message.reply_document(
                    document=f"{num}x_IP_BY_@JoannaChkBot.txt",
                    caption=resp,
                    reply_to_message_id=message.id)
                    os.remove(f"{num}x_IP_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
