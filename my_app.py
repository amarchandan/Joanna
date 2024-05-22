import logging

from pyrogram import Client

logging.basicConfig(level=logging.INFO)

plugins = dict(root="plugins")


bot = Client(
    "Joanna",
    api_id="24578407",
    api_hash="5f711fbe013fd0d20147f62728118510",
    bot_token="6964061507:AAHV0kOLwu51D8HWVv_yRg47H7RXZv_H6KU",
    plugins=plugins,
)

try:
    bot.run()
    print("Done Bot Active ✅")
except Exception as e:
    print(e)
