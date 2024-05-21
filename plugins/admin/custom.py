from pyrogram import Client, filters

from plugins.func.users_sql import *


@Client.on_message(filters.command("cs"))
async def cmd_cs(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1418571871"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        try:
            msg = message.text[len("/cs ") :]
            splitter = msg.split(" ")
            userid = splitter[0]
            module_name = splitter[1]
            value = splitter[2]
            updatedata(userid, module_name, value)
            resp = f"""
  USERID: <code>{userid}</code>
  MODULE NAME: {module_name}
  MODULE VALUE: {value}
  
     Changed
      """
            await message.reply_text(resp, message.id)
        except Exception as e:
            print(e)
