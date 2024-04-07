from pyrogram import Client, filters
from plugins.func.users_sql import *
from plugins.helper.inline import *


grp = "-1001582458495"

@Client.on_message(filters.command ('start'))
async def cmd_start(Client,message):
  try:
      user_id = str(message.from_user.id)
      regdata = fetchinfo(user_id)
      results = str(regdata)
      if results == 'None':
          resp = "Hey Dude You Are Not Register ⚠️.\n\n First Register By Using /register To Use Me!"
          await message.reply_text(resp, message.id)
      else:
          user_id = str(message.from_user.id)
          chat_type = str(message.chat.type)
          chat_id = str(message.chat.id)
          text = f"""
Welcome to Beta version 0.2 of Joanna! >_

Stay Updated! Subscribe To Our Announcement Channel @TeamMorpho For The Latest News!

This Is The CC Checker Bot With Many Gates And Tools.
This Is The Most Optimized Version And Adapted To Multiple Tasks.
Maybe you already know this bot, Click On Menu to know all my gates.
"""
          edit = await message.reply(
              text=text,
              reply_markup=InlineKeyboardMarkup(menu)
              )
          await Client.send_message(grp,f"NEW USERS {user_id}")
  except Exception as e:
      print(e)
