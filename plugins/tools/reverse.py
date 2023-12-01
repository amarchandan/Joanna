from pyrogram import Client, filters
import requests
import time
from plugins.func.users_sql import *
import re
import requests
import os
import os.path
s = requests.session()
ua = {
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' #user gent
	}

@Client.on_message(filters.command('rev'))
async def cmd_reverse(Client, message):
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
            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = "⚠️ #PREMIUM_ONLY ⚠️ \n Contact @K3VIN_X To Buy Premium Access !.Else You Can Use Free Then Join @MorPhoChat !"
                await message.reply_text(resp, message.id)
            else:
                if not message.reply_to_message:
                    return await message.reply_text("Please Reply To File To Reverse")
                if not message.reply_to_message.document:
                    return await message.reply_text("Please Reply To File To Reverse")
                tic = time.perf_counter()
                
                ms_ = 'Reversing'
                domain_file = await message.reply_to_message.download(progress_args=(ms_, f"`Downloading This File!`"))
                with open(domain_file, 'r') as file:
                    domains = file.read().splitlines()
                x = len(domains)
                if status == 'FREE' and x > 1000:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is FREE
You Can't Reverse More Than 1000 IP!
Upgrade Your Plan Or Wait For Next Update!
                """
                    await message.reply_text(resp, message.id)
                elif status == 'PREMIUM' and x > 50000:
                    resp = f"""
#ALERT_ ⚠️
Your Account Is PREMIUM But You Have Reverse More Than 50,000 IP!
                """
                    await message.reply_text(resp, message.id)
                else:
                    names = []
                    await message.reply_text(ms_)
                    for site in domains:
                        if site.startswith("http://"):
                            site = site.replace("http://", "")
                        if site.startswith("https://"):
                            site = site.replace("https://", "")
                        response = s.get("https://rapiddns.io/sameip/" + site + "?full=1#result", headers=ua).content.decode("utf-8")
                        pattern = r"</th>\n<td>(.*?)</td>"
                        result = re.findall(pattern, response)
                        for line in result:
                            line = line.strip()
                            if line.startswith("www."):
                                line = "" + line[4:]
                            if line not in names:
                                names.append(line)
                            with open('REVERSE_IP_BY_@JoannaChkBot.txt', 'a+') as f:
                                f.write('\n'.join(names))
                        toc = time.perf_counter()
                    chat_id = str(message.chat.id)
                    resp=f"""
REVERSE COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{x}</code>
┠ Time in Rev - {toc - tic:0.4f}sec
┠ Rev By -  <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [  ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠ ⚠️</a>
┗－－－－－－－－－－－－┛"""
                    await message.reply_document(
                    document='REVERSE_IP_BY_@JoannaChkBot.txt',
                    caption=resp,
                    reply_to_message_id=message.id)
                    os.remove('REVERSE_IP_BY_@JoannaChkBot.txt')
    except Exception as e:
            print(e)
