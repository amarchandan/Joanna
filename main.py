from pyrogram import Client
import logging
from plugins.func.users_sql import *


logging.basicConfig(level=logging.INFO)

plugins = dict(root="plugins")


bot = Client("Joanna",
             api_id="24578407",
             api_hash="5f711fbe013fd0d20147f62728118510",
             bot_token="6364102907:AAGCpOshrIoy4eMXUaFwpoaWtYR9ifaqj90",
             plugins=plugins)

try:
    bot.run()
    print("Done Bot Active ✅")
except Exception as e:
    print(e)




# from pyrogram import Client, compose, filters, enums
# from plugins.func.users_sql import *
# import asyncio
# import logging
# logging.basicConfig(level=logging.INFO)

# plugins = dict(root="plugins")


# bot = Client("my_bot",
#              api_id="24578407",
#              api_hash="5f711fbe013fd0d20147f62728118510",
#              bot_token="5989958877:AAFIEtR4zdKgq0CSK4PvdDcSndCQR9eQEXw",
#              plugins=plugins)


# # async def main():
# #   user = Client("scrapper",
# #                 api_id="24578407",
# #                 api_hash="5f711fbe013fd0d20147f62728118510",
# #                 session_string='BQAi8cjZI00NfCe_-Oc1mM8xG-4RzAlhUxbIwPRLcLhkNlvQWuggOArSw1QT5HwhbT5twY6xi4_3wtNwNWlnXJhvx0A8glvZKtG_CfRuhX-Fg_fgpfcmWwOpk2W6nxE9CfNqCFRnZTkasdtHMnWiL3sSRrWnPct9bBYQapvxHAnVacgUs_iCLJNJ8lZqTwCyMRDCyyILVmHXLof5s_CQvHgQLELAeiRKohLzcBE308XXD3Y4sbvjOl-lTrX8TGgR0HesQ0uFFLX29KtnUfGuCwiNL6zaqLrIRDuxr01o0EQbAA46xjxOeII4ZD5dg4YEfG2PLFipBGl3LPq57oJfDggCAAAAAYmZ2a0A')
# #   bot = Client("my_bot",
# #                api_id="24578407",
# #                api_hash="5f711fbe013fd0d20147f62728118510",
# #                bot_token="5989958877:AAFIEtR4zdKgq0CSK4PvdDcSndCQR9eQEXw",
# #                plugins=plugins)
# #   clients = [user, bot]
# #   bot.set_parse_mode(enums.ParseMode.HTML)




#   print("Done Bot Active ✅")
#   await compose(clients)
# asyncio.run(main())




# # async def main():
# #   user = Client("scrapper",
# #                 api_id="24578407",
# #                 api_hash="5f711fbe013fd0d20147f62728118510",
# #                 session_string='BQCkCakLK1Esap5Trk6rpFNdjGFj1Ad_PtGQ_TqbgY-uDopNwKyIU7mkf8-KIW_CesPmvkkEl06oDgGX0yrNPmlA3BD3ZcxCJtZK_exavW_LmRCiAyNul6oHtNXqeMkEQH6fzWBgxnNMG23lS0_FjaSvmE7ayYDEM3bUpmxyCV89sFbRbmKAhYaDGwQIBzM5wdYfbpgGf4u4mv2DMWAsjqvbWleuGwl4vZbFynbdL39zDJm0NP2D9vX05Cxd7PS8NsAk0HBWP89-kyb1XLQf114LXjxnbK0WQ1KhMfRWj07ejDxtcXCATJJ071ewQC2aqaoWVkkRYhCVtQkeT49ZDoeYAAAAAYmZ2a0A')
# #   bot = Client("my_bot",
# #                api_id="24578407",
# #                api_hash="5f711fbe013fd0d20147f62728118510",
# #                bot_token="5989958877:AAFIEtR4zdKgq0CSK4PvdDcSndCQR9eQEXw",
# #                plugins=plugins)
# #   clients = [user, bot]
# #   bot.set_parse_mode(enums.ParseMode.HTML)
# #   await compose(clients)

# #   print("Done Bot Active ✅")

# # asyncio.run(main())