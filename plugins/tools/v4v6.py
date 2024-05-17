import ipaddress
import os
import random
import time

import requests
from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()


@Client.on_message(filters.command("ips"))
async def cmd_ipgen(Client, message):
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
            if message.reply_to_message:
                bin = message.reply_to_message.text

            else:
                bin = message.text[len("/ips ") :]
                sknumxx1 = message.text[len("/ips  ") :]
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
            await message.reply_text(ress, message.id)
            tic = time.perf_counter()
            msg = message.text[len("/ips ") :]
            splitter = msg.split(" ")
            num = int(splitter[0])
            ip_type = splitter[1]
            generated_ips = []
            for _ in range(num):
                if ip_type == "ipv4":
                    generated_ips.append(
                        str(ipaddress.IPv4Address(random.randint(0, 2**32 - 1)))
                    )
                elif ip_type == "ipv6":
                    generated_ips.append(
                        str(ipaddress.IPv6Address(random.randint(0, 2**128 - 1)))
                    )
            with open(f"{num}x_IP_BY_@JoannaChkBot.txt", "w") as file:
                file.write("\n".join(generated_ips))
            toc = time.perf_counter()
            str(message.chat.id)
            resp = f"""
GENERATED COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{num}</code>
┠ Type - <code>{ip_type}</code>
┠ Time in Gen - {toc - tic:0.4f}sec
┠ Gen By -  <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠print('𝙍𝝣𝘽𝝣𝙇™ </> ⚠️')</a>
┗－－－－－－－－－－－－┛"""
            await message.reply_document(
                document=f"{num}x_IP_BY_@JoannaChkBot.txt",
                caption=resp,
                reply_to_message_id=message.id,
            )
            os.remove(f"{num}x_IP_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
