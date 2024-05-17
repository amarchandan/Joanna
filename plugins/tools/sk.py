import json
import time

import requests
from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()


def Getstr(string, start, end):
    string = " " + string
    ini = string.find(start)
    if ini == -1:
        return ""
    ini += len(start)
    length = string.find(end, ini) - ini
    return string[ini : ini + length].strip()


@Client.on_message(filters.command("sk"))
async def cmd_sk(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        str(message.chat.type)
        str(message.chat.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == "None":
            resp = " You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
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
                sk = message.reply_to_message.text
            else:
                sk = message.text[len("/sk ") :]
            if len(sk) == 0:
                nocc = """
  𝗣𝗟𝗘𝗔𝗦𝗘 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗔 𝗦𝗞 𝗞𝗘𝗬 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 ⚠️
          """
                return await message.reply_text(nocc, message.id)
            else:
                chkst = "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗦𝗞 𝗪𝗮𝗶𝘁...."
                done = await message.reply_text(chkst, message.id)
                tic = time.perf_counter()
                url = "https://api.stripe.com/v1/tokens"
                data = {
                    "card[number]": "4580420266153881",
                    "card[exp_month]": "09",
                    "card[exp_year]": "2025",
                    "card[cvc]": "704",
                }
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                }
                auth = (sk, "")

                resp = requests.post(url, data=data, headers=headers, auth=auth)
                await message.reply_text(resp, message.id)
                msg = Getstr(resp.text, '"message": "', '"')
                # BALANCE CHK

                url = "https://api.stripe.com/v1/balance"
                headers = {
                    "Content-Type": "application/x-www-form-urlencoded",
                }
                auth = (sk, "")

                response = requests.get(url, headers=headers, auth=auth)
                r2 = response.text
                parsed_data = json.loads(r2)
                await message.reply_text(r2, message.id)
                if "Expired API Key provided" in r2:
                    available_amount = "NA"
                elif "api_key_expired" in r2:
                    available_amount = "NA"
                else:
                    available_amount = parsed_data["available"][0]["amount"]

                curr = Getstr(r2, '"currency": "', '"')
                if "usd" in curr:
                    currn, currf, currs = "$", "🇺🇸", "USD"
                elif "inr" in curr:
                    currn, currf, currs = "₹", "🇮🇳", "INR"
                elif "cad" in curr:
                    currn, currf, currs = "$", "🇨🇦", "CAD"
                elif "aud" in curr:
                    currn, currf, currs = "$", "🇦🇺", "AUD"
                elif "aed" in curr:
                    currn, currf, currs = "د.إ", "🇦🇪", "AED"
                elif "sgd" in curr:
                    currn, currf, currs = "S$", "🇸🇬", "SGD"
                elif "nzd" in curr:
                    currn, currf, currs = "$", "🇳🇿", "NZD"
                elif "eur" in curr:
                    currn, currf, currs = "$", "🇪🇺", "EUR"
                elif "gbp" in curr:
                    currn, currf, currs = "£", "🇬🇧", "GBP"
                else:
                    currn, currf, currs = "N/A", "N/A", curr
                toc = time.perf_counter()
                result = f"""
  CHECK  SUCCESSFULLY 
┏－－－－－－－－－－－－┒
┠ SK - <code>{sk}</code>
┠ Resp - <code>{msg}</code>
┠ Balance - <code>{available_amount}</code>
┠ Currency - <code>{currn} {currf} {currs}</code>
┠ Time To Chk - {toc - tic:0.4f}sec
┠ Chk By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠print('𝙍𝝣𝘽𝝣𝙇™ </> ⚠️')</a>
┗－－－－－－－－－－－－┛
    """
                await Client.edit_message_text(message.chat.id, done.id, result)
    except Exception as e:
        print(e)
