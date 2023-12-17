from plugins.admin.gc.gc_func import *
from pyrogram import Client, filters
from plugins.func.users_sql import *
from datetime import date
from datetime import timedelta


grp = "-1002122350640"

@Client.on_message(filters.command('redeem'))
async def cmd_gc(Client, message):
    try:
        user_id = str(message.from_user.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == 'None':
            resp = "You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
            await message.reply_text(resp, message.id)
        else:
            user_id = str(message.from_user.id)
            gc = message.text[len('/redeem '):]
            resp = f"{gc}"
            get = getgc(gc)
            t = str(get)
            if t == 'None':
                resp = "INVALID GIFTCODE ❌ "
                await message.reply_text(resp, message.id)
            else:
                t = getgc(gc)
                status = t[1]
                plan = t[2]

                if status == 'ACTIVE':
                    if plan == 'PREMIUM':
                        fetch = fetchinfo(user_id)
                        tkey = int(fetch[8])
                        value = tkey + 1
                        module_name = "totalkey"
                        updatedata(user_id, module_name, value)
                        credit = int(fetch[5])
                        value = credit + 100
                        module_name = "credit"
                        updatedata(user_id, module_name, value)
                        module_name = "status"
                        value = "PREMIUM"
                        updatedata(user_id, module_name, value)
                        module_name = "expiry"
                        today = str(date.today())
                        value = str(date.today()+timedelta(days=5))
                        updatedata(user_id, module_name, value)
                        updategc(gc)
                        resp = "Redeem Successfully GiftCard To Your Account ✅. Type /credits To Know Credits"
                        await message.reply_text(resp, message.id)
                        await Client.send_message(grp,f"REDEM    {user_id}" )
                    elif plan == 'PLAN1':
                        fetch = fetchinfo(user_id)
                        tkey = int(fetch[8])
                        value = tkey + 1
                        module_name = "totalkey"
                        updatedata(user_id, module_name, value)
                        credit = int(fetch[5])
                        value = credit + 1000
                        module_name = "credit"
                        updatedata(user_id, module_name, value)
                        module_name = "status"
                        value = "PREMIUM"
                        updatedata(user_id, module_name, value)
                        module_name = "plan"
                        value = "Starter Plan 0.99$"
                        updatedata(user_id, module_name, value)
                        module_name = "expiry"
                        today = str(date.today())
                        value = str(date.today()+timedelta(days=7))
                        updatedata(user_id, module_name, value)
                        updategc(gc)
                        resp = "You Have Successfully Redeemed 'Starter Plan' Using GiftCode ✅.Type /info To Know More"
                        await message.reply_text(resp, message.id)
                        await Client.send_message(grp,"redem" )
                    elif plan == 'PLAN2':
                        fetch = fetchinfo(user_id)
                        tkey = int(fetch[8])
                        value = tkey + 1
                        module_name = "totalkey"
                        updatedata(user_id, module_name, value)
                        credit = int(fetch[5])
                        value = credit + 2000
                        module_name = "credit"
                        updatedata(user_id, module_name, value)
                        module_name = "status"
                        value = "PREMIUM"
                        updatedata(user_id, module_name, value)
                        module_name = "plan"
                        value = "Silver Plan 1.99$"
                        updatedata(user_id, module_name, value)
                        module_name = "expiry"
                        today = str(date.today())
                        value = str(date.today()+timedelta(days=15))
                        updatedata(user_id, module_name, value)
                        updategc(gc)
                        resp = "You Have Successfully Redeemed 'Silver Plan' Using GiftCode ✅.Type /info To Know More"
                        await message.reply_text(resp, message.id)
                        await Client.send_message(grp,"redem" )
                    elif plan == 'PLAN3':
                        fetch = fetchinfo(user_id)
                        tkey = int(fetch[8])
                        value = tkey + 1
                        module_name = "totalkey"
                        updatedata(user_id, module_name, value)
                        credit = int(fetch[5])
                        value = credit + 5000
                        module_name = "credit"
                        updatedata(user_id, module_name, value)
                        module_name = "status"
                        value = "PREMIUM"
                        updatedata(user_id, module_name, value)
                        module_name = "plan"
                        value = "Gold Plan 4.99$"
                        updatedata(user_id, module_name, value)
                        module_name = "expiry"
                        today = str(date.today())
                        value = str(date.today()+timedelta(days=30))
                        updatedata(user_id, module_name, value)
                        updategc(gc)
                        resp = "You Have Successfully Redeemed 'Gold Plan' Using GiftCode ✅.Type /info To Know More"
                        await message.reply_text(resp, message.id)
                        await Client.send_message(grp,"redem" )
                    else:
                        ok = "NONE HAPPENNED"
                        print(ok)

                elif status == 'USED':
                    resp = "GiftCode Already Redeemed ⚠️"
                    await message.reply_text(resp, message.id)
                elif status == 'None':
                    resp = "Invalid GiftCode ❌"
                    await message.reply_text(resp, message.id)
                else:
                    resp = "Invalid GiftCode ❌"
                    await message.reply_text(resp, message.id)
    except Exception as e:
        print(e)
