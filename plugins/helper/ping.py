from pyrogram import Client, filters


@Client.on_message(filters.command('ping'))
async def cmd_buy(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        # PLAN CHECK
        resp = f""" ᴘᴏɴɢ: 000.000 ms"""
        await message.reply_text(resp, message.id)
    except Exception as e:
        print(e)