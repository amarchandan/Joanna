import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pyrogram import Client, filters
from plugins.func.users_sql import *
import os
import socket
session = requests.session()
s = requests.session()


@Client.on_message(filters.command('dip'))
async def cmd_domip(Client, message):
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
                
                if not message.reply_to_message:
                    return await message.reply_text("Please Reply To File")
                if not message.reply_to_message.document:
                    return await message.reply_text("Please Reply To File")
                tic = time.perf_counter()
                ms_ = 'Checking....'
                domain_file = await message.reply_to_message.download(progress_args=(ms_, f"`Downloading This File!`"))
                with open(domain_file, 'r') as file:
                    domains = file.read().splitlines()
                x = len(domains)
                if status == 'FREE' and x > 1000:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is FREE
You Can't Check More Than 1000 Domain!
Upgrade Your Plan Or Wait For Next Update!
                """
                    await message.reply_text(resp, message.id)
                elif status == 'PREMIUM' and x > 50000:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is PREMIUM But You Have Check More Than 50000 SK!
                """
                    await message.reply_text(resp, message.id)
                else:
                    await message.reply_text(ms_)
                    results = []
                    for url in domains:
                        if 'http://' not in url:
                            IP1 = socket.gethostbyname(url)
                            results.append(IP1)
                        elif 'http://' in url:
                            url = url.replace('http://', '').replace('https://', '').replace('/', '')
                            IP2 = socket.gethostbyname(url)
                            results.append(IP2)

                    if results:
                        result_text = "\n".join(results)
                        with open(f"{x}x_DOMAIN_TO_IP_BY_@JoannaChkBot.txt", 'w') as result_file:
                            result_file.write(result_text)
                    toc = time.perf_counter()
                    chat_id = str(message.chat.id)
                    resp=f"""
 COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{x}</code>
┠ Time To Con - {toc - tic:0.4f}sec
┠ Con By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871"> @KevinCoder ⚠️</a>
┗－－－－－－－－－－－－┛"""
                    await message.reply_document(
                    document=f"{x}x_DOMAIN_TO_IP_BY_@JoannaChkBot.txt",
                    caption=resp,
                    reply_to_message_id=message.id)
                    os.remove(f"{x}x_DOMAIN_TO_IP_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
