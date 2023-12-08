from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from datetime import date
from datetime import datetime

menu = [
    [
        InlineKeyboardButton(text="Menu", callback_data="__main")
    ],
    [
        InlineKeyboardButton(text="Add Me", url="https://t.me/JoannaChkBot?startgroup"),
    ],
]

buttons = [
    [
        InlineKeyboardButton(text="Gate", callback_data="gates"),
        InlineKeyboardButton(text="Tools", callback_data="_tool"),
    ],
    [
        InlineKeyboardButton(text="Join Channel", url="https://t.me/MorPhoChat"),
        ],
    [
        InlineKeyboardButton(text="Premium", callback_data="premium_data"),
        ],
]

backbutton = [
    [
        InlineKeyboardButton(text="Gate", callback_data="gates"),
        InlineKeyboardButton(text="Tools", callback_data="_tool"),
    ],
    [
        InlineKeyboardButton(text="Premium", callback_data="premium_data"),
        ],
]

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
backtext = f"""
Welcome To Joanna Bot  |  {dt_string} 
━━━━━━━━━━━━━━━                                                                  
Hello This Is Beta Version telegram bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here.
━━━━━━━━━━━━━━━
Api Bot Status Is: OFFLINE | Joanna Api Is OFFLINE!
"""
gatebutton = [
                [
                InlineKeyboardButton("Auth", callback_data="_auth"),
                InlineKeyboardButton("Charge", callback_data="_charge"),
                ],
                [
                InlineKeyboardButton("Back",callback_data="__back"),
                ],
                ]
gatetext = """ALL GATES ARE DEAD SOON START"""

#Welcome to Joanna / Joanna Gateways Online
#━━━━━━━━━━━━━━━━━━━━━
#Gates CMDS:  None Api Gates! ✅
#━━━━━━━━━━━━━━━
#Gates auth: 1 ✅  |   Gates charge: 9 ✅
#━━━━━━━━━━━━━━━━
#Select the type of gate you want for your use!.

buttonscharge = [
                [
                InlineKeyboardButton("Back", callback_data="__gback"),
                InlineKeyboardButton("Next Page", callback_data="_chargepg2"),
                ],
                ]
buttonscharge2 = [
                [
                InlineKeyboardButton("Prev Page", callback_data="_charge"),
                InlineKeyboardButton("Next Page", callback_data="_chargepg2"),
                ],
                [
                    InlineKeyboardButton("Back", callback_data="__gback"),
                ],
                ]

mainback = """
Welcome back to Joanna Bot, it is a beta bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here
"""

