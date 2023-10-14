from plugins.admin.gc.gc_func import *
from pyrogram import Client, filters


@Client.on_message(filters.command('getplan3'))
async def cmd_getplan3(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1418571871"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        msg1 = await message.reply_text(resp, message.id)
    else:
        resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴.."
        send = await message.reply_text(resp, message.id)
        GC1 = f"Joanna -{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan3(GC1)

        resp = "𝗗𝗼𝗻𝗲"
        send = await Client.edit_message_text(message.chat.id, send.id, resp)
        final_resp = f"""
GiftCode Genarated ✅
Amount :- 1
Value : Gold Plan 30 Days

➔ <code>{GC1}</code>

For Redeem
Type /redeem
    """
        send = await Client.edit_message_text(message.chat.id, send.id, final_resp)
