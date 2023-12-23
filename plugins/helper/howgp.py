from pyrogram import Client, filters
from plugins.func.users_sql import *


@Client.on_message(filters.command('addbot'))
async def cmd_howgp(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        # PLAN CHECK

        texta = f"""
𝗧𝗢 𝗔𝗗𝗗 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 -

⚠️⚠️ 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗠𝗨𝗦𝗧 𝗕𝗘 𝗔𝗧𝗟𝗘𝗔𝗦𝗧 100+ 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 ⚠️⚠️

𝗙𝗜𝗥𝗦𝗧 𝗔𝗗𝗗 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 [𝙅𝙊𝘼𝙉𝙉𝘼](https://t.me/JoannaChkBot) 𝗜𝗡 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗔𝗦 𝗔𝗗𝗠𝗜𝗡. 𝗗𝗢𝗡'𝗧 𝗚𝗜𝗩𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗕𝗔𝗡 𝗨𝗦𝗘𝗥 𝗣𝗘𝗥𝗠𝗜𝗦𝗦𝗜𝗢𝗡 !

𝗧𝗛𝗔𝗧'𝗦 𝗜𝗧 . 𝗬𝗢𝗨 𝗚𝗢𝗧 𝗣𝗘𝗥𝗠𝗜𝗦𝗦𝗜𝗢𝗡 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 !
"""
        msg1 = await message.reply_text(texta, message.id)
        await plan_expirychk(user_id)
    except Exception as e:
        print(e)
