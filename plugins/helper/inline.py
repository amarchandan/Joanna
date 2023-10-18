from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from datetime import date
from datetime import datetime

buttons = [
    [
        InlineKeyboardButton(text="Gate", callback_data="gates"),
        InlineKeyboardButton(text="Tools", callback_data="_tool"),
    ],
    [
        InlineKeyboardButton(text="Group", url="https://t.me/Illegal_Carder"),
        InlineKeyboardButton(text="Channel", url="https://t.me/Illegal_Carder"),
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
Welcome To Joanna Api Bot  |  {dt_string} 
━━━━━━━━━━━━━━━                                                                  
Hello This Is Beta Version telegram bot, gateways, tools and functions are constantly being added, to know my different commands use the buttons shown here.
━━━━━━━━━━━━━━━
Api Bot Status Is: Online ✅ | Joanna Api Is Online!
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
gatetext = """
Welcome to Joanna / Joanna Gateways Online
━━━━━━━━━━━━━━━━━━━━━
Gates CMDS:  None Api Gates! ✅
━━━━━━━━━━━━━━━
Gates auth: 1 ✅  |   Gates charge: 9 ✅
━━━━━━━━━━━━━━━━
Select the type of gate you want for your use!."""

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
┏ Joanna Tools / [P: 1 | 1] ┒
━━━━━━━━━━━━
┠ Bin Generator:
┠ Format: $gen 601120  
┠ Condition: Online! ✅
 ━━━━━━━━━━━━
┠ Sk Ckeck:
┠ Format: $sk sk_live 
┠ Condition: Online! ✅
 ━━━━━━━━━━━━
┠ BIN Lookup:
┠ Format: $bin 601120 
┠ Condition: Online! ✅
 ━━━━━━━━━━━━
┠ Gen Address:
┠ Format: $dir Country_code 
┠ Condition: Online! ✅
 ━━━━━━━━━━━━
┠ IP Fraud Check:
┠ Format: $ip 1.1.1.1 
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