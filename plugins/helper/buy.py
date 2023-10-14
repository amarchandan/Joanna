from pyrogram import Client, filters
from plugins.func.users_sql import *


@Client.on_message(filters.command('buy'))
async def cmd_buy(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        # PLAN CHECK
        resp = f"""
SOON COMING
    """
        msg1 = await message.reply_text(resp, message.id)
        await plan_expirychk(user_id)
    except Exception as e:
        print(e)
