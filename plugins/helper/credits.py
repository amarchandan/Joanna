# IMPORT PYROGRAM MODULE
from pyrogram import Client, filters

# Reg Data Import
from plugins.func.users_sql import *


@Client.on_message(filters.command("credits"))
async def cmd_credit(Client, message):
    try:
        user_id = str(message.from_user.id)
        regdata = fetchinfo(user_id)
        credit = regdata[5]
        status = regdata[2]
        plan = regdata[3]
        results = str(regdata)
        first_name = str(message.from_user.first_name)
        if results == "None":
            resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
            await message.reply_text(resp, message.id)
        else:
            resp = f"""
Name : {first_name}
Credit : {credit}
Status : {status}
Plan : {plan}

Want More ? Type /buy To Get More Credits
      """
            await message.reply_text(resp, message.id)
            await plan_expirychk(user_id)
    except Exception as e:
        print(e)
