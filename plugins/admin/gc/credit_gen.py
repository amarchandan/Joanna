from plugins.admin.gc.gc_func import *
from pyrogram import Client, filters

@Client.on_message(filters.command ('gc'))
async def cmd_gc(client,message):
  user_id = str(message.from_user.id)
  CEO = "6305901836"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    GC1 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC1)
    GC2 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC2)
    GC3 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC3)
    GC4 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC4)
    GC5 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC5)
    GC6 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC6)
    GC7 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC7)
    GC8 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC8)
    GC9 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC9)
    GC10 = f"JOANNA-{gcgenfunc()}-{gcgenfunc()}-{gcgenfunc()}"
    insert_pm(GC10)
    respa = "𝗗𝗼𝗻𝗲"
    await message.reply_text(respa, message.id)
    final_resp = f"""
GiftCode Genarated ✅
Amount : 10
Value : 50 Credits + 2 Day PREMIUM

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
    send = await message.reply_text(final_resp, message.id)
