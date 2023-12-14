import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import ipranges
from pyrogram import Client, filters
from plugins.func.users_sql import *
import re
import os
session = requests.session()


@Client.on_message(filters.command('scrip1'))
async def cmd_scrip1(Client, message):
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
            GROUP = open("plugins/group.txt").read().splitlines()
            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = "⚠️ #PREMIUM_ONLY ⚠️ \n Contact @K3VIN_X To Buy Premium Access !.Else You Can Use Free Then Join @MorPhoChat !"
                await message.reply_text(resp, message.id)
            elif chat_type == "ChatType.GROUP" and chat_id not in GROUP:
                resp = "⚠️ #UNAUTHORIZED_CHAT ⚠️ \n Contact @K3VIN_X To Authorize!"
                await message.reply_text(resp, message.id)
            else:
                ress = "SCRAPING ..."
                firstchk = await message.reply_text(ress, message.id)
                tic = time.perf_counter()
                urls =  requests.get('https://usings.ru/bots.php?bot=&page=1').json()
                DRZXQGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
                if 'IP' in DRZXQGET:
                    REGEX = re.findall("[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}",DRZXQGET)
                    for DRZXQ in REGEX:
                        open('GrabbedIPs.txt','a').write(DRZXQ+'\n')
                    with open('GrabbedIPs.txt', 'r') as FIRSTPX:
                        FIRSTPXX = list(dict.fromkeys(FIRSTPX.read().splitlines()))
                        with open('GrabbedIPs.txt.tmp','a') as new:
                            new.write('\n'.join(FIRSTPXX))
                            print(FIRSTPXX)
                            new.close()
                    FIRSTPX.close()
                    #num = len(FIRSTPXX)
                os.remove('GrabbedIPs.txt')
                x = os.rename('GrabbedIPs.txt.tmp',"{num}x_IP_BY_@JoannaChkBot.txt")
                toc = time.perf_counter()
                chat_id = str(message.chat.id)
                resp=f"""
SCRAPPING COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code></code>
┠ Time in Scr - {toc - tic:0.4f}sec
┠ Scr By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871"> @KevinCoder ⚠️</a>
┗－－－－－－－－－－－－┛"""
                await message.reply_document(
                document="{num}x_IP_BY_@JoannaChkBot.txt",
                caption=resp,
                reply_to_message_id=message.id)
                os.remove("{num}x_IP_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
