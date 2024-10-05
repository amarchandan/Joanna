import re

import requests
from bs4 import BeautifulSoup
from pyrogram import Client, filters

from plugins.func.users_sql import *


# captcha
def check_captcha(url):
    response = requests.get(url).text
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
def check_cloud_in_website(url):
    response = requests.get(url)
    if "cloud" in response.text.lower():
        return True
    else:
        return False


def check_gateway(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101"
        }
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return None
    bsoup = BeautifulSoup(response.text, "html.parser")

    payment_gateways = {
        "stripe": [
            "script",
            {"src": re.compile(r".*js\.stripe\.com.*")},
            {"src": re.compile(r".*stripe.*")},
        ],
        "paypal": [
            "script",
            {"src": re.compile(r".*paypal.*")},
            {"src": re.compile(r".*checkout\.paypal\.com.*")},
            {"src": re.compile(r".*paypalobjects.*")},
        ],
        "braintree": [
            "script",
            {"src": re.compile(r".*braintree.*")},
            {"src": re.compile(r".*braintreegateway.*")},
        ],
        "worldpay": ["script", {"src": re.compile(r".*worldpay.*")}],
        "authnet": [
            "script",
            {"src": re.compile(r".*authorizenet.*")},
            {"src": re.compile(r".*authorize\.net.*")},
        ],
        "recurly": ["script", {"src": re.compile(r".*recurly.*")}],
        "shopify": ["script", {"src": re.compile(r".*shopify.*")}],
        "square": ["script", {"src": re.compile(r".*square.*")}],
        "cybersource": ["script", {"src": re.compile(r".*cybersource.*")}],
        "adyen": ["script", {"src": re.compile(r".*adyen.*")}],
        "2checkout": ["script", {"src": re.compile(r".*2checkout.*")}],
        "authorize.net": ["script", {"src": re.compile(r".*authorize\.net.*")}],
        "worldpay": ["script", {"src": re.compile(r".*worldpay.*")}],
        "eway": ["script", {"src": re.compile(r".*eway.*")}],
        "bluepay": ["script", {"src": re.compile(r".*bluepay.*")}],
    }

    detected_gateway = None

    for pg, patterns in payment_gateways.items():
        script_elements = (
            bsoup.find_all("script", {"src": patterns[1]["src"]})
            if len(patterns) > 1
            else []
        )
        script_elements += (
            bsoup.find_all("script", {"src": patterns[2]["src"]})
            if len(patterns) > 2
            else []
        )
        script_elements += (
            bsoup.find_all("script", {"src": patterns[3]["src"]})
            if len(patterns) > 3
            else []
        )

        if (
            bsoup.find(*patterns)
            or any(script_element for script_element in script_elements)
            or bsoup.find(string=re.compile(rf".*{pg}.*", re.IGNORECASE))
        ):
            detected_gateway = pg
            break

    return detected_gateway


def add_https_if_missing(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    return url


def process_url(url):
    url = url.strip()
    url = add_https_if_missing(url)
    result = check_gateway(url)
    if result and result[1]:
        return result
    else:
        return False


@Client.on_message(filters.command(["site", "gate"]))
async def cmd_ipp(Client, message):
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
            if message.reply_to_message:
                bin = message.reply_to_message.text
            else:
                bin = message.text[len("/site ") :]
            if len(bin) == 0:
                nocc = """
GIVE VALID LINK
          """
                return await message.reply_text(nocc, message.id)
            else:
                resp = """

                """
                pm = fetchinfo(user_id)
                status = pm[2]
                role = status
                url = process_url(bin)
                co = check_cloud_in_website(bin)
                try:
                    c = check_captcha(bin)
                except:
                    c = "False"
                ok = f"""
CHECK  SUCCESSFULLY 
  
Url - <code>{bin}</code>
Captcha - <code>{c}</code>
Cloud - <code>{co}</code>
Payment - <code>{url}</code>
Req by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.username}</a> | [ {role} ]
"""
                await message.reply_text(ok, message.id)
    except Exception as e:
        print(e)
