from datetime import date, timedelta

from pyrogram import Client, filters

from plugins.func.users_sql import *


@Client.on_message(filters.command("plan3"))
async def cmd_plan3(Client, message):
    user_id = str(message.from_user.id)
    CEO = "1418571871"
    if user_id != CEO:
        resp = "Require Owner Privilages ⚠️"
        await message.reply_text(resp, message.id)
    else:
        try:
            msg = message.text[len("/plan3 ") :]
            splitter = msg.split(" ")
            userid = splitter[0]
            paymnt_method = splitter[1]
            pmid = userid
            pm_chk = fetchinfo(pmid)
            pmresults = str(pm_chk)
            if pmresults == "None":
                resp = "User Is Not Registered To The Bot ❌"
                await message.reply_text(resp, message.id)
            else:
                module_name = "plan"
                value = "Gold Plan 4.99$"
                updatedata(pmid, module_name, value)
                fetch = fetchinfo(user_id)
                credit = int(fetch[5])
                module_name = "credit"
                deduct = credit + 5000
                value = deduct
                updatedata(pmid, module_name, value)
                today = str(date.today())
                validity = str(date.today() + timedelta(days=30))
                module_name = "expiry"
                value = validity
                updatedata(pmid, module_name, value)
                module_name = "status"
                value = "PREMIUM"
                updatedata(pmid, module_name, value)
                ad_resp = f"""User <a href="tg://user?id={pmid}">{pmid}</a> Successfully Purchased GOLD Plan At 4.99$"""
                await message.reply_text(ad_resp, message.id)
                receipt_id = randgen(len=10)
                user_resp = f"""
Thanks You For Purchasing Our Gold Plan ✅

ID : <code>{pmid}</code>
Plan : GOLD
Price : 0.99$
Puurchase Date : {today}
Expiry : {validity}
Validity : 30 Days
Status : PAID ☑️
Payment Method : {paymnt_method}.
Receipt Id : Joanna-{receipt_id}

This Is A Receipt For Your Plan Saved It In A Secure PLace. This Will Help You If AnyThing Goes Wrong With Your Plan Purchases .

Have Good Day - @K3VIN_X
        """
                await Client.send_message(pmid, user_resp)
        except Exception as e:
            print(e)
