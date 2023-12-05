from pyrogram import Client, filters
import requests
import json
import re
import time
from plugins.func.users_sql import *
import requests
import json
session = requests.session()


@Client.on_message(filters.command('ip'))
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
            if message.reply_to_message:
                bin = message.reply_to_message.text
            else:
                bin = message.text[len('/ip '):]
            if len(bin) == 0:
                nocc = """
GIVE VALID IP ❌
          """
                return await message.reply_text(nocc, message.id)
            else:
                url = f"https://ipapi.com/ip_api.php?ip={input_str}"    
                async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                r = await resp.json()
                if not r.get("hostname"):
                    return await msg.edit("<code>Invalid IP. Please Check Hostname.</code>")
                ok = f"""
<b>IP :</b> <code>{r.get("ip")}</code>
<b>Hostname :</b> <code>{r.get("hostname")}</code>
<b>Type :</b> <code>{r.get("type")}</code>
<b>Country Name :</b> <code>{r.get("country_name")} {r.get("location").get("country_flag_emoji")}</code>
<b>Region Name :</b> <code>{r.get("region_name")}</code> 
<b>City :</b> <code>{r.get("city")}</code> 
<b>Zip :</b> <code>{r.get("zip")}</code> 
<b>Latitude :</b> <code>{r.get("latitude")}</code> 
<b>Longitude :</b> <code>{r.get("longitude")}</code> 
<b>Current Time :</b> <code>{r.get("time_zone").get("current_time")}</code> 
<b>Currency :</b> <code>{r.get("currency").get("name")}</code> 
<b>ISP :</b> <code>{r.get("connection").get("isp")}</code> 
<b>Is Proxy :</b> <code>{bool_to_emoji(r.get("security").get("is_proxy"))}</code>
<b>Is Crawler :</b> <code>{bool_to_emoji(r.get("security").get("is_crawler"))}</code> 
<b>Treat Level :</b> <code>{r.get("security").get("threat_level")}</code>"""
                await msg.edit(ok,message.id)
    except Exception as e:
        print(e)
