from pyrogram import Client, filters

from plugins.admin.gc.gc_func import *


@Client.on_message(filters.command("getplan3"))
async def cmd_getplan3(Client, message):
    user_id = str(message.from_user.id)
    CEO = "6305901836"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        GC1 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan3(GC1)
        final_resp = f"""
GiftCode Genarated ✅
Amount :- 1
Value : Gold Plan 30 Days

➔ <code>{GC1}</code>

For Redeem
Type /redeem
    """
        await message.reply_text(final_resp, message.id)
