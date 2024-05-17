from pyrogram import Client, filters


@Client.on_message(filters.command("addmm"))
async def cmd_adm(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1418571871"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        resp = f"""
The Official Checker 🇮🇳 Admin Command -

● 𝗔𝗨𝗧𝗛 𝗔 𝗚𝗥𝗢𝗨𝗣 𝗖𝗠𝗗
➔ <code>/add -10098796668</code>
● 𝗨𝗡𝗔𝗨𝗧𝗛 𝗔 𝗚𝗥𝗢𝗨𝗣 𝗖𝗠𝗗
➔ <code>/del -10098796668</code>
● 𝗣𝗥𝗢𝗠𝗢𝗧𝗘 𝗔 𝗨𝗦𝗘𝗥 𝗖𝗠𝗗
➔ <code>/pm 1386450737</code>
● 𝗗𝗘𝗠𝗢𝗧𝗘 𝗔 𝗨𝗦𝗘𝗥 𝗖𝗠𝗗
➔ <code>/fr 1386450737</code>
● 𝗦𝗧𝗔𝗥𝗧𝗘𝗥 𝗣𝗟𝗔𝗡 𝗖𝗠𝗗
➔ <code>/plan1 1386450737</code>
● 𝗦𝗜𝗟𝗩𝗘𝗥 𝗣𝗟𝗔𝗡 𝗖𝗠𝗗
➔ <code>/plan2 1386450737</code>
● 𝗚𝗢𝗟𝗗 𝗣𝗟𝗔𝗡 𝗖𝗠𝗗
➔ <code>/plan3 1386450737</code>
● 𝗖𝗨𝗦𝗧𝗢𝗠 𝗨𝗦𝗘𝗥 𝗖𝗠𝗗
➔ <code>/cs 1386450737</code>
● 𝗚𝗘𝗡𝗔𝗥𝗔𝗧𝗘 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗚𝗖 𝗖𝗠𝗗
➔ <code>/pmgc 10</code>
● 𝗚𝗘𝗡𝗔𝗥𝗔𝗧𝗘 𝗦𝗧𝗔𝗥𝗧𝗘𝗥 𝗚𝗖 𝗖𝗠𝗗
➔ <code>/stgc 10</code>
● 𝗚𝗘𝗡𝗔𝗥𝗔𝗧𝗘 𝗦𝗜𝗟𝗩𝗘𝗥 𝗚𝗖 𝗖𝗠𝗗
➔ <code>/slgc 10</code>
● 𝗚𝗘𝗡𝗔𝗥𝗔𝗧𝗘 𝗚𝗢𝗟𝗗 𝗚𝗖 𝗖𝗠𝗗
➔ <code>/gldgc 10</code>
● 𝗚𝗜𝗩𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗧𝗢 𝗔 𝗨𝗦𝗘𝗥 𝗖𝗠𝗗
➔ <code>/ac 100 1386450737</code>
● 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗧𝗢 𝗔𝗟𝗟 𝗨𝗦𝗘𝗥𝗦 𝗖𝗠𝗗
➔ <code>/brd message</code>
    """
        await message.reply_text(resp, message.id)
