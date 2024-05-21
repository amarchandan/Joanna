from pyrogram import Client, filters

from plugins.admin.gc.gc_func import *
from plugins.func.users_sql import *


@Client.on_message(filters.command("ststs"))
async def cmd_stats(Client, message):
    try:
        user_id = str(message.from_user.id)
        str(message.chat.type)
        str(message.chat.id)
        # PLAN CHECK
        resp = f"""
        user  ==  {len(getalldata())}
        gift card == {len(getallgc())}
        """
        await message.reply_text(resp, message.id)
        await plan_expirychk(user_id)
    except Exception as e:
        print(e)
