from pyrogram import Client, filters
import requests
import json
import re
import time
from plugins.func.users_sql import *
import requests
import json
session = requests.session()


@Client.on_message(filters.command('rnd'))
async def cmd_bin(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == 'None':
            resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
            await message.reply_text(resp, message.id)
        else:
            #
            # PLAN CHECK
            await plan_expirychk(user_id)
            # PM AND AUTH CHECK
            pm = fetchinfo(user_id)
            status = pm[2]
            role = status
            session = requests.session()
            tic = time.perf_counter()
            api = requests.get("https://randomuser.me/api/?nat=us&inc=name,location").json()
            mr = api["results"][0]["name"]["title"]
            nombre = api["results"][0]["name"]["first"]
            last = api["results"][0]["name"]["last"]
            loca = api["results"][0]["location"]["street"]["name"]
            nm = api["results"][0]["location"]["street"]["number"]
            city = api["results"][0]["location"]["city"]
            state = api["results"][0]["location"]["state"]
            country = api["results"][0]["location"]["country"]
            postcode = api["results"][0]["location"]["postcode"]
            latitude = api["results"][0]["location"]["coordinates"]["latitude"]
            longitude = api["results"][0]["location"]["coordinates"]["longitude"]
            toc = time.perf_counter() 
            resp = f"""
  GEN  SUCCESSFULLY 
┏－－－－－－－－－－－－┒
┠ Name - <code>{mr} {nombre} {last}</code>
┠ Street - <code>{state}</code>
┠ City - <code>{city}</code>
┠ State - <code> {loca} {nm}</code>
┠ Postal_Code - <code> {postcode}</code>
┠ Country - <code>{country}</code>
┠ Time To Chk - {toc - tic:0.4f}sec
┠ Chk By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠ ⚠️</a>
┗－－－－－－－－－－－－┛
        """
            await message.reply_text(resp, message.id)
    except Exception as e:
        print(e)
