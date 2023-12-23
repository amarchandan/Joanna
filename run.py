import asyncio
import logging
from pathlib import Path
from pyrogram import Client, compose, filters, enums
from defs import getcards
import asyncio
from pyrogram import Client, compose
from plugins.func.users_sql import *

logging.basicConfig(level=logging.INFO)

plugins = dict(root="plugins")

async def main():
  user = Client("Joanna_Scr",
                api_id="20126690",
                api_hash="3ea37bd78cb3a8ca92caac7a23b542d9",
                session_string="BQF3CWcAB2_yaSoxgteSvk4uc_uqFOZc4iYMB48U0TMLNiEFDDR5CG31rzt77C43Z4LUYIMshmbEfYiuIX0oA85M9-rt5x3avvA4CbJupRIsjDEi83xHOeXq9l6QPRo-zYiJQkBhrMciUiJsSnHWVVN_bPflLVYtXulr_yYAJWh8SiiahKF5S43NbhHMtY_3MIiKYO6FJ7lLY8Mt5ItHF0R-GaX8_633LdRuATMbEs-s1Y5yZQFEIMfh2SW39WFgAleez8sjaV0-WAfLLq1XtIQkHkcEbLLQSUt5AN7GQyl2VbVt2LJ9wUkcYKVcoGTGgDy8ZvAQ_vrotzv5tV_TJkriyV75MQAAAAF33G0MAA")
  bot = Client("Joanna_Bot",
               api_id="20126690",
               api_hash="3ea37bd78cb3a8ca92caac7a23b542d9",
               bot_token="6327788045:AAFSvNAUlUCIMgPceFChvMLfo-edJqqJ7GM",
               plugins=plugins)
  clients = [user, bot]
  bot.set_parse_mode(enums.ParseMode.HTML)

  @bot.on_message(filters.command('adm'))
  async def cmd_help(client, message):
    await message.reply_text("i am working", message.id)

  @bot.on_message(filters.command('scr'))
  async def cmd_scr(client, message):
    msg = message.text[len('/scr '):]
    splitter = msg.split(' ')
    if len(msg) == 0:
      resp = f"""
OPPS! Format Error

Usage :-
#PUBLIC_GROUP
<code>/scr username 100</code>

#PRIVATE_GROUP
<code>/scr https://t.me/+fcY29MEGgmkwYjNl 50</code>

        """
      await message.reply_text(resp, message.id)
    else:
      #
      user_id = str(message.from_user.id)
      chat_type = str(message.chat.type)
      chat_id = str(message.chat.id)
      #PLAN CHECK

      regdata = fetchinfo(user_id)
      results = str(regdata)
      if results == 'None':
        resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me!"
        await message.reply_text(resp, message.id)
      else:
        #HERE
        #PM AND AUTH CHECK
        pm = fetchinfo(user_id)
        status = pm[2]
        role = status
        #CREDIT CHECK
        chk_credit = fetchinfo(user_id)
        credit = int(chk_credit[5])
        if credit < 3:
          resp = ""
          await message.reply_text(resp, message.id)
        else:
          #ANTISPAM MODULE
          user_id = str(message.from_user.id)
          results = fetchinfo(user_id)
          status = results[2]
          try:
            limit = int(splitter[1])
          except:
            limit = 100
            delete = await message.reply_text("SCRAPING ...", message.id)
            channel_link = splitter[0]
            if "https" in channel_link:
              try:
                join = await user.join_chat(channel_link)
                title = join.title
                channel_id = join.id
                amt_cc = 0
                dublicate = 0
                async for msg in user.get_chat_history(channel_id, limit):
                  all_history = str(msg.text)
                  if all_history == 'None':
                    all_history = "INVALID CC NUMBER BC"
                  else:
                    all_history = all_history
                  all_cards = all_history.split('\n')
                  cards = []
                  for x in all_cards:
                    car = getcards(x)
                    if car:
                      cards.append(car)
                    else:
                      continue
                  len_cards = len(cards)
                  if not len_cards:
                    resp = "Not Found Any Valid Card"
                  for item in cards:
                    amt_cc += 1
                    cc = item[0]
                    mes = item[1]
                    ano = item[2]
                    cvv = item[3]
                    fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                    file_name = f"{limit}x_By_@JoannaChkBot.txt"
                    with open(file_name, 'a') as f:
                      cclist = open(f"{file_name}").read().splitlines()
                      if fullcc in cclist:
                        dublicate += 1
                      else:
                        f.write(f"{fullcc}\n")
                total_cc = amt_cc
                cc_found = total_cc - dublicate
                await bot.delete_messages(message.chat.id, delete.id)
                caption = f"""
SCRAPPING COMPLETED ✅
┏－－－－－－－－－－－－┒
┠ Source -{title}
┠ Amount - {limit}
┠ Found - {cc_found}
┠ Removed - {dublicate}
┠ Scraped By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {status} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠  ⚠️</a>
┗－－－－－－－－－－－－┛
"""
                document = file_name
                scr_done = await message.reply_document(
                  document=document,
                  caption=caption,
                  reply_to_message_id=message.id)
                module_name = "credit"
                deduct = credit - 1
                value = deduct
                updatedata(user_id, module_name, value)
                if scr_done:
                  name = document
                  my_file = Path(name)
                  my_file.unlink(missing_ok=True)
              except Exception as e:
                e = str(e)
                fr_error = ''
                sec_error = ''
                if e == 'Telegram says: [400 USER_ALREADY_PARTICIPANT] - The user is already a participant of this chat (caused by "messages.ImportChatInvite")':
                  chat_info = await user.get_chat(channel_link)
                  channel_id = chat_info.id
                  title = chat_info.title
                  try:
                    amt_cc = 0
                    dublicate = 0
                    async for msg in user.get_chat_history(
                        channel_id, limit):
                      all_history = str(msg.text)
                      if all_history == 'None':
                        all_history = "INVALID CC NUMBER BC"
                      else:
                        all_history = all_history
                        all_cards = all_history.split('\n')
                        cards = []
                        for x in all_cards:
                          car = getcards(x)
                          if car:
                            cards.append(car)
                          else:
                            continue
                        len_cards = len(cards)
                        if not len_cards:
                          resp = "Not Found Any Valid Card"
                        for item in cards:
                          amt_cc += 1
                          cc = item[0]
                          mes = item[1]
                          ano = item[2]
                          cvv = item[3]
                          fullcc = f"{cc}|{mes}|{ano}|{cvv}"

                          file_name = f"{limit}x_By_@JoannaChkBot.txt"
                          with open(file_name, 'a') as f:
                            cclist = open(f"{file_name}").read().splitlines()
                            if fullcc in cclist:
                              dublicate += 1
                            else:
                              f.write(f"{fullcc}\n")

                      total_cc = amt_cc
                      cc_found = total_cc - dublicate
                      await bot.delete_messages(message.chat.id, delete.id)
                      caption = f"""
SCRAPPING COMPLETED ✅
┏－－－－－－－－－－－－┒
┠ Source -{title}
┠ Amount - {limit}
┠ Found - {cc_found}
┠ Removed - {dublicate}
┠ Scraped By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {status} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠  ⚠️</a>
┗－－－－－－－－－－－－┛
"""
                      document = file_name
                      scr_done = await message.reply_document(
                        document=document,
                        caption=caption,
                        reply_to_message_id=message.id)
                      module_name = "credit"
                      deduct = credit - 1
                      value = deduct
                      updatedata(user_id, module_name, value)

                      if scr_done:
                        name = document
                        my_file = Path(name)
                        my_file.unlink(missing_ok=True)
                  except Exception as e:
                    await bot.delete_messages(message.chat.id, delete.id)
                    await message.reply_text(e, message.id)
                elif e == 'Telegram says: [400 INVITE_HASH_EXPIRED] - The chat invite link is no longer valid (caused by "messages.ImportChatInvite")':
                  resp = "Wrong Invite Link ❌"
                  await bot.delete_messages(message.chat.id, delete.id)
                  await message.reply_text(resp, message.id)
                else:
                  await bot.delete_messages(message.chat.id, delete.id)
                  await message.reply_text(e, message.id)
              else:
                try:
                  amt_cc = 0
                  dublicate = 0
                  async for msg in user.get_chat_history(channel_link, limit):
                    all_history = str(msg.text)
                    if all_history == 'None':
                      all_history = "INVALID CC NUMBER BC"
                    else:
                      all_history = all_history
                    all_cards = all_history.split('\n')
                    cards = []
                    for x in all_cards:
                      car = getcards(x)
                      if car:
                        cards.append(car)
                      else:
                        continue
                    len_cards = len(cards)
                    if not len_cards:
                      resp = "Not Found Any Valid Card"
                    for item in cards:
                      amt_cc += 1
                      cc = item[0]
                      mes = item[1]
                      ano = item[2]
                      cvv = item[3]
                      fullcc = f"{cc}|{mes}|{ano}|{cvv}"

                      file_name = f"{limit}x_By_@JoannaChkBot.txt"
                      with open(file_name, 'a') as f:
                        cclist = open(f"{file_name}").read().splitlines()
                        if fullcc in cclist:
                          dublicate += 1
                        else:
                          f.write(f"{fullcc}\n")

                  chat_info = await user.get_chat(channel_link)
                  title = chat_info.title
                  total_cc = amt_cc
                  cc_found = total_cc - dublicate
                  await bot.delete_messages(message.chat.id, delete.id)
                  caption = f"""
SCRAPPING COMPLETED ✅
┏－－－－－－－－－－－－┒
┠ Source -{title}
┠ Amount - {limit}
┠ Found - {cc_found}
┠ Removed - {dublicate}
┠ Scraped By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {status} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠  ⚠️</a>
┗－－－－－－－－－－－－┛
"""
                  document = file_name
                  scr_done = await message.reply_document(
                    document=document,
                    caption=caption,
                    reply_to_message_id=message.id)
                  module_name = "credit"
                  deduct = credit - 1
                  value = deduct
                  updatedata(user_id, module_name, value)

                  if scr_done:
                    name = document
                    my_file = Path(name)
                    my_file.unlink(missing_ok=True)

                except Exception as e:
                  e = str(e)
                  if e == "Error : local variable 'file_name' referenced before assignment":
                    resp = "No CC Found"
                    await bot.delete_messages(message.chat.id, delete.id)
                    await message.reply_text(text=resp,
                                             reply_to_message_id=message.id)
                  elif e == 'Telegram says: [400 USERNAME_NOT_OCCUPIED] - The username is not occupied by anyone (caused by "contacts.ResolveUsername")':
                    resp = "Wrong UserName ❌"
                    await bot.delete_messages(message.chat.id, delete.id)
                    await message.reply_text(text=resp,
                                             reply_to_message_id=message.id)
                  elif e == "local variable 'file_name' referenced before assignment":
                    resp = "No CCs Found ❌"
                    await bot.delete_messages(message.chat.id, delete.id)
                    await message.reply_text(text=resp,
                                             reply_to_message_id=message.id)
                  elif e == 'Telegram says: [400 USERNAME_INVALID] - The username is invalid (caused by "contacts.ResolveUsername")':
                    resp = "Wrong UserName ❌"
                    await bot.delete_messages(message.chat.id, delete.id)
                    await message.reply_text(text=resp,
                                             reply_to_message_id=message.id)
                  else:
                    await bot.delete_messages(message.chat.id, delete.id)
                    await message.reply_text(text=e,
                                             reply_to_message_id=message.id)

  print("Done Bot Active ✅")
  await compose(clients)
asyncio.run(main())
