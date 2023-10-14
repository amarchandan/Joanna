import requests
from pyrogram import Client, filters
from pyrogram.types import Message
bot = ''
url = 'https://api.stripe.com/v1/token'
data = 'card[number]=4512238502012742&card[exp_month]=12&card[exp_year]=2023&card[cvc]=354'

@bot.on_message(filters.command("skc"))
async def check_stripe_key_command(client, message: Message):
    try:
        key = message.text.split(" ")[1]
        re = requests.get(url, data=data, auth=(key, ""))     
        repp = re.json()

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

        response_message = f" {r_text} \n\n {r_warning}"

        await message.reply(response_message)
    except IndexError:
        await message.reply("Invalid response from Stripe API.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")


@bot.on_message(filters.command("skb"))
async def check_stripe_key_command(client, message: Message):
    try:
        key = message.text.split(" ")[1]  # Extract the key from the command
        response = requests.get("https://api.stripe.com/v1/balance", auth=(key, ""))

        if response.status_code == 200:
            data = response.json()
            available_amount = data.get("available", [])[0].get("amount")
            pending_amount = data.get("pending", [])[0].get("amount")
            currency = data.get("available", [])[0].get("currency")

            response_message = (
                f"Available Amount: {available_amount / 100} {currency}\n"
                f"Pending Amount: {pending_amount / 100} {currency}"
            )
        else:
            response_message = (
                "Invalid response from Stripe API or unauthorized access."
            )

        await message.reply(response_message)
    except IndexError:
        await message.reply("Invalid response from Stripe API.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

#@bot.on_message(filters.command("ss"))
async def check_stripe_key_command(client, message: Message):
    try:
        key = message.text.split(" ")[1]  # Extract the key from the command
        response = requests.get('https://api.stripe.com/v1/tokens', auth=(key, ''))

        if response.status_code == 200:
            resp = response.json()
            res = resp["message"]
            response_message = f"Stripe Tokens Response:\n\n{res}"
        else:
            response_message = "Invalid response from Stripe API or unauthorized access."

        await message.reply(response_message)
    except IndexError:
        await message.reply("Invalid response from Stripe API.")
    except Exception as e:
        await message.reply(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    bot.run()