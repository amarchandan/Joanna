# Pyrogrm Import
# Reg Data Import
import time
from datetime import date

from pyrogram import Client, filters

from plugins.func.users_sql import *


@Client.on_message(filters.command("register"))
async def cmd_register(Client, message):
    try:
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        str(message.chat.id)
        antispam_time = int(time.time())
        reg_at = str(date.today())
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == "None":
            insert_reg_data(user_id, username, antispam_time, reg_at)
            pm = fetchinfo(user_id)
            role = pm[2]
            credit = pm[5]
            plan = pm[3]
            aniti = pm[6]
            resp = f"""
User Registered Successfully ✅

Role :- {role}
Plan :- {plan}
Credit:- {credit}
Anti Spam :- {aniti}

Type /start To Know My Work Ability."""
            await message.reply_text(resp, message.id)

        else:
            pm = fetchinfo(user_id)
            role = pm[2]
            credit = pm[5]
            plan = pm[3]
            aniti = pm[6]
            resp = f"""
Already Rigistered ⚠️

Role :- {role}
Plan :- {plan}
Credit:- {credit}
Anti Spam :- {aniti}

Type /start To Know My Work Ability ."""
            await message.reply_text(resp, message.id)
            await plan_expirychk(user_id)

    except Exception as e:
        print(e)
