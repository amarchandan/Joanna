import time

import requests
from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()


@Client.on_message(filters.command("rnd"))
async def cmd_bin(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        str(message.chat.type)
        str(message.chat.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == "None":
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
            requests.session()
            tic = time.perf_counter()
            api = requests.get(
                "https://randomuser.me/api/?nat=us&inc=name,location"
            ).json()
            mr = api["results"][0]["name"]["title"]
            nombre = api["results"][0]["name"]["first"]
            last = api["results"][0]["name"]["last"]
            loca = api["results"][0]["location"]["street"]["name"]
            nm = api["results"][0]["location"]["street"]["number"]
            city = api["results"][0]["location"]["city"]
            state = api["results"][0]["location"]["state"]
            country = api["results"][0]["location"]["country"]
            postcode = api["results"][0]["location"]["postcode"]
            api["results"][0]["location"]["coordinates"]["latitude"]
            api["results"][0]["location"]["coordinates"]["longitude"]
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
┠ Req by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.username}</a> | [ {role} ]
┗－－－－－－－－－－－－┛
        """
            await message.reply_text(resp, message.id)
    except Exception as e:
        print(e)
