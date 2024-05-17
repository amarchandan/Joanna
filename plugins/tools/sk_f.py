import re
import time

import requests


async def retrieve_balance(sk):
    response = requests.get("https://api.stripe.com/v1/balance", auth=(sk, ""))
    return response.json()


async def check_status(message, sk):
    tic = time.perf_counter()  # Start the timer
    bal_dt = await retrieve_balance(sk)
    try:
        avl_bln = bal_dt["available"][0]["amount"] / 100
        pnd_bln = bal_dt["pending"][0]["amount"] / 100
        crn = bal_dt["available"][0]["currency"]
    except KeyError:
        txtx = f"""
<b>SK KEY :</b>
<code>{sk}</code>
<b>Result : </b>𝗦𝗞 𝗞𝗘𝗬 𝗥𝗘𝗩𝗢𝗞𝗘𝗗 ❌
<b>Checked By</b> ➺ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
"""
        return txtx
    data = "card[number]=4512238502012742&card[exp_month]=12&card[exp_year]=2023&card[cvc]=354"
    response = requests.get(
        "https://api.stripe.com/v1/tokens", data=data, auth=(sk, "")
    )

    repp = response.text

    if "rate_limit" in repp:
        r_text = "𝗥𝗔𝗧𝗘 𝗟𝗜𝗠𝗜𝗧 ⚠️"
        r_warning = "𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅"
    elif "tok_" in repp:
        r_text = "𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅"
        r_warning = "𝗟𝗜𝗩𝗘 𝗞𝗘𝗬 ✅"
    elif "Invalid API Key provided" in repp:
        r_text = "𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗔𝗣𝗜 𝗞𝗘𝗬 𝗣𝗥𝗢𝗩𝗜𝗗𝗘𝗗 ❌"
        r_warning = "𝗦𝗞 𝗞𝗘𝗬 𝗗𝗘𝗔𝗗 ❌"
    elif "You did not provide an API key." in repp:
        r_text = "𝗡𝗢 𝗦𝗞 𝗞𝗘𝗬 𝗣𝗥𝗢𝗩𝗜𝗗𝗘𝗗 ❌"
        r_warning = "𝗡𝗢 𝗦𝗞 𝗞𝗘𝗬 𝗣𝗥𝗢𝗩𝗜𝗗𝗘𝗗 ❌"
    elif "testmode_charges_only" in repp or "test_mode_live_card" in repp:
        r_text = "𝗧𝗘𝗦𝗧 𝗠𝗢𝗗𝗘 𝗖𝗛𝗔𝗥𝗚𝗘 𝗢𝗡𝗟𝗬 ❌"
        r_warning = "𝗦𝗞 𝗞𝗘𝗬 𝗗𝗘𝗔𝗗 ❌"
    elif "api_key_expired" in repp:
        r_text = "𝗔𝗣𝗜 𝗞𝗘𝗬 𝗘𝗫𝗣𝗜𝗥𝗘𝗗 ❌"
        r_warning = "𝗦𝗞 𝗞𝗘𝗬 𝗗𝗘𝗔𝗗 ❌"
    else:
        r_text = "𝗦𝗞 𝗞𝗘𝗬 𝗗𝗘𝗔𝗗 ❌"
        r_warning = "𝗦𝗞 𝗞𝗘𝗬 𝗗𝗘𝗔𝗗 ❌"

    toc = time.perf_counter()  # Stop the timer
    txtxtx = f"""
{r_warning}

<b>SK ➺ </b>
<b><code>{sk}</code></b>
<b>Response :</b> {r_text}
<b>Currency : {crn}</b>
<b>Available Balance : {avl_bln}$</b>
<b>Pending Balance : {pnd_bln}$</b>
<b>Time Took : <code>{toc - tic:.2f}</code> Seconds</b>

<b>Checked By</b> ➺ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
<b>Bot By</b> ➺ <code><b>ASTRONAUT UNIVERSE</b></code>
"""

    return txtxtx


async def sk1(message):
    ttt = message.text
    skm = re.search(r"sk_live_[a-zA-Z0-9]+", ttt)
    sk = skm.group(0)
    rest_in_peace = await check_status(message, sk)

    await message.answer(rest_in_peace, parse_mode="html")
