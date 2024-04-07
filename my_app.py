from pyrogram import Client
import logging
from plugins.func.users_sql import *


logging.basicConfig(level=logging.INFO)

plugins = dict(root="plugins")


bot = Client("Joanna",
             api_id="24578407",
             api_hash="5f711fbe013fd0d20147f62728118510",
             bot_token="6327788045:AAFSvNAUlUCIMgPceFChvMLfo-edJqqJ7GM",
             plugins=plugins)

try:
    bot.run()
    print("Done Bot Active ✅")
except Exception as e:
    print(e)
