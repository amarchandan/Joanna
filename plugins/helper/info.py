from pyrogram import Client, filters
from plugins.func.users_sql import *

@Client.on_message(filters.command ('info'))
async def cmd_info(Client,message):
  try:
    user_id = str(message.from_user.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
      await message.reply_text(resp,message.id)
    else:
      
      if message.reply_to_message:
        user_id = str(message.reply_to_message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK 
        await plan_expirychk(user_id)
        user_id = str(message.reply_to_message.from_user.id)
        username = str(message.reply_to_message.from_user.username)
        first_name = str(message.reply_to_message.from_user.first_name)
        info = fetchinfo(user_id)
        results = str(info)
        if results=="None":
          send_info = f"""
User Info
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┠ FristName : {first_name}
┠ ID : <code>{user_id}</code>
┠ UserName : {username}
┠ Profile : <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
┠ Tg Restrictions : {message.reply_to_message.from_user.is_restricted}
┠ Tg ScamTag : {message.reply_to_message.from_user.is_scam}
┠ Tg Premium : {message.reply_to_message.from_user.is_premium}
┠ Status : NOT REGISTERED
┠ Credit : N/A
┠ Plan: N/A
┠ Plan Expiry : N/A
┠ Key Redeemed : N/A
┠ Registered At : N/A
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
          await message.reply_text(send_info,message.id)
        else:
          pid = str(message.reply_to_message.from_user.id)
          await plan_expirychk(pid)
          info = fetchinfo(user_id)
          results = info
          botid = results[10]
          status = results[2]
          plan = results[3]
          expiry = results[4]
          credit = results[5]
          antispam = results[6]
          antispam_time = results[7]
          totalkey = results[8]
          reg_at = results[9]
          send_info = f"""
User Info
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┠ FristName : {first_name}
┠ BOT ID : {botid}
┠ ID : <code>{user_id}</code>
┠ UserName : {username}
┠ Profile : <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
┠ Tg Restrictions : {message.reply_to_message.from_user.is_restricted}
┠ Tg ScamTag : {message.reply_to_message.from_user.is_scam}
┠ Tg Premium : {message.reply_to_message.from_user.is_premium}
┠ Status : {status}
┠ Credit : {credit}
┠ Plan: {plan}
┠ Plan Expiry : {expiry}
┠ Key Redeemed : {totalkey}
┠ Registered At : {reg_at}
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
          await message.reply_text(send_info,message.id)
      else:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK 
        await plan_expirychk(user_id)
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        first_name = str(message.from_user.first_name)
        info = fetchinfo(user_id)
        results = str(info)
        if results=="None":
          send_info = f"""
User Info
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┠ FristName : {first_name}
┠ ID : <code>{user_id}</code>
┠ UserName : {username}
┠ Profile : <a href="tg://user?id={message.from_user.id}">Profile Link</a>
┠ Tg Restrictions : {message.from_user.is_restricted}
┠ Tg ScamTag : {message.from_user.is_scam}
┠ Tg Premium : {message.from_user.is_premium}
┠ Status : NOT REGISTERED
┠ Credit : N/A
┠ Plan: N/A
┠ Plan Expiry : N/A
┠ Key Redeemed : N/A
┠ Registered At : N/A
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
          await message.reply_text(send_info,message.id)
        else:
          pid = str(message.from_user.id)
          await plan_expirychk(pid)
          info = fetchinfo(user_id)
          results = info
          botid = results[10]
          status = results[2]
          plan = results[3]
          expiry = results[4]
          credit = results[5]
          antispam = results[6]
          antispam_time = results[7]
          totalkey = results[8]
          reg_at = results[9]
          send_info = f"""
User Info
┏━━━━━━━━━━━━━━━━━━━━━━━
┠ FristName : {first_name}
┠ BOT ID : {botid}
┠ ID : <code>{user_id}</code>
┠ UserName : {username}
┠ Profile : <a href="tg://user?id={message.from_user.id}">Profile Link</a>
┠ Tg Restrictions : {message.from_user.is_restricted}
┠ Tg ScamTag : {message.from_user.is_scam}
┠ Tg Premium : {message.from_user.is_premium}
┠ Status : {status}
┠ Credit : {credit}
┠ Plan: {plan}
┠ Plan Expiry : {expiry}
┠ Key Redeemed : {totalkey}
┠ Registered At : {reg_at}
┗━━━━━━━━━━━━━━━━━━━━━━━
  """
        await message.reply_text(send_info,message.id)
  except Exception as e:
      print(e)