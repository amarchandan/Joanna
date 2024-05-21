from pyrogram import Client, filters
from plugins.func.users_sql import *
from datetime import date
from datetime import timedelta
import random
gc = -1001582458495

@Client.on_message(filters.command("aces"))
async def cmd_plan1(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1778110596"
    if user_id != CEO:
        resp = "OWNER ONLY ⚠️"
        await message.reply_text(resp, message.id)
    else:
        try:
            msg = message.text[len("/aces ") :]
            splitter = msg.split(" ")
            userid = splitter[0]
            paymnt_method = splitter[1]
            expda = splitter[2]
            expdate = int(expda)
            ced = splitter[3]
            cred = int(ced)
            pmid = userid
            pm_chk = fetchinfo(pmid)
            pmresults = str(pm_chk)
            if pmresults == "None":
                resp = "USER IS N0T REGISTERED TO THE BOT ❌ "
                await message.reply_text(resp, message.id)
            else:
                module_name = "plan"
                value = "PREMIUM"
                updatedata(pmid, module_name, value)
                fetch = fetchinfo(user_id)
                credit = int(fetch[5])
                module_name = "credit"
                deduct = credit + cred
                value = deduct
                updatedata(pmid, module_name, value)
                today = str(date.today())
                validity = str(date.today() + timedelta(days=expdate))
                module_name = "expiry"
                value = validity
                updatedata(pmid, module_name, value)
                module_name = "status"
                value = "PREMIUM"
                updatedata(pmid, module_name, value)
                ad_resp = f"""User <a href="tg://user?id={pmid}">{pmid}</a> Your Premium Plan Is Started """
                await message.reply_text(ad_resp, message.id)
                receipt_id = randgen(len=10)
                user_resp = f"""
Thanks You For Purchasing Our Premium Plan ✅

ID : <code>{pmid}</code>
Plan : PREMIUM
Credit : {deduct}
Purchase Date : {today}
Expiry : {validity}
Status : PAID ☑️
Payment Method : {paymnt_method}
Receipt Id : Joanna-{receipt_id}

This Is A Receipt For Your Plan Saved It In A Secure PLace. This Will Help You If AnyThing Goes Wrong With Your Plan Purchases .
        """
                await Client.send_message(pmid, user_resp)
                await Client.send_message(gc, user_resp)
        except Exception as e:
            print(e)
