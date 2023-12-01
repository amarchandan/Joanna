from pyrogram import Client
import logging
from plugins.func.users_sql import *


logging.basicConfig(level=logging.INFO)

plugins = dict(root="plugins")


bot = Client("Joanna",
             api_id="24578407",
             api_hash="5f711fbe013fd0d20147f62728118510",
             bot_token="6669312789:AAG_d464Q2TU48Wbb_uMkMbUSPldGHIzbvM",
             plugins=plugins)

try:
    bot.run()
    print("Done Bot Active ✅")
except Exception as e:
    print(e)
