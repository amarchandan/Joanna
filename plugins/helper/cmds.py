from pyrogram import Client, filters
from plugins.func.users_sql import *


@Client.on_message(filters.command(''))
async def cmd_cmds(Client, message):
    try:
        user_id = str(message.from_user.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == 'None':
            resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
            await message.reply_text(resp, message.id)
        else:
            user_id = str(message.from_user.id)
            # PLAN CHECK
            await plan_expirychk(user_id)
            text = """
    All of Official Checker Bot Commands ...-

➢ START BOT
➛ <code>/start</code>
➢ STRIPE AUTH 
➛ <code>/sa cc|mm|yy|cvv</code>
➢ SCRAPE CC FROM CHANNEL
➛ <code>/scr liveccbycp 100</code>
➢ CC BIN CHK
➛ <code>/bin cc|mm|yy|cvv</code>
➢ SK KEY CHECK
➛ <code>/sk sk_live_51kvhhbrfFJrdfTg</code>
➢ MAKE CC EXTRAP
➛ <code>/cxt cc|mm|yy|cvv</code>
➢ MAKE CC EXTRAP
➛ <code>/bin cc|mm|yy|cvv</code>
➢ CC GEN 
➛ <code>/gen bin</code>
➢ KNOW USER ID
➛ <code>/id</code>
➢ KNOW USER PROFILE
➛ <code>/info</code>
➢ KNOW CREDIT AMOUNT
➛ <code>/credit</code>
➢ REGISTER NEW USERS
➛ <code>/register</code>
➢ KNOW CREDIT SYSTEM
➛ <code>/crdsystem</code>
➢ ADD BOT TO UR GROUP
➛ <code>/howgp</code>
➢ BUY PAID PLAN
➛ <code>/buy</code>

MORE COMMAND AND GATES ADDING SOON !!!!
      """
        await message.reply_text(text, message.chat.id)
    except Exception as e:
        print(e)
