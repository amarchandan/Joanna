from pyrogram import Client, filters
from plugins.func.users_sql import *
from plugins.helper.inline import *

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
Welcome to version 0.1 of Joanna! >_

𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}></a>
    I Am CC Checker Bot With Many Gates And Tools.
    And Is The Most Optimized Version And Adapted To Multiple Tasks.
"""
          edit = await message.reply(
              text=text,
              reply_markup=InlineKeyboardMarkup(buttons)
              )
  except Exception as e:
      print(e)
