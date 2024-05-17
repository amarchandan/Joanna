import time

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import os

from pyrogram import Client, filters

from plugins.func.users_sql import *

session = requests.session()
s = requests.session()


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
        return "  Bluepay"
    elif "Magento" in response.text:
        return "  Magento"
    elif "woo" in response.text:
        return " Woo"
    elif "Shopify" in response.text:
        return "  Shopify"
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


@Client.on_message(filters.command("mgtw"))
async def cmd_massskchk(Client, message):
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
            # PLAN CHECK
            await plan_expirychk(user_id)
            # PM AND AUTH CHECK
            pm = fetchinfo(user_id)
            status = pm[2]
            role = status
            if not message.reply_to_message:
                return await message.reply_text("Please Reply To File")
            if not message.reply_to_message.document:
                return await message.reply_text("Please Reply To File")
            url_lists = []
            gate = []
            tic = time.perf_counter()
            ms_ = "Checking...."
            domain_file = await message.reply_to_message.download(
                progress_args=(ms_, f"`Downloading This File!`")
            )
            with open(domain_file, "r") as file:
                domains = file.read().splitlines()
            x = len(domains)
            await message.reply_text(ms_)
            for gtw in domains:
                try:
                    c = check_captcha(gtw)
                except:
                    c = "False"
                co = check_cloud_in_website(gtw)
                py = check_credit_card_payment(gtw)
                py.append(gate)
                response = (
                    f"Url - {gtw} :- Captcha - {c} :- Cloud - {co} :- Payment - {gate}"
                )
                url_lists.append(response)
            with open(f"{x}x_Url_CHK_BY_@JoannaChkBot.txt", "a+") as f:
                f.write("\n".join(url_lists))
            toc = time.perf_counter()
            str(message.chat.id)
            resp = f"""
Url CHECKING COMPLETED ✅

┏－－－－－－－－－－－－┒
┠ Amount - <code>{x}</code>
┠ Time To Chk - {toc - tic:0.4f}sec
┠ Chk By - <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> [ {role} ]
┠ 𝘋𝘦𝘝 - <a href="tg://user?id=1418571871">̠print('⏤͟͞𝙍𝝣𝘽𝝣𝙇™ </> ⚠️') </a>
┗－－－－－－－－－－－－┛"""
            await message.reply_document(
                document=f"{x}x_Url_CHK_BY_@JoannaChkBot.txt",
                caption=resp,
                reply_to_message_id=message.id,
            )
            os.remove(f"{x}x_Url_CHK_BY_@JoannaChkBot.txt")
    except Exception as e:
        print(e)
