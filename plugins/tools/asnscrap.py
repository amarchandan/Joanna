import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import ipranges
from pyrogram import Client, filters
from plugins.func.users_sql import *
import random
import os
session = requests.session()


@Client.on_message(filters.command('asnip'))
async def cmd_asnip(Client, message):
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
            if message.reply_to_message:
                bin = message.reply_to_message.text
            else:
                bin = message.text[len('/asnip '):]
            if len(bin) == 0:
                nocc = """
OPPS! WRONG FORMAT

USE :- /asnip 200

          """
                return await message.reply_text(nocc, message.id)

            ress = "SCRAPING ..."
            firstchk = await message.reply_text(ress, message.id)
            tic = time.perf_counter()
            num = int(message.command[1])
            r = requests.get(f'https://api.bgpview.io/asn/{num}/prefixes').json()
            rather = r['data']['ipv4_prefixes']
            for Yh in range(0, int(len(rather)) - 1):
                IPM = r['data']['ipv4_prefixes'][Yh]
                Jahl = IPM['ip'] + '/' + str(IPM['cidr'])
                IPL = ipranges.IP4Net(Jahl)
                for IP in IPL:
                    open(f'GrabbedIPs.txt', 'a', errors='ignore', encoding='utf-8').write(f'{IP}\n')
                with open('GrabbedIPs.txt', 'r') as FIRSTPX:
                    FIRSTPXX = list(dict.fromkeys(FIRSTPX.read().splitlines()))
                    with open('GrabbedIPs.txt.tmp','a') as new:
                        new.write('\n'.join(FIRSTPXX))
                        new.close()
                FIRSTPX.close()
            os.remove('GrabbedIPs.txt')
            x = os.rename('GrabbedIPs.txt.tmp',f"{num}x_IP_BY_@JoannaChkBot.txt")
            toc = time.perf_counter()
            chat_id = str(message.chat.id)
            resp=f"""
SCRAPPING COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{num}</code>
┠ Time in Scr - {toc - tic:0.4f}sec
┠ Scr By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871"> @KevinCoder ⚠️</a>
┗－－－－－－－－－－－－┛"""
            await message.reply_document(
            document=f"{num}x_IP_BY_@JoannaChkBot.txt",
            caption=resp,
            reply_to_message_id=message.id)
            os.remove(f"{num}x_IP_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
