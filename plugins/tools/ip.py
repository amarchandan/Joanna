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
async def cmd_ipp(Client, message):
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
                pm = fetchinfo(user_id)
                status = pm[2]
                role = status
                url = f"https://ipapi.com/ip_api.php?ip={bin}"    
                resp = requests.get(url)
                r = resp.json()
                if not r.get("hostname"):
                    await message.reply_text("<code>Invalid IP. Please Check Hostname.</code>")
                else:
                    ok = f"""
CHECK  SUCCESSFULLY 
┏－－－－－－－－－－－－－┒
┠ <b>IP :</b> <code>{r.get("ip")}</code>
┠ <b>Hostname :</b> <code>{r.get("hostname")}</code>
┠ <b>Type :</b> <code>{r.get("type")}</code>
┠ <b>Country Name :</b> <code>{r.get("country_name")} {r.get("location").get("country_flag_emoji")}</code>
┠ <b>Region Name :</b> <code>{r.get("region_name")}</code> 
┠ <b>City :</b> <code>{r.get("city")}</code> 
┠ <b>Zip :</b> <code>{r.get("zip")}</code> 
┠ <b>Latitude :</b> <code>{r.get("latitude")}</code> 
┠ <b>Longitude :</b> <code>{r.get("longitude")}</code> 
┠ <b>Continent :</b> <code>{r.get('continent_name', '')}</code>
┠ <b>ASN :</b> <code>{r.get('connection', {}).get('asn', '')}</code>
┠ <b>Current Time :</b> <code>{r.get("time_zone").get("current_time")}</code> 
┠ <b>Currency :</b> <code>{r.get("currency").get("name")}</code> 
┠ <b>ISP :</b> <code>{r.get("connection").get("isp")}</code> 
┠ <b>Is Proxy :</b> <code>{r.get('security', {}).get('is_proxy', {})}</code>
┠ <b>Is Crawler :</b> <code>{r.get('security', {}).get('is_crawler', {})}</code> 
┠ <b>Crawler Type :</b> <code>{r.get('security', {}).get('crawler_type', {})}</code>
┠ <b>Threat Type:</b> <code>{r.get('security', {}).get('threat_types', [])}</code>
┠ <b>Threat Level :</b> <code>{r.get('security', {}).get('threat_level', '')}</code>
┠ Chk By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠ ⚠️</a>
┗－－－－－－－－－－－－┛"""
                    await message.reply_text(ok, message.id)
    except Exception as e:
        print(e)