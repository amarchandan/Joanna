import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pyrogram import Client, filters
from plugins.func.users_sql import *
import os
import re
import string
session = requests.session()
s = requests.session()


def Getstr(string, start, end):
    string = ' ' + string
    ini = string.find(start)
    if ini == -1:
        return ''
    ini += len(start)
    length = string.find(end, ini) - ini
    return string[ini:ini + length].strip()

@Client.on_message(filters.command('masssk'))
async def cmd_massskchk(Client, message):
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
                    return await message.reply_text("Please Reply To File To Chk Sk")
                if not message.reply_to_message.document:
                    return await message.reply_text("Please Reply To File To Chk Sk")
                sk_list = []
                tic = time.perf_counter()
                ms_ = 'Checking....'
                domain_file = await message.reply_to_message.download(progress_args=(ms_, f"`Downloading This File!`"))
                with open(domain_file, 'r') as file:
                    domains = file.read().splitlines()
                x = len(domains)
                if status == 'FREE' and x > 10:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is FREE
You Can't Check More Than 10 SK!
Upgrade Your Plan Or Wait For Next Update!
                """
                    await message.reply_text(resp, message.id)
                elif status == 'PREMIUM' and x > 200:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is PREMIUM But You Have Check More Than 200 SK!
                """
                    await message.reply_text(resp, message.id)
                elif status == 'GOLD' and x > 1000:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is GOLD But You Have Check More Than 1K SK!
                    """
                    await message.reply_text(resp, message.id)
                else:
                    await message.reply_text(ms_)
                    for site in domains:
                        url = 'https://api.stripe.com/v1/tokens'
                        data = {
                            'card[number]': '4580420266153881',
                            'card[exp_month]': '09',
                            'card[exp_year]': '2025',
                            'card[cvc]': '704',
                            }
                        headers = {
                            'Content-Type': 'application/x-www-form-urlencoded',
                        }
                        auth = (site, '')
                        resp = requests.post(url, data=data, headers=headers, auth=auth)
                        resp1 = Getstr(resp.text, '"message": "', '"')
                        response = f'{resp1} - {site}'
                        sk_list.append(response)
                    with open(f'{x}x_SK_CHK_BY_@JoannaChkBot.txt', 'a+') as f:
                                f.write('\n'.join(sk_list))
                    toc = time.perf_counter()
                    chat_id = str(message.chat.id)
                    resp=f"""
SK CHECKING COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{x}</code>
┠ Time To Chk - {toc - tic:0.4f}sec
┠ Chk By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871"> @KevinCoder ⚠️</a>
┗－－－－－－－－－－－－┛"""
                    await message.reply_document(
                    document=f"{x}x_SK_CHK_BY_@JoannaChkBot.txt",
                    caption=resp,
                    reply_to_message_id=message.id)
                    os.remove(f"{x}x_SK_CHK_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
