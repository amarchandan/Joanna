import time
from datetime import date

from pyrogram import Client, filters

from plugins.func.users_sql import *
from plugins.helper.inline import *


@Client.on_message(filters.command(["start", "cmd", "cmds", "help"]))
async def cmd_start(Client, message):
    try:
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        str(message.chat.id)
        antispam_time = int(time.time())
        reg_at = str(date.today())
        regdata = fetchinfo(user_id)
        results = str(regdata)
        bot_id = f"JOANNA-{gcgenfunc()}"
        user_id = str(message.from_user.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == "None":
            insert_reg_data(user_id, username, antispam_time, reg_at, bot_id)
        else:
            None
        if results == "None":
            resp = "Hey Dude You Are Not Register ⚠️.\n\n First Register By Using /register To Use Me!"
            await message.reply_text(resp, message.id)
        else:
            user_id = str(message.from_user.id)
            str(message.chat.type)
            str(message.chat.id)
            text = f"""
Welcome to Beta version 0.2 of Joanna! >_

Stay Updated! Subscribe To Our Announcement Channel @TeamMorpho For The Latest News!

This Is The CC Checker Bot With Many Gates And Tools.
This Is The Most Optimized Version And Adapted To Multiple Tasks.
Maybe you already know this bot, Click On Menu to know all my gates.
"""
            edit = await message.reply(
                text=text, reply_markup=InlineKeyboardMarkup(menu)
            )
    except Exception as e:
        print(e)
