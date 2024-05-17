from pyrogram import Client, filters

from plugins.func.users_sql import *


@Client.on_message(filters.command("brod"))
async def cmd_brod(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1418571871"
    owner = 1418571871
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        resp = "HI ALL"
        filter_user = "users"
        get_all_user = getalldata(filter_user)
        try:
            for item in get_all_user:
                chat_id = int(item[0])
                print(chat_id)
                await Client.send_message(chat_id, resp)
        except Exception as e:
            await Client.send_message(owner, e)

    done = "DONE BRODCAST ✅"

    await message.reply_text(done, message.id)