@Client.on_callback_query()
async def button_click(client, query):
    data = query.data
    chat_id = query.message.chat.id
    if data == "gates":
        await query.edit_message_text(
            text=gatetext,
            reply_markup=InlineKeyboardMarkup(gatebutton),
        )
    elif data == "__main":
        await query.edit_message_text(
            f"""
Welcome To Joanna Api Bot  |  {dt_string} 
━━━━━━━━━━━━━━━                                                                  
Hello This Is Beta Version telegram bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here.
━━━━━━━━━━━━━━━
Api Bot Status Is: Online ✅ | Joanna Api Is Online!
            """,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif data == "__back":
        await query.edit_message_text(
            text=mainback,
            reply_markup=InlineKeyboardMarkup(backbutton)
        )
    elif data == "__gback":
        await query.edit_message_text(
            text=backtext,
            reply_markup=InlineKeyboardMarkup(gatebutton)
        )
    elif data == "premium_data":
        await query.edit_message_text(
            "COMING SOON",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="__back"),
                ],
                ]
            ),
        )
    elif data == "_auth":
        await query.edit_message_text(
            """
┏ Joanna Gateways Online | Auth Gateways  [P: 1 | 1] ┒
┠ Name :- Paypal Auth
┠ Format :- /pa card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- Stripe Auth
┠ Format :- /au card|month|year|cvv
┠ Condition :- OFF! | Comment: Offline API Gate!
┠ Type :- Need-Credits

┠ Name :-   Adyen
┠ Format :- /ad card|month|year|cvv
┠ Condition :- OFF! | Comment: Offline API Gate!
┠ Type :- Need-Credits

┠ Name :-BrainTree
┠ Format :- /ba card|month|year|cvv
┠ Condition :- OFF! | Comment: Offline API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="__gback"),
                ],
                ]
            ),
        )
    elif data == "_charge":
        await query.edit_message_text(
            """
┏ Joanna Gateways Online | Charge Gateways  [P: 1 | 2] ┒
┠ Name :- Stripe
┠ Amount :- $76
┠ Format :- /sb card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- Stripe
┠ Amount :- $30
┠ Format :- /sc card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- Stripe
┠ Amount :- $45
┠ Format :- /sd card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- Stripe
┠ Amount :- $100
┠ Format :- /sf card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- Stripe
┠ Amount :- $20
┠ Format :- /sg card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(buttonscharge),
        )
    elif data == "_chargepg2":
        await query.edit_message_text(
            """
┏ Joanna Gateways Online | Charge Gateways  [P: 2 | 2] ┒
┠ Name :- Stripe
┠ Amount :- $25
┠ Format :- /sh card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- Stripe
┠ Amount :- $35
┠ Format :- /si card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- Shopify Gate
┠ Amount :- $75
┠ Format :- /spa card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits

┠ Name :- Shopify Gate
┠ Amount :- $89.99
┠ Format :- /spb card|month|year|cvv
┠ Condition :- ON! ✅ | Comment: Online API Gate!
┠ Type :- Need-Credits
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(buttonscharge2),
        )
    elif data == "_tool":
        await query.edit_message_text(
            """
┏ Joanna Tools / [P: 1 | 3] ┒
┠ CC Scr:
┠ Format: $scr Username Quantity 
┠ Condition: Online! ✅

┠ IP Lookup:
┠ Format: $ip Your IP
┠ Condition: Online! ✅

┠ Checkout Parse:
┠ Format: $/cs Checkout_Link
┠ Condition: Online! ✅

┠ BIN Lookup:
┠ Format: $bin 601120 
┠ Condition: Online! ✅

┠ SK Lookup:
┠ Format: $sk SK_LIVE..... 
┠ Condition: Online! ✅

┠ CC GENERATE:
┠ Format: $gen [BIN] [QUANTITY](OPTIONAL)
┠ Condition: Online! ✅

┠ RANDOM US ADDRESS:
┠ Format: $rnd 
┠ Condition: Online! ✅

┠ GEN ADDRESS BY ZIP::
┠ Format: $zip [ZIP CODE]
┠ Condition: Online! ✅
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
            reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Back", callback_data="__back"),
                InlineKeyboardButton("Next Page", callback_data="_tool2"),
                ],
                ]
            ),
        )
    elif data == "_tool2":
       await query.edit_message_text(
            """
┏ Joanna SK Cracking Tool / [P: 2 | 3] ┒
┠ MASS SK CHK:
┠ Format: $masssk Reply To TxT File 
┠ Condition: Online! ✅

┠ GENERATE SK :
┠ Format: $gensk [QUANTITY] [SK LEN]
┠ Sk Len :- 1 - LONG SK ; 2 - MEDIUM SK ; 3 - SHORT SK
┠ Condition: Online! ✅

┠ IPV4 IPV6 GEN:
┠ Format: $ips [QUANTITY] ipv4|ipv6
┠ Condition: Online! ✅

┠ ASN IP SCR :
┠ Format: $asnip [QUANTITY] 
┠ Condition: Online! ✅

┠ GEN RANDOM IP :
┠ Format: $genip [QUANTITY]
┠ Condition: Online! ✅
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
           reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Prev Page", callback_data="_tool"),
                InlineKeyboardButton("Next Page", callback_data="_tool3"),
                ],
                [
                InlineKeyboardButton("Back", callback_data="__back"),
                ],
                ]
            ),
        )
    elif data == "_tool3":
        await query.edit_message_text(
            """
┏ Joanna SK Cracking Tool / [P: 3 | 3] ┒
┠ DEBUG SCAN :
┠ Format: $debug Reply To TxT File 
┠ Condition: Online! ✅

┠ ENV SCAN :
┠ Format: $env Reply To TxT File
┠ Condition: Online! ✅

┠ DOMAIN TO IP CON :
┠ Format: $dip Reply To TxT File
┠ Condition: Online! ✅

┠ IP RANGE :
┠ Format: $range Start_Ip - End_Ip
┠ Condition: Online! ✅

┠ IP TO DOMAIN :
┠ Format: $rev Reply To TxT File
┠ Condition: Online! ✅
┗━━━━━━━━━━━━━━━━━━━━━━━━┛
            """,
        reply_markup=InlineKeyboardMarkup(
                [
                [
                InlineKeyboardButton("Prev Page", callback_data="_tool2"),
                ],
                [
                InlineKeyboardButton("Back", callback_data="__back"),
                ],
                ]
            ),
        )
