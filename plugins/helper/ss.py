from pyrogram import Client, filters

from plugins.func.users_sql import *
from plugins.helper.inline import *


@Client.on_message(filters.command(["start", "cmd", "cmds", "help"]))
async def cmd_start(Client, message):
    try:
        user_id = str(message.from_user.id)
        regdata = fetchinfo(user_id)
        str(regdata)
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
        edit = await message.reply(text=text, reply_markup=InlineKeyboardMarkup(menu))
    except Exception as e:
        print(e)
