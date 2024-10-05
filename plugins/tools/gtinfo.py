import time

import requests
from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()

gateways = []


# captcha
def check_captcha(gtw):
    response = requests.get(gtw).text
    if (
        "https://www.google.com/recaptcha/api" in response
        or "captcha" in response
        or "verifyRecaptchaToken" in response
        or "grecaptcha" in response
        or "www.google.com/recaptcha" in response
    ):
        return True
    else:
        return False


# cloud
def check_cloud_in_website(gtw):
    response = requests.get(gtw)
    if "cloud" in response.text.lower():
        return True
    else:
        return False


# GATEWAY
def check_credit_card_payment(gtw):
    response = requests.get(gtw)
    if "stripe" in response.text:
        return " Stripe"
    elif "Cybersource" in response.text:
        return " Cybersource"
    elif "Barintree" in response.text:
        return "Barintree"
    elif "authorize.net" in response.text:
        return " authorize"
    elif "Bluepay" in response.text:
        return "Bluepay"
    elif "Magento" in response.text:
        return "Magento"
    elif "woo" in response.text:
        return " Woo"
    elif "Shopify" in response.text:
        return "Shopify"
    elif "adyan" in response.text or "Adyen" in response.text:
        return "adyan"
    elif "Paypal" in response.text:
        return "Paypal"
    elif "suqare" in response.text:
        return " suqare"
    elif "payflow" in response.text:
        return " payflow"
    elif "payment by" in response.text:
        return True
    elif "credit card" in response.text:
        return True
    else:
        return False


gate = []


@Client.on_message(filters.command("gate"))
async def cmd_gtw(Client, message):
    try:
        # NES TOOLS
        user_id = str(message.from_user.id)
        str(message.chat.type)
        str(message.chat.id)
        regdata = fetchinfo(user_id)
        results = str(regdata)
        if results == "None":
            resp = " You Are Not Registered ⚠️. First Register By Using /register To Use Me ."
            await message.reply_text(resp, message.id)
        else:
            #
            # PLAN CHECK
            await plan_expirychk(user_id)
            # PM AND AUTH CHECK
            pm = fetchinfo(user_id)
            status = pm[2]
            role = status
            if message.reply_to_message:
                gtw = message.reply_to_message.text
            else:
                gtw = message.text[len("/gate ") :]
            if len(gtw) == 0:
                nogt = """
  Please provide link ⚠️
          """
                return await message.reply_text(nogt, message.id)
            else:
                gate = []
                chkst = "check your site wait...."
                done = await message.reply_text(chkst, message.id)
                tic = time.perf_counter()
                try:
                    c = check_captcha(gtw)
                except:
                    c = "False"
                co = check_cloud_in_website(gtw)
                py = check_credit_card_payment(gtw)
                gate.append((py))
                toc = time.perf_counter()
                result = f"""
  CHECK  SUCCESSFULLY 
┏－－－－－－－－－－－－┒
┠ Url - <code>{gtw}</code>
┠ Captcha - <code>{c}</code>
┠ Cloud - <code>{co}</code>
┠ Payment - <code>{gate}</code>
┠ Time To Chk - {toc - tic:0.4f}sec
┠ Req by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.username}</a> | [ {role} ]
┗－－－－－－－－－－－－┛
    """
                await Client.edit_message_text(message.chat.id, done.id, result)
    except Exception as e:
        print(e)
