from pyrogram import Client, filters
from plugins.func.users_sql import *


@Client.on_message(filters.command('fr'))
async def cmd_fr(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1418571871"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        msg1 = await message.reply_text(resp, message.id)
    else:
        try:
            if message.reply_to_message:
                userpm = message.reply_to_message.from_user.id
            else:
                userpm = message.text[len('/fr '):]
            pmid = userpm
            pm_chk = fetchinfo(pmid)
            status = str(pm_chk[2])
            if status != 'PREMIUM':
                resp = f"""
<a href="tg://user?id={pmid}">{pmid}</a> Is Already A 'FREE' User ⚠️.
        """
                await message.reply_text(resp, message.id)
            else:
                module_name = "status"
                value = "FREE"
                updatedata(pmid, module_name, value)
                resp = f"""
<a href="tg://user?id={pmid}">{pmid}</a> Is Demoted To A 'FREE' User ✅.
        """
                await message.reply_text(resp, message.id)
                user_resp = """Hey Dude ! 
 Your Account Successfully Demoted To 'FREE' User✅"""
                await Client.send_message(pmid, user_resp)

        except Exception as e:
            print(e)
