import time

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os
import re

from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()


@Client.on_message(filters.command("scrip1"))
async def cmd_scrip1(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        str(message.chat.type)
        str(message.chat.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == "None":
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
            ress = "SCRAPING ..."
            await message.reply_text(ress, message.id)
            tic = time.perf_counter()
            urls = requests.get("https://usings.ru/bots.php?bot=&page=1").json()
            DRZXQGET = requests.get(
                urls,
                headers={
                    "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                },
                timeout=10,
            ).text
            if "IP" in DRZXQGET:
                REGEX = re.findall(
                    "[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}", DRZXQGET
                )
                for DRZXQ in REGEX:
                    open("GrabbedIPs.txt", "a").write(DRZXQ + "\n")
                with open("GrabbedIPs.txt", "r") as FIRSTPX:
                    FIRSTPXX = list(dict.fromkeys(FIRSTPX.read().splitlines()))
                    with open("GrabbedIPs.txt.tmp", "a") as new:
                        new.write("\n".join(FIRSTPXX))
                        print(FIRSTPXX)
                        new.close()
                FIRSTPX.close()
                # num = len(FIRSTPXX)
            os.remove("GrabbedIPs.txt")
            os.rename("GrabbedIPs.txt.tmp", "{num}x_IP_BY_@JoannaChkBot.txt")
            toc = time.perf_counter()
            str(message.chat.id)
            resp = f"""
SCRAPPING COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code></code>
┠ Time in Scr - {toc - tic:0.4f}sec
┠ Scr By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠ ⚠️</a>
┗－－－－－－－－－－－－┛"""
            await message.reply_document(
                document="{num}x_IP_BY_@JoannaChkBot.txt",
                caption=resp,
                reply_to_message_id=message.id,
            )
            os.remove("{num}x_IP_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
