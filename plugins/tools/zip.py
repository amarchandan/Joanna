from pyrogram import Client, filters
import requests
import json
import re
import time
from plugins.func.users_sql import *
import requests
import json
session = requests.session()


@Client.on_message(filters.command('zip'))
async def cmd_bin(Client, message):
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
                tic = time.perf_counter()
                zipp = message.text[len('/zip '):]
                if len(zipp) == 0:
                    nocc = """
Give Valid Zip Code
          """
                    return await message.reply_text(nocc, message.id)
                else:
                    session = requests.session()
                    zip_api = requests.get(f'https://zip.getziptastic.com/v2/US/{zipp}').json()
                    toc = time.perf_counter()
                    resp = f"""
   GRAB SUCCESSFULLY 
┏－－－－－－－－－－－－┒
┠ Country - <code>{zip_api['country']}</code>
┠ Postal_Code - <code> {zip_api['postal_code']}</code>
┠ City - <code>{zip_api['city']}</code>
┠ State - <code>{zip_api['state_short']}</code>
┠ Time To Chk - {toc - tic:0.4f}sec
┠ Chk By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠ ⚠️</a>
┗－－－－－－－－－－－－┛
"""
                    await message.reply_text(resp, message.id)
    except Exception as e:
        print(e)
