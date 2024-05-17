import os
import random
import time

import requests
from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()


@Client.on_message(filters.command("genip"))
async def cmd_rndomipgen(Client, message):
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
            ipn = message.text[len("/genip ") :]
            if message.reply_to_message:
                bin = message.reply_to_message.text

            else:
                bin = message.text[len("/genip ") :]
            if len(bin) == 0:
                nocc = """
OPPS! WRONG FORMAT

USE :- /genip 200

          """
                return await message.reply_text(nocc, message.id)

            ress = "Generating..."
            await message.reply_text(ress, message.id)
            tic = time.perf_counter()
            num = int(message.command[1])
            ips = []
            for _ in range(num):
                ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
                ips.append(ip)
            with open("GrabbedIPs.txt", "w") as file:
                file.write("\n".join(ips))
            with open("GrabbedIPs.txt", "r") as FIRSTPX:
                FIRSTPXX = list(dict.fromkeys(FIRSTPX.read().splitlines()))
                with open("GrabbedIPs.txt.tmp", "a") as new:
                    new.write("\n".join(FIRSTPXX))
                    new.close()
            FIRSTPX.close()
            os.remove("GrabbedIPs.txt")
            os.rename("GrabbedIPs.txt.tmp", f"{num}x_IP_BY_@JoannaChkBot.txt")
            toc = time.perf_counter()
            str(message.chat.id)
            resp = f"""
GENERATED COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{num}</code>
┠ Time in Gen - {toc - tic:0.4f}sec
┠ Gen By -  <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠ ⚠️</a>
┗－－－－－－－－－－－－┛"""
            await message.reply_document(
                document=f"{num}x_IP_BY_@JoannaChkBot.txt",
                caption=resp,
                reply_to_message_id=message.id,
            )
            os.remove(f"{num}x_IP_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
