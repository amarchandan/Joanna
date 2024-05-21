from pyrogram import Client, filters

from plugins.func.users_sql import *


@Client.on_message(filters.command("id"))
async def cmd_id(Client, message):
    try:
        user_id = str(message.from_user.id)
        str(message.chat.type)
        str(message.chat.id)
        # PLAN CHECK
        if message.reply_to_message:
            texta = f"""
Hey <a href="tg://user?id={message.reply_to_message.from_user.id}"> {message.reply_to_message.from_user.first_name}</a> !
USER ID: <code>{message.reply_to_message.from_user.id}</code> 
CHAT ID: <code>{message.chat.id}</code>
"""
            await message.reply_text(texta, message.id)
        else:
            texta = f"""
Hey <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> !
USER ID: <code>{message.from_user.id}</code> 
CHAT ID: <code>{message.chat.id}</code>
"""
            await message.reply_text(texta, message.id)
            await plan_expirychk(user_id)
    except Exception as e:
        print(e)
