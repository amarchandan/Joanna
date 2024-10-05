import requests
from pyrogram import Client, filters

from plugins.bin.bins import *
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
                resp = "⚠️ #UNAUTHORIZED_CHAT ⚠️ \n Contact @clutchemiwayor To Authorize!"
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
                bb = str(fbin)
                x = mydict.get(bb, {})
                brand = x.get("brand", "N/A")
                category = x.get("category", "N/A")
                country = x.get("country", "N/A")
                flag = x.get("flag", "N/A")
                issuer = x.get("issuer", "N/A")
                Type = x.get("Type", "N/A")

                resp = f"""
VALID BIN ✅

BIN - <code>{fbin}</code>
Brand - {brand}
Category - {category}
Type - {Type}
Issuer - {issuer}
COUNTRY: {country} - {flag}
Req BY <a href="tg://user?id={message.from_user.id}"> {message.from_user.username}</a> [ {role} ]
        """
                await message.reply_text(resp, message.id)
    except Exception as e:
        print(e)
