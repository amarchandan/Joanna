from pyrogram import Client, filters

from plugins.admin.gc.gc_func import *


@Client.on_message(filters.command("getplan2"))
async def cmd_getplan2(Client, message):
    user_id = str(message.from_user.id)
    CEO = "6305901836"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        resp = "𝗚𝗲𝗻𝗮𝗿𝗮𝘁𝗶𝗻𝗴.."
        await message.reply_text(resp, message.id)
        GC1 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC1)
        GC2 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC2)
        GC3 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC3)
        GC4 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC4)
        GC5 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan2(GC5)
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
        await message.reply_text(final_resp, message.id)
