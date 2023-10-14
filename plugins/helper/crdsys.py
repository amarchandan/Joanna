from pyrogram import Client, filters
from plugins.func.users_sql import *


@Client.on_message(filters.command('crdsystem'))
async def cmd_crdsystem(Client, message):
    try:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        # PLAN CHECK
        resp = f"""
Official Checker Bot Credit System....

● Auth Gates
➔ 1 Credit Per CC Check

● Charge Gates
➔ 1 Credit Per CC Check

● Mass Suth Gates
➔ 1 Credit Per CC Check

● Mass Charge Gates
➔ 1 Credit Per CC Check

● cc Scraper Gates
➔ 1 Credit Per Scraping
    """
        msg1 = await message.reply_text(resp, message.id)
        await plan_expirychk(user_id)
    except Exception as e:
        print(e)
