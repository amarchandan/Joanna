from pyrogram import Client, filters

from plugins.admin.gc.gc_func import *


@Client.on_message(filters.command("getplan1"))
async def cmd_getplan1(bot, message):
    user_id = str(message.from_user.id)
    CEO = "6305901836"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        GC1 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC1)
        GC2 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC2)
        GC3 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC3)
        GC4 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC4)
        GC5 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC5)
        GC6 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC6)
        GC7 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC7)
        GC8 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC8)
        GC9 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_plan1(GC9)
        GC10 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
        insert_pm(GC10)
        final_resp = f"""
GiftCode Genarated ✅
Amount :- 10
Value : Start Plan 7 Days

➔ <code>{GC1}</code>

➔ <code>{GC2}</code>

➔ <code>{GC3}</code>

➔ <code>{GC4}</code>

➔ <code>{GC5}</code>

➔ <code>{GC6}</code>

➔ <code>{GC7}</code>

➔ <code>{GC8}</code>

➔ <code>{GC9}</code>

➔ <code>{GC10}</code>

For Redeem
Type /redeem
    """
        await message.reply_text(final_resp, message.id)
