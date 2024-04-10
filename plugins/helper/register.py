#Pyrogrm Import
from pyrogram import Client, filters
#Reg Data Import
import time
from datetime import date
from datetime import timedelta
from plugins.func.users_sql import *

@Client.on_message(filters.command ('register'))
async def cmd_register(Client,message):
  try:
    user_id = str(message.from_user.id)
    username = str(message.from_user.username)
    chat_id = str(message.chat.id)
    antispam_time = int(time.time())
    reg_at = str(date.today())
    regdata = fetchinfo(user_id)
    results = str(regdata)
    bot_id = f"JOANNA-{gcgenfunc()}"
    if results=='None':
      registration = insert_reg_data(user_id,username,antispam_time,reg_at,bot_id)
      pm = fetchinfo(user_id)
      role = pm[2]
      botid = pm[10]
      credit= pm[5]
      plan = pm[3]
      aniti = pm[6]
      resp = f"""
User Registered Successfully ✅

USER BOT ID :- {botid}
Role :- {role}
Plan :- {plan}
Credit:- {credit}
Anti Spam :- {aniti}

Type /start To Know My Work Ability."""
      await message.reply_text(resp,message.id)
      await Client.send_message(grp,f"NEW USERS {user_id}")
      
    else:
      pm = fetchinfo(user_id)
      role = pm[2]
      botid = pm[10]
      credit= pm[5]
      plan = pm[3]
      aniti = pm[6]
      resp = f'''
Already Rigistered ⚠️

USER BOT ID :- {botid}
Role :- {role}
Plan :- {plan}
Credit:- {credit}
Anti Spam :- {aniti}

Type /start To Know My Work Ability .'''
      await message.reply_text(resp,message.id)
      await plan_expirychk(user_id)
    
  except Exception as e:
      print(e)
  
  
