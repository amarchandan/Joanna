import ipaddress
import os
import time

import requests
from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()


@Client.on_message(filters.command("range"))
async def cmd_ranger(Client, message):
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
            ipn = message.text[len("/range ") :]
            if message.reply_to_message:
                bin = message.reply_to_message.text

            else:
                bin = message.text[len("/range ") :]
                sknumxx1 = message.text[len("/range  ") :]
            if len(bin) == 0:
                nocc = """
OPPS! WRONG FORMAT

USE :- /range Start_Ip - End_Ip
          """
                return await message.reply_text(nocc, message.id)
            elif len(sknumxx1) == 1:
                nocc = """
OPPS! WRONG FORMAT

USE :- /range Start_Ip - End_Ip
          """
                return await message.reply_text(nocc, message.id)
            ress = "Generating..."
            await message.reply_text(ress, message.id)
            tic = time.perf_counter()
            msg = message.text[len("/range ") :]
            splitter = msg.split(" ")
            start_ip_str = splitter[0]
            end_ip_str = splitter[1]
            try:
                start_ip = ipaddress.ip_address(start_ip_str)
                end_ip = ipaddress.ip_address(end_ip_str)
            except ValueError:
                await message.reply_text("Invalid IP address format.", message.id)
                return
            generated_ips = []
            num = len(generated_ips)
            for ip in ipaddress.summarize_address_range(start_ip, end_ip):
                generated_ips.extend(str(ip) for ip in ipaddress.IPv4Network(ip))
            with open(f"{num}x_IP_RANGER_BY_@JoannaChkBot.txt", "w") as file:
                file.write("\n".join(generated_ips))
            toc = time.perf_counter()
            str(message.chat.id)
            resp = f"""
GENERATED COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{num}</code>
┠ Range - <code>{start_ip_str} - {end_ip_str}</code>
┠ Time in Range - {toc - tic:0.4f}sec
┠ Range By -  <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠print('𝙍𝝣𝘽𝝣𝙇™ </> ⚠️')</a>
┗－－－－－－－－－－－－┛"""
            await message.reply_document(
                document=f"{num}x_IP_RANGER_BY_@JoannaChkBot.txt",
                caption=resp,
                reply_to_message_id=message.id,
            )
            os.remove(f"{num}x_IP_RANGER_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
