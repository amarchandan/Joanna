from pyrogram import Client, filters
from plugins.func.users_sql import *


@Client.on_message(filters.command('howgp'))
async def cmd_howgp(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        # PLAN CHECK

        texta = f"""
𝗧𝗢 𝗔𝗗𝗗 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 -

⚠️⚠️ 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗠𝗨𝗦𝗧 𝗕𝗘 𝗔𝗧𝗟𝗘𝗔𝗦𝗧 100+ 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 ⚠️⚠️

𝗙𝗜𝗥𝗦𝗧 𝗔𝗗𝗗 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 [ @lol ] 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗔𝗦 𝗔𝗗𝗠𝗜𝗡. 𝗗𝗢𝗡'𝗧 𝗚𝗜𝗩𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗕𝗔𝗡 𝗨𝗦𝗘𝗥 𝗣𝗘𝗥𝗠𝗜𝗦𝗦𝗜𝗢𝗡. 

𝗧𝗛𝗘𝗡 𝗔𝗗𝗗 <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠  ⚠️</a> 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗔𝗡𝗗 𝗚𝗜𝗩𝗘 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗖𝗛𝗔𝗧 𝗜𝗗 𝗧𝗢 𝗛𝗜𝗠. . 𝗛𝗘 𝗪𝗜𝗟𝗟 𝗔𝗣𝗣𝗥𝗢𝗩𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣. 

𝗧𝗛𝗔𝗧'𝗦 𝗜𝗧 . 𝗬𝗢𝗨 𝗚𝗢𝗧 𝗣𝗘𝗥𝗠𝗜𝗦𝗦𝗜𝗢𝗡 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 😍.
"""
        msg1 = await message.reply_text(texta, message.id)
        await plan_expirychk(user_id)
    except Exception as e:
        print(e)
