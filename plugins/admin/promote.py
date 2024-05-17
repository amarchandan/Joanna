from pyrogram import Client, filters

from plugins.func.users_sql import *


@Client.on_message(filters.command("pm"))
async def cmd_pm(Client, message):
    try:
        user_id = str(message.from_user.id)
        CEO = "1418571871"
        if user_id != CEO:
            resp = "Require Owner Privilages ⚠️"
            await message.reply_text(resp, message.id)
        else:
            if message.reply_to_message:
                userpm = message.reply_to_message.from_user.id
            else:
                userpm = message.text[len("/pm ") :]
            pmid = userpm
            pm_chk = fetchinfo(pmid)
            status = str(pm_chk[2])
            if status != "FREE":
                resp = f"""
  <a href="tg://user?id={pmid}">{pmid}</a> Is Already Premium User ⚠️.
        """
                await message.reply_text(resp, message.id)
            else:
                module_name = "status"
                value = "PREMIUM"
                updatedata(pmid, module_name, value)
                resp = f"""
  <a href="tg://user?id={pmid}">{pmid}</a> Is Promoted To A Premium Uuser ✅.
        """
                await message.reply_text(resp, message.id)
                user_resp = """Hey Dude ! 
Your Account Successfully Promoted To 'PREMIUM' User ✅"""
                await Client.send_message(pmid, user_resp)

    except Exception as e:
        print(e)
