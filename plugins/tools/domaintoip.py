import time

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os
import socket

from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()
s = requests.session()


@Client.on_message(filters.command("dip"))
async def cmd_domip(Client, message):
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
            if not message.reply_to_message:
                return await message.reply_text("Please Reply To File")
            if not message.reply_to_message.document:
                return await message.reply_text("Please Reply To File")
            tic = time.perf_counter()
            ms_ = "Checking...."
            domain_file = await message.reply_to_message.download(
                progress_args=(ms_, f"`Downloading This File!`")
            )
            with open(domain_file, "r") as file:
                domains = file.read().splitlines()
            x = len(domains)
            await message.reply_text(ms_)
            results = []
            for url in domains:
                if "http://" not in url:
                    IP1 = socket.gethostbyname(url)
                    results.append(IP1)
                elif "http://" in url:
                    url = (
                        url.replace("http://", "")
                        .replace("https://", "")
                        .replace("/", "")
                    )
                    IP2 = socket.gethostbyname(url)
                    results.append(IP2)

            if results:
                result_text = "\n".join(results)
                with open(
                    f"{x}x_DOMAIN_TO_IP_BY_@JoannaChkBot.txt", "w"
                ) as result_file:
                    result_file.write(result_text)
            toc = time.perf_counter()
            str(message.chat.id)
            resp = f"""
 COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{x}</code>
┠ Time To Con - {toc - tic:0.4f}sec
┠ Req by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.username}</a> | [ {role} ]
┗－－－－－－－－－－－－┛"""
            await message.reply_document(
                document=f"{x}x_DOMAIN_TO_IP_BY_@JoannaChkBot.txt",
                caption=resp,
                reply_to_message_id=message.id,
            )
            os.remove(f"{x}x_DOMAIN_TO_IP_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
