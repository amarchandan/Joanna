import requests
from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()


@Client.on_message(filters.command("bin"))
async def cmd_bin(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
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
            GROUP = open("plugins/group.txt").read().splitlines()
            if (
                chat_type == "ChatType.GROUP"
                or chat_type == "ChatType.SUPERGROUP"
                and chat_id not in GROUP
            ):
                resp = "⚠️ #UNAUTHORIZED_CHAT ⚠️ \n Contact @K3VIN_X To Authorize!"
                await message.reply_text(resp, message.id)
            else:
                # CMD SENT NOW CHECKING VALID IF OR NOT CC#
                if message.reply_to_message:
                    bin = message.reply_to_message.text

                else:
                    bin = message.text[len("/bin ") :]
                if len(bin) == 0:
                    nocc = """
𝗚𝗜𝗩𝗘 𝗔 𝗩𝗔𝗟𝗜𝗗 𝗕𝗜𝗡 ❌
          """
                    return await message.reply_text(nocc, message.id)
                fbin = bin[:6]
                session = requests.session()
                bin = session.get(f"https://lookup.binlist.net/{fbin}").json()
                try:
                    brand = bin["scheme"].upper()
                except:
                    brand = "N/A"
                try:
                    type = bin["type"].upper()
                except:
                    type = "N/A"
                try:
                    level = bin["brand"].upper()
                except:
                    level = "N/A"
                try:
                    bank_data = bin["bank"]
                except:
                    bank_data = "N/A"
                try:
                    bank = bank_data["name"].upper()
                except:
                    bank = "N/A"
                try:
                    country_data = bin["country"]
                except:
                    country_data = "N/A"
                try:
                    country = country_data["name"].upper()
                except:
                    country = "N/A"
                try:
                    flag = country_data["emoji"]
                except:
                    flag = "N/A"
                try:
                    currency = country_data["currency"].upper()
                except:
                    currency = "N/A"
                resp = f"""
VALID BIN ✅

BIN:  <code>{fbin}</code>
BRAND: {brand}
LEVEL: {level}
TYPE: {type}
BANK: {bank}
COUNTRY: {country} - {flag} - {currency}

CHECKED BY <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
Bot By <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠  ⚠️</a>
        """
                await message.reply_text(resp, message.id)
    except Exception as e:
        print(e)
