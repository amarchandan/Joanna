from pyrogram import Client, filters
import requests
from plugins.func.users_sql import *

session = requests.session()

@Client.on_message(filters.command('sk'))
async def cmd_sk(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == 'None':
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
            if chat_type == "ChatType.PRIVATE" and status == "FREE":
                resp = "⚠️ #PREMIUM_ONLY ⚠️ \n Contact @K3VIN_X To Buy Premium Access !.Else You Can Use Free Then Join @MorPhoChat !"
                await message.reply_text(resp, message.id)
            else:
                if message.reply_to_message:
                    sk = message.reply_to_message.text
                else:
                    sk = message.text[len('/sk '):]
                if len(sk) == 0:
                    nocc = """
  𝗣𝗟𝗘𝗔𝗦𝗘 𝗣𝗥𝗢𝗩𝗜𝗗𝗘 𝗔 𝗦𝗞 𝗞𝗘𝗬 𝗧𝗢 𝗖𝗛𝗘𝗖𝗞 ⚠️
          """
                    return await message.reply_text(nocc, message.id)
                else:
                    chkst = "𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗦𝗞 𝗪𝗮𝗶𝘁...."
                    done = await message.reply_text(chkst, message.id)
                    skchk = f"https://rembleampi.site/api/sk.php?sk={sk}"
                    skinfo = requests.get(skchk)
                    result = skinfo.text

          
                    await Client.edit_message_text(message.chat.id, done.id, result)
    except Exception as e:
        print(e)
