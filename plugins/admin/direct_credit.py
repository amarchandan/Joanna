from pyrogram import Client, filters

from plugins.func.users_sql import *


@Client.on_message(filters.command("ac"))
async def cmd_ac(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1418571871"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        try:
            msg = message.text[len("/ac ") :]
            splitter = msg.split(" ")
            amt = int(splitter[0])
            user_id = splitter[1]
            module_name = "credit"
            fetch = fetchinfo(user_id)
            credit = int(fetch[5])
            value = credit + amt
            updatedata(user_id, module_name, value)
            resp = f"""
<code>{amt}</code> Credit Added To <a href="tg://user?id={user_id}">{user_id}</a> Successfully ✅
      """
            await message.reply_text(resp, message.id)
            user_sms = f"""
Congrats ! 
Your Account Just Got {amt} Credits ✅

Type /credits To Know Your Current Credits
      """
            await Client.send_message(user_id, user_sms)
        except Exception as e:
            print(e)
