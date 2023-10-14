from plugins.admin.gc.gc_func import *
from pyrogram import Client, filters


@Client.on_message(filters.command('getplan2'))
async def cmd_getplan2(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1418571871"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        msg1 = await message.reply_text(resp, message.id)
    else:
        resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴.."
        send = await message.reply_text(resp, message.id)
        GC1 = f"Joanna -{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC1)
        GC2 = f"Joanna -{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC2)
        GC3 = f"Joanna -{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC3)
        GC4 = f"Joanna -{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC4)
        GC5 = f"Joanna -{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC5)

        resp = "𝗗𝗼𝗻𝗲"
        send = await Client.edit_message_text(message.chat.id, send.id, resp)
        final_resp = f"""
GiftCode Genarated ✅
Amount :- 𝟱
Value : Silver PLan 15 Days

➔ <code>{GC1}</code>

➔ <code>{GC2}</code>

➔ <code>{GC3}</code>

➔ <code>{GC4}</code>

➔ <code>{GC5}</code>


For Redeem
Type /redeem
    """
        send = await Client.edit_message_text(message.chat.id, send.id, final_resp)
